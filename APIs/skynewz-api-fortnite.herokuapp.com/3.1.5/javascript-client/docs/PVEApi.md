# FortniteRestApi.PVEApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pveInfoGet**](PVEApi.md#pveInfoGet) | **GET** /pve/info | Get Fortnite PVE Info (storm, etc)
[**pveUserUsernameGet**](PVEApi.md#pveUserUsernameGet) | **GET** /pve/user/{username} | Get PVE Stat by given username



## pveInfoGet

> Object pveInfoGet()

Get Fortnite PVE Info (storm, etc)

### Example

```javascript
import FortniteRestApi from 'fortnite_rest_api';
let defaultClient = FortniteRestApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FortniteRestApi.PVEApi();
apiInstance.pveInfoGet((error, data, response) => {
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

**Object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pveUserUsernameGet

> Object pveUserUsernameGet(username)

Get PVE Stat by given username

### Example

```javascript
import FortniteRestApi from 'fortnite_rest_api';
let defaultClient = FortniteRestApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FortniteRestApi.PVEApi();
let username = "username_example"; // String | Fortnite username
apiInstance.pveUserUsernameGet(username, (error, data, response) => {
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
 **username** | **String**| Fortnite username | 

### Return type

**Object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

