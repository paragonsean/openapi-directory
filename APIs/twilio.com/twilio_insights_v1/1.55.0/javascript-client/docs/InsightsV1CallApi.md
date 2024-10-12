# TwilioInsights.InsightsV1CallApi

All URIs are relative to *https://insights.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchCall**](InsightsV1CallApi.md#fetchCall) | **GET** /v1/Voice/{Sid} | 



## fetchCall

> InsightsV1Call fetchCall(sid)





### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1CallApi();
let sid = "sid_example"; // String | 
apiInstance.fetchCall(sid, (error, data, response) => {
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

[**InsightsV1Call**](InsightsV1Call.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

