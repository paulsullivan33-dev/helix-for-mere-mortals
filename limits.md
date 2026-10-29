# Limits

**Outcome: you know, before Helix can
surprise you with any of them, the
walls of the tool — what it cannot do,
what it does only as well as its
helpers, and what its strictness costs.**
Every item here was met in the lab or
read off the tool's own reports; none
is a complaint. A finished editor's
limits are part of its shape.

## There is no plugin system

The feature list the download ships is
the feature list. There are no plugins,
no extensions, no scripting the editor
itself in this version — the project
speaks of adding extensibility in the
future, and future tense is where it
lives. If your workflow depends on an
editor behaviour Helix does not have —
a particular integration, a specialised
view, a custom command of your own
devising — there is no way to bolt it
on, and chapter 11's neighbours are
the honest answer. What configuration
exists (chapter 8) is settings, not
programming.

## It is a terminal editor

Helix draws with terminal characters
and thinks in keystrokes. There is no
graphical window of its own, no menu
bar, no minimap, and while the mouse
can click and select, nothing about the
design needs it. Its colours are the
terminal's colours — which is also why
themes depend on the terminal's true
colour support (chapter 8). Readers
who want a windowed application are
not being served a lesser one here;
they are being served a different kind
of thing.

## The language server is only as good as the server

Chapter 7's features — diagnostics,
rename, hover — are supplied by
whichever server a language has and you
have installed. Four servers are
*configured* for Python alone, and they
differ; a language with no server
installed gets none of it, and a
language with a weak server gets a weak
version. The editor's side of the
bargain is the wiring and the health
table; the expertise belongs to the
servers, and so does their quality.

## Coverage is per language, and uneven

Tree-sitter's gifts depend on each
language's grammar and query files, and
the health table grades them separately
because they genuinely differ: in the
lab's table, some languages lack
text-object queries (Markdown is one)
and some lack indent queries (TOML is
one), so `mif` in one language may have
no counterpart in another. The table,
not the marketing, is the coverage map:
`hx --health <language>` before you
rely on a structural feature in a new
language.

## The clipboard needs a provider

Helix does not own the system
clipboard; it asks a helper program —
`xclip` or `xsel` on X11, `wl-copy` on
Wayland, and their equivalents
elsewhere — and on a machine with none
of them it falls back to `termcode`,
which works only inside terminals that
support it. The lab's machine reported
exactly that fallback, which means
copying *out* of the editor to other
applications was the one ordinary act
this guide could not demonstrate on
that machine. `hx --health clipboard`
names your provider; on a desktop it
will usually name a real one.

## Strictness cuts both ways

Chapter 8's all-or-nothing config is a
design choice with a price: one typo
and *every* preference is suspended
until the file parses — relative line
numbers, theme, all of it — and a
setting the version does not know is a
startup-stopping error, not a warning.
The messages are excellent and the
health check adjudicates without
opening the editor, but the reader
should know the bargain: Helix would
rather refuse your file entirely than
guess which half of it you meant.

## The tutor is unfinished

By its own last page, the built-in
tutorial is a work in progress with
more sections planned. Its 48 lessons
are complete as far as they go — they
cover the whole core grammar — but
some corners of the editor (the
language-server keys among them) have
no lessons yet. Relatedly, the editor
is comparatively young: its author
calls it post-modern, and its version
number at this writing is 25.07.1 — a
date-based version (year, month,
release) — and it has a smaller
community than Vim's thirty years have
gathered.
Questions are answered, but the answer
archive is shallower.

## And the honest boundary of this guide

The lab ran one language server
(pylsp), on one platform (Linux), in a
terminal it drove by program. Chapters
7's undriven features, other platforms'
installs, and every comparison in
chapter 11 are documentation, labelled
as such in `criteria.md`. Helix's real
limits are above; this paragraph is
the guide's.
