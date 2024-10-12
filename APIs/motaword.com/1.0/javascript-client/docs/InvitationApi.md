# MotaWordApi.InvitationApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInvitationVendors**](InvitationApi.md#getInvitationVendors) | **POST** /invitation/vendors | Get vendor list for compiled invitation needs



## getInvitationVendors

> VendorInvitationList getInvitationVendors(opts)

Get vendor list for compiled invitation needs

Get vendor list for compiled invitation needs

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

let apiInstance = new MotaWordApi.InvitationApi();
let opts = {
  'fileNeedsVendor': [new MotaWordApi.FileNeedsVendor()] // [FileNeedsVendor] | 
};
apiInstance.getInvitationVendors(opts, (error, data, response) => {
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
 **fileNeedsVendor** | [**[FileNeedsVendor]**](FileNeedsVendor.md)|  | [optional] 

### Return type

[**VendorInvitationList**](VendorInvitationList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

