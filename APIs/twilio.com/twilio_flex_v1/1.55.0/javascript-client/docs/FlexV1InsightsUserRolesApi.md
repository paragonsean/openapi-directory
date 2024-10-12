# TwilioFlex.FlexV1InsightsUserRolesApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchInsightsUserRoles**](FlexV1InsightsUserRolesApi.md#fetchInsightsUserRoles) | **GET** /v1/Insights/UserRoles | 



## fetchInsightsUserRoles

> FlexV1InsightsUserRoles fetchInsightsUserRoles(opts)



This is used by Flex UI and Quality Management to fetch the Flex Insights roles for the user

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsUserRolesApi();
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.fetchInsightsUserRoles(opts, (error, data, response) => {
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

[**FlexV1InsightsUserRoles**](FlexV1InsightsUserRoles.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

