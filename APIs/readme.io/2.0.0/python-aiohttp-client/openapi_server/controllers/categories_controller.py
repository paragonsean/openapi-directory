from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_category(request: web.Request, slug, x_readme_version) -> web.Response:
    """Get category

    Returns the category with this slug

    :param slug: Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \&quot;Getting Started\&quot;, enter the slug \&quot;getting-started\&quot;
    :type slug: str
    :param x_readme_version: Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    :type x_readme_version: str

    """
    return web.Response(status=200)


async def get_category_docs(request: web.Request, slug, x_readme_version) -> web.Response:
    """Get docs for category

    Returns the docs and children docs within this category

    :param slug: Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \&quot;Getting Started\&quot;, enter the slug \&quot;getting-started\&quot;
    :type slug: str
    :param x_readme_version: Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    :type x_readme_version: str

    """
    return web.Response(status=200)
