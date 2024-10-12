from typing import List, Dict
from aiohttp import web

from openapi_server.models.analysis_archive_add_result import AnalysisArchiveAddResult
from openapi_server.models.analysis_archive_transition_rule import AnalysisArchiveTransitionRule
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.archive_summary import ArchiveSummary
from openapi_server.models.archived_analysis import ArchivedAnalysis
from openapi_server import util


async def archive_image_analysis(request: web.Request, body) -> web.Response:
    """archive_image_analysis

    

    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def create_analysis_archive_rule(request: web.Request, body) -> web.Response:
    """create_analysis_archive_rule

    

    :param body: 
    :type body: dict | bytes

    """
    body = AnalysisArchiveTransitionRule.from_dict(body)
    return web.Response(status=200)


async def delete_analysis_archive_rule(request: web.Request, rule_id) -> web.Response:
    """delete_analysis_archive_rule

    

    :param rule_id: 
    :type rule_id: str

    """
    return web.Response(status=200)


async def delete_archived_analysis(request: web.Request, image_digest, force=None) -> web.Response:
    """delete_archived_analysis

    Performs a synchronous archive deletion

    :param image_digest: 
    :type image_digest: str
    :param force: 
    :type force: bool

    """
    return web.Response(status=200)


async def get_analysis_archive_rule(request: web.Request, rule_id) -> web.Response:
    """get_analysis_archive_rule

    

    :param rule_id: 
    :type rule_id: str

    """
    return web.Response(status=200)


async def get_archived_analysis(request: web.Request, image_digest) -> web.Response:
    """get_archived_analysis

    Returns the archive metadata record identifying the image and tags for the analysis in the archive.

    :param image_digest: The image digest to identify the image analysis
    :type image_digest: str

    """
    return web.Response(status=200)


async def list_analysis_archive(request: web.Request, ) -> web.Response:
    """list_analysis_archive

    


    """
    return web.Response(status=200)


async def list_analysis_archive_rules(request: web.Request, system_global=None) -> web.Response:
    """list_analysis_archive_rules

    

    :param system_global: If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals
    :type system_global: bool

    """
    return web.Response(status=200)


async def list_archives(request: web.Request, ) -> web.Response:
    """list_archives

    


    """
    return web.Response(status=200)
