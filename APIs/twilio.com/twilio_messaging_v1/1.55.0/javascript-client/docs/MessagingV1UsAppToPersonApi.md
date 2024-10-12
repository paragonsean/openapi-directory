# TwilioMessaging.MessagingV1UsAppToPersonApi

All URIs are relative to *https://messaging.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUsAppToPerson**](MessagingV1UsAppToPersonApi.md#createUsAppToPerson) | **POST** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p | 
[**deleteUsAppToPerson**](MessagingV1UsAppToPersonApi.md#deleteUsAppToPerson) | **DELETE** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid} | 
[**fetchUsAppToPerson**](MessagingV1UsAppToPersonApi.md#fetchUsAppToPerson) | **GET** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid} | 
[**listUsAppToPerson**](MessagingV1UsAppToPersonApi.md#listUsAppToPerson) | **GET** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p | 
[**updateUsAppToPerson**](MessagingV1UsAppToPersonApi.md#updateUsAppToPerson) | **POST** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid} | 



## createUsAppToPerson

> MessagingV1ServiceUsAppToPerson createUsAppToPerson(messagingServiceSid, brandRegistrationSid, description, hasEmbeddedLinks, hasEmbeddedPhone, messageFlow, messageSamples, usAppToPersonUsecase, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1UsAppToPersonApi();
let messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to create the resources from.
let brandRegistrationSid = "brandRegistrationSid_example"; // String | A2P Brand Registration SID
let description = "description_example"; // String | A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
let hasEmbeddedLinks = true; // Boolean | Indicates that this SMS campaign will send messages that contain links.
let hasEmbeddedPhone = true; // Boolean | Indicates that this SMS campaign will send messages that contain phone numbers.
let messageFlow = "messageFlow_example"; // String | Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
let messageSamples = ["null"]; // [String] | An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars.
let usAppToPersonUsecase = "usAppToPersonUsecase_example"; // String | A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
let opts = {
  'ageGated': true, // Boolean | A boolean that specifies whether campaign is age gated or not.
  'directLending': true, // Boolean | A boolean that specifies whether campaign allows direct lending or not.
  'helpKeywords': ["null"], // [String] | End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
  'helpMessage': "helpMessage_example", // String | When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
  'optInKeywords': ["null"], // [String] | If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
  'optInMessage': "optInMessage_example", // String | If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
  'optOutKeywords': ["null"], // [String] | End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
  'optOutMessage': "optOutMessage_example", // String | Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
  'subscriberOptIn': true // Boolean | A boolean that specifies whether campaign has Subscriber Optin or not.
};
apiInstance.createUsAppToPerson(messagingServiceSid, brandRegistrationSid, description, hasEmbeddedLinks, hasEmbeddedPhone, messageFlow, messageSamples, usAppToPersonUsecase, opts, (error, data, response) => {
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
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to create the resources from. | 
 **brandRegistrationSid** | **String**| A2P Brand Registration SID | 
 **description** | **String**| A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters. | 
 **hasEmbeddedLinks** | **Boolean**| Indicates that this SMS campaign will send messages that contain links. | 
 **hasEmbeddedPhone** | **Boolean**| Indicates that this SMS campaign will send messages that contain phone numbers. | 
 **messageFlow** | **String**| Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum. | 
 **messageSamples** | [**[String]**](String.md)| An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars. | 
 **usAppToPersonUsecase** | **String**| A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..] | 
 **ageGated** | **Boolean**| A boolean that specifies whether campaign is age gated or not. | [optional] 
 **directLending** | **Boolean**| A boolean that specifies whether campaign allows direct lending or not. | [optional] 
 **helpKeywords** | [**[String]**](String.md)| End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum. | [optional] 
 **helpMessage** | **String**| When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). 20 character minimum. 320 character maximum. | [optional] 
 **optInKeywords** | [**[String]**](String.md)| If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum. | [optional] 
 **optInMessage** | **String**| If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum. | [optional] 
 **optOutKeywords** | [**[String]**](String.md)| End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum. | [optional] 
 **optOutMessage** | **String**| Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). 20 character minimum. 320 character maximum. | [optional] 
 **subscriberOptIn** | **Boolean**| A boolean that specifies whether campaign has Subscriber Optin or not. | [optional] 

### Return type

[**MessagingV1ServiceUsAppToPerson**](MessagingV1ServiceUsAppToPerson.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteUsAppToPerson

> deleteUsAppToPerson(messagingServiceSid, sid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1UsAppToPersonApi();
let messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to delete the resource from.
let sid = "sid_example"; // String | The SID of the US A2P Compliance resource to delete `QE2c6890da8086d771620e9b13fadeba0b`.
apiInstance.deleteUsAppToPerson(messagingServiceSid, sid, (error, data, response) => {
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
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to delete the resource from. | 
 **sid** | **String**| The SID of the US A2P Compliance resource to delete &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchUsAppToPerson

> MessagingV1ServiceUsAppToPerson fetchUsAppToPerson(messagingServiceSid, sid)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1UsAppToPersonApi();
let messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.
let sid = "sid_example"; // String | The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.
apiInstance.fetchUsAppToPerson(messagingServiceSid, sid, (error, data, response) => {
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
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from. | 
 **sid** | **String**| The SID of the US A2P Compliance resource to fetch &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;. | 

### Return type

[**MessagingV1ServiceUsAppToPerson**](MessagingV1ServiceUsAppToPerson.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsAppToPerson

> ListUsAppToPersonResponse listUsAppToPerson(messagingServiceSid, opts)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1UsAppToPersonApi();
let messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUsAppToPerson(messagingServiceSid, opts, (error, data, response) => {
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
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListUsAppToPersonResponse**](ListUsAppToPersonResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUsAppToPerson

> MessagingV1ServiceUsAppToPerson updateUsAppToPerson(messagingServiceSid, sid, ageGated, description, directLending, hasEmbeddedLinks, hasEmbeddedPhone, messageFlow, messageSamples)





### Example

```javascript
import TwilioMessaging from 'twilio_messaging';
let defaultClient = TwilioMessaging.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMessaging.MessagingV1UsAppToPersonApi();
let messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to update the resource from.
let sid = "sid_example"; // String | The SID of the US A2P Compliance resource to update `QE2c6890da8086d771620e9b13fadeba0b`.
let ageGated = true; // Boolean | A boolean that specifies whether campaign requires age gate for federally legal content.
let description = "description_example"; // String | A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
let directLending = true; // Boolean | A boolean that specifies whether campaign allows direct lending or not.
let hasEmbeddedLinks = true; // Boolean | Indicates that this SMS campaign will send messages that contain links.
let hasEmbeddedPhone = true; // Boolean | Indicates that this SMS campaign will send messages that contain phone numbers.
let messageFlow = "messageFlow_example"; // String | Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
let messageSamples = ["null"]; // [String] | An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars.
apiInstance.updateUsAppToPerson(messagingServiceSid, sid, ageGated, description, directLending, hasEmbeddedLinks, hasEmbeddedPhone, messageFlow, messageSamples, (error, data, response) => {
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
 **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to update the resource from. | 
 **sid** | **String**| The SID of the US A2P Compliance resource to update &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;. | 
 **ageGated** | **Boolean**| A boolean that specifies whether campaign requires age gate for federally legal content. | 
 **description** | **String**| A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters. | 
 **directLending** | **Boolean**| A boolean that specifies whether campaign allows direct lending or not. | 
 **hasEmbeddedLinks** | **Boolean**| Indicates that this SMS campaign will send messages that contain links. | 
 **hasEmbeddedPhone** | **Boolean**| Indicates that this SMS campaign will send messages that contain phone numbers. | 
 **messageFlow** | **String**| Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum. | 
 **messageSamples** | [**[String]**](String.md)| An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars. | 

### Return type

[**MessagingV1ServiceUsAppToPerson**](MessagingV1ServiceUsAppToPerson.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

