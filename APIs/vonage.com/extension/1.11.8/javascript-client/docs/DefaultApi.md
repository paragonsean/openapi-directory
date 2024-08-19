# ExtensionApi.DefaultApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/provisioning*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extensionCtrlGetAccountExtensionByID**](DefaultApi.md#extensionCtrlGetAccountExtensionByID) | **GET** /api/accounts/{account_id}/extensions/{extension_number} | Get extension data by account ID and extension number
[**extensionCtrlGetAccountExtensions**](DefaultApi.md#extensionCtrlGetAccountExtensions) | **GET** /api/accounts/{account_id}/extensions | Get account extensions data by account ID



## extensionCtrlGetAccountExtensionByID

> EndUserRouteHalResponse extensionCtrlGetAccountExtensionByID(accountId, extensionNumber)

Get extension data by account ID and extension number

### Example

```javascript
import ExtensionApi from 'extension_api';
let defaultClient = ExtensionApi.ApiClient.instance;
// Configure Bearer (OAuth) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ExtensionApi.DefaultApi();
let accountId = "accountId_example"; // String | The Vonage Business Cloud account ID
let extensionNumber = 789; // Number | The extension number
apiInstance.extensionCtrlGetAccountExtensionByID(accountId, extensionNumber, (error, data, response) => {
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
 **accountId** | **String**| The Vonage Business Cloud account ID | 
 **extensionNumber** | **Number**| The extension number | 

### Return type

[**EndUserRouteHalResponse**](EndUserRouteHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extensionCtrlGetAccountExtensions

> EndUserRouteHalResponse extensionCtrlGetAccountExtensions(accountId, opts)

Get account extensions data by account ID

### Example

```javascript
import ExtensionApi from 'extension_api';
let defaultClient = ExtensionApi.ApiClient.instance;
// Configure Bearer (OAuth) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ExtensionApi.DefaultApi();
let accountId = "accountId_example"; // String | The Vonage Business Cloud account ID
let opts = {
  'pageSize': 10, // Number | Number of records per page
  'page': 10, // Number | Current page number
  'locationId': 145214, // Number | Filter by location id
  'phoneNumber': "14155550100", // String | Filter by phone number
  'loginName': "jsmith", // String | Filter by login name
  'email': "john.smith@example.com" // String | Filter by email address
};
apiInstance.extensionCtrlGetAccountExtensions(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| The Vonage Business Cloud account ID | 
 **pageSize** | **Number**| Number of records per page | [optional] 
 **page** | **Number**| Current page number | [optional] 
 **locationId** | **Number**| Filter by location id | [optional] 
 **phoneNumber** | **String**| Filter by phone number | [optional] 
 **loginName** | **String**| Filter by login name | [optional] 
 **email** | **String**| Filter by email address | [optional] 

### Return type

[**EndUserRouteHalResponse**](EndUserRouteHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

