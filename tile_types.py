from typing import Tuple
import numpy as np 

graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
         ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", bool),
        ("transparent", bool),
        ("dark", graphic_dt), # not in FOV
        ("light", graphic_dt) # in FOV
    ]
)



def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int,int,int], Tuple[int,int,int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

SHROUD = np.array((ord(" "), (255,255,255), (0,0,0)), dtype=graphic_dt) # just a black tile. neither in fov or explored

floor = new_tile(
    walkable=True,
    transparent=True, 
    dark=(ord(" "), (255,255,255), (0, 22, 41)),
    light = (ord(" "), (255,255,255), (200, 180, 50))
)

wall = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord(" "), (255,255,255), (128,128,128)),
    light = (ord(" "), (255,255,255), (130,110,50))
)