from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_volume import UpdateVolume
from openapi_server.models.volume import Volume
from openapi_server import util


async def volumes_create_post(request: web.Request, x_auth_token, x_auth_project_id, name, fs_name=None) -> web.Response:
    """Create a volume in a space

    This endpoints creates a new volume in your space (corresponding IBM Containers command: &#x60;cf ic volume create VOLNAME&#x60;). A volume is used to persist and access app data between container restarts. Volumes are hosted on file shares that define the available actual storage in Bluemix and the number of input and output transactions per second (IOPS).    After you have created a volume, you must mount it to a container by using the &#x60;--volume&#x60; option in the &#x60;cf ic run&#x60; (single containers) or &#x60;cf ic group create&#x60; (container groups) command. You can also define the volume as part of the HTTP body and send a request to the &#x60;POST /containers/create&#x60; (single containers) or &#x60;POST /containers/groups&#x60; (container groups) endpoints.    Note: If you mount multiple containers in a space to the same volume, they share the data in the volume and can access them anytime. When a container is deleted, the associated volume is not removed.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name: The name of the volume. The name must be unique for a space and can contain uppercase letters, lowercase letters, numbers, underscores (_), and hyphens (-).
    :type name: str
    :param fs_name: The name of the file share that the volume is hosted on. File shares can have different storage sizes and IOPS based on the required workload. If this field is left blank, the volume is hosted on the default file share.
    :type fs_name: str

    """
    return web.Response(status=200)


async def volumes_json_get(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """List all volumes for a space

    This endpoint returns a list of all volumes that are available in the given space (corresponding IBM Containers command: &#x60;cf ic volume list&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)


async def volumes_name_delete(request: web.Request, x_auth_token, x_auth_project_id, name) -> web.Response:
    """Delete a volume

    Delete a volume with a given name from a space (corresponding IBM Containers command: &#x60;cf ic volume rm VOLNAME&#x60;). To delete a volume, all mounted containers must be unmounted first. After the volume is deleted, the data that are stored in the volume are lost. 

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name: The name of the volume that you want to delete. Run &#x60;cf ic volume list&#x60; or call the &#x60;GET /volumes/json&#x60; endpoint to retrieve a list of all volumes that are available in your space.
    :type name: str

    """
    return web.Response(status=200)


async def volumes_name_json_get(request: web.Request, x_auth_token, x_auth_project_id, name) -> web.Response:
    """Retrieve detailed information about a volume. 

    Retrieve a detailed list of information about a volume that is identified by the volume name (corresponding IBM Containers command: &#x60;cf ic volume inspect VOLNAME&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name: The name of the volume, for which you want to retrieve detailed information. Run &#x60;cf ic volume list&#x60; or call the &#x60;GET /volumes/json&#x60; endpoint to retrieve a list of all volumes that are available in your space.
    :type name: str

    """
    return web.Response(status=200)


async def volumes_name_post(request: web.Request, x_auth_token, x_auth_project_id, name, body) -> web.Response:
    """Share a volume with another space

    This endpoint provisions an existing volume that was created in one space to another space within the same organization. Single containers and container groups in each space can read and write to the shared volume. The volume remains owned by the original space it was created in, including management and billing. For example, the volume can be deleted from the original space only.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name: The name of the volume that you want to share with another space in your organization.
    :type name: str
    :param body: Input parameter that are required to provision an existing volume to a new space and to unprovision it from a space.
    :type body: dict | bytes

    """
    body = UpdateVolume.from_dict(body)
    return web.Response(status=200)
