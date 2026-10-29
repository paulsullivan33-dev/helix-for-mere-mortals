# The Neighbours

Helix does not live on an empty street.
This chapter places it among the editors
a reader of this series is most likely
to be choosing between, and says plainly
what each neighbour does better. Two of
them have guides of their own in this
series; all of the comparisons here are
from the projects' documentation and
reputation, not from lab runs — the lab
installed Helix, and chapter 12's ledger
keeps that straight.

## Vim — the original grammar

[Vim for Mere Mortals](https://paulsullivan33-dev.github.io/vim-for-mere-mortals/)
covers the editor Helix's family
descends from. Vim's grammar is verb
first (`dw` — delete, word), its reach
is enormous (every Unix-like system has
it or its ancestor `vi`, which is why
learning it is never wasted), and its
configuration and plugin ecosystem is
thirty years deep. What Vim does not
give you out of the box is Helix's
defining comforts: a motion deletes
before it shows you its target, multiple
cursors are not a native idea, and
language-server features arrive through
plugins you choose and maintain. If you
already speak Vim fluently, Helix will
feel like a familiar language with its
sentences reversed — an hour of the
tutor buys comprehension, and your old
editor will still be there. If you
speak neither, Helix is the gentler
first language of the two, because it
shows its work.

## Neovim — the extensible modern

[Neovim for Mere Mortals](https://paulsullivan33-dev.github.io/neovim-for-mere-mortals/)
covers Vim's fork, rebuilt around
extensibility: a real plugin system, a
built-in language-server client, and a
community that has assembled, piece by
piece, roughly the feature set Helix
ships whole. The honest trade is
assembly versus arrival. A Neovim setup
can exceed Helix — there is a plugin
for nearly anything, including things
Helix cannot do at all — but it is
*yours* to assemble, configure, update
and repair, and two Neovim users'
editors are different programs in
practice. Helix is the same program for
everyone, with the modern features
decided already. Choose Neovim if the
editor is a hobby in itself, or if you
need the one capability Helix lacks;
choose Helix if the editor is a tool
you want finished.

## Kakoune — the grammar's origin

Kakoune is where selection-first
editing was invented, and Helix says so
in its own documentation. It remains a
fine, principled editor: multiple
selections are its centre, its
interaction model leans on the Unix
shell (selections pipe through external
commands), and it exposes its workings
to scripting more deeply than Helix
does. What it does not ship is Helix's
soldered-in layer — tree-sitter text
objects and language servers are
Helix's additions to the inheritance.
A reader who falls in love with this
grammar and wants its most Unix-native,
most inspectable form should know
Kakoune exists; a reader who wants the
grammar with the modern machinery
included is holding it.

## The graphical editors

The big graphical code editors — VS
Code and its relatives — remain the
default for much of the world, and for
visible reasons: a mouse-first
interface, a marketplace of extensions,
debuggers and terminals integrated into
one window. Helix's counter-offer is
not contempt; it is weight and place.
It runs in any terminal, over any SSH
connection, on any small machine, with
no installation ceremony and no account;
its language intelligence is the *same*
server protocol the graphical editors
use, so the expertise is equal even
when the furniture is plainer. Plenty
of people keep both: the graphical
editor for the project-scale tasks,
Helix for the fast, remote, keyboard
work. Nothing in this guide requires
giving either up.
