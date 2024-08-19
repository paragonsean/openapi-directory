from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_signing_keys_response import ListSigningKeysResponse
from openapi_server.models.signing_key_response import SigningKeyResponse
from openapi_server import util


async def create_signing_key(request: web.Request, ) -> web.Response:
    """Create a signing key

    Creates a new signing key pair. When creating a new signing key, the API will generate a 2048-bit RSA key-pair and return the private key and a generated key-id; the public key will be stored at Mux to validate signed tokens.


    """
    return web.Response(status=200)


async def delete_signing_key(request: web.Request, signing_key_id) -> web.Response:
    """Delete a signing key

    Deletes an existing signing key. Use with caution, as this will invalidate any existing signatures and no JWTs can be signed using the key again.

    :param signing_key_id: The ID of the signing key.
    :type signing_key_id: str

    """
    return web.Response(status=200)


async def get_signing_key(request: web.Request, signing_key_id) -> web.Response:
    """Retrieve a signing key

    Retrieves the details of a signing key that has previously been created. Supply the unique signing key ID that was returned from your previous request, and Mux will return the corresponding signing key information. **The private key is not returned in this response.** 

    :param signing_key_id: The ID of the signing key.
    :type signing_key_id: str

    """
    return web.Response(status=200)


async def list_signing_keys(request: web.Request, limit=None, page=None) -> web.Response:
    """List signing keys

    Returns a list of signing keys.

    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int

    """
    return web.Response(status=200)
