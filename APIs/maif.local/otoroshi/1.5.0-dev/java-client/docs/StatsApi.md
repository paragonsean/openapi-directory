# StatsApi

All URIs are relative to *http://otoroshi-api.oto.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalLiveStats**](StatsApi.md#globalLiveStats) | **GET** /api/live | Get global otoroshi stats |
| [**serviceLiveStats**](StatsApi.md#serviceLiveStats) | **GET** /api/live/{id} | Get live feed of otoroshi stats |


<a id="globalLiveStats"></a>
# **globalLiveStats**
> Stats globalLiveStats()

Get global otoroshi stats

Get global otoroshi stats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    StatsApi apiInstance = new StatsApi(defaultClient);
    try {
      Stats result = apiInstance.globalLiveStats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#globalLiveStats");
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

[**Stats**](Stats.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="serviceLiveStats"></a>
# **serviceLiveStats**
> Stats serviceLiveStats(id)

Get live feed of otoroshi stats

Get live feed of global otoroshi stats (global) or for a service {id}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String id = "id_example"; // String | The service id or global for otoroshi stats
    try {
      Stats result = apiInstance.serviceLiveStats(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#serviceLiveStats");
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
| **id** | **String**| The service id or global for otoroshi stats | |

### Return type

[**Stats**](Stats.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/event-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

