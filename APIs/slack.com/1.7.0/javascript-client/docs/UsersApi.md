# SlackWebApi.UsersApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersConversations**](UsersApi.md#usersConversations) | **GET** /users.conversations | 
[**usersDeletePhoto**](UsersApi.md#usersDeletePhoto) | **POST** /users.deletePhoto | 
[**usersGetPresence**](UsersApi.md#usersGetPresence) | **GET** /users.getPresence | 
[**usersIdentity**](UsersApi.md#usersIdentity) | **GET** /users.identity | 
[**usersInfo**](UsersApi.md#usersInfo) | **GET** /users.info | 
[**usersList**](UsersApi.md#usersList) | **GET** /users.list | 
[**usersLookupByEmail**](UsersApi.md#usersLookupByEmail) | **GET** /users.lookupByEmail | 
[**usersProfileGet_0**](UsersApi.md#usersProfileGet_0) | **GET** /users.profile.get | 
[**usersProfileSet_0**](UsersApi.md#usersProfileSet_0) | **POST** /users.profile.set | 
[**usersSetActive**](UsersApi.md#usersSetActive) | **POST** /users.setActive | 
[**usersSetPhoto**](UsersApi.md#usersSetPhoto) | **POST** /users.setPhoto | 
[**usersSetPresence**](UsersApi.md#usersSetPresence) | **POST** /users.setPresence | 



## usersConversations

> UsersConversationsSuccessSchema usersConversations(opts)



List conversations the calling user may access.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:read`
  'user': "user_example", // String | Browse conversations by a specific user ID's membership. Non-public channels are restricted to those where the calling user shares membership.
  'types': "types_example", // String | Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`
  'excludeArchived': true, // Boolean | Set to `true` to exclude archived channels from the list
  'limit': 56, // Number | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.
  'cursor': "cursor_example" // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
};
apiInstance.usersConversations(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:read&#x60; | [optional] 
 **user** | **String**| Browse conversations by a specific user ID&#39;s membership. Non-public channels are restricted to those where the calling user shares membership. | [optional] 
 **types** | **String**| Mix and match channel types by providing a comma-separated list of any combination of &#x60;public_channel&#x60;, &#x60;private_channel&#x60;, &#x60;mpim&#x60;, &#x60;im&#x60; | [optional] 
 **excludeArchived** | **Boolean**| Set to &#x60;true&#x60; to exclude archived channels from the list | [optional] 
 **limit** | **Number**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. Must be an integer no larger than 1000. | [optional] 
 **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] 

### Return type

[**UsersConversationsSuccessSchema**](UsersConversationsSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersDeletePhoto

> UsersDeletePhotoSchema usersDeletePhoto(token)



Delete the user profile photo

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users.profile:write`
apiInstance.usersDeletePhoto(token, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:write&#x60; | 

### Return type

[**UsersDeletePhotoSchema**](UsersDeletePhotoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## usersGetPresence

> APIMethodUsersGetPresence usersGetPresence(token, opts)



Gets user presence information.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users:read`
let opts = {
  'user': "user_example" // String | User to get presence info on. Defaults to the authed user.
};
apiInstance.usersGetPresence(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users:read&#x60; | 
 **user** | **String**| User to get presence info on. Defaults to the authed user. | [optional] 

### Return type

[**APIMethodUsersGetPresence**](APIMethodUsersGetPresence.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdentity

> [UsersIdentitySchemaInner] usersIdentity(opts)



Get a user&#39;s identity.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let opts = {
  'token': "token_example" // String | Authentication token. Requires scope: `identity.basic`
};
apiInstance.usersIdentity(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;identity.basic&#x60; | [optional] 

### Return type

[**[UsersIdentitySchemaInner]**](UsersIdentitySchemaInner.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersInfo

> UsersInfoSuccessSchema usersInfo(token, opts)



Gets information about a user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users:read`
let opts = {
  'includeLocale': true, // Boolean | Set this to `true` to receive the locale for this user. Defaults to `false`
  'user': "user_example" // String | User to get info on
};
apiInstance.usersInfo(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users:read&#x60; | 
 **includeLocale** | **Boolean**| Set this to &#x60;true&#x60; to receive the locale for this user. Defaults to &#x60;false&#x60; | [optional] 
 **user** | **String**| User to get info on | [optional] 

### Return type

[**UsersInfoSuccessSchema**](UsersInfoSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersList

> UsersListSchema usersList(opts)



Lists all users in a Slack team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `users:read`
  'limit': 56, // Number | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached. Providing no `limit` value will result in Slack attempting to deliver you the entire result set. If the collection is too large you may experience `limit_required` or HTTP 500 errors.
  'cursor': "cursor_example", // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
  'includeLocale': true // Boolean | Set this to `true` to receive the locale for users. Defaults to `false`
};
apiInstance.usersList(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users:read&#x60; | [optional] 
 **limit** | **Number**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached. Providing no &#x60;limit&#x60; value will result in Slack attempting to deliver you the entire result set. If the collection is too large you may experience &#x60;limit_required&#x60; or HTTP 500 errors. | [optional] 
 **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] 
 **includeLocale** | **Boolean**| Set this to &#x60;true&#x60; to receive the locale for users. Defaults to &#x60;false&#x60; | [optional] 

### Return type

[**UsersListSchema**](UsersListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersLookupByEmail

> UsersLookupByEmailSuccessSchema usersLookupByEmail(token, email)



Find a user with an email address.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users:read.email`
let email = "email_example"; // String | An email address belonging to a user in the workspace
apiInstance.usersLookupByEmail(token, email, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users:read.email&#x60; | 
 **email** | **String**| An email address belonging to a user in the workspace | 

### Return type

[**UsersLookupByEmailSuccessSchema**](UsersLookupByEmailSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersProfileGet_0

> UsersProfileGetSchema usersProfileGet_0(token, opts)



Retrieves a user&#39;s profile information.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users.profile:read`
let opts = {
  'includeLabels': true, // Boolean | Include labels for each ID in custom profile fields
  'user': "user_example" // String | User to retrieve profile info for
};
apiInstance.usersProfileGet_0(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:read&#x60; | 
 **includeLabels** | **Boolean**| Include labels for each ID in custom profile fields | [optional] 
 **user** | **String**| User to retrieve profile info for | [optional] 

### Return type

[**UsersProfileGetSchema**](UsersProfileGetSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersProfileSet_0

> UsersProfileSetSchema usersProfileSet_0(token, opts)



Set the profile information for a user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users.profile:write`
let opts = {
  'name': "name_example", // String | Name of a single key to set. Usable only if `profile` is not passed.
  'profile': "profile_example", // String | Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters.
  'user': "user_example", // String | ID of user to change. This argument may only be specified by team admins on paid teams.
  'value': "value_example" // String | Value to set a single key to. Usable only if `profile` is not passed.
};
apiInstance.usersProfileSet_0(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:write&#x60; | 
 **name** | **String**| Name of a single key to set. Usable only if &#x60;profile&#x60; is not passed. | [optional] 
 **profile** | **String**| Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters. | [optional] 
 **user** | **String**| ID of user to change. This argument may only be specified by team admins on paid teams. | [optional] 
 **value** | **String**| Value to set a single key to. Usable only if &#x60;profile&#x60; is not passed. | [optional] 

### Return type

[**UsersProfileSetSchema**](UsersProfileSetSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## usersSetActive

> UsersSetActiveSchema usersSetActive(token)



Marked a user as active. Deprecated and non-functional.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users:write`
apiInstance.usersSetActive(token, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users:write&#x60; | 

### Return type

[**UsersSetActiveSchema**](UsersSetActiveSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersSetPhoto

> UsersSetPhotoSchema usersSetPhoto(token, opts)



Set the user profile photo

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users.profile:write`
let opts = {
  'cropW': "cropW_example", // String | Width/height of crop box (always square)
  'cropX': "cropX_example", // String | X coordinate of top-left corner of crop box
  'cropY': "cropY_example", // String | Y coordinate of top-left corner of crop box
  'image': "image_example" // String | File contents via `multipart/form-data`.
};
apiInstance.usersSetPhoto(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:write&#x60; | 
 **cropW** | **String**| Width/height of crop box (always square) | [optional] 
 **cropX** | **String**| X coordinate of top-left corner of crop box | [optional] 
 **cropY** | **String**| Y coordinate of top-left corner of crop box | [optional] 
 **image** | **String**| File contents via &#x60;multipart/form-data&#x60;. | [optional] 

### Return type

[**UsersSetPhotoSchema**](UsersSetPhotoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## usersSetPresence

> UsersSetPresenceSchema usersSetPresence(token, presence)



Manually sets user presence.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users:write`
let presence = "presence_example"; // String | Either `auto` or `away`
apiInstance.usersSetPresence(token, presence, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users:write&#x60; | 
 **presence** | **String**| Either &#x60;auto&#x60; or &#x60;away&#x60; | 

### Return type

[**UsersSetPresenceSchema**](UsersSetPresenceSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

