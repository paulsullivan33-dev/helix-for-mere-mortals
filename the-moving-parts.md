# The Moving Parts

Helix looks like one program, and at the
command line it is one program. Inside,
five parts do five different jobs, and
nearly every surprise in this guide —
including most of the troubleshooting
chapter — is one of these parts behaving
exactly as designed while the reader
expected another part's behaviour. This
chapter names them.

## The program itself

The `hx` binary is the editor: the
screen, the modes, the selections, the
keystrokes. It is written in Rust: one
program of about 19 MB, accompanied by
its **runtime folder**, which the next
section describes. (The unpacked release
is about 206 MB in all; the grammars are
most of it.) `hx` also carries
the command-line tools this guide uses
as instruments: `--version` states the
release, `--health` inspects the setup
(chapter 7), `-g` manages grammars, and
`--tutor` opens the built-in tutorial
(chapter 9). The full list is one
command away:

```bash
hx --help
```

(The lab's transcript
`helix-lab/transcripts/t00-version-and-help.txt`
keeps it.)

## The runtime: what the binary carries

Beside the binary sits a folder named
`runtime`, and it is not decoration. It
holds four things:

- `grammars/` — **245 prebuilt
  tree-sitter parsers** in the lab's
  release, one shared library per
  language, from Ada to Zig.
- `queries/` — the tree-sitter *queries*:
  small pattern files that say which
  parts of a parsed file are highlighted,
  which ranges count as text objects
  (chapter 5's function is found this
  way), and how indentation should fall.
- `themes/` — **174 theme files**, each
  a small TOML table of colours
  (chapter 8).
- `tutor` — the 50 KB text of the
  built-in tutorial (chapter 9).

The binary looks for its runtime in
set places — beside itself in the
release, or in your own config folder
(so you can override a theme or a query
without touching the release). The
health check names the directories it
found:

```text
Runtime directories: ~/.config/helix/runtime;<release>/runtime
```

(Transcript `t02-health-all.txt`.)
Delete or misplace the folder and the
editor still opens — with plain text,
no highlighting, and no text objects:
the binary and the runtime are a pair,
and chapter 3's check proves the pair
is together.

## Tree-sitter: the structure reader

**Tree-sitter** is a parser: it reads a
file of code and builds a tree of what
the code *is* — this range is a
function, that one is its argument list,
this is a comment. Because it re-parses
as you type and tolerates half-finished
code, Helix can do three things a
letter-by-letter highlighter cannot:
colour by meaning rather than by
spelling, offer **text objects** that
select a whole function or class, and
indent by structure. When chapter 7's
health table shows a ✓ for a language's
*Highlight*, *Textobjects* and *Indent*
columns, this is the part being graded.
It is also an honest dependency: a
language whose grammar or queries are
missing gets editing, but not the
structure-aware features — the health
table says which, language by language.

## The language servers: hired expertise

Tree-sitter knows what code *looks*
like; it does not know what it *means*.
Meaning — is this name defined, what
type is this, rename this symbol
everywhere it truly occurs — comes from
a **language server**: a separate
program, one per language, that Helix
starts and talks to in the Language
Server Protocol. Helix ships
*configuration* for dozens of them —
which program to run for Python, which
for Rust — but the programs themselves
are yours to install, and the editor
works, diminished, without any. The
health check again keeps the score:

```text
$ hx --health python
Configured language servers:
  ✘ ty: 'ty' not found in $PATH
  ✘ ruff: 'ruff' not found in $PATH
  ✘ jedi: 'jedi-language-server' not found in $PATH
  ✘ pylsp: 'pylsp' not found in $PATH
Tree-sitter parser: ✓
```

Four servers are *configured* for
Python in this version; the lab's
machine had none installed, so all four
show ✘ — while the parser's ✓ kept
highlighting and text objects working.
Chapter 7 installs one of the four and
puts it to work.

## The config files: strict steering

Two files steer everything, both in
`~/.config/helix/`, both in **TOML**
format:

- `config.toml` — the editor's own
  settings: theme, line numbers, cursor
  behaviour, and dozens more,
  every one optional.
- `languages.toml` — per-language
  overrides: which language server to
  run, which formatter, how to indent.

You may never need to write either —
the defaults are the product — but when
you do, the editor validates them
strictly and *as a whole*: one bad line
and the file is refused entire, with a
full-screen message naming the problem
and an offer to continue with defaults.
Chapter 8 breaks files on purpose and
reads the messages; the behaviour is
also visible without opening the editor,
in `--health`:

```text
Configuration file malformed
TOML parse error at line 1, column 17
  |
1 | theme = "gruvbox
  |                 ^
invalid basic string
```

(Transcript
`t08-health-config-and-languages.txt`.)

## Which part holds what

| Question | The part that answers it |
| --- | --- |
| Why is this keyword coloured? | Tree-sitter, via the theme |
| Why can I select the whole function? | A tree-sitter text-object query |
| Why is this name flagged as undefined? | The language server |
| Why did `gd` jump to the definition? | The language server |
| Why are line numbers relative? | `config.toml` |
| Why did the editor refuse my settings? | The config validator, at startup |
| Why is there no highlighting at all? | The runtime folder is not found |

Keep this table in mind. When Helix
surprises you, the surprise has an
address, and the address is one of
these five.
