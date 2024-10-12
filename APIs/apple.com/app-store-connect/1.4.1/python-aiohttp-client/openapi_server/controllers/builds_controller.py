from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_encryption_declaration_response import AppEncryptionDeclarationResponse
from openapi_server.models.app_response import AppResponse
from openapi_server.models.app_store_version_response import AppStoreVersionResponse
from openapi_server.models.beta_app_review_submission_response import BetaAppReviewSubmissionResponse
from openapi_server.models.beta_build_localizations_response import BetaBuildLocalizationsResponse
from openapi_server.models.beta_testers_response import BetaTestersResponse
from openapi_server.models.build_app_encryption_declaration_linkage_request import BuildAppEncryptionDeclarationLinkageRequest
from openapi_server.models.build_app_encryption_declaration_linkage_response import BuildAppEncryptionDeclarationLinkageResponse
from openapi_server.models.build_beta_detail_response import BuildBetaDetailResponse
from openapi_server.models.build_beta_groups_linkages_request import BuildBetaGroupsLinkagesRequest
from openapi_server.models.build_icons_response import BuildIconsResponse
from openapi_server.models.build_individual_testers_linkages_request import BuildIndividualTestersLinkagesRequest
from openapi_server.models.build_individual_testers_linkages_response import BuildIndividualTestersLinkagesResponse
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.build_update_request import BuildUpdateRequest
from openapi_server.models.builds_response import BuildsResponse
from openapi_server.models.diagnostic_signatures_response import DiagnosticSignaturesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.perf_power_metrics_response import PerfPowerMetricsResponse
from openapi_server.models.prerelease_version_response import PrereleaseVersionResponse
from openapi_server import util


async def builds_app_encryption_declaration_get_to_one_related(request: web.Request, id, fields_app_encryption_declarations=None) -> web.Response:
    """builds_app_encryption_declaration_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_encryption_declarations: the fields to include for returned resources of type appEncryptionDeclarations
    :type fields_app_encryption_declarations: List[str]

    """
    return web.Response(status=200)


async def builds_app_encryption_declaration_get_to_one_relationship(request: web.Request, id) -> web.Response:
    """builds_app_encryption_declaration_get_to_one_relationship

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def builds_app_encryption_declaration_update_to_one_relationship(request: web.Request, id, body) -> web.Response:
    """builds_app_encryption_declaration_update_to_one_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: Related linkage
    :type body: dict | bytes

    """
    body = BuildAppEncryptionDeclarationLinkageRequest.from_dict(body)
    return web.Response(status=200)


async def builds_app_get_to_one_related(request: web.Request, id, fields_apps=None) -> web.Response:
    """builds_app_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def builds_app_store_version_get_to_one_related(request: web.Request, id, fields_app_store_versions=None) -> web.Response:
    """builds_app_store_version_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_versions: the fields to include for returned resources of type appStoreVersions
    :type fields_app_store_versions: List[str]

    """
    return web.Response(status=200)


async def builds_beta_app_review_submission_get_to_one_related(request: web.Request, id, fields_beta_app_review_submissions=None) -> web.Response:
    """builds_beta_app_review_submission_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_app_review_submissions: the fields to include for returned resources of type betaAppReviewSubmissions
    :type fields_beta_app_review_submissions: List[str]

    """
    return web.Response(status=200)


