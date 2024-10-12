from typing import List, Dict
from aiohttp import web

from openapi_server.models.integration_configuration import IntegrationConfiguration
from openapi_server.models.integration_configurations import IntegrationConfigurations
from openapi_server import util


async def create_integration(request: web.Request, owner, api, version, integration_type_configuration) -> web.Response:
    """Create an integration for the specified API and version

    Use this operation to configure an integration for a specific API version. The integration type is determined by which object is provided in the request body (specifically, by the &#x60;configType&#x60; value).  For a list of fields that need to be provided in the request body, see the descriptions of the following objects in the \&quot;Models\&quot; section at the bottom of API docs:   * &#x60;AmazonApiGatewayIntegration&#x60;  * &#x60;AmazonApiGatewayLambdaIntegration&#x60;  * &#x60;ApigeeEdgeIntegration&#x60;  * &#x60;AutoMockingIntegration&#x60;  * &#x60;AzureApiManagementIntegration&#x60;  * &#x60;AzureDevopsServicesIntegration&#x60;  * &#x60;BitbucketCloudIntegration&#x60;  * &#x60;BitbucketServerIntegration&#x60;  * &#x60;GitHubIntegration&#x60;  * &#x60;GitHubEnterpriseIntegration&#x60;  * &#x60;GitLabIntegration&#x60;  * &#x60;IBMApiConnectIntegration&#x60;  * &#x60;WebhookIntegration&#x60;  **Notes:**   * The integration &#x60;name&#x60; must be unique among all integrations configured for the given API version.   * If &#x60;target&#x60; is the YAMl/JSON definition, you must specify the &#x60;outputFile&#x60;.   * If &#x60;syncMethod&#x60;&#x3D;_Advanced Sync_, you must specify a non-empty list of either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60; (or both). If you are not sure which paths to use, use &#x60;providedPaths&#x60;&#x3D;&#x60;[\&quot;*\&quot;]&#x60;.   * The operation does not validate the repository details and access tokens.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param integration_type_configuration: Can be one of the following objects:  | &#x60;configType&#x60; value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations
    :type integration_type_configuration: 

    """
    return web.Response(status=200)


async def delete_integration(request: web.Request, owner, api, version, integration_id) -> web.Response:
    """Delete an integration

    Delete an existing integration specified by its ID.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param integration_id: Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60;
    :type integration_id: str
    :type integration_id: str

    """
    return web.Response(status=200)


async def execute_integration(request: web.Request, owner, api, version, integration_id, commit_message=None) -> web.Response:
    """Run an integration

    Use this operation to trigger an existing integration.  Source control integrations push to (not pull from) the configured repository and branch. You can optionally provide a custom commit message.  **Note:** Webhooks cannot be triggered by this operation, they are only triggered when an API is saved or published. An attempt to trigger a webhook will return status code 400.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param integration_id: Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60;
    :type integration_id: str
    :type integration_id: str
    :param commit_message: Commit message for source control integrations
    :type commit_message: str

    """
    return web.Response(status=200)


async def get_integration_by_id(request: web.Request, owner, api, version, integration_id) -> web.Response:
    """Get integration settings

    Returns the configuration of the specified integration. Access tokens and passwords are not returned for security reasons.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param integration_id: Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60;
    :type integration_id: str
    :type integration_id: str

    """
    return web.Response(status=200)


