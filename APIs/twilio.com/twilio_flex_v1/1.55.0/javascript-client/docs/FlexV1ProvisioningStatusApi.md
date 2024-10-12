# TwilioFlex.FlexV1ProvisioningStatusApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchProvisioningStatus**](FlexV1ProvisioningStatusApi.md#fetchProvisioningStatus) | **GET** /v1/account/provision/status | 



## fetchProvisioningStatus

> FlexV1ProvisioningStatus fetchProvisioningStatus()





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1ProvisioningStatusApi();
apiInstance.fetchProvisioningStatus((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**FlexV1ProvisioningStatus**](FlexV1ProvisioningStatus.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

