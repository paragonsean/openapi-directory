# TwilioPreview.PreviewWirelessSimApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchWirelessSim**](PreviewWirelessSimApi.md#fetchWirelessSim) | **GET** /wireless/Sims/{Sid} | 
[**listWirelessSim**](PreviewWirelessSimApi.md#listWirelessSim) | **GET** /wireless/Sims | 
[**updateWirelessSim**](PreviewWirelessSimApi.md#updateWirelessSim) | **POST** /wireless/Sims/{Sid} | 



## fetchWirelessSim

> PreviewWirelessSim fetchWirelessSim(sid)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessSimApi();
let sid = "sid_example"; // String | 
apiInstance.fetchWirelessSim(sid, (error, data, response) => {
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
 **sid** | **String**|  | 

### Return type

[**PreviewWirelessSim**](PreviewWirelessSim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWirelessSim

> ListWirelessSimResponse listWirelessSim(opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessSimApi();
let opts = {
  'status': "status_example", // String | 
  'iccid': "iccid_example", // String | 
  'ratePlan': "ratePlan_example", // String | 
  'eId': "eId_example", // String | 
  'simRegistrationCode': "simRegistrationCode_example", // String | 
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWirelessSim(opts, (error, data, response) => {
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
 **status** | **String**|  | [optional] 
 **iccid** | **String**|  | [optional] 
 **ratePlan** | **String**|  | [optional] 
 **eId** | **String**|  | [optional] 
 **simRegistrationCode** | **String**|  | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListWirelessSimResponse**](ListWirelessSimResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWirelessSim

> PreviewWirelessSim updateWirelessSim(sid, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessSimApi();
let sid = "sid_example"; // String | 
let opts = {
  'callbackMethod': "callbackMethod_example", // String | 
  'callbackUrl': "callbackUrl_example", // String | 
  'commandsCallbackMethod': "commandsCallbackMethod_example", // String | 
  'commandsCallbackUrl': "commandsCallbackUrl_example", // String | 
  'friendlyName': "friendlyName_example", // String | 
  'ratePlan': "ratePlan_example", // String | 
  'smsFallbackMethod': "smsFallbackMethod_example", // String | 
  'smsFallbackUrl': "smsFallbackUrl_example", // String | 
  'smsMethod': "smsMethod_example", // String | 
  'smsUrl': "smsUrl_example", // String | 
  'status': "status_example", // String | 
  'uniqueName': "uniqueName_example", // String | 
  'voiceFallbackMethod': "voiceFallbackMethod_example", // String | 
  'voiceFallbackUrl': "voiceFallbackUrl_example", // String | 
  'voiceMethod': "voiceMethod_example", // String | 
  'voiceUrl': "voiceUrl_example" // String | 
};
apiInstance.updateWirelessSim(sid, opts, (error, data, response) => {
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
 **sid** | **String**|  | 
 **callbackMethod** | **String**|  | [optional] 
 **callbackUrl** | **String**|  | [optional] 
 **commandsCallbackMethod** | **String**|  | [optional] 
 **commandsCallbackUrl** | **String**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **ratePlan** | **String**|  | [optional] 
 **smsFallbackMethod** | **String**|  | [optional] 
 **smsFallbackUrl** | **String**|  | [optional] 
 **smsMethod** | **String**|  | [optional] 
 **smsUrl** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **uniqueName** | **String**|  | [optional] 
 **voiceFallbackMethod** | **String**|  | [optional] 
 **voiceFallbackUrl** | **String**|  | [optional] 
 **voiceMethod** | **String**|  | [optional] 
 **voiceUrl** | **String**|  | [optional] 

### Return type

[**PreviewWirelessSim**](PreviewWirelessSim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

