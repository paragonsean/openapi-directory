from typing import List, Dict
from aiohttp import web

from openapi_server.models.age_rating_declaration_response import AgeRatingDeclarationResponse
from openapi_server.models.app_store_review_detail_response import AppStoreReviewDetailResponse
from openapi_server.models.app_store_version_build_linkage_request import AppStoreVersionBuildLinkageRequest
from openapi_server.models.app_store_version_build_linkage_response import AppStoreVersionBuildLinkageResponse
from openapi_server.models.app_store_version_create_request import AppStoreVersionCreateRequest
from openapi_server.models.app_store_version_localizations_response import AppStoreVersionLocalizationsResponse
from openapi_server.models.app_store_version_phased_release_response import AppStoreVersionPhasedReleaseResponse
from openapi_server.models.app_store_version_response import AppStoreVersionResponse
from openapi_server.models.app_store_version_submission_response import AppStoreVersionSubmissionResponse
from openapi_server.models.app_store_version_update_request import AppStoreVersionUpdateRequest
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.idfa_declaration_response import IdfaDeclarationResponse
from openapi_server.models.routing_app_coverage_response import RoutingAppCoverageResponse
from openapi_server import util


async def app_store_versions_age_rating_declaration_get_to_one_related(request: web.Request, id, fields_age_rating_declarations=None) -> web.Response:
    """app_store_versions_age_rating_declaration_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_age_rating_declarations: the fields to include for returned resources of type ageRatingDeclarations
    :type fields_age_rating_declarations: List[str]

    """
    return web.Response(status=200)


async def app_store_versions_app_store_review_detail_get_to_one_related(request: web.Request, id, fields_app_store_review_details=None, fields_app_store_versions=None, fields_app_store_review_attachments=None, include=None) -> web.Response:
    """app_store_versions_app_store_review_detail_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_review_details: the fields to include for returned resources of type appStoreReviewDetails
    :type fields_app_store_review_details: List[str]
    :param fields_app_store_versions: the fields to include for returned resources of type appStoreVersions
    :type fields_app_store_versions: List[str]
    :param fields_app_store_review_attachments: the fields to include for returned resources of type appStoreReviewAttachments
    :type fields_app_store_review_attachments: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_store_versions_app_store_version_localizations_get_to_many_related(request: web.Request, id, fields_app_store_version_localizations=None, limit=None) -> web.Response:
    """app_store_versions_app_store_version_localizations_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_version_localizations: the fields to include for returned resources of type appStoreVersionLocalizations
    :type fields_app_store_version_localizations: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def app_store_versions_app_store_version_phased_release_get_to_one_related(request: web.Request, id, fields_app_store_version_phased_releases=None) -> web.Response:
    """app_store_versions_app_store_version_phased_release_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_version_phased_releases: the fields to include for returned resources of type appStoreVersionPhasedReleases
    :type fields_app_store_version_phased_releases: List[str]

    """
    return web.Response(status=200)


async def app_store_versions_app_store_version_submission_get_to_one_related(request: web.Request, id, fields_app_store_versions=None, fields_app_store_version_submissions=None, include=None) -> web.Response:
    """app_store_versions_app_store_version_submission_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_versions: the fields to include for returned resources of type appStoreVersions
    :type fields_app_store_versions: List[str]
    :param fields_app_store_version_submissions: the fields to include for returned resources of type appStoreVersionSubmissions
    :type fields_app_store_version_submissions: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_store_versions_build_get_to_one_related(request: web.Request, id, fields_builds=None) -> web.Response:
    """app_store_versions_build_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)


async def app_store_versions_build_get_to_one_relationship(request: web.Request, id) -> web.Response:
    """app_store_versions_build_get_to_one_relationship

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_store_versions_build_update_to_one_relationship(request: web.Request, id, body) -> web.Response:
    """app_store_versions_build_update_to_one_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: Related linkage
    :type body: dict | bytes

    """
    body = AppStoreVersionBuildLinkageRequest.from_dict(body)
    return web.Response(status=200)


async def app_store_versions_create_instance(request: web.Request, body) -> web.Response:
    """app_store_versions_create_instance

    

    :param body: AppStoreVersion representation
    :type body: dict | bytes

    """
    body = AppStoreVersionCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_store_versions_delete_instance(request: web.Request, id) -> web.Response:
    """app_store_versions_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_store_versions_get_instance(request: web.Request, id, fields_app_store_versions=None, include=None, fields_app_store_version_localizations=None, fields_idfa_declarations=None, fields_routing_app_coverages=None, fields_app_store_version_phased_releases=None, fields_age_rating_declarations=None, fields_app_store_review_details=None, fields_builds=None, fields_app_store_version_submissions=None, limit_app_store_version_localizations=None) -> web.Response:
    """app_store_versions_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_versions: the fields to include for returned resources of type appStoreVersions
    :type fields_app_store_versions: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_app_store_version_localizations: the fields to include for returned resources of type appStoreVersionLocalizations
    :type fields_app_store_version_localizations: List[str]
    :param fields_idfa_declarations: the fields to include for returned resources of type idfaDeclarations
    :type fields_idfa_declarations: List[str]
    :param fields_routing_app_coverages: the fields to include for returned resources of type routingAppCoverages
    :type fields_routing_app_coverages: List[str]
    :param fields_app_store_version_phased_releases: the fields to include for returned resources of type appStoreVersionPhasedReleases
    :type fields_app_store_version_phased_releases: List[str]
    :param fields_age_rating_declarations: the fields to include for returned resources of type ageRatingDeclarations
    :type fields_age_rating_declarations: List[str]
    :param fields_app_store_review_details: the fields to include for returned resources of type appStoreReviewDetails
    :type fields_app_store_review_details: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param fields_app_store_version_submissions: the fields to include for returned resources of type appStoreVersionSubmissions
    :type fields_app_store_version_submissions: List[str]
    :param limit_app_store_version_localizations: maximum number of related appStoreVersionLocalizations returned (when they are included)
    :type limit_app_store_version_localizations: int

    """
    return web.Response(status=200)


async def app_store_versions_idfa_declaration_get_to_one_related(request: web.Request, id, fields_idfa_declarations=None) -> web.Response:
    """app_store_versions_idfa_declaration_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_idfa_declarations: the fields to include for returned resources of type idfaDeclarations
    :type fields_idfa_declarations: List[str]

    """
    return web.Response(status=200)


async def app_store_versions_routing_app_coverage_get_to_one_related(request: web.Request, id, fields_routing_app_coverages=None) -> web.Response:
    """app_store_versions_routing_app_coverage_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_routing_app_coverages: the fields to include for returned resources of type routingAppCoverages
    :type fields_routing_app_coverages: List[str]

    """
    return web.Response(status=200)


async def app_store_versions_update_instance(request: web.Request, id, body) -> web.Response:
    """app_store_versions_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppStoreVersion representation
    :type body: dict | bytes

    """
    body = AppStoreVersionUpdateRequest.from_dict(body)
    return web.Response(status=200)
