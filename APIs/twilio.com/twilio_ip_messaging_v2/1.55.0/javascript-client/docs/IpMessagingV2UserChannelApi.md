# TwilioIpMessaging.IpMessagingV2UserChannelApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserChannel**](IpMessagingV2UserChannelApi.md#deleteUserChannel) | **DELETE** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels/{ChannelSid} | 
[**fetchUserChannel**](IpMessagingV2UserChannelApi.md#fetchUserChannel) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels/{ChannelSid} | 
[**listUserChannel**](IpMessagingV2UserChannelApi.md#listUserChannel) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels | 
[**updateUserChannel**](IpMessagingV2UserChannelApi.md#updateUserChannel) | **POST** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels/{ChannelSid} | 



## deleteUserChannel

> deleteUserChannel(serviceSid, userSid, channelSid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserChannelApi();
let serviceSid = "serviceSid_example"; // String | 
let userSid = "userSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
apiInstance.deleteUserChannel(serviceSid, userSid, channelSid, (error, data, response) => {
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
 **channelSid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchUserChannel

> IpMessagingV2ServiceUserUserChannel fetchUserChannel(serviceSid, userSid, channelSid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserChannelApi();
let serviceSid = "serviceSid_example"; // String | 
let userSid = "userSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
apiInstance.fetchUserChannel(serviceSid, userSid, channelSid, (error, data, response) => {
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
 **channelSid** | **String**|  | 

### Return type

[**IpMessagingV2ServiceUserUserChannel**](IpMessagingV2ServiceUserUserChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUserChannel

> ListUserChannelResponse listUserChannel(serviceSid, userSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserChannelApi();
let serviceSid = "serviceSid_example"; // String | 
let userSid = "userSid_example"; // String | 
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUserChannel(serviceSid, userSid, opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListUserChannelResponse**](ListUserChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUserChannel

> IpMessagingV2ServiceUserUserChannel updateUserChannel(serviceSid, userSid, channelSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2UserChannelApi();
let serviceSid = "serviceSid_example"; // String | 
let userSid = "userSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let opts = {
  'lastConsumedMessageIndex': 56, // Number | 
  'lastConsumptionTimestamp': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'notificationLevel': "notificationLevel_example" // UserChannelEnumNotificationLevel | 
};
apiInstance.updateUserChannel(serviceSid, userSid, channelSid, opts, (error, data, response) => {
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
 **channelSid** | **String**|  | 
 **lastConsumedMessageIndex** | **Number**|  | [optional] 
 **lastConsumptionTimestamp** | **Date**|  | [optional] 
 **notificationLevel** | **UserChannelEnumNotificationLevel**|  | [optional] 

### Return type

[**IpMessagingV2ServiceUserUserChannel**](IpMessagingV2ServiceUserUserChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

