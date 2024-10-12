# ImpalaHotelBookingApi.BookingsApi

All URIs are relative to *https://sandbox.impala.travel/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelBooking**](BookingsApi.md#cancelBooking) | **DELETE** /bookings/{bookingId} | Cancel a booking
[**createBooking**](BookingsApi.md#createBooking) | **POST** /bookings | Create a booking
[**listBookings**](BookingsApi.md#listBookings) | **GET** /bookings | List all bookings
[**retrieveBooking**](BookingsApi.md#retrieveBooking) | **GET** /bookings/{bookingId} | Retrieve a booking
[**updateBooking**](BookingsApi.md#updateBooking) | **PUT** /bookings/{bookingId} | Change a booking
[**updateBookingContact**](BookingsApi.md#updateBookingContact) | **PUT** /bookings/{bookingId}/booking-contact | Change a booking contact



## cancelBooking

> Booking cancelBooking(bookingId)

Cancel a booking

&lt;!-- theme: danger --&gt;  &gt; Cancels the specified booking with immediate effect. This action might result in a cancellation charge being charged.  Submitting this request means we&#39;ll notify the hotel of the cancellation and that they won&#39;t expect your guest.  You can use &#x60;GET /bookings/{bookingId}&#x60;to see the cancellation policies that apply to a booking at a given point in time. Please note that cancelling a booking will incur a cancellation fee according to the rules that apply at the time of cancellation. You can find the cancellation fee that has been charged in the response of this call in the &#x60;cancellation.fee&#x60; object.  If the booking you cancelled allows for a partial or full refund, we&#39;ll credit your Impala balance with the amount we charged you as the seller of this booking – meaning we&#39;ll deduct the amount the next time we&#39;re requesting payment for the sum of all the bookings you made.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.BookingsApi();
let bookingId = "bookingId_example"; // String | The unique identifier of the booking you would like to update.
apiInstance.cancelBooking(bookingId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookingId** | **String**| The unique identifier of the booking you would like to update. | 

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createBooking

> Booking createBooking(opts)

Create a booking

Creates a booking for for the rate and dates you specify in the request body.  You&#39;ll need a &#x60;roomTypes[].rates[].rateId&#x60; that&#39;s bookable for those dates, which you can find using the [Retrieve a hotel](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1hotels~1%7BhotelId%7D/get) endpoint.  If you have provided a credit card on the dashboard then **Impala will send the booking to the hotel immediately**. We&#39;ll ensure payment is taken care of before your guest arrives at the hotel.  * Your guest needs to be **paying you** the rate specified in &#x60;retailRate&#x60; (as listed in the [Retrieve a hotel](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1hotels~1%7BhotelId%7D/get) response) before you submit this request. * Once your request is received and the booking is confirmed, **Impala will charge you** as the seller this &#x60;retailRate&#x60; minus the &#x60;sellerCommissionPercentage&#x60; (which is the affiliate commission you get to keep). We&#39;ll use the business credit card you&#39;ve added to your account as payment method for this. * The difference between the amount you charge your guest (&#x60;retailRate&#x60;, e.g. 200 €) and what Impala charges you (&#x60;retailRate&#x60; minus &#x60;sellerCommissionPercentage&#x60;, e.g. 200 €) is your commission (in this example: 20 €) to keep.  You can find more information on how money flows between your guest and you, and you and Impala, [in this article](https://impala.stoplight.io/docs/booking-api/branches/v1.003/docs/good-to-know/payments-and-commissions.md)  &lt;!-- theme: warning --&gt;  &gt; **This request might take up to 20 seconds to load.** While we work to return a response to your request within milliseconds in most cases, some bookings require us to re-verify current pricing in real-time and doing so might take up to 20 seconds. Please make sure your app handles this waiting state appropriately.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.BookingsApi();
let opts = {
  'bookingRequest': {"bookingContact":{"email":"jocelin.carreon.crespo@example.com","firstName":"Jocelín","lastName":"Carreón Sample"},"end":"2019-08-24","rooms":[{"adults":2,"rateId":"i8fIZ277SPDq4UohuxAft5Sr29UhMvyc0VypRxLiRFLoTk0XHmEbgSQ"}],"start":"2019-08-24"} // BookingRequest | Specifies the room you want to book for your guest.
};
apiInstance.createBooking(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookingRequest** | [**BookingRequest**](BookingRequest.md)| Specifies the room you want to book for your guest. | [optional] 

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listBookings

> ListBookings200Response listBookings(opts)

List all bookings

Returns a list of all the bookings you&#39;ve made.  You can filter the list based on when bookings were created or last updated, as well as their arrival (&#x60;start&#x60;) and departure (&#x60;end&#x60;). These date-based filters allow to narrow down the result with modifiers for less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;).  Example: Adding the query parameters &#x60;start[gt]&#x3D;2021-05-20&amp;updated[lte]&#x3D;2020-11-20T11:11:00.000Z&#x60; would return bookings arriving after May 20th, 2020 that were updated before or on November 20th, 2020 at 11:11 am UTC.  You can specify the **sorting order** in which bookings are returned: * This is done by using the &#x60;sortBy&#x60; query parameter. * Results can be sorted by &#x60;createdAt&#x60; and &#x60;updatedAt&#x60; * The parameter allows for a comma-separated list of arguments with &#x60;:asc&#x60; (ascending, the default if no sorting is specified) and &#x60;:desc&#x60; (descending) modifiers.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.BookingsApi();
let opts = {
  'start': {key: null}, // Object | Allows for filtering based on arrival date of the booking in ISO 8601 format (e.g. `2021-12-01`). Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?start[lte]=2021-12-20&start[gte]=2021-12-10`
  'end': {key: null}, // Object | Allows for filtering based on departure date of the booking in ISO 8601 format (e.g. `2021-12-01`). Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?end[lte]=2021-12-25&end[gte]=2021-12-15`
  'created': {key: null}, // Object | Allows for filtering based on creation date and time of the booking in ISO 8601 format (e.g. `2020-11-04T17:37:37Z`) and UTC timezone. Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?created[lte]=2020-11-04T19:37:37Z&created[gte]=2020-11-04T15:56:37.000Z`
  'updated': {key: null}, // Object | Allows for filtering based on the date and time the booking was last updated, in ISO 8601 format (e.g. `2020-11-04T17:37:37Z`) and UTC timezone. Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?updated[lte]=2020-11-04T19:37:37Z&updated[gte]=2020-11-04T15:56:37.000Z`
  'size': 100, // Number | Pagination size. Defaults to 100 if omitted.
  'offset': 0, // Number | Pagination offset. Defaults to 0 if omitted.
  'sortBy': "createdAt:desc,updatedAt:asc" // String | Order in which the results should be sorted. Currently allows you to sort by `createdAt` and `updatedAt`. Specify multiple paramaters by separating with commas
};
apiInstance.listBookings(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**Object**](.md)| Allows for filtering based on arrival date of the booking in ISO 8601 format (e.g. &#x60;2021-12-01&#x60;). Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?start[lte]&#x3D;2021-12-20&amp;start[gte]&#x3D;2021-12-10&#x60; | [optional] 
 **end** | [**Object**](.md)| Allows for filtering based on departure date of the booking in ISO 8601 format (e.g. &#x60;2021-12-01&#x60;). Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?end[lte]&#x3D;2021-12-25&amp;end[gte]&#x3D;2021-12-15&#x60; | [optional] 
 **created** | [**Object**](.md)| Allows for filtering based on creation date and time of the booking in ISO 8601 format (e.g. &#x60;2020-11-04T17:37:37Z&#x60;) and UTC timezone. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?created[lte]&#x3D;2020-11-04T19:37:37Z&amp;created[gte]&#x3D;2020-11-04T15:56:37.000Z&#x60; | [optional] 
 **updated** | [**Object**](.md)| Allows for filtering based on the date and time the booking was last updated, in ISO 8601 format (e.g. &#x60;2020-11-04T17:37:37Z&#x60;) and UTC timezone. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?updated[lte]&#x3D;2020-11-04T19:37:37Z&amp;updated[gte]&#x3D;2020-11-04T15:56:37.000Z&#x60; | [optional] 
 **size** | **Number**| Pagination size. Defaults to 100 if omitted. | [optional] [default to 100]
 **offset** | **Number**| Pagination offset. Defaults to 0 if omitted. | [optional] [default to 0]
 **sortBy** | **String**| Order in which the results should be sorted. Currently allows you to sort by &#x60;createdAt&#x60; and &#x60;updatedAt&#x60;. Specify multiple paramaters by separating with commas | [optional] [default to &#39;createdAt:asc&#39;]

### Return type

[**ListBookings200Response**](ListBookings200Response.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveBooking

> Booking retrieveBooking(bookingId)

Retrieve a booking

Returns all details for the specified booking.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.BookingsApi();
let bookingId = "bookingId_example"; // String | The unique identifier of the booking you would like to update.
apiInstance.retrieveBooking(bookingId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookingId** | **String**| The unique identifier of the booking you would like to update. | 

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBooking

> Booking updateBooking(bookingId, opts)

Change a booking

&lt;!-- theme: danger --&gt;  &gt; Updates the specified booking with immediate effect. This action might result in a cancellation charge being charged.  &gt; Please note that if you wish to change the contact details associated with a booking, you should use the [Change a Booking&#39;s Contact Details](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings~1%7BbookingId%7D~1booking-contact/put) endpoint.  Changes / updates a confirmed booking with the details you provide in the request body.  When your guest needs to change their booking, you can use this endpoint to change any of the details you initially supplied when you [made their booking](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings/post), e.g. you&#39;ll need to query for availability and use the &#x60;roomTypes[].rates[].rateId&#x60; that are available currently for their new stay dates. Any new rates selected must be for the same hotel as the original booking.  A booking cannot be updated on or after the check in day of the original or new stay.  In addition, we require you do supply a &#x60;updateBookingVersionAtTimestamp&#x60; field with the &#x60;updatedAt&#x60; timestamp of the booking. You can find this value by looking up the booking via the [Retrieve a booking](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings~1%7BbookingId%7D/get) endpoint. This is to avoid race conditions where another update might have happened since the last time you have checked for the current details of this booking.  The &#x60;status&#x60; of this booking will switch back to &#x60;PENDING&#x60; until we have submitted and confirmed the new details with the hotel.  &lt;!-- theme: warning --&gt;  &gt; **This request might take up to 20 seconds to load.** While we work to return a response to your request within milliseconds in most cases, some bookings require us to re-verify current pricing in real-time and doing so might take up to 20 seconds. Please make sure your app handles this waiting state appropriately.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.BookingsApi();
let bookingId = "bookingId_example"; // String | The unique identifier of the booking you would like to update.
let opts = {
  'updateBookingRequest': {"bookingContact":{"email":"jocelin.carreon.crespo@example.com","firstName":"Jocelín","lastName":"Carreón Sample"},"end":"2019-08-24","rooms":[{"adults":2,"rateId":"i8fIZ277SPDq4UohuxAft5Sr29UhMvyc0VypRxLiRFLoTk0XHmEbgSQ"}],"start":"2019-08-24","updateBookingVersionAtTimestamp":"2020-12-20T11:01:30.745Z"} // UpdateBookingRequest | Specifies the room you want to book for your guest.
};
apiInstance.updateBooking(bookingId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookingId** | **String**| The unique identifier of the booking you would like to update. | 
 **updateBookingRequest** | [**UpdateBookingRequest**](UpdateBookingRequest.md)| Specifies the room you want to book for your guest. | [optional] 

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBookingContact

> Booking updateBookingContact(bookingId, opts)

Change a booking contact

Updates a confirmed booking with the booking contact details you provide in the request body.  In addition, we require you to supply a &#x60;updateBookingVersionAtTimestamp&#x60; field with the &#x60;updatedAt&#x60; timestamp of the booking. You can find this value by looking up the booking via the [Retrieve a booking](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings~1%7BbookingId%7D/get) endpoint. This is to avoid race conditions where another update might have happened since the last time you have checked for the current details of this booking.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.BookingsApi();
let bookingId = "bookingId_example"; // String | The unique identifier of the booking you would like to update.
let opts = {
  'updateBookingContactRequest': new ImpalaHotelBookingApi.UpdateBookingContactRequest() // UpdateBookingContactRequest | 
};
apiInstance.updateBookingContact(bookingId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookingId** | **String**| The unique identifier of the booking you would like to update. | 
 **updateBookingContactRequest** | [**UpdateBookingContactRequest**](UpdateBookingContactRequest.md)|  | [optional] 

### Return type

[**Booking**](Booking.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

