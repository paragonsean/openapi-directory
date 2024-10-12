from typing import List, Dict
from aiohttp import web

from openapi_server.models.secret import Secret
from openapi_server.models.secret_role import SecretRole
from openapi_server.models.secrets_secret_roles_list200_response import SecretsSecretRolesList200Response
from openapi_server.models.secrets_secrets_list200_response import SecretsSecretsList200Response
from openapi_server.models.writable_secret import WritableSecret
from openapi_server import util


async def secrets_choices_list(request: web.Request, ) -> web.Response:
    """secrets_choices_list

    


    """
    return web.Response(status=200)


async def secrets_choices_read(request: web.Request, id) -> web.Response:
    """secrets_choices_read

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def secrets_generate_rsa_key_pair_list(request: web.Request, ) -> web.Response:
    """secrets_generate_rsa_key_pair_list

    This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.      {         \&quot;public_key\&quot;: \&quot;&lt;public key&gt;\&quot;,         \&quot;private_key\&quot;: \&quot;&lt;private key&gt;\&quot;     }


    """
    return web.Response(status=200)


async def secrets_get_session_key_create(request: web.Request, ) -> web.Response:
    """secrets_get_session_key_create

    Retrieve a temporary session key to use for encrypting and decrypting secrets via the API. The user&#39;s private RSA key is POSTed with the name &#x60;private_key&#x60;. An example:      curl -v -X POST -H \&quot;Authorization: Token &lt;token&gt;\&quot; -H \&quot;Accept: application/json; indent&#x3D;4\&quot; \\     --data-urlencode \&quot;private_key@&lt;filename&gt;\&quot; https://netbox/api/secrets/get-session-key/  This request will yield a base64-encoded session key to be included in an &#x60;X-Session-Key&#x60; header in future requests:      {         \&quot;session_key\&quot;: \&quot;+8t4SI6XikgVmB5+/urhozx9O5qCQANyOk1MNe6taRf&#x3D;\&quot;     }  This endpoint accepts one optional parameter: &#x60;preserve_key&#x60;. If True and a session key exists, the existing session key will be returned instead of a new one.


    """
    return web.Response(status=200)


async def secrets_secret_roles_create(request: web.Request, body) -> web.Response:
    """secrets_secret_roles_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = SecretRole.from_dict(body)
    return web.Response(status=200)


async def secrets_secret_roles_delete(request: web.Request, id) -> web.Response:
    """secrets_secret_roles_delete

    

    :param id: A unique integer value identifying this secret role.
    :type id: int

    """
    return web.Response(status=200)


async def secrets_secret_roles_list(request: web.Request, name=None, slug=None, limit=None, offset=None) -> web.Response:
    """secrets_secret_roles_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def secrets_secret_roles_partial_update(request: web.Request, id, body) -> web.Response:
    """secrets_secret_roles_partial_update

    

    :param id: A unique integer value identifying this secret role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SecretRole.from_dict(body)
    return web.Response(status=200)


async def secrets_secret_roles_read(request: web.Request, id) -> web.Response:
    """secrets_secret_roles_read

    

    :param id: A unique integer value identifying this secret role.
    :type id: int

    """
    return web.Response(status=200)


async def secrets_secret_roles_update(request: web.Request, id, body) -> web.Response:
    """secrets_secret_roles_update

    

    :param id: A unique integer value identifying this secret role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SecretRole.from_dict(body)
    return web.Response(status=200)


async def secrets_secrets_create(request: web.Request, body) -> web.Response:
    """secrets_secrets_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableSecret.from_dict(body)
    return web.Response(status=200)


async def secrets_secrets_delete(request: web.Request, id) -> web.Response:
    """secrets_secrets_delete

    

    :param id: A unique integer value identifying this secret.
    :type id: int

    """
    return web.Response(status=200)


async def secrets_secrets_list(request: web.Request, name=None, id__in=None, q=None, role_id=None, role=None, device_id=None, device=None, tag=None, limit=None, offset=None) -> web.Response:
    """secrets_secrets_list

    

    :param name: 
    :type name: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
    :param device_id: 
    :type device_id: str
    :param device: 
    :type device: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def secrets_secrets_partial_update(request: web.Request, id, body) -> web.Response:
    """secrets_secrets_partial_update

    

    :param id: A unique integer value identifying this secret.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableSecret.from_dict(body)
    return web.Response(status=200)


async def secrets_secrets_read(request: web.Request, id) -> web.Response:
    """secrets_secrets_read

    

    :param id: A unique integer value identifying this secret.
    :type id: int

    """
    return web.Response(status=200)


async def secrets_secrets_update(request: web.Request, id, body) -> web.Response:
    """secrets_secrets_update

    

    :param id: A unique integer value identifying this secret.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableSecret.from_dict(body)
    return web.Response(status=200)
