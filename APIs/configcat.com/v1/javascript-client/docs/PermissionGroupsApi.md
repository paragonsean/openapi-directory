# ConfigCatPublicManagementApi.PermissionGroupsApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPermissionGroup**](PermissionGroupsApi.md#createPermissionGroup) | **POST** /v1/products/{productId}/permissions | Create Permission Group
[**deletePermissionGroup**](PermissionGroupsApi.md#deletePermissionGroup) | **DELETE** /v1/permissions/{permissionGroupId} | Delete Permission Group
[**getPermissionGroup**](PermissionGroupsApi.md#getPermissionGroup) | **GET** /v1/permissions/{permissionGroupId} | Get Permission Group
[**getPermissionGroups**](PermissionGroupsApi.md#getPermissionGroups) | **GET** /v1/products/{productId}/permissions | List Permission Groups
[**updatePermissionGroup**](PermissionGroupsApi.md#updatePermissionGroup) | **PUT** /v1/permissions/{permissionGroupId} | Update Permission Group



## createPermissionGroup

> PermissionGroupModelHaljson createPermissionGroup(productId, createPermissionGroupRequest)

Create Permission Group

This endpoint creates a new Permission Group in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.PermissionGroupsApi();
let productId = "productId_example"; // String | The identifier of the Product.
let createPermissionGroupRequest = new ConfigCatPublicManagementApi.CreatePermissionGroupRequest(); // CreatePermissionGroupRequest | 
apiInstance.createPermissionGroup(productId, createPermissionGroupRequest, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 
 **createPermissionGroupRequest** | [**CreatePermissionGroupRequest**](CreatePermissionGroupRequest.md)|  | 

### Return type

[**PermissionGroupModelHaljson**](PermissionGroupModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## deletePermissionGroup

> deletePermissionGroup(permissionGroupId)

Delete Permission Group

This endpoint removes a Permission Group identified by the &#x60;permissionGroupId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.PermissionGroupsApi();
let permissionGroupId = 789; // Number | The identifier of the Permission Group.
apiInstance.deletePermissionGroup(permissionGroupId, (error, data, response) => {
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
 **permissionGroupId** | **Number**| The identifier of the Permission Group. | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPermissionGroup

> PermissionGroupModelHaljson getPermissionGroup(permissionGroupId)

Get Permission Group

This endpoint returns the metadata of a Permission Group  identified by the &#x60;permissionGroupId&#x60;.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.PermissionGroupsApi();
let permissionGroupId = 789; // Number | The identifier of the Permission Group.
apiInstance.getPermissionGroup(permissionGroupId, (error, data, response) => {
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
 **permissionGroupId** | **Number**| The identifier of the Permission Group. | 

### Return type

[**PermissionGroupModelHaljson**](PermissionGroupModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getPermissionGroups

> [PermissionGroupModelHaljson] getPermissionGroups(productId)

List Permission Groups

This endpoint returns the list of the Permission Groups that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.PermissionGroupsApi();
let productId = "productId_example"; // String | The identifier of the Product.
apiInstance.getPermissionGroups(productId, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 

### Return type

[**[PermissionGroupModelHaljson]**](PermissionGroupModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## updatePermissionGroup

> PermissionGroupModelHaljson updatePermissionGroup(permissionGroupId, updatePermissionGroupRequest)

Update Permission Group

This endpoint updates a Permission Group identified by the &#x60;permissionGroupId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.PermissionGroupsApi();
let permissionGroupId = 789; // Number | The identifier of the Permission Group.
let updatePermissionGroupRequest = new ConfigCatPublicManagementApi.UpdatePermissionGroupRequest(); // UpdatePermissionGroupRequest | 
apiInstance.updatePermissionGroup(permissionGroupId, updatePermissionGroupRequest, (error, data, response) => {
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
 **permissionGroupId** | **Number**| The identifier of the Permission Group. | 
 **updatePermissionGroupRequest** | [**UpdatePermissionGroupRequest**](UpdatePermissionGroupRequest.md)|  | 

### Return type

[**PermissionGroupModelHaljson**](PermissionGroupModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json

