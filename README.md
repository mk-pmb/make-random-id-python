
make-random-id-python
=====================

Generate random identifiers smartly.

  * Support multiple ID maker functions with different config.
  * Use a factory in order to process each ID maker'config only once
    (e.g. counting the number of available symbols)
    and have the generated function do as few work as possible.
  * Solves the "length vs. dupes" problem for you (see below).



Usage
-----
For both API and CLI options, please refer to [`cli.py`](cli.py).



Length vs. dupes
----------------

The problem: A random ID may turn out to be a duplicate.

  * Depending on how large you want your IDs to be,
    just retrying may become slow as the ID space fills up.
  * Without proper checking, you may even run into an infinite loop
    once the ID space is full.
  * Large amounts of quick retries will also drain your randomness pool
    quite fast, which might cause availability and/or security problems.

So how can you build your URL shortener (or whatever) in a way that it
automatically balances user experience cost of long IDs vs. your CPU cost?

There many approaches, and fortunately for you, one of them is built into
this lib and on by default. The ID maker functions have one optional
parameter `wasdupe` (default: `False`). Just pass `True` if the previous
ID was a dupe.

The IDs start with a configured minimum length, and dupes are counted.
If the dupe counter reaches the configurable limit, it is reset and the
length of future IDs is increased by one. There's also a decay that will
decrease the dupe counter if a non-dupe was generated, to protect your
user experience from short streaks of bad luck.





License
-------
ISC
