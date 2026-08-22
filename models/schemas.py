"""
Pydantic schemas for API request/response models.
"""

from typing import Any, Optional

from pydantic import BaseModel, Field


# ─── Response Models ──────────────────────────────────────────────────────────


class Extent(BaseModel):
    """Geographic bounding box."""

    min_lon: float
    max_lon: float
    min_lat: float
    max_lat: float


class ElevationRange(BaseModel):
    """Elevation statistics."""

    min: float
    max: float


class DEMSize(BaseModel):
    """DEM grid dimensions."""

    rows: int
    cols: int


class AnalysisMetadata(BaseModel):
    """Metadata about the analyzed contour map."""

    filename: str
    contour_count: int
    elevation_range: ElevationRange
    extent: Extent
    dem_resolution_m: float
    dem_size: DEMSize


class DEMStats(BaseModel):
    """Summary statistics of the generated DEM."""

    mean_elevation: float
    std_elevation: float
    mean_slope_deg: float


class CatchmentInfo(BaseModel):
    """Catchment polygon and area for a candidate site."""

    area_km2: float
    polygon: dict  # GeoJSON Feature


class PondCandidate(BaseModel):
    """A candidate pond site with full analysis."""

    rank: int
    score: float = Field(..., description="Composite suitability score (0–1)")
    location: dict = Field(..., description='{"lat": ..., "lon": ...}')
    elevation_m: float
    depression_depth_m: float
    estimated_volume_m3: float
    estimated_surface_area_m2: float
    catchment: CatchmentInfo
    pond_footprint: Optional[dict] = None  # GeoJSON Feature of the inundation area
    twi: float = Field(..., description="Topographic Wetness Index")
    slope_deg: float


class AnalysisResponse(BaseModel):
    """Complete response from /api/analyzeContour."""

    status: str = "success"
    metadata: AnalysisMetadata
    contours_geojson: dict  # GeoJSON FeatureCollection
    candidates: list[PondCandidate]
    dem_stats: DEMStats
    water_bodies_geojson: Optional[dict] = None  # GeoJSON FeatureCollection of water exclusion zones


class ErrorResponse(BaseModel):
    """Error response."""

    status: str = "error"
    detail: str
    error_code: Optional[str] = None
