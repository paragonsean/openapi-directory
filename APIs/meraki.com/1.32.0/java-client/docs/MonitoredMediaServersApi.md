# MonitoredMediaServersApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationInsightMonitoredMediaServer_1**](MonitoredMediaServersApi.md#createOrganizationInsightMonitoredMediaServer_1) | **POST** /organizations/{organizationId}/insight/monitoredMediaServers | Add a media server to be monitored for this organization |
| [**deleteOrganizationInsightMonitoredMediaServer_1**](MonitoredMediaServersApi.md#deleteOrganizationInsightMonitoredMediaServer_1) | **DELETE** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Delete a monitored media server from this organization |
| [**getOrganizationInsightMonitoredMediaServer_1**](MonitoredMediaServersApi.md#getOrganizationInsightMonitoredMediaServer_1) | **GET** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Return a monitored media server for this organization |
| [**getOrganizationInsightMonitoredMediaServers_1**](MonitoredMediaServersApi.md#getOrganizationInsightMonitoredMediaServers_1) | **GET** /organizations/{organizationId}/insight/monitoredMediaServers | List the monitored media servers for this organization |
| [**updateOrganizationInsightMonitoredMediaServer_1**](MonitoredMediaServersApi.md#updateOrganizationInsightMonitoredMediaServer_1) | **PUT** /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId} | Update a monitored media server for this organization |


<a id="createOrganizationInsightMonitoredMediaServer_1"></a>
# **createOrganizationInsightMonitoredMediaServer_1**
> Object createOrganizationInsightMonitoredMediaServer_1(organizationId, createOrganizationInsightMonitoredMediaServerRequest)

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
import org.openapitools.client.api.MonitoredMediaServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MonitoredMediaServersApi apiInstance = new MonitoredMediaServersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInsightMonitoredMediaServerRequest createOrganizationInsightMonitoredMediaServerRequest = new CreateOrganizationInsightMonitoredMediaServerRequest(); // CreateOrganizationInsightMonitoredMediaServerRequest | 
    try {
      Object result = apiInstance.createOrganizationInsightMonitoredMediaServer_1(organizationId, createOrganizationInsightMonitoredMediaServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitoredMediaServersApi#createOrganizationInsightMonitoredMediaServer_1");
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

<a id="deleteOrganizationInsightMonitoredMediaServer_1"></a>
# **deleteOrganizationInsightMonitoredMediaServer_1**
> deleteOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId)

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
import org.openapitools.client.api.MonitoredMediaServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MonitoredMediaServersApi apiInstance = new MonitoredMediaServersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
    try {
      apiInstance.deleteOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitoredMediaServersApi#deleteOrganizationInsightMonitoredMediaServer_1");
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

<a id="getOrganizationInsightMonitoredMediaServer_1"></a>
# **getOrganizationInsightMonitoredMediaServer_1**
> Object getOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId)

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
import org.openapitools.client.api.MonitoredMediaServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MonitoredMediaServersApi apiInstance = new MonitoredMediaServersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitoredMediaServersApi#getOrganizationInsightMonitoredMediaServer_1");
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

<a id="getOrganizationInsightMonitoredMediaServers_1"></a>
# **getOrganizationInsightMonitoredMediaServers_1**
> List&lt;GetOrganizationInsightMonitoredMediaServers200ResponseInner&gt; getOrganizationInsightMonitoredMediaServers_1(organizationId)

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
import org.openapitools.client.api.MonitoredMediaServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MonitoredMediaServersApi apiInstance = new MonitoredMediaServersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<GetOrganizationInsightMonitoredMediaServers200ResponseInner> result = apiInstance.getOrganizationInsightMonitoredMediaServers_1(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitoredMediaServersApi#getOrganizationInsightMonitoredMediaServers_1");
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

<a id="updateOrganizationInsightMonitoredMediaServer_1"></a>
# **updateOrganizationInsightMonitoredMediaServer_1**
> Object updateOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId, updateOrganizationInsightMonitoredMediaServerRequest)

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
import org.openapitools.client.api.MonitoredMediaServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MonitoredMediaServersApi apiInstance = new MonitoredMediaServersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String monitoredMediaServerId = "monitoredMediaServerId_example"; // String | 
    UpdateOrganizationInsightMonitoredMediaServerRequest updateOrganizationInsightMonitoredMediaServerRequest = new UpdateOrganizationInsightMonitoredMediaServerRequest(); // UpdateOrganizationInsightMonitoredMediaServerRequest | 
    try {
      Object result = apiInstance.updateOrganizationInsightMonitoredMediaServer_1(organizationId, monitoredMediaServerId, updateOrganizationInsightMonitoredMediaServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitoredMediaServersApi#updateOrganizationInsightMonitoredMediaServer_1");
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