async def builds_beta_build_localizations_get_to_many_related(request: web.Request, id, fields_beta_build_localizations=None, limit=None) -> web.Response:
    """builds_beta_build_localizations_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_build_localizations: the fields to include for returned resources of type betaBuildLocalizations
    :type fields_beta_build_localizations: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def builds_beta_groups_create_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """builds_beta_groups_create_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BuildBetaGroupsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def builds_beta_groups_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """builds_beta_groups_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BuildBetaGroupsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def builds_build_beta_detail_get_to_one_related(request: web.Request, id, fields_build_beta_details=None) -> web.Response:
    """builds_build_beta_detail_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_build_beta_details: the fields to include for returned resources of type buildBetaDetails
    :type fields_build_beta_details: List[str]

    """
    return web.Response(status=200)


async def builds_diagnostic_signatures_get_to_many_related(request: web.Request, id, filter_diagnostic_type=None, fields_diagnostic_signatures=None, limit=None) -> web.Response:
    """builds_diagnostic_signatures_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_diagnostic_type: filter by attribute &#39;diagnosticType&#39;
    :type filter_diagnostic_type: List[str]
    :param fields_diagnostic_signatures: the fields to include for returned resources of type diagnosticSignatures
    :type fields_diagnostic_signatures: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def builds_get_collection(request: web.Request, filter_beta_app_review_submission_beta_review_state=None, filter_expired=None, filter_pre_release_version_platform=None, filter_pre_release_version_version=None, filter_processing_state=None, filter_uses_non_exempt_encryption=None, filter_version=None, filter_app=None, filter_app_store_version=None, filter_beta_groups=None, filter_pre_release_version=None, filter_id=None, sort=None, fields_builds=None, limit=None, include=None, fields_app_encryption_declarations=None, fields_beta_app_review_submissions=None, fields_build_beta_details=None, fields_build_icons=None, fields_perf_power_metrics=None, fields_pre_release_versions=None, fields_app_store_versions=None, fields_diagnostic_signatures=None, fields_beta_testers=None, fields_beta_build_localizations=None, fields_apps=None, limit_beta_build_localizations=None, limit_icons=None, limit_individual_testers=None) -> web.Response:
    """builds_get_collection

    

    :param filter_beta_app_review_submission_beta_review_state: filter by attribute &#39;betaAppReviewSubmission.betaReviewState&#39;
    :type filter_beta_app_review_submission_beta_review_state: List[str]
    :param filter_expired: filter by attribute &#39;expired&#39;
    :type filter_expired: List[str]
    :param filter_pre_release_version_platform: filter by attribute &#39;preReleaseVersion.platform&#39;
    :type filter_pre_release_version_platform: List[str]
    :param filter_pre_release_version_version: filter by attribute &#39;preReleaseVersion.version&#39;
    :type filter_pre_release_version_version: List[str]
    :param filter_processing_state: filter by attribute &#39;processingState&#39;
    :type filter_processing_state: List[str]
    :param filter_uses_non_exempt_encryption: filter by attribute &#39;usesNonExemptEncryption&#39;
    :type filter_uses_non_exempt_encryption: List[str]
    :param filter_version: filter by attribute &#39;version&#39;
    :type filter_version: List[str]
    :param filter_app: filter by id(s) of related &#39;app&#39;
    :type filter_app: List[str]
    :param filter_app_store_version: filter by id(s) of related &#39;appStoreVersion&#39;
    :type filter_app_store_version: List[str]
    :param filter_beta_groups: filter by id(s) of related &#39;betaGroups&#39;
    :type filter_beta_groups: List[str]
    :param filter_pre_release_version: filter by id(s) of related &#39;preReleaseVersion&#39;
    :type filter_pre_release_version: List[str]
    :param filter_id: filter by id(s)
    :type filter_id: List[str]
    :param sort: comma-separated list of sort expressions; resources will be sorted as specified
    :type sort: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_app_encryption_declarations: the fields to include for returned resources of type appEncryptionDeclarations
    :type fields_app_encryption_declarations: List[str]
    :param fields_beta_app_review_submissions: the fields to include for returned resources of type betaAppReviewSubmissions
    :type fields_beta_app_review_submissions: List[str]
    :param fields_build_beta_details: the fields to include for returned resources of type buildBetaDetails
    :type fields_build_beta_details: List[str]
    :param fields_build_icons: the fields to include for returned resources of type buildIcons
    :type fields_build_icons: List[str]
    :param fields_perf_power_metrics: the fields to include for returned resources of type perfPowerMetrics
    :type fields_perf_power_metrics: List[str]
    :param fields_pre_release_versions: the fields to include for returned resources of type preReleaseVersions
    :type fields_pre_release_versions: List[str]
    :param fields_app_store_versions: the fields to include for returned resources of type appStoreVersions
    :type fields_app_store_versions: List[str]
    :param fields_diagnostic_signatures: the fields to include for returned resources of type diagnosticSignatures
    :type fields_diagnostic_signatures: List[str]
    :param fields_beta_testers: the fields to include for returned resources of type betaTesters
    :type fields_beta_testers: List[str]
    :param fields_beta_build_localizations: the fields to include for returned resources of type betaBuildLocalizations
    :type fields_beta_build_localizations: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_beta_build_localizations: maximum number of related betaBuildLocalizations returned (when they are included)
    :type limit_beta_build_localizations: int
    :param limit_icons: maximum number of related icons returned (when they are included)
    :type limit_icons: int
    :param limit_individual_testers: maximum number of related individualTesters returned (when they are included)
    :type limit_individual_testers: int

    """
    return web.Response(status=200)


