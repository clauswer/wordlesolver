# wordlesolver
A Pythonscript that helps solving wordls

I know, I am very late to the party.
This is just a small, fun python project for my own training purposes.

For now, you have to load a list of all the possible words as a class.
With the class-methods, you can filter the list, depending on your wordl-results:
- remove all words containing certain characters (the gray ones): `nope()`
- keep all words containing certain characters, but remove words with the character at a certain position (the yellow ones): `somewhere()`
- keep all words with characters at a certain position (the green ones): `nailedit()`

The method-names are "inspired" by the [heise nerdle](https://nerdle.pinae.net/) (here the [github repository](https://github.com/pinae/Nerdle))

# Future improvements

- show best candidate, based on the most hints the useage of this word would give
  - maybe based on levenshtein-distances between the candidates?
- insert next candidate into used wordle-page
- load results from used wordle-page
  - and thus have a fully automated solving process ;o) 
