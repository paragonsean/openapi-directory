from typing import List, Dict
from aiohttp import web

from openapi_server.models.assessments_metadata_list_default_response import AssessmentsMetadataListDefaultResponse
from openapi_server.models.security_assessment_metadata import SecurityAssessmentMetadata
from openapi_server.models.security_assessment_metadata_list import SecurityAssessmentMetadataList
from openapi_server import util


async def assessments_metadata_get(request: web.Request, api_version, assessment_metadata_name) -> web.Response:
    """assessments_metadata_get

    Get metadata information on an assessment type

    :param api_version: API version for the operation
    :type api_version: str
    :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type
    :type assessment_metadata_name: str

    """
    return web.Response(status=200)


async def assessments_metadata_list(request: web.Request, api_version) -> web.Response:
    """assessments_metadata_list

    Get metadata information on all assessment types

    :param api_version: API version for the operation
    :type api_version: str

    """
    return web.Response(status=200)


async def assessments_metadata_subscription_create(request: web.Request, api_version, assessment_metadata_name, subscription_id, assessment_metadata) -> web.Response:
    """assessments_metadata_subscription_create

    Create metadata information on an assessment type in a specific subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type
    :type assessment_metadata_name: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param assessment_metadata: AssessmentMetadata object
    :type assessment_metadata: dict | bytes

    """
    assessment_metadata = SecurityAssessmentMetadata.from_dict(assessment_metadata)
    return web.Response(status=200)


async def assessments_metadata_subscription_delete(request: web.Request, api_version, assessment_metadata_name, subscription_id) -> web.Response:
    """assessments_metadata_subscription_delete

    Delete metadata information on an assessment type in a specific subscription, will cause the deletion of all the assessments of that type in that subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type
    :type assessment_metadata_name: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)


async def assessments_metadata_subscription_get(request: web.Request, api_version, assessment_metadata_name, subscription_id) -> web.Response:
    """assessments_metadata_subscription_get

    Get metadata information on an assessment type in a specific subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type
    :type assessment_metadata_name: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)


async def assessments_metadata_subscription_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """assessments_metadata_subscription_list

    Get metadata information on all assessment types in a specific subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)
