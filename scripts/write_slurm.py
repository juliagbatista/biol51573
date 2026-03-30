##shebang line to specify the Python interpreter to use when running this script
#!/usr/bin/env python3
 
import argparse

parser = argparse.ArgumentParser(description="This script generates a slurm script template")

# add a walltime argument 
parser.add_argument("walltime", help="Job walltime for the slurm script")
parser.add_argument("job_name", help="Name assigned to the job to be run")
parser.add_argument("email",help="personal email")
#walltime = 1
#job_name = 'big-analysis'

#parse the arguments
args = parser.parse_args()

print("#!/bin/bash")
print()
print(f"#SBATCH --job-name={args.job_name}")
print(f"#SBATCH --partition comp01")
print(f"#SBATCH --nodes=1")
print(f"#SBATCH --qos comp")
print(f"#SBATCH --cpus-per-task=32")
print(f"#SBATCH --time={args.walltime}:00:00")
print(f"#SBATCH --output=%x.%j.out")
print(f"#SBATCH --error=%x.%j.err")
print(f"#SBATCH --mail-type=ALL")
print(f"#SBATCH --mail-user=cer049@uark.edu")

print()
print(f"export OMP_NUM_THREADS=32")

print()
print(f"module purge")
print(f"module load intel/18.0.1 impi/18.0.1 mkl/18.0.1")

print()
print(f"cd $SLURM_SUBMIT_DIR")