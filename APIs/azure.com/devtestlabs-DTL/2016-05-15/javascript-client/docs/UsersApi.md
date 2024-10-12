# DevTestLabsClient.UsersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersCreateOrUpdate**](UsersApi.md#usersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{name} | 
[**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{name} | 
[**usersGet**](UsersApi.md#usersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{name} | 
[**usersList**](UsersApi.md#usersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users | 
[**usersUpdate**](UsersApi.md#usersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{name} | 



## usersCreateOrUpdate

> User usersCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, user)



Create or replace an existing user profile.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the user profile.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let user = new DevTestLabsClient.User(); // User | Profile of a lab user.
apiInstance.usersCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, user, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the user profile. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **user** | [**User**](User.md)| Profile of a lab user. | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersDelete

> usersDelete(subscriptionId, resourceGroupName, labName, name, apiVersion)



Delete user profile. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the user profile.
let apiVersion = "'2016-05-15'"; // String | Client API version.
apiInstance.usersDelete(subscriptionId, resourceGroupName, labName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the user profile. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGet

> User usersGet(subscriptionId, resourceGroupName, labName, name, apiVersion, opts)



Get user profile.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the user profile.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=identity)'
};
apiInstance.usersGet(subscriptionId, resourceGroupName, labName, name, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the user profile. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;identity)&#39; | [optional] 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersList

> ResponseWithContinuationUser usersList(subscriptionId, resourceGroupName, labName, apiVersion, opts)



List user profiles in a given lab.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=identity)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.usersList(subscriptionId, resourceGroupName, labName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;identity)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationUser**](ResponseWithContinuationUser.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUpdate

> User usersUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, user)



Modify properties of user profiles.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let name = "name_example"; // String | The name of the user profile.
let apiVersion = "'2016-05-15'"; // String | Client API version.
let user = new DevTestLabsClient.UserFragment(); // UserFragment | Profile of a lab user.
apiInstance.usersUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, user, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **name** | **String**| The name of the user profile. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-15&#39;]
 **user** | [**UserFragment**](UserFragment.md)| Profile of a lab user. | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

