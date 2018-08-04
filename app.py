# app.py
import asyncio
import time
import base64
from aiohttp import web
import aiohttp_cors

async def ping(request):
    data = {
        'dta':'pong'
    }
    return web.json_response(data=data)
    

app = web.Application()


app.add_routes([web.get('/ping', ping)])

# Configure CORS on all routes.
cors = aiohttp_cors.setup(app,defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})
for route in list(app.router.routes()):
    cors.add(route)

web.run_app(app)

