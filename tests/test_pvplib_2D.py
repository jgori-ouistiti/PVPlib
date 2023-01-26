import matplotlib.pyplot as plt
import sys
import copy
import json

sys.path.append("/home/juliengori/Documents/VC/pvplib/pvplib")

from pvplib import PVP_alpha, PVP_total, PVP_generalized, __version__


def test_version():
    assert __version__ == "0.3.0-dev0"


TEST_DATA_PATH = "tests/23714_fusion.json"
# pix to mm
DISTANCE_CONVERSION_CONDITIONS = 9.5 / 100

SHOW = False


def PVP_2D_add_trajectory():
    global pvp

    with open(TEST_DATA_PATH, "r") as _file:
        data = json.load(_file)
        trials = data["experiments"]["9"]["trials"]
        k = 0
        for key, value in trials.items():
            xT, yT = [v * DISTANCE_CONVERSION_CONDITIONS for v in value["pos_target"]]
            trajectories = value["mouse_tracks"]
            t, x, y = [], [], []
            for n, (_x, _y) in enumerate(trajectories):
                t.append(n * 0.01)
                x.append(float(_x) * DISTANCE_CONVERSION_CONDITIONS)
                y.append(float(_y) * DISTANCE_CONVERSION_CONDITIONS)

            if k == 1:
                # exit()
                pass
            pvp.add_trajectory(
                t, x, y, target=[xT, yT], extend_to=3, correct_start=True
            )
            k += 1


def PVP_2D_compute_profiles():
    global pvp
    pvp.compute_profiles()


def PVP_2D_plots():
    global pvp
    fig, axs = plt.subplots(2, 2)
    pvp.plot_kinematic_profiles(ax=[axs[0, 0], axs[0, 1]])
    # pvp.plot_std_profiles(axs[1, 0], fit=False)
    if SHOW:
        plt.show()
    plt.close()


def PVP_2D_remove_outliers():

    global pvp
    pvp_copy = copy.deepcopy(pvp)
    fig, axs = plt.subplots(3, 2)
    pvp_copy.plot_kinematic_profiles(ax=[axs[0, 0], axs[0, 1]])
    pvp_copy.plot_std_profiles(axs[1, 0], fit=False)
    pvp_copy._remove_outliers(remove_outliers_k_sigma_away=3.5)
    pvp_copy.plot_kinematic_profiles(ax=[axs[2, 0], axs[2, 1]])
    pvp_copy.plot_std_profiles(axs[1, 1], fit=False)
    plt.tight_layout()
    if SHOW:
        plt.show()
    plt.close()


def PVP_2D_plots_with_fits():
    global pvp
    std_prof, fit_x, fit_y, kinematic_profiles = pvp.compute_pvp(
        remove_outliers_k_sigma_away=3.5
    )
    fig, axs = plt.subplots(2, 2)
    pvp.plot_kinematic_profiles(ax=[axs[0, 0], axs[0, 1]])
    pvp.plot_std_profiles(axs[1, 0], fit=True)
    plt.tight_layout()
    if SHOW:
        plt.show()
    plt.close()


def PVP_2D_print():
    global pvp
    print(pvp)


def test_PVP_2D_alpha_functions():
    global pvp
    pvp = PVP_alpha()
    PVP_2D_add_trajectory()
    PVP_2D_compute_profiles()
    PVP_2D_plots()
    PVP_2D_remove_outliers()
    PVP_2D_plots_with_fits()
    PVP_2D_print()


def test_PVP_2D_total_functions():
    global pvp
    pvp = PVP_total()
    PVP_2D_add_trajectory()
    PVP_2D_compute_profiles()
    PVP_2D_plots()
    PVP_2D_remove_outliers()
    PVP_2D_plots_with_fits()
    PVP_2D_print()


def test_PVP_2D_generalized_functions():
    global pvp
    pvp = PVP_generalized()
    PVP_2D_add_trajectory()
    PVP_2D_compute_profiles()
    PVP_2D_plots()
    PVP_2D_remove_outliers()
    PVP_2D_plots_with_fits()
    PVP_2D_print()


def PVP_2D():
    test_PVP_2D_alpha_functions()
    test_PVP_2D_total_functions()
    test_PVP_2D_generalized_functions()


if __name__ == "__main__":
    PVP_2D()
