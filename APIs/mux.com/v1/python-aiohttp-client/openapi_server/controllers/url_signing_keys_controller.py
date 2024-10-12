from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_signing_keys_response import ListSigningKeysResponse
from openapi_server.models.signing_key_response import SigningKeyResponse
from openapi_server import util


async def create_url_signing_key(request: web.Request, ) -> web.Response:
    """Create a URL signing key

    This route is now deprecated, please use the &#x60;Signing Keys&#x60; API. Creates a new signing key pair. When creating a new signing key, the API will generate a 2048-bit RSA key-pair and return the private key and a generated key-id; the public key will be stored at Mux to validate signed tokens.  Note: Any new access tokens authenticating this route will be required to have &#x60;System&#x60; level permissions. 


    """
    return web.Response(status=200)


async def delete_url_signing_key(request: web.Request, signing_key_id) -> web.Response:
    """Delete a URL signing key

    This route is now deprecated, please use the &#x60;Signing Keys&#x60; API. Deletes an existing signing key. Use with caution, as this will invalidate any existing signatures and no URLs can be signed using the key again.  Note: Any new access tokens authenticating this route will be required to have &#x60;System&#x60; level permissions. 

    :param signing_key_id: The ID of the signing key.
    :type signing_key_id: str

    """
    return web.Response(status=200)


async def get_url_signing_key(request: web.Request, signing_key_id) -> web.Response:
    """Retrieve a URL signing key

    This route is now deprecated, please use the &#x60;Signing Keys&#x60; API. Retrieves the details of a URL signing key that has previously been created. Supply the unique signing key ID that was returned from your previous request, and Mux will return the corresponding signing key information. **The private key is not returned in this response.**  Note: Any new access tokens authenticating this route will be required to have &#x60;System&#x60; level permissions. 

    :param signing_key_id: The ID of the signing key.
    :type signing_key_id: str

    """
    return web.Response(status=200)


async def list_url_signing_keys(request: web.Request, limit=None, page=None) -> web.Response:
    """List URL signing keys

    This route is now deprecated, please use the &#x60;Signing Keys&#x60; API. Returns a list of URL signing keys.  Note: Any new access tokens authenticating this route will be required to have &#x60;System&#x60; level permissions. 

    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int

    """
    return web.Response(status=200)
