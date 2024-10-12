# TwilioPreview.PreviewMarketplaceAvailableAddOnExtensionApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchMarketplaceAvailableAddOnExtension**](PreviewMarketplaceAvailableAddOnExtensionApi.md#fetchMarketplaceAvailableAddOnExtension) | **GET** /marketplace/AvailableAddOns/{AvailableAddOnSid}/Extensions/{Sid} | 
[**listMarketplaceAvailableAddOnExtension**](PreviewMarketplaceAvailableAddOnExtensionApi.md#listMarketplaceAvailableAddOnExtension) | **GET** /marketplace/AvailableAddOns/{AvailableAddOnSid}/Extensions | 



## fetchMarketplaceAvailableAddOnExtension

> PreviewMarketplaceAvailableAddOnAvailableAddOnExtension fetchMarketplaceAvailableAddOnExtension(availableAddOnSid, sid)



Fetch an instance of an Extension for the Available Add-on.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceAvailableAddOnExtensionApi();
let availableAddOnSid = "availableAddOnSid_example"; // String | The SID of the AvailableAddOn resource with the extension to fetch.
let sid = "sid_example"; // String | The SID of the AvailableAddOn Extension resource to fetch.
apiInstance.fetchMarketplaceAvailableAddOnExtension(availableAddOnSid, sid, (error, data, response) => {
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
 **availableAddOnSid** | **String**| The SID of the AvailableAddOn resource with the extension to fetch. | 
 **sid** | **String**| The SID of the AvailableAddOn Extension resource to fetch. | 

### Return type

[**PreviewMarketplaceAvailableAddOnAvailableAddOnExtension**](PreviewMarketplaceAvailableAddOnAvailableAddOnExtension.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMarketplaceAvailableAddOnExtension

> ListMarketplaceAvailableAddOnExtensionResponse listMarketplaceAvailableAddOnExtension(availableAddOnSid, opts)



Retrieve a list of Extensions for the Available Add-on.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceAvailableAddOnExtensionApi();
let availableAddOnSid = "availableAddOnSid_example"; // String | The SID of the AvailableAddOn resource with the extensions to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMarketplaceAvailableAddOnExtension(availableAddOnSid, opts, (error, data, response) => {
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
 **availableAddOnSid** | **String**| The SID of the AvailableAddOn resource with the extensions to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMarketplaceAvailableAddOnExtensionResponse**](ListMarketplaceAvailableAddOnExtensionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

