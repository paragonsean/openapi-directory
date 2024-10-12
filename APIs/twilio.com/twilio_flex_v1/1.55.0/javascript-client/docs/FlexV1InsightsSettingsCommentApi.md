# TwilioFlex.FlexV1InsightsSettingsCommentApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchInsightsSettingsComment**](FlexV1InsightsSettingsCommentApi.md#fetchInsightsSettingsComment) | **GET** /v1/Insights/QualityManagement/Settings/CommentTags | 



## fetchInsightsSettingsComment

> FlexV1InsightsSettingsComment fetchInsightsSettingsComment(opts)



To get the Comment Settings for an Account

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsSettingsCommentApi();
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.fetchInsightsSettingsComment(opts, (error, data, response) => {
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

[**FlexV1InsightsSettingsComment**](FlexV1InsightsSettingsComment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

