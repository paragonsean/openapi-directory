# RatesApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ratesGet**](RatesApi.md#ratesGet) | **GET** /api/booking/v0/rates | Get a list of room offers for the specified guest stay details. |


<a id="ratesGet"></a>
# **ratesGet**
> Rates ratesGet(appId, appKey, hotelId, arrivalDate, departureDate, channelCode, adults, rooms, roomType, ratePlanCode, groupCode, expand)

Get a list of room offers for the specified guest stay details.

With the rates request you can get a list of different rate offers per room type. You will have to at least               specify the hotel, the arrival and departure date, number of adults per room and the channel code. The channel code              will define which rates will be returned based on the access control configuration for the rates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    RatesApi apiInstance = new RatesApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | Specifies the hotel id to request offers for.
    OffsetDateTime arrivalDate = OffsetDateTime.now(); // OffsetDateTime | Date of arrival for the guest in the ISO-8601 format \"YYYY-MM-DD\".
    OffsetDateTime departureDate = OffsetDateTime.now(); // OffsetDateTime | Date of departure for the guest in the ISO-8601 format \"YYYY-MM-DD\".
    String channelCode = "channelCode_example"; // String | Channel Code the rate plan needs to be configured for.
    byte[] adults = null; // byte[] | Number of adults per room.
    byte[] rooms = null; // byte[] | Number of rooms (default is 1).
    String roomType = "roomType_example"; // String | Only return offers with rates for the specified room type code.
    String ratePlanCode = "ratePlanCode_example"; // String | Only return offers for the specified room type code.
    String groupCode = "groupCode_example"; // String | Only return offers for the specified group code.
    String expand = "None"; // String | Expand the rates breakdown if required.
    try {
      Rates result = apiInstance.ratesGet(appId, appKey, hotelId, arrivalDate, departureDate, channelCode, adults, rooms, roomType, ratePlanCode, groupCode, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RatesApi#ratesGet");
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
| **arrivalDate** | **OffsetDateTime**| Date of arrival for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. | |
| **departureDate** | **OffsetDateTime**| Date of departure for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;. | |
| **channelCode** | **String**| Channel Code the rate plan needs to be configured for. | |
| **adults** | **byte[]**| Number of adults per room. | |
| **rooms** | **byte[]**| Number of rooms (default is 1). | [optional] |
| **roomType** | **String**| Only return offers with rates for the specified room type code. | [optional] |
| **ratePlanCode** | **String**| Only return offers for the specified room type code. | [optional] |
| **groupCode** | **String**| Only return offers for the specified group code. | [optional] |
| **expand** | **String**| Expand the rates breakdown if required. | [optional] [enum: None, Breakdown] |

### Return type

[**Rates**](Rates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Different rates for the requested stay details grouped by room type. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. It is also used if there are no rates available for the specified guest stay details. |  -  |
| **422** | The request failed to validate. Either a mandatory parameter was missing or no offers for               the requested stay details |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

