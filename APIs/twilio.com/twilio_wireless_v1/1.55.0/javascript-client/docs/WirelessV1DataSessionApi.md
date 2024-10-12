# TwilioWireless.WirelessV1DataSessionApi

All URIs are relative to *https://wireless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listDataSession**](WirelessV1DataSessionApi.md#listDataSession) | **GET** /v1/Sims/{SimSid}/DataSessions | 



## listDataSession

> ListDataSessionResponse listDataSession(simSid, opts)





### Example

```javascript
import TwilioWireless from 'twilio_wireless';
let defaultClient = TwilioWireless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioWireless.WirelessV1DataSessionApi();
let simSid = "simSid_example"; // String | The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) with the Data Sessions to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDataSession(simSid, opts, (error, data, response) => {
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
 **simSid** | **String**| The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) with the Data Sessions to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDataSessionResponse**](ListDataSessionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

