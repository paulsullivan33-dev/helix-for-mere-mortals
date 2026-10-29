# Language Servers, Built In

**Outcome: you can say what a language
server adds to the editor, check what
your machine has for any language, and
use the four features that matter most —
diagnostics, hover, go-to-definition,
and rename — knowing which part supplied
each.** Chapter 2 drew the line:
tree-sitter knows what code *looks*
like; a language server knows what it
*means*. This chapter crosses that line,
live: the lab installed one server and
exercised it (`helix-lab/transcripts/t09-language-server.txt`).

## The arrangement

A **language server** is a separate
program, one per language, speaking the
Language Server Protocol — the same
protocol the big graphical editors use,
which is why the same servers serve
them all. Helix ships the *wiring*: for
each language it knows which servers
exist, what their programs are called,
and how to start them. It does not ship
the servers. Install the program, put
it on your PATH, and the editor finds
it — no settings file, no enable step.
This is the "built in" of the chapter's
title: the support is built in; the
expertise is hired separately.

## The health check: the instrument

`hx --health` grades every language
(300 rows) on six things —
language server, debug adapter,
formatter, and tree-sitter's highlight,
text-object and indent queries — and
takes a language's name for the detail:

```bash
hx --health python
```

```text
Configured language servers:
  ✘ ty: 'ty' not found in $PATH
  ✘ ruff: 'ruff' not found in $PATH
  ✘ jedi: 'jedi-language-server' not found in $PATH
  ✘ pylsp: 'pylsp' not found in $PATH
Configured debug adapter: None
Configured formatter: None
Tree-sitter parser: ✓
Highlight queries: ✓
Textobject queries: ✓
Indent queries: ✓
```

Read it as two halves. The tree-sitter
half — parser and queries — ships with
the release, and its ✓ marks mean
highlighting and structural selections
work for Python *today*, server or no
server. The server half grades what you
have installed: Python has four
configured servers in this version, and
the lab's machine started with none of
them, so four ✘ marks. Other languages
grade differently — Markdown's row
shows its text-object queries missing
(✘) where Python's are present, which
is the table being honest about
coverage, not about your machine.
(Transcripts `t02-health-all.txt` and
`t03-health-per-language.txt`.) When a
language feature disappoints, this
table is the first place to look: it
splits "the editor can't" from "the
server isn't installed" from "nobody
wrote that query yet".

## One server, installed

The lab installed **pylsp** — the
Python language server — with pip, the
ordinary Python way (`pip install
python-lsp-server`; the details are
Python's ecosystem's business, and any
of the four configured servers would
have served). The health check confirms
the change of state in its own format:

```text
  ✓ pylsp: /home/hatch/workspace/helix-lab-work/venv/bin/pylsp
```

— a tick, and the path it found the
program at. From then on, opening a
Python file starts the server
automatically. The lab's file is
`helix-lab/sample.py`: a greeting
function, a call to it, and a last line
with a name, `mesage`, that is defined
nowhere — a deliberate error, planted
so the server has something to find.

## Diagnostics: errors before you run

Within moments of opening the file, the
editor marks it:

```text
●   8  print(mesage)
 NOR   sample.py            ● 1  1 sel
```

A bullet stands in the gutter beside
line 8, and the status line counts
`● 1` — one **diagnostic**, the server's
term for a reported problem. The server
found the error by *understanding* the
file: `mesage` is not a typo a speller
would catch; it is a name with no
definition, and only meaning-level
knowledge can say so.

The full account is one key away:
**Space, then `d`** opens the
diagnostics picker, which lists each
problem with its severity, its source
inside the server, and its message,
beside a preview of the file:

```text
  severity source   code message
> ERROR    pyflakes      undefined name 'mesage'
```

Press Enter on an entry and the picker
closes with your cursor standing on the
offending name itself — the lab's
cursor landed at line 8, column 7, the
`m` of `mesage` (transcript
`t12-picker-jump.txt`). Reading,
choosing, arriving: that is the whole
error-hunting loop, and it never ran
the program.

## Hover and go-to-definition

Stand on something meaningful and the
server will describe it. On the call
`greet("world")`, **Space, then `k`** —
hover — opens a small popup:

```text
greet(name)
Build a greeting for the given name.
```

The signature and the docstring: what
the function takes and what its author
said it does, without leaving the line.
(Plain `k`, without Space, is just
"move up" — the lab's first hover
attempts moved the cursor and showed
nothing, which is chapter 13's kind of
lesson: the leader key is part of the
address.)

From the same spot, **`gd`** — go to
definition — moves the cursor to the
`def greet(name):` line, landing at
1:5, the name itself. The editor keeps
a **jumplist**: **Ctrl-o** walks back
to where you jumped from, Ctrl-i
forward again. In a file of eight lines
this is a parlour trick; in a codebase
it is the difference between reading
code and searching for it.

## Rename: the meaning-level edit

Chapter 6 renamed `apple` by pattern —
every *spelling* in one file. A server
rename is a different animal: it renames
a *symbol*, the definition and every
true use, spelled howsoever. On the
`greet` definition, **Space, then `r`**
opens the prompt:

```text
rename-to:greet
```

The current name is filled in — as
real text, which the lab learned by
typing straight over it and producing
a function called `greetwelcome`. Clear
it first (**Ctrl-U** empties the
prompt), type the new name, Enter:
definition and call change together,
and the planted error on line 8 —
a different name entirely — is
untouched. Pattern edits change what
text *says*; this changes what it
*means*, and it is the clearest case
for why the server earns its install.

## What else the server brings

The same connection carries completion
as you type, a list of a file's symbols,
references (every use of the name under
the cursor) and code actions — the
server's offers to fix what it flagged.
The lab did not drive those four, and
this guide labels them documented-only
rather than pretend otherwise
(`criteria.md` keeps the ledger). The
machinery is identical — same server,
same protocol — and the health check
remains the way to prove a given
language's half of the bargain is
installed.
