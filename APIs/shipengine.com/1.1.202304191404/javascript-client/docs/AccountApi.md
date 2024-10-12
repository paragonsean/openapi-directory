# ShipEngineApi.AccountApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAccountImage**](AccountApi.md#createAccountImage) | **POST** /v1/account/settings/images | Create an Account Image
[**deleteAccountImageById**](AccountApi.md#deleteAccountImageById) | **DELETE** /v1/account/settings/images/{label_image_id} | Delete Account Image By Id
[**getAccountSettingsImagesById**](AccountApi.md#getAccountSettingsImagesById) | **GET** /v1/account/settings/images/{label_image_id} | Get Account Image By ID
[**listAccountImages**](AccountApi.md#listAccountImages) | **GET** /v1/account/settings/images | List Account Images
[**listAccountSettings**](AccountApi.md#listAccountSettings) | **GET** /v1/account/settings | List Account Settings
[**updateAccountSettingsImagesById**](AccountApi.md#updateAccountSettingsImagesById) | **PUT** /v1/account/settings/images/{label_image_id} | Update Account Image By ID



## createAccountImage

> GetAccountSettingsImagesResponseBody createAccountImage(createAccountSettingsImageRequestBody)

Create an Account Image

Create an Account Image

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.AccountApi();
let createAccountSettingsImageRequestBody = new ShipEngineApi.CreateAccountSettingsImageRequestBody(); // CreateAccountSettingsImageRequestBody | 
apiInstance.createAccountImage(createAccountSettingsImageRequestBody, (error, data, response) => {
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
 **createAccountSettingsImageRequestBody** | [**CreateAccountSettingsImageRequestBody**](CreateAccountSettingsImageRequestBody.md)|  | 

### Return type

[**GetAccountSettingsImagesResponseBody**](GetAccountSettingsImagesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccountImageById

> String deleteAccountImageById(labelImageId)

Delete Account Image By Id

Delete Account Image By Id

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.AccountApi();
let labelImageId = "labelImageId_example"; // String | Label Image Id
apiInstance.deleteAccountImageById(labelImageId, (error, data, response) => {
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
 **labelImageId** | **String**| Label Image Id | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## getAccountSettingsImagesById

> GetAccountSettingsImagesResponseBody getAccountSettingsImagesById(labelImageId)

Get Account Image By ID

Retrieve information for an account image.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.AccountApi();
let labelImageId = "labelImageId_example"; // String | Label Image Id
apiInstance.getAccountSettingsImagesById(labelImageId, (error, data, response) => {
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
 **labelImageId** | **String**| Label Image Id | 

### Return type

[**GetAccountSettingsImagesResponseBody**](GetAccountSettingsImagesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccountImages

> ListAccountSettingsImagesResponseBody listAccountImages()

List Account Images

List all account images for the ShipEngine account

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.AccountApi();
apiInstance.listAccountImages((error, data, response) => {
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

[**ListAccountSettingsImagesResponseBody**](ListAccountSettingsImagesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccountSettings

> GetAccountSettingsResponseBody listAccountSettings()

List Account Settings

List all account settings for the ShipEngine account

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.AccountApi();
apiInstance.listAccountSettings((error, data, response) => {
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

[**GetAccountSettingsResponseBody**](GetAccountSettingsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccountSettingsImagesById

> String updateAccountSettingsImagesById(labelImageId, updateAccountSettingsImageRequestBody)

Update Account Image By ID

Update information for an account image.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.AccountApi();
let labelImageId = "labelImageId_example"; // String | Label Image Id
let updateAccountSettingsImageRequestBody = new ShipEngineApi.UpdateAccountSettingsImageRequestBody(); // UpdateAccountSettingsImageRequestBody | 
apiInstance.updateAccountSettingsImagesById(labelImageId, updateAccountSettingsImageRequestBody, (error, data, response) => {
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
 **labelImageId** | **String**| Label Image Id | 
 **updateAccountSettingsImageRequestBody** | [**UpdateAccountSettingsImageRequestBody**](UpdateAccountSettingsImageRequestBody.md)|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain

