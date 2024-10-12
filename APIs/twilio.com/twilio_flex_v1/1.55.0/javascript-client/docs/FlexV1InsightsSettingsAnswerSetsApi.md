# TwilioFlex.FlexV1InsightsSettingsAnswerSetsApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchInsightsSettingsAnswersets**](FlexV1InsightsSettingsAnswerSetsApi.md#fetchInsightsSettingsAnswersets) | **GET** /v1/Insights/QualityManagement/Settings/AnswerSets | 



## fetchInsightsSettingsAnswersets

> FlexV1InsightsSettingsAnswersets fetchInsightsSettingsAnswersets(opts)



To get the Answer Set Settings for an Account

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsSettingsAnswerSetsApi();
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.fetchInsightsSettingsAnswersets(opts, (error, data, response) => {
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

[**FlexV1InsightsSettingsAnswersets**](FlexV1InsightsSettingsAnswersets.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

