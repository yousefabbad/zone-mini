import numpy as np

pi_zones = {}
# PiZone1: 1–10000
_lo, _hi = 1, 10000
_s = np.ones(_hi+1, bool)
_s[:2] = False
for p in range(2, int(np.sqrt(_hi))+1):
    if _s[p]:
        _s[p*p::p] = False
pi_zones[(_lo, _hi)] = np.cumsum(_s.astype(int))

def get_pi(x: int) -> int:
    for (lo, hi), lookup in pi_zones.items():
        if lo <= x <= hi:
            return int(lookup[x])
    raise ValueError(f"x={x} خارج نطاقات Pi–Zone")
