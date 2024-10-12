# NetBoxApi.UsersApi

All URIs are relative to *https://demo.netbox.dev/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersConfigList**](UsersApi.md#usersConfigList) | **GET** /users/config/ | 
[**usersGroupsBulkDelete**](UsersApi.md#usersGroupsBulkDelete) | **DELETE** /users/groups/ | 
[**usersGroupsBulkPartialUpdate**](UsersApi.md#usersGroupsBulkPartialUpdate) | **PATCH** /users/groups/ | 
[**usersGroupsBulkUpdate**](UsersApi.md#usersGroupsBulkUpdate) | **PUT** /users/groups/ | 
[**usersGroupsCreate**](UsersApi.md#usersGroupsCreate) | **POST** /users/groups/ | 
[**usersGroupsDelete**](UsersApi.md#usersGroupsDelete) | **DELETE** /users/groups/{id}/ | 
[**usersGroupsList**](UsersApi.md#usersGroupsList) | **GET** /users/groups/ | 
[**usersGroupsPartialUpdate**](UsersApi.md#usersGroupsPartialUpdate) | **PATCH** /users/groups/{id}/ | 
[**usersGroupsRead**](UsersApi.md#usersGroupsRead) | **GET** /users/groups/{id}/ | 
[**usersGroupsUpdate**](UsersApi.md#usersGroupsUpdate) | **PUT** /users/groups/{id}/ | 
[**usersPermissionsBulkDelete**](UsersApi.md#usersPermissionsBulkDelete) | **DELETE** /users/permissions/ | 
[**usersPermissionsBulkPartialUpdate**](UsersApi.md#usersPermissionsBulkPartialUpdate) | **PATCH** /users/permissions/ | 
[**usersPermissionsBulkUpdate**](UsersApi.md#usersPermissionsBulkUpdate) | **PUT** /users/permissions/ | 
[**usersPermissionsCreate**](UsersApi.md#usersPermissionsCreate) | **POST** /users/permissions/ | 
[**usersPermissionsDelete**](UsersApi.md#usersPermissionsDelete) | **DELETE** /users/permissions/{id}/ | 
[**usersPermissionsList**](UsersApi.md#usersPermissionsList) | **GET** /users/permissions/ | 
[**usersPermissionsPartialUpdate**](UsersApi.md#usersPermissionsPartialUpdate) | **PATCH** /users/permissions/{id}/ | 
[**usersPermissionsRead**](UsersApi.md#usersPermissionsRead) | **GET** /users/permissions/{id}/ | 
[**usersPermissionsUpdate**](UsersApi.md#usersPermissionsUpdate) | **PUT** /users/permissions/{id}/ | 
[**usersTokensBulkDelete**](UsersApi.md#usersTokensBulkDelete) | **DELETE** /users/tokens/ | 
[**usersTokensBulkPartialUpdate**](UsersApi.md#usersTokensBulkPartialUpdate) | **PATCH** /users/tokens/ | 
[**usersTokensBulkUpdate**](UsersApi.md#usersTokensBulkUpdate) | **PUT** /users/tokens/ | 
[**usersTokensCreate**](UsersApi.md#usersTokensCreate) | **POST** /users/tokens/ | 
[**usersTokensDelete**](UsersApi.md#usersTokensDelete) | **DELETE** /users/tokens/{id}/ | 
[**usersTokensList**](UsersApi.md#usersTokensList) | **GET** /users/tokens/ | 
[**usersTokensPartialUpdate**](UsersApi.md#usersTokensPartialUpdate) | **PATCH** /users/tokens/{id}/ | 
[**usersTokensProvisionCreate**](UsersApi.md#usersTokensProvisionCreate) | **POST** /users/tokens/provision/ | 
[**usersTokensRead**](UsersApi.md#usersTokensRead) | **GET** /users/tokens/{id}/ | 
[**usersTokensUpdate**](UsersApi.md#usersTokensUpdate) | **PUT** /users/tokens/{id}/ | 
[**usersUsersBulkDelete**](UsersApi.md#usersUsersBulkDelete) | **DELETE** /users/users/ | 
[**usersUsersBulkPartialUpdate**](UsersApi.md#usersUsersBulkPartialUpdate) | **PATCH** /users/users/ | 
[**usersUsersBulkUpdate**](UsersApi.md#usersUsersBulkUpdate) | **PUT** /users/users/ | 
[**usersUsersCreate**](UsersApi.md#usersUsersCreate) | **POST** /users/users/ | 
[**usersUsersDelete**](UsersApi.md#usersUsersDelete) | **DELETE** /users/users/{id}/ | 
[**usersUsersList**](UsersApi.md#usersUsersList) | **GET** /users/users/ | 
[**usersUsersPartialUpdate**](UsersApi.md#usersUsersPartialUpdate) | **PATCH** /users/users/{id}/ | 
[**usersUsersRead**](UsersApi.md#usersUsersRead) | **GET** /users/users/{id}/ | 
[**usersUsersUpdate**](UsersApi.md#usersUsersUpdate) | **PUT** /users/users/{id}/ | 



## usersConfigList

> usersConfigList()



Return the UserConfig for the currently authenticated User.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
apiInstance.usersConfigList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersGroupsBulkDelete

> usersGroupsBulkDelete()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
apiInstance.usersGroupsBulkDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersGroupsBulkPartialUpdate

> Group usersGroupsBulkPartialUpdate(group)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let group = new NetBoxApi.Group(); // Group | 
apiInstance.usersGroupsBulkPartialUpdate(group, (error, data, response) => {
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
 **group** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersGroupsBulkUpdate

> Group usersGroupsBulkUpdate(group)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let group = new NetBoxApi.Group(); // Group | 
apiInstance.usersGroupsBulkUpdate(group, (error, data, response) => {
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
 **group** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersGroupsCreate

> Group usersGroupsCreate(group)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let group = new NetBoxApi.Group(); // Group | 
apiInstance.usersGroupsCreate(group, (error, data, response) => {
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
 **group** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersGroupsDelete

> usersGroupsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this group.
apiInstance.usersGroupsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this group. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersGroupsList

> UsersGroupsList200Response usersGroupsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let opts = {
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'q': "q_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'nameEmpty': "nameEmpty_example", // String | 
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.usersGroupsList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **nameEmpty** | **String**|  | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**UsersGroupsList200Response**](UsersGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGroupsPartialUpdate

> Group usersGroupsPartialUpdate(id, group)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this group.
let group = new NetBoxApi.Group(); // Group | 
apiInstance.usersGroupsPartialUpdate(id, group, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this group. | 
 **group** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersGroupsRead

> Group usersGroupsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this group.
apiInstance.usersGroupsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this group. | 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGroupsUpdate

> Group usersGroupsUpdate(id, group)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this group.
let group = new NetBoxApi.Group(); // Group | 
apiInstance.usersGroupsUpdate(id, group, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this group. | 
 **group** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersPermissionsBulkDelete

> usersPermissionsBulkDelete()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
apiInstance.usersPermissionsBulkDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersPermissionsBulkPartialUpdate

> ObjectPermission usersPermissionsBulkPartialUpdate(writableObjectPermission)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let writableObjectPermission = new NetBoxApi.WritableObjectPermission(); // WritableObjectPermission | 
apiInstance.usersPermissionsBulkPartialUpdate(writableObjectPermission, (error, data, response) => {
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
 **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | 

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersPermissionsBulkUpdate

> ObjectPermission usersPermissionsBulkUpdate(writableObjectPermission)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let writableObjectPermission = new NetBoxApi.WritableObjectPermission(); // WritableObjectPermission | 
apiInstance.usersPermissionsBulkUpdate(writableObjectPermission, (error, data, response) => {
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
 **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | 

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersPermissionsCreate

> ObjectPermission usersPermissionsCreate(writableObjectPermission)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let writableObjectPermission = new NetBoxApi.WritableObjectPermission(); // WritableObjectPermission | 
apiInstance.usersPermissionsCreate(writableObjectPermission, (error, data, response) => {
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
 **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | 

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersPermissionsDelete

> usersPermissionsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this permission.
apiInstance.usersPermissionsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this permission. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersPermissionsList

> UsersPermissionsList200Response usersPermissionsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let opts = {
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'enabled': "enabled_example", // String | 
  'objectTypes': "objectTypes_example", // String | 
  'description': "description_example", // String | 
  'q': "q_example", // String | 
  'userId': "userId_example", // String | 
  'user': "user_example", // String | 
  'groupId': "groupId_example", // String | 
  'group': "group_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'nameEmpty': "nameEmpty_example", // String | 
  'objectTypesN': "objectTypesN_example", // String | 
  'descriptionN': "descriptionN_example", // String | 
  'descriptionIc': "descriptionIc_example", // String | 
  'descriptionNic': "descriptionNic_example", // String | 
  'descriptionIew': "descriptionIew_example", // String | 
  'descriptionNiew': "descriptionNiew_example", // String | 
  'descriptionIsw': "descriptionIsw_example", // String | 
  'descriptionNisw': "descriptionNisw_example", // String | 
  'descriptionIe': "descriptionIe_example", // String | 
  'descriptionNie': "descriptionNie_example", // String | 
  'descriptionEmpty': "descriptionEmpty_example", // String | 
  'userIdN': "userIdN_example", // String | 
  'userN': "userN_example", // String | 
  'groupIdN': "groupIdN_example", // String | 
  'groupN': "groupN_example", // String | 
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.usersPermissionsList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **enabled** | **String**|  | [optional] 
 **objectTypes** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **userId** | **String**|  | [optional] 
 **user** | **String**|  | [optional] 
 **groupId** | **String**|  | [optional] 
 **group** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **nameEmpty** | **String**|  | [optional] 
 **objectTypesN** | **String**|  | [optional] 
 **descriptionN** | **String**|  | [optional] 
 **descriptionIc** | **String**|  | [optional] 
 **descriptionNic** | **String**|  | [optional] 
 **descriptionIew** | **String**|  | [optional] 
 **descriptionNiew** | **String**|  | [optional] 
 **descriptionIsw** | **String**|  | [optional] 
 **descriptionNisw** | **String**|  | [optional] 
 **descriptionIe** | **String**|  | [optional] 
 **descriptionNie** | **String**|  | [optional] 
 **descriptionEmpty** | **String**|  | [optional] 
 **userIdN** | **String**|  | [optional] 
 **userN** | **String**|  | [optional] 
 **groupIdN** | **String**|  | [optional] 
 **groupN** | **String**|  | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**UsersPermissionsList200Response**](UsersPermissionsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersPermissionsPartialUpdate

> ObjectPermission usersPermissionsPartialUpdate(id, writableObjectPermission)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this permission.
let writableObjectPermission = new NetBoxApi.WritableObjectPermission(); // WritableObjectPermission | 
apiInstance.usersPermissionsPartialUpdate(id, writableObjectPermission, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this permission. | 
 **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | 

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersPermissionsRead

> ObjectPermission usersPermissionsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this permission.
apiInstance.usersPermissionsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this permission. | 

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersPermissionsUpdate

> ObjectPermission usersPermissionsUpdate(id, writableObjectPermission)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this permission.
let writableObjectPermission = new NetBoxApi.WritableObjectPermission(); // WritableObjectPermission | 
apiInstance.usersPermissionsUpdate(id, writableObjectPermission, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this permission. | 
 **writableObjectPermission** | [**WritableObjectPermission**](WritableObjectPermission.md)|  | 

### Return type

[**ObjectPermission**](ObjectPermission.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersTokensBulkDelete

> usersTokensBulkDelete()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
apiInstance.usersTokensBulkDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersTokensBulkPartialUpdate

> Token usersTokensBulkPartialUpdate(writableToken)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let writableToken = new NetBoxApi.WritableToken(); // WritableToken | 
apiInstance.usersTokensBulkPartialUpdate(writableToken, (error, data, response) => {
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
 **writableToken** | [**WritableToken**](WritableToken.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersTokensBulkUpdate

> Token usersTokensBulkUpdate(writableToken)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let writableToken = new NetBoxApi.WritableToken(); // WritableToken | 
apiInstance.usersTokensBulkUpdate(writableToken, (error, data, response) => {
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
 **writableToken** | [**WritableToken**](WritableToken.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersTokensCreate

> Token usersTokensCreate(writableToken)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let writableToken = new NetBoxApi.WritableToken(); // WritableToken | 
apiInstance.usersTokensCreate(writableToken, (error, data, response) => {
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
 **writableToken** | [**WritableToken**](WritableToken.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersTokensDelete

> usersTokensDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this token.
apiInstance.usersTokensDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this token. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersTokensList

> UsersTokensList200Response usersTokensList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let opts = {
  'id': "id_example", // String | 
  'key': "key_example", // String | 
  'writeEnabled': "writeEnabled_example", // String | 
  'description': "description_example", // String | 
  'q': "q_example", // String | 
  'userId': "userId_example", // String | 
  'user': "user_example", // String | 
  'created': "created_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'expires': "expires_example", // String | 
  'expiresGte': "expiresGte_example", // String | 
  'expiresLte': "expiresLte_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'keyN': "keyN_example", // String | 
  'keyIc': "keyIc_example", // String | 
  'keyNic': "keyNic_example", // String | 
  'keyIew': "keyIew_example", // String | 
  'keyNiew': "keyNiew_example", // String | 
  'keyIsw': "keyIsw_example", // String | 
  'keyNisw': "keyNisw_example", // String | 
  'keyIe': "keyIe_example", // String | 
  'keyNie': "keyNie_example", // String | 
  'keyEmpty': "keyEmpty_example", // String | 
  'descriptionN': "descriptionN_example", // String | 
  'descriptionIc': "descriptionIc_example", // String | 
  'descriptionNic': "descriptionNic_example", // String | 
  'descriptionIew': "descriptionIew_example", // String | 
  'descriptionNiew': "descriptionNiew_example", // String | 
  'descriptionIsw': "descriptionIsw_example", // String | 
  'descriptionNisw': "descriptionNisw_example", // String | 
  'descriptionIe': "descriptionIe_example", // String | 
  'descriptionNie': "descriptionNie_example", // String | 
  'descriptionEmpty': "descriptionEmpty_example", // String | 
  'userIdN': "userIdN_example", // String | 
  'userN': "userN_example", // String | 
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.usersTokensList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **key** | **String**|  | [optional] 
 **writeEnabled** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **userId** | **String**|  | [optional] 
 **user** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **expires** | **String**|  | [optional] 
 **expiresGte** | **String**|  | [optional] 
 **expiresLte** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **keyN** | **String**|  | [optional] 
 **keyIc** | **String**|  | [optional] 
 **keyNic** | **String**|  | [optional] 
 **keyIew** | **String**|  | [optional] 
 **keyNiew** | **String**|  | [optional] 
 **keyIsw** | **String**|  | [optional] 
 **keyNisw** | **String**|  | [optional] 
 **keyIe** | **String**|  | [optional] 
 **keyNie** | **String**|  | [optional] 
 **keyEmpty** | **String**|  | [optional] 
 **descriptionN** | **String**|  | [optional] 
 **descriptionIc** | **String**|  | [optional] 
 **descriptionNic** | **String**|  | [optional] 
 **descriptionIew** | **String**|  | [optional] 
 **descriptionNiew** | **String**|  | [optional] 
 **descriptionIsw** | **String**|  | [optional] 
 **descriptionNisw** | **String**|  | [optional] 
 **descriptionIe** | **String**|  | [optional] 
 **descriptionNie** | **String**|  | [optional] 
 **descriptionEmpty** | **String**|  | [optional] 
 **userIdN** | **String**|  | [optional] 
 **userN** | **String**|  | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**UsersTokensList200Response**](UsersTokensList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersTokensPartialUpdate

> Token usersTokensPartialUpdate(id, writableToken)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this token.
let writableToken = new NetBoxApi.WritableToken(); // WritableToken | 
apiInstance.usersTokensPartialUpdate(id, writableToken, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this token. | 
 **writableToken** | [**WritableToken**](WritableToken.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersTokensProvisionCreate

> usersTokensProvisionCreate()



Non-authenticated REST API endpoint via which a user may create a Token.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
apiInstance.usersTokensProvisionCreate((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersTokensRead

> Token usersTokensRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this token.
apiInstance.usersTokensRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this token. | 

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersTokensUpdate

> Token usersTokensUpdate(id, writableToken)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this token.
let writableToken = new NetBoxApi.WritableToken(); // WritableToken | 
apiInstance.usersTokensUpdate(id, writableToken, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this token. | 
 **writableToken** | [**WritableToken**](WritableToken.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUsersBulkDelete

> usersUsersBulkDelete()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
apiInstance.usersUsersBulkDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersUsersBulkPartialUpdate

> User usersUsersBulkPartialUpdate(writableUser)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let writableUser = new NetBoxApi.WritableUser(); // WritableUser | 
apiInstance.usersUsersBulkPartialUpdate(writableUser, (error, data, response) => {
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
 **writableUser** | [**WritableUser**](WritableUser.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUsersBulkUpdate

> User usersUsersBulkUpdate(writableUser)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let writableUser = new NetBoxApi.WritableUser(); // WritableUser | 
apiInstance.usersUsersBulkUpdate(writableUser, (error, data, response) => {
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
 **writableUser** | [**WritableUser**](WritableUser.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUsersCreate

> User usersUsersCreate(writableUser)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let writableUser = new NetBoxApi.WritableUser(); // WritableUser | 
apiInstance.usersUsersCreate(writableUser, (error, data, response) => {
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
 **writableUser** | [**WritableUser**](WritableUser.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUsersDelete

> usersUsersDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this user.
apiInstance.usersUsersDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this user. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## usersUsersList

> UsersUsersList200Response usersUsersList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let opts = {
  'id': "id_example", // String | 
  'username': "username_example", // String | 
  'firstName': "firstName_example", // String | 
  'lastName': "lastName_example", // String | 
  'email': "email_example", // String | 
  'isStaff': "isStaff_example", // String | 
  'isActive': "isActive_example", // String | 
  'q': "q_example", // String | 
  'groupId': "groupId_example", // String | 
  'group': "group_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'usernameN': "usernameN_example", // String | 
  'usernameIc': "usernameIc_example", // String | 
  'usernameNic': "usernameNic_example", // String | 
  'usernameIew': "usernameIew_example", // String | 
  'usernameNiew': "usernameNiew_example", // String | 
  'usernameIsw': "usernameIsw_example", // String | 
  'usernameNisw': "usernameNisw_example", // String | 
  'usernameIe': "usernameIe_example", // String | 
  'usernameNie': "usernameNie_example", // String | 
  'usernameEmpty': "usernameEmpty_example", // String | 
  'firstNameN': "firstNameN_example", // String | 
  'firstNameIc': "firstNameIc_example", // String | 
  'firstNameNic': "firstNameNic_example", // String | 
  'firstNameIew': "firstNameIew_example", // String | 
  'firstNameNiew': "firstNameNiew_example", // String | 
  'firstNameIsw': "firstNameIsw_example", // String | 
  'firstNameNisw': "firstNameNisw_example", // String | 
  'firstNameIe': "firstNameIe_example", // String | 
  'firstNameNie': "firstNameNie_example", // String | 
  'firstNameEmpty': "firstNameEmpty_example", // String | 
  'lastNameN': "lastNameN_example", // String | 
  'lastNameIc': "lastNameIc_example", // String | 
  'lastNameNic': "lastNameNic_example", // String | 
  'lastNameIew': "lastNameIew_example", // String | 
  'lastNameNiew': "lastNameNiew_example", // String | 
  'lastNameIsw': "lastNameIsw_example", // String | 
  'lastNameNisw': "lastNameNisw_example", // String | 
  'lastNameIe': "lastNameIe_example", // String | 
  'lastNameNie': "lastNameNie_example", // String | 
  'lastNameEmpty': "lastNameEmpty_example", // String | 
  'emailN': "emailN_example", // String | 
  'emailIc': "emailIc_example", // String | 
  'emailNic': "emailNic_example", // String | 
  'emailIew': "emailIew_example", // String | 
  'emailNiew': "emailNiew_example", // String | 
  'emailIsw': "emailIsw_example", // String | 
  'emailNisw': "emailNisw_example", // String | 
  'emailIe': "emailIe_example", // String | 
  'emailNie': "emailNie_example", // String | 
  'emailEmpty': "emailEmpty_example", // String | 
  'groupIdN': "groupIdN_example", // String | 
  'groupN': "groupN_example", // String | 
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.usersUsersList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **username** | **String**|  | [optional] 
 **firstName** | **String**|  | [optional] 
 **lastName** | **String**|  | [optional] 
 **email** | **String**|  | [optional] 
 **isStaff** | **String**|  | [optional] 
 **isActive** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **groupId** | **String**|  | [optional] 
 **group** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **usernameN** | **String**|  | [optional] 
 **usernameIc** | **String**|  | [optional] 
 **usernameNic** | **String**|  | [optional] 
 **usernameIew** | **String**|  | [optional] 
 **usernameNiew** | **String**|  | [optional] 
 **usernameIsw** | **String**|  | [optional] 
 **usernameNisw** | **String**|  | [optional] 
 **usernameIe** | **String**|  | [optional] 
 **usernameNie** | **String**|  | [optional] 
 **usernameEmpty** | **String**|  | [optional] 
 **firstNameN** | **String**|  | [optional] 
 **firstNameIc** | **String**|  | [optional] 
 **firstNameNic** | **String**|  | [optional] 
 **firstNameIew** | **String**|  | [optional] 
 **firstNameNiew** | **String**|  | [optional] 
 **firstNameIsw** | **String**|  | [optional] 
 **firstNameNisw** | **String**|  | [optional] 
 **firstNameIe** | **String**|  | [optional] 
 **firstNameNie** | **String**|  | [optional] 
 **firstNameEmpty** | **String**|  | [optional] 
 **lastNameN** | **String**|  | [optional] 
 **lastNameIc** | **String**|  | [optional] 
 **lastNameNic** | **String**|  | [optional] 
 **lastNameIew** | **String**|  | [optional] 
 **lastNameNiew** | **String**|  | [optional] 
 **lastNameIsw** | **String**|  | [optional] 
 **lastNameNisw** | **String**|  | [optional] 
 **lastNameIe** | **String**|  | [optional] 
 **lastNameNie** | **String**|  | [optional] 
 **lastNameEmpty** | **String**|  | [optional] 
 **emailN** | **String**|  | [optional] 
 **emailIc** | **String**|  | [optional] 
 **emailNic** | **String**|  | [optional] 
 **emailIew** | **String**|  | [optional] 
 **emailNiew** | **String**|  | [optional] 
 **emailIsw** | **String**|  | [optional] 
 **emailNisw** | **String**|  | [optional] 
 **emailIe** | **String**|  | [optional] 
 **emailNie** | **String**|  | [optional] 
 **emailEmpty** | **String**|  | [optional] 
 **groupIdN** | **String**|  | [optional] 
 **groupN** | **String**|  | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**UsersUsersList200Response**](UsersUsersList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUsersPartialUpdate

> User usersUsersPartialUpdate(id, writableUser)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this user.
let writableUser = new NetBoxApi.WritableUser(); // WritableUser | 
apiInstance.usersUsersPartialUpdate(id, writableUser, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this user. | 
 **writableUser** | [**WritableUser**](WritableUser.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersUsersRead

> User usersUsersRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this user.
apiInstance.usersUsersRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this user. | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUsersUpdate

> User usersUsersUpdate(id, writableUser)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.UsersApi();
let id = 56; // Number | A unique integer value identifying this user.
let writableUser = new NetBoxApi.WritableUser(); // WritableUser | 
apiInstance.usersUsersUpdate(id, writableUser, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this user. | 
 **writableUser** | [**WritableUser**](WritableUser.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

