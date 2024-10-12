# UsersOktaApi.LifecycleOperationsApi

All URIs are relative to *http://okta.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateUser**](LifecycleOperationsApi.md#activateUser) | **POST** /api/v1/users/{userId}/lifecycle/activate | Activate User
[**deactivateUser**](LifecycleOperationsApi.md#deactivateUser) | **POST** /api/v1/users/{userId}/lifecycle/deactivate | Deactivate User
[**resetPassword**](LifecycleOperationsApi.md#resetPassword) | **POST** /api/v1/users/{userId}/lifecycle/reset_password | Reset Password
[**setTempPassword**](LifecycleOperationsApi.md#setTempPassword) | **POST** /api/v1/users/{userId}/lifecycle/expire_password | Set Temp Password
[**suspendUser**](LifecycleOperationsApi.md#suspendUser) | **POST** /api/v1/users/{userId}/lifecycle/suspend | Suspend User
[**unlockUser**](LifecycleOperationsApi.md#unlockUser) | **POST** /api/v1/users/{userId}/lifecycle/unlock | Unlock User
[**unsuspendUser**](LifecycleOperationsApi.md#unsuspendUser) | **POST** /api/v1/users/{userId}/lifecycle/unsuspend | Unsuspend User



## activateUser

> activateUser(userId, opts)

Activate User

Activate User

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.LifecycleOperationsApi();
let userId = "userId_example"; // String | 
let opts = {
  'sendEmail': "false" // String | 
};
apiInstance.activateUser(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **sendEmail** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## deactivateUser

> deactivateUser(userId)

Deactivate User

Deactivate User

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.LifecycleOperationsApi();
let userId = "userId_example"; // String | 
apiInstance.deactivateUser(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## resetPassword

> resetPassword(userId, opts)

Reset Password

Reset Password

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.LifecycleOperationsApi();
let userId = "userId_example"; // String | 
let opts = {
  'sendEmail': "false" // String | 
};
apiInstance.resetPassword(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **sendEmail** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## setTempPassword

> setTempPassword(userId, opts)

Set Temp Password

Set Temp Password

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.LifecycleOperationsApi();
let userId = "userId_example"; // String | 
let opts = {
  'tempPassword': "true" // String | 
};
apiInstance.setTempPassword(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **tempPassword** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## suspendUser

> suspendUser(userId)

Suspend User

Suspend User

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.LifecycleOperationsApi();
let userId = "userId_example"; // String | 
apiInstance.suspendUser(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## unlockUser

> unlockUser(userId)

Unlock User

Unlock User

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.LifecycleOperationsApi();
let userId = "userId_example"; // String | 
apiInstance.unlockUser(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## unsuspendUser

> unsuspendUser(userId)

Unsuspend User

Unsuspend User

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.LifecycleOperationsApi();
let userId = "userId_example"; // String | 
apiInstance.unsuspendUser(userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined

