# TwilioChat.ChatV1UserApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUser**](ChatV1UserApi.md#createUser) | **POST** /v1/Services/{ServiceSid}/Users | 
[**deleteUser**](ChatV1UserApi.md#deleteUser) | **DELETE** /v1/Services/{ServiceSid}/Users/{Sid} | 
[**fetchUser**](ChatV1UserApi.md#fetchUser) | **GET** /v1/Services/{ServiceSid}/Users/{Sid} | 
[**listUser**](ChatV1UserApi.md#listUser) | **GET** /v1/Services/{ServiceSid}/Users | 
[**updateUser**](ChatV1UserApi.md#updateUser) | **POST** /v1/Services/{ServiceSid}/Users/{Sid} | 



## createUser

> ChatV1ServiceUser createUser(serviceSid, identity, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under.
let identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/v1/service). This value is often a username or email address. See the Identity documentation for more details.
let opts = {
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the new resource. This value is often used for display purposes.
  'roleSid': "roleSid_example" // String | The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the new User.
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under. | 
 **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/v1/service). This value is often a username or email address. See the Identity documentation for more details. | 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the new resource. This value is often used for display purposes. | [optional] 
 **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the new User. | [optional] 

### Return type

[**ChatV1ServiceUser**](ChatV1ServiceUser.md)

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

let apiInstance = new TwilioChat.ChatV1UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the User resource to delete.
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the User resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchUser

> ChatV1ServiceUser fetchUser(serviceSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the User resource to fetch.
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the User resource to fetch. | 

### Return type

[**ChatV1ServiceUser**](ChatV1ServiceUser.md)

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

let apiInstance = new TwilioChat.ChatV1UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from. | 
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

> ChatV1ServiceUser updateUser(serviceSid, sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1UserApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the User resource to update.
let opts = {
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It is often used for display purposes.
  'roleSid': "roleSid_example" // String | The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to this user.
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the User resource to update. | 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is often used for display purposes. | [optional] 
 **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to this user. | [optional] 

### Return type

[**ChatV1ServiceUser**](ChatV1ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

