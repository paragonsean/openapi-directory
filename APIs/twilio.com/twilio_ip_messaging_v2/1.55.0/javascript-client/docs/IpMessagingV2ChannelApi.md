# TwilioIpMessaging.IpMessagingV2ChannelApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChannel**](IpMessagingV2ChannelApi.md#createChannel) | **POST** /v2/Services/{ServiceSid}/Channels | 
[**deleteChannel**](IpMessagingV2ChannelApi.md#deleteChannel) | **DELETE** /v2/Services/{ServiceSid}/Channels/{Sid} | 
[**fetchChannel**](IpMessagingV2ChannelApi.md#fetchChannel) | **GET** /v2/Services/{ServiceSid}/Channels/{Sid} | 
[**listChannel**](IpMessagingV2ChannelApi.md#listChannel) | **GET** /v2/Services/{ServiceSid}/Channels | 
[**updateChannel**](IpMessagingV2ChannelApi.md#updateChannel) | **POST** /v2/Services/{ServiceSid}/Channels/{Sid} | 



## createChannel

> IpMessagingV2ServiceChannel createChannel(serviceSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | 
  'createdBy': "createdBy_example", // String | 
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'friendlyName': "friendlyName_example", // String | 
  'type': "type_example", // ChannelEnumChannelType | 
  'uniqueName': "uniqueName_example" // String | 
};
apiInstance.createChannel(serviceSid, opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**|  | [optional] 
 **createdBy** | **String**|  | [optional] 
 **dateCreated** | **Date**|  | [optional] 
 **dateUpdated** | **Date**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **type** | **ChannelEnumChannelType**|  | [optional] 
 **uniqueName** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceChannel**](IpMessagingV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteChannel

> deleteChannel(serviceSid, sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | 
let sid = "sid_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteChannel(serviceSid, sid, opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchChannel

> IpMessagingV2ServiceChannel fetchChannel(serviceSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.fetchChannel(serviceSid, sid, (error, data, response) => {
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

[**IpMessagingV2ServiceChannel**](IpMessagingV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannel

> ListChannelResponse listChannel(serviceSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | 
let opts = {
  'type': ["null"], // [ChannelEnumChannelType] | 
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listChannel(serviceSid, opts, (error, data, response) => {
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
 **type** | [**[ChannelEnumChannelType]**](ChannelEnumChannelType.md)|  | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListChannelResponse**](ListChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateChannel

> IpMessagingV2ServiceChannel updateChannel(serviceSid, sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2ChannelApi();
let serviceSid = "serviceSid_example"; // String | 
let sid = "sid_example"; // String | 
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | 
  'createdBy': "createdBy_example", // String | 
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'friendlyName': "friendlyName_example", // String | 
  'uniqueName': "uniqueName_example" // String | 
};
apiInstance.updateChannel(serviceSid, sid, opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**|  | [optional] 
 **createdBy** | **String**|  | [optional] 
 **dateCreated** | **Date**|  | [optional] 
 **dateUpdated** | **Date**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **uniqueName** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceChannel**](IpMessagingV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

