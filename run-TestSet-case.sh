#!/bin/sh
#
#  Reservation desired
#$ -R y
#
#  Reserve 8 CPUs for this job
#$ -pe parallel 32
#
#  Request 8G of RAM
#$ -l h_vmem=1G
#
#  Request it to run this long HH:MM:SS
#$ -l h_rt=00:59:00
#
#  Use /bin/bash to execute this script
#$ -S /bin/bash
#
#  Run job from current working directory
#$ -cwd
#
#  Send email when the job begins, ends, aborts, or is suspended
#$ -m beas

python ./scripts/run-pipeline.py -fn ./data/TestSet -sl TestSet-RefSeq.txt  -st 1 3 4 5 6 7 8 9 10 11 -t 32  > TestSet.log
