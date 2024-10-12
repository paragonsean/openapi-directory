# VisualStudioResourceProviderClient.AccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsCheckNameAvailability**](AccountsApi.md#accountsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/microsoft.visualstudio/checkNameAvailability | Accounts_CheckNameAvailability
[**accountsCreateOrUpdate**](AccountsApi.md#accountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{resourceName} | Accounts_CreateOrUpdate
[**accountsDelete**](AccountsApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{resourceName} | Accounts_Delete
[**accountsGet**](AccountsApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{resourceName} | Accounts_Get
[**accountsListByResourceGroup**](AccountsApi.md#accountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account | Accounts_ListByResourceGroup
[**accountsUpdate**](AccountsApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{resourceName} | Accounts_Update



## accountsCheckNameAvailability

> CheckNameAvailabilityResult accountsCheckNameAvailability(subscriptionId, apiVersion, body)

Accounts_CheckNameAvailability

Checks if the specified Visual Studio Team Services account name is available. Resource name can be either an account name or an account name and PUID.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let body = new VisualStudioResourceProviderClient.CheckNameAvailabilityParameter(); // CheckNameAvailabilityParameter | Parameters describing the name to check availability for.
apiInstance.accountsCheckNameAvailability(subscriptionId, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **body** | [**CheckNameAvailabilityParameter**](CheckNameAvailabilityParameter.md)| Parameters describing the name to check availability for. | 

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsCreateOrUpdate

> AccountResource accountsCreateOrUpdate(resourceGroupName, subscriptionId, apiVersion, resourceName, body)

Accounts_CreateOrUpdate

Creates or updates a Visual Studio Team Services account resource.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.AccountsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let resourceName = "resourceName_example"; // String | Name of the resource.
let body = new VisualStudioResourceProviderClient.AccountResourceRequest(); // AccountResourceRequest | The request data.
apiInstance.accountsCreateOrUpdate(resourceGroupName, subscriptionId, apiVersion, resourceName, body, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **resourceName** | **String**| Name of the resource. | 
 **body** | [**AccountResourceRequest**](AccountResourceRequest.md)| The request data. | 

### Return type

[**AccountResource**](AccountResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsDelete

> accountsDelete(resourceGroupName, subscriptionId, apiVersion, resourceName)

Accounts_Delete

Deletes a Visual Studio Team Services account resource.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.AccountsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let resourceName = "resourceName_example"; // String | Name of the resource.
apiInstance.accountsDelete(resourceGroupName, subscriptionId, apiVersion, resourceName, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **resourceName** | **String**| Name of the resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsGet

> AccountResource accountsGet(resourceGroupName, subscriptionId, apiVersion, resourceName)

Accounts_Get

Gets the Visual Studio Team Services account resource details.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.AccountsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let resourceName = "resourceName_example"; // String | Name of the resource.
apiInstance.accountsGet(resourceGroupName, subscriptionId, apiVersion, resourceName, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **resourceName** | **String**| Name of the resource. | 

### Return type

[**AccountResource**](AccountResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListByResourceGroup

> AccountResourceListResult accountsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Accounts_ListByResourceGroup

Gets all Visual Studio Team Services account resources under the resource group linked to the specified Azure subscription.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.AccountsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.accountsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AccountResourceListResult**](AccountResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsUpdate

> AccountResource accountsUpdate(resourceGroupName, subscriptionId, apiVersion, resourceName, body)

Accounts_Update

Updates tags for Visual Studio Team Services account resource.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.AccountsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let resourceName = "resourceName_example"; // String | Name of the resource.
let body = new VisualStudioResourceProviderClient.AccountTagRequest(); // AccountTagRequest | The request data.
apiInstance.accountsUpdate(resourceGroupName, subscriptionId, apiVersion, resourceName, body, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | 
 **subscriptionId** | **String**| The Azure subscription identifier. | 
 **apiVersion** | **String**| API Version | 
 **resourceName** | **String**| Name of the resource. | 
 **body** | [**AccountTagRequest**](AccountTagRequest.md)| The request data. | 

### Return type

[**AccountResource**](AccountResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

