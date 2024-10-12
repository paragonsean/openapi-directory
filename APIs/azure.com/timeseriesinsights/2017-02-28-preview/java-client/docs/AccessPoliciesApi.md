# AccessPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accessPoliciesCreateOrUpdate**](AccessPoliciesApi.md#accessPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName} |  |
| [**accessPoliciesDelete**](AccessPoliciesApi.md#accessPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName} |  |
| [**accessPoliciesGet**](AccessPoliciesApi.md#accessPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName} |  |
| [**accessPoliciesListByEnvironment**](AccessPoliciesApi.md#accessPoliciesListByEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies |  |
| [**accessPoliciesUpdate**](AccessPoliciesApi.md#accessPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/accessPolicies/{accessPolicyName} |  |


<a id="accessPoliciesCreateOrUpdate"></a>
# **accessPoliciesCreateOrUpdate**
> AccessPolicyResource accessPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, parameters)



Create or update an access policy in the specified environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String accessPolicyName = "accessPolicyName_example"; // String | Name of the access policy.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    AccessPolicyCreateOrUpdateParameters parameters = new AccessPolicyCreateOrUpdateParameters(); // AccessPolicyCreateOrUpdateParameters | Parameters for creating an access policy.
    try {
      AccessPolicyResource result = apiInstance.accessPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#accessPoliciesCreateOrUpdate");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **accessPolicyName** | **String**| Name of the access policy. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |
| **parameters** | [**AccessPolicyCreateOrUpdateParameters**](AccessPolicyCreateOrUpdateParameters.md)| Parameters for creating an access policy. | |

### Return type

[**AccessPolicyResource**](AccessPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The existing access policy definition was successfully updated. |  -  |
| **201** | The access policy was successfully created. |  -  |
| **0** | HTTP 400 (Bad Request): The given access policy request body is invalid; See the error code and message in the response for details. |  -  |

<a id="accessPoliciesDelete"></a>
# **accessPoliciesDelete**
> accessPoliciesDelete(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion)



Deletes the access policy with the specified name in the specified subscription, resource group, and environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String accessPolicyName = "accessPolicyName_example"; // String | The name of the Time Series Insights access policy associated with the specified environment.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      apiInstance.accessPoliciesDelete(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#accessPoliciesDelete");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **accessPolicyName** | **String**| The name of the Time Series Insights access policy associated with the specified environment. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The access policy was successfully deleted. |  -  |
| **204** | The access policy was successfully deleted. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, environment, or access policy could not be found. |  -  |

<a id="accessPoliciesGet"></a>
# **accessPoliciesGet**
> AccessPolicyResource accessPoliciesGet(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion)



Gets the access policy with the specified name in the specified environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String accessPolicyName = "accessPolicyName_example"; // String | The name of the Time Series Insights access policy associated with the specified environment.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      AccessPolicyResource result = apiInstance.accessPoliciesGet(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#accessPoliciesGet");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **accessPolicyName** | **String**| The name of the Time Series Insights access policy associated with the specified environment. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |

### Return type

[**AccessPolicyResource**](AccessPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The access policy definition was successfully retrieved and is in the response. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, environment, or access policy could not be found. |  -  |

<a id="accessPoliciesListByEnvironment"></a>
# **accessPoliciesListByEnvironment**
> AccessPolicyListResponse accessPoliciesListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion)



Lists all the available access policies associated with the environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      AccessPolicyListResponse result = apiInstance.accessPoliciesListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#accessPoliciesListByEnvironment");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |

### Return type

[**AccessPolicyListResponse**](AccessPolicyListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | access policies returned successfully. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, or environment could not be found. |  -  |

<a id="accessPoliciesUpdate"></a>
# **accessPoliciesUpdate**
> AccessPolicyResource accessPoliciesUpdate(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, accessPolicyUpdateParameters)



Updates the access policy with the specified name in the specified subscription, resource group, and environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccessPoliciesApi apiInstance = new AccessPoliciesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String accessPolicyName = "accessPolicyName_example"; // String | The name of the Time Series Insights access policy associated with the specified environment.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    AccessPolicyUpdateParameters accessPolicyUpdateParameters = new AccessPolicyUpdateParameters(); // AccessPolicyUpdateParameters | Request object that contains the updated information for the access policy.
    try {
      AccessPolicyResource result = apiInstance.accessPoliciesUpdate(subscriptionId, resourceGroupName, environmentName, accessPolicyName, apiVersion, accessPolicyUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessPoliciesApi#accessPoliciesUpdate");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **accessPolicyName** | **String**| The name of the Time Series Insights access policy associated with the specified environment. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |
| **accessPolicyUpdateParameters** | [**AccessPolicyUpdateParameters**](AccessPolicyUpdateParameters.md)| Request object that contains the updated information for the access policy. | |

### Return type

[**AccessPolicyResource**](AccessPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The access policy definition was successfully updated and is in the response. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, environment, or access policy could not be found. |  -  |

