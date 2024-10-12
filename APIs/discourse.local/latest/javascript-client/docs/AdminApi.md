# DiscourseApiDocumentation.AdminApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminGetUser_0**](AdminApi.md#adminGetUser_0) | **GET** /admin/users/{id}.json | Get a user by id
[**adminListUsers_0**](AdminApi.md#adminListUsers_0) | **GET** /admin/users/list/{flag}.json | Get a list of users
[**anonymizeUser_0**](AdminApi.md#anonymizeUser_0) | **PUT** /admin/users/{id}/anonymize.json | Anonymize a user
[**deleteUser_0**](AdminApi.md#deleteUser_0) | **DELETE** /admin/users/{id}.json | Delete a user
[**logOutUser_0**](AdminApi.md#logOutUser_0) | **POST** /admin/users/{id}/log_out.json | Log a user out
[**refreshGravatar_0**](AdminApi.md#refreshGravatar_0) | **POST** /user_avatar/{username}/refresh_gravatar.json | Refresh gravatar
[**silenceUser_0**](AdminApi.md#silenceUser_0) | **PUT** /admin/users/{id}/silence.json | Silence a user
[**suspendUser_0**](AdminApi.md#suspendUser_0) | **PUT** /admin/users/{id}/suspend.json | Suspend a user



## adminGetUser_0

> AdminGetUser200Response adminGetUser_0(id)

Get a user by id

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.AdminApi();
let id = 56; // Number | 
apiInstance.adminGetUser_0(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**AdminGetUser200Response**](AdminGetUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminListUsers_0

> [AdminListUsers200ResponseInner] adminListUsers_0(flag, opts)

Get a list of users

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.AdminApi();
let flag = "flag_example"; // String | 
let opts = {
  'order': "order_example", // String | 
  'asc': "asc_example", // String | 
  'page': 56, // Number | 
  'showEmails': true // Boolean | 
};
apiInstance.adminListUsers_0(flag, opts, (error, data, response) => {
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
 **flag** | **String**|  | 
 **order** | **String**|  | [optional] 
 **asc** | **String**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **showEmails** | **Boolean**|  | [optional] 

### Return type

[**[AdminListUsers200ResponseInner]**](AdminListUsers200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## anonymizeUser_0

> AnonymizeUser200Response anonymizeUser_0(id)

Anonymize a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.AdminApi();
let id = 56; // Number | 
apiInstance.anonymizeUser_0(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**AnonymizeUser200Response**](AnonymizeUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUser_0

> DeleteUser200Response deleteUser_0(id, opts)

Delete a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.AdminApi();
let id = 56; // Number | 
let opts = {
  'deleteUserRequest': new DiscourseApiDocumentation.DeleteUserRequest() // DeleteUserRequest | 
};
apiInstance.deleteUser_0(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **deleteUserRequest** | [**DeleteUserRequest**](DeleteUserRequest.md)|  | [optional] 

### Return type

[**DeleteUser200Response**](DeleteUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## logOutUser_0

> DeleteGroup200Response logOutUser_0(id)

Log a user out

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.AdminApi();
let id = 56; // Number | 
apiInstance.logOutUser_0(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**DeleteGroup200Response**](DeleteGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## refreshGravatar_0

> RefreshGravatar200Response refreshGravatar_0(username)

Refresh gravatar

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.AdminApi();
let username = "username_example"; // String | 
apiInstance.refreshGravatar_0(username, (error, data, response) => {
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
 **username** | **String**|  | 

### Return type

[**RefreshGravatar200Response**](RefreshGravatar200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## silenceUser_0

> SilenceUser200Response silenceUser_0(id, opts)

Silence a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.AdminApi();
let id = 56; // Number | 
let opts = {
  'silenceUserRequest': new DiscourseApiDocumentation.SilenceUserRequest() // SilenceUserRequest | 
};
apiInstance.silenceUser_0(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **silenceUserRequest** | [**SilenceUserRequest**](SilenceUserRequest.md)|  | [optional] 

### Return type

[**SilenceUser200Response**](SilenceUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## suspendUser_0

> SuspendUser200Response suspendUser_0(id, opts)

Suspend a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.AdminApi();
let id = 56; // Number | 
let opts = {
  'suspendUserRequest': new DiscourseApiDocumentation.SuspendUserRequest() // SuspendUserRequest | 
};
apiInstance.suspendUser_0(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **suspendUserRequest** | [**SuspendUserRequest**](SuspendUserRequest.md)|  | [optional] 

### Return type

[**SuspendUser200Response**](SuspendUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

