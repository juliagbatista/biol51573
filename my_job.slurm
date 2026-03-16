#!/bin/bash

#SBATCH --job-name=my_job
#SBATCH --partition=cloud72
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --time=01:00:00
#SBATCH --output=my_job.output
#SBATCH --error=my_job.error
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jg329@uark.edu

#set the number of threads
export OMP_NUM_THREADS=32

# Load necessary modules for your job 
module purge
module load intel/18.0.1 impi/18.0.1 mkl/18.0.1
module load blast

cd $SLURM_SUBMIT_DIR

#blast watermelon against itself
blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn

