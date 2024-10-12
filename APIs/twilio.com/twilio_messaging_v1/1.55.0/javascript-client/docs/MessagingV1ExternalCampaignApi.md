# TwilioMessaging.MessagingV1ExternalCampaignApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createExternalCampaign**](MessagingV1ExternalCampaignApi.md#createExternalCampaign) | **POST** /v1/Services/PreregisteredUsa2p | 



## createExternalCampaign

> MessagingV1ExternalCampaign createExternalCampaign(campaignId, messagingServiceSid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1ExternalCampaignApi();
let campaignId = "campaignId_example"; // String | ID of the preregistered campaign.
let messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) that the resource is associated with.
apiInstance.createExternalCampaign(campaignId, messagingServiceSid, (error, data, response) => {
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
 **campaignId** | **String**| ID of the preregistered campaign. | 
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) that the resource is associated with. | 

### Return type

[**MessagingV1ExternalCampaign**](MessagingV1ExternalCampaign.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

