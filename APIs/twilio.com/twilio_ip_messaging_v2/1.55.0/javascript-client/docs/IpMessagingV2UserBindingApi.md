# TwilioIpMessaging.IpMessagingV2UserBindingApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserBinding**](IpMessagingV2UserBindingApi.md#deleteUserBinding) | **DELETE** /v2/Services/{ServiceSid}/Users/{UserSid}/Bindings/{Sid} | 
[**fetchUserBinding**](IpMessagingV2UserBindingApi.md#fetchUserBinding) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Bindings/{Sid} | 
[**listUserBinding**](IpMessagingV2UserBindingApi.md#listUserBinding) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Bindings | 



## deleteUserBinding

> deleteUserBinding(serviceSid, userSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserBindingApi();
let serviceSid = "serviceSid_example"; // String | 
let userSid = "userSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.deleteUserBinding(serviceSid, userSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **userSid** | **String**|  | 
 **sid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchUserBinding

> IpMessagingV2ServiceUserUserBinding fetchUserBinding(serviceSid, userSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserBindingApi();
let serviceSid = "serviceSid_example"; // String | 
let userSid = "userSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.fetchUserBinding(serviceSid, userSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **userSid** | **String**|  | 
 **sid** | **String**|  | 

### Return type

[**IpMessagingV2ServiceUserUserBinding**](IpMessagingV2ServiceUserUserBinding.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUserBinding

> ListUserBindingResponse listUserBinding(serviceSid, userSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserBindingApi();
let serviceSid = "serviceSid_example"; // String | 
let userSid = "userSid_example"; // String | 
let opts = {
  'bindingType': ["null"], // [UserBindingEnumBindingType] | 
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUserBinding(serviceSid, userSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **userSid** | **String**|  | 
 **bindingType** | [**[UserBindingEnumBindingType]**](UserBindingEnumBindingType.md)|  | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListUserBindingResponse**](ListUserBindingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

