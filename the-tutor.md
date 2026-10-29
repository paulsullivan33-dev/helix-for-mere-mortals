# The Tutor

**Outcome: you know the editor ships
its own interactive course, how it
teaches, what its thirteen chapters
cover, and how to work through it
without wasting the effort.** Most
editors' tutorials are documents you
read beside the editor. Helix's is a
file you edit *inside* it, and this
short chapter is the guide to that
guide. Evidence:
`helix-lab/transcripts/t10-the-tutor.txt`.

## Opening it

Two doors, same room:

```bash
hx --tutor
```

or, from inside the editor, the command
`:tutor`. What opens is the release's
own tutorial file — the 50 KB `tutor`
text that lives in the runtime folder —
presented as an ordinary buffer with a
welcome screen:

```text
                 Welcome to the Helix tutorial!
        Press the j key until you reach the introduction.
```

The first instruction is a keystroke,
and that is the method throughout:
nothing in the tutor is only described.
Each short section states one idea in a
few lines, then numbers the steps to
perform it on example lines printed
right there in the file — lines with
deliberate mistakes in them, and the
corrected version shown below as the
target. You do the keys; the file on
screen either matches the target or it
doesn't. There is no separate exercise
environment to set up, and closing the
editor loses nothing: the tutor is a
fresh copy each time you open it.

## What it teaches, in order

Thirteen chapters, each closed by a
recap, roughly an evening's worth in
all:

1. **Movement, exiting, deletion,
   insert mode, saving** — chapter 4 of
   this guide, at the tutor's pace.
2. **More inserting** — appending,
   opening lines.
3. **Motions and selections** — the
   grammar of chapter 5 here, including
   the change command, counts, Select
   mode, and collapsing selections.
4. **Undo, copy and paste, searching.**
5. **Multiple cursors** — chapter 6
   here: duplication, the select
   command, regex selection, aligning,
   splitting into lines.
6. **Selecting to a character, the
   replace command, repetition.**
7. **Yank-and-replace, joining lines,
   indenting, incrementing numbers.**
8. **Registers and macros** — named
   clipboards, and keystrokes recorded
   and replayed.
9. **Searching for selections, the
   jumplist** — chapter 7's Ctrl-o home,
   plus growing a selection by search
   matches and labelled jumps.
10. **Cycling and removing selections,
    changing case, splitting
    selections.**
11. **Commenting** — whole lines and
    cursor-columns of them, one key.
12. **Match mode** — jumping between
    brackets, selecting inside and
    around, and the surrounds of
    chapter 5.
13. **Splits** — the editor's windows:
    creating them, moving between them,
    swapping and transposing them, and
    opening them from the file picker.

The file is honest about its own edge:
its last page says the tutorial is
still a work in progress, with more
sections planned. What exists is
finished, though — 48 numbered lessons
in the lab's count, every one with
something to do and a target to match.

## How to use it well

Work it *in* the editor, not beside
this guide: the tutor's entire value is
that the keys land under your fingers,
with the target text watching. Do a
chapter at a sitting; when one of its
keys names something this guide treats
later — the jumplist, registers,
splits — the tutor is the place to get
the muscle, and these chapters are the
place to get the reasons. And when a
recap says you now know a thing, test
it on a file of your own before
believing it: select a word in your
own notes, duplicate a cursor down your
own list. The tutor's pangrams are
practice dummies; the grammar is only
yours once it has drawn blood on real
text — a little, and healed by `u`.
