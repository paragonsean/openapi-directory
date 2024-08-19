from typing import List, Dict
from aiohttp import web

from openapi_server.models.regulatory_compliance_assessment import RegulatoryComplianceAssessment
from openapi_server.models.regulatory_compliance_assessment_list import RegulatoryComplianceAssessmentList
from openapi_server.models.regulatory_compliance_control import RegulatoryComplianceControl
from openapi_server.models.regulatory_compliance_control_list import RegulatoryComplianceControlList
from openapi_server.models.regulatory_compliance_standard import RegulatoryComplianceStandard
from openapi_server.models.regulatory_compliance_standard_list import RegulatoryComplianceStandardList
from openapi_server.models.regulatory_compliance_standards_list_default_response import RegulatoryComplianceStandardsListDefaultResponse
from openapi_server import util


async def regulatory_compliance_assessments_get(request: web.Request, api_version, subscription_id, regulatory_compliance_standard_name, regulatory_compliance_control_name, regulatory_compliance_assessment_name) -> web.Response:
    """regulatory_compliance_assessments_get

    Supported regulatory compliance details and state for selected assessment

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param regulatory_compliance_standard_name: Name of the regulatory compliance standard object
    :type regulatory_compliance_standard_name: str
    :param regulatory_compliance_control_name: Name of the regulatory compliance control object
    :type regulatory_compliance_control_name: str
    :param regulatory_compliance_assessment_name: Name of the regulatory compliance assessment object
    :type regulatory_compliance_assessment_name: str

    """
    return web.Response(status=200)


async def regulatory_compliance_assessments_list(request: web.Request, api_version, subscription_id, regulatory_compliance_standard_name, regulatory_compliance_control_name, filter=None) -> web.Response:
    """regulatory_compliance_assessments_list

    Details and state of assessments mapped to selected regulatory compliance control

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param regulatory_compliance_standard_name: Name of the regulatory compliance standard object
    :type regulatory_compliance_standard_name: str
    :param regulatory_compliance_control_name: Name of the regulatory compliance control object
    :type regulatory_compliance_control_name: str
    :param filter: OData filter. Optional.
    :type filter: str

    """
    return web.Response(status=200)


async def regulatory_compliance_controls_get(request: web.Request, api_version, subscription_id, regulatory_compliance_standard_name, regulatory_compliance_control_name) -> web.Response:
    """regulatory_compliance_controls_get

    Selected regulatory compliance control details and state

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param regulatory_compliance_standard_name: Name of the regulatory compliance standard object
    :type regulatory_compliance_standard_name: str
    :param regulatory_compliance_control_name: Name of the regulatory compliance control object
    :type regulatory_compliance_control_name: str

    """
    return web.Response(status=200)


async def regulatory_compliance_controls_list(request: web.Request, api_version, subscription_id, regulatory_compliance_standard_name, filter=None) -> web.Response:
    """regulatory_compliance_controls_list

    All supported regulatory compliance controls details and state for selected standard

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param regulatory_compliance_standard_name: Name of the regulatory compliance standard object
    :type regulatory_compliance_standard_name: str
    :param filter: OData filter. Optional.
    :type filter: str

    """
    return web.Response(status=200)


async def regulatory_compliance_standards_get(request: web.Request, api_version, subscription_id, regulatory_compliance_standard_name) -> web.Response:
    """regulatory_compliance_standards_get

    Supported regulatory compliance details state for selected standard

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param regulatory_compliance_standard_name: Name of the regulatory compliance standard object
    :type regulatory_compliance_standard_name: str

    """
    return web.Response(status=200)


async def regulatory_compliance_standards_list(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """regulatory_compliance_standards_list

    Supported regulatory compliance standards details and state

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param filter: OData filter. Optional.
    :type filter: str

    """
    return web.Response(status=200)
