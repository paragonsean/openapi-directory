# TwilioPreview.PreviewWirelessUsageApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchWirelessUsage**](PreviewWirelessUsageApi.md#fetchWirelessUsage) | **GET** /wireless/Sims/{SimSid}/Usage | 



## fetchWirelessUsage

> PreviewWirelessSimUsage fetchWirelessUsage(simSid, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessUsageApi();
let simSid = "simSid_example"; // String | 
let opts = {
  'end': "end_example", // String | 
  'start': "start_example" // String | 
};
apiInstance.fetchWirelessUsage(simSid, opts, (error, data, response) => {
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
 **simSid** | **String**|  | 
 **end** | **String**|  | [optional] 
 **start** | **String**|  | [optional] 

### Return type

[**PreviewWirelessSimUsage**](PreviewWirelessSimUsage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

