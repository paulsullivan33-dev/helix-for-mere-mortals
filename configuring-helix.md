# Configuration and Themes

**Outcome: you can steer the editor
with two small files, you know exactly
how it reacts to a mistake in them —
because this chapter makes the mistakes
on purpose — and you can change its
colours live and check the change
landed.** Helix needs no configuration
to be itself; everything here is
optional, which is why the chapter can
afford to be mostly about the edges.
The evidence is in
`helix-lab/transcripts/t07-config-files.txt`,
`t08-health-config-and-languages.txt`
and `t11-themes.txt`.

## The two files

Both live in `~/.config/helix/` and
both are TOML — the plain
`key = value` format with `[section]`
headers that much of the Rust and
Python world uses:

- `config.toml` steers the editor:
  theme, line numbers, cursor shapes,
  and dozens more settings, every one
  optional.
- `languages.toml` steers languages:
  per-language overrides of which
  language server runs, which formatter,
  and how indentation falls.

From inside the editor, `:config-open`
opens the first and `:config-open-language`
the second, and `:config-reload` takes
effect of your changes without a
restart; `hx` also accepts `-c FILE`
to start with a different config file
entirely. None of that was needed to
write this chapter's config, which is
four lines.

## A good config, and visible proof

The lab's working example:

```toml
theme = "gruvbox"

[editor]
line-number = "relative"
cursorline = true
```

`line-number = "relative"` is the
setting to request if you want proof a
config was *applied* and not merely
accepted: with the cursor on line 3,
the gutter stops reciting 1, 2, 3 and
instead shows each line's **distance
from the cursor** — 2, 1, and the
cursor line's own absolute number, 3:

```text
    2  The quick brown fox jumps over the lazy dog.
    1  Pack my box with five dozen liquor jugs.
    3  How vexingly quick daft zebras jump!
```

Motions in chapter 5 are counted in
lines, so a gutter that counts
distances is genuinely useful — and as
a test it is unambiguous: either the
numbers changed or the config did not
load. The log file
(`~/.cache/helix/helix.log`) stays
silent about a good config. It had one
thing to say about this session, which
is the themes section's business below.

## A bad config, refused whole

Now break it — the classic way, an
unterminated string:

```toml
theme = "gruvbox
```

Start the editor, and it does not start.
Instead, a full-screen message:

```text
Bad config: TOML parse error at line 1, column 17
  |
1 | theme = "gruvbox
  |                 ^
invalid basic string
Press <ENTER> to continue with default config
```

Line, column, a caret under the fault,
and the consequence in plain words:
press Enter and the editor runs with
**default** configuration — not with
the good half of your file. The refusal
is all-or-nothing, by design: a
half-applied configuration is a bug
report waiting to be misfiled.

A subtler fault gets the same
treatment. Give `[editor]` a key that
does not exist (`no-such-key = true`)
and startup stops again: the message
names the unknown field and then —
thoughtfully, enormously — lists *every
field that does exist*, so the message
doubles as the index of what you may
set. A value of the wrong type is
likewise refused. Nothing about a bad
config is silent, at the terminal or
away from it: `hx --health` prints the
same parse report without opening the
editor (transcript `t08`), which makes
it the check to run after any config
edit you are unsure of — before your
next real session depends on it.

## languages.toml, proven from outside

The language file is just as checkable
without opening anything. The lab's
example narrows Python to one server
and names a formatter:

```toml
[[language]]
name = "python"
formatter = { command = "cat" }
language-servers = ["pylsp"]
```

`hx --health python` then shows only
pylsp among the servers — the other
three configured names are gone from
the report, replaced by the reader's
choice — and the formatter line turns
to a tick with the found path:
`✓ /usr/bin/cat`. (`cat` is a stand-in,
a formatter that formats nothing; it
proves the plumbing, which was the
point.) This is the file where a
machine's real preferences live: the
server you actually installed, the
formatter your project uses, the
indent your codebase expects.

## Themes: picked live, checked by palette

A theme is one name in `config.toml`
— or no file at all: type `:theme`
and a space inside the editor and a
**picker** opens listing the themes by
name, 174 of them shipped in the
release's runtime (acme, ayu_dark, the
base16 family, catppuccin in four
flavours...). Moving through the list
redraws the editor behind it in each
theme as you pass — the preview is the
editor itself — and Enter keeps the
one you stopped on. The lab switched
to `gruvbox` this way and confirmed the
switch by the terminal's own palette:
the screen's background colour changed
from the default theme's deep purple
(`#3b224c`) to gruvbox's brown-black
(`#282828`), status line included
(transcript `t11-themes.txt`).

One condition, learned from the log:
a theme only applies if the terminal
can show its colours. Helix works in
**true colour** — millions of shades —
and if the terminal does not advertise
that ability, the chosen theme is
quietly *not* used and the fact is
written to `helix.log`:

```text
loaded theme `gruvbox` but cannot use it because
true color support is not enabled
```

The `[editor]` table has a `true-color`
setting for terminals that can but do
not say so. If a theme ever seems to
ignore you, that log line is the whole
diagnosis; chapter 13 collects it.
