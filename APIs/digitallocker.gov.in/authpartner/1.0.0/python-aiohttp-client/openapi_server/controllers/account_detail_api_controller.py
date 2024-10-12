from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_list_of_self_uploaded_documents500_response import GetListOfSelfUploadedDocuments500Response
from openapi_server.models.sample5 import Sample5
from openapi_server.models.upload_file_to_locker_id401_response import UploadFileToLockerId401Response
from openapi_server import util


async def account_detail_api_id(request: web.Request, ) -> web.Response:
    """Get User Details

    Client applications can call this API to get the DigiLocker Id, name, date of birth and gender of the account holder. An access token is required to call this API. The API will return the user details of the account with which the access token is linked. It is strongly recommended that the API can be called by client application only once after acquiring the access token. Since the user details do not change, the client application may store the values and use them when necessary than calling this API repeatedly.


    """
    return web.Response(status=200)
