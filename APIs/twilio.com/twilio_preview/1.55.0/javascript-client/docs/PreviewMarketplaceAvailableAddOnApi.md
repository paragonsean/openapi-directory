# TwilioPreview.PreviewMarketplaceAvailableAddOnApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchMarketplaceAvailableAddOn**](PreviewMarketplaceAvailableAddOnApi.md#fetchMarketplaceAvailableAddOn) | **GET** /marketplace/AvailableAddOns/{Sid} | 
[**listMarketplaceAvailableAddOn**](PreviewMarketplaceAvailableAddOnApi.md#listMarketplaceAvailableAddOn) | **GET** /marketplace/AvailableAddOns | 



## fetchMarketplaceAvailableAddOn

> PreviewMarketplaceAvailableAddOn fetchMarketplaceAvailableAddOn(sid)



Fetch an instance of an Add-on currently available to be installed.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceAvailableAddOnApi();
let sid = "sid_example"; // String | The SID of the AvailableAddOn resource to fetch.
apiInstance.fetchMarketplaceAvailableAddOn(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the AvailableAddOn resource to fetch. | 

### Return type

[**PreviewMarketplaceAvailableAddOn**](PreviewMarketplaceAvailableAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMarketplaceAvailableAddOn

> ListMarketplaceAvailableAddOnResponse listMarketplaceAvailableAddOn(opts)



Retrieve a list of Add-ons currently available to be installed.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewMarketplaceAvailableAddOnApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMarketplaceAvailableAddOn(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMarketplaceAvailableAddOnResponse**](ListMarketplaceAvailableAddOnResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

