# TwilioNumbers.NumbersV2ReplaceItemsApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createReplaceItems**](NumbersV2ReplaceItemsApi.md#createReplaceItems) | **POST** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ReplaceItems | 



## createReplaceItems

> NumbersV2RegulatoryComplianceBundleReplaceItems createReplaceItems(bundleSid, fromBundleSid)



Replaces all bundle items in the target bundle (specified in the path) with all the bundle items of the source bundle (specified by the from_bundle_sid body param)

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2ReplaceItemsApi();
let bundleSid = "bundleSid_example"; // String | The unique string that identifies the Bundle where the item assignments are going to be replaced.
let fromBundleSid = "fromBundleSid_example"; // String | The source bundle sid to copy the item assignments from.
apiInstance.createReplaceItems(bundleSid, fromBundleSid, (error, data, response) => {
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
 **bundleSid** | **String**| The unique string that identifies the Bundle where the item assignments are going to be replaced. | 
 **fromBundleSid** | **String**| The source bundle sid to copy the item assignments from. | 

### Return type

[**NumbersV2RegulatoryComplianceBundleReplaceItems**](NumbersV2RegulatoryComplianceBundleReplaceItems.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

