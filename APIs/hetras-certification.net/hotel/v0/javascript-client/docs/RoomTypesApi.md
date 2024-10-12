# HetrasHotelApiVersion0.RoomTypesApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roomTypesGetRoomType**](RoomTypesApi.md#roomTypesGetRoomType) | **GET** /api/hotel/v0/hotels/{hotelId}/room_types/{code} | Get all the details for a specific room type in the hotel.
[**roomTypesGetRoomTypes**](RoomTypesApi.md#roomTypesGetRoomTypes) | **GET** /api/hotel/v0/hotels/{hotelId}/room_types | Get a list with the details of all room types for for the specified hotel id.



## roomTypesGetRoomType

> RoomType roomTypesGetRoomType(appId, appKey, hotelId, code)

Get all the details for a specific room type in the hotel.

With this call you can load the details about a specific room type in the hotel.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RoomTypesApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the room type belongs to.
let code = "code_example"; // String | The code of the room type you want to see details for.
apiInstance.roomTypesGetRoomType(appId, appKey, hotelId, code, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the room type belongs to. | 
 **code** | **String**| The code of the room type you want to see details for. | 

### Return type

[**RoomType**](RoomType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roomTypesGetRoomTypes

> [RoomType] roomTypesGetRoomTypes(appId, appKey, hotelId)

Get a list with the details of all room types for for the specified hotel id.

With this call you can load the details about a all available room types for the specified hotel.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RoomTypesApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the room type belongs to.
apiInstance.roomTypesGetRoomTypes(appId, appKey, hotelId, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the room type belongs to. | 

### Return type

[**[RoomType]**](RoomType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

