with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    #print(file_contents)

    wordlist = file_contents.split()

    print(f"Total words: {len(wordlist)}")

    lettercounttext = file_contents.lower()

    lettercounts = {"a": 0, "b": 0, "c" : 0,"d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "l": 0, "m": 0, "n": 0,
                    "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    lettercounts["a"] = lettercounttext.count("a")
    lettercounts["b"] = lettercounttext.count("b")
    lettercounts["c"] = lettercounttext.count("c")
    lettercounts["d"] = lettercounttext.count("d")
    lettercounts["e"] = lettercounttext.count("e")
    lettercounts["f"] = lettercounttext.count("f")
    lettercounts["g"] = lettercounttext.count("g")
    lettercounts["h"] = lettercounttext.count("h")
    lettercounts["i"] = lettercounttext.count("i")
    lettercounts["j"] = lettercounttext.count("j")
    lettercounts["k"] = lettercounttext.count("k")
    lettercounts["l"] = lettercounttext.count("l")
    lettercounts["m"] = lettercounttext.count("m")
    lettercounts["n"] = lettercounttext.count("n")
    lettercounts["o"] = lettercounttext.count("o")
    lettercounts["p"] = lettercounttext.count("p")
    lettercounts["q"] = lettercounttext.count("q")
    lettercounts["r"] = lettercounttext.count("r")
    lettercounts["s"] = lettercounttext.count("s")
    lettercounts["t"] = lettercounttext.count("t")
    lettercounts["u"] = lettercounttext.count("u")
    lettercounts["v"] = lettercounttext.count("v")
    lettercounts["w"] = lettercounttext.count("w")
    lettercounts["x"] = lettercounttext.count("x")
    lettercounts["y"] = lettercounttext.count("y")
    lettercounts["z"] = lettercounttext.count("z")

    print(lettercounts)