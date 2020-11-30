
import random
import chess
import time

def heuristic(board, fen = None):
	if board.is_variant_win():
		return 100
	if board.is_variant_loss():
		return -100
	return 0

def sort_moves(board, moves):

	def score_move(move):
		return random.random()
	
	sorted_moves = sorted(moves, key = score_move, reverse = True)
	return sorted_moves

def negamax(board, depth, alpha, beta, color):
	
	if depth == 0 or board.is_game_over():
		return (None, color * heuristic(board.copy(), board.fen()))

	next_moves = list(board.legal_moves)
	sorted_moves = sort_moves(board, next_moves)

	value = float('-inf')
	for move in sorted_moves:
		
		next_board = board.copy()
		next_board.push(move)
		evaluation = -negamax(next_board, depth - 1, -beta, -alpha, -color)[1]

		if evaluation > value:
			value = evaluation
			main_move = move
		
		alpha = max(alpha, evaluation)
		if alpha >= beta: break
	
	return (main_move, value)

def agent(obs, config):

	start_time = time.time()

	board_fen = obs.board
	mark = obs.mark

	buffer = config.actTimeout / 10
	timeout = config.actTimeout - buffer

	board = chess.Board(board_fen)

	inf = float('inf')
	(move, score) = negamax(board, 4, -inf, inf, 1)
	return move