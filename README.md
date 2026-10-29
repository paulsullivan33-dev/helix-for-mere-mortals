# Helix for Mere Mortals

Most editors work the way Vim taught
them: you name an action first, then say
what it acts on — delete, then word;
change, then paragraph. **Helix** turns
that sentence around. You **select**
first, while the editor shows you exactly
what is selected, and only then do you
name the action. Select the word, *then*
delete it. Select three places at once,
*then* change them all with the same
keystrokes. It is a small inversion with
large consequences: you rarely delete
the wrong thing, because you saw the
selection before anything happened to
it.

Helix is also an editor that arrives
finished. Syntax highlighting that
understands the code's structure,
language-server features — go to
definition, rename, diagnostics, hover —
a fuzzy picker for files and themes, and
a built-in interactive tutor all ship in
the one download. There is no plugin
manager to learn and no configuration
file you must write before the editor is
useful; the project's whole pitch is
that the defaults are the product. The
price of that completeness is the flip
side of this guide's last chapters:
what is not built in is, for now, not
available at all — there is no plugin
system to add it with.

The lab behind this guide ran the real
thing: **Helix 25.07.1**, the official
release binary, on a small Linux
machine. It drove the editor the way a
reader would — keystroke by keystroke,
through a terminal, with the screens
captured as evidence — and made real
edits to real files: changed a word,
deleted and undeleted a line, walked a
selection word by word, deleted a
function's body by naming the function,
wrapped a word in parentheses, and
renamed every `apple` in a list in one
pass. Because an editor's language
features come from separate **language
server** programs, the lab also
installed one (pylsp, for Python) and
put the editor through its paces against
it: a deliberate error flagged before
anything ran, a jump to a definition, a
rename that updated the definition and
the call together. And it configured
things on purpose and by accident: a
theme that silently did not apply, and
config files broken two different ways,
to see exactly how the editor complains.

What the lab could not do, it did not
fake. Only one language server was
installed, so the other languages in
Helix's long list are health-checked
here, not exercised; their editor-side
machinery is the same machinery Python
used. Completion as you type was not
driven and is labelled documented-only
where it appears. Screen *colours* are
reported as the palette values the
terminal received, not as an aesthetic
judgement. `criteria.md` keeps the full
ledger of what was run and what was
only read.

## What this guide covers

- [**What Helix is**](what-helix-is.md) —
  the mental model: a modal editor whose
  grammar is selection, then action, and
  why the inversion matters
- [**The moving parts**](the-moving-parts.md) —
  the one binary, the runtime folder it
  carries, tree-sitter's structure
  knowledge, the language servers it
  talks to, and the config files that
  steer it
- [**Installing Helix**](installing-helix.md) —
  the release download, what is inside
  it, and the version and health checks
  that prove it runs
- [**Your first edit**](your-first-edit.md) —
  open a file, select a word, change it,
  delete a line, undelete it, save and
  quit — the whole loop in one sitting
- [**Selection first — the grammar**](selection-first.md) —
  how motions select, chunk by chunk;
  whole lines and whole files; collapsing
  a selection; and text objects that know
  what a function is
- [**Multiple cursors — editing in parallel**](multiple-cursors.md) —
  one selection per match of a pattern,
  cursors copied from line to line, and
  edits that land everywhere at once
- [**Language servers, built in**](language-servers.md) —
  what a language server adds, the health
  check that reports on each language,
  and diagnostics, hover, go-to-definition
  and rename, exercised live
- [**Configuration and themes**](configuring-helix.md) —
  the two TOML files, a strict editor
  that refuses a bad file whole, and the
  theme picker with its live preview
- [**The tutor**](the-tutor.md) —
  the interactive tutorial that ships
  inside the editor, what its thirteen
  chapters teach, and how to learn from it
- [**Recipes**](recipes.md) — rename a
  word everywhere in a file, fix a list
  in parallel, wrap every match in
  brackets, stub out a function, and hunt
  a server-reported error to its line
- [**The neighbours**](the-neighbours.md) —
  Vim and Neovim, the famous ancestors
  with the grammar the other way round;
  Kakoune, the editor Helix's grammar
  came from; and the graphical editors
- [**Limits**](limits.md) — no plugins,
  no graphical interface, language
  features only as good as the server
  you install, and a clipboard that
  needs a helper program
- [**Troubleshooting**](troubleshooting.md) —
  the "Bad config" screen, the theme that
  silently did not apply, the language
  server that is not on the PATH, the
  rename prompt that appends, and lines
  that merge when you change them
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Writing your own tree-sitter grammar or
language queries — the machinery is
described, the authoring is another
project. Building Helix from source,
including fetching and compiling
grammars yourself; the release download
ships them built. Configuring every one
of the dozens of editor options: this
guide teaches the file, the format, and
the checks, and names the handful of
settings it changes. Other platforms'
install details beyond the shape of
them — the lab's machine is Linux, and
the other downloads are labelled
documentation where they appear.

## How to use this guide

Read chapter 1 for the model and
chapter 2 before installing anything —
knowing which part holds what turns
later confusion into a named problem.
Chapter 3 installs, chapter 4 edits in
the same sitting. Chapters 5 and 6 are
the heart of it: read them slowly, with
a scratch file open, because everything
after assumes the grammar feels ordinary.
Chapter 7 needs a language server
installed to follow along live; its
health check is worth running even
without one. The lab's transcripts live
in `helix-lab/transcripts/`; its sample
files are `helix-lab/notes.txt`,
`helix-lab/fruit.txt`,
`helix-lab/numbers.txt` and
`helix-lab/sample.py`, and the script
that drove the editor is
`helix-lab/hxdrive.py`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Vim for Mere Mortals](https://paulsullivan33-dev.github.io/vim-for-mere-mortals/)
- [Neovim for Mere Mortals](https://paulsullivan33-dev.github.io/neovim-for-mere-mortals/)
- [tmux for Mere Mortals](https://paulsullivan33-dev.github.io/tmux-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/helix-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/helix-for-mere-mortals/blob/main/LICENSE-CODE).
