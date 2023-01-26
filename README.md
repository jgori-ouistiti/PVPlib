# PVPlib: A Python library to compute Positional Variance Profiles (PVP)


## Project description


This library allows you to easily compute and plot PVPs in 1, 2 and 3 dimensions.
The theory behind PVPs is explained in [1]. 

## Installing PVPlib


The library can be installed directly with pip:

```
python3 -m pip install pvplib
```

Alternatively, you can also build it using (poetry)[https://python-poetry.org/]

```
poetry install
```

## Using PVPlib


There are three versions of PVPs (PVP alpha, PVP total and PVP generalized). You can simply initialize them with

```{python}
from pvplib import PVP_alpha, PVP_total, PVP_generalized
pvp = PVP_alpha()
pvp = PVP_total()
pvp = PVP_generalized()
```
This produces a pvp object which you can populate with trajectories. For example, for a 2D trajectory with time series t, and position series x and y, where the target aimed toward is [xT, yT], you can write

```{python}
pvp.add_trajectory(t, x, y, target=[xT, yT])
```

These position series are preprocessed and projected on an orthonormal basis where the first basis vector is aligned with the origin-target direction. You can display trajectories on each projection with (2D example)

```{python}
pvp.plot_kinematic_profiles(ax=[ax0, ax1])
```

You can compute the pvp profiles with
```{python}
mean_profile, pvp_profile = pvp.compute_profiles()
```

and plot the results, together with the spline fit with 
```{python}
pvp.plot_std_profiles(ax, fit=True)
```



[1] Gori, J., & Rioul, O. (2020). A feedback information-theoretic transmission scheme (FITTS) for modeling trajectory variability in aimed movements. Biological Cybernetics, 114(6), 621-641.
