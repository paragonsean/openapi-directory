# TwilioVerify.VerifyV2WebhookApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWebhook**](VerifyV2WebhookApi.md#createWebhook) | **POST** /v2/Services/{ServiceSid}/Webhooks | 
[**deleteWebhook**](VerifyV2WebhookApi.md#deleteWebhook) | **DELETE** /v2/Services/{ServiceSid}/Webhooks/{Sid} | 
[**fetchWebhook**](VerifyV2WebhookApi.md#fetchWebhook) | **GET** /v2/Services/{ServiceSid}/Webhooks/{Sid} | 
[**listWebhook**](VerifyV2WebhookApi.md#listWebhook) | **GET** /v2/Services/{ServiceSid}/Webhooks | 
[**updateWebhook**](VerifyV2WebhookApi.md#updateWebhook) | **POST** /v2/Services/{ServiceSid}/Webhooks/{Sid} | 



## createWebhook

> VerifyV2ServiceWebhook createWebhook(serviceSid, eventTypes, friendlyName, webhookUrl, opts)



Create a new Webhook for the Service

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
let eventTypes = ["null"]; // [String] | The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
let friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the webhook. **This value should not contain PII.**
let webhookUrl = "webhookUrl_example"; // String | The URL associated with this Webhook.
let opts = {
  'status': "status_example", // WebhookEnumStatus | 
  'version': "version_example" // WebhookEnumVersion | 
};
apiInstance.createWebhook(serviceSid, eventTypes, friendlyName, webhookUrl, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The unique SID identifier of the Service. | 
 **eventTypes** | [**[String]**](String.md)| The array of events that this Webhook is subscribed to. Possible event types: &#x60;*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied&#x60; | 
 **friendlyName** | **String**| The string that you assigned to describe the webhook. **This value should not contain PII.** | 
 **webhookUrl** | **String**| The URL associated with this Webhook. | 
 **status** | **WebhookEnumStatus**|  | [optional] 
 **version** | **WebhookEnumVersion**|  | [optional] 

### Return type

[**VerifyV2ServiceWebhook**](VerifyV2ServiceWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteWebhook

> deleteWebhook(serviceSid, sid)



Delete a specific Webhook.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Webhook resource to delete.
apiInstance.deleteWebhook(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The unique SID identifier of the Service. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Webhook resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchWebhook

> VerifyV2ServiceWebhook fetchWebhook(serviceSid, sid)



Fetch a specific Webhook.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Webhook resource to fetch.
apiInstance.fetchWebhook(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The unique SID identifier of the Service. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Webhook resource to fetch. | 

### Return type

[**VerifyV2ServiceWebhook**](VerifyV2ServiceWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWebhook

> ListWebhookResponse listWebhook(serviceSid, opts)



Retrieve a list of all Webhooks for a Service.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWebhook(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The unique SID identifier of the Service. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListWebhookResponse**](ListWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWebhook

> VerifyV2ServiceWebhook updateWebhook(serviceSid, sid, opts)





### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Webhook resource to update.
let opts = {
  'eventTypes': ["null"], // [String] | The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the webhook. **This value should not contain PII.**
  'status': "status_example", // WebhookEnumStatus | 
  'version': "version_example", // WebhookEnumVersion | 
  'webhookUrl': "webhookUrl_example" // String | The URL associated with this Webhook.
};
apiInstance.updateWebhook(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The unique SID identifier of the Service. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Webhook resource to update. | 
 **eventTypes** | [**[String]**](String.md)| The array of events that this Webhook is subscribed to. Possible event types: &#x60;*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied&#x60; | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the webhook. **This value should not contain PII.** | [optional] 
 **status** | **WebhookEnumStatus**|  | [optional] 
 **version** | **WebhookEnumVersion**|  | [optional] 
 **webhookUrl** | **String**| The URL associated with this Webhook. | [optional] 

### Return type

[**VerifyV2ServiceWebhook**](VerifyV2ServiceWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

