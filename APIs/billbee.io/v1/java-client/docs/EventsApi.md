# EventsApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventApiGetList**](EventsApi.md#eventApiGetList) | **GET** /api/v1/events | Get a list of all events optionally filtered by date. This request is extra throttled to 2 calls per page per hour. |


<a id="eventApiGetList"></a>
# **eventApiGetList**
> Object eventApiGetList(minDate, maxDate, page, pageSize, typeId, orderId)

Get a list of all events optionally filtered by date. This request is extra throttled to 2 calls per page per hour.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    EventsApi apiInstance = new EventsApi(defaultClient);
    OffsetDateTime minDate = OffsetDateTime.now(); // OffsetDateTime | Specifies the oldest date to include in the response
    OffsetDateTime maxDate = OffsetDateTime.now(); // OffsetDateTime | Specifies the newest date to include in the response
    Integer page = 56; // Integer | Specifies the page to request
    Integer pageSize = 56; // Integer | Specifies the pagesize. Defaults to 50, max value is 250
    List<Integer> typeId = Arrays.asList(); // List<Integer> | Filter for specific event types
    Long orderId = 56L; // Long | Filter for specific order id
    try {
      Object result = apiInstance.eventApiGetList(minDate, maxDate, page, pageSize, typeId, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventApiGetList");
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
| **minDate** | **OffsetDateTime**| Specifies the oldest date to include in the response | [optional] |
| **maxDate** | **OffsetDateTime**| Specifies the newest date to include in the response | [optional] |
| **page** | **Integer**| Specifies the page to request | [optional] |
| **pageSize** | **Integer**| Specifies the pagesize. Defaults to 50, max value is 250 | [optional] |
| **typeId** | [**List&lt;Integer&gt;**](Integer.md)| Filter for specific event types | [optional] |
| **orderId** | **Long**| Filter for specific order id | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

