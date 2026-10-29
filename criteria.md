# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's sentences are stock sentences and pangrams.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool
   cannot do: no plugin system, terminal-only, language-server
   features only as good as the servers installed, coverage
   that varies by language, a clipboard that depends on an
   outside provider, configuration refused whole over one bad
   line, and a tutor its own last page calls unfinished.
8. **The honesty rule is in the text, early.** Helix raises no
   interception question of the kind other guides in this
   series carry, but chapter 1 and the README draw its own
   line plainly — the editor shows every selection before a
   verb acts on it, and this guide labels what it did not run
   in the same spirit — and the property the tool exists for
   (your text is changed only as you saw it selected) is
   stated before any procedure depends on it.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a shared Ubuntu Linux sandbox with no
display. Helix **25.07.1** was installed from the official
release archive `helix-25.07.1-x86_64-linux.tar.xz` and run
unmodified. The editor is interactive, so the lab drove it
through a pseudo-terminal (Python pexpect, screens rendered
with pyte at 100x30 with true colour advertised) and kept the
screens: every editing claim below is proven by a captured
screen or by the resulting file's contents, and the driver
script itself is kept at `helix-lab/hxdrive.py`. One language
server was installed for real — **pylsp** (python-lsp-server,
via pip into a lab virtual environment) — and exercised
against `helix-lab/sample.py`. All transcripts live in
`helix-lab/transcripts/` (t00-t12).

The lab had **no working system clipboard provider** (the
health check reports the `termcode` fallback) and no display,
so colours are reported as terminal palette values, never as
things seen. Everything the lab could not drive is listed as
documented-only below.

Run for real, with transcripts as evidence:

- Version and the full `--help` command list (t00); the
  release's contents counted: 245 prebuilt tree-sitter
  grammars, 174 theme files, the 50,338-byte tutor (t01).
- `--health` in full: the config/runtime/clipboard summary and
  the per-language table of 300 rows (t02); per-language
  detail for Python, Markdown and TOML, including their real
  gaps — Markdown's missing text-object queries, TOML's
  missing indent queries (t03).
- The first-edit loop: `e` selects a word, `c` changes it,
  `:w` writes with a receipt, `:q` quits; `x` selects a line,
  `d` deletes it, `u` restores it (t04).
- The selection grammar, proven by file outcomes: `w` hops
  chunk to chunk (deleting after two presses removed exactly
  " quick "), `x` takes the line with its newline, `%` the
  whole file, `;` collapses to its working end (3:37), the
  tree-sitter text object `mif` selects a function body for
  deletion, and `ms(` wraps a selection in parentheses (t05).
- Multiple cursors: `%` then `s` split the file into 3
  selections on the regex `apple`, changed to `fruit` in one
  `c`; `C` twice duplicated a cursor down a 3-line file and
  `e`/`c` rewrote all three lines; `,` keeps the primary
  selection (t06, including its postscript probe).
- Configuration: a good `config.toml` accepted and *proven
  applied* by the relative line-number gutter; a TOML syntax
  error refused at startup with a full-screen parse report;
  an unknown key refused with the valid fields listed;
  `hx --health` reporting the malformed config without
  opening the editor (t07, t08). A `languages.toml` override
  narrowing Python to one server and naming a formatter,
  confirmed in the health report (t08); pylsp's health line
  turning to a tick with its path once installed (t03
  postscript).
- Language server features against pylsp: the diagnostic
  gutter mark and status-line count for a planted undefined
  name; the `Space d` diagnostics picker (severity, source
  pyflakes, message); Enter in the picker landing the cursor
  on the offending name at 8:7 (t12); `Space k` hover showing
  signature and docstring; `gd` going to the definition and
  Ctrl-o returning; `Space r` rename changing definition and
  call together — including the prompt's prefilled name and
  the Ctrl-U that clears it (t09).
- The tutor: opened with `hx --tutor`, welcome and
  introduction screens captured, and its full contents read
  from the runtime file — 48 numbered lessons in 13 chapters,
  each with a recap, ending with its own work-in-progress
  notice (t10).
- Themes: the `:theme` picker listing themes with live
  preview, gruvbox chosen and applied at once, confirmed by
  the terminal palette (editor background #3b224c to #282828,
  status line to #504945) (t11); the true-colour refusal
  found in `helix.log` when the terminal does not advertise
  it (t07's config session).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The language-server features the lab did not drive:
  insert-mode completion, code actions, find-references, the
  symbol list, and format-on-save behaviour.
- Every language server other than pylsp (health-checked
  only), and debug adapters throughout.
- Fetching and building grammars with `hx -g fetch` /
  `hx -g build`.
- Clipboard providers beyond the termcode fallback — the
  lab's machine has no xclip, xsel or wl-copy, so copying to
  other applications could not be demonstrated.
- Keys described but not driven as exercises: Select mode's
  stretch selections, `mr`/`md` surround variants, repeated
  `x` growing a line selection, picker navigation by
  Ctrl-n/Ctrl-p, Ctrl-i forward on the jumplist, and the
  `:config-open` / `:config-reload` commands.
- Installs for macOS and Windows, distribution packages, and
  building Helix from source.
- The neighbour tools of chapter 11 (Vim, Neovim, Kakoune,
  graphical editors) — characterised, not run.
- How the editor *feels* at a human keyboard: timings,
  responsiveness, and colours as seen by an eye rather than
  read from a palette.

Fixtures are this guide's own and deliberately generic: three
pangrams, a five-line fruit list, a list of the words one,
two and three, and an eight-line Python greeting function
with one name deliberately left undefined so the language
server has something honest to find. No names, organisations
or real events.
