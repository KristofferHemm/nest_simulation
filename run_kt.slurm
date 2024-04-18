#!/bin/bash -x
#SBATCH --account=icei-hbp-2020-0005
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --output=run_kt.%j
#SBATCH --error=run_kt.%j
#SBATCH --time=00:20:00
#SBATCH --partition=batch

module load Stages/2023 GCC CMake Boost GSL OpenMPI Python SciPy-Stack mpi4py HDF h5py

export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

export MKL_THREADING_LAYER=GNU

cd /p/home/jusers/hemm1/jusuf/project/master/ai_alpha_to_delta

source /p/home/jusers/hemm1/jusuf/project/nest/bld_3.4/install/bin/nest_vars.sh

python run.py

