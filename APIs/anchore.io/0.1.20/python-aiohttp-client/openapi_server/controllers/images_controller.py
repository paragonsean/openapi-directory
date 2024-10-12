from typing import List, Dict
from aiohttp import web

from openapi_server.models.anchore_image import AnchoreImage
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.content_files_response import ContentFilesResponse
from openapi_server.models.content_java_package_response import ContentJAVAPackageResponse
from openapi_server.models.content_malware_response import ContentMalwareResponse
from openapi_server.models.content_package_response import ContentPackageResponse
from openapi_server.models.delete_image_response import DeleteImageResponse
from openapi_server.models.image_analysis_request import ImageAnalysisRequest
from openapi_server.models.metadata_response import MetadataResponse
from openapi_server.models.vulnerability_response import VulnerabilityResponse
from openapi_server import util


async def add_image(request: web.Request, body, force=None, autosubscribe=None, x_anchore_account=None) -> web.Response:
    """Submit a new image for analysis by the engine

    Creates a new analysis task that is executed asynchronously

    :param body: 
    :type body: dict | bytes
    :param force: Override any existing entry in the system
    :type force: bool
    :param autosubscribe: Instruct engine to automatically begin watching the added tag for updates from registry
    :type autosubscribe: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    body = ImageAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def delete_image(request: web.Request, image_digest, force=None, x_anchore_account=None) -> web.Response:
    """Delete an image analysis

    

    :param image_digest: 
    :type image_digest: str
    :param force: 
    :type force: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def delete_image_by_image_id(request: web.Request, image_id, force=None, x_anchore_account=None) -> web.Response:
    """Delete image by docker imageId

    

    :param image_id: 
    :type image_id: str
    :param force: 
    :type force: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def delete_images_async(request: web.Request, image_digests, force=None, x_anchore_account=None) -> web.Response:
    """Bulk mark images for deletion

    Delete analysis for image digests in the list asynchronously

    :param image_digests: 
    :type image_digests: List[str]
    :param force: 
    :type force: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image(request: web.Request, image_digest, x_anchore_account=None) -> web.Response:
    """Get image metadata

    

    :param image_digest: 
    :type image_digest: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_by_image_id(request: web.Request, image_id, x_anchore_account=None) -> web.Response:
    """Lookup image by docker imageId

    

    :param image_id: 
    :type image_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_content_by_type(request: web.Request, image_digest, ctype, x_anchore_account=None) -> web.Response:
    """Get the content of an image by type

    

    :param image_digest: 
    :type image_digest: str
    :param ctype: 
    :type ctype: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_content_by_type_files(request: web.Request, image_digest, x_anchore_account=None) -> web.Response:
    """Get the content of an image by type files

    

    :param image_digest: 
    :type image_digest: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_content_by_type_image_id(request: web.Request, image_id, ctype, x_anchore_account=None) -> web.Response:
    """Get the content of an image by type

    

    :param image_id: 
    :type image_id: str
    :param ctype: 
    :type ctype: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_content_by_type_image_id_files(request: web.Request, image_id, x_anchore_account=None) -> web.Response:
    """Get the content of an image by type files

    

    :param image_id: 
    :type image_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_content_by_type_image_id_javapackage(request: web.Request, image_id, x_anchore_account=None) -> web.Response:
    """Get the content of an image by type java

    

    :param image_id: 
    :type image_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_content_by_type_javapackage(request: web.Request, image_digest, x_anchore_account=None) -> web.Response:
    """Get the content of an image by type java

    

    :param image_digest: 
    :type image_digest: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_content_by_type_malware(request: web.Request, image_digest, x_anchore_account=None) -> web.Response:
    """Get the content of an image by type malware

    

    :param image_digest: 
    :type image_digest: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_metadata_by_type(request: web.Request, image_digest, mtype, x_anchore_account=None) -> web.Response:
    """Get the metadata of an image by type

    

    :param image_digest: 
    :type image_digest: str
    :param mtype: 
    :type mtype: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_policy_check(request: web.Request, image_digest, tag, policy_id=None, detail=None, history=None, interactive=None, x_anchore_account=None) -> web.Response:
    """Check policy evaluation status for image

    Get the policy evaluation for the given image

    :param image_digest: 
    :type image_digest: str
    :param tag: 
    :type tag: str
    :param policy_id: 
    :type policy_id: str
    :param detail: 
    :type detail: bool
    :param history: 
    :type history: bool
    :param interactive: 
    :type interactive: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_policy_check_by_image_id(request: web.Request, image_id, tag, policy_id=None, detail=None, history=None, x_anchore_account=None) -> web.Response:
    """Check policy evaluation status for image

    Get the policy evaluation for the given image

    :param image_id: 
    :type image_id: str
    :param tag: 
    :type tag: str
    :param policy_id: 
    :type policy_id: str
    :param detail: 
    :type detail: bool
    :param history: 
    :type history: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_sbom_native(request: web.Request, image_digest, x_anchore_account=None) -> web.Response:
    """Get image sbom in the native Anchore format

    

    :param image_digest: 
    :type image_digest: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_vulnerabilities_by_type(request: web.Request, image_digest, vtype, force_refresh=None, vendor_only=None, x_anchore_account=None) -> web.Response:
    """Get vulnerabilities by type

    

    :param image_digest: 
    :type image_digest: str
    :param vtype: 
    :type vtype: str
    :param force_refresh: 
    :type force_refresh: bool
    :param vendor_only: Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data. When set to true, it will filter out all vulnerabilities where &#x60;will_not_fix&#x60; is False. If false all vulnerabilities are returned regardless of &#x60;will_not_fix&#x60;
    :type vendor_only: bool
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_vulnerabilities_by_type_image_id(request: web.Request, image_id, vtype, x_anchore_account=None) -> web.Response:
    """Get vulnerabilities by type

    

    :param image_id: 
    :type image_id: str
    :param vtype: 
    :type vtype: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_vulnerability_types(request: web.Request, image_digest, x_anchore_account=None) -> web.Response:
    """Get vulnerability types

    

    :param image_digest: 
    :type image_digest: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_image_vulnerability_types_by_image_id(request: web.Request, image_id, x_anchore_account=None) -> web.Response:
    """Get vulnerability types

    

    :param image_id: 
    :type image_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def list_image_content(request: web.Request, image_digest, x_anchore_account=None) -> web.Response:
    """List image content types

    

    :param image_digest: 
    :type image_digest: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def list_image_content_by_imageid(request: web.Request, image_id, x_anchore_account=None) -> web.Response:
    """List image content types

    

    :param image_id: 
    :type image_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def list_image_metadata(request: web.Request, image_digest, x_anchore_account=None) -> web.Response:
    """List image metadata types

    

    :param image_digest: 
    :type image_digest: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def list_images(request: web.Request, history=None, fulltag=None, image_status=None, analysis_status=None, x_anchore_account=None) -> web.Response:
    """List all visible images

    List all images visible to the user

    :param history: Include image history in the response
    :type history: bool
    :param fulltag: Full docker-pull string to filter results by (e.g. docker.io/library/nginx:latest, or myhost.com:5000/testimages:v1.1.1)
    :type fulltag: str
    :param image_status: Filter by image_status value on the record. Default if omitted is &#39;active&#39;.
    :type image_status: str
    :param analysis_status: Filter by analysis_status value on the record.
    :type analysis_status: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)
