# TwilioMessaging.MessagingV1UsAppToPersonUsecaseApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchUsAppToPersonUsecase**](MessagingV1UsAppToPersonUsecaseApi.md#fetchUsAppToPersonUsecase) | **GET** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/Usecases | 



## fetchUsAppToPersonUsecase

> MessagingV1ServiceUsAppToPersonUsecase fetchUsAppToPersonUsecase(messagingServiceSid, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1UsAppToPersonUsecaseApi();
let messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.
let opts = {
  'brandRegistrationSid': "brandRegistrationSid_example" // String | The unique string to identify the A2P brand.
};
apiInstance.fetchUsAppToPersonUsecase(messagingServiceSid, opts, (error, data, response) => {
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
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from. | 
 **brandRegistrationSid** | **String**| The unique string to identify the A2P brand. | [optional] 

### Return type

[**MessagingV1ServiceUsAppToPersonUsecase**](MessagingV1ServiceUsAppToPersonUsecase.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

