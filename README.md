# IMDB-Top-Movies-Scraper

This repository allows you to scrape data from IMDb's top 250 list of movies.

The Python Script (`main.py`) has a function called `scrape(i:int, includeYear:bool)` where `i` is the total amount of movies to return (inclusive and `1 <= i <= 250`), and `includeYear` determines whether or not to include the year of the movie.

Example:

```python

scrape(10, True)

>>> ['The Shawshank Redemption (1994)', 'The Godfather (1972)', 'The Dark Knight (2008)', 'The Godfather Part II (1974)', '12 Angry Men (1957)', "Schindler's List (1993)", 'The Lord of the Rings: The Return of the King (2003)', 'Pulp Fiction (1994)', 'The Lord of the Rings: The Fellowship of the Ring (2001)', 'Il buono, il brutto, il cattivo (1966)']

```

## How to Format the Movies and Make Them "Pretty"?

To convert the movies to a readable string, you can use the `.join()` method:

```python

x = scrape(10, True)

# Join each item of `x` on a newline:
"\n".join(x)

>>> The Shawshank Redemption (1994)
>>> The Godfather (1972)
>>> The Dark Knight (2008)
>>> The Godfather Part II (1974)
>>> 12 Angry Men (1957)
>>> Schindler's List (1993)
>>> The Lord of the Rings: The Return of the King (2003)
>>> Pulp Fiction (1994)
>>> The Lord of the Rings: The Fellowship of the Ring (2001)
>>> Il buono, il brutto, il cattivo (1966)

```