async def get_integrations(request: web.Request, owner, api, version) -> web.Response:
    """Get all integrations configured for the specified API version

    The returned information includes integration types, names, unique IDs, and enabled/disabled status.  **Note:** The following integration types are currently not returned: Amazon API Gateway Lambda Sync, Apigee Edge, Azure API Management, IBM API Connect.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def patch_integration(request: web.Request, owner, api, version, integration_id, integration_type_configuration) -> web.Response:
    """Partially update integration settings

    Use this operation to partially update integration settings for the specified API and integration ID. For example, enable or disable an integration, or specify a new access token.  Only the fields provided in the request body will be updated; other settings will remain unchanged. For a list of fields that can be updated, see the following objects in the \&quot;Models\&quot; section at the bottom of API docs:   * &#x60;AmazonApiGatewayIntegration&#x60;  * &#x60;AmazonApiGatewayLambdaIntegration&#x60;  * &#x60;ApigeeEdgeIntegration&#x60;  * &#x60;AutoMockingIntegration&#x60;  * &#x60;AzureApiManagementIntegration&#x60;  * &#x60;AzureDevopsServicesIntegration&#x60;  * &#x60;BitbucketCloudIntegration&#x60;  * &#x60;BitbucketServerIntegration&#x60;  * &#x60;GitHubIntegration&#x60;  * &#x60;GitHubEnterpriseIntegration&#x60;  * &#x60;GitLabIntegration&#x60;  * &#x60;IBMApiConnectIntegration&#x60;  * &#x60;WebhookIntegration&#x60;  **Notes:**   * &#x60;configType&#x60; (integration type) cannot be changed.   * If updating the integration &#x60;name&#x60;, make sure the new name is unique among all integrations configured for the given API version.   * If you change &#x60;target&#x60; to the YAMl/JSON definition, you must also specify the &#x60;outputFile&#x60;.   * If you change &#x60;syncMethod&#x60; to _Advanced Sync_, you must also specify a non-empty list of either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60; (or both). If you are not sure which paths to use, use &#x60;providedPaths&#x60;&#x3D;&#x60;[\&quot;*\&quot;]&#x60;.   * The update operation does not validate the repository details and access tokens.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param integration_id: Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60;
    :type integration_id: str
    :type integration_id: str
    :param integration_type_configuration: An object that contains the integration parameters you want to update
    :type integration_type_configuration: 

    """
    return web.Response(status=200)


async def update_integration(request: web.Request, owner, api, version, integration_id, integration_type_configuration) -> web.Response:
    """Update integration settings

    Updates integration settings for the specified API and integration ID. The integration type is determined by which object is passed in the request body.  The request body must contain a **full representation** of an integration object. If you want to update just a few parameters, use the PATCH operation instead.  For a list of fields that need to be provided in the request body, see the descriptions of the following objects in the \&quot;Models\&quot; section at the bottom of API docs:   * &#x60;AmazonApiGatewayIntegration&#x60;  * &#x60;AmazonApiGatewayLambdaIntegration&#x60;  * &#x60;ApigeeEdgeIntegration&#x60;  * &#x60;AutoMockingIntegration&#x60;  * &#x60;AzureApiManagementIntegration&#x60;  * &#x60;AzureDevopsServicesIntegration&#x60;  * &#x60;BitbucketCloudIntegration&#x60;  * &#x60;BitbucketServerIntegration&#x60;  * &#x60;GitHubIntegration&#x60;  * &#x60;GitHubEnterpriseIntegration&#x60;  * &#x60;GitLabIntegration&#x60;  * &#x60;IBMApiConnectIntegration&#x60;  * &#x60;WebhookIntegration&#x60;  **Notes:**   * The integration &#x60;name&#x60; must be unique among all integrations configured for the given API version.   * If &#x60;target&#x60; is the YAMl/JSON definition, you must specify the &#x60;outputFile&#x60;.   * If &#x60;syncMethod&#x60;&#x3D;_Advanced Sync_, you must specify a non-empty list of either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60; (or both). If you are not sure which paths to use, use &#x60;providedPaths&#x60;&#x3D;&#x60;[\&quot;*\&quot;]&#x60;.   * The operation does not validate the repository details and access tokens.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param integration_id: Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60;
    :type integration_id: str
    :type integration_id: str
    :param integration_type_configuration: Can be one of the following objects:  | &#x60;configType&#x60; value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations
    :type integration_type_configuration: 

    """
    return web.Response(status=200)
