# HetrasHotelApiVersion0.HotelsApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hotelsGetHotel**](HotelsApi.md#hotelsGetHotel) | **GET** /api/hotel/v0/hotels/{hotelId} | Get the details of the hotel with the speccified hotel id.
[**hotelsGetHotels**](HotelsApi.md#hotelsGetHotels) | **GET** /api/hotel/v0/hotels | Get a list of all the hotels of a chain your application has access to.



## hotelsGetHotel

> Hotel hotelsGetHotel(appId, appKey, hotelId)

Get the details of the hotel with the speccified hotel id.

Load the details about the specified hotel.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.HotelsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | 
apiInstance.hotelsGetHotel(appId, appKey, hotelId, (error, data, response) => {
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
 **hotelId** | **Number**|  | 

### Return type

[**Hotel**](Hotel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hotelsGetHotels

> [Hotel] hotelsGetHotels(appId, appKey)

Get a list of all the hotels of a chain your application has access to.

Load the details about all the hotels your application has access to.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.HotelsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
apiInstance.hotelsGetHotels(appId, appKey, (error, data, response) => {
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

### Return type

[**[Hotel]**](Hotel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

