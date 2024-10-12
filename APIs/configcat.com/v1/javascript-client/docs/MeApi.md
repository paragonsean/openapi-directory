# ConfigCatPublicManagementApi.MeApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMe**](MeApi.md#getMe) | **GET** /v1/me | Get authenticated user details



## getMe

> MeModel getMe()

Get authenticated user details



### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.MeApi();
apiInstance.getMe((error, data, response) => {
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

[**MeModel**](MeModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json

