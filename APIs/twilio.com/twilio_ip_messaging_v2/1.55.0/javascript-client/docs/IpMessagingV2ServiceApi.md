# TwilioIpMessaging.IpMessagingV2ServiceApi

All URIs are relative to *https://ip-messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](IpMessagingV2ServiceApi.md#createService) | **POST** /v2/Services | 
[**deleteService**](IpMessagingV2ServiceApi.md#deleteService) | **DELETE** /v2/Services/{Sid} | 
[**fetchService**](IpMessagingV2ServiceApi.md#fetchService) | **GET** /v2/Services/{Sid} | 
[**listService**](IpMessagingV2ServiceApi.md#listService) | **GET** /v2/Services | 
[**updateService**](IpMessagingV2ServiceApi.md#updateService) | **POST** /v2/Services/{Sid} | 



## createService

> IpMessagingV2Service createService(friendlyName)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2ServiceApi();
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

[**IpMessagingV2Service**](IpMessagingV2Service.md)

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

let apiInstance = new TwilioIpMessaging.IpMessagingV2ServiceApi();
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

> IpMessagingV2Service fetchService(sid)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2ServiceApi();
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

[**IpMessagingV2Service**](IpMessagingV2Service.md)

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

let apiInstance = new TwilioIpMessaging.IpMessagingV2ServiceApi();
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

> IpMessagingV2Service updateService(sid, opts)





### Example

```javascript
import TwilioIpMessaging from 'twilio_ip_messaging';
let defaultClient = TwilioIpMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIpMessaging.IpMessagingV2ServiceApi();
let sid = "sid_example"; // String | 
let opts = {
  'consumptionReportInterval': 56, // Number | 
  'defaultChannelCreatorRoleSid': "defaultChannelCreatorRoleSid_example", // String | 
  'defaultChannelRoleSid': "defaultChannelRoleSid_example", // String | 
  'defaultServiceRoleSid': "defaultServiceRoleSid_example", // String | 
  'friendlyName': "friendlyName_example", // String | 
  'limitsChannelMembers': 56, // Number | 
  'limitsUserChannels': 56, // Number | 
  'mediaCompatibilityMessage': "mediaCompatibilityMessage_example", // String | 
  'notificationsAddedToChannelEnabled': true, // Boolean | 
  'notificationsAddedToChannelSound': "notificationsAddedToChannelSound_example", // String | 
  'notificationsAddedToChannelTemplate': "notificationsAddedToChannelTemplate_example", // String | 
  'notificationsInvitedToChannelEnabled': true, // Boolean | 
  'notificationsInvitedToChannelSound': "notificationsInvitedToChannelSound_example", // String | 
  'notificationsInvitedToChannelTemplate': "notificationsInvitedToChannelTemplate_example", // String | 
  'notificationsLogEnabled': true, // Boolean | 
  'notificationsNewMessageBadgeCountEnabled': true, // Boolean | 
  'notificationsNewMessageEnabled': true, // Boolean | 
  'notificationsNewMessageSound': "notificationsNewMessageSound_example", // String | 
  'notificationsNewMessageTemplate': "notificationsNewMessageTemplate_example", // String | 
  'notificationsRemovedFromChannelEnabled': true, // Boolean | 
  'notificationsRemovedFromChannelSound': "notificationsRemovedFromChannelSound_example", // String | 
  'notificationsRemovedFromChannelTemplate': "notificationsRemovedFromChannelTemplate_example", // String | 
  'postWebhookRetryCount': 56, // Number | 
  'postWebhookUrl': "postWebhookUrl_example", // String | 
  'preWebhookRetryCount': 56, // Number | 
  'preWebhookUrl': "preWebhookUrl_example", // String | 
  'reachabilityEnabled': true, // Boolean | 
  'readStatusEnabled': true, // Boolean | 
  'typingIndicatorTimeout': 56, // Number | 
  'webhookFilters': ["null"], // [String] | 
  'webhookMethod': "webhookMethod_example" // String | 
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
 **mediaCompatibilityMessage** | **String**|  | [optional] 
 **notificationsAddedToChannelEnabled** | **Boolean**|  | [optional] 
 **notificationsAddedToChannelSound** | **String**|  | [optional] 
 **notificationsAddedToChannelTemplate** | **String**|  | [optional] 
 **notificationsInvitedToChannelEnabled** | **Boolean**|  | [optional] 
 **notificationsInvitedToChannelSound** | **String**|  | [optional] 
 **notificationsInvitedToChannelTemplate** | **String**|  | [optional] 
 **notificationsLogEnabled** | **Boolean**|  | [optional] 
 **notificationsNewMessageBadgeCountEnabled** | **Boolean**|  | [optional] 
 **notificationsNewMessageEnabled** | **Boolean**|  | [optional] 
 **notificationsNewMessageSound** | **String**|  | [optional] 
 **notificationsNewMessageTemplate** | **String**|  | [optional] 
 **notificationsRemovedFromChannelEnabled** | **Boolean**|  | [optional] 
 **notificationsRemovedFromChannelSound** | **String**|  | [optional] 
 **notificationsRemovedFromChannelTemplate** | **String**|  | [optional] 
 **postWebhookRetryCount** | **Number**|  | [optional] 
 **postWebhookUrl** | **String**|  | [optional] 
 **preWebhookRetryCount** | **Number**|  | [optional] 
 **preWebhookUrl** | **String**|  | [optional] 
 **reachabilityEnabled** | **Boolean**|  | [optional] 
 **readStatusEnabled** | **Boolean**|  | [optional] 
 **typingIndicatorTimeout** | **Number**|  | [optional] 
 **webhookFilters** | [**[String]**](String.md)|  | [optional] 
 **webhookMethod** | **String**|  | [optional] 

### Return type

[**IpMessagingV2Service**](IpMessagingV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

