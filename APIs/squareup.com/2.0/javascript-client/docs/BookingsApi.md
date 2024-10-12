# SquareConnectApi.BookingsApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelBooking**](BookingsApi.md#cancelBooking) | **POST** /v2/bookings/{booking_id}/cancel | CancelBooking
[**createBooking**](BookingsApi.md#createBooking) | **POST** /v2/bookings | CreateBooking
[**listTeamMemberBookingProfiles**](BookingsApi.md#listTeamMemberBookingProfiles) | **GET** /v2/bookings/team-member-booking-profiles | ListTeamMemberBookingProfiles
[**retrieveBooking**](BookingsApi.md#retrieveBooking) | **GET** /v2/bookings/{booking_id} | RetrieveBooking
[**retrieveBusinessBookingProfile**](BookingsApi.md#retrieveBusinessBookingProfile) | **GET** /v2/bookings/business-booking-profile | RetrieveBusinessBookingProfile
[**retrieveTeamMemberBookingProfile**](BookingsApi.md#retrieveTeamMemberBookingProfile) | **GET** /v2/bookings/team-member-booking-profiles/{team_member_id} | RetrieveTeamMemberBookingProfile
[**searchAvailability**](BookingsApi.md#searchAvailability) | **POST** /v2/bookings/availability/search | SearchAvailability
[**updateBooking**](BookingsApi.md#updateBooking) | **PUT** /v2/bookings/{booking_id} | UpdateBooking



## cancelBooking

> CancelBookingResponse cancelBooking(bookingId, cancelBookingRequest)

CancelBooking

Cancels an existing booking.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.BookingsApi();
let bookingId = "bookingId_example"; // String | The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-cancelled booking.
let cancelBookingRequest = new SquareConnectApi.CancelBookingRequest(); // CancelBookingRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.cancelBooking(bookingId, cancelBookingRequest, (error, data, response) => {
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
 **bookingId** | **String**| The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-cancelled booking. | 
 **cancelBookingRequest** | [**CancelBookingRequest**](CancelBookingRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CancelBookingResponse**](CancelBookingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBooking

> CreateBookingResponse createBooking(createBookingRequest)

CreateBooking

Creates a booking.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.BookingsApi();
let createBookingRequest = new SquareConnectApi.CreateBookingRequest(); // CreateBookingRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createBooking(createBookingRequest, (error, data, response) => {
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
 **createBookingRequest** | [**CreateBookingRequest**](CreateBookingRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateBookingResponse**](CreateBookingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTeamMemberBookingProfiles

> ListTeamMemberBookingProfilesResponse listTeamMemberBookingProfiles(opts)

ListTeamMemberBookingProfiles

Lists booking profiles for team members.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.BookingsApi();
let opts = {
  'bookableOnly': true, // Boolean | Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`).
  'limit': 56, // Number | The maximum number of results to return.
  'cursor': "cursor_example", // String | The cursor for paginating through the results.
  'locationId': "locationId_example" // String | Indicates whether to include only team members enabled at the given location in the returned result.
};
apiInstance.listTeamMemberBookingProfiles(opts, (error, data, response) => {
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
 **bookableOnly** | **Boolean**| Indicates whether to include only bookable team members in the returned result (&#x60;true&#x60;) or not (&#x60;false&#x60;). | [optional] 
 **limit** | **Number**| The maximum number of results to return. | [optional] 
 **cursor** | **String**| The cursor for paginating through the results. | [optional] 
 **locationId** | **String**| Indicates whether to include only team members enabled at the given location in the returned result. | [optional] 

### Return type

[**ListTeamMemberBookingProfilesResponse**](ListTeamMemberBookingProfilesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveBooking

> RetrieveBookingResponse retrieveBooking(bookingId)

RetrieveBooking

Retrieves a booking.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.BookingsApi();
let bookingId = "bookingId_example"; // String | The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-retrieved booking.
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
 **bookingId** | **String**| The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-retrieved booking. | 

### Return type

[**RetrieveBookingResponse**](RetrieveBookingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveBusinessBookingProfile

> RetrieveBusinessBookingProfileResponse retrieveBusinessBookingProfile()

RetrieveBusinessBookingProfile

Retrieves a seller&#39;s booking profile.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.BookingsApi();
apiInstance.retrieveBusinessBookingProfile((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**RetrieveBusinessBookingProfileResponse**](RetrieveBusinessBookingProfileResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveTeamMemberBookingProfile

> RetrieveTeamMemberBookingProfileResponse retrieveTeamMemberBookingProfile(teamMemberId)

RetrieveTeamMemberBookingProfile

Retrieves a team member&#39;s booking profile.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.BookingsApi();
let teamMemberId = "teamMemberId_example"; // String | The ID of the team member to retrieve.
apiInstance.retrieveTeamMemberBookingProfile(teamMemberId, (error, data, response) => {
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
 **teamMemberId** | **String**| The ID of the team member to retrieve. | 

### Return type

[**RetrieveTeamMemberBookingProfileResponse**](RetrieveTeamMemberBookingProfileResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchAvailability

> SearchAvailabilityResponse searchAvailability(searchAvailabilityRequest)

SearchAvailability

Searches for availabilities for booking.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.BookingsApi();
let searchAvailabilityRequest = new SquareConnectApi.SearchAvailabilityRequest(); // SearchAvailabilityRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchAvailability(searchAvailabilityRequest, (error, data, response) => {
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
 **searchAvailabilityRequest** | [**SearchAvailabilityRequest**](SearchAvailabilityRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchAvailabilityResponse**](SearchAvailabilityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBooking

> UpdateBookingResponse updateBooking(bookingId, updateBookingRequest)

UpdateBooking

Updates a booking.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.BookingsApi();
let bookingId = "bookingId_example"; // String | The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-updated booking.
let updateBookingRequest = new SquareConnectApi.UpdateBookingRequest(); // UpdateBookingRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateBooking(bookingId, updateBookingRequest, (error, data, response) => {
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
 **bookingId** | **String**| The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-updated booking. | 
 **updateBookingRequest** | [**UpdateBookingRequest**](UpdateBookingRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateBookingResponse**](UpdateBookingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

