# PodsApi

All URIs are relative to *http://api.ss.solarvps.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**podsGet**](PodsApi.md#podsGet) | **GET** /pods | View all your pods |
| [**podsPodIdActionGet**](PodsApi.md#podsPodIdActionGet) | **GET** /pods/{podId}/{action} | Perform action on a specific pod |
| [**podsPodIdGet**](PodsApi.md#podsPodIdGet) | **GET** /pods/{podId} | View information on a specific pod |
| [**podsPodIdPingGet**](PodsApi.md#podsPodIdPingGet) | **GET** /pods/{podId}/ping | Ping your specified pod |


<a id="podsGet"></a>
# **podsGet**
> podsGet()

View all your pods

Shows all your pods

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PodsApi apiInstance = new PodsApi(defaultClient);
    try {
      apiInstance.podsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling PodsApi#podsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="podsPodIdActionGet"></a>
# **podsPodIdActionGet**
> podsPodIdActionGet(podId, action)

Perform action on a specific pod

Allowed actions are reboot, shutdown, boot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PodsApi apiInstance = new PodsApi(defaultClient);
    BigDecimal podId = new BigDecimal(78); // BigDecimal | Id of the pod you want to perform actions on
    String action = "action_example"; // String | Action to perform on selected pod
    try {
      apiInstance.podsPodIdActionGet(podId, action);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodsApi#podsPodIdActionGet");
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
| **podId** | **BigDecimal**| Id of the pod you want to perform actions on | |
| **action** | **String**| Action to perform on selected pod | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="podsPodIdGet"></a>
# **podsPodIdGet**
> podsPodIdGet(podId)

View information on a specific pod

Shows details of a specific pod. Enter 1 below to see an example

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PodsApi apiInstance = new PodsApi(defaultClient);
    BigDecimal podId = new BigDecimal(78); // BigDecimal | Id of the pod you want to perform actions on
    try {
      apiInstance.podsPodIdGet(podId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodsApi#podsPodIdGet");
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
| **podId** | **BigDecimal**| Id of the pod you want to perform actions on | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="podsPodIdPingGet"></a>
# **podsPodIdPingGet**
> podsPodIdPingGet(podId)

Ping your specified pod

Returns the ping response from your server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    PodsApi apiInstance = new PodsApi(defaultClient);
    BigDecimal podId = new BigDecimal(78); // BigDecimal | Id of the pod you want to ping check
    try {
      apiInstance.podsPodIdPingGet(podId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PodsApi#podsPodIdPingGet");
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
| **podId** | **BigDecimal**| Id of the pod you want to ping check | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

