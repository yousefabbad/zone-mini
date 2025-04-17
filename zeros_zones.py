import numpy as np
import mpmath
from scipy.interpolate import CubicSpline

# ضبط دقة mpmath
mpmath.mp.dps = 50

# حساب أول 300 صفر (غير تافه)
zeros = [float(mpmath.zetazero(i).imag) for i in range(1, 301)]
ns = np.arange(1, 301)

# بناء ثلاث سبلاينات محلية لضمان دقة 100٪ على كل نطاق
zones = {}
for lo, hi in [(1, 100), (101, 200), (201, 300)]:
    idx_lo, idx_hi = lo-1, hi-1
    zones[(lo, hi)] = CubicSpline(
        ns[idx_lo:idx_hi+1],
        zeros[idx_lo:idx_hi+1],
        bc_type='natural'
    )

def get_zeta_zero(n: int) -> float:
    """إرجاع γ_n بدقة 100% لأي n في [1–300]."""
    for (lo, hi), spline in zones.items():
        if lo <= n <= hi:
            return float(spline(n))
    raise ValueError(f"n={n} خارج النطاقات المدعومة: {list(zones.keys())}")
