# What Helix Is

You have text — code, notes, a config
file — and you want to change it *on
purpose*: exactly the words you mean,
and no others. Every editor is a theory
about how to aim those changes. The
famous theory, Vim's, is verb first:
press `d` (I am about to delete), then
`w` (a word) — and trust that the word
the editor understood is the word you
meant. When the trust is misplaced, you
find out from the damage.

**Helix is a text editor with the
sentence turned around: noun first,
then verb.** It is a **modal** editor —
it has modes, like Vim — that runs in a
terminal and is built around
**selections**. Moving the cursor
selects as it goes: press `w` and the
editor does not just step forward, it
*selects* the chunk it stepped over,
and shows you the selection, highlighted,
before anything has happened to it.
Only when the selection on screen is
the text you mean do you press the verb:
`d` to delete it, `c` to change it,
`y` to copy it. The editor's own
description of itself — *a post-modern
text editor*, printed by `hx --help` —
means exactly this: it comes after the
modern editors, and it has rearranged
their grammar.

This is worth pausing on, because it is
the reason the tool exists. The
selection-first grammar is not new —
Helix takes it from **Kakoune**, an
earlier editor built on the same idea
(chapter 11). What Helix adds is
everything around the grammar, finished
and included: **multiple cursors** as an
ordinary tool rather than a trick,
syntax highlighting that understands
the *structure* of the code (through a
system called **tree-sitter**), and the
**Language Server Protocol** — the same
machinery that powers big graphical
editors' go-to-definition, rename and
error-checking — wired in from the
start. The editor is one program,
written in Rust, downloaded as one
archive, and it asks for no plugins and
no starter configuration. Its author
calls the result "post-modern"; a
plainer description is: the Vim family's
hands, with the sentence rearranged and
the batteries not just included but
soldered in.

## A first taste

After installing (chapter 3), open a
file:

```bash
hx notes.txt
```

The cursor sits on the first character,
and that character is already a
selection — in Helix, the cursor *is* a
one-character selection. Press `e` and
the selection grows to the end of the
first word. Press `c` and the word is
gone, replaced by an insertion point:
type the new word, press Esc, and the
edit is done — seen at every step,
never guessed. Chapter 4 walks this
exact loop, and the lab's transcript
(`helix-lab/transcripts/t04-first-edit.txt`)
keeps the screens.

```text
 NOR   notes.txt          1 sel  1:3
```

That is the editor's **status line**,
and it teaches as you go: the mode
(`NOR`, normal), the file, how many
selections you hold (1), and where the
cursor's working end sits (line 1,
column 3 — the end of the word you just
selected).

## What it is not

Helix is not a word processor or a
graphical application: it lives in a
terminal, draws with characters, and
has no menus, tabs row of buttons, or
mouse-first workflow (the mouse works,
but nothing depends on it). It is not
an IDE in the project sense: it has no
build system, no debugger interface of
its own to drive your program with —
though it can talk to debug adapters
for languages that provide them — and
no project panel beyond its pickers.
It is not, yet, an extensible editor:
there is **no plugin system** in this
version, so the feature list the
download ships is the feature list,
full stop (chapter 12). And it is not
a Vim replacement you can use *as* Vim:
the keys look familiar and behave
differently — `w` selects, `d` deletes
only what is selected — and a Vim user's
first hour is mostly unlearning, which
is precisely what the built-in tutor
(chapter 9) is for.

## Who it is for

The programmer who edits in the
terminal — over SSH, inside tmux, on a
small machine — and wants the modern
language features there without a
weekend of configuration. The Vim or
Neovim user who is curious what the
grammar feels like the other way round,
and can afford an hour of being slow
again. The learner who wants one
editor whose tutorial, help and
features are all inside the tool itself.
The common thread is one person, a
keyboard, and text they want to change
with their eyes open.

## The honest catch, up front

An editor that arrives finished has
finished opinions. Helix's defaults are
good, and its configuration file is
small and strict — strict enough to
refuse the *whole file* over one bad
line, as chapter 8 demonstrates. If
your workflow needs the one feature it
lacks, there is no plugin to save you;
the answer is a different editor, and
chapter 11 names the candidates
honestly. And there is a second catch
this guide treats as a feature of the
telling: the lab drove the editor
through a captured terminal, so its
screens are reported as text and its
colours as palette values, and anything
the lab could not exercise — one
language server only, completion
undriven — is labelled as such rather
than smoothed over.
