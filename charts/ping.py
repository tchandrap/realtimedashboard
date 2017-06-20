"""
  Need to run `ping google.com >> /tmp/google.txt` in another terminal.
"""
import re
from bokeh.plotting import *
from bokeh.objects import GlyphRenderer

MAX_HISTORY = 1000
output_server("ping")

def tail_generator(filename="/tmp/google.txt", interval=0.5):
    """
    Reads file and then `tails` it -- checking at interval seconds
    Adapted from: http://code.activestate.com/recipes/157035-tail-f-in-python/
    """
    with open(filename, 'r') as f:
        while True:
            where = f.tell()
            line = f.readline()
            if not line:
                time.sleep(interval)
                f.seek(where)
            else:
                yield line

def parse_line(line):
    """Find sequence and rtt -- return as int, float or return None"""
    regex = re.compile(r'icmp_seq=(?P<seq>[0-9]+) .* time=(?P<time>[0-9.]+) ms')
    m = regex.search(line)
    if not m:
       return None
    return int(m.groupdict()["seq"]), float(m.groupdict()["time"])

x = [-1]
y = [0]
line(x,y)
#show()

renderer = [r for r in curplot().renderers if isinstance(r, GlyphRenderer)][0]
ds = renderer.data_source

f = tail_generator()
for line_ in f:
    
    data = parse_line(line_)
    if data is None:
        continue
    x.append(data[0])
    y.append(data[1])
    
    if len(x) > MAX_HISTORY:
        x = x[-MAX_HISTORY:]
    if len(y) > MAX_HISTORY:
        y = y[-MAX_HISTORY:]
    ds.data["x"] = x
    ds.data["y"] = y
   
    ds._dirty = True
    session().store_obj(ds)
time.sleep(.01)