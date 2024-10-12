# LicenseManagerApi.AppKeysApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createnewappkey**](AppKeysApi.md#createnewappkey) | **POST** /api/vlm/appkeys | Create new appkey
[**getappkeysfromaccount**](AppKeysApi.md#getappkeysfromaccount) | **GET** /api/vlm/appkeys | Get appKeys from account
[**updateappkey**](AppKeysApi.md#updateappkey) | **PUT** /api/vlm/appkeys/{id} | Update appkey



## createnewappkey

> CreatenewappkeyResponse createnewappkey(createnewappkeyRequest)

Create new appkey

Creates a new pair of &#x60;appKey&#x60; and &#x60;appToken&#x60;.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LicenseManagerApi.AppKeysApi();
let createnewappkeyRequest = {"label":"my new appkey"}; // CreatenewappkeyRequest | 
apiInstance.createnewappkey(createnewappkeyRequest, (error, data, response) => {
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
 **createnewappkeyRequest** | [**CreatenewappkeyRequest**](CreatenewappkeyRequest.md)|  | 

### Return type

[**CreatenewappkeyResponse**](CreatenewappkeyResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getappkeysfromaccount

> [Getappkeysfromaccount] getappkeysfromaccount(contentType)

Get appKeys from account

Gets all application keys from an account.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LicenseManagerApi.AppKeysApi();
let contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
apiInstance.getappkeysfromaccount(contentType, (error, data, response) => {
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
 **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | 

### Return type

[**[Getappkeysfromaccount]**](Getappkeysfromaccount.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateappkey

> updateappkey(id, updateappkeyRequest)

Update appkey

Activates or deactivates an &#x60;appKey&#x60; by its ID.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LicenseManagerApi.AppKeysApi();
let id = "id_example"; // String | ID from the appKey which will be updated
let updateappkeyRequest = {"isActive":false}; // UpdateappkeyRequest | Request body for updating AppKeys
apiInstance.updateappkey(id, updateappkeyRequest, (error, data, response) => {
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
 **id** | **String**| ID from the appKey which will be updated | 
 **updateappkeyRequest** | [**UpdateappkeyRequest**](UpdateappkeyRequest.md)| Request body for updating AppKeys | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

