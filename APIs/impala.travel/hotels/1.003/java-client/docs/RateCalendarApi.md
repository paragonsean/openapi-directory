# RateCalendarApi

All URIs are relative to *https://sandbox.impala.travel/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listRatePlanForHotelForRatePlanId**](RateCalendarApi.md#listRatePlanForHotelForRatePlanId) | **GET** /hotels/{hotelId}/rate-plans/{ratePlanId} | List a rate plan (rate calendar) for a hotel (Beta endpoint). |
| [**listRatePlansForHotel**](RateCalendarApi.md#listRatePlansForHotel) | **GET** /hotels/{hotelId}/rate-plans | List all rate plans (rate calendar) for a hotel (Beta endpoint) |


<a id="listRatePlanForHotelForRatePlanId"></a>
# **listRatePlanForHotelForRatePlanId**
> RatePlan listRatePlanForHotelForRatePlanId(hotelId, ratePlanId, updatedAt, size, offset, start, end, roomTypeId)

List a rate plan (rate calendar) for a hotel (Beta endpoint).

Returns a single rate plan available for you for a hotel.  Rate plans are products the hotel is offering. They typically consist of a combination of restrictiveness in case of cancellations or changes, the time they&#39;re bookable, minimum or maximum length of stay restrictions (e.g. week-long bookings), included components like breakfast or dinner and/or the conditions under which the room can be sold (e.g. private rates that can only be offered and sold to a closed user group behind login).  Examples of rate plans:  * Non-refundable room rate that includes breakfast * Room-only rate with free cancellation up to 14 days before arrival  This endpoint returns a singular available rate plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RateCalendarApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    RateCalendarApi apiInstance = new RateCalendarApi(defaultClient);
    UUID hotelId = UUID.fromString("40c0b330-186a-40bf-ae36-2c61fb322db0"); // UUID | The uuid of hotel for which rate plans are being fetched.
    Integer ratePlanId = 112; // Integer | The id of requested rateplan
    Object updatedAt = new HashMap(); // Object | Returns rate plans changed after the supplied date.
    BigDecimal size = new BigDecimal("25"); // BigDecimal | Number of rate plans returned on a given page (pagination).
    BigDecimal offset = new BigDecimal("0"); // BigDecimal | Offset from the first rate plan in the result (for pagination).
    String start = "2022-05-12"; // String | Start date of the considered time window for the returned rate plan.
    String end = "2022-05-12"; // String | Start date of the considered time window for the returned rate plan.
    UUID roomTypeId = UUID.fromString("6d3a255d-3b22-48a4-8076-3ae3d0ade3d7"); // UUID | The uuid of room for which rate plans are being fetched.
    try {
      RatePlan result = apiInstance.listRatePlanForHotelForRatePlanId(hotelId, ratePlanId, updatedAt, size, offset, start, end, roomTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RateCalendarApi#listRatePlanForHotelForRatePlanId");
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
| **hotelId** | **UUID**| The uuid of hotel for which rate plans are being fetched. | |
| **ratePlanId** | **Integer**| The id of requested rateplan | |
| **updatedAt** | [**Object**](.md)| Returns rate plans changed after the supplied date. | [optional] |
| **size** | **BigDecimal**| Number of rate plans returned on a given page (pagination). | [optional] [default to 25] |
| **offset** | **BigDecimal**| Offset from the first rate plan in the result (for pagination). | [optional] [default to 0] |
| **start** | **String**| Start date of the considered time window for the returned rate plan. | [optional] |
| **end** | **String**| Start date of the considered time window for the returned rate plan. | [optional] |
| **roomTypeId** | **UUID**| The uuid of room for which rate plans are being fetched. | [optional] |

### Return type

[**RatePlan**](RatePlan.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your request wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed. |  -  |
| **404** | Not Found |  -  |

<a id="listRatePlansForHotel"></a>
# **listRatePlansForHotel**
> ListRatePlansForHotel200Response listRatePlansForHotel(hotelId, updatedAt, size, offset, start, end, roomId)

List all rate plans (rate calendar) for a hotel (Beta endpoint)

Returns a list of all rate plans available for you for a hotel.  Rate plans are products the hotel is offering. They typically consist of a combination of restrictiveness in case of cancellations or changes, the time they&#39;re bookable, minimum or maximum length of stay restrictions (e.g. week-long bookings), included components like breakfast or dinner and/or the conditions under which the room can be sold (e.g. private rates that can only be offered and sold to a closed user group behind login).  Examples of rate plans:  * Non-refundable room rate that includes breakfast * Room-only rate with free cancellation up to 14 days before arrival  For each such rate plan this endpoint returns the room types it&#39;s available for, alongside prices for each date and occupancy that can be sold – or the information that the room isn&#39;t available (closed) for a certain date.  For the vast majority of our customers, availability searches using the [List all hotels](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1hotels/get) endpoint are the best choice. It accepts the dates your guest is looking for and provides the rates to display.  This endpoint can help augment this for two additional use cases:  This endpoint allows you to query rate prices for all future dates in one go, making it a great choice to feed availability information and prices into your own system or displaying a rate calender to guide your guests to gain an overview of future availability and prices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RateCalendarApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    RateCalendarApi apiInstance = new RateCalendarApi(defaultClient);
    UUID hotelId = UUID.fromString("40c0b330-186a-40bf-ae36-2c61fb322db0"); // UUID | The uuid of hotel for which rate plans are being fetched.
    Object updatedAt = new HashMap(); // Object | Returns rate plans changed after the supplied date.
    BigDecimal size = new BigDecimal("25"); // BigDecimal | Number of rate plans returned on a given page (pagination).
    BigDecimal offset = new BigDecimal("0"); // BigDecimal | Offset from the first rate plan in the result (for pagination).
    String start = "2022-05-12"; // String | Start date of the considered time window for the returned rate plan.
    String end = "2022-05-12"; // String | Start date of the considered time window for the returned rate plan.
    UUID roomId = UUID.fromString("6d3a255d-3b22-48a4-8076-3ae3d0ade3d7"); // UUID | The UUID of room for which rate plans are being fetched.
    try {
      ListRatePlansForHotel200Response result = apiInstance.listRatePlansForHotel(hotelId, updatedAt, size, offset, start, end, roomId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RateCalendarApi#listRatePlansForHotel");
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
| **hotelId** | **UUID**| The uuid of hotel for which rate plans are being fetched. | |
| **updatedAt** | [**Object**](.md)| Returns rate plans changed after the supplied date. | [optional] |
| **size** | **BigDecimal**| Number of rate plans returned on a given page (pagination). | [optional] [default to 25] |
| **offset** | **BigDecimal**| Offset from the first rate plan in the result (for pagination). | [optional] [default to 0] |
| **start** | **String**| Start date of the considered time window for the returned rate plan. | [optional] |
| **end** | **String**| Start date of the considered time window for the returned rate plan. | [optional] |
| **roomId** | **UUID**| The UUID of room for which rate plans are being fetched. | [optional] |

### Return type

[**ListRatePlansForHotel200Response**](ListRatePlansForHotel200Response.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your request wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed. |  -  |
| **404** | Not Found |  -  |

