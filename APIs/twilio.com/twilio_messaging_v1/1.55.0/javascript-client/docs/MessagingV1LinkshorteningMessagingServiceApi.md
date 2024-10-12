# TwilioMessaging.MessagingV1LinkshorteningMessagingServiceApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLinkshorteningMessagingService**](MessagingV1LinkshorteningMessagingServiceApi.md#createLinkshorteningMessagingService) | **POST** /v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid} | 
[**deleteLinkshorteningMessagingService**](MessagingV1LinkshorteningMessagingServiceApi.md#deleteLinkshorteningMessagingService) | **DELETE** /v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid} | 



## createLinkshorteningMessagingService

> MessagingV1LinkshorteningMessagingService createLinkshorteningMessagingService(domainSid, messagingServiceSid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1LinkshorteningMessagingServiceApi();
let domainSid = "domainSid_example"; // String | The domain SID to associate with a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
let messagingServiceSid = "messagingServiceSid_example"; // String | A messaging service SID to associate with a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
apiInstance.createLinkshorteningMessagingService(domainSid, messagingServiceSid, (error, data, response) => {
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
 **domainSid** | **String**| The domain SID to associate with a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain | 
 **messagingServiceSid** | **String**| A messaging service SID to associate with a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain | 

### Return type

[**MessagingV1LinkshorteningMessagingService**](MessagingV1LinkshorteningMessagingService.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLinkshorteningMessagingService

> deleteLinkshorteningMessagingService(domainSid, messagingServiceSid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1LinkshorteningMessagingServiceApi();
let domainSid = "domainSid_example"; // String | The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
let messagingServiceSid = "messagingServiceSid_example"; // String | A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
apiInstance.deleteLinkshorteningMessagingService(domainSid, messagingServiceSid, (error, data, response) => {
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
 **domainSid** | **String**| The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain | 
 **messagingServiceSid** | **String**| A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

