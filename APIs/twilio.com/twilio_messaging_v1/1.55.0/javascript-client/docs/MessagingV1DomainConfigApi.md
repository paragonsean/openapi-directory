# TwilioMessaging.MessagingV1DomainConfigApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchDomainConfig**](MessagingV1DomainConfigApi.md#fetchDomainConfig) | **GET** /v1/LinkShortening/Domains/{DomainSid}/Config | 
[**updateDomainConfig**](MessagingV1DomainConfigApi.md#updateDomainConfig) | **POST** /v1/LinkShortening/Domains/{DomainSid}/Config | 



## fetchDomainConfig

> MessagingV1DomainConfig fetchDomainConfig(domainSid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1DomainConfigApi();
let domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this config should be associated with.
apiInstance.fetchDomainConfig(domainSid, (error, data, response) => {
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
 **domainSid** | **String**| Unique string used to identify the domain that this config should be associated with. | 

### Return type

[**MessagingV1DomainConfig**](MessagingV1DomainConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDomainConfig

> MessagingV1DomainConfig updateDomainConfig(domainSid, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1DomainConfigApi();
let domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this config should be associated with.
let opts = {
  'callbackUrl': "callbackUrl_example", // String | URL to receive click events to your webhook whenever the recipients click on the shortened links
  'continueOnFailure': true, // Boolean | Boolean field to set customer delivery preference when there is a failure in linkShortening service
  'disableHttps': true, // Boolean | Customer's choice to send links with/without \\\"https://\\\" attached to shortened url. If true, messages will not be sent with https:// at the beginning of the url. If false, messages will be sent with https:// at the beginning of the url. False is the default behavior if it is not specified.
  'fallbackUrl': "fallbackUrl_example" // String | Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping.
};
apiInstance.updateDomainConfig(domainSid, opts, (error, data, response) => {
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
 **domainSid** | **String**| Unique string used to identify the domain that this config should be associated with. | 
 **callbackUrl** | **String**| URL to receive click events to your webhook whenever the recipients click on the shortened links | [optional] 
 **continueOnFailure** | **Boolean**| Boolean field to set customer delivery preference when there is a failure in linkShortening service | [optional] 
 **disableHttps** | **Boolean**| Customer&#39;s choice to send links with/without \\\&quot;https://\\\&quot; attached to shortened url. If true, messages will not be sent with https:// at the beginning of the url. If false, messages will be sent with https:// at the beginning of the url. False is the default behavior if it is not specified. | [optional] 
 **fallbackUrl** | **String**| Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping. | [optional] 

### Return type

[**MessagingV1DomainConfig**](MessagingV1DomainConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

