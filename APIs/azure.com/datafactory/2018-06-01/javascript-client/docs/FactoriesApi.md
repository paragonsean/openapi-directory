# DataFactoryManagementClient.FactoriesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factoriesConfigureFactoryRepo**](FactoriesApi.md#factoriesConfigureFactoryRepo) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/configureFactoryRepo | 
[**factoriesCreateOrUpdate**](FactoriesApi.md#factoriesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName} | 
[**factoriesDelete**](FactoriesApi.md#factoriesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName} | 
[**factoriesGet**](FactoriesApi.md#factoriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName} | 
[**factoriesGetDataPlaneAccess**](FactoriesApi.md#factoriesGetDataPlaneAccess) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getDataPlaneAccess | 
[**factoriesGetGitHubAccessToken**](FactoriesApi.md#factoriesGetGitHubAccessToken) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getGitHubAccessToken | 
[**factoriesList**](FactoriesApi.md#factoriesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/factories | 
[**factoriesListByResourceGroup**](FactoriesApi.md#factoriesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories | 
[**factoriesUpdate**](FactoriesApi.md#factoriesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName} | 



## factoriesConfigureFactoryRepo

> Factory factoriesConfigureFactoryRepo(subscriptionId, locationId, apiVersion, factoryRepoUpdate)



Updates a factory&#39;s repo information.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.FactoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let locationId = "locationId_example"; // String | The location identifier.
let apiVersion = "apiVersion_example"; // String | The API version.
let factoryRepoUpdate = new DataFactoryManagementClient.FactoryRepoUpdate(); // FactoryRepoUpdate | Update factory repo request definition.
apiInstance.factoriesConfigureFactoryRepo(subscriptionId, locationId, apiVersion, factoryRepoUpdate, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **locationId** | **String**| The location identifier. | 
 **apiVersion** | **String**| The API version. | 
 **factoryRepoUpdate** | [**FactoryRepoUpdate**](FactoryRepoUpdate.md)| Update factory repo request definition. | 

### Return type

[**Factory**](Factory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## factoriesCreateOrUpdate

> Factory factoriesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, apiVersion, factory, opts)



Creates or updates a factory.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.FactoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let factory = new DataFactoryManagementClient.Factory(); // Factory | Factory resource definition.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the factory entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
};
apiInstance.factoriesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, apiVersion, factory, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **apiVersion** | **String**| The API version. | 
 **factory** | [**Factory**](Factory.md)| Factory resource definition. | 
 **ifMatch** | **String**| ETag of the factory entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] 

### Return type

[**Factory**](Factory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## factoriesDelete

> factoriesDelete(subscriptionId, resourceGroupName, factoryName, apiVersion)



Deletes a factory.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.FactoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.factoriesDelete(subscriptionId, resourceGroupName, factoryName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factoriesGet

> Factory factoriesGet(subscriptionId, resourceGroupName, factoryName, apiVersion, opts)



Gets a factory.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.FactoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag of the factory entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
};
apiInstance.factoriesGet(subscriptionId, resourceGroupName, factoryName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **apiVersion** | **String**| The API version. | 
 **ifNoneMatch** | **String**| ETag of the factory entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. | [optional] 

### Return type

[**Factory**](Factory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factoriesGetDataPlaneAccess

> AccessPolicyResponse factoriesGetDataPlaneAccess(subscriptionId, resourceGroupName, factoryName, apiVersion, policy)



Get Data Plane access.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.FactoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let policy = new DataFactoryManagementClient.UserAccessPolicy(); // UserAccessPolicy | Data Plane user access policy definition.
apiInstance.factoriesGetDataPlaneAccess(subscriptionId, resourceGroupName, factoryName, apiVersion, policy, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **apiVersion** | **String**| The API version. | 
 **policy** | [**UserAccessPolicy**](UserAccessPolicy.md)| Data Plane user access policy definition. | 

### Return type

[**AccessPolicyResponse**](AccessPolicyResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## factoriesGetGitHubAccessToken

> GitHubAccessTokenResponse factoriesGetGitHubAccessToken(subscriptionId, resourceGroupName, factoryName, apiVersion, gitHubAccessTokenRequest)



Get GitHub Access Token.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.FactoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let gitHubAccessTokenRequest = new DataFactoryManagementClient.GitHubAccessTokenRequest(); // GitHubAccessTokenRequest | Get GitHub access token request definition.
apiInstance.factoriesGetGitHubAccessToken(subscriptionId, resourceGroupName, factoryName, apiVersion, gitHubAccessTokenRequest, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **apiVersion** | **String**| The API version. | 
 **gitHubAccessTokenRequest** | [**GitHubAccessTokenRequest**](GitHubAccessTokenRequest.md)| Get GitHub access token request definition. | 

### Return type

[**GitHubAccessTokenResponse**](GitHubAccessTokenResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## factoriesList

> FactoryListResponse factoriesList(subscriptionId, apiVersion)



Lists factories under the specified subscription.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.FactoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.factoriesList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**FactoryListResponse**](FactoryListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factoriesListByResourceGroup

> FactoryListResponse factoriesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists factories.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.FactoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.factoriesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**FactoryListResponse**](FactoryListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factoriesUpdate

> Factory factoriesUpdate(subscriptionId, resourceGroupName, factoryName, apiVersion, factoryUpdateParameters)



Updates a factory.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.FactoriesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let factoryUpdateParameters = new DataFactoryManagementClient.FactoryUpdateParameters(); // FactoryUpdateParameters | The parameters for updating a factory.
apiInstance.factoriesUpdate(subscriptionId, resourceGroupName, factoryName, apiVersion, factoryUpdateParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **apiVersion** | **String**| The API version. | 
 **factoryUpdateParameters** | [**FactoryUpdateParameters**](FactoryUpdateParameters.md)| The parameters for updating a factory. | 

### Return type

[**Factory**](Factory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