async def builds_get_instance(request: web.Request, id, fields_builds=None, include=None, fields_app_encryption_declarations=None, fields_beta_app_review_submissions=None, fields_build_beta_details=None, fields_build_icons=None, fields_perf_power_metrics=None, fields_pre_release_versions=None, fields_app_store_versions=None, fields_diagnostic_signatures=None, fields_beta_testers=None, fields_beta_build_localizations=None, fields_apps=None, limit_beta_build_localizations=None, limit_icons=None, limit_individual_testers=None) -> web.Response:
    """builds_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_app_encryption_declarations: the fields to include for returned resources of type appEncryptionDeclarations
    :type fields_app_encryption_declarations: List[str]
    :param fields_beta_app_review_submissions: the fields to include for returned resources of type betaAppReviewSubmissions
    :type fields_beta_app_review_submissions: List[str]
    :param fields_build_beta_details: the fields to include for returned resources of type buildBetaDetails
    :type fields_build_beta_details: List[str]
    :param fields_build_icons: the fields to include for returned resources of type buildIcons
    :type fields_build_icons: List[str]
    :param fields_perf_power_metrics: the fields to include for returned resources of type perfPowerMetrics
    :type fields_perf_power_metrics: List[str]
    :param fields_pre_release_versions: the fields to include for returned resources of type preReleaseVersions
    :type fields_pre_release_versions: List[str]
    :param fields_app_store_versions: the fields to include for returned resources of type appStoreVersions
    :type fields_app_store_versions: List[str]
    :param fields_diagnostic_signatures: the fields to include for returned resources of type diagnosticSignatures
    :type fields_diagnostic_signatures: List[str]
    :param fields_beta_testers: the fields to include for returned resources of type betaTesters
    :type fields_beta_testers: List[str]
    :param fields_beta_build_localizations: the fields to include for returned resources of type betaBuildLocalizations
    :type fields_beta_build_localizations: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]
    :param limit_beta_build_localizations: maximum number of related betaBuildLocalizations returned (when they are included)
    :type limit_beta_build_localizations: int
    :param limit_icons: maximum number of related icons returned (when they are included)
    :type limit_icons: int
    :param limit_individual_testers: maximum number of related individualTesters returned (when they are included)
    :type limit_individual_testers: int

    """
    return web.Response(status=200)


async def builds_icons_get_to_many_related(request: web.Request, id, fields_build_icons=None, limit=None) -> web.Response:
    """builds_icons_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_build_icons: the fields to include for returned resources of type buildIcons
    :type fields_build_icons: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def builds_individual_testers_create_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """builds_individual_testers_create_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BuildIndividualTestersLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def builds_individual_testers_delete_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """builds_individual_testers_delete_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = BuildIndividualTestersLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def builds_individual_testers_get_to_many_related(request: web.Request, id, fields_beta_testers=None, limit=None) -> web.Response:
    """builds_individual_testers_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_testers: the fields to include for returned resources of type betaTesters
    :type fields_beta_testers: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def builds_individual_testers_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """builds_individual_testers_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def builds_perf_power_metrics_get_to_many_related(request: web.Request, id, filter_device_type=None, filter_metric_type=None, filter_platform=None) -> web.Response:
    """builds_perf_power_metrics_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_device_type: filter by attribute &#39;deviceType&#39;
    :type filter_device_type: List[str]
    :param filter_metric_type: filter by attribute &#39;metricType&#39;
    :type filter_metric_type: List[str]
    :param filter_platform: filter by attribute &#39;platform&#39;
    :type filter_platform: List[str]

    """
    return web.Response(status=200)


async def builds_pre_release_version_get_to_one_related(request: web.Request, id, fields_pre_release_versions=None) -> web.Response:
    """builds_pre_release_version_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_pre_release_versions: the fields to include for returned resources of type preReleaseVersions
    :type fields_pre_release_versions: List[str]

    """
    return web.Response(status=200)


async def builds_update_instance(request: web.Request, id, body) -> web.Response:
    """builds_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: Build representation
    :type body: dict | bytes

    """
    body = BuildUpdateRequest.from_dict(body)
    return web.Response(status=200)
