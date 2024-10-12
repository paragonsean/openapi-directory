# TwilioConversations.ConversationsV1UserApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createServiceUser**](ConversationsV1UserApi.md#createServiceUser) | **POST** /v1/Services/{ChatServiceSid}/Users | 
[**createUser**](ConversationsV1UserApi.md#createUser) | **POST** /v1/Users | 
[**deleteServiceUser**](ConversationsV1UserApi.md#deleteServiceUser) | **DELETE** /v1/Services/{ChatServiceSid}/Users/{Sid} | 
[**deleteUser**](ConversationsV1UserApi.md#deleteUser) | **DELETE** /v1/Users/{Sid} | 
[**fetchServiceUser**](ConversationsV1UserApi.md#fetchServiceUser) | **GET** /v1/Services/{ChatServiceSid}/Users/{Sid} | 
[**fetchUser**](ConversationsV1UserApi.md#fetchUser) | **GET** /v1/Users/{Sid} | 
[**listServiceUser**](ConversationsV1UserApi.md#listServiceUser) | **GET** /v1/Services/{ChatServiceSid}/Users | 
[**listUser**](ConversationsV1UserApi.md#listUser) | **GET** /v1/Users | 
[**updateServiceUser**](ConversationsV1UserApi.md#updateServiceUser) | **POST** /v1/Services/{ChatServiceSid}/Users/{Sid} | 
[**updateUser**](ConversationsV1UserApi.md#updateUser) | **POST** /v1/Users/{Sid} | 



## createServiceUser

> ConversationsV1ServiceServiceUser createServiceUser(chatServiceSid, identity, opts)



Add a new conversation user to your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ServiceUserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the resource.
  'roleSid': "roleSid_example" // String | The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
};
apiInstance.createServiceUser(chatServiceSid, identity, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with. | 
 **identity** | **String**| The application-defined string that uniquely identifies the resource&#39;s User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive. | 
 **xTwilioWebhookEnabled** | **ServiceUserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] 
 **roleSid** | **String**| The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user. | [optional] 

### Return type

[**ConversationsV1ServiceServiceUser**](ConversationsV1ServiceServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## createUser

> ConversationsV1User createUser(identity, opts)



Add a new conversation user to your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the resource.
  'roleSid': "roleSid_example" // String | The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
};
apiInstance.createUser(identity, opts, (error, data, response) => {
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
 **identity** | **String**| The application-defined string that uniquely identifies the resource&#39;s User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive. | 
 **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] 
 **roleSid** | **String**| The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user. | [optional] 

### Return type

[**ConversationsV1User**](ConversationsV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteServiceUser

> deleteServiceUser(chatServiceSid, sid, opts)



Remove a conversation user from your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to delete the User resource from.
let sid = "sid_example"; // String | The SID of the User resource to delete. This value can be either the `sid` or the `identity` of the User resource to delete.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // ServiceUserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteServiceUser(chatServiceSid, sid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to delete the User resource from. | 
 **sid** | **String**| The SID of the User resource to delete. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to delete. | 
 **xTwilioWebhookEnabled** | **ServiceUserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteUser

> deleteUser(sid, opts)



Remove a conversation user from your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let sid = "sid_example"; // String | The SID of the User resource to delete. This value can be either the `sid` or the `identity` of the User resource to delete.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteUser(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the User resource to delete. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to delete. | 
 **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchServiceUser

> ConversationsV1ServiceServiceUser fetchServiceUser(chatServiceSid, sid)



Fetch a conversation user from your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to fetch the User resource from.
let sid = "sid_example"; // String | The SID of the User resource to fetch. This value can be either the `sid` or the `identity` of the User resource to fetch.
apiInstance.fetchServiceUser(chatServiceSid, sid, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to fetch the User resource from. | 
 **sid** | **String**| The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch. | 

### Return type

[**ConversationsV1ServiceServiceUser**](ConversationsV1ServiceServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchUser

> ConversationsV1User fetchUser(sid)



Fetch a conversation user from your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let sid = "sid_example"; // String | The SID of the User resource to fetch. This value can be either the `sid` or the `identity` of the User resource to fetch.
apiInstance.fetchUser(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch. | 

### Return type

[**ConversationsV1User**](ConversationsV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceUser

> ListServiceUserResponse listServiceUser(chatServiceSid, opts)



Retrieve a list of all conversation users in your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to read the User resources from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listServiceUser(chatServiceSid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to read the User resources from. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceUserResponse**](ListServiceUserResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUser

> ListUserResponse listUser(opts)



Retrieve a list of all conversation users in your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUser(opts, (error, data, response) => {
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

[**ListUserResponse**](ListUserResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateServiceUser

> ConversationsV1ServiceServiceUser updateServiceUser(chatServiceSid, sid, opts)



Update an existing conversation user in your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
let sid = "sid_example"; // String | The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ServiceUserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the resource.
  'roleSid': "roleSid_example" // String | The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
};
apiInstance.updateServiceUser(chatServiceSid, sid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with. | 
 **sid** | **String**| The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update. | 
 **xTwilioWebhookEnabled** | **ServiceUserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] 
 **roleSid** | **String**| The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user. | [optional] 

### Return type

[**ConversationsV1ServiceServiceUser**](ConversationsV1ServiceServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateUser

> ConversationsV1User updateUser(sid, opts)



Update an existing conversation user in your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserApi();
let sid = "sid_example"; // String | The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the resource.
  'roleSid': "roleSid_example" // String | The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
};
apiInstance.updateUser(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update. | 
 **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] 
 **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] 
 **roleSid** | **String**| The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user. | [optional] 

### Return type

[**ConversationsV1User**](ConversationsV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

