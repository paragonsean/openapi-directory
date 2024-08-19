from typing import List, Dict
from aiohttp import web

from openapi_server.models.fileshare import Fileshare
from openapi_server.models.fileshare_param import FileshareParam
from openapi_server.models.get_fileshare_details import GetFileshareDetails
from openapi_server import util


async def volumes_fs_create_post(request: web.Request, x_auth_token, x_auth_project_id, body) -> web.Response:
    """Create a file share in a space

    This endpoint creates a new file share in a space (corresponding IBM Containers command: &#x60;cf ic volume fs-create FSNAME FSSIZE FSIOPS&#x60;).    A file share is a persistent NFS-based (Network File System) storage system that hosts Docker volumes in a Bluemix space and allows a user to store and access container and app-related files. To store files in a file share, you must create a container volume and save the data into this volume.   As soon as you create your first volume in a space with the &#x60;cf ic volume create VOLNAME&#x60; command or the &#x60;POST /volumes/create&#x60; API endpoint, a default file share with 20 GB at 4 IOPS (Input Output operations Per Second) is created at no cost.   The organization manager can create file shares with specific storage size and IOPS to meet the storage needs of the space. File shares can be provisioned in sizes from 20 GB to 12 TB and at IOPS per GB of 0.25, 2 or 4. Run &#x60;cf ic volume fs-flavor-list&#x60; or call the &#x60;GET /volumes/fs/flavors/json&#x60; API endpoint to retrieve a list of available file share sizes. The file share size in relation to the number of IOPS impacts the speed that data can be read and written from and to the container volume.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param body: The input parameter to create a new file share in a space.
    :type body: dict | bytes

    """
    body = FileshareParam.from_dict(body)
    return web.Response(status=200)


async def volumes_fs_flavors_json_get(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """List available file share sizes

    This endpoint returns a list of available file shares in gigabyte (corresponding IBM Containers command: &#x60;cf ic volume fs-flavor-list&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)


async def volumes_fs_json_get(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """List available file shares in a space

    This endpoint returns a list of all file shares that are availble in a space (corresponding IBM Containers command: &#x60;cf ic volume fs-list&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)


async def volumes_fs_name_delete(request: web.Request, x_auth_token, x_auth_project_id, name) -> web.Response:
    """Delete a file share

    This endpoint deletes a file share from a space (corresponding IBM Containers command: &#x60;cf ic volume fs-rm FSNAME&#x60;).   Before you can delete a file share, all mounted volumes must be deleted first. To delete a volume, run &#x60;cf ic volume rm VOLNAME&#x60; or call the &#x60;DELETE /volumes/{name}&#x60; API endpoint.    **Note:** To delete a file share you must have been granted organization developer rights.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name: The name of the file share that you want to delete. Run &#x60;cf ic volume fs-list&#x60; or call the &#x60;GET /volumes/fs/json&#x60; API endpoint to retrieve a list of available file shares in your space.
    :type name: str

    """
    return web.Response(status=200)


async def volumes_fs_name_json_get(request: web.Request, x_auth_token, x_auth_project_id, name) -> web.Response:
    """Inspect a file share

    This endpoint returns detailed information about a file share (corresponding IBM Containers command: &#x60;cf ic volume fs-inspect FSNAME&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name: The name of the file share that you want to inspect. Run &#x60;cf ic volume fs-list&#x60; or call the &#x60;GET /volumes/fs/json&#x60; endpoint to retrieve a list of available file shares in your space.
    :type name: str

    """
    return web.Response(status=200)
