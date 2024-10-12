# HetrasBookingApiVersion0.BookingsApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookingsCancelReservation**](BookingsApi.md#bookingsCancelReservation) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/cancel | Cancel one reservation.
[**bookingsCheckIn**](BookingsApi.md#bookingsCheckIn) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/check_in | Performs a check in operation for a reservation.
[**bookingsCheckOut**](BookingsApi.md#bookingsCheckOut) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/check_out | Performs a check out operation for a reservation.
[**bookingsCreateBooking**](BookingsApi.md#bookingsCreateBooking) | **POST** /api/booking/v0/bookings | Create a new booking.
[**bookingsGetBooking**](BookingsApi.md#bookingsGetBooking) | **GET** /api/booking/v0/bookings/{confirmationId} | Load all reservations for one booking by confirmation id.
[**bookingsGetBookings**](BookingsApi.md#bookingsGetBookings) | **GET** /api/booking/v0/bookings | Find bookings matching the given filter criteria.
[**bookingsGetBookingsCount**](BookingsApi.md#bookingsGetBookingsCount) | **GET** /api/booking/v0/bookings/$count | Get total count of bookings matchung the given filter criteria.
[**bookingsGetReservation**](BookingsApi.md#bookingsGetReservation) | **GET** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber} | Load a specific reservation from a booking.
[**bookingsPatch**](BookingsApi.md#bookingsPatch) | **PATCH** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber} | Partially updates a reservation.
[**bookingsPaymentToken**](BookingsApi.md#bookingsPaymentToken) | **PUT** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/payment_token | Post a payment token for a reservation.
[**bookingsPostRoomAssignment**](BookingsApi.md#bookingsPostRoomAssignment) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/assign_room | Assign a room to a reservation.
[**bookingsTerminalAuthorization**](BookingsApi.md#bookingsTerminalAuthorization) | **POST** /api/booking/v0/bookings/{confirmationId}/reservations/{reservationNumber}/pre_authorize | Performs a chip and pin credit card authorization for a reservation.



## bookingsCancelReservation

> CancellationResponse bookingsCancelReservation(appId, appKey, confirmationId, reservationNumber, opts)

Cancel one reservation.

This request will cancel one specific reservation. It will show up in the hetras UI in the Cancellation and NoShow              processing screen and it will be up to the hotel staff to either charge or waive the cancellation fee.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
let reservationNumber = 56; // Number | Specifies the reservation number for the reservation to cancel.
let opts = {
  'sendConfirmation': true // Boolean | Whether to send a confirmation email to the primary guest
};
apiInstance.bookingsCancelReservation(appId, appKey, confirmationId, reservationNumber, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | 
 **reservationNumber** | **Number**| Specifies the reservation number for the reservation to cancel. | 
 **sendConfirmation** | **Boolean**| Whether to send a confirmation email to the primary guest | [optional] 

### Return type

[**CancellationResponse**](CancellationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## bookingsCheckIn

> BaseResponse bookingsCheckIn(appId, appKey, confirmationId, reservationNumber, checkInDetails)

Performs a check in operation for a reservation.

With this call you can set a reservation to the status inhouse. It allows only single room reservations to be checked in.              The reservation must have assigned a vacant and clean room.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
let reservationNumber = 56; // Number | Specifies the reservation number for the reservation to be checked in.
let checkInDetails = new HetrasBookingApiVersion0.CheckInDetails(); // CheckInDetails | Specifies checkIn details, for example Client Identity.
apiInstance.bookingsCheckIn(appId, appKey, confirmationId, reservationNumber, checkInDetails, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | 
 **reservationNumber** | **Number**| Specifies the reservation number for the reservation to be checked in. | 
 **checkInDetails** | [**CheckInDetails**](CheckInDetails.md)| Specifies checkIn details, for example Client Identity. | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## bookingsCheckOut

> BaseResponse bookingsCheckOut(appId, appKey, confirmationId, reservationNumber)

Performs a check out operation for a reservation.

With this call you can set a reservation to the checkout status. It allows only single room reservations to be checked out.              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
let reservationNumber = 56; // Number | Specifies the reservation number for the reservation to be checked out.
apiInstance.bookingsCheckOut(appId, appKey, confirmationId, reservationNumber, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | 
 **reservationNumber** | **Number**| Specifies the reservation number for the reservation to be checked out. | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## bookingsCreateBooking

> ReservationConfirmation bookingsCreateBooking(appId, appKey, reservation, opts)

Create a new booking.

Create a new booking as defined in the requests payload. You can get more information about the payload if you check out the              documentation for the reservation request model.&lt;br /&gt;              Please also have a look at the &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/tutorials\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Tutorials&lt;/a&gt;.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let reservation = new HetrasBookingApiVersion0.Reservation(); // Reservation | Specifies the details of the booking to be created.
let opts = {
  'sendConfirmation': true // Boolean | Whether to send a confirmation email to the primary guest
};
apiInstance.bookingsCreateBooking(appId, appKey, reservation, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **reservation** | [**Reservation**](Reservation.md)| Specifies the details of the booking to be created. | 
 **sendConfirmation** | **Boolean**| Whether to send a confirmation email to the primary guest | [optional] 

### Return type

[**ReservationConfirmation**](ReservationConfirmation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## bookingsGetBooking

> ReservationsResponse bookingsGetBooking(appId, appKey, confirmationId, opts)

Load all reservations for one booking by confirmation id.

A booking groups all reservations done in one single request and can be identified by the confirmation id.              Guests usually use the confirmation id to check in at the kiosk, on the website or mobile device. In hetras              all reservations of one booking share the room type, rate plan and number of guests per room.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let confirmationId = "confirmationId_example"; // String | The confirmation id for the booking to load.
let opts = {
  'expand': "expand_example", // String | Specifies the expand type.
  'exclude': "exclude_example" // String | Specifies the exclude type.
};
apiInstance.bookingsGetBooking(appId, appKey, confirmationId, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **confirmationId** | **String**| The confirmation id for the booking to load. | 
 **expand** | **String**| Specifies the expand type. | [optional] 
 **exclude** | **String**| Specifies the exclude type. | [optional] 

### Return type

[**ReservationsResponse**](ReservationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## bookingsGetBookings

> BookingListResponse bookingsGetBookings(appId, appKey, opts)

Find bookings matching the given filter criteria.

Here you can easily find bookings matching various criteria. The booking you are looking for has to fullfill all the specified criteria              at the same time. So if you specify a customer name and a channel code you will get all bookings where the firstname or lastname of a guest or a               contact contains the specified value and that have been done through the defined channel.              A booking can consist of multiple reservations, so even if you are looking for a specific reservation which is part of a multi-room booking you will get              all reservations for this booking returned.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let opts = {
  'hotelId': 56, // Number | Only return bookings for this specific hotel.
  'cancellationId': "cancellationId_example", // String | Return bookings for this cancellation id.
  'reservationNumber': 56, // Number | Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels.
  'customerName': "customerName_example", // String | Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
  'customerEmail': "customerEmail_example", // String | Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
  'customerId': "customerId_example", // String | Return all bookings the id of one of the guests or the contact matches the specified value.
  'roomNumber': "roomNumber_example", // String | Return all bookings having the specified room number assigned.
  'externalId': "externalId_example", // String | Return all bookings exactly matching the specified external id. This filter is case sensitive.
  'companyName': "companyName_example", // String | Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
  'companyId': "companyId_example", // String | Return all bookings the id of the company or travel agent profile matches the specified value.
  'companyEmail': "companyEmail_example", // String | Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
  'blockCode': "blockCode_example", // String | Return all bookings where the block code matches the specified value.
  'reservationStatuses': ["null"], // [String] | Return all bookings where the reservation status is one of the specified values.
  'marketCodes': ["null"], // [String] | Return all bookings where the market code is one of the specified values.
  'channelCodes': ["null"], // [String] | Return all bookings where the channel code is one of the specified values.
  'subChannelCodes': ["null"], // [String] | Return all bookings where the subchannel code is one of the specified values.
  'roomTypes': ["null"], // [String] | Return all bookings where the room type is one of the specified values.
  'ratePlanCodes': ["null"], // [String] | Return all bookings where the rate plan code is one of the specified values.
  'labels': ["null"], // [String] | Return all reservations with at least one of the specified labels.
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later.
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier.
  'dateFilter': "dateFilter_example", // String | Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range.
  'exclude': "exclude_example", // String | To be able to request reservations without personal data based on GDPR.
  'skip': 56, // Number | Amount of items to skip.
  'top': 56, // Number | Amount of items to select.
  'inlinecount': "inlinecount_example" // String | Return total number of items for a given filter criteria.
};
apiInstance.bookingsGetBookings(appId, appKey, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **hotelId** | **Number**| Only return bookings for this specific hotel. | [optional] 
 **cancellationId** | **String**| Return bookings for this cancellation id. | [optional] 
 **reservationNumber** | **Number**| Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels. | [optional] 
 **customerName** | **String**| Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
 **customerEmail** | **String**| Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
 **customerId** | **String**| Return all bookings the id of one of the guests or the contact matches the specified value. | [optional] 
 **roomNumber** | **String**| Return all bookings having the specified room number assigned. | [optional] 
 **externalId** | **String**| Return all bookings exactly matching the specified external id. This filter is case sensitive. | [optional] 
 **companyName** | **String**| Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
 **companyId** | **String**| Return all bookings the id of the company or travel agent profile matches the specified value. | [optional] 
 **companyEmail** | **String**| Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
 **blockCode** | **String**| Return all bookings where the block code matches the specified value. | [optional] 
 **reservationStatuses** | [**[String]**](String.md)| Return all bookings where the reservation status is one of the specified values. | [optional] 
 **marketCodes** | [**[String]**](String.md)| Return all bookings where the market code is one of the specified values. | [optional] 
 **channelCodes** | [**[String]**](String.md)| Return all bookings where the channel code is one of the specified values. | [optional] 
 **subChannelCodes** | [**[String]**](String.md)| Return all bookings where the subchannel code is one of the specified values. | [optional] 
 **roomTypes** | [**[String]**](String.md)| Return all bookings where the room type is one of the specified values. | [optional] 
 **ratePlanCodes** | [**[String]**](String.md)| Return all bookings where the rate plan code is one of the specified values. | [optional] 
 **labels** | [**[String]**](String.md)| Return all reservations with at least one of the specified labels. | [optional] 
 **from** | **Date**| Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later. | [optional] 
 **to** | **Date**| End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier. | [optional] 
 **dateFilter** | **String**| Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range. | [optional] 
 **exclude** | **String**| To be able to request reservations without personal data based on GDPR. | [optional] 
 **skip** | **Number**| Amount of items to skip. | [optional] 
 **top** | **Number**| Amount of items to select. | [optional] 
 **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] 

### Return type

[**BookingListResponse**](BookingListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## bookingsGetBookingsCount

> TotalCountResponse bookingsGetBookingsCount(appId, appKey, opts)

Get total count of bookings matchung the given filter criteria.

Get the count of all bookings matching your criteria. The bookings have to fullfill all the specified criteria              at the same time. So if you specify a customer name and a channel code you will get the count for all bookings where the firstname or lastname               of a guest or a contact contains the specified value and that have been done through the defined channel.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let opts = {
  'hotelId': 56, // Number | Only return bookings for this specific hotel.
  'cancellationId': "cancellationId_example", // String | Return bookings for this cancellation id.
  'reservationNumber': 56, // Number | Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels.
  'customerName': "customerName_example", // String | Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
  'customerEmail': "customerEmail_example", // String | Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
  'customerId': "customerId_example", // String | Return all bookings the id of one of the guests or the contact matches the specified value.
  'roomNumber': "roomNumber_example", // String | Return all bookings having the specified room number assigned.
  'externalId': "externalId_example", // String | Return all bookings exactly matching the specified external id. This filter is case sensitive.
  'companyName': "companyName_example", // String | Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
  'companyId': "companyId_example", // String | Return all bookings the id of the company or travel agent profile matches the specified value.
  'companyEmail': "companyEmail_example", // String | Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
  'blockCode': "blockCode_example", // String | Return all bookings where the block code matches the specified value.
  'reservationStatuses': ["null"], // [String] | Return all bookings where the reservation status is one of the specified values.
  'marketCodes': ["null"], // [String] | Return all bookings where the market code is one of the specified values.
  'channelCodes': ["null"], // [String] | Return all bookings where the channel code is one of the specified values.
  'subChannelCodes': ["null"], // [String] | Return all bookings where the subchannel code is one of the specified values.
  'roomTypes': ["null"], // [String] | Return all bookings where the room type is one of the specified values.
  'ratePlanCodes': ["null"], // [String] | Return all bookings where the rate plan code is one of the specified values.
  'labels': ["null"], // [String] | Return all reservations with at least one of the specified labels.
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later.
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier.
  'dateFilter': "dateFilter_example", // String | Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range.
  'exclude': "exclude_example" // String | To be able to request reservations without personal data based on GDPR.
};
apiInstance.bookingsGetBookingsCount(appId, appKey, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **hotelId** | **Number**| Only return bookings for this specific hotel. | [optional] 
 **cancellationId** | **String**| Return bookings for this cancellation id. | [optional] 
 **reservationNumber** | **Number**| Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels. | [optional] 
 **customerName** | **String**| Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
 **customerEmail** | **String**| Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
 **customerId** | **String**| Return all bookings the id of one of the guests or the contact matches the specified value. | [optional] 
 **roomNumber** | **String**| Return all bookings having the specified room number assigned. | [optional] 
 **externalId** | **String**| Return all bookings exactly matching the specified external id. This filter is case sensitive. | [optional] 
 **companyName** | **String**| Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
 **companyId** | **String**| Return all bookings the id of the company or travel agent profile matches the specified value. | [optional] 
 **companyEmail** | **String**| Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
 **blockCode** | **String**| Return all bookings where the block code matches the specified value. | [optional] 
 **reservationStatuses** | [**[String]**](String.md)| Return all bookings where the reservation status is one of the specified values. | [optional] 
 **marketCodes** | [**[String]**](String.md)| Return all bookings where the market code is one of the specified values. | [optional] 
 **channelCodes** | [**[String]**](String.md)| Return all bookings where the channel code is one of the specified values. | [optional] 
 **subChannelCodes** | [**[String]**](String.md)| Return all bookings where the subchannel code is one of the specified values. | [optional] 
 **roomTypes** | [**[String]**](String.md)| Return all bookings where the room type is one of the specified values. | [optional] 
 **ratePlanCodes** | [**[String]**](String.md)| Return all bookings where the rate plan code is one of the specified values. | [optional] 
 **labels** | [**[String]**](String.md)| Return all reservations with at least one of the specified labels. | [optional] 
 **from** | **Date**| Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later. | [optional] 
 **to** | **Date**| End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier. | [optional] 
 **dateFilter** | **String**| Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range. | [optional] 
 **exclude** | **String**| To be able to request reservations without personal data based on GDPR. | [optional] 

### Return type

[**TotalCountResponse**](TotalCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## bookingsGetReservation

> ReservationResponse bookingsGetReservation(appId, appKey, confirmationId, reservationNumber, opts)

Load a specific reservation from a booking.

With this request you can load one specific reservation done with one booking request.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
let reservationNumber = 56; // Number | Specifies the reservation number for the reservation to load.
let opts = {
  'expand': "expand_example", // String | Specifies the expand type.
  'exclude': "exclude_example" // String | Specifies the exclude type.
};
apiInstance.bookingsGetReservation(appId, appKey, confirmationId, reservationNumber, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | 
 **reservationNumber** | **Number**| Specifies the reservation number for the reservation to load. | 
 **expand** | **String**| Specifies the expand type. | [optional] 
 **exclude** | **String**| Specifies the exclude type. | [optional] 

### Return type

[**ReservationResponse**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## bookingsPatch

> Object bookingsPatch(appId, appKey, confirmationId, reservationNumber, patchRequest)

Partially updates a reservation.

The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call allows to update the following fields:              external_id, market_code, channel_code, subchannel_code, guarantee_type, comment, addon_services, labels, guests, contact and company.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/addon_services\&quot;, \&quot;value\&quot;: [\&quot;BREAKFAST\&quot;, \&quot;PARKING\&quot;]                },                {                  \&quot;op\&quot;: \&quot;add\&quot;, \&quot;path\&quot;: \&quot;/labels/-\&quot;, \&quot;value\&quot;: \&quot;MOBILE\&quot;                },                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/guests/SHOW-1234\&quot;, \&quot;value\&quot;: { \&quot;customer_id\&quot;: \&quot;SHOW-1234\&quot;, \&quot;primary\&quot;: false }                },                {                  \&quot;op\&quot;: \&quot;add\&quot;, \&quot;path\&quot;: \&quot;/guests/-\&quot;, \&quot;value\&quot;: { \&quot;customer_id\&quot;: \&quot;SHOW-5678\&quot;, \&quot;primary\&quot;: true }                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
let reservationNumber = 56; // Number | Specifies the reservation number for the reservation that has to be updated.
let patchRequest = [new HetrasBookingApiVersion0.OperationReservationPatchableModel()]; // [OperationReservationPatchableModel] | A set of JSON Patch operations
apiInstance.bookingsPatch(appId, appKey, confirmationId, reservationNumber, patchRequest, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | 
 **reservationNumber** | **Number**| Specifies the reservation number for the reservation that has to be updated. | 
 **patchRequest** | [**[OperationReservationPatchableModel]**](OperationReservationPatchableModel.md)| A set of JSON Patch operations | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## bookingsPaymentToken

> BaseResponse bookingsPaymentToken(appId, appKey, confirmationId, reservationNumber, authorizationRequest)

Post a payment token for a reservation.

TBD.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
let reservationNumber = 56; // Number | Specifies the reservation number for the reservation to be checked in.
let authorizationRequest = new HetrasBookingApiVersion0.AuthorizationRequest(); // AuthorizationRequest | 
apiInstance.bookingsPaymentToken(appId, appKey, confirmationId, reservationNumber, authorizationRequest, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | 
 **reservationNumber** | **Number**| Specifies the reservation number for the reservation to be checked in. | 
 **authorizationRequest** | [**AuthorizationRequest**](AuthorizationRequest.md)|  | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## bookingsPostRoomAssignment

> AssignRoomResponse bookingsPostRoomAssignment(appId, appKey, confirmationId, reservationNumber, opts)

Assign a room to a reservation.

By default this API call assigns a random room, which has the proper room type, is not already assigned              to another reservation or has any maintenance status set for the stay period of the underlying reservation. If the              arrival date for the underlying reservation is the current business day dirty rooms are excluded by default. For reservation              arriving on any latter day the room condition is not taken into account.&lt;br /&gt;              By specifiying the room selection criteria in the request body you can influence which room will be assigned. See the request model              for further details.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
let reservationNumber = 56; // Number | Specifies the reservation number for the reservation the room should be assigned to.
let opts = {
  'assigningCriteria': new HetrasBookingApiVersion0.AssignRoomCriteria() // AssignRoomCriteria | Specifies the criteria for the room selection.
};
apiInstance.bookingsPostRoomAssignment(appId, appKey, confirmationId, reservationNumber, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | 
 **reservationNumber** | **Number**| Specifies the reservation number for the reservation the room should be assigned to. | 
 **assigningCriteria** | [**AssignRoomCriteria**](AssignRoomCriteria.md)| Specifies the criteria for the room selection. | [optional] 

### Return type

[**AssignRoomResponse**](AssignRoomResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## bookingsTerminalAuthorization

> BaseResponse bookingsTerminalAuthorization(appId, appKey, confirmationId, reservationNumber, authorizationRequest)

Performs a chip and pin credit card authorization for a reservation.

With this call you can trigger a terminal authorization prompt for a reservation guest.               For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example

```javascript
import HetrasBookingApiVersion0 from 'hetras_booking_api_version_0';

let apiInstance = new HetrasBookingApiVersion0.BookingsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let confirmationId = "confirmationId_example"; // String | The confirmation id for the booking the reservation was made.
let reservationNumber = 56; // Number | Specifies the reservation number for the reservation to be checked in.
let authorizationRequest = new HetrasBookingApiVersion0.TerminalAuthorizationRequest(); // TerminalAuthorizationRequest | Specifies authorization details, such as amount and client identity.
apiInstance.bookingsTerminalAuthorization(appId, appKey, confirmationId, reservationNumber, authorizationRequest, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **confirmationId** | **String**| The confirmation id for the booking the reservation was made. | 
 **reservationNumber** | **Number**| Specifies the reservation number for the reservation to be checked in. | 
 **authorizationRequest** | [**TerminalAuthorizationRequest**](TerminalAuthorizationRequest.md)| Specifies authorization details, such as amount and client identity. | 

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

