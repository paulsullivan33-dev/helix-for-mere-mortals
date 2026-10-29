# Glossary

- **Buffer** — a file's text as the
  editor holds it; several files can be
  open as several buffers, one shown at
  a time or in splits.
- **Change** — the verb `c`: delete the
  selection and enter Insert mode in
  its place (chapter 4).
- **Collapse** — the key `;`: shrink a
  selection to a one-character cursor,
  at its working end (chapter 5).
- **Cursor** — in Helix, always a
  selection of at least one character;
  "the cursor" usually means the
  working end of the primary selection.
- **Diagnostic** — a problem a language
  server reports about a file: an error
  or a warning, with a place and a
  message (chapter 7).
- **Formatter** — an external program
  that rewrites a file in its canonical
  layout; Helix can run one per
  language, configured in
  `languages.toml`.
- **Grammar (tree-sitter)** — the
  parser for a language, shipped
  prebuilt in the runtime folder, that
  lets the editor see code's structure
  (chapter 2).
- **Gutter** — the margin at the left
  of the text: line numbers, and the
  bullets that mark diagnostics.
- **Health check** — `hx --health`, the
  built-in report on configuration,
  runtime, clipboard, and every
  language's servers and queries
  (chapters 3 and 7).
- **Hover** — `Space k`: a popup
  describing the thing under the
  cursor, supplied by the language
  server.
- **Insert mode** — the mode for typing
  text; entered by verbs like `c` and
  `i`, left with Esc. Status line `INS`.
- **Jumplist** — the editor's memory of
  where jumps took you from; Ctrl-o
  walks back, Ctrl-i forward.
- **Language server** — a separate
  program, one per language, that gives
  the editor meaning-level knowledge
  over the Language Server Protocol
  (chapter 7).
- **Leader key** — Space, in Normal
  mode: the first half of the addresses
  (`Space d`, `Space k`, `Space r`)
  that reach the language features.
- **Match mode** — the key `m`: the
  doorway to text objects, bracket
  jumping and surrounds (chapter 5).
- **Modal** — having modes: the same
  key does different work in Normal,
  Insert and Select mode, and the
  status line always says which.
- **Motion** — a key that moves the
  selection's working end — `w`, `e`,
  `b`, `f` — selecting what it crosses
  (chapter 5).
- **Multiple cursors / selections** —
  several selections held at once, all
  acted on by the same verb; the status
  line counts them as `1/3 sels`
  (chapter 6).
- **Normal mode** — the starting mode:
  keys are commands, not text. Status
  line `NOR`.
- **Picker** — a list the editor opens
  over the file — themes, diagnostics,
  files — that you filter by typing and
  confirm with Enter.
- **Primary selection** — the one of
  several that the screen follows and
  menus describe; `,` keeps only it.
- **Query (tree-sitter)** — a small
  pattern file in the runtime that says
  which parsed ranges are highlighted,
  count as text objects, or set
  indentation.
- **Regex** — a regular expression: a
  pattern describing a shape of text,
  used by the select command (`s`) to
  split a selection at every match.
- **Runtime** — the folder the binary
  carries: grammars, queries, themes
  and the tutor (chapter 2).
- **Select mode** — the mode entered
  with `v`, in which motions stretch a
  selection from a fixed anchor. Status
  line `SEL`.
- **Selection** — the unit of Helix
  editing: the highlighted text the
  next verb will act on. Always at
  least one character; always visible.
- **Surround** — a matched pair of
  characters (brackets, quotes) placed
  around a selection, or replaced, or
  removed: `ms`, `mr`, `md` in match
  mode.
- **Text object** — a named piece of
  structure — word, paragraph, function
  — selectable as a whole through match
  mode, by tree-sitter's knowledge
  (chapter 5).
- **TOML** — the plain configuration
  format of both `config.toml` and
  `languages.toml`: `key = value` lines
  under `[section]` headers.
- **True colour** — a terminal's
  ability to show millions of colours;
  Helix themes need it advertised (or
  the `true-color` setting) to apply
  (chapter 8).
- **Tutor** — the built-in interactive
  tutorial: `hx --tutor` or `:tutor`,
  48 lessons in a file you edit
  (chapter 9).
- **Verb** — a key that acts on the
  selection: `d` delete, `c` change,
  `y` copy (yank). Always second; the
  selection comes first.
- **Working end** — the end of a
  selection that motions move and the
  status line reports (`1:3`); the
  other end is the anchor.
