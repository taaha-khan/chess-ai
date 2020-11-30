
from stockfish import Stockfish
import random
import chess

engine = Stockfish('stockfish_12/stockfish_12_engine')

def agent(obs, config):
	timeout = config.actTimeout
	engine.set_fen_position(obs.board)
	best_move = engine.get_best_move_time(timeout * 1e3)
	return chess.Move.from_uci(best_move)