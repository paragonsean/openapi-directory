# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_flow_executions_request import CancelFlowExecutionsRequest
from openapi_server.models.cancel_flow_executions_response import CancelFlowExecutionsResponse
from openapi_server.models.create_connector_profile_request import CreateConnectorProfileRequest
from openapi_server.models.create_connector_profile_response import CreateConnectorProfileResponse
from openapi_server.models.create_flow_request import CreateFlowRequest
from openapi_server.models.create_flow_response import CreateFlowResponse
from openapi_server.models.delete_connector_profile_request import DeleteConnectorProfileRequest
from openapi_server.models.delete_flow_request import DeleteFlowRequest
from openapi_server.models.describe_connector_entity_request import DescribeConnectorEntityRequest
from openapi_server.models.describe_connector_entity_response import DescribeConnectorEntityResponse
from openapi_server.models.describe_connector_profiles_request import DescribeConnectorProfilesRequest
from openapi_server.models.describe_connector_profiles_response import DescribeConnectorProfilesResponse
from openapi_server.models.describe_connector_request import DescribeConnectorRequest
from openapi_server.models.describe_connector_response import DescribeConnectorResponse
from openapi_server.models.describe_connectors_request import DescribeConnectorsRequest
from openapi_server.models.describe_connectors_response import DescribeConnectorsResponse
from openapi_server.models.describe_flow_execution_records_request import DescribeFlowExecutionRecordsRequest
from openapi_server.models.describe_flow_execution_records_response import DescribeFlowExecutionRecordsResponse
from openapi_server.models.describe_flow_request import DescribeFlowRequest
from openapi_server.models.describe_flow_response import DescribeFlowResponse
from openapi_server.models.list_connector_entities_request import ListConnectorEntitiesRequest
from openapi_server.models.list_connector_entities_response import ListConnectorEntitiesResponse
from openapi_server.models.list_connectors_request import ListConnectorsRequest
from openapi_server.models.list_connectors_response import ListConnectorsResponse
from openapi_server.models.list_flows_request import ListFlowsRequest
from openapi_server.models.list_flows_response import ListFlowsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.register_connector_request import RegisterConnectorRequest
from openapi_server.models.register_connector_response import RegisterConnectorResponse
from openapi_server.models.reset_connector_metadata_cache_request import ResetConnectorMetadataCacheRequest
from openapi_server.models.start_flow_request import StartFlowRequest
from openapi_server.models.start_flow_response import StartFlowResponse
from openapi_server.models.stop_flow_response import StopFlowResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.unregister_connector_request import UnregisterConnectorRequest
from openapi_server.models.update_connector_profile_request import UpdateConnectorProfileRequest
from openapi_server.models.update_connector_profile_response import UpdateConnectorProfileResponse
from openapi_server.models.update_connector_registration_request import UpdateConnectorRegistrationRequest
from openapi_server.models.update_connector_registration_response import UpdateConnectorRegistrationResponse
from openapi_server.models.update_flow_request import UpdateFlowRequest
from openapi_server.models.update_flow_response import UpdateFlowResponse


pytestmark = pytest.mark.asyncio

