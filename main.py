from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Backend API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Hello World! Welcome to the Backend API"}


@app.get("/webhooks")
async def webhook(request: Request):
    """Webhook endpoint that extracts and returns query parameters."""
    query_params = dict(request.query_params)
    challenge = query_params.get("hub.challenge")
    print(challenge)
    return Response(content=challenge, media_type="text/plain")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "API is running"}


@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    """Get user by ID."""
    return {"user_id": user_id, "name": f"User {user_id}", "status": "active"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
