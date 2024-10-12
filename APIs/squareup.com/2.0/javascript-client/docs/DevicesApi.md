# SquareConnectApi.DevicesApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeviceCode**](DevicesApi.md#createDeviceCode) | **POST** /v2/devices/codes | CreateDeviceCode
[**getDeviceCode**](DevicesApi.md#getDeviceCode) | **GET** /v2/devices/codes/{id} | GetDeviceCode
[**listDeviceCodes**](DevicesApi.md#listDeviceCodes) | **GET** /v2/devices/codes | ListDeviceCodes



## createDeviceCode

> CreateDeviceCodeResponse createDeviceCode(createDeviceCodeRequest)

CreateDeviceCode

Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected terminal mode.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DevicesApi();
let createDeviceCodeRequest = new SquareConnectApi.CreateDeviceCodeRequest(); // CreateDeviceCodeRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createDeviceCode(createDeviceCodeRequest, (error, data, response) => {
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
 **createDeviceCodeRequest** | [**CreateDeviceCodeRequest**](CreateDeviceCodeRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateDeviceCodeResponse**](CreateDeviceCodeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDeviceCode

> GetDeviceCodeResponse getDeviceCode(id)

GetDeviceCode

Retrieves DeviceCode with the associated ID.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DevicesApi();
let id = "id_example"; // String | The unique identifier for the device code.
apiInstance.getDeviceCode(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the device code. | 

### Return type

[**GetDeviceCodeResponse**](GetDeviceCodeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeviceCodes

> ListDeviceCodesResponse listDeviceCodes(opts)

ListDeviceCodes

Lists all DeviceCodes associated with the merchant.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DevicesApi();
let opts = {
  'cursor': "cursor_example", // String | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
  'locationId': "locationId_example", // String | If specified, only returns DeviceCodes of the specified location. Returns DeviceCodes of all locations if empty.
  'productType': "productType_example", // String | If specified, only returns DeviceCodes targeting the specified product type. Returns DeviceCodes of all product types if empty.
  'status': "status_example" // String | If specified, returns DeviceCodes with the specified statuses. Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.
};
apiInstance.listDeviceCodes(opts, (error, data, response) => {
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
 **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information. | [optional] 
 **locationId** | **String**| If specified, only returns DeviceCodes of the specified location. Returns DeviceCodes of all locations if empty. | [optional] 
 **productType** | **String**| If specified, only returns DeviceCodes targeting the specified product type. Returns DeviceCodes of all product types if empty. | [optional] 
 **status** | **String**| If specified, returns DeviceCodes with the specified statuses. Returns DeviceCodes of status &#x60;PAIRED&#x60; and &#x60;UNPAIRED&#x60; if empty. | [optional] 

### Return type

[**ListDeviceCodesResponse**](ListDeviceCodesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

