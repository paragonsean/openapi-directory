# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection import Connection
from openapi_server.models.custom_connector import CustomConnector
from openapi_server.models.custom_connector_version import CustomConnectorVersion
from openapi_server.models.endpoint_attachment import EndpointAttachment
from openapi_server.models.event_subscription import EventSubscription
from openapi_server.models.event_type import EventType
from openapi_server.models.list_actions_response import ListActionsResponse
from openapi_server.models.list_connections_response import ListConnectionsResponse
from openapi_server.models.list_connector_versions_response import ListConnectorVersionsResponse
from openapi_server.models.list_connectors_response import ListConnectorsResponse
from openapi_server.models.list_custom_connector_versions_response import ListCustomConnectorVersionsResponse
from openapi_server.models.list_custom_connectors_response import ListCustomConnectorsResponse
from openapi_server.models.list_endpoint_attachments_response import ListEndpointAttachmentsResponse
from openapi_server.models.list_entity_types_response import ListEntityTypesResponse
from openapi_server.models.list_event_subscriptions_response import ListEventSubscriptionsResponse
from openapi_server.models.list_event_types_response import ListEventTypesResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_managed_zones_response import ListManagedZonesResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_providers_response import ListProvidersResponse
from openapi_server.models.list_runtime_action_schemas_response import ListRuntimeActionSchemasResponse
from openapi_server.models.list_runtime_entity_schemas_response import ListRuntimeEntitySchemasResponse
from openapi_server.models.listen_event_request import ListenEventRequest
from openapi_server.models.managed_zone import ManagedZone
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_connection_schema_metadata_get_action(client):
    """Test case for connectors_projects_locations_connections_connection_schema_metadata_get_action

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('actionId', 'action_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{nameget_actio}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_connection_schema_metadata_get_entity_type(client):
    """Test case for connectors_projects_locations_connections_connection_schema_metadata_get_entity_type

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('entityId', 'entity_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{nameget_entity_typ}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_connection_schema_metadata_list_actions(client):
    """Test case for connectors_projects_locations_connections_connection_schema_metadata_list_actions

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namelist_action}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_connection_schema_metadata_list_entity_types(client):
    """Test case for connectors_projects_locations_connections_connection_schema_metadata_list_entity_types

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namelist_entity_type}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_connection_schema_metadata_refresh(client):
    """Test case for connectors_projects_locations_connections_connection_schema_metadata_refresh

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namerefres}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_create(client):
    """Test case for connectors_projects_locations_connections_create

    
    """
    body = {"envoyImageLocation":"envoyImageLocation","sslConfig":{"clientCertType":"CERT_TYPE_UNSPECIFIED","clientCertificate":{"secretVersion":"secretVersion"},"serverCertType":"CERT_TYPE_UNSPECIFIED","clientPrivateKeyPass":{"secretVersion":"secretVersion"},"privateServerCertificate":{"secretVersion":"secretVersion"},"trustModel":"PUBLIC","type":"SSL_TYPE_UNSPECIFIED","additionalVariables":[{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"},{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"}],"clientPrivateKey":{"secretVersion":"secretVersion"},"useSsl":True},"authConfig":{"authKey":"authKey","sshPublicKey":{"sshClientCertPass":{"secretVersion":"secretVersion"},"certType":"certType","sshClientCert":{"secretVersion":"secretVersion"},"username":"username"},"userPassword":{"password":{"secretVersion":"secretVersion"},"username":"username"},"oauth2ClientCredentials":{"clientId":"clientId","clientSecret":{"secretVersion":"secretVersion"}},"authType":"AUTH_TYPE_UNSPECIFIED","oauth2AuthCodeFlow":{"redirectUri":"redirectUri","authUri":"authUri","authCode":"authCode","clientId":"clientId","pkceVerifier":"pkceVerifier","enablePkce":True,"clientSecret":{"secretVersion":"secretVersion"},"scopes":["scopes","scopes"]},"oauth2JwtBearer":{"clientKey":{"secretVersion":"secretVersion"},"jwtClaims":{"audience":"audience","subject":"subject","issuer":"issuer"}},"additionalVariables":[{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"},{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"}]},"description":"description","eventingRuntimeData":{"eventsListenerPscSa":"eventsListenerPscSa","eventsListenerEndpoint":"eventsListenerEndpoint","status":{"description":"description","state":"STATE_UNSPECIFIED"}},"eventingConfig":{"triggerConfigVariables":[{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"},{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"}],"authConfig":{"authKey":"authKey","sshPublicKey":{"sshClientCertPass":{"secretVersion":"secretVersion"},"certType":"certType","sshClientCert":{"secretVersion":"secretVersion"},"username":"username"},"userPassword":{"password":{"secretVersion":"secretVersion"},"username":"username"},"oauth2ClientCredentials":{"clientId":"clientId","clientSecret":{"secretVersion":"secretVersion"}},"authType":"AUTH_TYPE_UNSPECIFIED","oauth2AuthCodeFlow":{"redirectUri":"redirectUri","authUri":"authUri","authCode":"authCode","clientId":"clientId","pkceVerifier":"pkceVerifier","enablePkce":True,"clientSecret":{"secretVersion":"secretVersion"},"scopes":["scopes","scopes"]},"oauth2JwtBearer":{"clientKey":{"secretVersion":"secretVersion"},"jwtClaims":{"audience":"audience","subject":"subject","issuer":"issuer"}},"additionalVariables":[{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"},{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"}]},"privateConnectivityEnabled":True,"eventsListenerIngressEndpoint":"eventsListenerIngressEndpoint","listenerAuthConfig":{"authKey":"authKey","sshPublicKey":{"sshClientCertPass":{"secretVersion":"secretVersion"},"certType":"certType","sshClientCert":{"secretVersion":"secretVersion"},"username":"username"},"userPassword":{"password":{"secretVersion":"secretVersion"},"username":"username"},"oauth2ClientCredentials":{"clientId":"clientId","clientSecret":{"secretVersion":"secretVersion"}},"authType":"AUTH_TYPE_UNSPECIFIED","oauth2AuthCodeFlow":{"redirectUri":"redirectUri","authUri":"authUri","authCode":"authCode","clientId":"clientId","pkceVerifier":"pkceVerifier","enablePkce":True,"clientSecret":{"secretVersion":"secretVersion"},"scopes":["scopes","scopes"]},"oauth2JwtBearer":{"clientKey":{"secretVersion":"secretVersion"},"jwtClaims":{"audience":"audience","subject":"subject","issuer":"issuer"}},"additionalVariables":[{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"},{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"}]},"enrichmentEnabled":True,"deadLetterConfig":{"topic":"topic","projectId":"projectId"},"additionalVariables":[{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"},{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"}],"proxyDestinationConfig":{"destinations":[{"port":0,"serviceAttachment":"serviceAttachment","host":"host"},{"port":0,"serviceAttachment":"serviceAttachment","host":"host"}],"key":"key"},"registrationDestinationConfig":{"destinations":[{"port":0,"serviceAttachment":"serviceAttachment","host":"host"},{"port":0,"serviceAttachment":"serviceAttachment","host":"host"}],"key":"key"}},"eventingEnablementType":"EVENTING_ENABLEMENT_TYPE_UNSPECIFIED","nodeConfig":{"minNodeCount":1,"maxNodeCount":6},"imageLocation":"imageLocation","connectionRevision":"connectionRevision","connectorVersionLaunchStage":"LAUNCH_STAGE_UNSPECIFIED","lockConfig":{"reason":"reason","locked":True},"connectorVersion":"connectorVersion","connectorVersionInfraConfig":{"deploymentModel":"DEPLOYMENT_MODEL_UNSPECIFIED","internalclientRatelimitThreshold":"internalclientRatelimitThreshold","connectionRatelimitWindowSeconds":"connectionRatelimitWindowSeconds","ratelimitThreshold":"ratelimitThreshold","hpaConfig":{"memoryUtilizationThreshold":"memoryUtilizationThreshold","cpuUtilizationThreshold":"cpuUtilizationThreshold"},"resourceLimits":{"memory":"memory","cpu":"cpu"},"resourceRequests":{"memory":"memory","cpu":"cpu"},"sharedDeployment":"sharedDeployment"},"destinationConfigs":[{"destinations":[{"port":0,"serviceAttachment":"serviceAttachment","host":"host"},{"port":0,"serviceAttachment":"serviceAttachment","host":"host"}],"key":"key"},{"destinations":[{"port":0,"serviceAttachment":"serviceAttachment","host":"host"},{"port":0,"serviceAttachment":"serviceAttachment","host":"host"}],"key":"key"}],"logConfig":{"enabled":True},"serviceDirectory":"serviceDirectory","serviceAccount":"serviceAccount","updateTime":"updateTime","isTrustedTester":True,"suspended":True,"configVariables":[{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"},{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"}],"labels":{"key":"labels"},"createTime":"createTime","subscriptionType":"SUBSCRIPTION_TYPE_UNSPECIFIED","name":"name","status":{"description":"description","state":"STATE_UNSPECIFIED","status":"status"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('connectionId', 'connection_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/connections'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_event_subscriptions_create(client):
    """Test case for connectors_projects_locations_connections_event_subscriptions_create

    
    """
    body = {"jms":{"name":"name","type":"TYPE_UNSPECIFIED"},"subscriberLink":"subscriberLink","eventTypeId":"eventTypeId","subscriber":"subscriber","createTime":"createTime","destinations":{"endpoint":{"headers":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"endpointUri":"endpointUri"},"serviceAccount":"serviceAccount","type":"TYPE_UNSPECIFIED"},"name":"name","updateTime":"updateTime","status":{"description":"description","state":"STATE_UNSPECIFIED"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('eventSubscriptionId', 'event_subscription_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/eventSubscriptions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_event_subscriptions_list(client):
    """Test case for connectors_projects_locations_connections_event_subscriptions_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/eventSubscriptions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_event_subscriptions_retry(client):
    """Test case for connectors_projects_locations_connections_event_subscriptions_retry

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameretr}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_list(client):
    """Test case for connectors_projects_locations_connections_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/connections'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_listen_event(client):
    """Test case for connectors_projects_locations_connections_listen_event

    
    """
    body = {"payload":{"key":""}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{resource_pathlisten_even}'.format(_resource_path='_resource_path_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_repair_eventing(client):
    """Test case for connectors_projects_locations_connections_repair_eventing

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namerepair_eventin}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_runtime_action_schemas_list(client):
    """Test case for connectors_projects_locations_connections_runtime_action_schemas_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/runtimeActionSchemas'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_connections_runtime_entity_schemas_list(client):
    """Test case for connectors_projects_locations_connections_runtime_entity_schemas_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/runtimeEntitySchemas'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_endpoint_attachments_create(client):
    """Test case for connectors_projects_locations_endpoint_attachments_create

    
    """
    body = {"createTime":"createTime","serviceAttachment":"serviceAttachment","name":"name","description":"description","endpointIp":"endpointIp","updateTime":"updateTime","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('endpointAttachmentId', 'endpoint_attachment_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/endpointAttachments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_endpoint_attachments_list(client):
    """Test case for connectors_projects_locations_endpoint_attachments_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/endpointAttachments'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_global_custom_connectors_create(client):
    """Test case for connectors_projects_locations_global_custom_connectors_create

    
    """
    body = {"activeConnectorVersions":["activeConnectorVersions","activeConnectorVersions"],"createTime":"createTime","displayName":"displayName","name":"name","description":"description","logo":"logo","updateTime":"updateTime","customConnectorType":"CUSTOM_CONNECTOR_TYPE_UNSPECIFIED","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('customConnectorId', 'custom_connector_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/customConnectors'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_global_custom_connectors_custom_connector_versions_create(client):
    """Test case for connectors_projects_locations_global_custom_connectors_custom_connector_versions_create

    
    """
    body = {"authConfig":{"authKey":"authKey","sshPublicKey":{"sshClientCertPass":{"secretVersion":"secretVersion"},"certType":"certType","sshClientCert":{"secretVersion":"secretVersion"},"username":"username"},"userPassword":{"password":{"secretVersion":"secretVersion"},"username":"username"},"oauth2ClientCredentials":{"clientId":"clientId","clientSecret":{"secretVersion":"secretVersion"}},"authType":"AUTH_TYPE_UNSPECIFIED","oauth2AuthCodeFlow":{"redirectUri":"redirectUri","authUri":"authUri","authCode":"authCode","clientId":"clientId","pkceVerifier":"pkceVerifier","enablePkce":True,"clientSecret":{"secretVersion":"secretVersion"},"scopes":["scopes","scopes"]},"oauth2JwtBearer":{"clientKey":{"secretVersion":"secretVersion"},"jwtClaims":{"audience":"audience","subject":"subject","issuer":"issuer"}},"additionalVariables":[{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"},{"stringValue":"stringValue","secretValue":{"secretVersion":"secretVersion"},"intValue":"intValue","boolValue":True,"encryptionKeyValue":{"type":"TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"key":"key"}]},"createTime":"createTime","specLocation":"specLocation","name":"name","serviceAccount":"serviceAccount","updateTime":"updateTime","enableBackendDestinationConfig":True,"state":"STATE_UNSPECIFIED","destinationConfigs":[{"destinations":[{"port":0,"serviceAttachment":"serviceAttachment","host":"host"},{"port":0,"serviceAttachment":"serviceAttachment","host":"host"}],"key":"key"},{"destinations":[{"port":0,"serviceAttachment":"serviceAttachment","host":"host"},{"port":0,"serviceAttachment":"serviceAttachment","host":"host"}],"key":"key"}],"backendVariableTemplates":[{"displayName":"displayName","description":"description","locationType":"LOCATION_TYPE_UNSPECIFIED","required":True,"enumOptions":[{"displayName":"displayName","id":"id"},{"displayName":"displayName","id":"id"}],"roleGrant":{"principal":"PRINCIPAL_UNSPECIFIED","resource":{"pathTemplate":"pathTemplate","type":"TYPE_UNSPECIFIED"},"helperTextTemplate":"helperTextTemplate","roles":["roles","roles"]},"isAdvanced":True,"requiredCondition":{"fieldComparisons":[{"comparator":"COMPARATOR_UNSPECIFIED","stringValue":"stringValue","intValue":"intValue","boolValue":True,"key":"key"},{"comparator":"COMPARATOR_UNSPECIFIED","stringValue":"stringValue","intValue":"intValue","boolValue":True,"key":"key"}],"logicalOperator":"OPERATOR_UNSPECIFIED","logicalExpressions":[null,null]},"valueType":"VALUE_TYPE_UNSPECIFIED","state":"STATE_UNSPECIFIED","authorizationCodeLink":{"clientId":"clientId","enablePkce":True,"scopes":["scopes","scopes"],"uri":"uri"},"validationRegex":"validationRegex","key":"key"},{"displayName":"displayName","description":"description","locationType":"LOCATION_TYPE_UNSPECIFIED","required":True,"enumOptions":[{"displayName":"displayName","id":"id"},{"displayName":"displayName","id":"id"}],"roleGrant":{"principal":"PRINCIPAL_UNSPECIFIED","resource":{"pathTemplate":"pathTemplate","type":"TYPE_UNSPECIFIED"},"helperTextTemplate":"helperTextTemplate","roles":["roles","roles"]},"isAdvanced":True,"requiredCondition":{"fieldComparisons":[{"comparator":"COMPARATOR_UNSPECIFIED","stringValue":"stringValue","intValue":"intValue","boolValue":True,"key":"key"},{"comparator":"COMPARATOR_UNSPECIFIED","stringValue":"stringValue","intValue":"intValue","boolValue":True,"key":"key"}],"logicalOperator":"OPERATOR_UNSPECIFIED","logicalExpressions":[null,null]},"valueType":"VALUE_TYPE_UNSPECIFIED","state":"STATE_UNSPECIFIED","authorizationCodeLink":{"clientId":"clientId","enablePkce":True,"scopes":["scopes","scopes"],"uri":"uri"},"validationRegex":"validationRegex","key":"key"}],"labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('customConnectorVersionId', 'custom_connector_version_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/customConnectorVersions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_global_custom_connectors_custom_connector_versions_list(client):
    """Test case for connectors_projects_locations_global_custom_connectors_custom_connector_versions_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/customConnectorVersions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_global_custom_connectors_list(client):
    """Test case for connectors_projects_locations_global_custom_connectors_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/customConnectors'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_global_managed_zones_create(client):
    """Test case for connectors_projects_locations_global_managed_zones_create

    
    """
    body = {"createTime":"createTime","dns":"dns","name":"name","description":"description","updateTime":"updateTime","targetProject":"targetProject","targetVpc":"targetVpc","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('managedZoneId', 'managed_zone_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/managedZones'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_global_managed_zones_list(client):
    """Test case for connectors_projects_locations_global_managed_zones_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/managedZones'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_global_managed_zones_patch(client):
    """Test case for connectors_projects_locations_global_managed_zones_patch

    
    """
    body = {"createTime":"createTime","dns":"dns","name":"name","description":"description","updateTime":"updateTime","targetProject":"targetProject","targetVpc":"targetVpc","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_list(client):
    """Test case for connectors_projects_locations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_operations_cancel(client):
    """Test case for connectors_projects_locations_operations_cancel

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_operations_delete(client):
    """Test case for connectors_projects_locations_operations_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('force', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_operations_list(client):
    """Test case for connectors_projects_locations_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_providers_connectors_list(client):
    """Test case for connectors_projects_locations_providers_connectors_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/connectors'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_providers_connectors_versions_eventtypes_get(client):
    """Test case for connectors_projects_locations_providers_connectors_versions_eventtypes_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_providers_connectors_versions_eventtypes_list(client):
    """Test case for connectors_projects_locations_providers_connectors_versions_eventtypes_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/eventtypes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_providers_connectors_versions_list(client):
    """Test case for connectors_projects_locations_providers_connectors_versions_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/versions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_providers_get_iam_policy(client):
    """Test case for connectors_projects_locations_providers_get_iam_policy

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_providers_list(client):
    """Test case for connectors_projects_locations_providers_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/providers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_providers_set_iam_policy(client):
    """Test case for connectors_projects_locations_providers_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_projects_locations_providers_test_iam_permissions(client):
    """Test case for connectors_projects_locations_providers_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

