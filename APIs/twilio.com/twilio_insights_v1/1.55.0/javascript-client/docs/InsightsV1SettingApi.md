# TwilioInsights.InsightsV1SettingApi

All URIs are relative to *https://insights.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAccountSettings**](InsightsV1SettingApi.md#fetchAccountSettings) | **GET** /v1/Voice/Settings | 
[**updateAccountSettings**](InsightsV1SettingApi.md#updateAccountSettings) | **POST** /v1/Voice/Settings | 



## fetchAccountSettings

> InsightsV1AccountSettings fetchAccountSettings(opts)



Get the Voice Insights Settings.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1SettingApi();
let opts = {
  'subaccountSid': "subaccountSid_example" // String | The unique SID identifier of the Subaccount.
};
apiInstance.fetchAccountSettings(opts, (error, data, response) => {
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
 **subaccountSid** | **String**| The unique SID identifier of the Subaccount. | [optional] 

### Return type

[**InsightsV1AccountSettings**](InsightsV1AccountSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccountSettings

> InsightsV1AccountSettings updateAccountSettings(opts)



Update a specific Voice Insights Setting.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1SettingApi();
let opts = {
  'advancedFeatures': true, // Boolean | A boolean flag to enable Advanced Features for Voice Insights.
  'subaccountSid': "subaccountSid_example", // String | The unique SID identifier of the Subaccount.
  'voiceTrace': true // Boolean | A boolean flag to enable Voice Trace.
};
apiInstance.updateAccountSettings(opts, (error, data, response) => {
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
 **advancedFeatures** | **Boolean**| A boolean flag to enable Advanced Features for Voice Insights. | [optional] 
 **subaccountSid** | **String**| The unique SID identifier of the Subaccount. | [optional] 
 **voiceTrace** | **Boolean**| A boolean flag to enable Voice Trace. | [optional] 

### Return type

[**InsightsV1AccountSettings**](InsightsV1AccountSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

