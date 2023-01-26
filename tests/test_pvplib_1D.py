import matplotlib.pyplot as plt
import sys
import copy

sys.path.append("/home/juliengori/Documents/VC/pvplib/pvplib")

from pvplib import PVP_alpha, PVP_total, PVP_generalized, __version__


def test_version():
    assert __version__ == "0.3.0-dev0"


TEST_DATA_PATH = "tests/sample_data_PPD.csv"
D = 212
xT = D / 2 / 1000

SHOW = False


def PVP_1D_add_trajectory():
    global pvp
    with open(TEST_DATA_PATH, "r") as _file:
        for nl, _line in enumerate(_file):
            if nl == 0:
                continue
            if "Movement" in _line:
                try:
                    if (
                        x[0] > 0
                    ):  # use both left-to-right and right-to-left movements without changing origin, hack for the PDdataset
                        x = [-_x for _x in x]
                    pvp.add_trajectory(
                        t, x, target=[xT], extend_to=3, correct_start=False
                    )
                except NameError:  # t,x,y have not been defined yet
                    pass
                t = []
                x = []
                y = []
                continue
            _t, _x = _line.split(";")[:2]
            t.append(float(_t))
            x.append(float(_x))


def PVP_1D_compute_profiles():
    global pvp
    pvp.compute_profiles()


def PVP_1D_plots():
    global pvp
    fig, axs = plt.subplots(1, 2)
    pvp.plot_kinematic_profiles([axs[0]])
    pvp.plot_std_profiles(axs[1], fit=False)
    if SHOW:
        plt.show()
    plt.close()


def PVP_1D_remove_outliers():

    global pvp
    pvp_copy = copy.deepcopy(pvp)
    fig, axs = plt.subplots(2, 2)
    pvp_copy.plot_kinematic_profiles([axs[0, 0]])
    pvp_copy.plot_std_profiles(axs[1, 0], fit=False)
    pvp_copy._remove_outliers(remove_outliers_k_sigma_away=3.5)
    pvp_copy.plot_kinematic_profiles([axs[0, 1]])
    pvp_copy.plot_std_profiles(axs[1, 0], fit=False)
    plt.tight_layout()
    if SHOW:
        plt.show()
    plt.close()


def PVP_1D_compute_pvp():
    global pvp
    std_prof, fit_x, fit_y, kinematic_profiles = pvp.compute_pvp(
        remove_outliers_k_sigma_away=3.5
    )
    fig, axs = plt.subplots(1, 2)
    pvp.plot_kinematic_profiles([axs[0]])
    pvp.plot_std_profiles(axs[1], fit=False)
    if SHOW:
        plt.show()
    plt.close()


def PVP_1D_plots_with_fits():
    global pvp
    std_prof, fit_x, fit_y, kinematic_profiles = pvp.compute_pvp(
        remove_outliers_k_sigma_away=3.5
    )
    fig, axs = plt.subplots(1, 2)
    pvp.plot_kinematic_profiles([axs[0]])
    pvp.plot_std_profiles(axs[1], fit=True)
    if SHOW:
        plt.show()
    plt.close()


def PVP_1D_print():
    global pvp
    print(pvp)


def test_PVP_1D_alpha():
    global pvp
    pvp = PVP_alpha()
    PVP_1D_add_trajectory()
    PVP_1D_compute_profiles()
    PVP_1D_plots()
    PVP_1D_remove_outliers()
    PVP_1D_compute_pvp()
    PVP_1D_plots_with_fits()
    PVP_1D_print()


def test_PVP_1D_total():
    global pvp
    pvp = PVP_total()
    PVP_1D_add_trajectory()
    PVP_1D_compute_profiles()
    PVP_1D_plots()
    PVP_1D_remove_outliers()
    PVP_1D_compute_pvp()
    PVP_1D_plots_with_fits()
    PVP_1D_print()


def test_PVP_1D_generalized():
    global pvp
    pvp = PVP_generalized()
    PVP_1D_add_trajectory()
    PVP_1D_compute_profiles()
    PVP_1D_plots()
    PVP_1D_remove_outliers()
    PVP_1D_compute_pvp()
    PVP_1D_plots_with_fits()
    PVP_1D_print()


def PVP_1D():
    test_PVP_1D_alpha()
    test_PVP_1D_total()
    test_PVP_1D_generalized()


if __name__ == "__main__":
    PVP_1D()
