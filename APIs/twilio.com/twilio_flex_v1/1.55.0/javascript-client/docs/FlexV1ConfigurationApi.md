# TwilioFlex.FlexV1ConfigurationApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchConfiguration**](FlexV1ConfigurationApi.md#fetchConfiguration) | **GET** /v1/Configuration | 



## fetchConfiguration

> FlexV1Configuration fetchConfiguration(opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1ConfigurationApi();
let opts = {
  'uiVersion': "uiVersion_example" // String | The Pinned UI version of the Configuration resource to fetch.
};
apiInstance.fetchConfiguration(opts, (error, data, response) => {
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
 **uiVersion** | **String**| The Pinned UI version of the Configuration resource to fetch. | [optional] 

### Return type

[**FlexV1Configuration**](FlexV1Configuration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

