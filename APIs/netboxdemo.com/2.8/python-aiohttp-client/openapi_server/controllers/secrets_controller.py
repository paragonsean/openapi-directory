from typing import List, Dict
from aiohttp import web

from openapi_server.models.secret import Secret
from openapi_server.models.secret_role import SecretRole
from openapi_server.models.secrets_secret_roles_list200_response import SecretsSecretRolesList200Response
from openapi_server.models.secrets_secrets_list200_response import SecretsSecretsList200Response
from openapi_server.models.writable_secret import WritableSecret
from openapi_server import util


async def secrets_generate_rsa_key_pair_list(request: web.Request, ) -> web.Response:
    """This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.

    {         \&quot;public_key\&quot;: \&quot;&lt;public key&gt;\&quot;,         \&quot;private_key\&quot;: \&quot;&lt;private key&gt;\&quot;     }


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


async def secrets_secret_roles_list(request: web.Request, id=None, name=None, slug=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, limit=None, offset=None) -> web.Response:
    """secrets_secret_roles_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param q: 
    :type q: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
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

    Call to super to allow for caching

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


async def secrets_secrets_list(request: web.Request, id=None, name=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, role_id=None, role=None, device_id=None, device=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, role_id__n=None, role__n=None, device_id__n=None, device__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """secrets_secrets_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
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
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param device_id__n: 
    :type device_id__n: str
    :param device__n: 
    :type device__n: str
    :param tag__n: 
    :type tag__n: str
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
