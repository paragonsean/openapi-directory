# AvailabilityApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**availabilityGet**](AvailabilityApi.md#availabilityGet) | **GET** /api/booking/v0/availability | Gets the availability and occupancy for a specific hotel and timespan. |


<a id="availabilityGet"></a>
# **availabilityGet**
> AvailabilityResponse availabilityGet(appId, appKey, hotelId, from, to, expand, skip, top, inlinecount)

Gets the availability and occupancy for a specific hotel and timespan.

Read past occupancy and future availability for a specific hotel. You can also request the breakdown per room type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    AvailabilityApi apiInstance = new AvailabilityApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | Specifies the hotel id to request the availability for.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Defines the first business day you would like to get availability numbers for.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | Defines the last business day you would like to get availability numbers for. The maximum time span between <i>from</i>´and <i>to</i>              is limited to 365 days.
    String expand = "RoomTypes"; // String | You can expand the room types breakdown per business day for the availibility numbers if need be.
    Integer skip = 56; // Integer | Amount of items to skip.
    Integer top = 56; // Integer | Amount of items to select.
    String inlinecount = "None"; // String | Return total number of items for a given filter criteria.
    try {
      AvailabilityResponse result = apiInstance.availabilityGet(appId, appKey, hotelId, from, to, expand, skip, top, inlinecount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityApi#availabilityGet");
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
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **hotelId** | **Integer**| Specifies the hotel id to request the availability for. | |
| **from** | **OffsetDateTime**| Defines the first business day you would like to get availability numbers for. | |
| **to** | **OffsetDateTime**| Defines the last business day you would like to get availability numbers for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. | |
| **expand** | **String**| You can expand the room types breakdown per business day for the availibility numbers if need be. | [optional] [enum: RoomTypes] |
| **skip** | **Integer**| Amount of items to skip. | [optional] |
| **top** | **Integer**| Amount of items to select. | [optional] |
| **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] [enum: None, AllPages] |

### Return type

[**AvailabilityResponse**](AvailabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of availabilities per business day. |  -  |
| **400** | Bad request. Request parameters syntactically erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |

