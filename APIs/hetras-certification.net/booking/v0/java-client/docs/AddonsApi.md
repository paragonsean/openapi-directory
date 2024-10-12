# AddonsApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addonsGet**](AddonsApi.md#addonsGet) | **GET** /api/booking/v0/addons | Get a list of offers for addon services for the specified guest stay details. |


<a id="addonsGet"></a>
# **addonsGet**
> Addons addonsGet(appId, appKey, hotelId, arrivalDate, departureDate, channelCode, adults, rooms, roomType, ratePlanCode, expand)

Get a list of offers for addon services for the specified guest stay details.

With the addons request you can get a list of offers for addon services available for a specific rate, room type              and guest stay details.The channel code will define which rates will be returned based on the access control               configuration for related rates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    AddonsApi apiInstance = new AddonsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | Specifies the hotel id to request offers for.
    OffsetDateTime arrivalDate = OffsetDateTime.now(); // OffsetDateTime | Date from when the addon service will be booked to the reservation in the ISO-8601 format \"YYYY-MM-DD\".
    OffsetDateTime departureDate = OffsetDateTime.now(); // OffsetDateTime | Date until when the addon service will be booked to the reservation in the ISO-8601 format \"YYYY-MM-DD\".              This is usually the departure date of the reservation.
    String channelCode = "channelCode_example"; // String | Channel Code the rate plan needs to be configured for.
    byte[] adults = null; // byte[] | Number of adults per room.
    byte[] rooms = null; // byte[] | Number of rooms.
    String roomType = "roomType_example"; // String | Only return offers for the specified room type code.
    String ratePlanCode = "ratePlanCode_example"; // String | Only return offers for the specified rate plan code.
    String expand = "None"; // String | Expand the rates breakdown if required.
    try {
      Addons result = apiInstance.addonsGet(appId, appKey, hotelId, arrivalDate, departureDate, channelCode, adults, rooms, roomType, ratePlanCode, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddonsApi#addonsGet");
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
| **hotelId** | **Integer**| Specifies the hotel id to request offers for. | |
| **arrivalDate** | **OffsetDateTime**| Date from when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. | |
| **departureDate** | **OffsetDateTime**| Date until when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;.              This is usually the departure date of the reservation. | |
| **channelCode** | **String**| Channel Code the rate plan needs to be configured for. | |
| **adults** | **byte[]**| Number of adults per room. | |
| **rooms** | **byte[]**| Number of rooms. | |
| **roomType** | **String**| Only return offers for the specified room type code. | |
| **ratePlanCode** | **String**| Only return offers for the specified rate plan code. | |
| **expand** | **String**| Expand the rates breakdown if required. | [optional] [enum: None, Breakdown] |

### Return type

[**Addons**](Addons.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All addon offers for the requested stay details. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. Either a mandatory parameter was missing or no offers for               the requested stay details |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

