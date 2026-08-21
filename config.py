"""
Configuration settings for the Pond Planning System backend.
All parameters are configurable to support generalization to different contour maps.
"""

from pydantic import BaseModel


class AnalysisConfig(BaseModel):
    """Configuration for terrain analysis parameters."""

    # DEM Generation
    dem_resolution_m: float = 5.0  # Grid cell size in meters
    max_contour_vertices: int = 50000  # Subsample threshold for interpolation perf
    rbf_kernel: str = "thin_plate_spline"  # scipy RBF kernel

    # Depression Detection
    min_depression_depth_m: float = 0.3  # Minimum fill depth to consider as depression
    min_depression_area_cells: int = 20  # Minimum connected depression size

    # Candidate Selection
    candidate_min_spacing_m: float = 50.0  # Min distance between candidates
    num_candidates: int = 5  # Default number of candidates to return
    score_weights: dict = {
        "depression": 0.35,
        "twi": 0.25,
        "slope": 0.20,
        "accumulation": 0.20,
    }

    # Catchment
    min_catchment_area_km2: float = 0.01  # Minimum catchment to be meaningful


# Server config
HOST = "0.0.0.0"
PORT = 8000
CORS_ORIGINS = ["http://localhost:5173", "http://localhost:3000", "http://127.0.0.1:5173"]

# Max upload file size (50 MB)
MAX_UPLOAD_SIZE_MB = 50
