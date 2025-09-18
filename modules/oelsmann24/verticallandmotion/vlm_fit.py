import argparse

''' vlm_fit.py

This runs the fitting stage for the vertical land motion component of the IPCC AR6
workflow.

Parameters:
pipeline_id = Unique identifier for the pipeline running this code

Note: This is currently a NULL process. Rates are already read in during the preprocess
stage.

'''

def gloabl_vlm_fit(pipeline_id):
	
	return(None)

	
if __name__ == '__main__':	
	
	# Initialize the command-line argument parser
	parser = argparse.ArgumentParser(description="Run the fitting stage for the GlobalVLM workflow",\
	epilog="Note: This is meant to be run as part of the GlobalVLM module within the Framework for the Assessment of Changes To Sea-level (FACTS)")
	
	# Define the command line arguments to be expected
	parser.add_argument('--pipeline_id', help="Unique identifier for this instance of the module")
	
	# Parse the arguments
	args = parser.parse_args()
	
	# Run the preprocessing stage with the user defined RCP scenario
	gloabl_vlm_fit(args.pipeline_id)
	
	# Done
	exit()