# Your First Edit

**Outcome: one file, opened, changed,
saved and closed — with every step seen
before it landed.** This chapter makes
the smallest possible tour of the whole
loop: a word changed the selection-first
way, a line deleted and then forgiven
by undo, and the two commands that end
every session. The lab ran exactly this
sequence and kept the screens
(`helix-lab/transcripts/t04-first-edit.txt`);
the file is the lab's `helix-lab/notes.txt`,
three pangrams, and you can follow along
in any file of your own.

## Open, and read the screen

```bash
hx notes.txt
```

```text
    1  The quick brown fox jumps over the lazy dog.
    2  Pack my box with five dozen liquor jugs.
    3  How vexingly quick daft zebras jump!
    ~
 NOR   notes.txt          1 sel  1:1
```

Three things to notice before touching
a key. The numbers at the left are the
**gutter**: line numbers, with room
beside them where later chapters' marks
will appear. The `~` lines are simply
"no text here" — the file is three
lines; the screen is taller than the
file. And the **status line** along the
bottom reports the state of play:
`NOR` for **Normal mode** — the mode
you start in, where keys are commands —
the file's name, `1 sel` for the one
selection you always have, and `1:1`,
the position of the selection's working
end: line 1, column 1.

## Modes, in one paragraph

Helix is **modal**: the same key does
different work in different modes.
Normal mode is for moving and acting on
selections. **Insert mode** — status
line `INS` — is for typing text, and
you leave it with **Esc**. A third,
**Select mode** (`SEL`), appears in
chapter 5 for stretching selections by
hand. That is the whole scheme; every
surprise in a first session is one of
these three rooms, and the status line
always says which room you are in.

## Change a word: select, then act

The cursor is sitting on the `T` of
`The`, which makes `T` a one-character
selection. Now the grammar of chapter 1,
at walking pace:

1. Press `e`. The selection grows to the
   **end of the word**: all of `The` is
   now selected, and the status line's
   position reads `1:3` — the working
   end sits on the `e`. Nothing has been
   deleted; you are looking at a proposal.
2. Press `c` — **change**. The selected
   word is removed and you are in Insert
   mode, exactly where the word was. The
   status line says `INS`, and the file
   is marked changed: `[+]` beside its
   name.
3. Type the replacement: `A`.
4. Press **Esc**. You are back in Normal
   mode, and the line reads `A quick
   brown fox...`

Delete the selection with `d` instead
of `c` and nothing replaces it; copy it
with `y` and nothing is removed at all.
The verb always comes second, and it
always acts on precisely what you saw
selected. That is the entire trick, and
chapters 5 and 6 are variations on it.

## Delete a line, then forgive it

Move down one line with `j`, then:

1. Press `x`. The **whole line** is
   selected — line 2, end to end,
   including its ending. (Line selections
   reach through the line's newline;
   chapter 13 tells the story of what
   that does when you *change* several
   of them at once.)
2. Press `d`. The line is gone; the
   file has two lines.
3. Press `u` — **undo**. The line is
   back, as if nothing happened. (`U`
   redoes what `u` undid.)

Undo is not a courtesy in Helix, it is
load-bearing: an editor that asks you
to select before acting still lets you
select wrongly, and `u` is how the
first hour stays safe.

## Save and leave

Two commands, typed as commands — press
`:` and a command line opens at the
bottom of the screen:

- `:w` — **write** the file. The editor
  answers with a receipt:
  `'notes.txt' written, 4L 122.0B` —
  lines and bytes, so you know the write
  was real. (4 lines for a 3-line file
  counts the final newline's line; the
  lab counted too, and worried, and it
  is fine.)
- `:q` — **quit**. With unsaved changes,
  `:q` refuses and says so; `:q!` quits
  anyway and throws the changes away,
  and `:wq` writes and quits in one.

## The check

Open the file any other way — `cat
notes.txt` — and line 1 should begin
`A quick brown fox`. If it does, you
have performed the complete act of
editing, Helix-style: opened, seen a
selection, acted on it, forgiven a
deletion, saved, and left. Everything
from here is reach: bigger selections,
more of them at once, and an editor
that knows what the text means.
