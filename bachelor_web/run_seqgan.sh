#! /bin/bash
source ./venv/bin/activate
# virtualenv is now active.

python3 ../seqGAN-tensorflow-master/run.py

deactivate
