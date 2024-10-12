from typing import List, Dict
from aiohttp import web

from openapi_server.models.container import Container
from openapi_server.models.container_id import ContainerId
from openapi_server.models.container_info import ContainerInfo
from openapi_server.models.create_container import CreateContainer
from openapi_server.models.get_container_status import GetContainerStatus
from openapi_server import util


async def containers_create_post(request: web.Request, x_auth_token, x_auth_project_id, body, name=None) -> web.Response:
    """Create and start a single container

    This endpoint creates and starts a single container in your space based on the Docker image that is specified in the Image field of the request json. A single container in IBM Containers is similar to a container that you create in your local Docker environment. Single containers are a good way to start with IBM Containers and to learn about how containers work in the IBM Cloud and the features that IBM Containers provides. They are also recommended when you want to run simple app tests or during the development process of an app.    In the Docker API there are two separate APIs to create and start a container. However in IBM Containers a container is created and started in a single API call. Therefore, this API merges parameters from the Docker API to create and start container.    To create a container with IBM Containers, you must at least define the image that the container is based on.  - Image: You must include the full path to the image in your private Bluemix registry in the format: &#x60;registry.ng.bluemix.net/&lt;namespace&gt;/&lt;image&gt;&#x60;.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param body: Summary of input parameter to create a container in IBM Containers.
    :type body: dict | bytes
    :param name: Choose a name for your container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter.
    :type name: str

    """
    body = CreateContainer.from_dict(body)
    return web.Response(status=200)


async def containers_id_status_get(request: web.Request, x_auth_token, x_auth_project_id, id) -> web.Response:
    """List the current state of a container.

    This endpoint returns the current state of a container. This state can either be a transient state, such as BUILDING and NETWORKING, or a non-transient state, such as RUNNING, SHUTDOWN, CRASHED, or SUSPENDED.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param id: The unique identifier that represents the container. Run &#x60;cf ic ps&#x60;, or call the &#x60;GET /containers/json&#x60; endpoint to retrieve the ID of the container.
    :type id: str

    """
    return web.Response(status=200)


async def containers_json_get(request: web.Request, x_auth_token, x_auth_project_id, all=None, filters=None) -> web.Response:
    """List single containers in a space.

    This endpoint returns a list of all single containers in a space that are currently in a running state (corresponding IBM Containers command: &#x60;cf ic ps&#x60;). To list all single containers independent of their current state, set the &#x60;all&#x60; query parameter to true.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param all: By default, the &#x60;GET /containers/json&#x60; endpoint returns a list of all single containers in a space that are in a running state. To request a list of all containers independent of their current state, set the &#x60;all&#x60; query parameter to true. Allowed values are: &#x60;all&#x3D;true&#x60;, &#x60;all&#x3D;True&#x60;, and &#x60;all&#x3D;1&#x60;. 
    :type all: str
    :param filters: You can filter your containers by any environment variable key or value that is listed in the &#x60;Env&#x60; section of your CLI/ API response when you run the &#x60;cf ic inspect &lt;container&gt;&#x60; command, or call the &#x60;GET /containers/{id}/json&#x60; endpoint. Your search criteria does not need to be an exact match. It can also be a part of the key or value you are looking for. For example, to filter all containers with an environment variable that contains &#x60;id&#x60; in one of their environment variables, use &#x60;filter&#x3D;id&#x60;.
    :type filters: str

    """
    return web.Response(status=200)


async def containers_name_or_id_delete(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, force=None) -> web.Response:
    """Remove a single container

    Remove a single container that is identified by container ID or name from a space (corresponding IBM Containers command: &#x60;cf ic delete &lt;container&gt;&#x60;). The container must be stopped before it can be deleted, unless the &#x60;force&#x60; query parameter is set to true.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The unique identifier or name of the container that you want to delete. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review all containers in your space.
    :type name_or_id: str
    :param force: Use the &#x60;force&#x60; query parameter if you want to delete the container independent of their current state. The container does not need to be stopped first. To force the deletion of a container, enter &#x60;force&#x3D;true&#x60;, &#x60;force&#x3D;True&#x60;, or &#x60;force&#x3D;1&#x60;. If you want to delete containers that are in a non-running state only, do either not set this query parameter, or enter &#x60;force&#x3D;false&#x60;, &#x60;force&#x3D;False&#x60;, or &#x60;force&#x3D;0&#x60;.
    :type force: bool

    """
    return web.Response(status=200)


