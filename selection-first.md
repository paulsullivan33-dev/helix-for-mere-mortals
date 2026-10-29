# Selection First — The Grammar

**Outcome: you can name any piece of a
file — a word, a line, a whole function —
by selecting it, and you know what the
selection holds before any verb touches
it.** Chapter 4 changed a word with `e`
and `c`. This chapter is the grammar
behind that trick, taken in order:
motions, lines, the whole file,
collapsing, and the selections that
know what code is. Every claim here was
run in the lab and kept, screens and
resulting files side by side, in
`helix-lab/transcripts/t05-selection-grammar.txt`.

## Motions select, in chunks

In Helix there is no separate "move"
and "select": a motion key moves the
selection's working end, and the text
it crosses becomes the selection. But
the unit is the **chunk**, not the
distance. Open a line of words and
press `w`:

- Once: the selection is `The ` — the
  word, *and the space after it*. The
  status line's working end reads `1:4`,
  standing on that trailing space.
- Again: the selection does **not**
  stretch from the line's start. It hops:
  now it holds ` quick ` — the next word
  with its surrounding spaces — and the
  working end reads `1:10`.

The lab proved the hop the plain way:
`w`, `w`, then `d`. If the selection had
stretched, both words would be gone.
The file afterwards begins:

```text
The brown fox jumps over the lazy dog.
```

Only the second chunk was deleted. The
lesson generalises, and it is the
tutor's own teaching order (chapter 9):
think of each motion press as *select
the next thing of this kind* — `w` the
next word-chunk, `e` to a word's end
(chapter 4's word-grab), `b` back a
chunk, `f` plus a character to select
up to and including that character.
What you see selected is what the next
verb gets: no more, no less.

Two keys adjust any selection by hand.
**`;` collapses** the selection to a
one-character cursor — at its *working
end*, which is a real choice: after `%`
(below), `;` leaves the cursor standing
on the file's last character, not its
first. And holding selections is only
half the story: **Select mode** — press
`v` — turns the grammar around, so
motions *stretch* the selection from a
fixed anchor instead of hopping chunk
to chunk. Both styles end with the same
verbs.

## Lines, files, and the whole board

Some selections are wholes:

- `x` selects the **current line**,
  end to end including its newline.
  Press it again and the selection grows
  by a line. Chapter 4 deleted one.
- `%` selects the **whole file** — one
  selection (the status line still says
  `1 sel`), working end on the last
  character. It is the front door to
  chapter 6's pattern-splitting, and on
  its own it makes `y` a copy-everything
  and `d` an act of faith in undo.
- `gg` and `G` are the travel keys —
  top of file, bottom of file; with a
  number, `8G` goes to line 8, a precision
  the lab used constantly and chapter 10
  puts to work hunting an error.

## Text objects: selections that know code

Here is where chapter 2's tree-sitter
earns its keep. A **text object** is a
named piece of structure — a word, a
paragraph, a pair of brackets, a
function — and the **match mode** key
`m` is how you ask for one. The pattern
is `m`, then `i` for *inside* (or `a`
for *around*, which includes the
delimiters), then the object's key.

The lab's experiment: the cursor sits
inside a small Python function — on its
second line, in the middle of the body.
The keys are `m`, `i`, `f`:

1. `m` enters match mode.
2. `i` says *inside*.
3. `f` says *function* — tree-sitter
   knows where the function begins and
   ends, something no counting of lines
   could tell you.

The function **body** — the docstring,
the assignment, the return — becomes
the selection, one selection, status
line `1 sel`. Then `d`, and the file
afterwards keeps the definition line
and the calls, with an empty indented
line where the body was:

```text
def greet(name):
    


print(greet("world"))
```

The same shape of keystroke selects
inside a word (`miw` is *not* needed —
plain `e` does words), inside
parentheses or quotes (the bracket and
quote keys are their own objects),
inside a paragraph of prose, or around
a whole class. And match mode carries
a second family: **surround**. Select
something, then `ms` and a character,
and the selection gains that character
as a pair around it. The lab selected a
word the walking way (`w`, then `e` —
the chunk ` quick`, with its leading
space) and pressed `ms(`:

```text
The( quick) brown fox jumps over the lazy dog.
```

The parentheses wrapped exactly the
selection, space and all — which is the
grammar's honesty again: it shows you
the chunk first, so the wrap lands
where you saw it would. (`mr` replaces
one surround with another; `md`
deletes one. All three are match-mode
verbs on a selection that must exist
first.)

## The check

On a scratch file, walk: `w` twice,
note the status line's positions, then
`d` and read the line — one chunk
should be gone, its neighbours intact.
Then `%`, `;`, and note where the
cursor lands. If both match this
chapter, the grammar is yours; chapter
6 multiplies it.
