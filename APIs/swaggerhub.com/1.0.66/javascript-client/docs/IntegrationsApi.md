# SwaggerHubRegistryApi.IntegrationsApi

All URIs are relative to *https://api.swaggerhub.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIntegration**](IntegrationsApi.md#createIntegration) | **POST** /apis/{owner}/{api}/{version}/integrations | Create an integration for the specified API and version
[**deleteIntegration**](IntegrationsApi.md#deleteIntegration) | **DELETE** /apis/{owner}/{api}/{version}/integrations/{integrationId} | Delete an integration
[**executeIntegration**](IntegrationsApi.md#executeIntegration) | **POST** /apis/{owner}/{api}/{version}/integrations/{integrationId}/execute | Run an integration
[**getIntegrationById**](IntegrationsApi.md#getIntegrationById) | **GET** /apis/{owner}/{api}/{version}/integrations/{integrationId} | Get integration settings
[**getIntegrations**](IntegrationsApi.md#getIntegrations) | **GET** /apis/{owner}/{api}/{version}/integrations | Get all integrations configured for the specified API version
[**patchIntegration**](IntegrationsApi.md#patchIntegration) | **PATCH** /apis/{owner}/{api}/{version}/integrations/{integrationId} | Partially update integration settings
[**updateIntegration**](IntegrationsApi.md#updateIntegration) | **PUT** /apis/{owner}/{api}/{version}/integrations/{integrationId} | Update integration settings



## createIntegration

> IntegrationConfiguration createIntegration(owner, api, version, integrationTypeConfiguration)

Create an integration for the specified API and version

Use this operation to configure an integration for a specific API version. The integration type is determined by which object is provided in the request body (specifically, by the &#x60;configType&#x60; value).  For a list of fields that need to be provided in the request body, see the descriptions of the following objects in the \&quot;Models\&quot; section at the bottom of API docs:   * &#x60;AmazonApiGatewayIntegration&#x60;  * &#x60;AmazonApiGatewayLambdaIntegration&#x60;  * &#x60;ApigeeEdgeIntegration&#x60;  * &#x60;AutoMockingIntegration&#x60;  * &#x60;AzureApiManagementIntegration&#x60;  * &#x60;AzureDevopsServicesIntegration&#x60;  * &#x60;BitbucketCloudIntegration&#x60;  * &#x60;BitbucketServerIntegration&#x60;  * &#x60;GitHubIntegration&#x60;  * &#x60;GitHubEnterpriseIntegration&#x60;  * &#x60;GitLabIntegration&#x60;  * &#x60;IBMApiConnectIntegration&#x60;  * &#x60;WebhookIntegration&#x60;  **Notes:**   * The integration &#x60;name&#x60; must be unique among all integrations configured for the given API version.   * If &#x60;target&#x60; is the YAMl/JSON definition, you must specify the &#x60;outputFile&#x60;.   * If &#x60;syncMethod&#x60;&#x3D;_Advanced Sync_, you must specify a non-empty list of either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60; (or both). If you are not sure which paths to use, use &#x60;providedPaths&#x60;&#x3D;&#x60;[\&quot;*\&quot;]&#x60;.   * The operation does not validate the repository details and access tokens.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.IntegrationsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let integrationTypeConfiguration = {key: null}; // Object | Can be one of the following objects:  | `configType` value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations
apiInstance.createIntegration(owner, api, version, integrationTypeConfiguration, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **integrationTypeConfiguration** | **Object**| Can be one of the following objects:  | &#x60;configType&#x60; value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations | 

### Return type

[**IntegrationConfiguration**](IntegrationConfiguration.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteIntegration

> deleteIntegration(owner, api, version, integrationId)

Delete an integration

Delete an existing integration specified by its ID.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.IntegrationsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let integrationId = "integrationId_example"; // String | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
apiInstance.deleteIntegration(owner, api, version, integrationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **integrationId** | **String**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## executeIntegration

> executeIntegration(owner, api, version, integrationId, opts)

Run an integration

Use this operation to trigger an existing integration.  Source control integrations push to (not pull from) the configured repository and branch. You can optionally provide a custom commit message.  **Note:** Webhooks cannot be triggered by this operation, they are only triggered when an API is saved or published. An attempt to trigger a webhook will return status code 400.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.IntegrationsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let integrationId = "integrationId_example"; // String | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
let opts = {
  'commitMessage': "commitMessage_example" // String | Commit message for source control integrations
};
apiInstance.executeIntegration(owner, api, version, integrationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **integrationId** | **String**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | 
 **commitMessage** | **String**| Commit message for source control integrations | [optional] 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIntegrationById

> IntegrationConfiguration getIntegrationById(owner, api, version, integrationId)

Get integration settings

Returns the configuration of the specified integration. Access tokens and passwords are not returned for security reasons.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.IntegrationsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let integrationId = "integrationId_example"; // String | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
apiInstance.getIntegrationById(owner, api, version, integrationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **integrationId** | **String**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | 

### Return type

[**IntegrationConfiguration**](IntegrationConfiguration.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegrations

> IntegrationConfigurations getIntegrations(owner, api, version)

Get all integrations configured for the specified API version

The returned information includes integration types, names, unique IDs, and enabled/disabled status.  **Note:** The following integration types are currently not returned: Amazon API Gateway Lambda Sync, Apigee Edge, Azure API Management, IBM API Connect.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.IntegrationsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
apiInstance.getIntegrations(owner, api, version, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 

### Return type

[**IntegrationConfigurations**](IntegrationConfigurations.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchIntegration

> patchIntegration(owner, api, version, integrationId, integrationTypeConfiguration)

Partially update integration settings

Use this operation to partially update integration settings for the specified API and integration ID. For example, enable or disable an integration, or specify a new access token.  Only the fields provided in the request body will be updated; other settings will remain unchanged. For a list of fields that can be updated, see the following objects in the \&quot;Models\&quot; section at the bottom of API docs:   * &#x60;AmazonApiGatewayIntegration&#x60;  * &#x60;AmazonApiGatewayLambdaIntegration&#x60;  * &#x60;ApigeeEdgeIntegration&#x60;  * &#x60;AutoMockingIntegration&#x60;  * &#x60;AzureApiManagementIntegration&#x60;  * &#x60;AzureDevopsServicesIntegration&#x60;  * &#x60;BitbucketCloudIntegration&#x60;  * &#x60;BitbucketServerIntegration&#x60;  * &#x60;GitHubIntegration&#x60;  * &#x60;GitHubEnterpriseIntegration&#x60;  * &#x60;GitLabIntegration&#x60;  * &#x60;IBMApiConnectIntegration&#x60;  * &#x60;WebhookIntegration&#x60;  **Notes:**   * &#x60;configType&#x60; (integration type) cannot be changed.   * If updating the integration &#x60;name&#x60;, make sure the new name is unique among all integrations configured for the given API version.   * If you change &#x60;target&#x60; to the YAMl/JSON definition, you must also specify the &#x60;outputFile&#x60;.   * If you change &#x60;syncMethod&#x60; to _Advanced Sync_, you must also specify a non-empty list of either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60; (or both). If you are not sure which paths to use, use &#x60;providedPaths&#x60;&#x3D;&#x60;[\&quot;*\&quot;]&#x60;.   * The update operation does not validate the repository details and access tokens.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.IntegrationsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let integrationId = "integrationId_example"; // String | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
let integrationTypeConfiguration = {key: null}; // Object | An object that contains the integration parameters you want to update
apiInstance.patchIntegration(owner, api, version, integrationId, integrationTypeConfiguration, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **integrationId** | **String**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | 
 **integrationTypeConfiguration** | **Object**| An object that contains the integration parameters you want to update | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateIntegration

> updateIntegration(owner, api, version, integrationId, integrationTypeConfiguration)

Update integration settings

Updates integration settings for the specified API and integration ID. The integration type is determined by which object is passed in the request body.  The request body must contain a **full representation** of an integration object. If you want to update just a few parameters, use the PATCH operation instead.  For a list of fields that need to be provided in the request body, see the descriptions of the following objects in the \&quot;Models\&quot; section at the bottom of API docs:   * &#x60;AmazonApiGatewayIntegration&#x60;  * &#x60;AmazonApiGatewayLambdaIntegration&#x60;  * &#x60;ApigeeEdgeIntegration&#x60;  * &#x60;AutoMockingIntegration&#x60;  * &#x60;AzureApiManagementIntegration&#x60;  * &#x60;AzureDevopsServicesIntegration&#x60;  * &#x60;BitbucketCloudIntegration&#x60;  * &#x60;BitbucketServerIntegration&#x60;  * &#x60;GitHubIntegration&#x60;  * &#x60;GitHubEnterpriseIntegration&#x60;  * &#x60;GitLabIntegration&#x60;  * &#x60;IBMApiConnectIntegration&#x60;  * &#x60;WebhookIntegration&#x60;  **Notes:**   * The integration &#x60;name&#x60; must be unique among all integrations configured for the given API version.   * If &#x60;target&#x60; is the YAMl/JSON definition, you must specify the &#x60;outputFile&#x60;.   * If &#x60;syncMethod&#x60;&#x3D;_Advanced Sync_, you must specify a non-empty list of either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60; (or both). If you are not sure which paths to use, use &#x60;providedPaths&#x60;&#x3D;&#x60;[\&quot;*\&quot;]&#x60;.   * The operation does not validate the repository details and access tokens.

### Example

```javascript
import SwaggerHubRegistryApi from 'swagger_hub_registry_api';
let defaultClient = SwaggerHubRegistryApi.ApiClient.instance;
// Configure API key authorization: TokenSecured
let TokenSecured = defaultClient.authentications['TokenSecured'];
TokenSecured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenSecured.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerHubRegistryApi.IntegrationsApi();
let owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
let api = "api_example"; // String | API name (case-sensitive)
let version = "version_example"; // String | Version identifier
let integrationId = "integrationId_example"; // String | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
let integrationTypeConfiguration = {key: null}; // Object | Can be one of the following objects:  | `configType` value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations
apiInstance.updateIntegration(owner, api, version, integrationId, integrationTypeConfiguration, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| API owner (organization or user, case-sensitive) | 
 **api** | **String**| API name (case-sensitive) | 
 **version** | **String**| Version identifier | 
 **integrationId** | **String**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | 
 **integrationTypeConfiguration** | **Object**| Can be one of the following objects:  | &#x60;configType&#x60; value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations | 

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

