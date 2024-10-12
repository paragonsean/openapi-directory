# TwilioPreview.PreviewMarketplaceInstalledAddOnExtensionApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchMarketplaceInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnExtensionApi.md#fetchMarketplaceInstalledAddOnExtension) | **GET** /marketplace/InstalledAddOns/{InstalledAddOnSid}/Extensions/{Sid} | 
[**listMarketplaceInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnExtensionApi.md#listMarketplaceInstalledAddOnExtension) | **GET** /marketplace/InstalledAddOns/{InstalledAddOnSid}/Extensions | 
[**updateMarketplaceInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnExtensionApi.md#updateMarketplaceInstalledAddOnExtension) | **POST** /marketplace/InstalledAddOns/{InstalledAddOnSid}/Extensions/{Sid} | 



## fetchMarketplaceInstalledAddOnExtension

> PreviewMarketplaceInstalledAddOnInstalledAddOnExtension fetchMarketplaceInstalledAddOnExtension(installedAddOnSid, sid)



Fetch an instance of an Extension for the Installed Add-on.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceInstalledAddOnExtensionApi();
let installedAddOnSid = "installedAddOnSid_example"; // String | The SID of the InstalledAddOn resource with the extension to fetch.
let sid = "sid_example"; // String | The SID of the InstalledAddOn Extension resource to fetch.
apiInstance.fetchMarketplaceInstalledAddOnExtension(installedAddOnSid, sid, (error, data, response) => {
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
 **installedAddOnSid** | **String**| The SID of the InstalledAddOn resource with the extension to fetch. | 
 **sid** | **String**| The SID of the InstalledAddOn Extension resource to fetch. | 

### Return type

[**PreviewMarketplaceInstalledAddOnInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnInstalledAddOnExtension.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMarketplaceInstalledAddOnExtension

> ListMarketplaceInstalledAddOnExtensionResponse listMarketplaceInstalledAddOnExtension(installedAddOnSid, opts)



Retrieve a list of Extensions for the Installed Add-on.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceInstalledAddOnExtensionApi();
let installedAddOnSid = "installedAddOnSid_example"; // String | The SID of the InstalledAddOn resource with the extensions to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMarketplaceInstalledAddOnExtension(installedAddOnSid, opts, (error, data, response) => {
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
 **installedAddOnSid** | **String**| The SID of the InstalledAddOn resource with the extensions to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMarketplaceInstalledAddOnExtensionResponse**](ListMarketplaceInstalledAddOnExtensionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMarketplaceInstalledAddOnExtension

> PreviewMarketplaceInstalledAddOnInstalledAddOnExtension updateMarketplaceInstalledAddOnExtension(installedAddOnSid, sid, enabled)



Update an Extension for an Add-on installation.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceInstalledAddOnExtensionApi();
let installedAddOnSid = "installedAddOnSid_example"; // String | The SID of the InstalledAddOn resource with the extension to update.
let sid = "sid_example"; // String | The SID of the InstalledAddOn Extension resource to update.
let enabled = true; // Boolean | Whether the Extension should be invoked.
apiInstance.updateMarketplaceInstalledAddOnExtension(installedAddOnSid, sid, enabled, (error, data, response) => {
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
 **installedAddOnSid** | **String**| The SID of the InstalledAddOn resource with the extension to update. | 
 **sid** | **String**| The SID of the InstalledAddOn Extension resource to update. | 
 **enabled** | **Boolean**| Whether the Extension should be invoked. | 

### Return type

[**PreviewMarketplaceInstalledAddOnInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnInstalledAddOnExtension.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

