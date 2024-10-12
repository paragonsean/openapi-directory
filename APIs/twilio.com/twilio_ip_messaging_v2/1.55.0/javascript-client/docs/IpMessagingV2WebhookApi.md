# TwilioIpMessaging.IpMessagingV2WebhookApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChannelWebhook**](IpMessagingV2WebhookApi.md#createChannelWebhook) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks | 
[**deleteChannelWebhook**](IpMessagingV2WebhookApi.md#deleteChannelWebhook) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} | 
[**fetchChannelWebhook**](IpMessagingV2WebhookApi.md#fetchChannelWebhook) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} | 
[**listChannelWebhook**](IpMessagingV2WebhookApi.md#listChannelWebhook) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks | 
[**updateChannelWebhook**](IpMessagingV2WebhookApi.md#updateChannelWebhook) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} | 



## createChannelWebhook

> IpMessagingV2ServiceChannelChannelWebhook createChannelWebhook(serviceSid, channelSid, type, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let type = "type_example"; // ChannelWebhookEnumType | 
let opts = {
  'configurationFilters': ["null"], // [String] | 
  'configurationFlowSid': "configurationFlowSid_example", // String | 
  'configurationMethod': "configurationMethod_example", // ChannelWebhookEnumMethod | 
  'configurationRetryCount': 56, // Number | 
  'configurationTriggers': ["null"], // [String] | 
  'configurationUrl': "configurationUrl_example" // String | 
};
apiInstance.createChannelWebhook(serviceSid, channelSid, type, opts, (error, data, response) => {
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
 **type** | **ChannelWebhookEnumType**|  | 
 **configurationFilters** | [**[String]**](String.md)|  | [optional] 
 **configurationFlowSid** | **String**|  | [optional] 
 **configurationMethod** | **ChannelWebhookEnumMethod**|  | [optional] 
 **configurationRetryCount** | **Number**|  | [optional] 
 **configurationTriggers** | [**[String]**](String.md)|  | [optional] 
 **configurationUrl** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceChannelChannelWebhook**](IpMessagingV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteChannelWebhook

> deleteChannelWebhook(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.deleteChannelWebhook(serviceSid, channelSid, sid, (error, data, response) => {
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


## fetchChannelWebhook

> IpMessagingV2ServiceChannelChannelWebhook fetchChannelWebhook(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
apiInstance.fetchChannelWebhook(serviceSid, channelSid, sid, (error, data, response) => {
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

[**IpMessagingV2ServiceChannelChannelWebhook**](IpMessagingV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelWebhook

> ListChannelWebhookResponse listChannelWebhook(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listChannelWebhook(serviceSid, channelSid, opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListChannelWebhookResponse**](ListChannelWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateChannelWebhook

> IpMessagingV2ServiceChannelChannelWebhook updateChannelWebhook(serviceSid, channelSid, sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | 
let channelSid = "channelSid_example"; // String | 
let sid = "sid_example"; // String | 
let opts = {
  'configurationFilters': ["null"], // [String] | 
  'configurationFlowSid': "configurationFlowSid_example", // String | 
  'configurationMethod': "configurationMethod_example", // ChannelWebhookEnumMethod | 
  'configurationRetryCount': 56, // Number | 
  'configurationTriggers': ["null"], // [String] | 
  'configurationUrl': "configurationUrl_example" // String | 
};
apiInstance.updateChannelWebhook(serviceSid, channelSid, sid, opts, (error, data, response) => {
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
 **configurationFilters** | [**[String]**](String.md)|  | [optional] 
 **configurationFlowSid** | **String**|  | [optional] 
 **configurationMethod** | **ChannelWebhookEnumMethod**|  | [optional] 
 **configurationRetryCount** | **Number**|  | [optional] 
 **configurationTriggers** | [**[String]**](String.md)|  | [optional] 
 **configurationUrl** | **String**|  | [optional] 

### Return type

[**IpMessagingV2ServiceChannelChannelWebhook**](IpMessagingV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

