# BookingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBooking**](BookingApi.md#createBooking) | **POST** /booking/hotel-bookings | Create Orders associated to the Hotel Offers |


<a id="createBooking"></a>
# **createBooking**
> HotelBookedResponse createBooking(requestBody, amaClientRef, acceptEncoding)

Create Orders associated to the Hotel Offers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    BookingApi apiInstance = new BookingApi(defaultClient);
    BookingSchema requestBody = new BookingSchema(); // BookingSchema | `offerId`, `guests`, `payments` and optional `rooms` for the repartition (when used the `rooms` array items must match the shopping offer `roomQuantity`) 
    String amaClientRef = "amaClientRef_example"; // String | Client Reference to track Request/Response
    String acceptEncoding = "gzip"; // String | Compress the Response
    try {
      HotelBookedResponse result = apiInstance.createBooking(requestBody, amaClientRef, acceptEncoding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingApi#createBooking");
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
| **requestBody** | [**BookingSchema**](BookingSchema.md)| &#x60;offerId&#x60;, &#x60;guests&#x60;, &#x60;payments&#x60; and optional &#x60;rooms&#x60; for the repartition (when used the &#x60;rooms&#x60; array items must match the shopping offer &#x60;roomQuantity&#x60;)  | |
| **amaClientRef** | **String**| Client Reference to track Request/Response | [optional] |
| **acceptEncoding** | **String**| Compress the Response | [optional] [enum: gzip, identity] |

### Return type

[**HotelBookedResponse**](HotelBookedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.amadeus+json
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Booked |  -  |
| **400** | Bad Request  code    | title                                                          | owner    | pointer ------- | -------------------------------------------------------------- | -------- | -------   477   | INVALID FORMAT                                                 | Amadeus  |   4725   | INVALID PASSENGER ASSOCIATION                                  | Amadeus  | data/rooms/guestIds 33555   | NUMBER OF ROOMS MISMATCH BETWEEN SHOPPING AND BOOKING          | Amadeus  | data/rooms 33554   | PRICE HAS CHANGED. PLEASE GET A NEW OFFERID AND TRY AGAIN      | Amadeus  | data/offerId 36803   | OFFERID HAS EXPIRED. PLEASE GET A NEW OFFERID AND TRY AGAIN    | Amadeus  | data/offerId  1205   | INVALID CREDIT CARD TYPE                                       | Amadeus  | data/payments/card/vendorCode  8517   | INVALID CREDIT CARD NUMBER                                     | Provider | data/payments/card/cardNumber  1427   | GUARANTEE REQUIRED                                             | Provider | data/payments/card  1146   | DEPOSIT REQUIRED                                               | Provider | data/payments/card  3659   | CREDIT CARD DEPOSIT REQUIRED                                   | Provider | data/payments/card  3682   | CREDIT CARD NOT ACCEPTED AT HOTEL PROPERTY                     | Provider | data/payments/card/vendorCode  3871   | CREDIT CARD EXPIRATION DATE INVALID FOR CHECK IN DATE          | Provider | data/payments/card/expiryDate    |  -  |
| **500** | Internal Server Error  code    | title                                                          | owner                                 ------- | -------------------------------------------------------------- | ------- 00011   | UNABLE TO PROCESS                                              | Provider 04070   | UNABLE TO PROCESS - CONTACT HELP DESK                          | Amadeus  |  -  |

