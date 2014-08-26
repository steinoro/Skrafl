# -*- coding: utf-8 -*-

""" Skrafltester

    Author: Vilhjalmur Thorsteinsson, 2014

    This module implements a testing function for the
    functionality in skraflmechanics.py and skraflplayer.py

"""

from skraflmechanics import Manager, State, Move
from skraflplayer import AutoPlayer

def test():

    manager = Manager()

    state = State()
    print unicode(state)

    # Test placing a simple move
    move = Move(u"þú", 0, 0)
    move.add_cover(7, 7, u"þ", u"þ")
    move.add_cover(8, 7, u"ú", u"ú")
    legal = state.check_legality(move)
    if legal != Move.LEGAL:
        print(u"Play is not legal, code {0}".format(Move.errortext(legal)))
        return
    print(u"Play {0} is legal and scores {1} points".format(unicode(move), state.score(move)))

    state.apply_move(move)

    print(unicode(state))

    move = Move(u"þessi", 0, 0)
    move.add_cover(7, 8, u"e", u"e")
    move.add_cover(7, 9, u"s", u"s")
    move.add_cover(7, 10, u"s", u"s")
    move.add_cover(7, 11, u"i", u"i")
    legal = state.check_legality(move)
    if legal != Move.LEGAL:
        print(u"Play is not legal, code {0}".format(Move.errortext(legal)))
        return
    print(u"Play {0} is legal and scores {1} points".format(unicode(move), state.score(move)))

    state.apply_move(move)

    print(unicode(state))

    move = Move(u"kexi", 0, 0)
    move.add_cover(4, 11, u"k", u"k")
    move.add_cover(5, 11, u"e", u"e")
    move.add_cover(6, 11, u"x", u"x")
    legal = state.check_legality(move)
    if legal != Move.LEGAL:
        print(u"Play is not legal, code {0}".format(Move.errortext(legal)))
        return
    print(u"Play {0} is legal and scores {1} points".format(unicode(move), state.score(move)))

    state.apply_move(move)

    print(unicode(state))

    move = Move(u"taska", 0, 0)
    move.add_cover(5, 10, u"t", u"t")
    move.add_cover(6, 10, u"a", u"a")
    move.add_cover(8, 10, u"k", u"k")
    move.add_cover(9, 10, u"a", u"a")
    legal = state.check_legality(move)
    if legal != Move.LEGAL:
        print(u"Play is not legal, code {0}".format(Move.errortext(legal)))
        return
    print(u"Play {0} is legal and scores {1} points".format(unicode(move), state.score(move)))

    state.apply_move(move)

    print(unicode(state))

    move = Move(u"ofar", 0, 0)
    move.add_cover(5, 12, u"f", u"f")
    move.add_cover(6, 12, u"?", u"a")
    move.add_cover(7, 12, u"r", u"r")
    legal = state.check_legality(move)
    if legal != Move.LEGAL:
        print(u"Play is not legal, code {0}".format(Move.errortext(legal)))
        return
    print(u"Play {0} is legal and scores {1} points".format(unicode(move), state.score(move)))

    state.apply_move(move)

    print(unicode(state))

    move = Move(u"kona", 0, 0)
    move.add_cover(4, 12, u"o", u"o")
    move.add_cover(4, 13, u"n", u"n")
    move.add_cover(4, 14, u"a", u"a")
    legal = state.check_legality(move)
    if legal != Move.LEGAL:
        print(u"Play is not legal, code {0}".format(Move.errortext(legal)))
        return
    print(u"Play {0} is legal and scores {1} points".format(unicode(move), state.score(move)))

    state.apply_move(move)

    print(unicode(state))

    # Generate a sequence of moves, switching player sides automatically

    for _ in range(4):

        apl = AutoPlayer(state)
        move = apl.generate_move()

        legal = state.check_legality(move)
        if legal != Move.LEGAL:
            # Oops: the autoplayer generated an illegal move
            print(u"Play is not legal, code {0}".format(Move.errortext(legal)))
            return
        print(u"Play {0} is legal and scores {1} points".format(unicode(move), state.score(move)))

        state.apply_move(move)

        print(unicode(state))

