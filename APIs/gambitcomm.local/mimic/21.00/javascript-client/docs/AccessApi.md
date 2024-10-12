# MimicRestApi.AccessApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accessAdd**](AccessApi.md#accessAdd) | **POST** /mimic/access/add/{user}/{agents}/{mask} | Adds/Overwrites the user entry in the access control database.
[**accessDel**](AccessApi.md#accessDel) | **DELETE** /mimic/access/del/{user} | Clears a users entry from access control database.
[**accessGetAcldb**](AccessApi.md#accessGetAcldb) | **GET** /mimic/access/get/acldb | Returns the current access control database in use.
[**accessGetAdmindir**](AccessApi.md#accessGetAdmindir) | **GET** /mimic/access/get/admindir | Returns the current admin directory.
[**accessGetAdminuser**](AccessApi.md#accessGetAdminuser) | **GET** /mimic/access/get/adminuser | Returns the current administrator.
[**accessGetEnabled**](AccessApi.md#accessGetEnabled) | **GET** /mimic/access/get/enabled | Returns the state of access control checking.
[**accessList**](AccessApi.md#accessList) | **GET** /mimic/access/list | Returns an array of entries.
[**accessLoad**](AccessApi.md#accessLoad) | **PUT** /mimic/access/load/{filename} | Loads the specified file for access control data.
[**accessSave**](AccessApi.md#accessSave) | **PUT** /mimic/access/save/{filename} | Saves current access control data in specified file.
[**accessSetAcldb**](AccessApi.md#accessSetAcldb) | **PUT** /mimic/access/set/acldb/{databaseName} | Allows setting the name of the current access control database.
[**accessSetEnabled**](AccessApi.md#accessSetEnabled) | **PUT** /mimic/access/set/enabled/{enabledOrNot} | Allows the user to enable/disable the access control check.



## accessAdd

> String accessAdd(user, agents, mask)

Adds/Overwrites the user entry in the access control database.

Adds/Overwrites the user entry in the access control database.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
let user = "user_example"; // String | Username of the simulator hosting system
let agents = "agents_example"; // String | Agent range in minimal range representation
let mask = "mask_example"; // String | Currently not used
apiInstance.accessAdd(user, agents, mask, (error, data, response) => {
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
 **user** | **String**| Username of the simulator hosting system | 
 **agents** | **String**| Agent range in minimal range representation | 
 **mask** | **String**| Currently not used | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessDel

> String accessDel(user)

Clears a users entry from access control database.

Using &#39;*&#39; for user clears all the users.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
let user = "user_example"; // String | username of the simulator hosting system
apiInstance.accessDel(user, (error, data, response) => {
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
 **user** | **String**| username of the simulator hosting system | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessGetAcldb

> String accessGetAcldb()

Returns the current access control database in use.

If nothing is specified then this returns \&quot;\&quot;.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
apiInstance.accessGetAcldb((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessGetAdmindir

> String accessGetAdmindir()

Returns the current admin directory.

If nothing is specified in admin/settings.cfg then returns \&quot;\&quot;. If no admin directory is specified then the shared area will be used where needed (e.g. for persistent info, access control data files etc. )

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
apiInstance.accessGetAdmindir((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessGetAdminuser

> String accessGetAdminuser()

Returns the current administrator.

If nothing is specified in admin/settings.cfg then returns \&quot;\&quot;.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
apiInstance.accessGetAdminuser((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessGetEnabled

> String accessGetEnabled()

Returns the state of access control checking.

0 indicates that it is disabled, 1 indicates it is enabled.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
apiInstance.accessGetEnabled((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessList

> [AccessEntry] accessList()

Returns an array of entries.

Each entry consists of user, agents (in minimal range representation) and access mask (not used currently).

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
apiInstance.accessList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[AccessEntry]**](AccessEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessLoad

> [String] accessLoad(filename)

Loads the specified file for access control data.

If filename is not specified then the currently set &#39;acldb&#39; parameter is used.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
let filename = "filename_example"; // String | Filename to load
apiInstance.accessLoad(filename, (error, data, response) => {
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
 **filename** | **String**| Filename to load | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessSave

> [String] accessSave(filename)

Saves current access control data in specified file.

If filename is not specified then the currently set &#39;acldb&#39; parameter is used.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
let filename = "filename_example"; // String | Filename to save
apiInstance.accessSave(filename, (error, data, response) => {
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
 **filename** | **String**| Filename to save | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessSetAcldb

> String accessSetAcldb(databaseName)

Allows setting the name of the current access control database.

This will be used for subsequent load and save operations.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
let databaseName = "databaseName_example"; // String | Database name to use
apiInstance.accessSetAcldb(databaseName, (error, data, response) => {
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
 **databaseName** | **String**| Database name to use | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessSetEnabled

> String accessSetEnabled(enabledOrNot)

Allows the user to enable/disable the access control check.

0 indicates disabled, 1 indicates enabled.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.AccessApi();
let enabledOrNot = "enabledOrNot_example"; // String | indicator
apiInstance.accessSetEnabled(enabledOrNot, (error, data, response) => {
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
 **enabledOrNot** | **String**| indicator | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

