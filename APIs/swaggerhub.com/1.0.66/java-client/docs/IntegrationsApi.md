# IntegrationsApi

All URIs are relative to *https://api.swaggerhub.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIntegration**](IntegrationsApi.md#createIntegration) | **POST** /apis/{owner}/{api}/{version}/integrations | Create an integration for the specified API and version |
| [**deleteIntegration**](IntegrationsApi.md#deleteIntegration) | **DELETE** /apis/{owner}/{api}/{version}/integrations/{integrationId} | Delete an integration |
| [**executeIntegration**](IntegrationsApi.md#executeIntegration) | **POST** /apis/{owner}/{api}/{version}/integrations/{integrationId}/execute | Run an integration |
| [**getIntegrationById**](IntegrationsApi.md#getIntegrationById) | **GET** /apis/{owner}/{api}/{version}/integrations/{integrationId} | Get integration settings |
| [**getIntegrations**](IntegrationsApi.md#getIntegrations) | **GET** /apis/{owner}/{api}/{version}/integrations | Get all integrations configured for the specified API version |
| [**patchIntegration**](IntegrationsApi.md#patchIntegration) | **PATCH** /apis/{owner}/{api}/{version}/integrations/{integrationId} | Partially update integration settings |
| [**updateIntegration**](IntegrationsApi.md#updateIntegration) | **PUT** /apis/{owner}/{api}/{version}/integrations/{integrationId} | Update integration settings |


<a id="createIntegration"></a>
# **createIntegration**
> IntegrationConfiguration createIntegration(owner, api, version, integrationTypeConfiguration)

Create an integration for the specified API and version

Use this operation to configure an integration for a specific API version. The integration type is determined by which object is provided in the request body (specifically, by the &#x60;configType&#x60; value).  For a list of fields that need to be provided in the request body, see the descriptions of the following objects in the \&quot;Models\&quot; section at the bottom of API docs:   * &#x60;AmazonApiGatewayIntegration&#x60;  * &#x60;AmazonApiGatewayLambdaIntegration&#x60;  * &#x60;ApigeeEdgeIntegration&#x60;  * &#x60;AutoMockingIntegration&#x60;  * &#x60;AzureApiManagementIntegration&#x60;  * &#x60;AzureDevopsServicesIntegration&#x60;  * &#x60;BitbucketCloudIntegration&#x60;  * &#x60;BitbucketServerIntegration&#x60;  * &#x60;GitHubIntegration&#x60;  * &#x60;GitHubEnterpriseIntegration&#x60;  * &#x60;GitLabIntegration&#x60;  * &#x60;IBMApiConnectIntegration&#x60;  * &#x60;WebhookIntegration&#x60;  **Notes:**   * The integration &#x60;name&#x60; must be unique among all integrations configured for the given API version.   * If &#x60;target&#x60; is the YAMl/JSON definition, you must specify the &#x60;outputFile&#x60;.   * If &#x60;syncMethod&#x60;&#x3D;_Advanced Sync_, you must specify a non-empty list of either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60; (or both). If you are not sure which paths to use, use &#x60;providedPaths&#x60;&#x3D;&#x60;[\&quot;*\&quot;]&#x60;.   * The operation does not validate the repository details and access tokens.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    Object integrationTypeConfiguration = null; // Object | Can be one of the following objects:  | `configType` value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations
    try {
      IntegrationConfiguration result = apiInstance.createIntegration(owner, api, version, integrationTypeConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#createIntegration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **integrationTypeConfiguration** | **Object**| Can be one of the following objects:  | &#x60;configType&#x60; value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations | |

### Return type

[**IntegrationConfiguration**](IntegrationConfiguration.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The integration was successfully created. The response contains the auto-generated ID of the created integration and its confguration (excluding the access tokens and passwords). |  -  |
| **400** | The integration configuration was invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The authenticating user does not have permissions to create integrations in this API |  -  |
| **404** | The specified owner, API, or version was not found |  -  |
| **409** | An integration with this name already exists in this API |  -  |
| **415** | Invalid content type |  -  |

<a id="deleteIntegration"></a>
# **deleteIntegration**
> deleteIntegration(owner, api, version, integrationId)

Delete an integration

Delete an existing integration specified by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    UUID integrationId = UUID.randomUUID(); // UUID | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
    try {
      apiInstance.deleteIntegration(owner, api, version, integrationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#deleteIntegration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **integrationId** | **UUID**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The integration was successfully deleted |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The authenticating user does not have permissions to delete integrations from this API |  -  |
| **404** | The specified owner, API, version, or integration ID was not found |  -  |

<a id="executeIntegration"></a>
# **executeIntegration**
> executeIntegration(owner, api, version, integrationId, commitMessage)

Run an integration

Use this operation to trigger an existing integration.  Source control integrations push to (not pull from) the configured repository and branch. You can optionally provide a custom commit message.  **Note:** Webhooks cannot be triggered by this operation, they are only triggered when an API is saved or published. An attempt to trigger a webhook will return status code 400.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    UUID integrationId = UUID.randomUUID(); // UUID | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
    String commitMessage = "commitMessage_example"; // String | Commit message for source control integrations
    try {
      apiInstance.executeIntegration(owner, api, version, integrationId, commitMessage);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#executeIntegration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **integrationId** | **UUID**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | |
| **commitMessage** | **String**| Commit message for source control integrations | [optional] |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The integration was executed successfully |  -  |
| **205** | The integration was executed successfully and the API has been updated |  -  |
| **400** | The integration encountered an error while executing. Check that the integration settings (such as access tokens) are valid. |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The authenticating user does not have access to integrations in this API |  -  |
| **404** | The specified API or integration ID was not found |  -  |
| **409** | The specified integration is disabled |  -  |

<a id="getIntegrationById"></a>
# **getIntegrationById**
> IntegrationConfiguration getIntegrationById(owner, api, version, integrationId)

Get integration settings

Returns the configuration of the specified integration. Access tokens and passwords are not returned for security reasons.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    UUID integrationId = UUID.randomUUID(); // UUID | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
    try {
      IntegrationConfiguration result = apiInstance.getIntegrationById(owner, api, version, integrationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#getIntegrationById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **integrationId** | **UUID**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | |

### Return type

[**IntegrationConfiguration**](IntegrationConfiguration.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Can be one of the following objects: &#x60;AmazonApiGatewayIntegration&#x60;, &#x60;AmazonApiGatewayLambdaIntegration&#x60;, &#x60;ApigeeEdgeIntegration&#x60;, &#x60;AutoMockingIntegration&#x60;, &#x60;AzureApiManagementIntegration&#x60;, &#x60;AzureDevopsServicesIntegration&#x60;, &#x60;BitbucketCloudIntegration&#x60;, &#x60;BitbucketServerIntegration&#x60;, &#x60;GitHubIntegration&#x60;, &#x60;GitHubEnterpriseIntegration&#x60;, &#x60;GitLabIntegration&#x60;, &#x60;IBMApiConnectIntegration&#x60;, &#x60;WebhookIntegration&#x60;  |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The authenticating user does not have access to integrations in this API |  -  |
| **404** | The specified owner, API, version, or integration ID was not found |  -  |

<a id="getIntegrations"></a>
# **getIntegrations**
> IntegrationConfigurations getIntegrations(owner, api, version)

Get all integrations configured for the specified API version

The returned information includes integration types, names, unique IDs, and enabled/disabled status.  **Note:** The following integration types are currently not returned: Amazon API Gateway Lambda Sync, Apigee Edge, Azure API Management, IBM API Connect.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    try {
      IntegrationConfigurations result = apiInstance.getIntegrations(owner, api, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#getIntegrations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |

### Return type

[**IntegrationConfigurations**](IntegrationConfigurations.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object that contains information about the configured integrations |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The authenticating user does not have access to integrations in this API |  -  |
| **404** | The specified API or version was not found |  -  |

<a id="patchIntegration"></a>
# **patchIntegration**
> patchIntegration(owner, api, version, integrationId, integrationTypeConfiguration)

Partially update integration settings

Use this operation to partially update integration settings for the specified API and integration ID. For example, enable or disable an integration, or specify a new access token.  Only the fields provided in the request body will be updated; other settings will remain unchanged. For a list of fields that can be updated, see the following objects in the \&quot;Models\&quot; section at the bottom of API docs:   * &#x60;AmazonApiGatewayIntegration&#x60;  * &#x60;AmazonApiGatewayLambdaIntegration&#x60;  * &#x60;ApigeeEdgeIntegration&#x60;  * &#x60;AutoMockingIntegration&#x60;  * &#x60;AzureApiManagementIntegration&#x60;  * &#x60;AzureDevopsServicesIntegration&#x60;  * &#x60;BitbucketCloudIntegration&#x60;  * &#x60;BitbucketServerIntegration&#x60;  * &#x60;GitHubIntegration&#x60;  * &#x60;GitHubEnterpriseIntegration&#x60;  * &#x60;GitLabIntegration&#x60;  * &#x60;IBMApiConnectIntegration&#x60;  * &#x60;WebhookIntegration&#x60;  **Notes:**   * &#x60;configType&#x60; (integration type) cannot be changed.   * If updating the integration &#x60;name&#x60;, make sure the new name is unique among all integrations configured for the given API version.   * If you change &#x60;target&#x60; to the YAMl/JSON definition, you must also specify the &#x60;outputFile&#x60;.   * If you change &#x60;syncMethod&#x60; to _Advanced Sync_, you must also specify a non-empty list of either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60; (or both). If you are not sure which paths to use, use &#x60;providedPaths&#x60;&#x3D;&#x60;[\&quot;*\&quot;]&#x60;.   * The update operation does not validate the repository details and access tokens.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    UUID integrationId = UUID.randomUUID(); // UUID | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
    Object integrationTypeConfiguration = null; // Object | An object that contains the integration parameters you want to update
    try {
      apiInstance.patchIntegration(owner, api, version, integrationId, integrationTypeConfiguration);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#patchIntegration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **integrationId** | **UUID**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | |
| **integrationTypeConfiguration** | **Object**| An object that contains the integration parameters you want to update | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Integration was successfully updated |  -  |
| **400** | The specified integration configuration is invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The authenticating user does not have access to integrations in this API |  -  |
| **404** | The specified owner, API, version, or integration ID was not found |  -  |
| **415** | Invalid content type |  -  |

<a id="updateIntegration"></a>
# **updateIntegration**
> updateIntegration(owner, api, version, integrationId, integrationTypeConfiguration)

Update integration settings

Updates integration settings for the specified API and integration ID. The integration type is determined by which object is passed in the request body.  The request body must contain a **full representation** of an integration object. If you want to update just a few parameters, use the PATCH operation instead.  For a list of fields that need to be provided in the request body, see the descriptions of the following objects in the \&quot;Models\&quot; section at the bottom of API docs:   * &#x60;AmazonApiGatewayIntegration&#x60;  * &#x60;AmazonApiGatewayLambdaIntegration&#x60;  * &#x60;ApigeeEdgeIntegration&#x60;  * &#x60;AutoMockingIntegration&#x60;  * &#x60;AzureApiManagementIntegration&#x60;  * &#x60;AzureDevopsServicesIntegration&#x60;  * &#x60;BitbucketCloudIntegration&#x60;  * &#x60;BitbucketServerIntegration&#x60;  * &#x60;GitHubIntegration&#x60;  * &#x60;GitHubEnterpriseIntegration&#x60;  * &#x60;GitLabIntegration&#x60;  * &#x60;IBMApiConnectIntegration&#x60;  * &#x60;WebhookIntegration&#x60;  **Notes:**   * The integration &#x60;name&#x60; must be unique among all integrations configured for the given API version.   * If &#x60;target&#x60; is the YAMl/JSON definition, you must specify the &#x60;outputFile&#x60;.   * If &#x60;syncMethod&#x60;&#x3D;_Advanced Sync_, you must specify a non-empty list of either &#x60;providedPaths&#x60; or &#x60;managedPaths&#x60; (or both). If you are not sure which paths to use, use &#x60;providedPaths&#x60;&#x3D;&#x60;[\&quot;*\&quot;]&#x60;.   * The operation does not validate the repository details and access tokens.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String owner = "owner_example"; // String | API owner (organization or user, case-sensitive)
    String api = "api_example"; // String | API name (case-sensitive)
    String version = "version_example"; // String | Version identifier
    UUID integrationId = UUID.randomUUID(); // UUID | Integration ID (case-sensitive). To get the available integration IDs, use `GET /apis/{owner}/{api}/{version}/integrations`
    Object integrationTypeConfiguration = null; // Object | Can be one of the following objects:  | `configType` value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations
    try {
      apiInstance.updateIntegration(owner, api, version, integrationId, integrationTypeConfiguration);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#updateIntegration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**| API owner (organization or user, case-sensitive) | |
| **api** | **String**| API name (case-sensitive) | |
| **version** | **String**| Version identifier | |
| **integrationId** | **UUID**| Integration ID (case-sensitive). To get the available integration IDs, use &#x60;GET /apis/{owner}/{api}/{version}/integrations&#x60; | |
| **integrationTypeConfiguration** | **Object**| Can be one of the following objects:  | &#x60;configType&#x60; value        | Object | | ------------------------- | ------ | | AMAZON_API_GATEWAY        | AmazonApiGatewayIntegration | | AMAZON_API_GATEWAY_LAMBDA | AmazonApiGatewayLambdaIntegration | | API_AUTO_MOCKING          | AutoMockingIntegration | | APIGEE_EDGE               | ApigeeEdgeIntegration | | AZURE_API_MANAGEMENT      | AzureApiManagementIntegration | | AZURE_DEVOPS_SERVICES     | AzureDevopsServicesIntegration | | BITBUCKET_CLOUD           | BitbucketCloudIntegration | | BITBUCKET_SERVER          | BitbucketServerIntegration | | GITHUB                    | GitHubIntegration | | GITHUB_ENTERPRISE         | GitHubEnterpriseIntegration | | GITLAB                    | GitLabIntegration | | IBM_API_CONNECT           | IBMApiConnectIntegration | | WEBHOOK                   | WebhookIntegration |  For more examples, see the JSON files in this repository: https://github.com/SmartBear/swaggerhub-cli/tree/master/examples/integrations | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Integration was successfully updated |  -  |
| **400** | The specified integration configuration is invalid |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The authenticating user does not have access to integrations in this API |  -  |
| **404** | The specified combination of owner, API, version, integrationId, and configType was not found |  -  |
| **415** | Invalid content type |  -  |

