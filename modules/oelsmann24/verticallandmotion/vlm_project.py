import numpy as np 
import xarray as xr 
import pandas as pd 
import argparse




''' vlm_project.py

This runs the projection stage for the global vertical land motion component.

Parameters:
nsamps = Number of samples to draw
rng_seed = Seed value for the random number generator
locationfilename = File that contains points for localization
pipeline_id = Unique identifier for the pipeline running this code

'''



def vlm_project(pipeline_id):

	return(None)

	
if __name__ == '__main__':	
	
	# Initialize the command-line argument parser
	parser = argparse.ArgumentParser(description="Run the projection stage for the NZInsarGPS vertical land motion workflow",\
	epilog="Note: This is meant to be run as part of the ??? module within the Framework for the Assessment of Changes To Sea-level (FACTS)")
	
	# Define the command line arguments to be expected
	parser.add_argument('--pipeline_id', help="Unique identifier for this instance of the module")
	
	# Parse the arguments
	args = parser.parse_args()
	
	# Run the preprocessing stage with the user defined RCP scenario
	vlm_project(args.pipeline_id)
	
	# Done
	exit()