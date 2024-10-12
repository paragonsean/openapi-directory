# TwilioApi.Api20100401NewKeyApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNewKey**](Api20100401NewKeyApi.md#createNewKey) | **POST** /2010-04-01/Accounts/{AccountSid}/Keys.json | 



## createNewKey

> ApiV2010AccountNewKey createNewKey(accountSid, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401NewKeyApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Key resource.
let opts = {
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
};
apiInstance.createNewKey(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Key resource. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 

### Return type

[**ApiV2010AccountNewKey**](ApiV2010AccountNewKey.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

