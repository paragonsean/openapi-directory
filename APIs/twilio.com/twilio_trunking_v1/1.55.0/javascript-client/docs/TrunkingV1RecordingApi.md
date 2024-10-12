# TwilioTrunking.TrunkingV1RecordingApi

All URIs are relative to *https://trunking.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchRecording**](TrunkingV1RecordingApi.md#fetchRecording) | **GET** /v1/Trunks/{TrunkSid}/Recording | 
[**updateRecording**](TrunkingV1RecordingApi.md#updateRecording) | **POST** /v1/Trunks/{TrunkSid}/Recording | 



## fetchRecording

> TrunkingV1TrunkRecording fetchRecording(trunkSid)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1RecordingApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the recording settings.
apiInstance.fetchRecording(trunkSid, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk from which to fetch the recording settings. | 

### Return type

[**TrunkingV1TrunkRecording**](TrunkingV1TrunkRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRecording

> TrunkingV1TrunkRecording updateRecording(trunkSid, opts)





### Example

```javascript
import TwilioTrunking from 'twilio_trunking';
let defaultClient = TwilioTrunking.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTrunking.TrunkingV1RecordingApi();
let trunkSid = "trunkSid_example"; // String | The SID of the Trunk that will have its recording settings updated.
let opts = {
  'mode': "mode_example", // RecordingEnumRecordingMode | 
  'trim': "trim_example" // RecordingEnumRecordingTrim | 
};
apiInstance.updateRecording(trunkSid, opts, (error, data, response) => {
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
 **trunkSid** | **String**| The SID of the Trunk that will have its recording settings updated. | 
 **mode** | **RecordingEnumRecordingMode**|  | [optional] 
 **trim** | **RecordingEnumRecordingTrim**|  | [optional] 

### Return type

[**TrunkingV1TrunkRecording**](TrunkingV1TrunkRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

