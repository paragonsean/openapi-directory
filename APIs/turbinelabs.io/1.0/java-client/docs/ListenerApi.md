# ListenerApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listenerGet**](ListenerApi.md#listenerGet) | **GET** /listener | list listeners |
| [**listenerListenerKeyDelete**](ListenerApi.md#listenerListenerKeyDelete) | **DELETE** /listener/{listenerKey} | delete listener |
| [**listenerListenerKeyGet**](ListenerApi.md#listenerListenerKeyGet) | **GET** /listener/{listenerKey} | get listener |
| [**listenerListenerKeyPut**](ListenerApi.md#listenerListenerKeyPut) | **PUT** /listener/{listenerKey} | modify listener |
| [**listenerPost**](ListenerApi.md#listenerPost) | **POST** /listener | create listener |


<a id="listenerGet"></a>
# **listenerGet**
> MultiListenerResult listenerGet(filters)

list listeners

Get a list of listeners

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListenerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ListenerApi apiInstance = new ListenerApi(defaultClient);
    String filters = "filters_example"; // String | A JSON encoded array of ListenerFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ListenerFilter will be included. 
    try {
      MultiListenerResult result = apiInstance.listenerGet(filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListenerApi#listenerGet");
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
| **filters** | **String**| A JSON encoded array of ListenerFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ListenerFilter will be included.  | [optional] |

### Return type

[**MultiListenerResult**](MultiListenerResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a list of listeners |  -  |
| **0** | Unexpected error |  -  |

<a id="listenerListenerKeyDelete"></a>
# **listenerListenerKeyDelete**
> Listener listenerListenerKeyDelete(listenerKey, checksum)

delete listener

Delete existing listener

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListenerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ListenerApi apiInstance = new ListenerApi(defaultClient);
    String listenerKey = "72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f"; // String | the listener key
    String checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the listener to be deleted
    try {
      Listener result = apiInstance.listenerListenerKeyDelete(listenerKey, checksum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListenerApi#listenerListenerKeyDelete");
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
| **listenerKey** | **String**| the listener key | |
| **checksum** | **String**| the current checksum of the listener to be deleted | |

### Return type

[**Listener**](Listener.md)

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

<a id="listenerListenerKeyGet"></a>
# **listenerListenerKeyGet**
> ListenerResult listenerListenerKeyGet(listenerKey)

get listener

Get details for a single listener

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListenerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ListenerApi apiInstance = new ListenerApi(defaultClient);
    String listenerKey = "72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f"; // String | the listener key
    try {
      ListenerResult result = apiInstance.listenerListenerKeyGet(listenerKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListenerApi#listenerListenerKeyGet");
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
| **listenerKey** | **String**| the listener key | |

### Return type

[**ListenerResult**](ListenerResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a single listener |  -  |
| **0** | Unexpected error |  -  |

<a id="listenerListenerKeyPut"></a>
# **listenerListenerKeyPut**
> ListenerResult listenerListenerKeyPut(listenerKey, listener)

modify listener

Modify an existing listener

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListenerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ListenerApi apiInstance = new ListenerApi(defaultClient);
    String listenerKey = "5074fe62-821e-4034-55bd-b9caa09af2a1"; // String | the listener key
    Listener listener = new Listener(); // Listener | the listener to modify
    try {
      ListenerResult result = apiInstance.listenerListenerKeyPut(listenerKey, listener);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListenerApi#listenerListenerKeyPut");
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
| **listenerKey** | **String**| the listener key | |
| **listener** | [**Listener**](Listener.md)| the listener to modify | |

### Return type

[**ListenerResult**](ListenerResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A result containing the modified cluster |  -  |
| **0** | Unexpected error |  -  |

<a id="listenerPost"></a>
# **listenerPost**
> ListenerResult listenerPost(listener)

create listener

Create a new listener

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListenerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ListenerApi apiInstance = new ListenerApi(defaultClient);
    ListenerCreate listener = new ListenerCreate(); // ListenerCreate | the listener to create
    try {
      ListenerResult result = apiInstance.listenerPost(listener);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListenerApi#listenerPost");
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
| **listener** | [**ListenerCreate**](ListenerCreate.md)| the listener to create | |

### Return type

[**ListenerResult**](ListenerResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the newly created listener |  -  |
| **0** | Unexpected error |  -  |

