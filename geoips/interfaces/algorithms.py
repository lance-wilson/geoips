# # # Distribution Statement A. Approved for public release. Distribution unlimited.
# # #
# # # Author:
# # # Naval Research Laboratory, Marine Meteorology Division
# # #
# # # This program is free software: you can redistribute it and/or modify it under
# # # the terms of the NRLMMD License included with this program. This program is
# # # distributed WITHOUT ANY WARRANTY; without even the implied warranty of
# # # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the included license
# # # for more details. If you did not receive the license, for more information see:
# # # https://github.com/U-S-NRL-Marine-Meteorology-Division/

"""Algorithms interface module."""

from geoips.interfaces.base import BaseInterface, BasePlugin


class AlgorithmsInterface(BaseInterface):
    """Data manipulations to apply to the dataset."""

    name = "algorithms"
    deprecated_family_attr = "alg_func_type"

    required_args = {
        "single_channel": ["arrays"],
        "channel_combination": ["arrays"],
        "list_numpy_to_numpy": ["arrays"],
        "xarray_to_numpy": ["xobj"],
        "rgb": ["arrays"],
        "xarray_dict_to_xarray": ["xarray_dict"],
        "xarray_dict_dict_to_xarray": ["xarray_dict_dict"],
        "xarray_dict_to_xarray_dict": ["xarray_dict"],
        "xarray_dict_area_def_to_numpy": ["xarray_dict", "area_def"],
    }

    required_kwargs = {
        "single_channel": [],
        "channel_combination": [],
        "xarray_to_numpy": [],
        "list_numpy_to_numpy": [],
        "rgb": [],
        "xarray_dict_to_xarray": [],
        "xarray_dict_dict_to_xarray": [],
        "xarray_dict_to_xarray_dict": [],
        "xarray_dict_area_def_to_numpy": [],
    }


algorithms = AlgorithmsInterface()
