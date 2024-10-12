# Id4iApi.TransferApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSendInfo**](TransferApi.md#getSendInfo) | **GET** /api/v1/transfers/{id4n}/sendInfo | Show transfer preparation information
[**prepare**](TransferApi.md#prepare) | **PUT** /api/v1/transfers/{id4n}/sendInfo | Prepare an object for transfer
[**receive**](TransferApi.md#receive) | **PUT** /api/v1/transfers/{id4n}/receiveInfo | Transfer a GUID or collection, obtaining it (i.e. becoming the holder) and if allowed also taking ownership



## getSendInfo

> TransferSendInfo getSendInfo(id4n)

Show transfer preparation information

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.TransferApi();
let id4n = "id4n_example"; // String | The ID4N to retrieve information about
apiInstance.getSendInfo(id4n, (error, data, response) => {
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
 **id4n** | **String**| The ID4N to retrieve information about | 

### Return type

[**TransferSendInfo**](TransferSendInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## prepare

> Object prepare(id4n, transferSendInfo)

Prepare an object for transfer

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.TransferApi();
let id4n = "id4n_example"; // String | The ID4N to prepare for transfer
let transferSendInfo = new Id4iApi.TransferSendInfo(); // TransferSendInfo | Transfer preparation status
apiInstance.prepare(id4n, transferSendInfo, (error, data, response) => {
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
 **id4n** | **String**| The ID4N to prepare for transfer | 
 **transferSendInfo** | [**TransferSendInfo**](TransferSendInfo.md)| Transfer preparation status | 

### Return type

**Object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## receive

> receive(id4n, transferReceiveInfo)

Transfer a GUID or collection, obtaining it (i.e. becoming the holder) and if allowed also taking ownership

Taking ownership can be forbidden by a previous owner. See methods prepare and getInfo

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.TransferApi();
let id4n = "id4n_example"; // String | This ID4N identifies the object to take hold of
let transferReceiveInfo = new Id4iApi.TransferReceiveInfo(); // TransferReceiveInfo | Required information to receive an id4n object
apiInstance.receive(id4n, transferReceiveInfo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id4n** | **String**| This ID4N identifies the object to take hold of | 
 **transferReceiveInfo** | [**TransferReceiveInfo**](TransferReceiveInfo.md)| Required information to receive an id4n object | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

