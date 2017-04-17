import h5py
import numpy as np

file=h5py.File('x.h5','w')
dset = file.create_dataset('data', (800000,100,100,3),dtype='uint8')
dset[700000,0:100,0,2]=np.arange(100)
file.close()

file=h5py.File('x.h5','r')
dset = file['data']
print dset[700000,0:100,0,2]
file.close()