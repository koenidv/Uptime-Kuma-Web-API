# authentication.py
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from uptime_kuma_api import UptimeKumaApi, UptimeKumaException

from config import settings, logger as logging

http_bearer = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
):
    if not settings.API_KEY:
        raise HTTPException(status_code=500, detail="API_KEY is not configured")

    if credentials.credentials != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

    try:
        api = UptimeKumaApi(settings.KUMA_SERVER)
        api.login(settings.KUMA_USERNAME, settings.KUMA_PASSWORD)
        return {"token": credentials.credentials, "api": api}
    except UptimeKumaException as e:
        logging.fatal(e)
        raise HTTPException(400, {"error": str(e)})
