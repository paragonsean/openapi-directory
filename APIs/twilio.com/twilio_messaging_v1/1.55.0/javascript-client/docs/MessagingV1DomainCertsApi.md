# TwilioMessaging.MessagingV1DomainCertsApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDomainCertV4**](MessagingV1DomainCertsApi.md#deleteDomainCertV4) | **DELETE** /v1/LinkShortening/Domains/{DomainSid}/Certificate | 
[**fetchDomainCertV4**](MessagingV1DomainCertsApi.md#fetchDomainCertV4) | **GET** /v1/LinkShortening/Domains/{DomainSid}/Certificate | 
[**updateDomainCertV4**](MessagingV1DomainCertsApi.md#updateDomainCertV4) | **POST** /v1/LinkShortening/Domains/{DomainSid}/Certificate | 



## deleteDomainCertV4

> deleteDomainCertV4(domainSid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1DomainCertsApi();
let domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this certificate should be associated with.
apiInstance.deleteDomainCertV4(domainSid, (error, data, response) => {
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
 **domainSid** | **String**| Unique string used to identify the domain that this certificate should be associated with. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchDomainCertV4

> MessagingV1DomainCertV4 fetchDomainCertV4(domainSid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1DomainCertsApi();
let domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this certificate should be associated with.
apiInstance.fetchDomainCertV4(domainSid, (error, data, response) => {
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
 **domainSid** | **String**| Unique string used to identify the domain that this certificate should be associated with. | 

### Return type

[**MessagingV1DomainCertV4**](MessagingV1DomainCertV4.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDomainCertV4

> MessagingV1DomainCertV4 updateDomainCertV4(domainSid, tlsCert)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1DomainCertsApi();
let domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this certificate should be associated with.
let tlsCert = "tlsCert_example"; // String | Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.
apiInstance.updateDomainCertV4(domainSid, tlsCert, (error, data, response) => {
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
 **domainSid** | **String**| Unique string used to identify the domain that this certificate should be associated with. | 
 **tlsCert** | **String**| Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain. | 

### Return type

[**MessagingV1DomainCertV4**](MessagingV1DomainCertV4.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

