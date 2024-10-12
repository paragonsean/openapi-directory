# TwilioChat.ChatV1InviteApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInvite**](ChatV1InviteApi.md#createInvite) | **POST** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Invites | 
[**deleteInvite**](ChatV1InviteApi.md#deleteInvite) | **DELETE** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Invites/{Sid} | 
[**fetchInvite**](ChatV1InviteApi.md#fetchInvite) | **GET** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Invites/{Sid} | 
[**listInvite**](ChatV1InviteApi.md#listInvite) | **GET** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Invites | 



## createInvite

> ChatV1ServiceChannelInvite createInvite(serviceSid, channelSid, identity, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1InviteApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the new resource belongs to.
let identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/v1/service). See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more info.
let opts = {
  'roleSid': "roleSid_example" // String | The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the new member.
};
apiInstance.createInvite(serviceSid, channelSid, identity, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the new resource belongs to. | 
 **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/v1/service). See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more info. | 
 **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the new member. | [optional] 

### Return type

[**ChatV1ServiceChannelInvite**](ChatV1ServiceChannelInvite.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteInvite

> deleteInvite(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1InviteApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource to delete belongs to.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Invite resource to delete.
apiInstance.deleteInvite(serviceSid, channelSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource to delete belongs to. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Invite resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchInvite

> ChatV1ServiceChannelInvite fetchInvite(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1InviteApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource to fetch belongs to.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Invite resource to fetch.
apiInstance.fetchInvite(serviceSid, channelSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource to fetch belongs to. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Invite resource to fetch. | 

### Return type

[**ChatV1ServiceChannelInvite**](ChatV1ServiceChannelInvite.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInvite

> ListInviteResponse listInvite(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1InviteApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resources to read belong to.
let opts = {
  'identity': ["null"], // [String] | The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)'s `identity` value of the resources to read. See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInvite(serviceSid, channelSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resources to read belong to. | 
 **identity** | [**[String]**](String.md)| The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)&#39;s &#x60;identity&#x60; value of the resources to read. See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInviteResponse**](ListInviteResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

