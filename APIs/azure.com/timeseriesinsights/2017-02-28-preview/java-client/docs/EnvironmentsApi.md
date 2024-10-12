# EnvironmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**environmentsCreateOrUpdate**](EnvironmentsApi.md#environmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName} |  |
| [**environmentsDelete**](EnvironmentsApi.md#environmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName} |  |
| [**environmentsGet**](EnvironmentsApi.md#environmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName} |  |
| [**environmentsListByResourceGroup**](EnvironmentsApi.md#environmentsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments |  |
| [**environmentsListBySubscription**](EnvironmentsApi.md#environmentsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.TimeSeriesInsights/environments |  |
| [**environmentsUpdate**](EnvironmentsApi.md#environmentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName} |  |


<a id="environmentsCreateOrUpdate"></a>
# **environmentsCreateOrUpdate**
> EnvironmentResource environmentsCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, apiVersion, parameters)



Create or update an environment in the specified subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | Name of the environment
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    EnvironmentCreateOrUpdateParameters parameters = new EnvironmentCreateOrUpdateParameters(); // EnvironmentCreateOrUpdateParameters | Parameters for creating an environment resource.
    try {
      EnvironmentResource result = apiInstance.environmentsCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsCreateOrUpdate");
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
| **environmentName** | **String**| Name of the environment | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |
| **parameters** | [**EnvironmentCreateOrUpdateParameters**](EnvironmentCreateOrUpdateParameters.md)| Parameters for creating an environment resource. | |

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The existing environment definition was successfully updated. |  -  |
| **201** | The environment create request was accepted. Environment provisioning is an asynchronous operation. You can periodically get your environment definition and monitor progress via the provisioningState property. |  -  |
| **404** | The subscription or resource group could not be found. |  -  |
| **0** | HTTP 400 (Bad Request): The given environment request body is invalid; See the error code and message in the response for details. |  -  |

<a id="environmentsDelete"></a>
# **environmentsDelete**
> environmentsDelete(subscriptionId, resourceGroupName, environmentName, apiVersion)



Deletes the environment with the specified name in the specified subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      apiInstance.environmentsDelete(subscriptionId, resourceGroupName, environmentName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsDelete");
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

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The environment was successfully deleted. |  -  |
| **204** | The environment was successfully deleted. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, or environment could not be found. |  -  |

<a id="environmentsGet"></a>
# **environmentsGet**
> EnvironmentResource environmentsGet(subscriptionId, resourceGroupName, environmentName, apiVersion)



Gets the environment with the specified name in the specified subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      EnvironmentResource result = apiInstance.environmentsGet(subscriptionId, resourceGroupName, environmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsGet");
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

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The environment definition was successfully retrieved and is in the response. If you are polling for the completion of a provisioning or scale operation, you can check its status via the provisioningState property. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, or environment could not be found. |  -  |

<a id="environmentsListByResourceGroup"></a>
# **environmentsListByResourceGroup**
> EnvironmentListResponse environmentsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the available environments associated with the subscription and within the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      EnvironmentListResponse result = apiInstance.environmentsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsListByResourceGroup");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |

### Return type

[**EnvironmentListResponse**](EnvironmentListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Environments returned successfully. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, or resource group could not be found. |  -  |

<a id="environmentsListBySubscription"></a>
# **environmentsListBySubscription**
> EnvironmentListResponse environmentsListBySubscription(subscriptionId, apiVersion)



Lists all the available environments within a subscription, irrespective of the resource groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      EnvironmentListResponse result = apiInstance.environmentsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsListBySubscription");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |

### Return type

[**EnvironmentListResponse**](EnvironmentListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Environments returned successfully. |  -  |
| **0** | HTTP 404 (Not Found): The subscription could not be found. |  -  |

<a id="environmentsUpdate"></a>
# **environmentsUpdate**
> EnvironmentResource environmentsUpdate(subscriptionId, resourceGroupName, environmentName, apiVersion, environmentUpdateParameters)



Updates the environment with the specified name in the specified subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentsApi apiInstance = new EnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    EnvironmentUpdateParameters environmentUpdateParameters = new EnvironmentUpdateParameters(); // EnvironmentUpdateParameters | Request object that contains the updated information for the environment.
    try {
      EnvironmentResource result = apiInstance.environmentsUpdate(subscriptionId, resourceGroupName, environmentName, apiVersion, environmentUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentsApi#environmentsUpdate");
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
| **environmentUpdateParameters** | [**EnvironmentUpdateParameters**](EnvironmentUpdateParameters.md)| Request object that contains the updated information for the environment. | |

### Return type

[**EnvironmentResource**](EnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The environment definition was successfully updated and is in the response. If the environment was updated synchronously, the response will include a provisioningState value of \&quot;Succeeded\&quot;. If the environment was updated asynchronously, the response will include a provisioningState value of \&quot;Updating\&quot;.  You can periodically get your environment definition and monitor progress of the update via the provisioningState property. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, or environment could not be found. |  -  |

