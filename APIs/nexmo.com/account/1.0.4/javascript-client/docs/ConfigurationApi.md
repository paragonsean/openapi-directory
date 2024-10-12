# AccountApi.ConfigurationApi

All URIs are relative to *https://api.nexmo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeAccountSettings**](ConfigurationApi.md#changeAccountSettings) | **POST** /account/settings | Change Account Settings
[**registerSender**](ConfigurationApi.md#registerSender) | **POST** /account/register-sender | Register an email sender



## changeAccountSettings

> AccountSettings changeAccountSettings(apiKey, apiSecret, opts)

Change Account Settings

Update the default webhook URLs associated with your account:   * Callback URL for incoming SMS messages   * Callback URL for delivery receipts  Note that the URLs you provide must be valid and active. Vonage will check that they return a 200 OK response before the setting is saved.

### Example

```javascript
import AccountApi from 'account_api';

let apiInstance = new AccountApi.ConfigurationApi();
let apiKey = "abcd1234"; // String | Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
let apiSecret = "ABCDEFGH01234abc"; // String | Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
let opts = {
  'drCallBackUrl': "drCallBackUrl_example", // String | The webhook URL that Vonage makes a request to when a delivery receipt is available  for an SMS sent by one of your Vonage numbers. Send an empty string to unset this value.
  'moCallBackUrl': "moCallBackUrl_example" // String | The default webhook URL for inbound SMS. If an SMS is received at a Vonage number  that does not have its own inbound SMS webhook configured, Vonage makes a request here. Send an empty string to unset this value.
};
apiInstance.changeAccountSettings(apiKey, apiSecret, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com) | 
 **apiSecret** | **String**| Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com) | 
 **drCallBackUrl** | **String**| The webhook URL that Vonage makes a request to when a delivery receipt is available  for an SMS sent by one of your Vonage numbers. Send an empty string to unset this value. | [optional] 
 **moCallBackUrl** | **String**| The default webhook URL for inbound SMS. If an SMS is received at a Vonage number  that does not have its own inbound SMS webhook configured, Vonage makes a request here. Send an empty string to unset this value. | [optional] 

### Return type

[**AccountSettings**](AccountSettings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## registerSender

> RegisterEmailResponse registerSender(apiKey, apiSecret, registerEmailRequest)

Register an email sender

Register an email sender with an API Key for using email with Verify V2.

### Example

```javascript
import AccountApi from 'account_api';

let apiInstance = new AccountApi.ConfigurationApi();
let apiKey = "abcd1234"; // String | Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
let apiSecret = "ABCDEFGH01234abc"; // String | Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
let registerEmailRequest = new AccountApi.RegisterEmailRequest(); // RegisterEmailRequest | 
apiInstance.registerSender(apiKey, apiSecret, registerEmailRequest, (error, data, response) => {
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
 **apiKey** | **String**| Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com) | 
 **apiSecret** | **String**| Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com) | 
 **registerEmailRequest** | [**RegisterEmailRequest**](RegisterEmailRequest.md)|  | 

### Return type

[**RegisterEmailResponse**](RegisterEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

