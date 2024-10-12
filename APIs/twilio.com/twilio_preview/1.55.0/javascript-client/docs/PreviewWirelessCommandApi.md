# TwilioPreview.PreviewWirelessCommandApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWirelessCommand**](PreviewWirelessCommandApi.md#createWirelessCommand) | **POST** /wireless/Commands | 
[**fetchWirelessCommand**](PreviewWirelessCommandApi.md#fetchWirelessCommand) | **GET** /wireless/Commands/{Sid} | 
[**listWirelessCommand**](PreviewWirelessCommandApi.md#listWirelessCommand) | **GET** /wireless/Commands | 



## createWirelessCommand

> PreviewWirelessCommand createWirelessCommand(command, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessCommandApi();
let command = "command_example"; // String | 
let opts = {
  'callbackMethod': "callbackMethod_example", // String | 
  'callbackUrl': "callbackUrl_example", // String | 
  'commandMode': "commandMode_example", // String | 
  'device': "device_example", // String | 
  'includeSid': "includeSid_example", // String | 
  'sim': "sim_example" // String | 
};
apiInstance.createWirelessCommand(command, opts, (error, data, response) => {
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
 **command** | **String**|  | 
 **callbackMethod** | **String**|  | [optional] 
 **callbackUrl** | **String**|  | [optional] 
 **commandMode** | **String**|  | [optional] 
 **device** | **String**|  | [optional] 
 **includeSid** | **String**|  | [optional] 
 **sim** | **String**|  | [optional] 

### Return type

[**PreviewWirelessCommand**](PreviewWirelessCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchWirelessCommand

> PreviewWirelessCommand fetchWirelessCommand(sid)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessCommandApi();
let sid = "sid_example"; // String | 
apiInstance.fetchWirelessCommand(sid, (error, data, response) => {
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

[**PreviewWirelessCommand**](PreviewWirelessCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWirelessCommand

> ListWirelessCommandResponse listWirelessCommand(opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessCommandApi();
let opts = {
  'device': "device_example", // String | 
  'sim': "sim_example", // String | 
  'status': "status_example", // String | 
  'direction': "direction_example", // String | 
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWirelessCommand(opts, (error, data, response) => {
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
 **device** | **String**|  | [optional] 
 **sim** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **direction** | **String**|  | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListWirelessCommandResponse**](ListWirelessCommandResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

