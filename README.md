A word-ladder puzzle solver.  You can replace the dict.txt file with your own dictionary of
words.

Examples:

    $ ./ladder.py todd john
    TODD (3)
    TOAD (3)
    LOAD (3)
    LOAN (2)
    JOAN (1)
    JOHN (0)

    $ ./ladder.py geek wire
    GEEK (4)
    WEEK (3)
    WEED (3)
    WELD (3)
    WILD (2)
    WILE (1)
    WIRE (0)

    $ ./test.sh
    test_foobar (test_ladder.TestLadder) ... ok
    test_mismatch (test_ladder.TestLadder) ... ok
    test_not_in_dict (test_ladder.TestLadder) ... Warning: --- is not in dictionary.
    ok
    hamming (ladder)
    Doctest: ladder.hamming ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.081s

    OK
