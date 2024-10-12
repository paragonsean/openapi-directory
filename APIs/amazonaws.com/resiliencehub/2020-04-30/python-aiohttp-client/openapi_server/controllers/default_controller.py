from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_draft_app_version_resource_mappings_request import AddDraftAppVersionResourceMappingsRequest
from openapi_server.models.add_draft_app_version_resource_mappings_response import AddDraftAppVersionResourceMappingsResponse
from openapi_server.models.assessment_status import AssessmentStatus
from openapi_server.models.batch_update_recommendation_status_request import BatchUpdateRecommendationStatusRequest
from openapi_server.models.batch_update_recommendation_status_response import BatchUpdateRecommendationStatusResponse
from openapi_server.models.create_app_request import CreateAppRequest
from openapi_server.models.create_app_response import CreateAppResponse
from openapi_server.models.create_app_version_app_component_request import CreateAppVersionAppComponentRequest
from openapi_server.models.create_app_version_app_component_response import CreateAppVersionAppComponentResponse
from openapi_server.models.create_app_version_resource_request import CreateAppVersionResourceRequest
from openapi_server.models.create_app_version_resource_response import CreateAppVersionResourceResponse
from openapi_server.models.create_recommendation_template_request import CreateRecommendationTemplateRequest
from openapi_server.models.create_recommendation_template_response import CreateRecommendationTemplateResponse
from openapi_server.models.create_resiliency_policy_request import CreateResiliencyPolicyRequest
from openapi_server.models.create_resiliency_policy_response import CreateResiliencyPolicyResponse
from openapi_server.models.delete_app_assessment_request import DeleteAppAssessmentRequest
from openapi_server.models.delete_app_assessment_response import DeleteAppAssessmentResponse
from openapi_server.models.delete_app_input_source_request import DeleteAppInputSourceRequest
from openapi_server.models.delete_app_input_source_response import DeleteAppInputSourceResponse
from openapi_server.models.delete_app_request import DeleteAppRequest
from openapi_server.models.delete_app_response import DeleteAppResponse
from openapi_server.models.delete_app_version_app_component_request import DeleteAppVersionAppComponentRequest
from openapi_server.models.delete_app_version_app_component_response import DeleteAppVersionAppComponentResponse
from openapi_server.models.delete_app_version_resource_request import DeleteAppVersionResourceRequest
from openapi_server.models.delete_app_version_resource_response import DeleteAppVersionResourceResponse
from openapi_server.models.delete_recommendation_template_request import DeleteRecommendationTemplateRequest
from openapi_server.models.delete_recommendation_template_response import DeleteRecommendationTemplateResponse
from openapi_server.models.delete_resiliency_policy_request import DeleteResiliencyPolicyRequest
from openapi_server.models.delete_resiliency_policy_response import DeleteResiliencyPolicyResponse
from openapi_server.models.describe_app_assessment_request import DescribeAppAssessmentRequest
from openapi_server.models.describe_app_assessment_response import DescribeAppAssessmentResponse
from openapi_server.models.describe_app_request import DescribeAppRequest
from openapi_server.models.describe_app_response import DescribeAppResponse
from openapi_server.models.describe_app_version_app_component_request import DescribeAppVersionAppComponentRequest
from openapi_server.models.describe_app_version_app_component_response import DescribeAppVersionAppComponentResponse
from openapi_server.models.describe_app_version_request import DescribeAppVersionRequest
from openapi_server.models.describe_app_version_resource_request import DescribeAppVersionResourceRequest
from openapi_server.models.describe_app_version_resource_response import DescribeAppVersionResourceResponse
from openapi_server.models.describe_app_version_resources_resolution_status_request import DescribeAppVersionResourcesResolutionStatusRequest
from openapi_server.models.describe_app_version_resources_resolution_status_response import DescribeAppVersionResourcesResolutionStatusResponse
from openapi_server.models.describe_app_version_response import DescribeAppVersionResponse
from openapi_server.models.describe_app_version_template_request import DescribeAppVersionTemplateRequest
from openapi_server.models.describe_app_version_template_response import DescribeAppVersionTemplateResponse
from openapi_server.models.describe_draft_app_version_resources_import_status_response import DescribeDraftAppVersionResourcesImportStatusResponse
from openapi_server.models.describe_resiliency_policy_request import DescribeResiliencyPolicyRequest
from openapi_server.models.describe_resiliency_policy_response import DescribeResiliencyPolicyResponse
from openapi_server.models.import_resources_to_draft_app_version_request import ImportResourcesToDraftAppVersionRequest
from openapi_server.models.import_resources_to_draft_app_version_response import ImportResourcesToDraftAppVersionResponse
from openapi_server.models.list_alarm_recommendations_request import ListAlarmRecommendationsRequest
from openapi_server.models.list_alarm_recommendations_response import ListAlarmRecommendationsResponse
from openapi_server.models.list_app_assessment_compliance_drifts_request import ListAppAssessmentComplianceDriftsRequest
from openapi_server.models.list_app_assessment_compliance_drifts_response import ListAppAssessmentComplianceDriftsResponse
from openapi_server.models.list_app_assessments_response import ListAppAssessmentsResponse
from openapi_server.models.list_app_component_compliances_response import ListAppComponentCompliancesResponse
from openapi_server.models.list_app_component_recommendations_response import ListAppComponentRecommendationsResponse
from openapi_server.models.list_app_input_sources_request import ListAppInputSourcesRequest
from openapi_server.models.list_app_input_sources_response import ListAppInputSourcesResponse
from openapi_server.models.list_app_version_app_components_request import ListAppVersionAppComponentsRequest
from openapi_server.models.list_app_version_app_components_response import ListAppVersionAppComponentsResponse
from openapi_server.models.list_app_version_resource_mappings_request import ListAppVersionResourceMappingsRequest
from openapi_server.models.list_app_version_resource_mappings_response import ListAppVersionResourceMappingsResponse
from openapi_server.models.list_app_version_resources_request import ListAppVersionResourcesRequest
from openapi_server.models.list_app_version_resources_response import ListAppVersionResourcesResponse
from openapi_server.models.list_app_versions_request import ListAppVersionsRequest
from openapi_server.models.list_app_versions_response import ListAppVersionsResponse
from openapi_server.models.list_apps_response import ListAppsResponse
from openapi_server.models.list_recommendation_templates_response import ListRecommendationTemplatesResponse
from openapi_server.models.list_resiliency_policies_response import ListResiliencyPoliciesResponse
from openapi_server.models.list_sop_recommendations_response import ListSopRecommendationsResponse
from openapi_server.models.list_suggested_resiliency_policies_response import ListSuggestedResiliencyPoliciesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_test_recommendations_response import ListTestRecommendationsResponse
from openapi_server.models.list_unsupported_app_version_resources_response import ListUnsupportedAppVersionResourcesResponse
from openapi_server.models.publish_app_version_request import PublishAppVersionRequest
from openapi_server.models.publish_app_version_response import PublishAppVersionResponse
from openapi_server.models.put_draft_app_version_template_request import PutDraftAppVersionTemplateRequest
from openapi_server.models.put_draft_app_version_template_response import PutDraftAppVersionTemplateResponse
from openapi_server.models.recommendation_template_status import RecommendationTemplateStatus
from openapi_server.models.remove_draft_app_version_resource_mappings_request import RemoveDraftAppVersionResourceMappingsRequest
from openapi_server.models.remove_draft_app_version_resource_mappings_response import RemoveDraftAppVersionResourceMappingsResponse
from openapi_server.models.resolve_app_version_resources_response import ResolveAppVersionResourcesResponse
from openapi_server.models.start_app_assessment_request import StartAppAssessmentRequest
from openapi_server.models.start_app_assessment_response import StartAppAssessmentResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_app_request import UpdateAppRequest
from openapi_server.models.update_app_response import UpdateAppResponse
from openapi_server.models.update_app_version_app_component_request import UpdateAppVersionAppComponentRequest
from openapi_server.models.update_app_version_app_component_response import UpdateAppVersionAppComponentResponse
from openapi_server.models.update_app_version_request import UpdateAppVersionRequest
from openapi_server.models.update_app_version_resource_request import UpdateAppVersionResourceRequest
from openapi_server.models.update_app_version_resource_response import UpdateAppVersionResourceResponse
from openapi_server.models.update_app_version_response import UpdateAppVersionResponse
from openapi_server.models.update_resiliency_policy_request import UpdateResiliencyPolicyRequest
from openapi_server.models.update_resiliency_policy_response import UpdateResiliencyPolicyResponse
from openapi_server import util


