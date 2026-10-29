# Troubleshooting

**Outcome: the failures this guide
actually met — and the ones its checks
exist to catch — each with the test
that identifies it and the move that
fixes it.** Every entry names which part
of chapter 2's map is speaking, because
in Helix the error almost always says
so, if you know where it lives.

## The editor opens with "Bad config"

*The part speaking: the config
validator.* A full-screen message
names a parse error with line, column
and a caret, and offers default
configuration on Enter. Do not just
press Enter and carry on — your whole
file is suspended until it parses
(chapter 8). Fix the named line in
`~/.config/helix/config.toml`, and
adjudicate without opening the editor:

```bash
hx --health
```

which prints `Configuration file
malformed` and the same report while
the file is bad, and the ordinary
summary once it is good.

## A setting "does nothing" — or stops startup

Same speaker, quieter case: a key the
version does not know
(`no-such-key = true` under `[editor]`)
is a startup-stopping error whose
message lists the valid fields — read
the list; the name you want is in it,
spelled the version's way. If instead
the editor starts but a setting seems
inert, check the section it sits under:
keys mean what their `[table]` says
they mean, and a right key in the wrong
table is a valid file that steers
nothing you intended. The lab's test
for "did it load" is the relative
line-number gutter of chapter 8 —
visible at a glance, impossible to fake.

## The theme does not apply

*The part speaking: the terminal, via
the theme.* You picked a theme (chapter
8) and the colours stayed default.
Read `~/.cache/helix/helix.log` for the
confession:

```text
loaded theme `gruvbox` but cannot use it because
true color support is not enabled
```

The terminal is not advertising true
colour. Either run Helix in a terminal
that does, or tell the editor to use
it anyway — `[editor] true-color = true`
— for terminals that can but do not say
so. A theme picked in the `:theme`
picker but never written to
`config.toml` also explains a theme
that vanishes next session: the picker
changes the present; the file changes
the future.

## "not found in $PATH" for a language

*The part speaking: the health table.*
`hx --health python` shows
`✘ pylsp: 'pylsp' not found in $PATH`:
the server is configured but its
program is not installed, or is
installed somewhere the PATH does not
reach. Install the server (chapter 7),
or narrow `languages.toml` to the
server you actually have. Remember the
two halves of that report: a ✘ on the
server line costs you meaning-level
features only — highlighting and text
objects are tree-sitter's, and go on
working.

## Hover shows nothing; the cursor just moves

*The part speaking: the keymap.*
Plain `k` is "move up" (chapter 4).
Hover is **Space, then `k`** — the
leader key is part of the address, and
the same holds for the rest of chapter
7's features: diagnostics are `Space
d`, rename is `Space r`. The lab's
first hover attempts politely moved
the cursor and displayed nothing at
all, which is the signature of this
mistake: the editor did exactly what
was typed.

## Rename renames too much

*The part speaking: the rename prompt.*
`Space r` opens its prompt with the
current name already typed in, as real
text. Typing your new name *appends*
to it — the lab produced `greetwelcome`
twice before reading the prompt
properly. **Ctrl-U** empties the prompt;
then type the new name alone. If a
rename instead reports a parse error
from the server (the lab met one asking
a server to rename an empty spot), the
file is unchanged and the cause is the
request, not the editor: perform
renames standing on the symbol itself.

## Changing several lines made them one line

*The part speaking: the line
selection.* A selection made with `x`
includes the line's newline, so `c`
across several such selections deletes
the newlines along with the words, and
the lines merge — the lab's exhibit is
a three-line file that became `iteme`.
The fix is order, from chapter 6:
duplicate bare cursors with `C` first,
*then* stretch each with a motion like
`e`, then change. And the mercy is
chapter 4's: `u` restores the merged
lines in one press, after which the
right order is easy to remember.

## Pickers swallow your keystrokes

*The part speaking: the picker's
filter.* In the `:theme` picker (and
every picker), typing narrows the list
by what you type — so keys meant for
the editor go to the filter instead.
That is correct behaviour: navigate
with the arrow keys or Ctrl-n/Ctrl-p,
confirm with Enter, abandon with Esc.
If a picker seems to be eating a
session, Esc returns you to the file,
unchanged.

## No highlighting anywhere

*The part speaking: the runtime.*
Plain text in every language, no text
objects, themes missing: the binary
cannot find its `runtime` folder.
`hx --health` names the directories it
searched on its *Runtime directories*
line — keep the release's `runtime`
beside the binary, or provide your own
under `~/.config/helix/runtime`
(chapters 2 and 3). The warning
`Runtime directory does not exist`
about the *personal* folder is normal
and not this fault; the fault is the
release's own folder absent from the
list.
