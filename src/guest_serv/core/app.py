from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.guest_serv.core.config import cors_settings


def create_app() -> FastAPI:
    app = FastAPI(
        title="Backoffice API",
        description="API for guest_serv",
        version="0.1.0",
    )

    if cors_settings.enabled:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_settings.allow_origins,
            allow_credentials=cors_settings.allow_credentials,
            allow_methods=cors_settings.allow_methods,
            allow_headers=cors_settings.allow_headers,
        )

    return app


__all__ = ("create_app",)
