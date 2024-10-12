# TwilioIpMessaging.IpMessagingV2MessageApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMessage**](IpMessagingV2MessageApi.md#createMessage) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages | 
[**deleteMessage**](IpMessagingV2MessageApi.md#deleteMessage) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} | 
[**fetchMessage**](IpMessagingV2MessageApi.md#fetchMessage) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} | 
[**listMessage**](IpMessagingV2MessageApi.md#listMessage) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages | 
[**updateMessage**](IpMessagingV2MessageApi.md#updateMessage) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} | 



## createMessage

> IpMessagingV2ServiceChannelMessage createMessage(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MessageApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // MessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | 
  'body': "body_example", // String | 
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'from': "from_example", // String | 
  'lastUpdatedBy': "lastUpdatedBy_example", // String | 
  'mediaSid': "mediaSid_example" // String | 
};
apiInstance.createMessage(serviceSid, channelSid, opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **MessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**|  | [optional] 
 **body** | **String**|  | [optional] 
 **dateCreated** | **Date**|  | [optional] 
 **dateUpdated** | **Date**|  | [optional] 
 **from** | **String**|  | [optional] 
 **lastUpdatedBy** | **String**|  | [optional] 
 **mediaSid** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceChannelMessage**](IpMessagingV2ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteMessage

> deleteMessage(serviceSid, channelSid, sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MessageApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // MessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteMessage(serviceSid, channelSid, sid, opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **MessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchMessage

> IpMessagingV2ServiceChannelMessage fetchMessage(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MessageApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.fetchMessage(serviceSid, channelSid, sid, (error, data, response) => {
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

[**IpMessagingV2ServiceChannelMessage**](IpMessagingV2ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMessage

> ListMessageResponse listMessage(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MessageApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let opts = {
  'order': "order_example", // MessageEnumOrderType | 
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMessage(serviceSid, channelSid, opts, (error, data, response) => {
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
 **order** | **MessageEnumOrderType**|  | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMessageResponse**](ListMessageResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMessage

> IpMessagingV2ServiceChannelMessage updateMessage(serviceSid, channelSid, sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2MessageApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // MessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | 
  'body': "body_example", // String | 
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'from': "from_example", // String | 
  'lastUpdatedBy': "lastUpdatedBy_example" // String | 
};
apiInstance.updateMessage(serviceSid, channelSid, sid, opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **MessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**|  | [optional] 
 **body** | **String**|  | [optional] 
 **dateCreated** | **Date**|  | [optional] 
 **dateUpdated** | **Date**|  | [optional] 
 **from** | **String**|  | [optional] 
 **lastUpdatedBy** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceChannelMessage**](IpMessagingV2ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

