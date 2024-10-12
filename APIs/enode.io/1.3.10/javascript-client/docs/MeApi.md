# EnodeApi.MeApi

All URIs are relative to *https://api.test.enode.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disconnectVendor**](MeApi.md#disconnectVendor) | **DELETE** /me/vendors/{vendor} | Disconnect Vendor
[**getMe**](MeApi.md#getMe) | **GET** /me | Get My User



## disconnectVendor

> disconnectVendor(vendor)

Disconnect Vendor

Disconnect a single Vendor from the User&#39;s account.  All stored data about their Vendor account will be deleted, and any vehicles that were provided by that Vendor will disappear from the system.

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.MeApi();
let vendor = "TESLA"; // String | Vendor to be unlinked
apiInstance.disconnectVendor(vendor, (error, data, response) => {
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
 **vendor** | **String**| Vendor to be unlinked | 

### Return type

null (empty response body)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMe

> GetMe200Response getMe()

Get My User

Returns metadata about the authenticated User, including a list of vendors for which the user has provided credentials.

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.MeApi();
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

[**GetMe200Response**](GetMe200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

