# InsightApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationInsightMonitoredMediaServer**](InsightApi.md#createOrganizationInsightMonitoredMediaServer) | **POST** /organizations/{organizationId}/insight/monitoredMediaServers | Add a media server to be monitored for this organization |
| [**deleteOrganizationInsightMonitoredMediaServer**](InsightApi.md#deleteOrganizationInsightMonitoredMediaServer) | **DELETE** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Delete a monitored media server from this organization |
| [**getNetworkInsightApplicationHealthByTime**](InsightApi.md#getNetworkInsightApplicationHealthByTime) | **GET** /networks/{networkId}/insight/applications/{applicationId}/healthByTime | Get application health by time |
| [**getOrganizationInsightApplications**](InsightApi.md#getOrganizationInsightApplications) | **GET** /organizations/{organizationId}/insight/applications | List all Insight tracked applications |
| [**getOrganizationInsightMonitoredMediaServer**](InsightApi.md#getOrganizationInsightMonitoredMediaServer) | **GET** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Return a monitored media server for this organization |
| [**getOrganizationInsightMonitoredMediaServers**](InsightApi.md#getOrganizationInsightMonitoredMediaServers) | **GET** /organizations/{organizationId}/insight/monitoredMediaServers | List the monitored media servers for this organization |
| [**updateOrganizationInsightMonitoredMediaServer**](InsightApi.md#updateOrganizationInsightMonitoredMediaServer) | **PUT** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Update a monitored media server for this organization |


<a id="createOrganizationInsightMonitoredMediaServer"></a>
# **createOrganizationInsightMonitoredMediaServer**
> Object createOrganizationInsightMonitoredMediaServer(organizationId, createOrganizationInsightMonitoredMediaServerRequest)

Add a media server to be monitored for this organization

Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInsightMonitoredMediaServerRequest createOrganizationInsightMonitoredMediaServerRequest = new CreateOrganizationInsightMonitoredMediaServerRequest(); // CreateOrganizationInsightMonitoredMediaServerRequest | 
    try {
      Object result = apiInstance.createOrganizationInsightMonitoredMediaServer(organizationId, createOrganizationInsightMonitoredMediaServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#createOrganizationInsightMonitoredMediaServer");
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
| **organizationId** | **String**|  | |
| **createOrganizationInsightMonitoredMediaServerRequest** | [**CreateOrganizationInsightMonitoredMediaServerRequest**](CreateOrganizationInsightMonitoredMediaServerRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteOrganizationInsightMonitoredMediaServer"></a>
# **deleteOrganizationInsightMonitoredMediaServer**
> deleteOrganizationInsightMonitoredMediaServer(organizationId, monitoredMediaServerId)

Delete a monitored media server from this organization

Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
    try {
      apiInstance.deleteOrganizationInsightMonitoredMediaServer(organizationId, monitoredMediaServerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#deleteOrganizationInsightMonitoredMediaServer");
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
| **organizationId** | **String**|  | |
| **monitoredMediaServerId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getNetworkInsightApplicationHealthByTime"></a>
# **getNetworkInsightApplicationHealthByTime**
> List&lt;GetNetworkInsightApplicationHealthByTime200ResponseInner&gt; getNetworkInsightApplicationHealthByTime(networkId, applicationId, t0, t1, timespan, resolution)

Get application health by time

Get application health by time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String applicationId = "applicationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300.
    try {
      List<GetNetworkInsightApplicationHealthByTime200ResponseInner> result = apiInstance.getNetworkInsightApplicationHealthByTime(networkId, applicationId, t0, t1, timespan, resolution);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getNetworkInsightApplicationHealthByTime");
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
| **networkId** | **String**|  | |
| **applicationId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 7 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300. | [optional] |

### Return type

[**List&lt;GetNetworkInsightApplicationHealthByTime200ResponseInner&gt;**](GetNetworkInsightApplicationHealthByTime200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationInsightApplications"></a>
# **getOrganizationInsightApplications**
> List&lt;GetOrganizationInsightApplications200ResponseInner&gt; getOrganizationInsightApplications(organizationId)

List all Insight tracked applications

List all Insight tracked applications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<GetOrganizationInsightApplications200ResponseInner> result = apiInstance.getOrganizationInsightApplications(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getOrganizationInsightApplications");
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
| **organizationId** | **String**|  | |

### Return type

[**List&lt;GetOrganizationInsightApplications200ResponseInner&gt;**](GetOrganizationInsightApplications200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationInsightMonitoredMediaServer"></a>
# **getOrganizationInsightMonitoredMediaServer**
> Object getOrganizationInsightMonitoredMediaServer(organizationId, monitoredMediaServerId)

Return a monitored media server for this organization

Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationInsightMonitoredMediaServer(organizationId, monitoredMediaServerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getOrganizationInsightMonitoredMediaServer");
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
| **organizationId** | **String**|  | |
| **monitoredMediaServerId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationInsightMonitoredMediaServers"></a>
# **getOrganizationInsightMonitoredMediaServers**
> List&lt;GetOrganizationInsightMonitoredMediaServers200ResponseInner&gt; getOrganizationInsightMonitoredMediaServers(organizationId)

List the monitored media servers for this organization

List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<GetOrganizationInsightMonitoredMediaServers200ResponseInner> result = apiInstance.getOrganizationInsightMonitoredMediaServers(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#getOrganizationInsightMonitoredMediaServers");
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
| **organizationId** | **String**|  | |

### Return type

[**List&lt;GetOrganizationInsightMonitoredMediaServers200ResponseInner&gt;**](GetOrganizationInsightMonitoredMediaServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationInsightMonitoredMediaServer"></a>
# **updateOrganizationInsightMonitoredMediaServer**
> Object updateOrganizationInsightMonitoredMediaServer(organizationId, monitoredMediaServerId, updateOrganizationInsightMonitoredMediaServerRequest)

Update a monitored media server for this organization

Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InsightApi apiInstance = new InsightApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
    UpdateOrganizationInsightMonitoredMediaServerRequest updateOrganizationInsightMonitoredMediaServerRequest = new UpdateOrganizationInsightMonitoredMediaServerRequest(); // UpdateOrganizationInsightMonitoredMediaServerRequest | 
    try {
      Object result = apiInstance.updateOrganizationInsightMonitoredMediaServer(organizationId, monitoredMediaServerId, updateOrganizationInsightMonitoredMediaServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightApi#updateOrganizationInsightMonitoredMediaServer");
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
| **organizationId** | **String**|  | |
| **monitoredMediaServerId** | **String**|  | |
| **updateOrganizationInsightMonitoredMediaServerRequest** | [**UpdateOrganizationInsightMonitoredMediaServerRequest**](UpdateOrganizationInsightMonitoredMediaServerRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

