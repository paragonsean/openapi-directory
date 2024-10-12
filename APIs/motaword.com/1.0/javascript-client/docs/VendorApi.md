# MotaWordApi.VendorApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAvailableVendors**](VendorApi.md#getAvailableVendors) | **POST** /users/available-vendors | Get a list of vendors available for the criteria given



## getAvailableVendors

> UserList getAvailableVendors(opts)

Get a list of vendors available for the criteria given

Get a list of vendors available for the criteria given

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.VendorApi();
let opts = {
  '_with': ["null"], // [String] | Include detailed information. Possible values 'user'. Requesting user info enrichment takes much longer.
  'availableVendorsFilter': new MotaWordApi.AvailableVendorsFilter() // AvailableVendorsFilter | 
};
apiInstance.getAvailableVendors(opts, (error, data, response) => {
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
 **_with** | [**[String]**](String.md)| Include detailed information. Possible values &#39;user&#39;. Requesting user info enrichment takes much longer. | [optional] 
 **availableVendorsFilter** | [**AvailableVendorsFilter**](AvailableVendorsFilter.md)|  | [optional] 

### Return type

[**UserList**](UserList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