async def test_cancel_flow_executions(client):
    """Test case for cancel_flow_executions

    
    """
    body = {"executionIds":"","flowName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cancel-flow-executions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_connector_profile(client):
    """Test case for create_connector_profile

    
    """
    body = {"connectorType":"","connectorProfileConfig":{"connectorProfileCredentials":{"Amplitude":{"apiKey":"","secretKey":""},"GoogleAnalytics":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":"","refreshToken":""},"ServiceNow":{"password":"","username":""},"CustomConnector":{"apiKey":{"apiKey":"","apiSecretKey":""},"custom":{"customAuthenticationType":"","credentialsMap":""},"authenticationType":"","basic":{"password":"","username":""},"oauth2":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":"","refreshToken":""}},"SAPOData":{"basicAuthCredentials":{"password":"","username":""},"oAuthCredentials":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":"","refreshToken":""}},"Pardot":{"oAuthRequest":{"redirectUri":"","authCode":""},"accessToken":"","clientCredentialsArn":"","refreshToken":""},"Honeycode":{"oAuthRequest":{"redirectUri":"","authCode":""},"accessToken":"","refreshToken":""},"Veeva":{"password":"","username":""},"Trendmicro":{"apiSecretKey":""},"Datadog":{"apiKey":"","applicationKey":""},"Marketo":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":""},"Redshift":{"password":"","username":""},"Singular":{"apiKey":""},"Slack":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":""},"Snowflake":{"password":"","username":""},"Dynatrace":{"apiToken":""},"Zendesk":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":""},"InforNexus":{"accessKeyId":"","secretAccessKey":"","datakey":"","userId":""},"Salesforce":{"oAuthRequest":{"redirectUri":"","authCode":""},"oAuth2GrantType":"","jwtToken":"","accessToken":"","clientCredentialsArn":"","refreshToken":""}},"connectorProfileProperties":{"Amplitude":"","GoogleAnalytics":"","ServiceNow":{"instanceUrl":""},"CustomConnector":{"oAuth2Properties":{"tokenUrl":"","tokenUrlCustomProperties":"","oAuth2GrantType":""},"profileProperties":""},"SAPOData":{"privateLinkServiceName":"","logonLanguage":"","oAuthProperties":{"tokenUrl":"","oAuthScopes":"","authCodeUrl":""},"disableSSO":"","applicationHostUrl":"","applicationServicePath":"","clientNumber":"","portNumber":""},"Pardot":{"isSandboxEnvironment":"","businessUnitId":"","instanceUrl":""},"Honeycode":"","Veeva":{"instanceUrl":""},"Trendmicro":"","Datadog":{"instanceUrl":""},"Marketo":{"instanceUrl":""},"Redshift":{"bucketName":"","databaseName":"","roleArn":"","bucketPrefix":"","workgroupName":"","clusterIdentifier":"","isRedshiftServerless":"","dataApiRoleArn":"","databaseUrl":""},"Singular":"","Slack":{"instanceUrl":""},"Snowflake":{"bucketName":"","privateLinkServiceName":"","stage":"","accountName":"","bucketPrefix":"","warehouse":"","region":""},"Dynatrace":{"instanceUrl":""},"Zendesk":{"instanceUrl":""},"InforNexus":{"instanceUrl":""},"Salesforce":{"isSandboxEnvironment":"","usePrivateLinkForMetadataAndAuthorization":"","instanceUrl":""}}},"connectionMode":"","connectorProfileName":"","clientToken":"","kmsArn":"","connectorLabel":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/create-connector-profile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_flow(client):
    """Test case for create_flow

    
    """
    body = {"destinationFlowConfigList":"","triggerConfig":{"triggerProperties":{"Scheduled":{"scheduleOffset":"","scheduleExpression":"","timezone":"","flowErrorDeactivationThreshold":"","dataPullMode":"","firstExecutionFrom":"","scheduleStartTime":"","scheduleEndTime":""}},"triggerType":""},"sourceFlowConfig":{"connectorType":"","apiVersion":"","connectorProfileName":"","incrementalPullConfig":{"datetimeTypeFieldName":""},"sourceConnectorProperties":{"Amplitude":{"object":""},"S3":{"bucketName":"","bucketPrefix":"","s3InputFormatConfig":{"s3InputFileType":""}},"GoogleAnalytics":{"object":""},"ServiceNow":{"object":""},"CustomConnector":{"customProperties":"","entityName":"","dataTransferApi":{"Type":"","Name":""}},"SAPOData":{"objectPath":""},"Pardot":{"object":""},"Veeva":{"includeSourceFiles":"","documentType":"","includeAllVersions":"","includeRenditions":"","object":""},"Trendmicro":{"object":""},"Datadog":{"object":""},"Marketo":{"object":""},"Singular":{"object":""},"Slack":{"object":""},"Dynatrace":{"object":""},"Zendesk":{"object":""},"InforNexus":{"object":""},"Salesforce":{"includeDeletedRecords":"","enableDynamicFieldUpdate":"","object":"","dataTransferApi":""}}},"clientToken":"","kmsArn":"","description":"","flowName":"","metadataCatalogConfig":{"glueDataCatalog":{"databaseName":"","tablePrefix":"","roleArn":""}},"tasks":"","tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/create-flow',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_connector_profile(client):
    """Test case for delete_connector_profile

    
    """
    body = {"forceDelete":"","connectorProfileName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/delete-connector-profile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_flow(client):
    """Test case for delete_flow

    
    """
    body = {"forceDelete":"","flowName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/delete-flow',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_connector(client):
    """Test case for describe_connector

    
    """
    body = {"connectorType":"","connectorLabel":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/describe-connector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_connector_entity(client):
    """Test case for describe_connector_entity

    
    """
    body = {"connectorType":"","apiVersion":"","connectorProfileName":"","connectorEntityName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/describe-connector-entity',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_connector_profiles(client):
    """Test case for describe_connector_profiles

    
    """
    body = {"connectorType":"","maxResults":"","nextToken":"","connectorProfileNames":"","connectorLabel":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/describe-connector-profiles',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_connectors(client):
    """Test case for describe_connectors

    
    """
    body = {"connectorTypes":"","maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/describe-connectors',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_flow(client):
    """Test case for describe_flow

    
    """
    body = {"flowName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/describe-flow',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_flow_execution_records(client):
    """Test case for describe_flow_execution_records

    
    """
    body = {"maxResults":"","nextToken":"","flowName":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/describe-flow-execution-records',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_connector_entities(client):
    """Test case for list_connector_entities

    
    """
    body = {"connectorType":"","apiVersion":"","connectorProfileName":"","maxResults":"","nextToken":"","entitiesPath":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/list-connector-entities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_connectors(client):
    """Test case for list_connectors

    
    """
    body = {"maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/list-connectors',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_flows(client):
    """Test case for list_flows

    
    """
    body = {"maxResults":"","nextToken":""}
    params = [('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/list-flows',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_connector(client):
    """Test case for register_connector

    
    """
    body = {"connectorProvisioningType":"","clientToken":"","connectorLabel":"","description":"","connectorProvisioningConfig":{"lambda":{"lambdaArn":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/register-connector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_connector_metadata_cache(client):
    """Test case for reset_connector_metadata_cache

    
    """
    body = {"connectorType":"","apiVersion":"","connectorProfileName":"","connectorEntityName":"","entitiesPath":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/reset-connector-metadata-cache',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_flow(client):
    """Test case for start_flow

    
    """
    body = {"clientToken":"","flowName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/start-flow',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_flow(client):
    """Test case for stop_flow

    
    """
    body = {"flowName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/stop-flow',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unregister_connector(client):
    """Test case for unregister_connector

    
    """
    body = {"forceDelete":"","connectorLabel":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/unregister-connector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    params = [('tagKeys', ['tag_keys_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tags/{resource_arntag_key}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_connector_profile(client):
    """Test case for update_connector_profile

    
    """
    body = {"connectorProfileConfig":{"connectorProfileCredentials":{"Amplitude":{"apiKey":"","secretKey":""},"GoogleAnalytics":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":"","refreshToken":""},"ServiceNow":{"password":"","username":""},"CustomConnector":{"apiKey":{"apiKey":"","apiSecretKey":""},"custom":{"customAuthenticationType":"","credentialsMap":""},"authenticationType":"","basic":{"password":"","username":""},"oauth2":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":"","refreshToken":""}},"SAPOData":{"basicAuthCredentials":{"password":"","username":""},"oAuthCredentials":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":"","refreshToken":""}},"Pardot":{"oAuthRequest":{"redirectUri":"","authCode":""},"accessToken":"","clientCredentialsArn":"","refreshToken":""},"Honeycode":{"oAuthRequest":{"redirectUri":"","authCode":""},"accessToken":"","refreshToken":""},"Veeva":{"password":"","username":""},"Trendmicro":{"apiSecretKey":""},"Datadog":{"apiKey":"","applicationKey":""},"Marketo":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":""},"Redshift":{"password":"","username":""},"Singular":{"apiKey":""},"Slack":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":""},"Snowflake":{"password":"","username":""},"Dynatrace":{"apiToken":""},"Zendesk":{"clientId":"","oAuthRequest":{"redirectUri":"","authCode":""},"clientSecret":"","accessToken":""},"InforNexus":{"accessKeyId":"","secretAccessKey":"","datakey":"","userId":""},"Salesforce":{"oAuthRequest":{"redirectUri":"","authCode":""},"oAuth2GrantType":"","jwtToken":"","accessToken":"","clientCredentialsArn":"","refreshToken":""}},"connectorProfileProperties":{"Amplitude":"","GoogleAnalytics":"","ServiceNow":{"instanceUrl":""},"CustomConnector":{"oAuth2Properties":{"tokenUrl":"","tokenUrlCustomProperties":"","oAuth2GrantType":""},"profileProperties":""},"SAPOData":{"privateLinkServiceName":"","logonLanguage":"","oAuthProperties":{"tokenUrl":"","oAuthScopes":"","authCodeUrl":""},"disableSSO":"","applicationHostUrl":"","applicationServicePath":"","clientNumber":"","portNumber":""},"Pardot":{"isSandboxEnvironment":"","businessUnitId":"","instanceUrl":""},"Honeycode":"","Veeva":{"instanceUrl":""},"Trendmicro":"","Datadog":{"instanceUrl":""},"Marketo":{"instanceUrl":""},"Redshift":{"bucketName":"","databaseName":"","roleArn":"","bucketPrefix":"","workgroupName":"","clusterIdentifier":"","isRedshiftServerless":"","dataApiRoleArn":"","databaseUrl":""},"Singular":"","Slack":{"instanceUrl":""},"Snowflake":{"bucketName":"","privateLinkServiceName":"","stage":"","accountName":"","bucketPrefix":"","warehouse":"","region":""},"Dynatrace":{"instanceUrl":""},"Zendesk":{"instanceUrl":""},"InforNexus":{"instanceUrl":""},"Salesforce":{"isSandboxEnvironment":"","usePrivateLinkForMetadataAndAuthorization":"","instanceUrl":""}}},"connectionMode":"","connectorProfileName":"","clientToken":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/update-connector-profile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_connector_registration(client):
    """Test case for update_connector_registration

    
    """
    body = {"clientToken":"","connectorLabel":"","description":"","connectorProvisioningConfig":{"lambda":{"lambdaArn":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/update-connector-registration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_flow(client):
    """Test case for update_flow

    
    """
    body = {"destinationFlowConfigList":"","triggerConfig":{"triggerProperties":{"Scheduled":{"scheduleOffset":"","scheduleExpression":"","timezone":"","flowErrorDeactivationThreshold":"","dataPullMode":"","firstExecutionFrom":"","scheduleStartTime":"","scheduleEndTime":""}},"triggerType":""},"sourceFlowConfig":{"connectorType":"","apiVersion":"","connectorProfileName":"","incrementalPullConfig":{"datetimeTypeFieldName":""},"sourceConnectorProperties":{"Amplitude":{"object":""},"S3":{"bucketName":"","bucketPrefix":"","s3InputFormatConfig":{"s3InputFileType":""}},"GoogleAnalytics":{"object":""},"ServiceNow":{"object":""},"CustomConnector":{"customProperties":"","entityName":"","dataTransferApi":{"Type":"","Name":""}},"SAPOData":{"objectPath":""},"Pardot":{"object":""},"Veeva":{"includeSourceFiles":"","documentType":"","includeAllVersions":"","includeRenditions":"","object":""},"Trendmicro":{"object":""},"Datadog":{"object":""},"Marketo":{"object":""},"Singular":{"object":""},"Slack":{"object":""},"Dynatrace":{"object":""},"Zendesk":{"object":""},"InforNexus":{"object":""},"Salesforce":{"includeDeletedRecords":"","enableDynamicFieldUpdate":"","object":"","dataTransferApi":""}}},"clientToken":"","description":"","flowName":"","metadataCatalogConfig":{"glueDataCatalog":{"databaseName":"","tablePrefix":"","roleArn":""}},"tasks":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/update-flow',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

