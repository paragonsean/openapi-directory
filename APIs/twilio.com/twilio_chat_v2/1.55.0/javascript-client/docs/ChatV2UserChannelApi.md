# TwilioChat.ChatV2UserChannelApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserChannel**](ChatV2UserChannelApi.md#deleteUserChannel) | **DELETE** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels/{ChannelSid} | 
[**fetchUserChannel**](ChatV2UserChannelApi.md#fetchUserChannel) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels/{ChannelSid} | 
[**listUserChannel**](ChatV2UserChannelApi.md#listUserChannel) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels | 
[**updateUserChannel**](ChatV2UserChannelApi.md#updateUserChannel) | **POST** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels/{ChannelSid} | 



## deleteUserChannel

> deleteUserChannel(serviceSid, userSid, channelSid, opts)



Removes User from selected Channel.

### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2UserChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
let userSid = "userSid_example"; // String | The SID of the [User](https://www.twilio.com/docs/api/chat/rest/users) to read the User Channel resources from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource belongs to.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // UserChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteUserChannel(serviceSid, userSid, channelSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from. | 
 **userSid** | **String**| The SID of the [User](https://www.twilio.com/docs/api/chat/rest/users) to read the User Channel resources from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource belongs to. | 
 **xTwilioWebhookEnabled** | **UserChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchUserChannel

> ChatV2ServiceUserUserChannel fetchUserChannel(serviceSid, userSid, channelSid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2UserChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the User Channel resource from.
let userSid = "userSid_example"; // String | The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) to fetch the User Channel resource from. This value can be either the `sid` or the `identity` of the User resource.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) that has the User Channel to fetch. This value can be either the `sid` or the `unique_name` of the Channel to fetch.
apiInstance.fetchUserChannel(serviceSid, userSid, channelSid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the User Channel resource from. | 
 **userSid** | **String**| The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) to fetch the User Channel resource from. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) that has the User Channel to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel to fetch. | 

### Return type

[**ChatV2ServiceUserUserChannel**](ChatV2ServiceUserUserChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUserChannel

> ListUserChannelResponse listUserChannel(serviceSid, userSid, opts)



List all Channels for a given User.

### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2UserChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the User Channel resources from.
let userSid = "userSid_example"; // String | The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) to read the User Channel resources from. This value can be either the `sid` or the `identity` of the User resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUserChannel(serviceSid, userSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the User Channel resources from. | 
 **userSid** | **String**| The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) to read the User Channel resources from. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListUserChannelResponse**](ListUserChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUserChannel

> ChatV2ServiceUserUserChannel updateUserChannel(serviceSid, userSid, channelSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2UserChannelApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the User Channel resource in.
let userSid = "userSid_example"; // String | The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) to update the User Channel resource from. This value can be either the `sid` or the `identity` of the User resource.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) with the User Channel resource to update. This value can be the Channel resource's `sid` or `unique_name`.
let opts = {
  'lastConsumedMessageIndex': 56, // Number | The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) in the [Channel](https://www.twilio.com/docs/chat/channels) that the Member has read.
  'lastConsumptionTimestamp': new Date("2013-10-20T19:20:30+01:00"), // Date | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels).
  'notificationLevel': "notificationLevel_example" // UserChannelEnumNotificationLevel | 
};
apiInstance.updateUserChannel(serviceSid, userSid, channelSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the User Channel resource in. | 
 **userSid** | **String**| The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) to update the User Channel resource from. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) with the User Channel resource to update. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **lastConsumedMessageIndex** | **Number**| The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) in the [Channel](https://www.twilio.com/docs/chat/channels) that the Member has read. | [optional] 
 **lastConsumptionTimestamp** | **Date**| The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels). | [optional] 
 **notificationLevel** | **UserChannelEnumNotificationLevel**|  | [optional] 

### Return type

[**ChatV2ServiceUserUserChannel**](ChatV2ServiceUserUserChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

