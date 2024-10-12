# TwilioIpMessaging.IpMessagingV2UserApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUser**](IpMessagingV2UserApi.md#createUser) | **POST** /v2/Services/{ServiceSid}/Users | 
[**deleteUser**](IpMessagingV2UserApi.md#deleteUser) | **DELETE** /v2/Services/{ServiceSid}/Users/{Sid} | 
[**fetchUser**](IpMessagingV2UserApi.md#fetchUser) | **GET** /v2/Services/{ServiceSid}/Users/{Sid} | 
[**listUser**](IpMessagingV2UserApi.md#listUser) | **GET** /v2/Services/{ServiceSid}/Users | 
[**updateUser**](IpMessagingV2UserApi.md#updateUser) | **POST** /v2/Services/{ServiceSid}/Users/{Sid} | 



## createUser

> IpMessagingV2ServiceUser createUser(serviceSid, identity, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserApi();
let serviceSid = "serviceSid_example"; // String | 
let identity = "identity_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | 
  'friendlyName': "friendlyName_example", // String | 
  'roleSid': "roleSid_example" // String | 
};
apiInstance.createUser(serviceSid, identity, opts, (error, data, response) => {
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
 **identity** | **String**|  | 
 **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **roleSid** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceUser**](IpMessagingV2ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteUser

> deleteUser(serviceSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserApi();
let serviceSid = "serviceSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.deleteUser(serviceSid, sid, (error, data, response) => {
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
 **sid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchUser

> IpMessagingV2ServiceUser fetchUser(serviceSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserApi();
let serviceSid = "serviceSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.fetchUser(serviceSid, sid, (error, data, response) => {
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
 **sid** | **String**|  | 

### Return type

[**IpMessagingV2ServiceUser**](IpMessagingV2ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUser

> ListUserResponse listUser(serviceSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserApi();
let serviceSid = "serviceSid_example"; // String | 
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUser(serviceSid, opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListUserResponse**](ListUserResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUser

> IpMessagingV2ServiceUser updateUser(serviceSid, sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserApi();
let serviceSid = "serviceSid_example"; // String | 
let sid = "sid_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | 
  'friendlyName': "friendlyName_example", // String | 
  'roleSid': "roleSid_example" // String | 
};
apiInstance.updateUser(serviceSid, sid, opts, (error, data, response) => {
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
 **sid** | **String**|  | 
 **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **roleSid** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceUser**](IpMessagingV2ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

