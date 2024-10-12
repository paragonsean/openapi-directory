from typing import List, Dict
from aiohttp import web

from openapi_server.models.image_detail import ImageDetail
from openapi_server.models.image_info import ImageInfo
from openapi_server import util


async def build_post(request: web.Request, x_auth_token, x_auth_project_id, t, body, q=None, nocache=None, pull=None) -> web.Response:
    """Build a Docker image from a Dockerfile

    This API builds a new container image from a Dockerfile that is stored on your local machine and pushes the image to the private Bluemix registry (corresponding IBM Containers command: &#x60;cf ic build&#x60;).   To push an image to your Bluemix registry, a namespace must be set for the organization. Run &#x60;cf ic namespace get&#x60; or call the &#x60;GET /registry/namespaces&#x60; API to check if a namespace is already set. If not, run &#x60;cf ic namespace set NAMESPACE&#x60; or call the &#x60;PUT /registry/namespaces/{namespace}&#x60; API to set a namespace for your organization.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param t: Tag the image with the full path to your private Bluemix registry in the following format: &#x60;t&#x3D;registry.ng.bluemix.net/&lt;namespace&gt;/&lt;image_name&gt;:&lt;tag&gt;&#x60;. This path is used to push the image to the private Bluemix registry after it is built.
    :type t: str
    :param body: Must be the content of a tar archive compressed with gzip. The archive must include a file called &#39;Dockerfile&#39; at its root. It may include any number of other files which will be accessible in the build context.
    :type body: str
    :param q: You can choose whether or not to show the verbose build output to review every step during the container image build. If you set the query parameter to &#x60;q&#x3D;false&#x60;, &#x60;q&#x3D;False&#x60;, or &#x60;q&#x3D;0&#x60;, the verbose build output is suppressed. To show the verbose build output, enter &#x60;q&#x3D;true&#x60;, &#x60;q&#x3D;True&#x60;, or &#x60;q&#x3D;1&#x60;.
    :type q: bool
    :param nocache: If you set the query parameter to &#x60;nocache&#x3D;true&#x60;, &#x60;nocache&#x3D;True&#x60;, or &#x60;nocache&#x3D;1&#x60;, the cache will not be used to build your image. To use the cache, enter &#x60;nocache&#x3D;false&#x60;, &#x60;nocache&#x3D;False&#x60;, or &#x60;nocache&#x3D;0&#x60;.
    :type nocache: bool
    :param pull: If set to pull&#x3D;true, pull&#x3D;True, or pull&#x3D;1, then a newer version of the image is always attempted to be pulled even though an older version of the image exists locally. If set to pull&#x3D;false, pull&#x3D;False, or pull&#x3D;0, then the local image will be used if one exists.
    :type pull: bool

    """
    return web.Response(status=200)


async def images_id_delete(request: web.Request, x_auth_token, x_auth_project_id, id) -> web.Response:
    """Remove a Docker image.

    Remove a Docker image from the private Bluemix registry that is identified by the image ID (corresponding IBM Containers command: &#x60;cf ic rmi &lt;image&gt;&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param id: The unique identifier representing a Docker image. Run &#x60;cf ic images&#x60;, or call the &#x60;GET /images/json&#x60; endpoint to review the Docker images that are available in your private Bluemix registry.
    :type id: str

    """
    return web.Response(status=200)


async def images_json_get(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """List all Docker images that are available in your private Bluemix registry.

    This endpoint returns a list of all available Docker images in a private Bluemix registry (corresponding IBM Containers command: &#x60;cf ic images&#x60;.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)


async def images_name_or_id_json_get(request: web.Request, x_auth_token, x_auth_project_id, name_or_id) -> web.Response:
    """Inspect a Docker image in private Bluemix registry

    This endpoint returns detailed information about a Docker image that is stored in the private Bluemix registry of an organization (corresponding IBM Containers command: &#x60;cf ic inspect &lt;image_name_or_id&gt;&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The full private Bluemix registry path to your image or the unique ID of the image that you want to inspect. Run &#x60;cf ic images&#x60; or call the &#x60;GET /images/json&#x60; endpoint to review the images in your private Bluemix registry. 
    :type name_or_id: str

    """
    return web.Response(status=200)
