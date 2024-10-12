# TwilioFlex.FlexV1InsightsSessionApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInsightsSession**](FlexV1InsightsSessionApi.md#createInsightsSession) | **POST** /v1/Insights/Session | 



## createInsightsSession

> FlexV1InsightsSession createInsightsSession(opts)



To obtain session details for fetching reports and dashboards

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsSessionApi();
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.createInsightsSession(opts, (error, data, response) => {
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
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

[**FlexV1InsightsSession**](FlexV1InsightsSession.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

