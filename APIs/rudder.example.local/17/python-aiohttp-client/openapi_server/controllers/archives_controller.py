from typing import List, Dict
from aiohttp import web

from openapi_server.models.import200_response import Import200Response
from openapi_server import util


async def call_import(request: web.Request, archive=None, merge=None) -> web.Response:
    """Import a ZIP archive of policies into Rudder

    Import a ZIP archive of techniques, directives, groups and rules in a saved in a normalized format into Rudder

    :param archive: The ZIP archive file containing policies in a conventional layout and serialization format
    :type archive: str
    :param merge: Optional merge algo of the import. Default &#x60;override-all&#x60; means what is in the archive is the new reality. &#x60;keep-rule-groups&#x60; will keep existing target definition for existing rules (ignore archive value).
    :type merge: str

    """
    return web.Response(status=200)


async def export(request: web.Request, rules=None, directives=None, techniques=None, groups=None, include=None) -> web.Response:
    """Get a ZIP archive of the requested items and their dependencies

    Get a ZIP archive or rules, directives, techniques and groups with optionally their dependencies

    :param rules: IDs (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of rules to include
    :type rules: List[str]
    :param directives: IDs (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of directives to include
    :type directives: List[str]
    :param techniques: IDs, ie technique name/technique version (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of techniques to include
    :type techniques: List[str]
    :param groups: IDs (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of groups to include
    :type groups: List[str]
    :param include: Scope of dependencies to include in archive, where rule as directives and groups dependencies, directives have techniques dependencies, and techniques and groups don&#39;t have dependencies. &#39;none&#39; means no dependencies will be include, &#39;all&#39; means that the whole tree will,  &#39;directives&#39; and &#39;groups&#39; means to include them specifically, &#39;techniques&#39; means to include both directives and techniques.
    :type include: List[str]

    """
    return web.Response(status=200)
