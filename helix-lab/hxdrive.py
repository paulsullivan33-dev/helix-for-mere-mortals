"""Drive hx through a pty and snapshot the rendered screen with pyte."""
import os, time, pexpect, pyte

class Session:
    def __init__(self, argv, env_extra=None, cols=100, rows=30):
        env = dict(os.environ)
        env["TERM"] = "xterm-256color"
        if env_extra:
            env.update(env_extra)
        self.screen = pyte.Screen(cols, rows)
        self.stream = pyte.ByteStream(self.screen)
        self.child = pexpect.spawn(argv[0], argv[1:], env=env,
                                   dimensions=(rows, cols), timeout=20)

    def pump(self, dur=0.7):
        end = time.time() + dur
        while time.time() < end:
            try:
                data = self.child.read_nonblocking(size=65536, timeout=0.15)
                if data:
                    self.stream.feed(data)
            except (pexpect.TIMEOUT, pexpect.EOF):
                pass

    def keys(self, s, settle=0.7):
        self.child.send(s)
        self.pump(settle)

    def snap(self, out, label):
        out.write("--- screen: %s ---\n" % label)
        for line in self.screen.display:
            out.write(line.rstrip() + "\n")
        out.write("\n")

    def colors(self):
        seen = {}
        for row in self.screen.buffer.values():
            for ch in row.values():
                if ch.fg != "default":
                    seen[ch.fg] = seen.get(ch.fg, 0) + 1
        return seen

    def quit(self):
        try:
            self.child.send(":q!\r")
            self.pump(0.5)
        except Exception:
            pass
        try:
            self.child.terminate(force=True)
        except Exception:
            pass

    def selected_runs(self, max_row=12):
        """Return [(row, text)] for runs of cells with a non-default
        background in the editing area (selection + cursor)."""
        runs = []
        for r in sorted(self.screen.buffer):
            if r >= max_row:
                continue
            row = self.screen.buffer[r]
            cur, start = "", None
            for c in sorted(row):
                ch = row[c]
                if ch.bg != "default":
                    if start is None:
                        start = c
                    cur += ch.data
                else:
                    if cur:
                        runs.append((r, cur))
                        cur, start = "", None
            if cur:
                runs.append((r, cur))
        return runs
