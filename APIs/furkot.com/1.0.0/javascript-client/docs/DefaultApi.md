# FurkotTrips.DefaultApi

All URIs are relative to *https://trips.furkot.com/pub/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tripGet**](DefaultApi.md#tripGet) | **GET** /trip | 
[**tripTripIdStopGet**](DefaultApi.md#tripTripIdStopGet) | **GET** /trip/{trip_id}/stop | 



## tripGet

> [Trip] tripGet()



list user&#39;s trips

### Example

```javascript
import FurkotTrips from 'furkot_trips';
let defaultClient = FurkotTrips.ApiClient.instance;
// Configure OAuth2 access token for authorization: furkot_auth_access_code
let furkot_auth_access_code = defaultClient.authentications['furkot_auth_access_code'];
furkot_auth_access_code.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: furkot_auth_implicit
let furkot_auth_implicit = defaultClient.authentications['furkot_auth_implicit'];
furkot_auth_implicit.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FurkotTrips.DefaultApi();
apiInstance.tripGet((error, data, response) => {
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

[**[Trip]**](Trip.md)

### Authorization

[furkot_auth_access_code](../README.md#furkot_auth_access_code), [furkot_auth_implicit](../README.md#furkot_auth_implicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tripTripIdStopGet

> [Step] tripTripIdStopGet(tripId)



list stops for a trip identified by {trip_id}

### Example

```javascript
import FurkotTrips from 'furkot_trips';
let defaultClient = FurkotTrips.ApiClient.instance;
// Configure OAuth2 access token for authorization: furkot_auth_access_code
let furkot_auth_access_code = defaultClient.authentications['furkot_auth_access_code'];
furkot_auth_access_code.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: furkot_auth_implicit
let furkot_auth_implicit = defaultClient.authentications['furkot_auth_implicit'];
furkot_auth_implicit.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FurkotTrips.DefaultApi();
let tripId = "tripId_example"; // String | id of the trip
apiInstance.tripTripIdStopGet(tripId, (error, data, response) => {
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
 **tripId** | **String**| id of the trip | 

### Return type

[**[Step]**](Step.md)

### Authorization

[furkot_auth_access_code](../README.md#furkot_auth_access_code), [furkot_auth_implicit](../README.md#furkot_auth_implicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

