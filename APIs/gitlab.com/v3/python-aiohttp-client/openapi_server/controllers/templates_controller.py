from typing import List, Dict
from aiohttp import web

from openapi_server.models.repo_license import RepoLicense
from openapi_server.models.template import Template
from openapi_server.models.templates_list import TemplatesList
from openapi_server import util


async def get_v3_templates_dockerfiles(request: web.Request, ) -> web.Response:
    """Get the list of the available template

    This feature was introduced in GitLab 8.15.


    """
    return web.Response(status=200)


async def get_v3_templates_dockerfiles_name(request: web.Request, name) -> web.Response:
    """Get the text for a specific template present in local filesystem

    This feature was introduced in GitLab 8.15.

    :param name: The name of the template
    :type name: str

    """
    return web.Response(status=200)


async def get_v3_templates_gitignores(request: web.Request, ) -> web.Response:
    """Get the list of the available template

    This feature was introduced in GitLab 8.8.


    """
    return web.Response(status=200)


async def get_v3_templates_gitignores_name(request: web.Request, name) -> web.Response:
    """Get the text for a specific template present in local filesystem

    This feature was introduced in GitLab 8.8.

    :param name: The name of the template
    :type name: str

    """
    return web.Response(status=200)


async def get_v3_templates_gitlab_ci_ymls(request: web.Request, ) -> web.Response:
    """Get the list of the available template

    This feature was introduced in GitLab 8.9.


    """
    return web.Response(status=200)


async def get_v3_templates_gitlab_ci_ymls_name(request: web.Request, name) -> web.Response:
    """Get the text for a specific template present in local filesystem

    This feature was introduced in GitLab 8.9.

    :param name: The name of the template
    :type name: str

    """
    return web.Response(status=200)


async def get_v3_templates_licenses(request: web.Request, popular=None) -> web.Response:
    """Get the list of the available license template

    This feature was introduced in GitLab 8.7.

    :param popular: If passed, returns only popular licenses
    :type popular: bool

    """
    return web.Response(status=200)


async def get_v3_templates_licenses_name(request: web.Request, name) -> web.Response:
    """Get the text for a specific license

    This feature was introduced in GitLab 8.7.

    :param name: The name of the template
    :type name: str

    """
    return web.Response(status=200)
