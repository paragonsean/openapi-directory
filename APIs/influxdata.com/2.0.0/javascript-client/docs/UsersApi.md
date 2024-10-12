# InfluxOssApiService.UsersApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUsersID**](UsersApi.md#deleteUsersID) | **DELETE** /users/{userID} | Delete a user
[**getFlags**](UsersApi.md#getFlags) | **GET** /flags | Return the feature flags for the currently authenticated user
[**getMe**](UsersApi.md#getMe) | **GET** /me | Retrieve the currently authenticated user
[**getUsers**](UsersApi.md#getUsers) | **GET** /users | List all users
[**getUsersID**](UsersApi.md#getUsersID) | **GET** /users/{userID} | Retrieve a user
[**patchUsersID**](UsersApi.md#patchUsersID) | **PATCH** /users/{userID} | Update a user
[**postUsers**](UsersApi.md#postUsers) | **POST** /users | Create a user
[**postUsersIDPassword**](UsersApi.md#postUsersIDPassword) | **POST** /users/{userID}/password | Update a password
[**putMePassword**](UsersApi.md#putMePassword) | **PUT** /me/password | Update a password



## deleteUsersID

> deleteUsersID(userID, opts)

Delete a user

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.UsersApi();
let userID = "userID_example"; // String | The ID of the user to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteUsersID(userID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the user to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFlags

> {String: Object} getFlags(opts)

Return the feature flags for the currently authenticated user

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.UsersApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getFlags(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMe

> UserResponse getMe(opts)

Retrieve the currently authenticated user

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.UsersApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getMe(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsers

> Users getUsers(opts)

List all users

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.UsersApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'offset': 56, // Number | 
  'limit': 20, // Number | 
  'after': "after_example", // String | The last resource ID from which to seek from (but not including). This is to be used instead of `offset`. 
  'name': "name_example", // String | 
  'id': "id_example" // String | 
};
apiInstance.getUsers(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **after** | **String**| The last resource ID from which to seek from (but not including). This is to be used instead of &#x60;offset&#x60;.  | [optional] 
 **name** | **String**|  | [optional] 
 **id** | **String**|  | [optional] 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersID

> UserResponse getUsersID(userID, opts)

Retrieve a user

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.UsersApi();
let userID = "userID_example"; // String | The user ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getUsersID(userID, opts, (error, data, response) => {
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
 **userID** | **String**| The user ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchUsersID

> UserResponse patchUsersID(userID, user, opts)

Update a user

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.UsersApi();
let userID = "userID_example"; // String | The ID of the user to update.
let user = new InfluxOssApiService.User(); // User | User update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchUsersID(userID, user, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the user to update. | 
 **user** | [**User**](User.md)| User update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUsers

> UserResponse postUsers(user, opts)

Create a user

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.UsersApi();
let user = new InfluxOssApiService.User(); // User | User to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postUsers(user, opts, (error, data, response) => {
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
 **user** | [**User**](User.md)| User to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUsersIDPassword

> postUsersIDPassword(userID, passwordResetBody, opts)

Update a password

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';
let defaultClient = InfluxOssApiService.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new InfluxOssApiService.UsersApi();
let userID = "userID_example"; // String | The user ID.
let passwordResetBody = new InfluxOssApiService.PasswordResetBody(); // PasswordResetBody | New password
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postUsersIDPassword(userID, passwordResetBody, opts, (error, data, response) => {
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
 **userID** | **String**| The user ID. | 
 **passwordResetBody** | [**PasswordResetBody**](PasswordResetBody.md)| New password | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putMePassword

> putMePassword(passwordResetBody, opts)

Update a password

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';
let defaultClient = InfluxOssApiService.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new InfluxOssApiService.UsersApi();
let passwordResetBody = new InfluxOssApiService.PasswordResetBody(); // PasswordResetBody | New password
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.putMePassword(passwordResetBody, opts, (error, data, response) => {
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
 **passwordResetBody** | [**PasswordResetBody**](PasswordResetBody.md)| New password | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

