
from chessboard import display
import chess

import stockfish_agent
import random_agent
import agent

def run(agents, show_display = True):

	board = chess.Board()
	display.start()

	player = 0

	while not display.checkForQuit():

		display.update(board.fen())

		if not board.is_game_over():

			obs = lambda: None
			obs.board = board.fen()
			obs.mark = board.turn

			config = lambda: None
			config.actTimeout = 1

			active = agents[player]
			agent_move = active(obs, config)

			board.push(agent_move)
			player = -(player - 1)

	display.terminate()

run([stockfish_agent.agent, stockfish_agent.agent])