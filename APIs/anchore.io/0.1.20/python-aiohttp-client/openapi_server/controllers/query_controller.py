from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.paginated_image_list import PaginatedImageList
from openapi_server.models.paginated_vulnerability_list import PaginatedVulnerabilityList
from openapi_server.models.paginated_vulnerable_image_list import PaginatedVulnerableImageList
from openapi_server import util


async def query_images_by_package(request: web.Request, name, package_type=None, version=None, page=None, limit=None, x_anchore_account=None) -> web.Response:
    """List of images containing given package

    Filterable query interface to search for images containing specified package

    :param name: Name of package to search for (e.g. sed)
    :type name: str
    :param package_type: Type of package to filter on (e.g. dpkg)
    :type package_type: str
    :param version: Version of named package to filter on (e.g. 4.4-1)
    :type version: str
    :param page: The page of results to fetch. Pages start at 1
    :type page: str
    :param limit: Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
    :type limit: int
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def query_images_by_vulnerability(request: web.Request, vulnerability_id, namespace=None, affected_package=None, severity=None, vendor_only=None, page=None, limit=None, x_anchore_account=None) -> web.Response:
    """List images vulnerable to the specific vulnerability ID.

    Returns a listing of images and their respective packages vulnerable to the given vulnerability ID

    :param vulnerability_id: The ID of the vulnerability to search for within all images stored in anchore-engine (e.g. CVE-1999-0001)
    :type vulnerability_id: str
    :param namespace: Filter results to images within the given vulnerability namespace (e.g. debian:8, ubuntu:14.04)
    :type namespace: str
    :param affected_package: Filter results to images with vulnable packages with the given package name (e.g. libssl)
    :type affected_package: str
    :param severity: Filter results to vulnerable package/vulnerability with the given severity
    :type severity: str
    :param vendor_only: Filter results to include only vulnerabilities that are not marked as invalid by upstream OS vendor data
    :type vendor_only: bool
    :param page: The page of results to fetch. Pages start at 1
    :type page: int
    :param limit: Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
    :type limit: int
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def query_vulnerabilities(request: web.Request, id, affected_package=None, affected_package_version=None, page=None, limit=None, namespace=None) -> web.Response:
    """Listing information about given vulnerability

    List (w/filters) vulnerability records known by the system, with affected packages information if present

    :param id: The ID of the vulnerability (e.g. CVE-1999-0001)
    :type id: List[str]
    :param affected_package: Filter results by specified package name (e.g. sed)
    :type affected_package: str
    :param affected_package_version: Filter results by specified package version (e.g. 4.4-1)
    :type affected_package_version: str
    :param page: The page of results to fetch. Pages start at 1
    :type page: str
    :param limit: Limit the number of records for the requested page. If omitted or set to 0, return all results in a single page
    :type limit: int
    :param namespace: Namespace(s) to filter vulnerability records by
    :type namespace: List[str]

    """
    return web.Response(status=200)
