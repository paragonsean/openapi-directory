# OpenapiJsClient.AdministrativeApi

All URIs are relative to *https://app.drchrono.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doctorsList**](AdministrativeApi.md#doctorsList) | **GET** /api/doctors | 
[**doctorsRead**](AdministrativeApi.md#doctorsRead) | **GET** /api/doctors/{id} | 
[**userGroupsList**](AdministrativeApi.md#userGroupsList) | **GET** /api/user_groups | 
[**userGroupsRead**](AdministrativeApi.md#userGroupsRead) | **GET** /api/user_groups/{id} | 
[**usersList**](AdministrativeApi.md#usersList) | **GET** /api/users | 
[**usersRead**](AdministrativeApi.md#usersRead) | **GET** /api/users/{id} | 



## doctorsList

> DoctorsList200Response doctorsList(opts)



Retrieve or search doctors within practice group

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.AdministrativeApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.doctorsList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**DoctorsList200Response**](DoctorsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## doctorsRead

> Doctor doctorsRead(id, opts)



Retrieve an existing dcotor

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.AdministrativeApi();
let id = "id_example"; // String | 
let opts = {
  'doctor': 56 // Number | 
};
apiInstance.doctorsRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **doctor** | **Number**|  | [optional] 

### Return type

[**Doctor**](Doctor.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userGroupsList

> UserGroupsList200Response userGroupsList(opts)



Retrieve or search user groups

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.AdministrativeApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.userGroupsList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**UserGroupsList200Response**](UserGroupsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userGroupsRead

> UserProfilesGroup userGroupsRead(id, opts)



Retrieve an existing user group

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.AdministrativeApi();
let id = "id_example"; // String | 
let opts = {
  'doctor': 56 // Number | 
};
apiInstance.userGroupsRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **doctor** | **Number**|  | [optional] 

### Return type

[**UserProfilesGroup**](UserProfilesGroup.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersList

> UsersList200Response usersList(opts)



Retrieve or search users, &#x60;/api/users/current&#x60; can be used to identify logged in user, it will redirect to &#x60;/api/users/{current_user_id}&#x60;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.AdministrativeApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'doctor': 56 // Number | 
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**UsersList200Response**](UsersList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersRead

> UserProfile usersRead(id, opts)



Retrieve an existing user, &#x60;/api/users/current&#x60; can be used to identify logged in user, it will redirect to &#x60;/api/users/{current_user_id}&#x60;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.AdministrativeApi();
let id = "id_example"; // String | 
let opts = {
  'doctor': 56 // Number | 
};
apiInstance.usersRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **doctor** | **Number**|  | [optional] 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

