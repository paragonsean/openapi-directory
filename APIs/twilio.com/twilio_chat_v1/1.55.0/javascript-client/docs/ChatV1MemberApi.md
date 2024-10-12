# TwilioChat.ChatV1MemberApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMember**](ChatV1MemberApi.md#createMember) | **POST** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Members | 
[**deleteMember**](ChatV1MemberApi.md#deleteMember) | **DELETE** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} | 
[**fetchMember**](ChatV1MemberApi.md#fetchMember) | **GET** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} | 
[**listMember**](ChatV1MemberApi.md#listMember) | **GET** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Members | 
[**updateMember**](ChatV1MemberApi.md#updateMember) | **POST** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} | 



## createMember

> ChatV1ServiceChannelMember createMember(serviceSid, channelSid, identity, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1MemberApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under.
let channelSid = "channelSid_example"; // String | The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the new member belongs to. Can be the Channel resource's `sid` or `unique_name`.
let identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/services). See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details.
let opts = {
  'roleSid': "roleSid_example" // String | The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/api/services).
};
apiInstance.createMember(serviceSid, channelSid, identity, opts, (error, data, response) => {
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
 **channelSid** | **String**| The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the new member belongs to. Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/services). See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details. | 
 **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/api/services). | [optional] 

### Return type

[**ChatV1ServiceChannelMember**](ChatV1ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteMember

> deleteMember(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1MemberApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from.
let channelSid = "channelSid_example"; // String | The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the message belongs to.  Can be the Channel's `sid` or `unique_name`.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Member resource to delete.
apiInstance.deleteMember(serviceSid, channelSid, sid, (error, data, response) => {
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
 **channelSid** | **String**| The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the message belongs to.  Can be the Channel&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Member resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchMember

> ChatV1ServiceChannelMember fetchMember(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1MemberApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.
let channelSid = "channelSid_example"; // String | The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the member to fetch belongs to. Can be the Channel resource's `sid` or `unique_name` value.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Member resource to fetch.
apiInstance.fetchMember(serviceSid, channelSid, sid, (error, data, response) => {
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
 **channelSid** | **String**| The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the member to fetch belongs to. Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60; value. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Member resource to fetch. | 

### Return type

[**ChatV1ServiceChannelMember**](ChatV1ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMember

> ListMemberResponse listMember(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1MemberApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
let channelSid = "channelSid_example"; // String | The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the members to read belong to. Can be the Channel resource's `sid` or `unique_name` value.
let opts = {
  'identity': ["null"], // [String] | The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)'s `identity` value of the resources to read. See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMember(serviceSid, channelSid, opts, (error, data, response) => {
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
 **channelSid** | **String**| The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the members to read belong to. Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60; value. | 
 **identity** | [**[String]**](String.md)| The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)&#39;s &#x60;identity&#x60; value of the resources to read. See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMemberResponse**](ListMemberResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMember

> ChatV1ServiceChannelMember updateMember(serviceSid, channelSid, sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1MemberApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from.
let channelSid = "channelSid_example"; // String | The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the member to update belongs to. Can be the Channel resource's `sid` or `unique_name`.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Member resource to update.
let opts = {
  'lastConsumedMessageIndex': 56, // Number | The index of the last [Message](https://www.twilio.com/docs/api/chat/rest/messages) that the Member has read within the [Channel](https://www.twilio.com/docs/api/chat/rest/channels).
  'roleSid': "roleSid_example" // String | The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/api/services).
};
apiInstance.updateMember(serviceSid, channelSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from. | 
 **channelSid** | **String**| The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the member to update belongs to. Can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Member resource to update. | 
 **lastConsumedMessageIndex** | **Number**| The index of the last [Message](https://www.twilio.com/docs/api/chat/rest/messages) that the Member has read within the [Channel](https://www.twilio.com/docs/api/chat/rest/channels). | [optional] 
 **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/api/services). | [optional] 

### Return type

[**ChatV1ServiceChannelMember**](ChatV1ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

