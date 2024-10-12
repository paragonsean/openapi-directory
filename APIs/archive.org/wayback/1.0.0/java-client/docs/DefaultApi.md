# DefaultApi

All URIs are relative to *https://api.archive.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**waybackV1AvailableGet**](DefaultApi.md#waybackV1AvailableGet) | **GET** /wayback/v1/available |  |
| [**waybackV1AvailablePost**](DefaultApi.md#waybackV1AvailablePost) | **POST** /wayback/v1/available |  |


<a id="waybackV1AvailableGet"></a>
# **waybackV1AvailableGet**
> waybackV1AvailableGet(url, timestamp, paramCallback, timeout, closest, statusCode, tag)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.archive.org");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String url = "url_example"; // String | A single URL to query.
    String timestamp = "timestamp_example"; // String | Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00 
    String paramCallback = "paramCallback_example"; // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. 
    BigDecimal timeout = new BigDecimal("5"); // BigDecimal | Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0. 
    String closest = "either"; // String | The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests. 
    Integer statusCode = 200; // Integer | HTTP status codes to filter by. Only results with these codes will be returned 
    String tag = "tag_example"; // String | The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values. 
    try {
      apiInstance.waybackV1AvailableGet(url, timestamp, paramCallback, timeout, closest, statusCode, tag);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#waybackV1AvailableGet");
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
| **url** | **String**| A single URL to query. | |
| **timestamp** | **String**| Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00  | [optional] |
| **paramCallback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.  | [optional] |
| **timeout** | **BigDecimal**| Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0.  | [optional] [default to 5] |
| **closest** | **String**| The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests.  | [optional] [default to either] [enum: either, before, after] |
| **statusCode** | **Integer**| HTTP status codes to filter by. Only results with these codes will be returned  | [optional] [enum: 200, 201, 202, 203, 204, 205, 206, 300, 301, 302, 303, 304, 305, 306, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 426, 428, 429, 431, 500, 501, 502, 503, 504, 505, 506, 507, 511] |
| **tag** | **String**| The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values.  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applcation/json, application/javascript, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nominal Availability results |  -  |
| **0** | Unexpected error |  -  |

<a id="waybackV1AvailablePost"></a>
# **waybackV1AvailablePost**
> waybackV1AvailablePost(url, timestamp, paramCallback, timeout, closest, statusCode, tag, availabilityRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.archive.org");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String url = "url_example"; // String | A single URL to query.
    String timestamp = "timestamp_example"; // String | Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00 
    String paramCallback = "paramCallback_example"; // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. 
    BigDecimal timeout = new BigDecimal("5"); // BigDecimal | Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0. 
    String closest = "either"; // String | The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests. 
    Integer statusCode = 200; // Integer | HTTP status codes to filter by. Only results with these codes will be returned 
    String tag = "tag_example"; // String | The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values. 
    List<AvailabilityRequest> availabilityRequest = Arrays.asList(); // List<AvailabilityRequest> | 
    try {
      apiInstance.waybackV1AvailablePost(url, timestamp, paramCallback, timeout, closest, statusCode, tag, availabilityRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#waybackV1AvailablePost");
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
| **url** | **String**| A single URL to query. | |
| **timestamp** | **String**| Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00  | [optional] |
| **paramCallback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.  | [optional] |
| **timeout** | **BigDecimal**| Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0.  | [optional] [default to 5] |
| **closest** | **String**| The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests.  | [optional] [default to either] [enum: either, before, after] |
| **statusCode** | **Integer**| HTTP status codes to filter by. Only results with these codes will be returned  | [optional] [enum: 200, 201, 202, 203, 204, 205, 206, 300, 301, 302, 303, 304, 305, 306, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 426, 428, 429, 431, 500, 501, 502, 503, 504, 505, 506, 507, 511] |
| **tag** | **String**| The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values.  | [optional] |
| **availabilityRequest** | [**List&lt;AvailabilityRequest&gt;**](AvailabilityRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/csv
 - **Accept**: applcation/json, application/javascript, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nominal Availability results |  -  |
| **0** | Unexpected error |  -  |

