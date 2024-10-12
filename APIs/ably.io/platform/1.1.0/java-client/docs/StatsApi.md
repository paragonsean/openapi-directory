# StatsApi

All URIs are relative to *https://rest.ably.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStats**](StatsApi.md#getStats) | **GET** /stats | Retrieve usage statistics for an application |
| [**getTime**](StatsApi.md#getTime) | **GET** /time | Get the service time |


<a id="getStats"></a>
# **getStats**
> Object getStats(xAblyVersion, format, start, limit, end, direction, unit)

Retrieve usage statistics for an application

The Ably system can be queried to obtain usage statistics for a given application, and results are provided aggregated across all channels in use in the application in the specified period. Stats may be used to track usage against account quotas.

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
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    String start = "start_example"; // String | 
    Integer limit = 56; // Integer | 
    String end = "now"; // String | 
    String direction = "forwards"; // String | 
    String unit = "minute"; // String | Specifies the unit of aggregation in the returned results.
    try {
      Object result = apiInstance.getStats(xAblyVersion, format, start, limit, end, direction, unit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#getStats");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **start** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **end** | **String**|  | [optional] [default to now] |
| **direction** | **String**|  | [optional] [default to backwards] [enum: forwards, backwards] |
| **unit** | **String**| Specifies the unit of aggregation in the returned results. | [optional] [default to minute] [enum: minute, hour, day, month] |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="getTime"></a>
# **getTime**
> List&lt;Integer&gt; getTime(xAblyVersion, format)

Get the service time

This returns the service time in milliseconds since the epoch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    try {
      List<Integer> result = apiInstance.getTime(xAblyVersion, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#getTime");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |

### Return type

**List&lt;Integer&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

