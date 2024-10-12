# ManagedLabsClient.UsersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersCreateOrUpdate**](UsersApi.md#usersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName} | 
[**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName} | 
[**usersGet**](UsersApi.md#usersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName} | 
[**usersList**](UsersApi.md#usersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users | 
[**usersUpdate**](UsersApi.md#usersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName} | 



## usersCreateOrUpdate

> User usersCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user)



Create or replace an existing User.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let user = new ManagedLabsClient.User(); // User | The User registered to a lab
apiInstance.usersCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **user** | [**User**](User.md)| The User registered to a lab | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersDelete

> usersDelete(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion)



Delete user. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.usersDelete(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGet

> User usersGet(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, opts)



Get user

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=email)'
};
apiInstance.usersGet(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, opts, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;email)&#39; | [optional] 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersList

> ResponseWithContinuationUser usersList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, opts)



List users in a given lab.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=email)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.usersList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, opts, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;email)&#39; | [optional] 
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

> User usersUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user)



Modify properties of users.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.UsersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let user = new ManagedLabsClient.UserFragment(); // UserFragment | The User registered to a lab
apiInstance.usersUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user, (error, data, response) => {
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
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **user** | [**UserFragment**](UserFragment.md)| The User registered to a lab | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

