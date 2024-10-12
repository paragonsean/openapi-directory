# SlackWebApi.UsergroupsUsersApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usergroupsUsersList**](UsergroupsUsersApi.md#usergroupsUsersList) | **GET** /usergroups.users.list | 
[**usergroupsUsersUpdate**](UsergroupsUsersApi.md#usergroupsUsersUpdate) | **POST** /usergroups.users.update | 



## usergroupsUsersList

> UsergroupsUsersListSchema usergroupsUsersList(token, usergroup, opts)



List all users in a User Group

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsergroupsUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `usergroups:read`
let usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
let opts = {
  'includeDisabled': true // Boolean | Allow results that involve disabled User Groups.
};
apiInstance.usergroupsUsersList(token, usergroup, opts, (error, data, response) => {
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


## usergroupsUsersUpdate

> UsergroupsUsersUpdateSchema usergroupsUsersUpdate(token, usergroup, users, opts)



Update the list of users for a User Group

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.UsergroupsUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `usergroups:write`
let usergroup = "usergroup_example"; // String | The encoded ID of the User Group to update.
let users = "users_example"; // String | A comma separated string of encoded user IDs that represent the entire list of users for the User Group.
let opts = {
  'includeCount': true // Boolean | Include the number of users in the User Group.
};
apiInstance.usergroupsUsersUpdate(token, usergroup, users, opts, (error, data, response) => {
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

