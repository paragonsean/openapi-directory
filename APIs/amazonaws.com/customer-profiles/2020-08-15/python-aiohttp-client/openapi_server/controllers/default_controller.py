from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_profile_key_request import AddProfileKeyRequest
from openapi_server.models.add_profile_key_response import AddProfileKeyResponse
from openapi_server.models.create_calculated_attribute_definition_request import CreateCalculatedAttributeDefinitionRequest
from openapi_server.models.create_calculated_attribute_definition_response import CreateCalculatedAttributeDefinitionResponse
from openapi_server.models.create_domain_request import CreateDomainRequest
from openapi_server.models.create_domain_response import CreateDomainResponse
from openapi_server.models.create_event_stream_request import CreateEventStreamRequest
from openapi_server.models.create_event_stream_response import CreateEventStreamResponse
from openapi_server.models.create_integration_workflow_request import CreateIntegrationWorkflowRequest
from openapi_server.models.create_integration_workflow_response import CreateIntegrationWorkflowResponse
from openapi_server.models.create_profile_request import CreateProfileRequest
from openapi_server.models.create_profile_response import CreateProfileResponse
from openapi_server.models.delete_domain_response import DeleteDomainResponse
from openapi_server.models.delete_integration_request import DeleteIntegrationRequest
from openapi_server.models.delete_integration_response import DeleteIntegrationResponse
from openapi_server.models.delete_profile_key_request import DeleteProfileKeyRequest
from openapi_server.models.delete_profile_key_response import DeleteProfileKeyResponse
from openapi_server.models.delete_profile_object_request import DeleteProfileObjectRequest
from openapi_server.models.delete_profile_object_response import DeleteProfileObjectResponse
from openapi_server.models.delete_profile_object_type_response import DeleteProfileObjectTypeResponse
from openapi_server.models.delete_profile_request import DeleteProfileRequest
from openapi_server.models.delete_profile_response import DeleteProfileResponse
from openapi_server.models.get_auto_merging_preview_request import GetAutoMergingPreviewRequest
from openapi_server.models.get_auto_merging_preview_response import GetAutoMergingPreviewResponse
from openapi_server.models.get_calculated_attribute_definition_response import GetCalculatedAttributeDefinitionResponse
from openapi_server.models.get_calculated_attribute_for_profile_response import GetCalculatedAttributeForProfileResponse
from openapi_server.models.get_domain_response import GetDomainResponse
from openapi_server.models.get_event_stream_response import GetEventStreamResponse
from openapi_server.models.get_identity_resolution_job_response import GetIdentityResolutionJobResponse
from openapi_server.models.get_integration_response import GetIntegrationResponse
from openapi_server.models.get_matches_response import GetMatchesResponse
from openapi_server.models.get_profile_object_type_response import GetProfileObjectTypeResponse
from openapi_server.models.get_profile_object_type_template_response import GetProfileObjectTypeTemplateResponse
from openapi_server.models.get_similar_profiles_request import GetSimilarProfilesRequest
from openapi_server.models.get_similar_profiles_response import GetSimilarProfilesResponse
from openapi_server.models.get_workflow_response import GetWorkflowResponse
from openapi_server.models.get_workflow_steps_response import GetWorkflowStepsResponse
from openapi_server.models.list_account_integrations_response import ListAccountIntegrationsResponse
from openapi_server.models.list_calculated_attribute_definitions_response import ListCalculatedAttributeDefinitionsResponse
from openapi_server.models.list_calculated_attributes_for_profile_response import ListCalculatedAttributesForProfileResponse
from openapi_server.models.list_domains_response import ListDomainsResponse
from openapi_server.models.list_event_streams_response import ListEventStreamsResponse
from openapi_server.models.list_identity_resolution_jobs_response import ListIdentityResolutionJobsResponse
from openapi_server.models.list_integrations_response import ListIntegrationsResponse
from openapi_server.models.list_profile_object_type_templates_response import ListProfileObjectTypeTemplatesResponse
from openapi_server.models.list_profile_object_types_response import ListProfileObjectTypesResponse
from openapi_server.models.list_profile_objects_request import ListProfileObjectsRequest
from openapi_server.models.list_profile_objects_response import ListProfileObjectsResponse
from openapi_server.models.list_rule_based_matches_response import ListRuleBasedMatchesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_workflows_request import ListWorkflowsRequest
from openapi_server.models.list_workflows_response import ListWorkflowsResponse
from openapi_server.models.merge_profiles_request import MergeProfilesRequest
from openapi_server.models.merge_profiles_response import MergeProfilesResponse
from openapi_server.models.put_integration_request import PutIntegrationRequest
from openapi_server.models.put_integration_response import PutIntegrationResponse
from openapi_server.models.put_profile_object_request import PutProfileObjectRequest
from openapi_server.models.put_profile_object_response import PutProfileObjectResponse
from openapi_server.models.put_profile_object_type_request import PutProfileObjectTypeRequest
from openapi_server.models.put_profile_object_type_response import PutProfileObjectTypeResponse
from openapi_server.models.search_profiles_request import SearchProfilesRequest
from openapi_server.models.search_profiles_response import SearchProfilesResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_calculated_attribute_definition_request import UpdateCalculatedAttributeDefinitionRequest
from openapi_server.models.update_calculated_attribute_definition_response import UpdateCalculatedAttributeDefinitionResponse
from openapi_server.models.update_domain_request import UpdateDomainRequest
from openapi_server.models.update_domain_response import UpdateDomainResponse
from openapi_server.models.update_profile_request import UpdateProfileRequest
from openapi_server.models.update_profile_response import UpdateProfileResponse
from openapi_server import util


