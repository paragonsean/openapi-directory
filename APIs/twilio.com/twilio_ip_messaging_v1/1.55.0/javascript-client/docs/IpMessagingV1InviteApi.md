# TwilioIpMessaging.IpMessagingV1InviteApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInvite**](IpMessagingV1InviteApi.md#createInvite) | **POST** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Invites | 
[**deleteInvite**](IpMessagingV1InviteApi.md#deleteInvite) | **DELETE** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Invites/{Sid} | 
[**fetchInvite**](IpMessagingV1InviteApi.md#fetchInvite) | **GET** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Invites/{Sid} | 
[**listInvite**](IpMessagingV1InviteApi.md#listInvite) | **GET** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Invites | 



## createInvite

> IpMessagingV1ServiceChannelInvite createInvite(serviceSid, channelSid, identity, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1InviteApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let identity = "identity_example"; // String | 
let opts = {
  'roleSid': "roleSid_example" // String | 
};
apiInstance.createInvite(serviceSid, channelSid, identity, opts, (error, data, response) => {
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
 **channelSid** | **String**|  | 
 **identity** | **String**|  | 
 **roleSid** | **String**|  | [optional] 

### Return type

[**IpMessagingV1ServiceChannelInvite**](IpMessagingV1ServiceChannelInvite.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteInvite

> deleteInvite(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1InviteApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.deleteInvite(serviceSid, channelSid, sid, (error, data, response) => {
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
 **channelSid** | **String**|  | 
 **sid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchInvite

> IpMessagingV1ServiceChannelInvite fetchInvite(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1InviteApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.fetchInvite(serviceSid, channelSid, sid, (error, data, response) => {
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
 **channelSid** | **String**|  | 
 **sid** | **String**|  | 

### Return type

[**IpMessagingV1ServiceChannelInvite**](IpMessagingV1ServiceChannelInvite.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInvite

> ListInviteResponse listInvite(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1InviteApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let opts = {
  'identity': ["null"], // [String] | 
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInvite(serviceSid, channelSid, opts, (error, data, response) => {
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
 **channelSid** | **String**|  | 
 **identity** | [**[String]**](String.md)|  | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInviteResponse**](ListInviteResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

