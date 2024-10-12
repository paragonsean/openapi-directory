# SquareConnectApi.CashDrawersApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listCashDrawerShiftEvents**](CashDrawersApi.md#listCashDrawerShiftEvents) | **GET** /v2/cash-drawers/shifts/{shift_id}/events | ListCashDrawerShiftEvents
[**listCashDrawerShifts**](CashDrawersApi.md#listCashDrawerShifts) | **GET** /v2/cash-drawers/shifts | ListCashDrawerShifts
[**retrieveCashDrawerShift**](CashDrawersApi.md#retrieveCashDrawerShift) | **GET** /v2/cash-drawers/shifts/{shift_id} | RetrieveCashDrawerShift



## listCashDrawerShiftEvents

> ListCashDrawerShiftEventsResponse listCashDrawerShiftEvents(locationId, shiftId, opts)

ListCashDrawerShiftEvents

Provides a paginated list of events for a single cash drawer shift.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CashDrawersApi();
let locationId = "locationId_example"; // String | The ID of the location to list cash drawer shifts for.
let shiftId = "shiftId_example"; // String | The shift ID.
let opts = {
  'limit': 56, // Number | Number of resources to be returned in a page of results (200 by default, 1000 max).
  'cursor': "cursor_example" // String | Opaque cursor for fetching the next page of results.
};
apiInstance.listCashDrawerShiftEvents(locationId, shiftId, opts, (error, data, response) => {
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
 **locationId** | **String**| The ID of the location to list cash drawer shifts for. | 
 **shiftId** | **String**| The shift ID. | 
 **limit** | **Number**| Number of resources to be returned in a page of results (200 by default, 1000 max). | [optional] 
 **cursor** | **String**| Opaque cursor for fetching the next page of results. | [optional] 

### Return type

[**ListCashDrawerShiftEventsResponse**](ListCashDrawerShiftEventsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCashDrawerShifts

> ListCashDrawerShiftsResponse listCashDrawerShifts(locationId, opts)

ListCashDrawerShifts

Provides the details for all of the cash drawer shifts for a location in a date range.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CashDrawersApi();
let locationId = "locationId_example"; // String | The ID of the location to query for a list of cash drawer shifts.
let opts = {
  'sortOrder': "sortOrder_example", // String | The order in which cash drawer shifts are listed in the response, based on their opened_at field. Default value: ASC
  'beginTime': "beginTime_example", // String | The inclusive start time of the query on opened_at, in ISO 8601 format.
  'endTime': "endTime_example", // String | The exclusive end date of the query on opened_at, in ISO 8601 format.
  'limit': 56, // Number | Number of cash drawer shift events in a page of results (200 by default, 1000 max).
  'cursor': "cursor_example" // String | Opaque cursor for fetching the next page of results.
};
apiInstance.listCashDrawerShifts(locationId, opts, (error, data, response) => {
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
 **locationId** | **String**| The ID of the location to query for a list of cash drawer shifts. | 
 **sortOrder** | **String**| The order in which cash drawer shifts are listed in the response, based on their opened_at field. Default value: ASC | [optional] 
 **beginTime** | **String**| The inclusive start time of the query on opened_at, in ISO 8601 format. | [optional] 
 **endTime** | **String**| The exclusive end date of the query on opened_at, in ISO 8601 format. | [optional] 
 **limit** | **Number**| Number of cash drawer shift events in a page of results (200 by default, 1000 max). | [optional] 
 **cursor** | **String**| Opaque cursor for fetching the next page of results. | [optional] 

### Return type

[**ListCashDrawerShiftsResponse**](ListCashDrawerShiftsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveCashDrawerShift

> RetrieveCashDrawerShiftResponse retrieveCashDrawerShift(locationId, shiftId)

RetrieveCashDrawerShift

Provides the summary details for a single cash drawer shift. See [ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2021-08-18/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CashDrawersApi();
let locationId = "locationId_example"; // String | The ID of the location to retrieve cash drawer shifts from.
let shiftId = "shiftId_example"; // String | The shift ID.
apiInstance.retrieveCashDrawerShift(locationId, shiftId, (error, data, response) => {
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
 **locationId** | **String**| The ID of the location to retrieve cash drawer shifts from. | 
 **shiftId** | **String**| The shift ID. | 

### Return type

[**RetrieveCashDrawerShiftResponse**](RetrieveCashDrawerShiftResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

