# Installing Helix

**Outcome: an `hx` program that runs on
your machine, states its version, and
can prove — before you edit anything —
that it found its runtime and knows
what your setup is missing.** Helix is
a program plus a folder of parts it
carries (chapter 2); this chapter
installs both and checks the pair is
together.

## The release download

The lab installed Helix **25.07.1** from
the project's GitHub releases
(`github.com/helix-editor/helix`). There
is one archive per platform —
`helix-25.07.1-x86_64-linux.tar.xz` for
ordinary 64-bit Linux PCs, a matching
`aarch64-linux` build for ARM machines,
and builds for macOS and Windows beside
them (those two are documented here,
not lab-run: the lab's machine is
Linux). Many Linux distributions also
package Helix, and the project documents
building from source; the release
archive is the route this guide
verifies, because it is self-contained
and identical everywhere.

Unpacked, the archive is one folder:

```text
helix-25.07.1-x86_64-linux/
  hx                    the program
  runtime/              grammars, queries, themes, the tutor
  contrib/              shell completions and the like
  LICENSE, README.md
```

Nothing is installed into the system:
no package manager and no administrator
rights are needed to unpack it, and
deleting the folder removes Helix
completely. Put the `hx` program
somewhere on your PATH — or don't, and
call it by its full path; what matters
is that the `runtime` folder stays
within reach of the binary, since that
is the first place the binary looks for
it.

## The checks

```bash
hx --version
```

```text
helix 25.07.1 (a05c151b)
```

That is the program introducing itself
(the trailing code is the exact build).
Second, prove the runtime was found.
The head of the full health report is
the summary of the whole setup:

```bash
hx --health
```

```text
Config file: default
Language file: default
Log file: ~/.cache/helix/helix.log
Runtime directories: ~/.config/helix/runtime;<release>/runtime
Runtime directory does not exist: ~/.config/helix/runtime
System clipboard provider: termcode
```

Four facts to read off these lines.
*Config file: default* says you have no
`config.toml` yet — expected, and fine.
The *Runtime directories* line names
where the editor looked; the release's
own `runtime` must be among them, or
highlighting, themes and text objects
will be silently absent. The warning
under it is also normal: your *personal*
runtime folder (for overrides, chapter
2) does not exist until you create it.
And the clipboard line names the helper
the editor will use for the system
clipboard — `termcode` here, a fallback
that works inside some terminals; on a
desktop it will usually name a real
provider (chapter 12 returns to this).
Asked for the clipboard alone
(`hx --health clipboard`), the report
is just that one provider line.

The full health table — one row per
language, 300 of them — is
chapter 7's instrument; for now, the
clipboard category is the acceptance
test. Both checks, with the release's
contents listed file by file, are kept
in the lab's transcripts
`t00-version-and-help.txt`,
`t01-runtime-contents.txt` and
`t02-health-all.txt`.

## The shape of a session

Files open by name, and a name can
carry a position:

```bash
hx notes.txt          one file
hx a.txt b.txt        several files, one per buffer
hx notes.txt:12       at line 12
hx notes.txt:12:4     at line 12, column 4
```

Nothing about the install decides where
your files live, where your config goes
(`~/.config/helix/`, chapter 8), or
which language servers exist (chapter
7) — the install is only the editor and
its runtime, and it is deliberately the
smallest chapter in this guide. That is
the product working as designed.
