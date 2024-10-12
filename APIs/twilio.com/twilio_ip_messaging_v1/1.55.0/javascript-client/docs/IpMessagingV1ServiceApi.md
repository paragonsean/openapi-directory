# TwilioIpMessaging.IpMessagingV1ServiceApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](IpMessagingV1ServiceApi.md#createService) | **POST** /v1/Services | 
[**deleteService**](IpMessagingV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} | 
[**fetchService**](IpMessagingV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} | 
[**listService**](IpMessagingV1ServiceApi.md#listService) | **GET** /v1/Services | 
[**updateService**](IpMessagingV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} | 



## createService

> IpMessagingV1Service createService(friendlyName)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1ServiceApi();
let friendlyName = "friendlyName_example"; // String | 
apiInstance.createService(friendlyName, (error, data, response) => {
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
 **friendlyName** | **String**|  | 

### Return type

[**IpMessagingV1Service**](IpMessagingV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteService

> deleteService(sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1ServiceApi();
let sid = "sid_example"; // String | 
apiInstance.deleteService(sid, (error, data, response) => {
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
 **sid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchService

> IpMessagingV1Service fetchService(sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1ServiceApi();
let sid = "sid_example"; // String | 
apiInstance.fetchService(sid, (error, data, response) => {
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
 **sid** | **String**|  | 

### Return type

[**IpMessagingV1Service**](IpMessagingV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listService

> ListServiceResponse listService(opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1ServiceApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listService(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateService

> IpMessagingV1Service updateService(sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV1ServiceApi();
let sid = "sid_example"; // String | 
let opts = {
  'consumptionReportInterval': 56, // Number | 
  'defaultChannelCreatorRoleSid': "defaultChannelCreatorRoleSid_example", // String | 
  'defaultChannelRoleSid': "defaultChannelRoleSid_example", // String | 
  'defaultServiceRoleSid': "defaultServiceRoleSid_example", // String | 
  'friendlyName': "friendlyName_example", // String | 
  'limitsChannelMembers': 56, // Number | 
  'limitsUserChannels': 56, // Number | 
  'notificationsAddedToChannelEnabled': true, // Boolean | 
  'notificationsAddedToChannelTemplate': "notificationsAddedToChannelTemplate_example", // String | 
  'notificationsInvitedToChannelEnabled': true, // Boolean | 
  'notificationsInvitedToChannelTemplate': "notificationsInvitedToChannelTemplate_example", // String | 
  'notificationsNewMessageEnabled': true, // Boolean | 
  'notificationsNewMessageTemplate': "notificationsNewMessageTemplate_example", // String | 
  'notificationsRemovedFromChannelEnabled': true, // Boolean | 
  'notificationsRemovedFromChannelTemplate': "notificationsRemovedFromChannelTemplate_example", // String | 
  'postWebhookUrl': "postWebhookUrl_example", // String | 
  'preWebhookUrl': "preWebhookUrl_example", // String | 
  'reachabilityEnabled': true, // Boolean | 
  'readStatusEnabled': true, // Boolean | 
  'typingIndicatorTimeout': 56, // Number | 
  'webhookFilters': ["null"], // [String] | 
  'webhookMethod': "webhookMethod_example", // String | 
  'webhooksOnChannelAddMethod': "webhooksOnChannelAddMethod_example", // String | 
  'webhooksOnChannelAddUrl': "webhooksOnChannelAddUrl_example", // String | 
  'webhooksOnChannelAddedMethod': "webhooksOnChannelAddedMethod_example", // String | 
  'webhooksOnChannelAddedUrl': "webhooksOnChannelAddedUrl_example", // String | 
  'webhooksOnChannelDestroyMethod': "webhooksOnChannelDestroyMethod_example", // String | 
  'webhooksOnChannelDestroyUrl': "webhooksOnChannelDestroyUrl_example", // String | 
  'webhooksOnChannelDestroyedMethod': "webhooksOnChannelDestroyedMethod_example", // String | 
  'webhooksOnChannelDestroyedUrl': "webhooksOnChannelDestroyedUrl_example", // String | 
  'webhooksOnChannelUpdateMethod': "webhooksOnChannelUpdateMethod_example", // String | 
  'webhooksOnChannelUpdateUrl': "webhooksOnChannelUpdateUrl_example", // String | 
  'webhooksOnChannelUpdatedMethod': "webhooksOnChannelUpdatedMethod_example", // String | 
  'webhooksOnChannelUpdatedUrl': "webhooksOnChannelUpdatedUrl_example", // String | 
  'webhooksOnMemberAddMethod': "webhooksOnMemberAddMethod_example", // String | 
  'webhooksOnMemberAddUrl': "webhooksOnMemberAddUrl_example", // String | 
  'webhooksOnMemberAddedMethod': "webhooksOnMemberAddedMethod_example", // String | 
  'webhooksOnMemberAddedUrl': "webhooksOnMemberAddedUrl_example", // String | 
  'webhooksOnMemberRemoveMethod': "webhooksOnMemberRemoveMethod_example", // String | 
  'webhooksOnMemberRemoveUrl': "webhooksOnMemberRemoveUrl_example", // String | 
  'webhooksOnMemberRemovedMethod': "webhooksOnMemberRemovedMethod_example", // String | 
  'webhooksOnMemberRemovedUrl': "webhooksOnMemberRemovedUrl_example", // String | 
  'webhooksOnMessageRemoveMethod': "webhooksOnMessageRemoveMethod_example", // String | 
  'webhooksOnMessageRemoveUrl': "webhooksOnMessageRemoveUrl_example", // String | 
  'webhooksOnMessageRemovedMethod': "webhooksOnMessageRemovedMethod_example", // String | 
  'webhooksOnMessageRemovedUrl': "webhooksOnMessageRemovedUrl_example", // String | 
  'webhooksOnMessageSendMethod': "webhooksOnMessageSendMethod_example", // String | 
  'webhooksOnMessageSendUrl': "webhooksOnMessageSendUrl_example", // String | 
  'webhooksOnMessageSentMethod': "webhooksOnMessageSentMethod_example", // String | 
  'webhooksOnMessageSentUrl': "webhooksOnMessageSentUrl_example", // String | 
  'webhooksOnMessageUpdateMethod': "webhooksOnMessageUpdateMethod_example", // String | 
  'webhooksOnMessageUpdateUrl': "webhooksOnMessageUpdateUrl_example", // String | 
  'webhooksOnMessageUpdatedMethod': "webhooksOnMessageUpdatedMethod_example", // String | 
  'webhooksOnMessageUpdatedUrl': "webhooksOnMessageUpdatedUrl_example" // String | 
};
apiInstance.updateService(sid, opts, (error, data, response) => {
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
 **sid** | **String**|  | 
 **consumptionReportInterval** | **Number**|  | [optional] 
 **defaultChannelCreatorRoleSid** | **String**|  | [optional] 
 **defaultChannelRoleSid** | **String**|  | [optional] 
 **defaultServiceRoleSid** | **String**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **limitsChannelMembers** | **Number**|  | [optional] 
 **limitsUserChannels** | **Number**|  | [optional] 
 **notificationsAddedToChannelEnabled** | **Boolean**|  | [optional] 
 **notificationsAddedToChannelTemplate** | **String**|  | [optional] 
 **notificationsInvitedToChannelEnabled** | **Boolean**|  | [optional] 
 **notificationsInvitedToChannelTemplate** | **String**|  | [optional] 
 **notificationsNewMessageEnabled** | **Boolean**|  | [optional] 
 **notificationsNewMessageTemplate** | **String**|  | [optional] 
 **notificationsRemovedFromChannelEnabled** | **Boolean**|  | [optional] 
 **notificationsRemovedFromChannelTemplate** | **String**|  | [optional] 
 **postWebhookUrl** | **String**|  | [optional] 
 **preWebhookUrl** | **String**|  | [optional] 
 **reachabilityEnabled** | **Boolean**|  | [optional] 
 **readStatusEnabled** | **Boolean**|  | [optional] 
 **typingIndicatorTimeout** | **Number**|  | [optional] 
 **webhookFilters** | [**[String]**](String.md)|  | [optional] 
 **webhookMethod** | **String**|  | [optional] 
 **webhooksOnChannelAddMethod** | **String**|  | [optional] 
 **webhooksOnChannelAddUrl** | **String**|  | [optional] 
 **webhooksOnChannelAddedMethod** | **String**|  | [optional] 
 **webhooksOnChannelAddedUrl** | **String**|  | [optional] 
 **webhooksOnChannelDestroyMethod** | **String**|  | [optional] 
 **webhooksOnChannelDestroyUrl** | **String**|  | [optional] 
 **webhooksOnChannelDestroyedMethod** | **String**|  | [optional] 
 **webhooksOnChannelDestroyedUrl** | **String**|  | [optional] 
 **webhooksOnChannelUpdateMethod** | **String**|  | [optional] 
 **webhooksOnChannelUpdateUrl** | **String**|  | [optional] 
 **webhooksOnChannelUpdatedMethod** | **String**|  | [optional] 
 **webhooksOnChannelUpdatedUrl** | **String**|  | [optional] 
 **webhooksOnMemberAddMethod** | **String**|  | [optional] 
 **webhooksOnMemberAddUrl** | **String**|  | [optional] 
 **webhooksOnMemberAddedMethod** | **String**|  | [optional] 
 **webhooksOnMemberAddedUrl** | **String**|  | [optional] 
 **webhooksOnMemberRemoveMethod** | **String**|  | [optional] 
 **webhooksOnMemberRemoveUrl** | **String**|  | [optional] 
 **webhooksOnMemberRemovedMethod** | **String**|  | [optional] 
 **webhooksOnMemberRemovedUrl** | **String**|  | [optional] 
 **webhooksOnMessageRemoveMethod** | **String**|  | [optional] 
 **webhooksOnMessageRemoveUrl** | **String**|  | [optional] 
 **webhooksOnMessageRemovedMethod** | **String**|  | [optional] 
 **webhooksOnMessageRemovedUrl** | **String**|  | [optional] 
 **webhooksOnMessageSendMethod** | **String**|  | [optional] 
 **webhooksOnMessageSendUrl** | **String**|  | [optional] 
 **webhooksOnMessageSentMethod** | **String**|  | [optional] 
 **webhooksOnMessageSentUrl** | **String**|  | [optional] 
 **webhooksOnMessageUpdateMethod** | **String**|  | [optional] 
 **webhooksOnMessageUpdateUrl** | **String**|  | [optional] 
 **webhooksOnMessageUpdatedMethod** | **String**|  | [optional] 
 **webhooksOnMessageUpdatedUrl** | **String**|  | [optional] 

### Return type

[**IpMessagingV1Service**](IpMessagingV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

