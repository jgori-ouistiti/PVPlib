
Welcome to PVPlib's documentation!
==============================================

Project description
=====================

This library allows you to easily compute and plot PVPs in 1, 2 and 3 dimensions.
The theory behind PVPs is explained in [1]_ and [2]_. 

Installing PVPlib
=======================

The library can be installed directly with pip:

.. code-block:: bash
    
    python3 -m pip install pvplib


Alternatively, you can also downlaod the source and build it using `poetry <https://python-poetry.org/>`_

.. code-block:: bash

    poetry install

Using PVPlib
==============

There are three versions of PVPs (PVP alpha, PVP total and PVP generalized). You can simply initialize them with

.. code-block::

    from pvplib import PVP_alpha, PVP_total, PVP_generalized
    pvp = PVP_alpha()
    pvp = PVP_total()
    pvp = PVP_generalized()

This produces a pvp object which you can populate with trajectories. For example, for a 2D trajectory with time series t, and position series x and y, where the target aimed toward is [xT, yT], you can write

.. code-block::

    pvp.add_trajectory(t, x, y, target=[xT, yT])


These position series are preprocessed and projected on an orthonormal basis where the first basis vector is aligned with the origin-target direction. You can display trajectories on each projection with (2D example)

.. code-block::
    
    pvp.plot_kinematic_profiles(ax=[ax0, ax1])


You can compute the pvp profiles with

.. code-block::
    
    mean_profile, pvp_profile = pvp.compute_profiles()


and plot the results, together with the spline fit with 

.. code-block::
    
    pvp.plot_std_profiles(ax, fit=True)




.. [1] Gori, J., & Rioul, O. (2020). A feedback information-theoretic transmission scheme (FITTS) for modeling trajectory variability in aimed movements. Biological Cybernetics, 114(6), 621-641.

.. [2] Gori, J., and Bellut, Q. (2023, April, to appear). Positional Variance Profiles (PVPs): A New Take on the Speed-Accuracy Tradeoff. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems.

   
.. toctree::
    :maxdepth: 1
    :caption: See also

	Home page <self>
	API reference <_autosummary/pvplib>



Known Caveats
=====================

Currently, the library only handles dimensions up to 3-D. The existing code is fully compatible with any N dimension, except for a single method. However, because it is unclear why an N > 3 PVP would be useful, I haven't generalized the method yet. You can open a feature request on GitHub if you need an N-D version.


Indices
===========

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
