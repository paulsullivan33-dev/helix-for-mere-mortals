# Multiple Cursors — Editing in Parallel

**Outcome: you can hold several
selections at once and edit them all
with the same keystrokes — every
occurrence of a word changed in one
pass, three lines rewritten in one
typing.** One selection is a courtesy;
several are a power tool. This chapter
builds them two ways — by pattern, and
by hand — and every step was run in the
lab (`helix-lab/transcripts/t06-multiple-cursors.txt`).

## The words for it

With more than one selection, one is
the **primary** — the status line
counts in fractions: `1/3 sels` means
three selections, the first of them
primary (the one the screen follows and
menus describe). Verbs act on *all* of
them. The crowd is managed with `,`,
which keeps only the primary selection
and dismisses the rest — chapter 9's
tutor teaches it as the way to take a
cursor back. And `C`, this chapter's
duplicator, has an upward twin: `Alt-C`
duplicates onto the line above, as `C`
does below.

## By pattern: split a selection on a regex

The lab's file is a list with a repeat
in it — `helix-lab/fruit.txt`:

```text
apple
banana
apple
cherry
apple
```

The job: every `apple` becomes `fruit`.
Three keys do the aiming:

1. `%` — select the whole file (chapter
   5's one big selection).
2. `s` — the **select** command. A
   prompt opens at the bottom of the
   screen: `select:` — it wants a
   **regular expression**, a pattern in
   the usual slashes-free form.
3. Type `apple` and press Enter.

The one big selection is replaced by
three small ones, one per match, and
the status line reads `1/3 sels`. No
search-and-replace dialog, no "replace
all? (y/n)": the matches are simply
*selected*, visibly, and the next move
is yours. That next move, here, is
chapter 4's change: `c`, type `fruit`,
Esc. The file afterwards:

```text
fruit
banana
fruit
cherry
fruit
```

Same keystrokes, three places, and the
lines between the matches were never
involved. Because the split is a regex,
the pattern can be a shape rather than
a word — a date format, a number, a
prefix — and because the result is just
selections, any verb works: `d` deletes
every match, `y` copies them all, `ms(`
would wrap each one in parentheses.

## By hand: duplicate the cursor downward

Sometimes there is no pattern; there
are just lines. The lab's second file
(`helix-lab/numbers.txt`) holds `one`,
`two`, `three`, and the job is to
rewrite all three. Put the cursor on
the first line and press `C` — **copy
selection to the next line** — twice.
The status line reads `3/3 sels`: a
cursor on each line, all in the same
column. Now the grammar applies to all
three at once: `e` selects each line's
word (three words, three different
lengths, each fully selected), and
`c`, type `item`, Esc — the file
afterwards is `item`, `item`, `item`,
each line written by the same four
keystrokes.

One caution, earned in the lab and
told properly in chapter 13: duplicate
the **cursor**, not a whole-line
selection. A line selection made with
`x` includes the line's newline, so
*changing* several of them at once
deletes the newlines too and the lines
merge into one. Start from a plain
cursor, extend with `C`, then stretch
each cursor with a motion — the order
this chapter used — and the lines stay
lines.

## When to reach for which

Pattern-split when the targets share a
*shape* — a word, a code pattern, every
date in a log — especially when you
cannot see them all on one screen.
Duplicate-by-hand when the targets are
a visible run of lines and the change
is the same on each. Both end the same
way chapter 4 did: a selection you can
see, a verb you choose, and `u` — undo
— if the crowd surprised you, because
with three selections the surprise is
three times as large and the undo is
the same one key.
