﻿# -*- coding: utf-8 -*-

""" Web server for SCRABBLE(tm) rack permutations

    Author: Vilhjalmur Thorsteinsson, 2014

    This web server module uses the Flask framework to implement
    a simple form page where the user can enter a SCRABBLE(tm) rack
    and get a list of all legal word permutations from the rack,
    as well as combinations with a single additional letter.

    The actual permutation engine is found in skraflpermuter.py

    The server is compatible with Python 2.7 and 3.x, CPython and PyPy.
    (To get it to run under PyPy 2.7.6 the author had to patch
    \pypy\lib-python\2.7\mimetypes.py to fix a bug that was not
    present in the CPython 2.7 distribution of the same file.)

    Note: SCRABBLE is a registered trademark. This software or its author
    are in no way affiliated with or endorsed by the owners or licensees
    of the SCRABBLE trademark.

"""

from flask import Flask
from flask import render_template
from flask import request

import logging
import time

import skraflpermuter


# Standard Flask initialization

app = Flask(__name__)
app.config['DEBUG'] = False


def _process_rack(rack):
    """ Process a given input rack
        Returns True if OK or False if the rack was invalid, i.e. contains invalid letters
    """
    # Create a Tabulator to process the rack
    t = skraflpermuter.Tabulator()
    t0 = time.time()

    if not t.process(rack):
        # Something was wrong with the rack
        # Show the user an error response page
        return render_template("errorword.html")

    t1 = time.time()
    # For logging, the 'latin-1' encoding seems to work on App Engine in Windows.
    # Straight Unicode or utf-8 don't work.
    logging.info(u"Processed rack \"{0}\" in {1:.2f} seconds".format(rack, t1 - t0).encode("latin-1"))

    # The rack was successfully processed and tabulated
    # Show the user a result page
    return render_template("result.html", result=t)


@app.route("/", methods=['GET', 'POST'])
def main():
    """ Handler for the main (index) page where the user enters a Scrabble rack.
    The page can be invoked via POST from itself, or by a GET, optionally with the
    rack parameter set, i.e. GET /?rack=xxx
    """
    rack = u''
    if request.method == 'POST':
        # A form POST, probably from the page itself
        try:
            # Funny string addition below ensures that the result is in
            # Unicode under both Python 2 and 3
            rack = u'' + request.form['rack']
        except:
            rack = u''
    else:
        # Presumably a GET: look at the URL parameters
        try:
            # Funny string addition below ensures that the result is in
            # Unicode under both Python 2 and 3
            rack = u'' + request.args.get('rack', '')
        except:
            rack = u''
    if rack:
        # We have something to do: process the entered rack
        # Currently we do not do anything useful with racks of more than 15 characters
        rack = rack[0:15]
        return _process_rack(rack)
    # If nothing to do, just show the main rack entry form
    return render_template("main.html")


@app.route("/help/")
def help():
    """ Show help page """
    return render_template("help.html")


# Run a default Flask web server for testing if invoked directly as a main program
if __name__ == "__main__":
    app.run(debug=True)
