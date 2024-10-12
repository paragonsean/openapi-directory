# HttpServersApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkWebhooksHttpServer_2**](HttpServersApi.md#createNetworkWebhooksHttpServer_2) | **POST** /networks/{networkId}/webhooks/httpServers | Add an HTTP server to a network |
| [**deleteNetworkWebhooksHttpServer_2**](HttpServersApi.md#deleteNetworkWebhooksHttpServer_2) | **DELETE** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Delete an HTTP server from a network |
| [**getNetworkWebhooksHttpServer_2**](HttpServersApi.md#getNetworkWebhooksHttpServer_2) | **GET** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Return an HTTP server for a network |
| [**getNetworkWebhooksHttpServers_2**](HttpServersApi.md#getNetworkWebhooksHttpServers_2) | **GET** /networks/{networkId}/webhooks/httpServers | List the HTTP servers for a network |
| [**updateNetworkWebhooksHttpServer_2**](HttpServersApi.md#updateNetworkWebhooksHttpServer_2) | **PUT** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Update an HTTP server |


<a id="createNetworkWebhooksHttpServer_2"></a>
# **createNetworkWebhooksHttpServer_2**
> GetNetworkWebhooksHttpServers200ResponseInner createNetworkWebhooksHttpServer_2(networkId, createNetworkWebhooksHttpServerRequest)

Add an HTTP server to a network

Add an HTTP server to a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    HttpServersApi apiInstance = new HttpServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWebhooksHttpServerRequest createNetworkWebhooksHttpServerRequest = new CreateNetworkWebhooksHttpServerRequest(); // CreateNetworkWebhooksHttpServerRequest | 
    try {
      GetNetworkWebhooksHttpServers200ResponseInner result = apiInstance.createNetworkWebhooksHttpServer_2(networkId, createNetworkWebhooksHttpServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpServersApi#createNetworkWebhooksHttpServer_2");
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
| **createNetworkWebhooksHttpServerRequest** | [**CreateNetworkWebhooksHttpServerRequest**](CreateNetworkWebhooksHttpServerRequest.md)|  | |

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkWebhooksHttpServer_2"></a>
# **deleteNetworkWebhooksHttpServer_2**
> deleteNetworkWebhooksHttpServer_2(networkId, httpServerId)

Delete an HTTP server from a network

Delete an HTTP server from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    HttpServersApi apiInstance = new HttpServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String httpServerId = "httpServerId_example"; // String | 
    try {
      apiInstance.deleteNetworkWebhooksHttpServer_2(networkId, httpServerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpServersApi#deleteNetworkWebhooksHttpServer_2");
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
| **httpServerId** | **String**|  | |

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

<a id="getNetworkWebhooksHttpServer_2"></a>
# **getNetworkWebhooksHttpServer_2**
> GetNetworkWebhooksHttpServers200ResponseInner getNetworkWebhooksHttpServer_2(networkId, httpServerId)

Return an HTTP server for a network

Return an HTTP server for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    HttpServersApi apiInstance = new HttpServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String httpServerId = "httpServerId_example"; // String | 
    try {
      GetNetworkWebhooksHttpServers200ResponseInner result = apiInstance.getNetworkWebhooksHttpServer_2(networkId, httpServerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpServersApi#getNetworkWebhooksHttpServer_2");
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
| **httpServerId** | **String**|  | |

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWebhooksHttpServers_2"></a>
# **getNetworkWebhooksHttpServers_2**
> List&lt;GetNetworkWebhooksHttpServers200ResponseInner&gt; getNetworkWebhooksHttpServers_2(networkId)

List the HTTP servers for a network

List the HTTP servers for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    HttpServersApi apiInstance = new HttpServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkWebhooksHttpServers200ResponseInner> result = apiInstance.getNetworkWebhooksHttpServers_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpServersApi#getNetworkWebhooksHttpServers_2");
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

### Return type

[**List&lt;GetNetworkWebhooksHttpServers200ResponseInner&gt;**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWebhooksHttpServer_2"></a>
# **updateNetworkWebhooksHttpServer_2**
> GetNetworkWebhooksHttpServers200ResponseInner updateNetworkWebhooksHttpServer_2(networkId, httpServerId, updateNetworkWebhooksHttpServerRequest)

Update an HTTP server

Update an HTTP server. To change a URL, create a new HTTP server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    HttpServersApi apiInstance = new HttpServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String httpServerId = "httpServerId_example"; // String | 
    UpdateNetworkWebhooksHttpServerRequest updateNetworkWebhooksHttpServerRequest = new UpdateNetworkWebhooksHttpServerRequest(); // UpdateNetworkWebhooksHttpServerRequest | 
    try {
      GetNetworkWebhooksHttpServers200ResponseInner result = apiInstance.updateNetworkWebhooksHttpServer_2(networkId, httpServerId, updateNetworkWebhooksHttpServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpServersApi#updateNetworkWebhooksHttpServer_2");
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
| **httpServerId** | **String**|  | |
| **updateNetworkWebhooksHttpServerRequest** | [**UpdateNetworkWebhooksHttpServerRequest**](UpdateNetworkWebhooksHttpServerRequest.md)|  | [optional] |

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

