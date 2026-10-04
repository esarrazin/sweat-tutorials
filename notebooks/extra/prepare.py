# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (C) 2026 CESBIO / Centre National d'Etudes Spatiales
"""
Module containing functions to process data
"""

import numpy as np
import numpy.typing as npt
import xarray as xr

# Functions for handling EC data


def setup_data(
    dry: tuple[float, float],
    wet: tuple[float, float],
    albedo: tuple[float, float],
    valid: tuple[float, float] = (0.0, 1.0),
    fcover: tuple[float, float] | None = None,
    size: int = 125,
    seed: int = 0,
) -> xr.Dataset:
    """
    Generate data for tests
    """

    def dry_edge(v: npt.NDArray) -> npt.NDArray:
        return dry[1] * v + dry[0]

    def wet_edge(v: npt.NDArray) -> npt.NDArray:
        return wet[1] * v + wet[0]

    np.random.seed(seed)
    lon = np.linspace(start=1.0, stop=2.0, num=size, dtype=np.float32)
    lat = np.linspace(start=43.0, stop=44.0, num=size, dtype=np.float32)
    valid_arr = np.random.choice(
        [0, 1], size=(size, size), p=[valid[0], valid[1]]
    ).astype(int)
    albedo_arr = np.random.uniform(
        low=albedo[0], high=albedo[1], size=(size, size)
    )
    lst_func = np.vectorize(
        lambda x: np.random.uniform(wet_edge(x), dry_edge(x))
    )
    lst_arr = lst_func(albedo_arr)
    if fcover is not None:
        fcover_arr = np.random.uniform(
            low=fcover[0], high=fcover[1], size=(size, size)
        )
        lst_func = np.vectorize(
            lambda x, y: np.random.uniform(
                max(wet_edge(x), wet_edge(y)), min(dry_edge(x), dry_edge(y)) #type: ignore
            )
        )
        lst_arr = lst_func(fcover_arr, albedo_arr)
    ef_albedo_arr = (dry_edge(albedo_arr) - lst_arr) / (
        dry_edge(albedo_arr) - wet_edge(albedo_arr)
    )
    data_vars = {
        "albedo": (["lon", "lat"], albedo_arr),
        "lst": (["lon", "lat"], lst_arr),
        "valid": (["lon", "lat"], valid_arr),
        "flags": (["lon", "lat"], np.where(valid_arr, 0, 2).astype(int)),
        "ef_albedo": (["lon", "lat"], ef_albedo_arr),
    }
    if fcover is not None:
        ef_fcover_arr = (dry_edge(fcover_arr) - lst_arr) / (
            dry_edge(fcover_arr) - wet_edge(fcover_arr)
        )
        data_vars["fcover"] = (["lon", "lat"], fcover_arr)
        data_vars["ef_fcover"] = (["lon", "lat"], ef_fcover_arr)
    return xr.Dataset(
        data_vars=data_vars,
        coords={
            "lon": ("lon", lon),
            "lat": ("lat", lat),
        },
        attrs={"description": "Test data"},
    )
    