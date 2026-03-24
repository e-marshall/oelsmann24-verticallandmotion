import click
import logging

from oelsmann24_verticallandmotion.vlm_preprocess import (
    global_preprocess_verticallandmotion,
)
from oelsmann24_verticallandmotion.vlm_postprocess import vlm_postprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--pipeline-id",
    type=str,
    default="1234",
    help="Unique identifier for the processing pipeline.",
)
@click.option(
    "--input-vlm-reconstruction-file",
    type=str,
    required=True,
    help="Path to the input VLM reconstruction data file.",
)
@click.option(
    "--input-gps-vlm-file",
    type=str,
    required=True,
    help="Path to the input GPS VLM data file.",
)
@click.option(
    "--input-gia-vlm-file",
    type=str,
    required=True,
    help="Path to the input GIA VLM data file.",
)
@click.option(
    "--input-dist2coast-file",
    type=str,
    required=True,
    help="Path to the input distance to coast GRD file.",
)
@click.option(
    "--input-example-file",
    type=str,
    required=True,
    help="Path to the input example data file.",
)
@click.option(
    "--nsamps",
    type=int,
    required=True,
    help="Number of samples to generate.",
)
@click.option(
    "--seed",
    type=int,
    default=1234,
    show_default=True,
    help="Seed value for random number generator.",
)
@click.option(
    "--baseyear",
    type=int,
    default=2005,
    help="Base or reference year for projections",
)
@click.option(
    "--pyear-start",
    type=int,
    default=2000,
    help="Year for which projections start",
    show_default=True,
)
@click.option(
    "--pyear-step",
    default=10,
    type=int,
    show_default=True,
    help="Step sizes in years between pyear-start and pyear-stop",
)
@click.option(
    "--pyear-end",
    type=int,
    default=2100,
    show_default=True,
    help="Year for which projections end",
)
@click.option(
    "--location-file",
    type=str,
    help="File that contains name, id, lat, and lon of points for localization",
    required=True,
)
@click.option(
    "--chunk-size",
    type=int,
    default=50,
    show_default=True,
    help="Number of locations to process at a time",
)
@click.option(
    "--output-lslr-file",
    type=str,
    required=True,
    help="Path to the output local sea-level rise projections file.",
)
def main(
    pipeline_id: str,
    input_vlm_reconstruction_file: str,
    input_gps_vlm_file: str,
    input_gia_vlm_file: str,
    input_dist2coast_file: str,
    input_example_file: str,
    nsamps: int,
    seed: int,
    baseyear: int,
    pyear_start: int,
    pyear_step: int,
    pyear_end: int,
    location_file: str,
    chunk_size: int,
    output_lslr_file: str,
):
    """Command-line interface for the oelsmann24-verticallandmotion package."""
    click.echo("Hello from oelsmann24-verticallandmotion!")
    logger.info("Starting preprocessing...")
    preprocess_dict = global_preprocess_verticallandmotion(
        pipeline_id=pipeline_id,
        input_vlm_reconstruction_file=input_vlm_reconstruction_file,
        input_gps_vlm_file=input_gps_vlm_file,
        input_gia_vlm_file=input_gia_vlm_file,
        input_dist2coast_file=input_dist2coast_file,
        input_example_file=input_example_file,
    )
    logger.info("Preprocessing completed.")
    # logic for postprocess args
    if baseyear < 2000:
        raise ValueError(
            "Baseyear cannot be less than year 2000. Baseyear value received: %s",
            baseyear,
        )
    if baseyear > 2300:
        raise ValueError(
            "Baseyear cannot be greater than year 2300. Baseyear value received: %s",
            baseyear,
        )
    if pyear_start < 2000:
        raise ValueError(
            "Projection start year cannot be less than year 2000. Projection start year value received: %s",
            pyear_start,
        )
    if pyear_end > 2300:
        raise ValueError(
            "Projection stop year cannot be greater than year 2300. Projection stop year value received: %s",
            pyear_end,
        )
    if pyear_start >= pyear_end:
        raise ValueError(
            "Projection start year must be less than projection stop year. Projection start year value received: %s, projection stop year value received: %s",
            pyear_start,
            pyear_end,
        )
    if pyear_step < 1:
        raise ValueError(
            "Projection year step must be at least 1 year. Projection year step value received: %s",
            pyear_step,
        )
    logger.info("Starting postprocessing...")

    vlm_postprocess(
        preprocess_dict=preprocess_dict,
        nsamps=nsamps,
        rng_seed=seed,
        location_file=location_file,
        baseyear=baseyear,
        pyear_start=pyear_start,
        pyear_end=pyear_end,
        pyear_step=pyear_step,
        chunksize=chunk_size,
        pipeline_id=pipeline_id,
        output_lslr_file=output_lslr_file,
    )
    logger.info("Postprocessing completed.")
