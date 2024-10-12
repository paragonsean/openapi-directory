# ManagedServiceIdentityClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.ManagedIdentity/operations | 
[**userAssignedIdentitiesCreateOrUpdate**](DefaultApi.md#userAssignedIdentitiesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName} | 
[**userAssignedIdentitiesDelete**](DefaultApi.md#userAssignedIdentitiesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName} | 
[**userAssignedIdentitiesGet**](DefaultApi.md#userAssignedIdentitiesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName} | 
[**userAssignedIdentitiesListByResourceGroup**](DefaultApi.md#userAssignedIdentitiesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities | 
[**userAssignedIdentitiesListBySubscription**](DefaultApi.md#userAssignedIdentitiesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ManagedIdentity/userAssignedIdentities | 
[**userAssignedIdentitiesUpdate**](DefaultApi.md#userAssignedIdentitiesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{resourceName} | 



## operationsList

> OperationListResult operationsList(apiVersion)



Lists available operations for the Microsoft.ManagedIdentity provider

### Example

```javascript
import ManagedServiceIdentityClient from 'managed_service_identity_client';
let defaultClient = ManagedServiceIdentityClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServiceIdentityClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Version of API to invoke.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of API to invoke. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userAssignedIdentitiesCreateOrUpdate

> Identity userAssignedIdentitiesCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, parameters)



Create or update an identity in the specified subscription and resource group.

### Example

```javascript
import ManagedServiceIdentityClient from 'managed_service_identity_client';
let defaultClient = ManagedServiceIdentityClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServiceIdentityClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
let resourceName = "resourceName_example"; // String | The name of the identity resource.
let apiVersion = "apiVersion_example"; // String | Version of API to invoke.
let parameters = new ManagedServiceIdentityClient.Identity(); // Identity | Parameters to create or update the identity
apiInstance.userAssignedIdentitiesCreateOrUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | 
 **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | 
 **resourceName** | **String**| The name of the identity resource. | 
 **apiVersion** | **String**| Version of API to invoke. | 
 **parameters** | [**Identity**](Identity.md)| Parameters to create or update the identity | 

### Return type

[**Identity**](Identity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## userAssignedIdentitiesDelete

> userAssignedIdentitiesDelete(subscriptionId, resourceGroupName, resourceName, apiVersion)



Deletes the identity.

### Example

```javascript
import ManagedServiceIdentityClient from 'managed_service_identity_client';
let defaultClient = ManagedServiceIdentityClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServiceIdentityClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
let resourceName = "resourceName_example"; // String | The name of the identity resource.
let apiVersion = "apiVersion_example"; // String | Version of API to invoke.
apiInstance.userAssignedIdentitiesDelete(subscriptionId, resourceGroupName, resourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | 
 **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | 
 **resourceName** | **String**| The name of the identity resource. | 
 **apiVersion** | **String**| Version of API to invoke. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userAssignedIdentitiesGet

> Identity userAssignedIdentitiesGet(subscriptionId, resourceGroupName, resourceName, apiVersion)



Gets the identity.

### Example

```javascript
import ManagedServiceIdentityClient from 'managed_service_identity_client';
let defaultClient = ManagedServiceIdentityClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServiceIdentityClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
let resourceName = "resourceName_example"; // String | The name of the identity resource.
let apiVersion = "apiVersion_example"; // String | Version of API to invoke.
apiInstance.userAssignedIdentitiesGet(subscriptionId, resourceGroupName, resourceName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | 
 **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | 
 **resourceName** | **String**| The name of the identity resource. | 
 **apiVersion** | **String**| Version of API to invoke. | 

### Return type

[**Identity**](Identity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userAssignedIdentitiesListByResourceGroup

> UserAssignedIdentitiesListResult userAssignedIdentitiesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the userAssignedIdentities available under the specified ResourceGroup.

### Example

```javascript
import ManagedServiceIdentityClient from 'managed_service_identity_client';
let defaultClient = ManagedServiceIdentityClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServiceIdentityClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
let apiVersion = "apiVersion_example"; // String | Version of API to invoke.
apiInstance.userAssignedIdentitiesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | 
 **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | 
 **apiVersion** | **String**| Version of API to invoke. | 

### Return type

[**UserAssignedIdentitiesListResult**](UserAssignedIdentitiesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userAssignedIdentitiesListBySubscription

> UserAssignedIdentitiesListResult userAssignedIdentitiesListBySubscription(subscriptionId, apiVersion)



Lists all the userAssignedIdentities available under the specified subscription.

### Example

```javascript
import ManagedServiceIdentityClient from 'managed_service_identity_client';
let defaultClient = ManagedServiceIdentityClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServiceIdentityClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
let apiVersion = "apiVersion_example"; // String | Version of API to invoke.
apiInstance.userAssignedIdentitiesListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | 
 **apiVersion** | **String**| Version of API to invoke. | 

### Return type

[**UserAssignedIdentitiesListResult**](UserAssignedIdentitiesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userAssignedIdentitiesUpdate

> Identity userAssignedIdentitiesUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, parameters)



Update an identity in the specified subscription and resource group.

### Example

```javascript
import ManagedServiceIdentityClient from 'managed_service_identity_client';
let defaultClient = ManagedServiceIdentityClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedServiceIdentityClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Id of the Subscription to which the identity belongs.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the identity belongs.
let resourceName = "resourceName_example"; // String | The name of the identity resource.
let apiVersion = "apiVersion_example"; // String | Version of API to invoke.
let parameters = new ManagedServiceIdentityClient.Identity(); // Identity | Parameters to update the identity
apiInstance.userAssignedIdentitiesUpdate(subscriptionId, resourceGroupName, resourceName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Id of the Subscription to which the identity belongs. | 
 **resourceGroupName** | **String**| The name of the Resource Group to which the identity belongs. | 
 **resourceName** | **String**| The name of the identity resource. | 
 **apiVersion** | **String**| Version of API to invoke. | 
 **parameters** | [**Identity**](Identity.md)| Parameters to update the identity | 

### Return type

[**Identity**](Identity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

