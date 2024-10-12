from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2_metapub_program_information_batch_post_request import ApiV2MetapubProgramInformationBatchPostRequest
from openapi_server.models.program_information_batch import ProgramInformationBatch
from openapi_server import util


async def api_v2_metapub_program_information_batch_batch_id_get(request: web.Request, batch_id) -> web.Response:
    """Get an EPG batch operation.

    Gets the batch information which can be used to check the status of the operation or retrieve more details if the batch fails.

    :param batch_id: 
    :type batch_id: int

    """
    return web.Response(status=200)


async def api_v2_metapub_program_information_batch_post(request: web.Request, body=None) -> web.Response:
    """Create a batch operation on EPG information.

    Create a batch to process the metadata of one or more electronic program guide (EPG) programs using metadata that has been uploaded to the customer&#39;s CD Drive. If multiple EPG programs are present in the metadata, they will all be updated, however updates across programs are not atomic. Note that an EPG program maps to the ContentDepot concept of an episode which is also known as a \&quot;program instance\&quot;.  A batch operation must be explicitly created rather than the server attempting to detect new metadata in order to allow for all the content to be uploaded including any supporting content like images. A batch operation is accepted and queued for asynchronous processing at a later time. A client can poll the batch periodically to determine when it completes and the resulting state. 

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV2MetapubProgramInformationBatchPostRequest.from_dict(body)
    return web.Response(status=200)
