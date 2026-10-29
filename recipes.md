# Recipes

**Outcome: five whole jobs, each done
with moves from earlier chapters and
nothing else.** A recipe here is a
composition, not a new feature: every
key appears in the chapter that
introduced it. Recipes 1, 2, 4 and 5
were run in the lab end to end as
written; recipe 3 composes two
separate lab runs (a pattern split,
and a surround) whose combination
follows the rule that verbs act on all
selections at once. If one surprises
you, the chapters are the explanation
and `u` is the exit.

## Rename a word in the whole file

*Chapters 5 and 6.* You have used a
wrong name eleven times in one file
and the right name in none. (For a
name whose *meaning* matters — a
variable, a function — prefer the
server rename of chapter 7; this recipe
is for text: labels, headings, words.)

1. `%` — select the whole file.
2. `s`, type the word, Enter — one
   selection per occurrence.
3. `c`, type the new word, Esc.
4. `:w`.

The lab's version turned three lines
of `apple` into three of `fruit`
(`helix-lab/transcripts/t06-multiple-cursors.txt`);
the pattern can be a regular
expression, so punctuation and spacing
around the word are yours to include
or exclude deliberately.

## Fix a list so every line matches

*Chapter 6.* Three lines each hold a
different word and all should hold the
same one — a packing list, a rota, a
set of repeated labels.

1. Cursor on the first line.
2. `C` once per further line — a cursor
   on each, same column (`3/3 sels` for
   three).
3. `e` — each cursor selects its own
   line's word, whatever its length.
4. `c`, type the word, Esc.

Remember the order — duplicate first,
*then* extend. Starting from whole-line
selections (`x`) and changing them
together eats the newlines and merges
the lines; chapter 13 has the lab's
exhibit.

## Wrap every match in brackets

*Chapters 5 and 6.* Every occurrence of
a term should gain parentheses — terms
in a glossary, codes in a table.

1. `%`, then `s`, type the term, Enter —
   every match selected.
2. `ms(` — match-mode surround, open
   bracket: each selection gains the
   pair around it.

The lab wrapped a single selected word
this way (`The( quick) brown...`,
transcript `t05`); the same two keys
after a split act on every match at
once, because surround is a verb and
verbs act on all selections.

## Empty out a function, keep its shape

*Chapter 5.* A function needs rewriting
from the inside: signature and callers
stay, body goes.

1. Cursor anywhere inside the function.
2. `mif` — match, inside, function: the
   whole body is one selection.
3. `d` — delete. The definition line
   remains, with an empty indented body
   line beneath it.
4. `i` to enter Insert mode there, and
   type the new body at your leisure.

Tree-sitter found the boundaries, so
this works the same in a three-line
helper and a sixty-line monster, and in
any language whose queries the health
table ticks.

## Walk the errors, one by one

*Chapter 7.* A file the language server
has opinions about, and you want them
in order, at the scene of each.

1. `Space d` — the diagnostics picker.
2. Read the list: severity, source,
   message. (The lab's read: `ERROR
   pyflakes — undefined name 'mesage'`.)
3. Enter on the first entry — you are
   standing on the offending name.
4. Fix it — `e` to select a mistyped
   word, `c` to retype it, or `Space r`
   if it is a symbol to rename properly.
5. Repeat from step 1; the picker
   re-reads the server's current
   account each time it opens.

No build ran, no test ran; the server
did the reading. When the picker is
empty, the file is — by the server's
lights, which are meaning-level lights —
clean.
