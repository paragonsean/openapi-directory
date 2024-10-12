# ProxyApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**proxyGet**](ProxyApi.md#proxyGet) | **GET** /proxy | list proxies |
| [**proxyPost**](ProxyApi.md#proxyPost) | **POST** /proxy | create proxy |
| [**proxyProxyKeyDelete**](ProxyApi.md#proxyProxyKeyDelete) | **DELETE** /proxy/{proxyKey} | delete proxy |
| [**proxyProxyKeyGet**](ProxyApi.md#proxyProxyKeyGet) | **GET** /proxy/{proxyKey} | get proxy |


<a id="proxyGet"></a>
# **proxyGet**
> MultiProxyResult proxyGet(filters)

list proxies

Get a list of proxies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    String filters = "filters_example"; // String | A JSON encoded array of ProxyFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ProxyFilter will be included. 
    try {
      MultiProxyResult result = apiInstance.proxyGet(filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#proxyGet");
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
| **filters** | **String**| A JSON encoded array of ProxyFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ProxyFilter will be included.  | [optional] |

### Return type

[**MultiProxyResult**](MultiProxyResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a list of proxies |  -  |
| **0** | Unexpected error |  -  |

<a id="proxyPost"></a>
# **proxyPost**
> ProxyResult proxyPost(proxy)

create proxy

Create a new proxy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    ProxyCreate proxy = new ProxyCreate(); // ProxyCreate | the proxy to create
    try {
      ProxyResult result = apiInstance.proxyPost(proxy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#proxyPost");
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
| **proxy** | [**ProxyCreate**](ProxyCreate.md)| the proxy to create | |

### Return type

[**ProxyResult**](ProxyResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the newly created proxy |  -  |
| **0** | Unexpected error |  -  |

<a id="proxyProxyKeyDelete"></a>
# **proxyProxyKeyDelete**
> Proxy proxyProxyKeyDelete(proxyKey, checksum)

delete proxy

Delete existing proxy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    String proxyKey = "72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f"; // String | the proxy key
    String checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the proxy to be deleted
    try {
      Proxy result = apiInstance.proxyProxyKeyDelete(proxyKey, checksum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#proxyProxyKeyDelete");
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
| **proxyKey** | **String**| the proxy key | |
| **checksum** | **String**| the current checksum of the proxy to be deleted | |

### Return type

[**Proxy**](Proxy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | an empty result |  -  |
| **0** | Unexpected error |  -  |

<a id="proxyProxyKeyGet"></a>
# **proxyProxyKeyGet**
> ProxyResult proxyProxyKeyGet(proxyKey)

get proxy

Get details for a single proxy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    String proxyKey = "72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f"; // String | the proxy key
    try {
      ProxyResult result = apiInstance.proxyProxyKeyGet(proxyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#proxyProxyKeyGet");
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
| **proxyKey** | **String**| the proxy key | |

### Return type

[**ProxyResult**](ProxyResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a single proxy |  -  |
| **0** | Unexpected error |  -  |

