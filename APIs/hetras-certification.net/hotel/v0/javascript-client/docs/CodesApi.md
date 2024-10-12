# HetrasHotelApiVersion0.CodesApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codesGetCode**](CodesApi.md#codesGetCode) | **GET** /api/hotel/v0/hotels/{hotelId}/codes/{id} | Get all the details for a specific code available for the hotel.
[**codesGetCodes**](CodesApi.md#codesGetCodes) | **GET** /api/hotel/v0/hotels/{hotelId}/codes | Get a list of codes for the specified hotel either filtered by type or code.



## codesGetCode

> CodeFullEntry codesGetCode(appId, appKey, hotelId, id)

Get all the details for a specific code available for the hotel.

Read the details about a specific code available for the defined hotel.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.CodesApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the code available for.
let id = "id_example"; // String | The code identifier you want to see details for.
apiInstance.codesGetCode(appId, appKey, hotelId, id, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id the code available for. | 
 **id** | **String**| The code identifier you want to see details for. | 

### Return type

[**CodeFullEntry**](CodeFullEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## codesGetCodes

> CodesListResponse codesGetCodes(appId, appKey, hotelId, opts)

Get a list of codes for the specified hotel either filtered by type or code.

With this call you can find codes for a hotel by type or code. By default and without any filter criteria              defined it will return you all available codes.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.CodesApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id you are trying to find codes for.
let opts = {
  'code': "code_example", // String | Return all results matching the specified code. A code is unique in combination with the type              which means when you query for a code you could get multiple results each for a different type
  'type': "type_example" // String | Return all codes for the specified type
};
apiInstance.codesGetCodes(appId, appKey, hotelId, opts, (error, data, response) => {
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
 **hotelId** | **Number**| The hotel id you are trying to find codes for. | 
 **code** | **String**| Return all results matching the specified code. A code is unique in combination with the type              which means when you query for a code you could get multiple results each for a different type | [optional] 
 **type** | **String**| Return all codes for the specified type | [optional] 

### Return type

[**CodesListResponse**](CodesListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