async def containers_name_or_id_json_get(request: web.Request, x_auth_token, x_auth_project_id, name_or_id) -> web.Response:
    """Inspect a single container

    This endpoint retrieves detailed information about a single container (corresponding IBM Containers command: &#x60;cf ic inspect &lt;container&gt;&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The name or ID of the container that you want to inspect. Run the &#x60;cf ic ps&#x60; command or call the &#x60;GET /containers/json&#x60; endpoint to retrieve a list of containers in your space.
    :type name_or_id: str

    """
    return web.Response(status=200)


async def containers_name_or_id_pause_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id) -> web.Response:
    """Pause a single container

    Pause all processes in a running single container with a given container ID or name (corresponding IBM Containers command: &#x60;cf ic pause &lt;container&gt;&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The unique identifier or name of the container that you want to pause. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review all containers in your space that are currently in a running state.
    :type name_or_id: str

    """
    return web.Response(status=200)


async def containers_name_or_id_rename_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, name) -> web.Response:
    """Rename a single container

    Change the current name of an existing single container that is identified by the container ID or name (corresponding IBM Containers command: &#x60;cf ic rename &lt;old_name&gt; &lt;new_name&gt;&#x60;). 

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The unique identifier or name of the container that you want to rename. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review all containers in your space.
    :type name_or_id: str
    :param name: The new name for the container. The characters in the name can include uppercase letters, lowercase letters, numbers, periods (.), underscores (_), or hyphens (-), but the name must start with a letter.
    :type name: str

    """
    return web.Response(status=200)


async def containers_name_or_id_restart_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, t=None) -> web.Response:
    """Restart a single container

    Restart a container with a given container ID or name (corresponding IBM Containers command: &#x60;cf ic restart &lt;container&gt;&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The unique identifier or name of the container that you want to restart. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review all containers in your space.
    :type name_or_id: str
    :param t: The number of seconds to wait before the container is restarted. For example, if you want a container to restart after 10 seconds, enter &#x60;t&#x3D;10&#x60;.
    :type t: int

    """
    return web.Response(status=200)


async def containers_name_or_id_start_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id) -> web.Response:
    """Start a single container

    Start a single container with a given container name or ID (corresponding IBM Containers command: &#x60;cf ic start &lt;container&gt;&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The unique identifier or name of the container that you want to start. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review the containers in your space that are currently not in a running state.
    :type name_or_id: str

    """
    return web.Response(status=200)


async def containers_name_or_id_stop_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, t=None) -> web.Response:
    """Stop a single container

    Stop a single container with a given container name or ID (corresponding IBM Containers command: &#x60;cf ic stop &lt;container&gt;&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The unique identifier or name of the container that you want to stop. Run &#x60;cf ic ps&#x60; or call the &#x60;GET /containers/json&#x60; endpoint to review the containers in your space that are currently in a running state.
    :type name_or_id: str
    :param t: The number of seconds to wait before the container is stopped. For example, if you want a container to stop after 10 seconds, enter &#x60;t&#x3D;10&#x60;.
    :type t: int

    """
    return web.Response(status=200)


async def containers_name_or_id_unpause_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id) -> web.Response:
    """Unpause a single container

    Unpause all processes that are currently stopped inside a single containers with a given container ID or name (corresponding IBM Containers command: &#x60;cf ic unpause &lt;container&gt;&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The unique identifier or name of the container that you want to unpause. Run &#x60;cf ic ps -a&#x60; or call the &#x60;GET /containers/json?all&#x3D;true&#x60; endpoint to review all containers in your space.
    :type name_or_id: str

    """
    return web.Response(status=200)
