# BookingsApi

All URIs are relative to *https://sandbox.impala.travel/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelBooking**](BookingsApi.md#cancelBooking) | **DELETE** /bookings/{bookingId} | Cancel a booking |
| [**createBooking**](BookingsApi.md#createBooking) | **POST** /bookings | Create a booking |
| [**listBookings**](BookingsApi.md#listBookings) | **GET** /bookings | List all bookings |
| [**retrieveBooking**](BookingsApi.md#retrieveBooking) | **GET** /bookings/{bookingId} | Retrieve a booking |
| [**updateBooking**](BookingsApi.md#updateBooking) | **PUT** /bookings/{bookingId} | Change a booking |
| [**updateBookingContact**](BookingsApi.md#updateBookingContact) | **PUT** /bookings/{bookingId}/booking-contact | Change a booking contact |


<a id="cancelBooking"></a>
# **cancelBooking**
> Booking cancelBooking(bookingId)

Cancel a booking

&lt;!-- theme: danger --&gt;  &gt; Cancels the specified booking with immediate effect. This action might result in a cancellation charge being charged.  Submitting this request means we&#39;ll notify the hotel of the cancellation and that they won&#39;t expect your guest.  You can use &#x60;GET /bookings/{bookingId}&#x60;to see the cancellation policies that apply to a booking at a given point in time. Please note that cancelling a booking will incur a cancellation fee according to the rules that apply at the time of cancellation. You can find the cancellation fee that has been charged in the response of this call in the &#x60;cancellation.fee&#x60; object.  If the booking you cancelled allows for a partial or full refund, we&#39;ll credit your Impala balance with the amount we charged you as the seller of this booking – meaning we&#39;ll deduct the amount the next time we&#39;re requesting payment for the sum of all the bookings you made.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String bookingId = "bookingId_example"; // String | The unique identifier of the booking you would like to update.
    try {
      Booking result = apiInstance.cancelBooking(bookingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#cancelBooking");
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
| **bookingId** | **String**| The unique identifier of the booking you would like to update. | |

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the cancelled booking. This includes the &#x60;cancellation.fee&#x60; object with details on the fee for this cancellation (most frequently this means either a zero fee, so the booking is fully refundable, or the full amount of the stay is due as a fee, meaning the booking was non-refundable). |  -  |
| **400** | Your request wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed. |  -  |
| **401** | Your request was sent without or with an incorrect API key. This most frequently happens when the &#x60;x-api-key&#x60; header wasn&#39;t added or contains an incorrect value. This might also happen if you&#39;re trying to access the production API endpoints with a sandbox API key or vice versa. |  -  |
| **403** | This booking can&#39;t be cancelled. This most frequently happens when you&#39;re trying to cancel a booking that has already started. Impala allows you to handle booking management up to a guest&#39;s arrival. Once the guest is staying or due arrival, please contact the hotel directly for questions around their current stay. |  -  |
| **404** | Not found |  -  |
| **500** | An internal server error within the Impala platform has occurred. Our team will investigate the error. We recommend that you contact us at support@impala.travel with the x-correlation-id value contained within the response headers. Sending us this value will allow us to identify the precise error you encountered. |  -  |

<a id="createBooking"></a>
# **createBooking**
> Booking createBooking(bookingRequest)

Create a booking

Creates a booking for for the rate and dates you specify in the request body.  You&#39;ll need a &#x60;roomTypes[].rates[].rateId&#x60; that&#39;s bookable for those dates, which you can find using the [Retrieve a hotel](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1hotels~1%7BhotelId%7D/get) endpoint.  If you have provided a credit card on the dashboard then **Impala will send the booking to the hotel immediately**. We&#39;ll ensure payment is taken care of before your guest arrives at the hotel.  * Your guest needs to be **paying you** the rate specified in &#x60;retailRate&#x60; (as listed in the [Retrieve a hotel](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1hotels~1%7BhotelId%7D/get) response) before you submit this request. * Once your request is received and the booking is confirmed, **Impala will charge you** as the seller this &#x60;retailRate&#x60; minus the &#x60;sellerCommissionPercentage&#x60; (which is the affiliate commission you get to keep). We&#39;ll use the business credit card you&#39;ve added to your account as payment method for this. * The difference between the amount you charge your guest (&#x60;retailRate&#x60;, e.g. 200 €) and what Impala charges you (&#x60;retailRate&#x60; minus &#x60;sellerCommissionPercentage&#x60;, e.g. 200 €) is your commission (in this example: 20 €) to keep.  You can find more information on how money flows between your guest and you, and you and Impala, [in this article](https://impala.stoplight.io/docs/booking-api/branches/v1.003/docs/good-to-know/payments-and-commissions.md)  &lt;!-- theme: warning --&gt;  &gt; **This request might take up to 20 seconds to load.** While we work to return a response to your request within milliseconds in most cases, some bookings require us to re-verify current pricing in real-time and doing so might take up to 20 seconds. Please make sure your app handles this waiting state appropriately.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    BookingRequest bookingRequest = new BookingRequest(); // BookingRequest | Specifies the room you want to book for your guest.
    try {
      Booking result = apiInstance.createBooking(bookingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#createBooking");
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
| **bookingRequest** | [**BookingRequest**](BookingRequest.md)| Specifies the room you want to book for your guest. | [optional] |

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | We&#39;ve created the booking and are returning some of its details in the response body. |  -  |
| **400** | Your request wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed.  |  -  |
| **401** | Your request was sent without or with an incorrect API key. This most frequently happens when the &#x60;x-api-key&#x60; header wasn&#39;t added or contains an incorrect value. This might also happen if you&#39;re trying to access the production API endpoints with a sandbox API key or vice versa. |  -  |
| **403** | You are not authorized to use this service. Please contact support@impala.travel to gain access. |  -  |
| **500** | An internal server error within the Impala platform has occurred. Our team will investigate the error. We recommend that you contact us at support@impala.travel with the x-correlation-id value contained within the response headers. Sending us this value will allow us to identify the precise error you encountered. |  -  |

<a id="listBookings"></a>
# **listBookings**
> ListBookings200Response listBookings(start, end, created, updated, size, offset, sortBy)

List all bookings

Returns a list of all the bookings you&#39;ve made.  You can filter the list based on when bookings were created or last updated, as well as their arrival (&#x60;start&#x60;) and departure (&#x60;end&#x60;). These date-based filters allow to narrow down the result with modifiers for less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;).  Example: Adding the query parameters &#x60;start[gt]&#x3D;2021-05-20&amp;updated[lte]&#x3D;2020-11-20T11:11:00.000Z&#x60; would return bookings arriving after May 20th, 2020 that were updated before or on November 20th, 2020 at 11:11 am UTC.  You can specify the **sorting order** in which bookings are returned: * This is done by using the &#x60;sortBy&#x60; query parameter. * Results can be sorted by &#x60;createdAt&#x60; and &#x60;updatedAt&#x60; * The parameter allows for a comma-separated list of arguments with &#x60;:asc&#x60; (ascending, the default if no sorting is specified) and &#x60;:desc&#x60; (descending) modifiers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    Object start = new HashMap(); // Object | Allows for filtering based on arrival date of the booking in ISO 8601 format (e.g. `2021-12-01`). Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?start[lte]=2021-12-20&start[gte]=2021-12-10`
    Object end = new HashMap(); // Object | Allows for filtering based on departure date of the booking in ISO 8601 format (e.g. `2021-12-01`). Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?end[lte]=2021-12-25&end[gte]=2021-12-15`
    Object created = new HashMap(); // Object | Allows for filtering based on creation date and time of the booking in ISO 8601 format (e.g. `2020-11-04T17:37:37Z`) and UTC timezone. Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?created[lte]=2020-11-04T19:37:37Z&created[gte]=2020-11-04T15:56:37.000Z`
    Object updated = new HashMap(); // Object | Allows for filtering based on the date and time the booking was last updated, in ISO 8601 format (e.g. `2020-11-04T17:37:37Z`) and UTC timezone. Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?updated[lte]=2020-11-04T19:37:37Z&updated[gte]=2020-11-04T15:56:37.000Z`
    BigDecimal size = new BigDecimal("100"); // BigDecimal | Pagination size. Defaults to 100 if omitted.
    BigDecimal offset = new BigDecimal("0"); // BigDecimal | Pagination offset. Defaults to 0 if omitted.
    String sortBy = "createdAt:asc"; // String | Order in which the results should be sorted. Currently allows you to sort by `createdAt` and `updatedAt`. Specify multiple paramaters by separating with commas
    try {
      ListBookings200Response result = apiInstance.listBookings(start, end, created, updated, size, offset, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#listBookings");
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
| **start** | [**Object**](.md)| Allows for filtering based on arrival date of the booking in ISO 8601 format (e.g. &#x60;2021-12-01&#x60;). Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?start[lte]&#x3D;2021-12-20&amp;start[gte]&#x3D;2021-12-10&#x60; | [optional] |
| **end** | [**Object**](.md)| Allows for filtering based on departure date of the booking in ISO 8601 format (e.g. &#x60;2021-12-01&#x60;). Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?end[lte]&#x3D;2021-12-25&amp;end[gte]&#x3D;2021-12-15&#x60; | [optional] |
| **created** | [**Object**](.md)| Allows for filtering based on creation date and time of the booking in ISO 8601 format (e.g. &#x60;2020-11-04T17:37:37Z&#x60;) and UTC timezone. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?created[lte]&#x3D;2020-11-04T19:37:37Z&amp;created[gte]&#x3D;2020-11-04T15:56:37.000Z&#x60; | [optional] |
| **updated** | [**Object**](.md)| Allows for filtering based on the date and time the booking was last updated, in ISO 8601 format (e.g. &#x60;2020-11-04T17:37:37Z&#x60;) and UTC timezone. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?updated[lte]&#x3D;2020-11-04T19:37:37Z&amp;updated[gte]&#x3D;2020-11-04T15:56:37.000Z&#x60; | [optional] |
| **size** | **BigDecimal**| Pagination size. Defaults to 100 if omitted. | [optional] [default to 100] |
| **offset** | **BigDecimal**| Pagination offset. Defaults to 0 if omitted. | [optional] [default to 0] |
| **sortBy** | **String**| Order in which the results should be sorted. Currently allows you to sort by &#x60;createdAt&#x60; and &#x60;updatedAt&#x60;. Specify multiple paramaters by separating with commas | [optional] [default to createdAt:asc] |

### Return type

[**ListBookings200Response**](ListBookings200Response.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of bookings (filtered based on your query parameters). |  -  |
| **400** | Your request wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed. |  -  |
| **401** | Your request was sent without or with an incorrect API key. This most frequently happens when the &#x60;x-api-key&#x60; header wasn&#39;t added or contains an incorrect value. This might also happen if you&#39;re trying to access the production API endpoints with a sandbox API key or vice versa. |  -  |
| **500** | An internal server error within the Impala platform has occurred. Our team will investigate the error. We recommend that you contact us at support@impala.travel with the x-correlation-id value contained within the response headers. Sending us this value will allow us to identify the precise error you encountered. |  -  |

<a id="retrieveBooking"></a>
# **retrieveBooking**
> Booking retrieveBooking(bookingId)

Retrieve a booking

Returns all details for the specified booking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String bookingId = "bookingId_example"; // String | The unique identifier of the booking you would like to update.
    try {
      Booking result = apiInstance.retrieveBooking(bookingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#retrieveBooking");
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
| **bookingId** | **String**| The unique identifier of the booking you would like to update. | |

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the requested booking. |  -  |
| **400** | Your request wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed. |  -  |
| **401** | Your request was sent without or with an incorrect API key. This most frequently happens when the &#x60;x-api-key&#x60; header wasn&#39;t added or contains an incorrect value. This might also happen if you&#39;re trying to access the production API endpoints with a sandbox API key or vice versa. |  -  |
| **404** | You&#39;ve likely requested a booking that doesn&#39;t exist. This might be because of a typo in the booking ID. Impala booking IDs start with &#x60;IM-&#x60; for real-life bookings and &#x60;SANDBOX-&#x60; for all bookings created in our sandbox environment (e.g. &#x60;/bookings/IM-0576-00000601&#x60;). |  -  |
| **500** | An internal server error within the Impala platform has occurred. Our team will investigate the error. We recommend that you contact us at support@impala.travel with the x-correlation-id value contained within the response headers. Sending us this value will allow us to identify the precise error you encountered. |  -  |

<a id="updateBooking"></a>
# **updateBooking**
> Booking updateBooking(bookingId, updateBookingRequest)

Change a booking

&lt;!-- theme: danger --&gt;  &gt; Updates the specified booking with immediate effect. This action might result in a cancellation charge being charged.  &gt; Please note that if you wish to change the contact details associated with a booking, you should use the [Change a Booking&#39;s Contact Details](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings~1%7BbookingId%7D~1booking-contact/put) endpoint.  Changes / updates a confirmed booking with the details you provide in the request body.  When your guest needs to change their booking, you can use this endpoint to change any of the details you initially supplied when you [made their booking](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings/post), e.g. you&#39;ll need to query for availability and use the &#x60;roomTypes[].rates[].rateId&#x60; that are available currently for their new stay dates. Any new rates selected must be for the same hotel as the original booking.  A booking cannot be updated on or after the check in day of the original or new stay.  In addition, we require you do supply a &#x60;updateBookingVersionAtTimestamp&#x60; field with the &#x60;updatedAt&#x60; timestamp of the booking. You can find this value by looking up the booking via the [Retrieve a booking](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings~1%7BbookingId%7D/get) endpoint. This is to avoid race conditions where another update might have happened since the last time you have checked for the current details of this booking.  The &#x60;status&#x60; of this booking will switch back to &#x60;PENDING&#x60; until we have submitted and confirmed the new details with the hotel.  &lt;!-- theme: warning --&gt;  &gt; **This request might take up to 20 seconds to load.** While we work to return a response to your request within milliseconds in most cases, some bookings require us to re-verify current pricing in real-time and doing so might take up to 20 seconds. Please make sure your app handles this waiting state appropriately.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String bookingId = "bookingId_example"; // String | The unique identifier of the booking you would like to update.
    UpdateBookingRequest updateBookingRequest = new UpdateBookingRequest(); // UpdateBookingRequest | Specifies the room you want to book for your guest.
    try {
      Booking result = apiInstance.updateBooking(bookingId, updateBookingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#updateBooking");
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
| **bookingId** | **String**| The unique identifier of the booking you would like to update. | |
| **updateBookingRequest** | [**UpdateBookingRequest**](UpdateBookingRequest.md)| Specifies the room you want to book for your guest. | [optional] |

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | We&#39;ve submitted the change to the hotel and are returning some of its details in the response body. |  -  |
| **400** | Your request was invalid or wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed.  |  -  |
| **401** | Your request was sent without or with an incorrect API key. This most frequently happens when the &#x60;x-api-key&#x60; header wasn&#39;t added or contains an incorrect value. This might also happen if you&#39;re trying to access the production API endpoints with a sandbox API key or vice versa. |  -  |
| **404** | Not found |  -  |
| **500** | An internal server error within the Impala platform has occurred. Our team will investigate the error. We recommend that you contact us at support@impala.travel with the x-correlation-id value contained within the response headers. Sending us this value will allow us to identify the precise error you encountered. |  -  |

<a id="updateBookingContact"></a>
# **updateBookingContact**
> Booking updateBookingContact(bookingId, updateBookingContactRequest)

Change a booking contact

Updates a confirmed booking with the booking contact details you provide in the request body.  In addition, we require you to supply a &#x60;updateBookingVersionAtTimestamp&#x60; field with the &#x60;updatedAt&#x60; timestamp of the booking. You can find this value by looking up the booking via the [Retrieve a booking](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings~1%7BbookingId%7D/get) endpoint. This is to avoid race conditions where another update might have happened since the last time you have checked for the current details of this booking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String bookingId = "bookingId_example"; // String | The unique identifier of the booking you would like to update.
    UpdateBookingContactRequest updateBookingContactRequest = new UpdateBookingContactRequest(); // UpdateBookingContactRequest | 
    try {
      Booking result = apiInstance.updateBookingContact(bookingId, updateBookingContactRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#updateBookingContact");
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
| **bookingId** | **String**| The unique identifier of the booking you would like to update. | |
| **updateBookingContactRequest** | [**UpdateBookingContactRequest**](UpdateBookingContactRequest.md)|  | [optional] |

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | We&#39;ve submitted the change to the hotel and are returning the booking details in the response body. |  -  |
| **400** | Your request was invalid or wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed.  |  -  |
| **401** | Your request was sent without or with an incorrect API key. This most frequently happens when the &#x60;x-api-key&#x60; header wasn&#39;t added or contains an incorrect value. This might also happen if you&#39;re trying to access the production API endpoints with a sandbox API key or vice versa. |  -  |
| **404** | Not found |  -  |
| **500** | An internal server error within the Impala platform has occurred. Our team will investigate the error. We recommend that you contact us at support@impala.travel with the x-correlation-id value contained within the response headers. Sending us this value will allow us to identify the precise error you encountered. |  -  |

