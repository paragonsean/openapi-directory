# TwilioMessaging.MessagingV1LinkshorteningMessagingServiceDomainAssociationApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchLinkshorteningMessagingServiceDomainAssociation**](MessagingV1LinkshorteningMessagingServiceDomainAssociationApi.md#fetchLinkshorteningMessagingServiceDomainAssociation) | **GET** /v1/LinkShortening/MessagingServices/{MessagingServiceSid}/Domain | 



## fetchLinkshorteningMessagingServiceDomainAssociation

> MessagingV1LinkshorteningMessagingServiceDomainAssociation fetchLinkshorteningMessagingServiceDomainAssociation(messagingServiceSid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1LinkshorteningMessagingServiceDomainAssociationApi();
let messagingServiceSid = "messagingServiceSid_example"; // String | Unique string used to identify the Messaging service that this domain should be associated with.
apiInstance.fetchLinkshorteningMessagingServiceDomainAssociation(messagingServiceSid, (error, data, response) => {
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
 **messagingServiceSid** | **String**| Unique string used to identify the Messaging service that this domain should be associated with. | 

### Return type

[**MessagingV1LinkshorteningMessagingServiceDomainAssociation**](MessagingV1LinkshorteningMessagingServiceDomainAssociation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

