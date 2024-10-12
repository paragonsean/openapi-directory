# TwilioIpMessaging.IpMessagingV2MemberApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMember**](IpMessagingV2MemberApi.md#createMember) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members | 
[**deleteMember**](IpMessagingV2MemberApi.md#deleteMember) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} | 
[**fetchMember**](IpMessagingV2MemberApi.md#fetchMember) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} | 
[**listMember**](IpMessagingV2MemberApi.md#listMember) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members | 
[**updateMember**](IpMessagingV2MemberApi.md#updateMember) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} | 



## createMember

> IpMessagingV2ServiceChannelMember createMember(serviceSid, channelSid, identity, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MemberApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let identity = "identity_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // MemberEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | 
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'lastConsumedMessageIndex': 56, // Number | 
  'lastConsumptionTimestamp': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'roleSid': "roleSid_example" // String | 
};
apiInstance.createMember(serviceSid, channelSid, identity, opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **MemberEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**|  | [optional] 
 **dateCreated** | **Date**|  | [optional] 
 **dateUpdated** | **Date**|  | [optional] 
 **lastConsumedMessageIndex** | **Number**|  | [optional] 
 **lastConsumptionTimestamp** | **Date**|  | [optional] 
 **roleSid** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceChannelMember**](IpMessagingV2ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteMember

> deleteMember(serviceSid, channelSid, sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MemberApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // MemberEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteMember(serviceSid, channelSid, sid, opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **MemberEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchMember

> IpMessagingV2ServiceChannelMember fetchMember(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MemberApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.fetchMember(serviceSid, channelSid, sid, (error, data, response) => {
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

[**IpMessagingV2ServiceChannelMember**](IpMessagingV2ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMember

> ListMemberResponse listMember(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MemberApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let opts = {
  'identity': ["null"], // [String] | 
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMember(serviceSid, channelSid, opts, (error, data, response) => {
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

[**ListMemberResponse**](ListMemberResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMember

> IpMessagingV2ServiceChannelMember updateMember(serviceSid, channelSid, sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MemberApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // MemberEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | 
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'lastConsumedMessageIndex': 56, // Number | 
  'lastConsumptionTimestamp': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'roleSid': "roleSid_example" // String | 
};
apiInstance.updateMember(serviceSid, channelSid, sid, opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **MemberEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**|  | [optional] 
 **dateCreated** | **Date**|  | [optional] 
 **dateUpdated** | **Date**|  | [optional] 
 **lastConsumedMessageIndex** | **Number**|  | [optional] 
 **lastConsumptionTimestamp** | **Date**|  | [optional] 
 **roleSid** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceChannelMember**](IpMessagingV2ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

