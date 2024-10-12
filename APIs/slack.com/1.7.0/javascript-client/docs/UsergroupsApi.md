# SlackWebApi.UsergroupsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usergroupsCreate**](UsergroupsApi.md#usergroupsCreate) | **POST** /usergroups.create | 
[**usergroupsDisable**](UsergroupsApi.md#usergroupsDisable) | **POST** /usergroups.disable | 
[**usergroupsEnable**](UsergroupsApi.md#usergroupsEnable) | **POST** /usergroups.enable | 
[**usergroupsList**](UsergroupsApi.md#usergroupsList) | **GET** /usergroups.list | 
[**usergroupsUpdate**](UsergroupsApi.md#usergroupsUpdate) | **POST** /usergroups.update | 
[**usergroupsUsersList_0**](UsergroupsApi.md#usergroupsUsersList_0) | **GET** /usergroups.users.list | 
[**usergroupsUsersUpdate_0**](UsergroupsApi.md#usergroupsUsersUpdate_0) | **POST** /usergroups.users.update | 



## usergroupsCreate

> UsergroupsCreateSchema usergroupsCreate(token, name, opts)



Create a User Group

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
let name = "name_example"; // String | A name for the User Group. Must be unique among User Groups.
let opts = {
  'channels': "channels_example", // String | A comma separated string of encoded channel IDs for which the User Group uses as a default.
  'description': "description_example", // String | A short description of the User Group.
  'handle': "handle_example", // String | A mention handle. Must be unique among channels, users and User Groups.
  'includeCount': true // Boolean | Include the number of users in each User Group.
};
apiInstance.usergroupsCreate(token, name, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;usergroups:write&#x60; | 
 **name** | **String**| A name for the User Group. Must be unique among User Groups. | 
 **channels** | **String**| A comma separated string of encoded channel IDs for which the User Group uses as a default. | [optional] 
 **description** | **String**| A short description of the User Group. | [optional] 
 **handle** | **String**| A mention handle. Must be unique among channels, users and User Groups. | [optional] 
 **includeCount** | **Boolean**| Include the number of users in each User Group. | [optional] 

### Return type

[**UsergroupsCreateSchema**](UsergroupsCreateSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## usergroupsDisable

> UsergroupsDisableSchema usergroupsDisable(token, usergroup, opts)



Disable an existing User Group

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
let usergroup = "usergroup_example"; // String | The encoded ID of the User Group to disable.
let opts = {
  'includeCount': true // Boolean | Include the number of users in the User Group.
};
apiInstance.usergroupsDisable(token, usergroup, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;usergroups:write&#x60; | 
 **usergroup** | **String**| The encoded ID of the User Group to disable. | 
 **includeCount** | **Boolean**| Include the number of users in the User Group. | [optional] 

### Return type

[**UsergroupsDisableSchema**](UsergroupsDisableSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## usergroupsEnable

> UsergroupsEnableSchema usergroupsEnable(token, usergroup, opts)



Enable a User Group

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
let usergroup = "usergroup_example"; // String | The encoded ID of the User Group to enable.
let opts = {
  'includeCount': true // Boolean | Include the number of users in the User Group.
};
apiInstance.usergroupsEnable(token, usergroup, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;usergroups:write&#x60; | 
 **usergroup** | **String**| The encoded ID of the User Group to enable. | 
 **includeCount** | **Boolean**| Include the number of users in the User Group. | [optional] 

### Return type

[**UsergroupsEnableSchema**](UsergroupsEnableSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## usergroupsList

> UsergroupsListSchema usergroupsList(token, opts)



List all User Groups for a team

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `usergroups:read`
let opts = {
  'includeUsers': true, // Boolean | Include the list of users for each User Group.
  'includeCount': true, // Boolean | Include the number of users in each User Group.
  'includeDisabled': true // Boolean | Include disabled User Groups.
};
apiInstance.usergroupsList(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;usergroups:read&#x60; | 
 **includeUsers** | **Boolean**| Include the list of users for each User Group. | [optional] 
 **includeCount** | **Boolean**| Include the number of users in each User Group. | [optional] 
 **includeDisabled** | **Boolean**| Include disabled User Groups. | [optional] 

### Return type

[**UsergroupsListSchema**](UsergroupsListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usergroupsUpdate

> UsergroupsUpdateSchema usergroupsUpdate(token, usergroup, opts)



Update an existing User Group

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
let usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
let opts = {
  'channels': "channels_example", // String | A comma separated string of encoded channel IDs for which the User Group uses as a default.
  'description': "description_example", // String | A short description of the User Group.
  'handle': "handle_example", // String | A mention handle. Must be unique among channels, users and User Groups.
  'includeCount': true, // Boolean | Include the number of users in the User Group.
  'name': "name_example" // String | A name for the User Group. Must be unique among User Groups.
};
apiInstance.usergroupsUpdate(token, usergroup, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;usergroups:write&#x60; | 
 **usergroup** | **String**| The encoded ID of the User Group to update. | 
 **channels** | **String**| A comma separated string of encoded channel IDs for which the User Group uses as a default. | [optional] 
 **description** | **String**| A short description of the User Group. | [optional] 
 **handle** | **String**| A mention handle. Must be unique among channels, users and User Groups. | [optional] 
 **includeCount** | **Boolean**| Include the number of users in the User Group. | [optional] 
 **name** | **String**| A name for the User Group. Must be unique among User Groups. | [optional] 

### Return type

[**UsergroupsUpdateSchema**](UsergroupsUpdateSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## usergroupsUsersList_0

> UsergroupsUsersListSchema usergroupsUsersList_0(token, usergroup, opts)



List all users in a User Group

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `usergroups:read`
let usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
let opts = {
  'includeDisabled': true // Boolean | Allow results that involve disabled User Groups.
};
apiInstance.usergroupsUsersList_0(token, usergroup, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;usergroups:read&#x60; | 
 **usergroup** | **String**| The encoded ID of the User Group to update. | 
 **includeDisabled** | **Boolean**| Allow results that involve disabled User Groups. | [optional] 

### Return type

[**UsergroupsUsersListSchema**](UsergroupsUsersListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usergroupsUsersUpdate_0

> UsergroupsUsersUpdateSchema usergroupsUsersUpdate_0(token, usergroup, users, opts)



Update the list of users for a User Group

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
let usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
let users = "users_example"; // String | A comma separated string of encoded user IDs that represent the entire list of users for the User Group.
let opts = {
  'includeCount': true // Boolean | Include the number of users in the User Group.
};
apiInstance.usergroupsUsersUpdate_0(token, usergroup, users, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;usergroups:write&#x60; | 
 **usergroup** | **String**| The encoded ID of the User Group to update. | 
 **users** | **String**| A comma separated string of encoded user IDs that represent the entire list of users for the User Group. | 
 **includeCount** | **Boolean**| Include the number of users in the User Group. | [optional] 

### Return type

[**UsergroupsUsersUpdateSchema**](UsergroupsUsersUpdateSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

