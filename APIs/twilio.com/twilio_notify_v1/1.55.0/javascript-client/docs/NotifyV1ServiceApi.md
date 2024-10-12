# TwilioNotify.NotifyV1ServiceApi

All URIs are relative to *https://notify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](NotifyV1ServiceApi.md#createService) | **POST** /v1/Services | 
[**deleteService**](NotifyV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} | 
[**fetchService**](NotifyV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} | 
[**listService**](NotifyV1ServiceApi.md#listService) | **GET** /v1/Services | 
[**updateService**](NotifyV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} | 



## createService

> NotifyV1Service createService(opts)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1ServiceApi();
let opts = {
  'alexaSkillId': "alexaSkillId_example", // String | Deprecated.
  'apnCredentialSid': "apnCredentialSid_example", // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings.
  'defaultAlexaNotificationProtocolVersion': "defaultAlexaNotificationProtocolVersion_example", // String | Deprecated.
  'defaultApnNotificationProtocolVersion': "defaultApnNotificationProtocolVersion_example", // String | The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
  'defaultFcmNotificationProtocolVersion': "defaultFcmNotificationProtocolVersion_example", // String | The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
  'defaultGcmNotificationProtocolVersion': "defaultGcmNotificationProtocolVersion_example", // String | The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
  'deliveryCallbackEnabled': true, // Boolean | Callback configuration that enables delivery callbacks, default false
  'deliveryCallbackUrl': "deliveryCallbackUrl_example", // String | URL to send delivery status callback.
  'facebookMessengerPageId': "facebookMessengerPageId_example", // String | Deprecated.
  'fcmCredentialSid': "fcmCredentialSid_example", // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'gcmCredentialSid': "gcmCredentialSid_example", // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings.
  'logEnabled': true, // Boolean | Whether to log notifications. Can be: `true` or `false` and the default is `true`.
  'messagingServiceSid': "messagingServiceSid_example" // String | The SID of the [Messaging Service](https://www.twilio.com/docs/sms/quickstart#messaging-services) to use for SMS Bindings. This parameter must be set in order to send SMS notifications.
};
apiInstance.createService(opts, (error, data, response) => {
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
 **alexaSkillId** | **String**| Deprecated. | [optional] 
 **apnCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings. | [optional] 
 **defaultAlexaNotificationProtocolVersion** | **String**| Deprecated. | [optional] 
 **defaultApnNotificationProtocolVersion** | **String**| The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] 
 **defaultFcmNotificationProtocolVersion** | **String**| The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] 
 **defaultGcmNotificationProtocolVersion** | **String**| The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] 
 **deliveryCallbackEnabled** | **Boolean**| Callback configuration that enables delivery callbacks, default false | [optional] 
 **deliveryCallbackUrl** | **String**| URL to send delivery status callback. | [optional] 
 **facebookMessengerPageId** | **String**| Deprecated. | [optional] 
 **fcmCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **gcmCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings. | [optional] 
 **logEnabled** | **Boolean**| Whether to log notifications. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] 
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/sms/quickstart#messaging-services) to use for SMS Bindings. This parameter must be set in order to send SMS notifications. | [optional] 

### Return type

[**NotifyV1Service**](NotifyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteService

> deleteService(sid)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to delete.
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchService

> NotifyV1Service fetchService(sid)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to fetch.
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to fetch. | 

### Return type

[**NotifyV1Service**](NotifyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listService

> ListServiceResponse listService(opts)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1ServiceApi();
let opts = {
  'friendlyName': "friendlyName_example", // String | The string that identifies the Service resources to read.
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
 **friendlyName** | **String**| The string that identifies the Service resources to read. | [optional] 
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

> NotifyV1Service updateService(sid, opts)





### Example

```javascript
import TwilioNotify from 'twilio_notify';
let defaultClient = TwilioNotify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNotify.NotifyV1ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to update.
let opts = {
  'alexaSkillId': "alexaSkillId_example", // String | Deprecated.
  'apnCredentialSid': "apnCredentialSid_example", // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings.
  'defaultAlexaNotificationProtocolVersion': "defaultAlexaNotificationProtocolVersion_example", // String | Deprecated.
  'defaultApnNotificationProtocolVersion': "defaultApnNotificationProtocolVersion_example", // String | The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
  'defaultFcmNotificationProtocolVersion': "defaultFcmNotificationProtocolVersion_example", // String | The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
  'defaultGcmNotificationProtocolVersion': "defaultGcmNotificationProtocolVersion_example", // String | The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource.
  'deliveryCallbackEnabled': true, // Boolean | Callback configuration that enables delivery callbacks, default false
  'deliveryCallbackUrl': "deliveryCallbackUrl_example", // String | URL to send delivery status callback.
  'facebookMessengerPageId': "facebookMessengerPageId_example", // String | Deprecated.
  'fcmCredentialSid': "fcmCredentialSid_example", // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'gcmCredentialSid': "gcmCredentialSid_example", // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings.
  'logEnabled': true, // Boolean | Whether to log notifications. Can be: `true` or `false` and the default is `true`.
  'messagingServiceSid': "messagingServiceSid_example" // String | The SID of the [Messaging Service](https://www.twilio.com/docs/sms/quickstart#messaging-services) to use for SMS Bindings. This parameter must be set in order to send SMS notifications.
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to update. | 
 **alexaSkillId** | **String**| Deprecated. | [optional] 
 **apnCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for APN Bindings. | [optional] 
 **defaultAlexaNotificationProtocolVersion** | **String**| Deprecated. | [optional] 
 **defaultApnNotificationProtocolVersion** | **String**| The protocol version to use for sending APNS notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] 
 **defaultFcmNotificationProtocolVersion** | **String**| The protocol version to use for sending FCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] 
 **defaultGcmNotificationProtocolVersion** | **String**| The protocol version to use for sending GCM notifications. Can be overridden on a Binding by Binding basis when creating a [Binding](https://www.twilio.com/docs/notify/api/binding-resource) resource. | [optional] 
 **deliveryCallbackEnabled** | **Boolean**| Callback configuration that enables delivery callbacks, default false | [optional] 
 **deliveryCallbackUrl** | **String**| URL to send delivery status callback. | [optional] 
 **facebookMessengerPageId** | **String**| Deprecated. | [optional] 
 **fcmCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for FCM Bindings. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **gcmCredentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) to use for GCM Bindings. | [optional] 
 **logEnabled** | **Boolean**| Whether to log notifications. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] 
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/sms/quickstart#messaging-services) to use for SMS Bindings. This parameter must be set in order to send SMS notifications. | [optional] 

### Return type

[**NotifyV1Service**](NotifyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

