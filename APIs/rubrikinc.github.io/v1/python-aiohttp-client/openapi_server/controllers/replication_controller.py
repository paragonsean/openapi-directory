from typing import List, Dict
from aiohttp import web

from openapi_server.models.disable_per_location_pause import DisablePerLocationPause
from openapi_server.models.enable_per_location_pause import EnablePerLocationPause
from openapi_server import util


async def disable_per_location_pause(request: web.Request, body) -> web.Response:
    """Resume replication from specified source clusters

    A single Rubrik cluster can be the replication target for multiple source Rubrik clusters. For each source cluster specified, this resumes replication from that source cluster to the target cluster. This call must be made on the target cluster. 

    :param body: A configuration value that specifies which source clusters resume replication. Snapshots taken before or during the replication pause can be skipped. 
    :type body: dict | bytes

    """
    body = DisablePerLocationPause.from_dict(body)
    return web.Response(status=200)


async def enable_per_location_pause(request: web.Request, body) -> web.Response:
    """Pause replication from specified source clusters

    A single Rubrik cluster can be the replication target for multiple source Rubrik clusters. For each source cluster specified, this pauses replication from that source cluster to the target cluster. This call must be made on the target cluster. 

    :param body: A configuration value that specifies which source clusters pause replication. Replication jobs can be canceled immediately or be allowed to finish. 
    :type body: dict | bytes

    """
    body = EnablePerLocationPause.from_dict(body)
    return web.Response(status=200)
