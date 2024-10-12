# TwilioMessaging.MessagingV1DeactivationsApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchDeactivation**](MessagingV1DeactivationsApi.md#fetchDeactivation) | **GET** /v1/Deactivations | 



## fetchDeactivation

> fetchDeactivation(opts)



Fetch a list of all United States numbers that have been deactivated on a specific date.

### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1DeactivationsApi();
let opts = {
  'date': new Date("2013-10-20") // Date | The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.
};
apiInstance.fetchDeactivation(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **Date**| The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format. | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

