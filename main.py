"""
Pond Planning System — FastAPI Backend
Main application entry point.
"""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import CORS_ORIGINS, HOST, PORT
from routes.analysis import router as analysis_router

# ── Logging ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger(__name__)

# ── FastAPI App ──────────────────────────────────────────────────────────────

app = FastAPI(
    title="Pond Planning System API",
    description=(
        "AI-based Village Pond Planning System. Analyzes contour maps (KML/KMZ) "
        "to identify optimal pond locations, estimate catchment areas, "
        "and compute storage volumes."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS ─────────────────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routes ───────────────────────────────────────────────────────────────────

app.include_router(analysis_router)


@app.get("/", tags=["Health"])
async def root():
    """Health check endpoint."""
    return {
        "status": "running",
        "service": "Pond Planning System API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
async def health():
    """Health check."""
    return {"status": "healthy"}


# ── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn

    logger.info(f"Starting Pond Planning API on {HOST}:{PORT}")
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