async def add_profile_key(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_profile_key

    &lt;p&gt;Associates a new key value with a specific profile, such as a Contact Record ContactId.&lt;/p&gt; &lt;p&gt;A profile object can have a single unique key and any number of additional keys that can be used to identify the profile that it belongs to.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = AddProfileKeyRequest.from_dict(body)
    return web.Response(status=200)


async def create_calculated_attribute_definition(request: web.Request, domain_name, calculated_attribute_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_calculated_attribute_definition

    Creates a new calculated attribute definition. After creation, new object data ingested into Customer Profiles will be included in the calculated attribute, which can be retrieved for a profile using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetCalculatedAttributeForProfile.html\&quot;&gt;GetCalculatedAttributeForProfile&lt;/a&gt; API. Defining a calculated attribute makes it available for all profiles within a domain. Each calculated attribute can only reference one &lt;code&gt;ObjectType&lt;/code&gt; and at most, two fields from that &lt;code&gt;ObjectType&lt;/code&gt;.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param calculated_attribute_name: The unique name of the calculated attribute.
    :type calculated_attribute_name: str
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
    body = CreateCalculatedAttributeDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def create_domain(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_domain

    &lt;p&gt;Creates a domain, which is a container for all customer data, such as customer profile attributes, object types, profile keys, and encryption keys. You can create multiple domains, and each domain can have multiple third-party integrations.&lt;/p&gt; &lt;p&gt;Each Amazon Connect instance can be associated with only one domain. Multiple Amazon Connect instances can be associated with one domain.&lt;/p&gt; &lt;p&gt;Use this API or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html\&quot;&gt;UpdateDomain&lt;/a&gt; to enable &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html\&quot;&gt;identity resolution&lt;/a&gt;: set &lt;code&gt;Matching&lt;/code&gt; to true.&lt;/p&gt; &lt;p&gt;To prevent cross-service impersonation when you call this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html\&quot;&gt;Cross-service confused deputy prevention&lt;/a&gt; for sample policies that you should apply. &lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = CreateDomainRequest.from_dict(body)
    return web.Response(status=200)


async def create_event_stream(request: web.Request, domain_name, event_stream_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_event_stream

    &lt;p&gt;Creates an event stream, which is a subscription to real-time events, such as when profiles are created and updated through Amazon Connect Customer Profiles.&lt;/p&gt; &lt;p&gt;Each event stream can be associated with only one Kinesis Data Stream destination in the same region and Amazon Web Services account as the customer profiles domain&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param event_stream_name: The name of the event stream.
    :type event_stream_name: str
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
    body = CreateEventStreamRequest.from_dict(body)
    return web.Response(status=200)


async def create_integration_workflow(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_integration_workflow

     Creates an integration workflow. An integration workflow is an async process which ingests historic data and sets up an integration for ongoing updates. The supported Amazon AppFlow sources are Salesforce, ServiceNow, and Marketo. 

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = CreateIntegrationWorkflowRequest.from_dict(body)
    return web.Response(status=200)


async def create_profile(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_profile

    &lt;p&gt;Creates a standard profile.&lt;/p&gt; &lt;p&gt;A standard profile represents the following attributes for a customer profile in a domain.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = CreateProfileRequest.from_dict(body)
    return web.Response(status=200)


async def delete_calculated_attribute_definition(request: web.Request, domain_name, calculated_attribute_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_calculated_attribute_definition

    Deletes an existing calculated attribute definition. Note that deleting a default calculated attribute is possible, however once deleted, you will be unable to undo that action and will need to recreate it on your own using the CreateCalculatedAttributeDefinition API if you want it back.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param calculated_attribute_name: The unique name of the calculated attribute.
    :type calculated_attribute_name: str
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


async def delete_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_domain

    Deletes a specific domain and all of its customer data, such as customer profile attributes and their related objects.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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


async def delete_event_stream(request: web.Request, domain_name, event_stream_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_event_stream

    Disables and deletes the specified event stream.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param event_stream_name: The name of the event stream
    :type event_stream_name: str
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


async def delete_integration(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_integration

    Removes an integration from a specific domain.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = DeleteIntegrationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_profile(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_profile

    Deletes the standard customer profile and all data pertaining to the profile.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = DeleteProfileRequest.from_dict(body)
    return web.Response(status=200)


async def delete_profile_key(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_profile_key

    Removes a searchable key from a customer profile.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = DeleteProfileKeyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_profile_object(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_profile_object

    Removes an object associated with a profile of a given ProfileObjectType.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = DeleteProfileObjectRequest.from_dict(body)
    return web.Response(status=200)


async def delete_profile_object_type(request: web.Request, domain_name, object_type_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_profile_object_type

    Removes a ProfileObjectType from a specific domain as well as removes all the ProfileObjects of that type. It also disables integrations from this specific ProfileObjectType. In addition, it scrubs all of the fields of the standard profile that were populated from this ProfileObjectType.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param object_type_name: The name of the profile object type.
    :type object_type_name: str
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


async def delete_workflow(request: web.Request, domain_name, workflow_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_workflow

    Deletes the specified workflow and all its corresponding resources. This is an async process.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param workflow_id: Unique identifier for the workflow.
    :type workflow_id: str
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


async def get_auto_merging_preview(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_auto_merging_preview

    &lt;p&gt;Tests the auto-merging settings of your Identity Resolution Job without merging your data. It randomly selects a sample of matching groups from the existing matching results, and applies the automerging settings that you provided. You can then view the number of profiles in the sample, the number of matches, and the number of profiles identified to be merged. This enables you to evaluate the accuracy of the attributes in your matching list. &lt;/p&gt; &lt;p&gt;You can&#39;t view which profiles are matched and would be merged.&lt;/p&gt; &lt;important&gt; &lt;p&gt;We strongly recommend you use this API to do a dry run of the automerging process before running the Identity Resolution Job. Include &lt;b&gt;at least&lt;/b&gt; two matching attributes. If your matching list includes too few attributes (such as only &lt;code&gt;FirstName&lt;/code&gt; or only &lt;code&gt;LastName&lt;/code&gt;), there may be a large number of matches. This increases the chances of erroneous merges.&lt;/p&gt; &lt;/important&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = GetAutoMergingPreviewRequest.from_dict(body)
    return web.Response(status=200)


async def get_calculated_attribute_definition(request: web.Request, domain_name, calculated_attribute_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_calculated_attribute_definition

    Provides more information on a calculated attribute definition for Customer Profiles.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param calculated_attribute_name: The unique name of the calculated attribute.
    :type calculated_attribute_name: str
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


async def get_calculated_attribute_for_profile(request: web.Request, domain_name, profile_id, calculated_attribute_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_calculated_attribute_for_profile

    Retrieve a calculated attribute for a customer profile.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param profile_id: The unique identifier of a customer profile.
    :type profile_id: str
    :param calculated_attribute_name: The unique name of the calculated attribute.
    :type calculated_attribute_name: str
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


async def get_domain(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_domain

    Returns information about a specific domain.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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


async def get_event_stream(request: web.Request, domain_name, event_stream_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_event_stream

    Returns information about the specified event stream in a specific domain.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param event_stream_name: The name of the event stream provided during create operations.
    :type event_stream_name: str
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


async def get_identity_resolution_job(request: web.Request, domain_name, job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_identity_resolution_job

    &lt;p&gt;Returns information about an Identity Resolution Job in a specific domain. &lt;/p&gt; &lt;p&gt;Identity Resolution Jobs are set up using the Amazon Connect admin console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/use-identity-resolution.html\&quot;&gt;Use Identity Resolution to consolidate similar profiles&lt;/a&gt;.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param job_id: The unique identifier of the Identity Resolution Job.
    :type job_id: str
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


async def get_integration(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_integration

    Returns an integration for a domain.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = DeleteIntegrationRequest.from_dict(body)
    return web.Response(status=200)


async def get_matches(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_matches

    &lt;p&gt;Before calling this API, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html\&quot;&gt;CreateDomain&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html\&quot;&gt;UpdateDomain&lt;/a&gt; to enable identity resolution: set &lt;code&gt;Matching&lt;/code&gt; to true.&lt;/p&gt; &lt;p&gt;GetMatches returns potentially matching profiles, based on the results of the latest run of a machine learning process. &lt;/p&gt; &lt;important&gt; &lt;p&gt;The process of matching duplicate profiles. If &lt;code&gt;Matching&lt;/code&gt; &#x3D; &lt;code&gt;true&lt;/code&gt;, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. &lt;/p&gt; &lt;p&gt;After the Identity Resolution Job completes, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html\&quot;&gt;GetMatches&lt;/a&gt; API to return and review the results. Or, if you have configured &lt;code&gt;ExportingConfig&lt;/code&gt; in the &lt;code&gt;MatchingRequest&lt;/code&gt;, you can download the results from S3.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Amazon Connect uses the following profile attributes to identify matches:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;PhoneNumber&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;HomePhoneNumber&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;BusinessPhoneNumber&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;MobilePhoneNumber&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EmailAddress&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;PersonalEmailAddress&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;BusinessEmailAddress&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;FullName&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For example, two or more profiles—with spelling mistakes such as &lt;b&gt;John Doe&lt;/b&gt; and &lt;b&gt;Jhn Doe&lt;/b&gt;, or different casing email addresses such as &lt;b&gt;JOHN_DOE@ANYCOMPANY.COM&lt;/b&gt; and &lt;b&gt;johndoe@anycompany.com&lt;/b&gt;, or different phone number formats such as &lt;b&gt;555-010-0000&lt;/b&gt; and &lt;b&gt;+1-555-010-0000&lt;/b&gt;—can be detected as belonging to the same customer &lt;b&gt;John Doe&lt;/b&gt; and merged into a unified profile.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_profile_object_type(request: web.Request, domain_name, object_type_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_profile_object_type

    Returns the object types for a specific domain.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param object_type_name: The name of the profile object type.
    :type object_type_name: str
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


async def get_profile_object_type_template(request: web.Request, template_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_profile_object_type_template

    &lt;p&gt;Returns the template information for a specific object type.&lt;/p&gt; &lt;p&gt;A template is a predefined ProfileObjectType, such as “Salesforce-Account” or “Salesforce-Contact.” When a user sends a ProfileObject, using the PutProfileObject API, with an ObjectTypeName that matches one of the TemplateIds, it uses the mappings from the template.&lt;/p&gt;

    :param template_id: A unique identifier for the object template.
    :type template_id: str
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


async def get_similar_profiles(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_similar_profiles

    Returns a set of profiles that belong to the same matching group using the &lt;code&gt;matchId&lt;/code&gt; or &lt;code&gt;profileId&lt;/code&gt;. You can also specify the type of matching that you want for finding similar profiles using either &lt;code&gt;RULE_BASED_MATCHING&lt;/code&gt; or &lt;code&gt;ML_BASED_MATCHING&lt;/code&gt;.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: The pagination token from the previous &lt;code&gt;GetSimilarProfiles&lt;/code&gt; API call.
    :type next_token: str
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int

    """
    body = GetSimilarProfilesRequest.from_dict(body)
    return web.Response(status=200)


async def get_workflow(request: web.Request, domain_name, workflow_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_workflow

    Get details of specified workflow.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param workflow_id: Unique identifier for the workflow.
    :type workflow_id: str
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


async def get_workflow_steps(request: web.Request, domain_name, workflow_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """get_workflow_steps

    Get granular list of steps in workflow.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param workflow_id: Unique identifier for the workflow.
    :type workflow_id: str
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
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_account_integrations(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, include_hidden=None) -> web.Response:
    """list_account_integrations

    Lists all of the integrations associated to a specific URI in the AWS account.

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
    :param next_token: The pagination token from the previous ListAccountIntegrations API call.
    :type next_token: str
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int
    :param include_hidden: Boolean to indicate if hidden integration should be returned. Defaults to &lt;code&gt;False&lt;/code&gt;.
    :type include_hidden: bool

    """
    body = DeleteIntegrationRequest.from_dict(body)
    return web.Response(status=200)


async def list_calculated_attribute_definitions(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_calculated_attribute_definitions

    Lists calculated attribute definitions for Customer Profiles

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: The pagination token from the previous call to ListCalculatedAttributeDefinitions.
    :type next_token: str
    :param max_results: The maximum number of calculated attribute definitions returned per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_calculated_attributes_for_profile(request: web.Request, domain_name, profile_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_calculated_attributes_for_profile

    Retrieve a list of calculated attributes for a customer profile.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param profile_id: The unique identifier of a customer profile.
    :type profile_id: str
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
    :param next_token: The pagination token from the previous call to ListCalculatedAttributesForProfile.
    :type next_token: str
    :param max_results: The maximum number of calculated attributes returned per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_domains(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_domains

    Returns a list of all the domains for an AWS account that have been created.

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
    :param next_token: The pagination token from the previous ListDomain API call.
    :type next_token: str
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_event_streams(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_event_streams

    Returns a list of all the event streams in a specific domain.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: Identifies the next page of results to return.
    :type next_token: str
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_identity_resolution_jobs(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_identity_resolution_jobs

    Lists all of the Identity Resolution Jobs in your domain. The response sorts the list by &lt;code&gt;JobStartTime&lt;/code&gt;.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_integrations(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, include_hidden=None) -> web.Response:
    """list_integrations

    Lists all of the integrations in your domain.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: The pagination token from the previous ListIntegrations API call.
    :type next_token: str
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int
    :param include_hidden: Boolean to indicate if hidden integration should be returned. Defaults to &lt;code&gt;False&lt;/code&gt;.
    :type include_hidden: bool

    """
    return web.Response(status=200)


async def list_profile_object_type_templates(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_profile_object_type_templates

    Lists all of the template information for object types.

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
    :param next_token: The pagination token from the previous ListObjectTypeTemplates API call.
    :type next_token: str
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_profile_object_types(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_profile_object_types

    Lists all of the templates available within the service.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: Identifies the next page of results to return.
    :type next_token: str
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_profile_objects(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_profile_objects

    Returns a list of objects associated with a profile of a given ProfileObjectType.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: The pagination token from the previous call to ListProfileObjects.
    :type next_token: str
    :param max_results: The maximum number of objects returned per page.
    :type max_results: int

    """
    body = ListProfileObjectsRequest.from_dict(body)
    return web.Response(status=200)


async def list_rule_based_matches(request: web.Request, domain_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_rule_based_matches

    Returns a set of &lt;code&gt;MatchIds&lt;/code&gt; that belong to the given domain.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: The pagination token from the previous &lt;code&gt;ListRuleBasedMatches&lt;/code&gt; API call.
    :type next_token: str
    :param max_results: The maximum number of &lt;code&gt;MatchIds&lt;/code&gt; returned per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Displays the tags associated with an Amazon Connect Customer Profiles resource. In Connect Customer Profiles, domains, profile object types, and integrations can be tagged.

    :param resource_arn: The ARN of the resource for which you want to view tags.
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


async def list_workflows(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_workflows

    Query to list all workflows.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return per page.
    :type max_results: int

    """
    body = ListWorkflowsRequest.from_dict(body)
    return web.Response(status=200)


async def merge_profiles(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """merge_profiles

    &lt;p&gt;Runs an AWS Lambda job that does the following:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;All the profileKeys in the &lt;code&gt;ProfileToBeMerged&lt;/code&gt; will be moved to the main profile.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All the objects in the &lt;code&gt;ProfileToBeMerged&lt;/code&gt; will be moved to the main profile.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All the &lt;code&gt;ProfileToBeMerged&lt;/code&gt; will be deleted at the end.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All the profileKeys in the &lt;code&gt;ProfileIdsToBeMerged&lt;/code&gt; will be moved to the main profile.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Standard fields are merged as follows:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Fields are always \&quot;union\&quot;-ed if there are no conflicts in standard fields or attributeKeys.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When there are conflicting fields:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;If no &lt;code&gt;SourceProfileIds&lt;/code&gt; entry is specified, the main Profile value is always taken. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If a &lt;code&gt;SourceProfileIds&lt;/code&gt; entry is specified, the specified profileId is always taken, even if it is a NULL value.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;/li&gt; &lt;/ol&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;You can use MergeProfiles together with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html\&quot;&gt;GetMatches&lt;/a&gt;, which returns potentially matching profiles, or use it with the results of another matching system. After profiles have been merged, they cannot be separated (unmerged).&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = MergeProfilesRequest.from_dict(body)
    return web.Response(status=200)


async def put_integration(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_integration

    &lt;p&gt;Adds an integration between the service and a third-party service, which includes Amazon AppFlow and Amazon Connect.&lt;/p&gt; &lt;p&gt;An integration can belong to only one domain.&lt;/p&gt; &lt;p&gt;To add or remove tags on an existing Integration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html\&quot;&gt; TagResource &lt;/a&gt;/&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html\&quot;&gt; UntagResource&lt;/a&gt;.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = PutIntegrationRequest.from_dict(body)
    return web.Response(status=200)


async def put_profile_object(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_profile_object

    &lt;p&gt;Adds additional objects to customer profiles of a given ObjectType.&lt;/p&gt; &lt;p&gt;When adding a specific profile object, like a Contact Record, an inferred profile can get created if it is not mapped to an existing profile. The resulting profile will only have a phone number populated in the standard ProfileObject. Any additional Contact Records with the same phone number will be mapped to the same inferred profile.&lt;/p&gt; &lt;p&gt;When a ProfileObject is created and if a ProfileObjectType already exists for the ProfileObject, it will provide data to a standard profile depending on the ProfileObjectType definition.&lt;/p&gt; &lt;p&gt;PutProfileObject needs an ObjectType, which can be created using PutProfileObjectType.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = PutProfileObjectRequest.from_dict(body)
    return web.Response(status=200)


async def put_profile_object_type(request: web.Request, domain_name, object_type_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_profile_object_type

    &lt;p&gt;Defines a ProfileObjectType.&lt;/p&gt; &lt;p&gt;To add or remove tags on an existing ObjectType, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html\&quot;&gt; TagResource&lt;/a&gt;/&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param object_type_name: The name of the profile object type.
    :type object_type_name: str
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
    body = PutProfileObjectTypeRequest.from_dict(body)
    return web.Response(status=200)


async def search_profiles(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """search_profiles

    &lt;p&gt;Searches for profiles within a specific domain using one or more predefined search keys (e.g., _fullName, _phone, _email, _account, etc.) and/or custom-defined search keys. A search key is a data type pair that consists of a &lt;code&gt;KeyName&lt;/code&gt; and &lt;code&gt;Values&lt;/code&gt; list.&lt;/p&gt; &lt;p&gt;This operation supports searching for profiles with a minimum of 1 key-value(s) pair and up to 5 key-value(s) pairs using either &lt;code&gt;AND&lt;/code&gt; or &lt;code&gt;OR&lt;/code&gt; logic.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    :param next_token: The pagination token from the previous SearchProfiles API call.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of objects returned per page.&lt;/p&gt; &lt;p&gt;The default is 20 if this parameter is not included in the request.&lt;/p&gt;
    :type max_results: int

    """
    body = SearchProfilesRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified Amazon Connect Customer Profiles resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In Connect Customer Profiles, domains, profile object types, and integrations can be tagged.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to AWS and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the TagResource action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a resource.&lt;/p&gt;

    :param resource_arn: The ARN of the resource that you&#39;re adding tags to.
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

    Removes one or more tags from the specified Amazon Connect Customer Profiles resource. In Connect Customer Profiles, domains, profile object types, and integrations can be tagged.

    :param resource_arn: The ARN of the resource from which you are removing tags.
    :type resource_arn: str
    :param tag_keys: The list of tag keys to remove from the resource.
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


async def update_calculated_attribute_definition(request: web.Request, domain_name, calculated_attribute_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_calculated_attribute_definition

    Updates an existing calculated attribute definition. When updating the Conditions, note that increasing the date range of a calculated attribute will not trigger inclusion of historical data greater than the current date range.

    :param domain_name: The unique name of the domain.
    :type domain_name: str
    :param calculated_attribute_name: The unique name of the calculated attribute.
    :type calculated_attribute_name: str
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
    body = UpdateCalculatedAttributeDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def update_domain(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_domain

    &lt;p&gt;Updates the properties of a domain, including creating or selecting a dead letter queue or an encryption key.&lt;/p&gt; &lt;p&gt;After a domain is created, the name can’t be changed.&lt;/p&gt; &lt;p&gt;Use this API or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html\&quot;&gt;CreateDomain&lt;/a&gt; to enable &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html\&quot;&gt;identity resolution&lt;/a&gt;: set &lt;code&gt;Matching&lt;/code&gt; to true.&lt;/p&gt; &lt;p&gt;To prevent cross-service impersonation when you call this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html\&quot;&gt;Cross-service confused deputy prevention&lt;/a&gt; for sample policies that you should apply. &lt;/p&gt; &lt;p&gt;To add or remove tags on an existing Domain, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;/&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = UpdateDomainRequest.from_dict(body)
    return web.Response(status=200)


async def update_profile(request: web.Request, domain_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_profile

    &lt;p&gt;Updates the properties of a profile. The ProfileId is required for updating a customer profile.&lt;/p&gt; &lt;p&gt;When calling the UpdateProfile API, specifying an empty string value means that any existing value will be removed. Not specifying a string value means that any value already there will be kept.&lt;/p&gt;

    :param domain_name: The unique name of the domain.
    :type domain_name: str
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
    body = UpdateProfileRequest.from_dict(body)
    return web.Response(status=200)
