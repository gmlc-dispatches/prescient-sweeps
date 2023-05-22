import os
import sys

from parameters import update_function
from dispatches_prescient_sweeps.prescient_options_15_reserves_1000_shortfall import prescient_options
from dispatches_prescient_sweeps.utils import run_sweep

prescient_options["output_directory"] = str(os.path.splitext(os.path.basename(__file__))[0])

start, stop = int(sys.argv[1]), int(sys.argv[2])

run_sweep(update_function, prescient_options, start, stop)
