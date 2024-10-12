# TwilioIntelligence.IntelligenceV2ServiceApi

All URIs are relative to *https://intelligence.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](IntelligenceV2ServiceApi.md#createService) | **POST** /v2/Services | 
[**deleteService**](IntelligenceV2ServiceApi.md#deleteService) | **DELETE** /v2/Services/{Sid} | 
[**fetchService**](IntelligenceV2ServiceApi.md#fetchService) | **GET** /v2/Services/{Sid} | 
[**listService**](IntelligenceV2ServiceApi.md#listService) | **GET** /v2/Services | 
[**updateService**](IntelligenceV2ServiceApi.md#updateService) | **POST** /v2/Services/{Sid} | 



## createService

> IntelligenceV2Service createService(uniqueName, opts)



Create a new Service for the given Account

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2ServiceApi();
let uniqueName = "uniqueName_example"; // String | Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
let opts = {
  'autoRedaction': true, // Boolean | Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
  'autoTranscribe': true, // Boolean | Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
  'dataLogging': true, // Boolean | Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
  'friendlyName': "friendlyName_example", // String | A human readable description of this resource, up to 64 characters.
  'languageCode': "languageCode_example", // String | The default language code of the audio.
  'mediaRedaction': true, // Boolean | Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
  'webhookHttpMethod': "webhookHttpMethod_example", // ServiceEnumHttpMethod | 
  'webhookUrl': "webhookUrl_example" // String | The URL Twilio will request when executing the Webhook.
};
apiInstance.createService(uniqueName, opts, (error, data, response) => {
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
 **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID. | 
 **autoRedaction** | **Boolean**| Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service. | [optional] 
 **autoTranscribe** | **Boolean**| Instructs the Speech Recognition service to automatically transcribe all recordings made on the account. | [optional] 
 **dataLogging** | **Boolean**| Data logging allows Twilio to improve the quality of the speech recognition &amp; language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent. | [optional] 
 **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] 
 **languageCode** | **String**| The default language code of the audio. | [optional] 
 **mediaRedaction** | **Boolean**| Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise. | [optional] 
 **webhookHttpMethod** | **ServiceEnumHttpMethod**|  | [optional] 
 **webhookUrl** | **String**| The URL Twilio will request when executing the Webhook. | [optional] 

### Return type

[**IntelligenceV2Service**](IntelligenceV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteService

> deleteService(sid)



Delete a specific Service.

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2ServiceApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Service.
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
 **sid** | **String**| A 34 character string that uniquely identifies this Service. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchService

> IntelligenceV2Service fetchService(sid)



Fetch a specific Service.

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2ServiceApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Service.
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
 **sid** | **String**| A 34 character string that uniquely identifies this Service. | 

### Return type

[**IntelligenceV2Service**](IntelligenceV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listService

> ListServiceResponse listService(opts)



Retrieves a list of all Services for an account.

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2ServiceApi();
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

> IntelligenceV2Service updateService(sid, opts)



Update a specific Service.

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2ServiceApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Service.
let opts = {
  'ifMatch': "ifMatch_example", // String | The If-Match HTTP request header
  'autoRedaction': true, // Boolean | Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
  'autoTranscribe': true, // Boolean | Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
  'dataLogging': true, // Boolean | Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
  'friendlyName': "friendlyName_example", // String | A human readable description of this resource, up to 64 characters.
  'languageCode': "languageCode_example", // String | The default language code of the audio.
  'mediaRedaction': true, // Boolean | Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
  'uniqueName': "uniqueName_example", // String | Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
  'webhookHttpMethod': "webhookHttpMethod_example", // ServiceEnumHttpMethod | 
  'webhookUrl': "webhookUrl_example" // String | The URL Twilio will request when executing the Webhook.
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
 **sid** | **String**| A 34 character string that uniquely identifies this Service. | 
 **ifMatch** | **String**| The If-Match HTTP request header | [optional] 
 **autoRedaction** | **Boolean**| Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service. | [optional] 
 **autoTranscribe** | **Boolean**| Instructs the Speech Recognition service to automatically transcribe all recordings made on the account. | [optional] 
 **dataLogging** | **Boolean**| Data logging allows Twilio to improve the quality of the speech recognition &amp; language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent. | [optional] 
 **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] 
 **languageCode** | **String**| The default language code of the audio. | [optional] 
 **mediaRedaction** | **Boolean**| Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise. | [optional] 
 **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID. | [optional] 
 **webhookHttpMethod** | **ServiceEnumHttpMethod**|  | [optional] 
 **webhookUrl** | **String**| The URL Twilio will request when executing the Webhook. | [optional] 

### Return type

[**IntelligenceV2Service**](IntelligenceV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

