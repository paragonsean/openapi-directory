# TwilioSupersim.SupersimV1SettingsUpdateApi

All URIs are relative to *https://supersim.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listSettingsUpdate**](SupersimV1SettingsUpdateApi.md#listSettingsUpdate) | **GET** /v1/SettingsUpdates | 



## listSettingsUpdate

> ListSettingsUpdateResponse listSettingsUpdate(opts)



Retrieve a list of Settings Updates.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1SettingsUpdateApi();
let opts = {
  'sim': "sim_example", // String | Filter the Settings Updates by a Super SIM's SID or UniqueName.
  'status': "status_example", // SettingsUpdateEnumStatus | Filter the Settings Updates by status. Can be `scheduled`, `in-progress`, `successful`, or `failed`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSettingsUpdate(opts, (error, data, response) => {
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
 **sim** | **String**| Filter the Settings Updates by a Super SIM&#39;s SID or UniqueName. | [optional] 
 **status** | **SettingsUpdateEnumStatus**| Filter the Settings Updates by status. Can be &#x60;scheduled&#x60;, &#x60;in-progress&#x60;, &#x60;successful&#x60;, or &#x60;failed&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSettingsUpdateResponse**](ListSettingsUpdateResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

