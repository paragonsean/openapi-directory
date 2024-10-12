# BookingsApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bookingsCancelReservation**](BookingsApi.md#bookingsCancelReservation) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/cancel | Cancel one reservation. |
| [**bookingsCheckIn**](BookingsApi.md#bookingsCheckIn) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/check_in | Performs a check in operation for a reservation. |
| [**bookingsCheckOut**](BookingsApi.md#bookingsCheckOut) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/check_out | Performs a check out operation for a reservation. |
| [**bookingsCreateBooking**](BookingsApi.md#bookingsCreateBooking) | **POST** /api/booking/v0/bookings | Create a new booking. |
| [**bookingsGetBooking**](BookingsApi.md#bookingsGetBooking) | **GET** /api/booking/v0/bookings/{confirmationId} | Load all reservations for one booking by confirmation id. |
| [**bookingsGetBookings**](BookingsApi.md#bookingsGetBookings) | **GET** /api/booking/v0/bookings | Find bookings matching the given filter criteria. |
| [**bookingsGetBookingsCount**](BookingsApi.md#bookingsGetBookingsCount) | **GET** /api/booking/v0/bookings/$count | Get total count of bookings matchung the given filter criteria. |
| [**bookingsGetReservation**](BookingsApi.md#bookingsGetReservation) | **GET** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber} | Load a specific reservation from a booking. |
| [**bookingsPatch**](BookingsApi.md#bookingsPatch) | **PATCH** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber} | Partially updates a reservation. |
| [**bookingsPaymentToken**](BookingsApi.md#bookingsPaymentToken) | **PUT** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/payment_token | Post a payment token for a reservation. |
| [**bookingsPostRoomAssignment**](BookingsApi.md#bookingsPostRoomAssignment) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/assign_room | Assign a room to a reservation. |
| [**bookingsTerminalAuthorization**](BookingsApi.md#bookingsTerminalAuthorization) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/pre_authorize | Performs a chip and pin credit card authorization for a reservation. |


<a id="bookingsCancelReservation"></a>
# **bookingsCancelReservation**
> CancellationResponse bookingsCancelReservation(appId, appKey, confirmationId, reservationNumber, sendConfirmation)

Cancel one reservation.

This request will cancel one specific reservation. It will show up in the hetras UI in the Cancellation and NoShow              processing screen and it will be up to the hotel staff to either charge or waive the cancellation fee.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
    Integer reservationNumber = 56; // Integer | Specifies the reservation number for the reservation to cancel.
    Boolean sendConfirmation = true; // Boolean | Whether to send a confirmation email to the primary guest
    try {
      CancellationResponse result = apiInstance.bookingsCancelReservation(appId, appKey, confirmationId, reservationNumber, sendConfirmation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsCancelReservation");
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
| **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | |
| **reservationNumber** | **Integer**| Specifies the reservation number for the reservation to cancel. | |
| **sendConfirmation** | **Boolean**| Whether to send a confirmation email to the primary guest | [optional] |

### Return type

[**CancellationResponse**](CancellationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the cancellation id and the cancellation fee that will be charged to the folio of the reservation. |  -  |
| **400** | Bad request. Request body erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsCheckIn"></a>
# **bookingsCheckIn**
> BaseResponse bookingsCheckIn(appId, appKey, confirmationId, reservationNumber, checkInDetails)

Performs a check in operation for a reservation.

With this call you can set a reservation to the status inhouse. It allows only single room reservations to be checked in.              The reservation must have assigned a vacant and clean room.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
    Integer reservationNumber = 56; // Integer | Specifies the reservation number for the reservation to be checked in.
    CheckInDetails checkInDetails = new CheckInDetails(); // CheckInDetails | Specifies checkIn details, for example Client Identity.
    try {
      BaseResponse result = apiInstance.bookingsCheckIn(appId, appKey, confirmationId, reservationNumber, checkInDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsCheckIn");
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
| **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | |
| **reservationNumber** | **Integer**| Specifies the reservation number for the reservation to be checked in. | |
| **checkInDetails** | [**CheckInDetails**](CheckInDetails.md)| Specifies checkIn details, for example Client Identity. | |

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The check in was successful |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. The reason could be wrong room or reservation status, wrong start date of reservation etc. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsCheckOut"></a>
# **bookingsCheckOut**
> BaseResponse bookingsCheckOut(appId, appKey, confirmationId, reservationNumber)

Performs a check out operation for a reservation.

With this call you can set a reservation to the checkout status. It allows only single room reservations to be checked out.              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
    Integer reservationNumber = 56; // Integer | Specifies the reservation number for the reservation to be checked out.
    try {
      BaseResponse result = apiInstance.bookingsCheckOut(appId, appKey, confirmationId, reservationNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsCheckOut");
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
| **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | |
| **reservationNumber** | **Integer**| Specifies the reservation number for the reservation to be checked out. | |

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The check out was successful |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. The reason could be wrong reservation status, such as it was already checked out. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsCreateBooking"></a>
# **bookingsCreateBooking**
> ReservationConfirmation bookingsCreateBooking(appId, appKey, reservation, sendConfirmation)

Create a new booking.

Create a new booking as defined in the requests payload. You can get more information about the payload if you check out the              documentation for the reservation request model.&lt;br /&gt;              Please also have a look at the &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/tutorials\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Tutorials&lt;/a&gt;.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Reservation reservation = new Reservation(); // Reservation | Specifies the details of the booking to be created.
    Boolean sendConfirmation = true; // Boolean | Whether to send a confirmation email to the primary guest
    try {
      ReservationConfirmation result = apiInstance.bookingsCreateBooking(appId, appKey, reservation, sendConfirmation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsCreateBooking");
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
| **reservation** | [**Reservation**](Reservation.md)| Specifies the details of the booking to be created. | |
| **sendConfirmation** | **Boolean**| Whether to send a confirmation email to the primary guest | [optional] |

### Return type

[**ReservationConfirmation**](ReservationConfirmation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The creation of the booking was successful. You will get back the confirmation id and maybe warnings, if              e.g. the prepayment could not be captured. |  -  |
| **400** | Bad request. Request body erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsGetBooking"></a>
# **bookingsGetBooking**
> ReservationsResponse bookingsGetBooking(appId, appKey, confirmationId, expand, exclude)

Load all reservations for one booking by confirmation id.

A booking groups all reservations done in one single request and can be identified by the confirmation id.              Guests usually use the confirmation id to check in at the kiosk, on the website or mobile device. In hetras              all reservations of one booking share the room type, rate plan and number of guests per room.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String confirmationId = "confirmationId_example"; // String | The confirmation id for the booking to load.
    String expand = "None"; // String | Specifies the expand type.
    String exclude = "None"; // String | Specifies the exclude type.
    try {
      ReservationsResponse result = apiInstance.bookingsGetBooking(appId, appKey, confirmationId, expand, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsGetBooking");
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
| **confirmationId** | **String**| The confirmation id for the booking to load. | |
| **expand** | **String**| Specifies the expand type. | [optional] [enum: None, RoomRates] |
| **exclude** | **String**| Specifies the exclude type. | [optional] [enum: None, Customers] |

### Return type

[**ReservationsResponse**](ReservationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of all reservations for that booking. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsGetBookings"></a>
# **bookingsGetBookings**
> BookingListResponse bookingsGetBookings(appId, appKey, hotelId, cancellationId, reservationNumber, customerName, customerEmail, customerId, roomNumber, externalId, companyName, companyId, companyEmail, blockCode, reservationStatuses, marketCodes, channelCodes, subChannelCodes, roomTypes, ratePlanCodes, labels, from, to, dateFilter, exclude, skip, top, inlinecount)

Find bookings matching the given filter criteria.

Here you can easily find bookings matching various criteria. The booking you are looking for has to fullfill all the specified criteria              at the same time. So if you specify a customer name and a channel code you will get all bookings where the firstname or lastname of a guest or a               contact contains the specified value and that have been done through the defined channel.              A booking can consist of multiple reservations, so even if you are looking for a specific reservation which is part of a multi-room booking you will get              all reservations for this booking returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | Only return bookings for this specific hotel.
    String cancellationId = "cancellationId_example"; // String | Return bookings for this cancellation id.
    Integer reservationNumber = 56; // Integer | Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels.
    String customerName = "customerName_example"; // String | Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    String customerEmail = "customerEmail_example"; // String | Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    String customerId = "customerId_example"; // String | Return all bookings the id of one of the guests or the contact matches the specified value.
    String roomNumber = "roomNumber_example"; // String | Return all bookings having the specified room number assigned.
    String externalId = "externalId_example"; // String | Return all bookings exactly matching the specified external id. This filter is case sensitive.
    String companyName = "companyName_example"; // String | Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    String companyId = "companyId_example"; // String | Return all bookings the id of the company or travel agent profile matches the specified value.
    String companyEmail = "companyEmail_example"; // String | Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    String blockCode = "blockCode_example"; // String | Return all bookings where the block code matches the specified value.
    List<String> reservationStatuses = Arrays.asList(); // List<String> | Return all bookings where the reservation status is one of the specified values.
    List<String> marketCodes = Arrays.asList(); // List<String> | Return all bookings where the market code is one of the specified values.
    List<String> channelCodes = Arrays.asList(); // List<String> | Return all bookings where the channel code is one of the specified values.
    List<String> subChannelCodes = Arrays.asList(); // List<String> | Return all bookings where the subchannel code is one of the specified values.
    List<String> roomTypes = Arrays.asList(); // List<String> | Return all bookings where the room type is one of the specified values.
    List<String> ratePlanCodes = Arrays.asList(); // List<String> | Return all bookings where the rate plan code is one of the specified values.
    List<String> labels = Arrays.asList(); // List<String> | Return all reservations with at least one of the specified labels.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier.
    String dateFilter = "ArrivalDate"; // String | Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range.
    String exclude = "Customers"; // String | To be able to request reservations without personal data based on GDPR.
    Integer skip = 56; // Integer | Amount of items to skip.
    Integer top = 56; // Integer | Amount of items to select.
    String inlinecount = "None"; // String | Return total number of items for a given filter criteria.
    try {
      BookingListResponse result = apiInstance.bookingsGetBookings(appId, appKey, hotelId, cancellationId, reservationNumber, customerName, customerEmail, customerId, roomNumber, externalId, companyName, companyId, companyEmail, blockCode, reservationStatuses, marketCodes, channelCodes, subChannelCodes, roomTypes, ratePlanCodes, labels, from, to, dateFilter, exclude, skip, top, inlinecount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsGetBookings");
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
| **hotelId** | **Integer**| Only return bookings for this specific hotel. | [optional] |
| **cancellationId** | **String**| Return bookings for this cancellation id. | [optional] |
| **reservationNumber** | **Integer**| Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels. | [optional] |
| **customerName** | **String**| Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] |
| **customerEmail** | **String**| Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] |
| **customerId** | **String**| Return all bookings the id of one of the guests or the contact matches the specified value. | [optional] |
| **roomNumber** | **String**| Return all bookings having the specified room number assigned. | [optional] |
| **externalId** | **String**| Return all bookings exactly matching the specified external id. This filter is case sensitive. | [optional] |
| **companyName** | **String**| Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] |
| **companyId** | **String**| Return all bookings the id of the company or travel agent profile matches the specified value. | [optional] |
| **companyEmail** | **String**| Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] |
| **blockCode** | **String**| Return all bookings where the block code matches the specified value. | [optional] |
| **reservationStatuses** | [**List&lt;String&gt;**](String.md)| Return all bookings where the reservation status is one of the specified values. | [optional] [enum: Tentative, Waitlisted, OnRequest, NonGuaranteed, Guaranteed, InHouse, CheckedOut, NoShow, Denied, Cancelled, Released, Walked, Expired, WalkIn, Registered] |
| **marketCodes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the market code is one of the specified values. | [optional] |
| **channelCodes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the channel code is one of the specified values. | [optional] |
| **subChannelCodes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the subchannel code is one of the specified values. | [optional] |
| **roomTypes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the room type is one of the specified values. | [optional] |
| **ratePlanCodes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the rate plan code is one of the specified values. | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| Return all reservations with at least one of the specified labels. | [optional] |
| **from** | **OffsetDateTime**| Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later. | [optional] |
| **to** | **OffsetDateTime**| End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier. | [optional] |
| **dateFilter** | **String**| Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range. | [optional] [enum: ArrivalDate, DepartureDate, StayDate, CreationDate, ModificationDate] |
| **exclude** | **String**| To be able to request reservations without personal data based on GDPR. | [optional] [enum: Customers] |
| **skip** | **Integer**| Amount of items to skip. | [optional] |
| **top** | **Integer**| Amount of items to select. | [optional] |
| **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] [enum: None, AllPages] |

### Return type

[**BookingListResponse**](BookingListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of reservations for the requested hotel identifier. |  -  |
| **204** | There are no bookings matching your filter criteria. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsGetBookingsCount"></a>
# **bookingsGetBookingsCount**
> TotalCountResponse bookingsGetBookingsCount(appId, appKey, hotelId, cancellationId, reservationNumber, customerName, customerEmail, customerId, roomNumber, externalId, companyName, companyId, companyEmail, blockCode, reservationStatuses, marketCodes, channelCodes, subChannelCodes, roomTypes, ratePlanCodes, labels, from, to, dateFilter, exclude)

Get total count of bookings matchung the given filter criteria.

Get the count of all bookings matching your criteria. The bookings have to fullfill all the specified criteria              at the same time. So if you specify a customer name and a channel code you will get the count for all bookings where the firstname or lastname               of a guest or a contact contains the specified value and that have been done through the defined channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | Only return bookings for this specific hotel.
    String cancellationId = "cancellationId_example"; // String | Return bookings for this cancellation id.
    Integer reservationNumber = 56; // Integer | Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels.
    String customerName = "customerName_example"; // String | Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    String customerEmail = "customerEmail_example"; // String | Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    String customerId = "customerId_example"; // String | Return all bookings the id of one of the guests or the contact matches the specified value.
    String roomNumber = "roomNumber_example"; // String | Return all bookings having the specified room number assigned.
    String externalId = "externalId_example"; // String | Return all bookings exactly matching the specified external id. This filter is case sensitive.
    String companyName = "companyName_example"; // String | Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    String companyId = "companyId_example"; // String | Return all bookings the id of the company or travel agent profile matches the specified value.
    String companyEmail = "companyEmail_example"; // String | Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    String blockCode = "blockCode_example"; // String | Return all bookings where the block code matches the specified value.
    List<String> reservationStatuses = Arrays.asList(); // List<String> | Return all bookings where the reservation status is one of the specified values.
    List<String> marketCodes = Arrays.asList(); // List<String> | Return all bookings where the market code is one of the specified values.
    List<String> channelCodes = Arrays.asList(); // List<String> | Return all bookings where the channel code is one of the specified values.
    List<String> subChannelCodes = Arrays.asList(); // List<String> | Return all bookings where the subchannel code is one of the specified values.
    List<String> roomTypes = Arrays.asList(); // List<String> | Return all bookings where the room type is one of the specified values.
    List<String> ratePlanCodes = Arrays.asList(); // List<String> | Return all bookings where the rate plan code is one of the specified values.
    List<String> labels = Arrays.asList(); // List<String> | Return all reservations with at least one of the specified labels.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier.
    String dateFilter = "ArrivalDate"; // String | Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range.
    String exclude = "Customers"; // String | To be able to request reservations without personal data based on GDPR.
    try {
      TotalCountResponse result = apiInstance.bookingsGetBookingsCount(appId, appKey, hotelId, cancellationId, reservationNumber, customerName, customerEmail, customerId, roomNumber, externalId, companyName, companyId, companyEmail, blockCode, reservationStatuses, marketCodes, channelCodes, subChannelCodes, roomTypes, ratePlanCodes, labels, from, to, dateFilter, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsGetBookingsCount");
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
| **hotelId** | **Integer**| Only return bookings for this specific hotel. | [optional] |
| **cancellationId** | **String**| Return bookings for this cancellation id. | [optional] |
| **reservationNumber** | **Integer**| Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels. | [optional] |
| **customerName** | **String**| Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] |
| **customerEmail** | **String**| Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] |
| **customerId** | **String**| Return all bookings the id of one of the guests or the contact matches the specified value. | [optional] |
| **roomNumber** | **String**| Return all bookings having the specified room number assigned. | [optional] |
| **externalId** | **String**| Return all bookings exactly matching the specified external id. This filter is case sensitive. | [optional] |
| **companyName** | **String**| Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] |
| **companyId** | **String**| Return all bookings the id of the company or travel agent profile matches the specified value. | [optional] |
| **companyEmail** | **String**| Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] |
| **blockCode** | **String**| Return all bookings where the block code matches the specified value. | [optional] |
| **reservationStatuses** | [**List&lt;String&gt;**](String.md)| Return all bookings where the reservation status is one of the specified values. | [optional] [enum: Tentative, Waitlisted, OnRequest, NonGuaranteed, Guaranteed, InHouse, CheckedOut, NoShow, Denied, Cancelled, Released, Walked, Expired, WalkIn, Registered] |
| **marketCodes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the market code is one of the specified values. | [optional] |
| **channelCodes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the channel code is one of the specified values. | [optional] |
| **subChannelCodes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the subchannel code is one of the specified values. | [optional] |
| **roomTypes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the room type is one of the specified values. | [optional] |
| **ratePlanCodes** | [**List&lt;String&gt;**](String.md)| Return all bookings where the rate plan code is one of the specified values. | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| Return all reservations with at least one of the specified labels. | [optional] |
| **from** | **OffsetDateTime**| Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later. | [optional] |
| **to** | **OffsetDateTime**| End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier. | [optional] |
| **dateFilter** | **String**| Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range. | [optional] [enum: ArrivalDate, DepartureDate, StayDate, CreationDate, ModificationDate] |
| **exclude** | **String**| To be able to request reservations without personal data based on GDPR. | [optional] [enum: Customers] |

### Return type

[**TotalCountResponse**](TotalCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The total booking count for a given filter criteria. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsGetReservation"></a>
# **bookingsGetReservation**
> ReservationResponse bookingsGetReservation(appId, appKey, confirmationId, reservationNumber, expand, exclude)

Load a specific reservation from a booking.

With this request you can load one specific reservation done with one booking request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
    Integer reservationNumber = 56; // Integer | Specifies the reservation number for the reservation to load.
    String expand = "None"; // String | Specifies the expand type.
    String exclude = "None"; // String | Specifies the exclude type.
    try {
      ReservationResponse result = apiInstance.bookingsGetReservation(appId, appKey, confirmationId, reservationNumber, expand, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsGetReservation");
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
| **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | |
| **reservationNumber** | **Integer**| Specifies the reservation number for the reservation to load. | |
| **expand** | **String**| Specifies the expand type. | [optional] [enum: None, RoomRates] |
| **exclude** | **String**| Specifies the exclude type. | [optional] [enum: None, Customers] |

### Return type

[**ReservationResponse**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the details of the reservation specified. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsPatch"></a>
# **bookingsPatch**
> Object bookingsPatch(appId, appKey, confirmationId, reservationNumber, patchRequest)

Partially updates a reservation.

The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call allows to update the following fields:              external_id, market_code, channel_code, subchannel_code, guarantee_type, comment, addon_services, labels, guests, contact and company.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/addon_services\&quot;, \&quot;value\&quot;: [\&quot;BREAKFAST\&quot;, \&quot;PARKING\&quot;]                },                {                  \&quot;op\&quot;: \&quot;add\&quot;, \&quot;path\&quot;: \&quot;/labels/-\&quot;, \&quot;value\&quot;: \&quot;MOBILE\&quot;                },                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/guests/SHOW-1234\&quot;, \&quot;value\&quot;: { \&quot;customer_id\&quot;: \&quot;SHOW-1234\&quot;, \&quot;primary\&quot;: false }                },                {                  \&quot;op\&quot;: \&quot;add\&quot;, \&quot;path\&quot;: \&quot;/guests/-\&quot;, \&quot;value\&quot;: { \&quot;customer_id\&quot;: \&quot;SHOW-5678\&quot;, \&quot;primary\&quot;: true }                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
    Integer reservationNumber = 56; // Integer | Specifies the reservation number for the reservation that has to be updated.
    List<OperationReservationPatchableModel> patchRequest = Arrays.asList(); // List<OperationReservationPatchableModel> | A set of JSON Patch operations
    try {
      Object result = apiInstance.bookingsPatch(appId, appKey, confirmationId, reservationNumber, patchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsPatch");
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
| **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | |
| **reservationNumber** | **Integer**| Specifies the reservation number for the reservation that has to be updated. | |
| **patchRequest** | [**List&lt;OperationReservationPatchableModel&gt;**](OperationReservationPatchableModel.md)| A set of JSON Patch operations | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The update was successful. Reponse would contain a referer to the updated reservation. |  -  |
| **400** | Bad request. Request body erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsPaymentToken"></a>
# **bookingsPaymentToken**
> BaseResponse bookingsPaymentToken(appId, appKey, confirmationId, reservationNumber, authorizationRequest)

Post a payment token for a reservation.

TBD.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
    Integer reservationNumber = 56; // Integer | Specifies the reservation number for the reservation to be checked in.
    AuthorizationRequest authorizationRequest = new AuthorizationRequest(); // AuthorizationRequest | 
    try {
      BaseResponse result = apiInstance.bookingsPaymentToken(appId, appKey, confirmationId, reservationNumber, authorizationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsPaymentToken");
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
| **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | |
| **reservationNumber** | **Integer**| Specifies the reservation number for the reservation to be checked in. | |
| **authorizationRequest** | [**AuthorizationRequest**](AuthorizationRequest.md)|  | |

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The payment token was added successfully |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. The reason could be wrong room or reservation status, wrong start date of reservation etc. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsPostRoomAssignment"></a>
# **bookingsPostRoomAssignment**
> AssignRoomResponse bookingsPostRoomAssignment(appId, appKey, confirmationId, reservationNumber, assigningCriteria)

Assign a room to a reservation.

By default this API call assigns a random room, which has the proper room type, is not already assigned              to another reservation or has any maintenance status set for the stay period of the underlying reservation. If the              arrival date for the underlying reservation is the current business day dirty rooms are excluded by default. For reservation              arriving on any latter day the room condition is not taken into account.&lt;br /&gt;              By specifiying the room selection criteria in the request body you can influence which room will be assigned. See the request model              for further details.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
    Integer reservationNumber = 56; // Integer | Specifies the reservation number for the reservation the room should be assigned to.
    AssignRoomCriteria assigningCriteria = new AssignRoomCriteria(); // AssignRoomCriteria | Specifies the criteria for the room selection.
    try {
      AssignRoomResponse result = apiInstance.bookingsPostRoomAssignment(appId, appKey, confirmationId, reservationNumber, assigningCriteria);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsPostRoomAssignment");
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
| **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | |
| **reservationNumber** | **Integer**| Specifies the reservation number for the reservation the room should be assigned to. | |
| **assigningCriteria** | [**AssignRoomCriteria**](AssignRoomCriteria.md)| Specifies the criteria for the room selection. | [optional] |

### Return type

[**AssignRoomResponse**](AssignRoomResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The room assignment was successful. The Reponse would contain the room number assigned. |  -  |
| **400** | Bad request. Request body erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. The reason could be no available rooms or a mismatch of room types etc. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

<a id="bookingsTerminalAuthorization"></a>
# **bookingsTerminalAuthorization**
> BaseResponse bookingsTerminalAuthorization(appId, appKey, confirmationId, reservationNumber, authorizationRequest)

Performs a chip and pin credit card authorization for a reservation.

With this call you can trigger a terminal authorization prompt for a reservation guest.               For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    BookingsApi apiInstance = new BookingsApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    String confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
    Integer reservationNumber = 56; // Integer | Specifies the reservation number for the reservation to be checked in.
    TerminalAuthorizationRequest authorizationRequest = new TerminalAuthorizationRequest(); // TerminalAuthorizationRequest | Specifies authorization details, such as amount and client identity.
    try {
      BaseResponse result = apiInstance.bookingsTerminalAuthorization(appId, appKey, confirmationId, reservationNumber, authorizationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingsApi#bookingsTerminalAuthorization");
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
| **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | |
| **reservationNumber** | **Integer**| Specifies the reservation number for the reservation to be checked in. | |
| **authorizationRequest** | [**TerminalAuthorizationRequest**](TerminalAuthorizationRequest.md)| Specifies authorization details, such as amount and client identity. | |

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. The reason could be wrong room or reservation status, wrong start date of reservation etc. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

