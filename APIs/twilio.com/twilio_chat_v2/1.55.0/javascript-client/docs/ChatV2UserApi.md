# TwilioChat.ChatV2UserApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUser**](ChatV2UserApi.md#createUser) | **POST** /v2/Services/{ServiceSid}/Users | 
[**deleteUser**](ChatV2UserApi.md#deleteUser) | **DELETE** /v2/Services/{ServiceSid}/Users/{Sid} | 
[**fetchUser**](ChatV2UserApi.md#fetchUser) | **GET** /v2/Services/{ServiceSid}/Users/{Sid} | 
[**listUser**](ChatV2UserApi.md#listUser) | **GET** /v2/Services/{ServiceSid}/Users | 
[**updateUser**](ChatV2UserApi.md#updateUser) | **POST** /v2/Services/{ServiceSid}/Users/{Sid} | 



## createUser

> ChatV2ServiceUser createUser(serviceSid, identity, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the User resource under.
let identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). This value is often a username or email address. See the Identity documentation for more info.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the new resource. This value is often used for display purposes.
  'roleSid': "roleSid_example" // String | The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the new User.
};
apiInstance.createUser(serviceSid, identity, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the User resource under. | 
 **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). This value is often a username or email address. See the Identity documentation for more info. | 
 **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the new resource. This value is often used for display purposes. | [optional] 
 **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the new User. | [optional] 

### Return type

[**ChatV2ServiceUser**](ChatV2ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteUser

> deleteUser(serviceSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the User resource from.
let sid = "sid_example"; // String | The SID of the User resource to delete. This value can be either the `sid` or the `identity` of the User resource to delete.
apiInstance.deleteUser(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the User resource from. | 
 **sid** | **String**| The SID of the User resource to delete. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchUser

> ChatV2ServiceUser fetchUser(serviceSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the User resource from.
let sid = "sid_example"; // String | The SID of the User resource to fetch. This value can be either the `sid` or the `identity` of the User resource to fetch.
apiInstance.fetchUser(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the User resource from. | 
 **sid** | **String**| The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch. | 

### Return type

[**ChatV2ServiceUser**](ChatV2ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUser

> ListUserResponse listUser(serviceSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the User resources from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUser(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the User resources from. | 
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


## updateUser

> ChatV2ServiceUser updateUser(serviceSid, sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the User resource in.
let sid = "sid_example"; // String | The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It is often used for display purposes.
  'roleSid': "roleSid_example" // String | The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the User.
};
apiInstance.updateUser(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the User resource in. | 
 **sid** | **String**| The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update. | 
 **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is often used for display purposes. | [optional] 
 **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the User. | [optional] 

### Return type

[**ChatV2ServiceUser**](ChatV2ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

