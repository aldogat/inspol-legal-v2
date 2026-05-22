from routes.dashboard import router as dashboard_router

app.include_router(dashboard_router, prefix="/api/v1")
