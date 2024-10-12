from typing import List, Dict
from aiohttp import web

from openapi_server.models.doc import Doc
from openapi_server import util


async def create_doc(request: web.Request, x_readme_version, body) -> web.Response:
    """Create doc

    Create a new doc inside of this project

    :param x_readme_version: Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    :type x_readme_version: str
    :param body: Doc object
    :type body: dict | bytes

    """
    body = Doc.from_dict(body)
    return web.Response(status=200)


async def delete_doc(request: web.Request, slug, x_readme_version) -> web.Response:
    """Delete doc

    Delete the doc with this slug

    :param slug: Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \&quot;New Features\&quot;, enter the slug \&quot;new-features\&quot;
    :type slug: str
    :param x_readme_version: Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    :type x_readme_version: str

    """
    return web.Response(status=200)


async def get_doc(request: web.Request, slug, x_readme_version) -> web.Response:
    """Get doc

    Returns the doc with this slug

    :param slug: Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \&quot;New Features\&quot;, enter the slug \&quot;new-features\&quot;
    :type slug: str
    :param x_readme_version: Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    :type x_readme_version: str

    """
    return web.Response(status=200)


async def search_docs(request: web.Request, search, x_readme_version) -> web.Response:
    """Search docs

    Returns all docs that match the search

    :param search: Search string to look for
    :type search: str
    :param x_readme_version: Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    :type x_readme_version: str

    """
    return web.Response(status=200)


async def update_doc(request: web.Request, slug, x_readme_version, body) -> web.Response:
    """Update doc

    Update a doc with this slug

    :param slug: Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \&quot;New Features\&quot;, enter the slug \&quot;new-features\&quot;
    :type slug: str
    :param x_readme_version: Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    :type x_readme_version: str
    :param body: Doc object
    :type body: dict | bytes

    """
    body = Doc.from_dict(body)
    return web.Response(status=200)
