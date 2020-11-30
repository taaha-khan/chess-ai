
import random
import chess

def agent(obs, config):

	board_fen = obs.board
	board = chess.Board(board_fen)

	legal_moves = list(board.legal_moves)
	random.shuffle(legal_moves)

	return legal_moves[0]