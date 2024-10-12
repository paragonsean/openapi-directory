# EventSourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventSourcesCreateOrUpdate**](EventSourcesApi.md#eventSourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName} |  |
| [**eventSourcesDelete**](EventSourcesApi.md#eventSourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName} |  |
| [**eventSourcesGet**](EventSourcesApi.md#eventSourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName} |  |
| [**eventSourcesListByEnvironment**](EventSourcesApi.md#eventSourcesListByEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources |  |
| [**eventSourcesUpdate**](EventSourcesApi.md#eventSourcesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/eventSources/{eventSourceName} |  |


<a id="eventSourcesCreateOrUpdate"></a>
# **eventSourcesCreateOrUpdate**
> EventSourceResource eventSourcesCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, parameters)



Create or update an event source under the specified environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventSourcesApi apiInstance = new EventSourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String eventSourceName = "eventSourceName_example"; // String | Name of the event source.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    EventSourceCreateOrUpdateParameters parameters = new EventSourceCreateOrUpdateParameters(); // EventSourceCreateOrUpdateParameters | Parameters for creating an event source resource.
    try {
      EventSourceResource result = apiInstance.eventSourcesCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSourcesApi#eventSourcesCreateOrUpdate");
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
| **eventSourceName** | **String**| Name of the event source. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |
| **parameters** | [**EventSourceCreateOrUpdateParameters**](EventSourceCreateOrUpdateParameters.md)| Parameters for creating an event source resource. | |

### Return type

[**EventSourceResource**](EventSourceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The existing event source definition was successfully updated. |  -  |
| **201** | The event source was successfully created. |  -  |
| **0** | HTTP 400 (Bad Request): The given event source request body is invalid; See the error code and message in the response for details. |  -  |

<a id="eventSourcesDelete"></a>
# **eventSourcesDelete**
> eventSourcesDelete(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion)



Deletes the event source with the specified name in the specified subscription, resource group, and environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventSourcesApi apiInstance = new EventSourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String eventSourceName = "eventSourceName_example"; // String | The name of the Time Series Insights event source associated with the specified environment.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      apiInstance.eventSourcesDelete(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSourcesApi#eventSourcesDelete");
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
| **eventSourceName** | **String**| The name of the Time Series Insights event source associated with the specified environment. | |
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
| **200** | The event source was successfully deleted. |  -  |
| **204** | The event source was successfully deleted. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, environment, or event source could not be found. |  -  |

<a id="eventSourcesGet"></a>
# **eventSourcesGet**
> EventSourceResource eventSourcesGet(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion)



Gets the event source with the specified name in the specified environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventSourcesApi apiInstance = new EventSourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String eventSourceName = "eventSourceName_example"; // String | The name of the Time Series Insights event source associated with the specified environment.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      EventSourceResource result = apiInstance.eventSourcesGet(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSourcesApi#eventSourcesGet");
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
| **eventSourceName** | **String**| The name of the Time Series Insights event source associated with the specified environment. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |

### Return type

[**EventSourceResource**](EventSourceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The event source definition was successfully retrieved and is in the response. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, environment, or event source could not be found. |  -  |

<a id="eventSourcesListByEnvironment"></a>
# **eventSourcesListByEnvironment**
> EventSourceListResponse eventSourcesListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion)



Lists all the available event sources associated with the subscription and within the specified resource group and environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventSourcesApi apiInstance = new EventSourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    try {
      EventSourceListResponse result = apiInstance.eventSourcesListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSourcesApi#eventSourcesListByEnvironment");
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

[**EventSourceListResponse**](EventSourceListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Environments returned successfully. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, or environment could not be found. |  -  |

<a id="eventSourcesUpdate"></a>
# **eventSourcesUpdate**
> EventSourceResource eventSourcesUpdate(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, eventSourceUpdateParameters)



Updates the event source with the specified name in the specified subscription, resource group, and environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventSourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventSourcesApi apiInstance = new EventSourcesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String eventSourceName = "eventSourceName_example"; // String | The name of the Time Series Insights event source associated with the specified environment.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-02-28-preview.
    EventSourceUpdateParameters eventSourceUpdateParameters = new EventSourceUpdateParameters(); // EventSourceUpdateParameters | Request object that contains the updated information for the event source.
    try {
      EventSourceResource result = apiInstance.eventSourcesUpdate(subscriptionId, resourceGroupName, environmentName, eventSourceName, apiVersion, eventSourceUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventSourcesApi#eventSourcesUpdate");
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
| **eventSourceName** | **String**| The name of the Time Series Insights event source associated with the specified environment. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-02-28-preview. | |
| **eventSourceUpdateParameters** | [**EventSourceUpdateParameters**](EventSourceUpdateParameters.md)| Request object that contains the updated information for the event source. | |

### Return type

[**EventSourceResource**](EventSourceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The event source definition was successfully updated and is in the response. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, environment, or event source could not be found. |  -  |