async def add_draft_app_version_resource_mappings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_draft_app_version_resource_mappings

    Adds the resource mapping for the draft application version. You can also update an existing resource mapping to a new physical resource.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AddDraftAppVersionResourceMappingsRequest.from_dict(body)
    return web.Response(status=200)


async def batch_update_recommendation_status(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_update_recommendation_status

    Enables you to include or exclude one or more operational recommendations.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchUpdateRecommendationStatusRequest.from_dict(body)
    return web.Response(status=200)


async def create_app(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app

    &lt;p&gt;Creates an Resilience Hub application. An Resilience Hub application is a collection of Amazon Web Services resources structured to prevent and recover Amazon Web Services application disruptions. To describe a Resilience Hub application, you provide an application name, resources from one or more CloudFormation stacks, Resource Groups, Terraform state files, AppRegistry applications, and an appropriate resiliency policy. In addition, you can also add resources that are located on Amazon Elastic Kubernetes Service (Amazon EKS) clusters as optional resources. For more information about the number of resources supported per application, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/resiliencehub.html#limits_resiliencehub\&quot;&gt;Service quotas&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After you create an Resilience Hub application, you publish it so that you can run a resiliency assessment on it. You can then use recommendations from the assessment to improve resiliency by running another assessment, comparing results, and then iterating the process until you achieve your goals for recovery time objective (RTO) and recovery point objective (RPO).&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAppRequest.from_dict(body)
    return web.Response(status=200)


async def create_app_version_app_component(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_version_app_component

    &lt;p&gt;Creates a new Application Component in the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this Application Component for running assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAppVersionAppComponentRequest.from_dict(body)
    return web.Response(status=200)


async def create_app_version_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_app_version_resource

    &lt;p&gt;Adds a resource to the Resilience Hub application and assigns it to the specified Application Components. If you specify a new Application Component, Resilience Hub will automatically create the Application Component.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This action has no effect outside Resilience Hub.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To update application version with new &lt;code&gt;physicalResourceID&lt;/code&gt;, you must call &lt;code&gt;ResolveAppVersionResources&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateAppVersionResourceRequest.from_dict(body)
    return web.Response(status=200)


async def create_recommendation_template(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_recommendation_template

    Creates a new recommendation template for the Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateRecommendationTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_resiliency_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_resiliency_policy

    Creates a resiliency policy for an application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateResiliencyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_app(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app

    Deletes an Resilience Hub application. This is a destructive action that can&#39;t be undone.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteAppRequest.from_dict(body)
    return web.Response(status=200)


async def delete_app_assessment(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_assessment

    Deletes an Resilience Hub application assessment. This is a destructive action that can&#39;t be undone.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteAppAssessmentRequest.from_dict(body)
    return web.Response(status=200)


async def delete_app_input_source(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_input_source

    Deletes the input source and all of its imported resources from the Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteAppInputSourceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_app_version_app_component(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_version_app_component

    &lt;p&gt;Deletes an Application Component from the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this Application Component for running assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You will not be able to delete an Application Component if it has resources associated with it.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteAppVersionAppComponentRequest.from_dict(body)
    return web.Response(status=200)


async def delete_app_version_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_app_version_resource

    &lt;p&gt;Deletes a resource from the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can only delete a manually added resource. To exclude non-manually added resources, use the &lt;code&gt;UpdateAppVersionResource&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This action has no effect outside Resilience Hub.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteAppVersionResourceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_recommendation_template(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_recommendation_template

    Deletes a recommendation template. This is a destructive action that can&#39;t be undone.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteRecommendationTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_resiliency_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resiliency_policy

    Deletes a resiliency policy. This is a destructive action that can&#39;t be undone.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteResiliencyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def describe_app(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app

    Describes an Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAppRequest.from_dict(body)
    return web.Response(status=200)


async def describe_app_assessment(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_assessment

    Describes an assessment for an Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAppAssessmentRequest.from_dict(body)
    return web.Response(status=200)


async def describe_app_version(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_version

    Describes the Resilience Hub application version.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAppVersionRequest.from_dict(body)
    return web.Response(status=200)


async def describe_app_version_app_component(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_version_app_component

    Describes an Application Component in the Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAppVersionAppComponentRequest.from_dict(body)
    return web.Response(status=200)


async def describe_app_version_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_version_resource

    &lt;p&gt;Describes a resource of the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API accepts only one of the following parameters to descibe the resource:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;resourceName&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;logicalResourceId&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;physicalResourceId&lt;/code&gt; (Along with &lt;code&gt;physicalResourceId&lt;/code&gt;, you can also provide &lt;code&gt;awsAccountId&lt;/code&gt;, and &lt;code&gt;awsRegion&lt;/code&gt;)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAppVersionResourceRequest.from_dict(body)
    return web.Response(status=200)


async def describe_app_version_resources_resolution_status(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_version_resources_resolution_status

    Returns the resolution status for the specified resolution identifier for an application version. If &lt;code&gt;resolutionId&lt;/code&gt; is not specified, the current resolution status is returned.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAppVersionResourcesResolutionStatusRequest.from_dict(body)
    return web.Response(status=200)


async def describe_app_version_template(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_app_version_template

    Describes details about an Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAppVersionTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def describe_draft_app_version_resources_import_status(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_draft_app_version_resources_import_status

    &lt;p&gt;Describes the status of importing resources to an application version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you get a 404 error with &lt;code&gt;ResourceImportStatusNotFoundAppMetadataException&lt;/code&gt;, you must call &lt;code&gt;importResourcesToDraftAppVersion&lt;/code&gt; after creating the application and before calling &lt;code&gt;describeDraftAppVersionResourcesImportStatus&lt;/code&gt; to obtain the status.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAppRequest.from_dict(body)
    return web.Response(status=200)


async def describe_resiliency_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_resiliency_policy

    Describes a specified resiliency policy for an Resilience Hub application. The returned policy object includes creation time, data location constraints, the Amazon Resource Name (ARN) for the policy, tags, tier, and more.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeResiliencyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def import_resources_to_draft_app_version(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """import_resources_to_draft_app_version

    Imports resources to Resilience Hub application draft version from different input sources. For more information about the input sources supported by Resilience Hub, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html\&quot;&gt;Discover the structure and describe your Resilience Hub application&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ImportResourcesToDraftAppVersionRequest.from_dict(body)
    return web.Response(status=200)


async def list_alarm_recommendations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_alarm_recommendations

    Lists the alarm recommendations for an Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAlarmRecommendationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_app_assessment_compliance_drifts(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_app_assessment_compliance_drifts

    List of compliance drifts that were detected while running an assessment.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAppAssessmentComplianceDriftsRequest.from_dict(body)
    return web.Response(status=200)


async def list_app_assessments(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, app_arn=None, assessment_name=None, assessment_status=None, compliance_status=None, invoker=None, max_results=None, next_token=None, reverse_order=None) -> web.Response:
    """list_app_assessments

    Lists the assessments for an Resilience Hub application. You can use request parameters to refine the results for the response object.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param app_arn: Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide.
    :type app_arn: str
    :param assessment_name: The name for the assessment.
    :type assessment_name: str
    :param assessment_status: The current status of the assessment for the resiliency policy.
    :type assessment_status: list | bytes
    :param compliance_status: The current status of compliance for the resiliency policy.
    :type compliance_status: str
    :param invoker: Specifies the entity that invoked a specific assessment, either a &lt;code&gt;User&lt;/code&gt; or the &lt;code&gt;System&lt;/code&gt;.
    :type invoker: str
    :param max_results: Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved.
    :type max_results: int
    :param next_token: Null, or the token from a previous call to get the next set of results.
    :type next_token: str
    :param reverse_order: The default is to sort by ascending &lt;b&gt;startTime&lt;/b&gt;. To sort by descending &lt;b&gt;startTime&lt;/b&gt;, set reverseOrder to &lt;code&gt;true&lt;/code&gt;.
    :type reverse_order: bool

    """
    assessment_status = [AssessmentStatus.from_dict(d) for d in assessment_status]
    return web.Response(status=200)


async def list_app_component_compliances(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_app_component_compliances

    Lists the compliances for an Resilience Hub Application Component.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAlarmRecommendationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_app_component_recommendations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_app_component_recommendations

    Lists the recommendations for an Resilience Hub Application Component.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAlarmRecommendationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_app_input_sources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_app_input_sources

    Lists all the input sources of the Resilience Hub application. For more information about the input sources supported by Resilience Hub, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resilience-hub/latest/userguide/discover-structure.html\&quot;&gt;Discover the structure and describe your Resilience Hub application&lt;/a&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAppInputSourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_app_version_app_components(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_app_version_app_components

    Lists all the Application Components in the Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAppVersionAppComponentsRequest.from_dict(body)
    return web.Response(status=200)


async def list_app_version_resource_mappings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_app_version_resource_mappings

    Lists how the resources in an application version are mapped/sourced from. Mappings can be physical resource identifiers, CloudFormation stacks, resource-groups, or an application registry app.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAppVersionResourceMappingsRequest.from_dict(body)
    return web.Response(status=200)


async def list_app_version_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_app_version_resources

    Lists all the resources in an Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAppVersionResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_app_versions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_app_versions

    Lists the different versions for the Resilience Hub applications.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAppVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_apps(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, app_arn=None, max_results=None, name=None, next_token=None) -> web.Response:
    """list_apps

    &lt;p&gt;Lists your Resilience Hub applications.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can filter applications using only one filter at a time or without using any filter. If you try to filter applications using multiple filters, you will get the following error:&lt;/p&gt; &lt;p&gt; &lt;code&gt;An error occurred (ValidationException) when calling the ListApps operation: Only one filter is supported for this operation.&lt;/code&gt; &lt;/p&gt; &lt;/note&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param app_arn: Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide.
    :type app_arn: str
    :param max_results: Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved.
    :type max_results: int
    :param name: The name for the one of the listed applications.
    :type name: str
    :param next_token: Null, or the token from a previous call to get the next set of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_recommendation_templates(request: web.Request, assessment_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, name=None, next_token=None, recommendation_template_arn=None, reverse_order=None, status=None) -> web.Response:
    """list_recommendation_templates

    Lists the recommendation templates for the Resilience Hub applications.

    :param assessment_arn: Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app-assessment/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide.
    :type assessment_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved.
    :type max_results: int
    :param name: The name for one of the listed recommendation templates.
    :type name: str
    :param next_token: Null, or the token from a previous call to get the next set of results.
    :type next_token: str
    :param recommendation_template_arn: The Amazon Resource Name (ARN) for a recommendation template.
    :type recommendation_template_arn: str
    :param reverse_order: The default is to sort by ascending &lt;b&gt;startTime&lt;/b&gt;. To sort by descending &lt;b&gt;startTime&lt;/b&gt;, set reverseOrder to &lt;code&gt;true&lt;/code&gt;.
    :type reverse_order: bool
    :param status: Status of the action.
    :type status: list | bytes

    """
    status = [RecommendationTemplateStatus.from_dict(d) for d in status]
    return web.Response(status=200)


async def list_resiliency_policies(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, policy_name=None) -> web.Response:
    """list_resiliency_policies

    Lists the resiliency policies for the Resilience Hub applications.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved.
    :type max_results: int
    :param next_token: Null, or the token from a previous call to get the next set of results.
    :type next_token: str
    :param policy_name: The name of the policy
    :type policy_name: str

    """
    return web.Response(status=200)


async def list_sop_recommendations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_sop_recommendations

    Lists the standard operating procedure (SOP) recommendations for the Resilience Hub applications.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAlarmRecommendationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_suggested_resiliency_policies(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_suggested_resiliency_policies

    Lists the suggested resiliency policies for the Resilience Hub applications.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Maximum number of results to include in the response. If more results exist than the specified &lt;code&gt;MaxResults&lt;/code&gt; value, a token is included in the response so that the remaining results can be retrieved.
    :type max_results: int
    :param next_token: Null, or the token from a previous call to get the next set of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags for your resources in your Resilience Hub applications.

    :param resource_arn: The Amazon Resource Name (ARN) for a specific resource in your Resilience Hub application.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_test_recommendations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_test_recommendations

    Lists the test recommendations for the Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAlarmRecommendationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_unsupported_app_version_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_unsupported_app_version_resources

    Lists the resources that are not currently supported in Resilience Hub. An unsupported resource is a resource that exists in the object that was used to create an app, but is not supported by Resilience Hub.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAppVersionResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def publish_app_version(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """publish_app_version

    Publishes a new version of a specific Resilience Hub application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PublishAppVersionRequest.from_dict(body)
    return web.Response(status=200)


async def put_draft_app_version_template(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_draft_app_version_template

    Adds or updates the app template for an Resilience Hub application draft version.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutDraftAppVersionTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def remove_draft_app_version_resource_mappings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_draft_app_version_resource_mappings

    Removes resource mappings from a draft application version.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RemoveDraftAppVersionResourceMappingsRequest.from_dict(body)
    return web.Response(status=200)


async def resolve_app_version_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resolve_app_version_resources

    Resolves the resources for an application version.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeAppVersionTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def start_app_assessment(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_app_assessment

    Creates a new application assessment for an application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartAppAssessmentRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Applies one or more tags to a resource.

    :param resource_arn: Amazon Resource Name (ARN) of the resource. 
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes one or more tags from a resource.

    :param resource_arn: Amazon Resource Name (ARN) of the resource. 
    :type resource_arn: str
    :param tag_keys: The keys of the tags you want to remove.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_app(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app

    Updates an application.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAppRequest.from_dict(body)
    return web.Response(status=200)


async def update_app_version(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_version

    &lt;p&gt;Updates the Resilience Hub application version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this information for running resiliency assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAppVersionRequest.from_dict(body)
    return web.Response(status=200)


async def update_app_version_app_component(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_version_app_component

    &lt;p&gt;Updates an existing Application Component in the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this Application Component for running assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAppVersionAppComponentRequest.from_dict(body)
    return web.Response(status=200)


async def update_app_version_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_app_version_resource

    &lt;p&gt;Updates the resource details in the Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This action has no effect outside Resilience Hub.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;This API updates the Resilience Hub application draft version. To use this resource for running resiliency assessments, you must publish the Resilience Hub application using the &lt;code&gt;PublishAppVersion&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To update application version with new &lt;code&gt;physicalResourceID&lt;/code&gt;, you must call &lt;code&gt;ResolveAppVersionResources&lt;/code&gt; API.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAppVersionResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_resiliency_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_resiliency_policy

    Updates a resiliency policy.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateResiliencyPolicyRequest.from_dict(body)
    return web.Response(status=200)
