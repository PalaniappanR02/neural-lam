import numpy as np
import pandas as pd
import xarray as xr
import os

def create_synthetic_zarr(path, nx=10, ny=10, nt=5):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    ds = xr.Dataset(coords={'time': pd.date_range('2016-01-01', periods=nt, freq='1H'), 'x': np.arange(nx), 'y': np.arange(ny), 'z': [6, 12, 20, 27, 31, 39, 45, 60]})
    for var in ['U', 'V', 'T']:
        ds[var] = (('time', 'x', 'y', 'z'), np.random.rand(nt, nx, ny, 8).astype(np.float32))
    for var in ['T_2M', 'U_10M', 'V_10M', 'PMSL']:
        ds[var] = (('time', 'x', 'y'), np.random.rand(nt, nx, ny).astype(np.float32))
    ds.to_zarr(path, mode='w')
    print(f'Successfully generated synthetic data at: {path}')

if __name__ == '__main__':
    create_synthetic_zarr('data/cosmo_sample.zarr')