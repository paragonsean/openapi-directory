# DataFactoryManagementClient.IntegrationRuntimesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationRuntimesCreateLinkedIntegrationRuntime**](IntegrationRuntimesApi.md#integrationRuntimesCreateLinkedIntegrationRuntime) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/linkedIntegrationRuntime | 
[**integrationRuntimesCreateOrUpdate**](IntegrationRuntimesApi.md#integrationRuntimesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName} | 
[**integrationRuntimesDelete**](IntegrationRuntimesApi.md#integrationRuntimesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName} | 
[**integrationRuntimesGet**](IntegrationRuntimesApi.md#integrationRuntimesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName} | 
[**integrationRuntimesGetConnectionInfo**](IntegrationRuntimesApi.md#integrationRuntimesGetConnectionInfo) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/getConnectionInfo | 
[**integrationRuntimesGetMonitoringData**](IntegrationRuntimesApi.md#integrationRuntimesGetMonitoringData) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/monitoringData | 
[**integrationRuntimesGetStatus**](IntegrationRuntimesApi.md#integrationRuntimesGetStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/getStatus | 
[**integrationRuntimesListAuthKeys**](IntegrationRuntimesApi.md#integrationRuntimesListAuthKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/listAuthKeys | 
[**integrationRuntimesListByFactory**](IntegrationRuntimesApi.md#integrationRuntimesListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes | 
[**integrationRuntimesRegenerateAuthKey**](IntegrationRuntimesApi.md#integrationRuntimesRegenerateAuthKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/regenerateAuthKey | 
[**integrationRuntimesRemoveLinks**](IntegrationRuntimesApi.md#integrationRuntimesRemoveLinks) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/removeLinks | 
[**integrationRuntimesStart**](IntegrationRuntimesApi.md#integrationRuntimesStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/start | 
[**integrationRuntimesStop**](IntegrationRuntimesApi.md#integrationRuntimesStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/stop | 
[**integrationRuntimesSyncCredentials**](IntegrationRuntimesApi.md#integrationRuntimesSyncCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/syncCredentials | 
[**integrationRuntimesUpdate**](IntegrationRuntimesApi.md#integrationRuntimesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName} | 
[**integrationRuntimesUpgrade**](IntegrationRuntimesApi.md#integrationRuntimesUpgrade) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/integrationRuntimes/{integrationRuntimeName}/upgrade | 



## integrationRuntimesCreateLinkedIntegrationRuntime

> IntegrationRuntimeStatusResponse integrationRuntimesCreateLinkedIntegrationRuntime(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, createLinkedIntegrationRuntimeRequest)



Create a linked integration runtime entry in a shared integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
let createLinkedIntegrationRuntimeRequest = new DataFactoryManagementClient.CreateLinkedIntegrationRuntimeRequest(); // CreateLinkedIntegrationRuntimeRequest | The linked integration runtime properties.
apiInstance.integrationRuntimesCreateLinkedIntegrationRuntime(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, createLinkedIntegrationRuntimeRequest, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 
 **createLinkedIntegrationRuntimeRequest** | [**CreateLinkedIntegrationRuntimeRequest**](CreateLinkedIntegrationRuntimeRequest.md)| The linked integration runtime properties. | 

### Return type

[**IntegrationRuntimeStatusResponse**](IntegrationRuntimeStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationRuntimesCreateOrUpdate

> IntegrationRuntimeResource integrationRuntimesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, integrationRuntime, opts)



Creates or updates an integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
let integrationRuntime = new DataFactoryManagementClient.IntegrationRuntimeResource(); // IntegrationRuntimeResource | Integration runtime resource definition.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the integration runtime entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
};
apiInstance.integrationRuntimesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, integrationRuntime, opts, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 
 **integrationRuntime** | [**IntegrationRuntimeResource**](IntegrationRuntimeResource.md)| Integration runtime resource definition. | 
 **ifMatch** | **String**| ETag of the integration runtime entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] 

### Return type

[**IntegrationRuntimeResource**](IntegrationRuntimeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationRuntimesDelete

> integrationRuntimesDelete(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Deletes an integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesDelete(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesGet

> IntegrationRuntimeResource integrationRuntimesGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, opts)



Gets an integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag of the integration runtime entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
};
apiInstance.integrationRuntimesGet(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, opts, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 
 **ifNoneMatch** | **String**| ETag of the integration runtime entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. | [optional] 

### Return type

[**IntegrationRuntimeResource**](IntegrationRuntimeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesGetConnectionInfo

> IntegrationRuntimesGetConnectionInfo200Response integrationRuntimesGetConnectionInfo(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Gets the on-premises integration runtime connection information for encrypting the on-premises data source credentials.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesGetConnectionInfo(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationRuntimesGetConnectionInfo200Response**](IntegrationRuntimesGetConnectionInfo200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesGetMonitoringData

> IntegrationRuntimesGetMonitoringData200Response integrationRuntimesGetMonitoringData(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Get the integration runtime monitoring data, which includes the monitor data for all the nodes under this integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesGetMonitoringData(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationRuntimesGetMonitoringData200Response**](IntegrationRuntimesGetMonitoringData200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesGetStatus

> IntegrationRuntimeStatusResponse integrationRuntimesGetStatus(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Gets detailed status information for an integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesGetStatus(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationRuntimeStatusResponse**](IntegrationRuntimeStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesListAuthKeys

> IntegrationRuntimesListAuthKeys200Response integrationRuntimesListAuthKeys(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Retrieves the authentication keys for an integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesListAuthKeys(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationRuntimesListAuthKeys200Response**](IntegrationRuntimesListAuthKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesListByFactory

> IntegrationRuntimeListResponse integrationRuntimesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists integration runtimes.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, (error, data, response) => {
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

### Return type

[**IntegrationRuntimeListResponse**](IntegrationRuntimeListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesRegenerateAuthKey

> IntegrationRuntimesListAuthKeys200Response integrationRuntimesRegenerateAuthKey(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, regenerateKeyParameters)



Regenerates the authentication key for an integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
let regenerateKeyParameters = new DataFactoryManagementClient.IntegrationRuntimesRegenerateAuthKeyRequest(); // IntegrationRuntimesRegenerateAuthKeyRequest | The parameters for regenerating integration runtime authentication key.
apiInstance.integrationRuntimesRegenerateAuthKey(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, regenerateKeyParameters, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 
 **regenerateKeyParameters** | [**IntegrationRuntimesRegenerateAuthKeyRequest**](IntegrationRuntimesRegenerateAuthKeyRequest.md)| The parameters for regenerating integration runtime authentication key. | 

### Return type

[**IntegrationRuntimesListAuthKeys200Response**](IntegrationRuntimesListAuthKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationRuntimesRemoveLinks

> integrationRuntimesRemoveLinks(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, linkedIntegrationRuntimeRequest)



Remove all linked integration runtimes under specific data factory in a self-hosted integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
let linkedIntegrationRuntimeRequest = new DataFactoryManagementClient.LinkedIntegrationRuntimeRequest(); // LinkedIntegrationRuntimeRequest | The data factory name for the linked integration runtime.
apiInstance.integrationRuntimesRemoveLinks(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, linkedIntegrationRuntimeRequest, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 
 **linkedIntegrationRuntimeRequest** | [**LinkedIntegrationRuntimeRequest**](LinkedIntegrationRuntimeRequest.md)| The data factory name for the linked integration runtime. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationRuntimesStart

> IntegrationRuntimeStatusResponse integrationRuntimesStart(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Starts a ManagedReserved type integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesStart(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationRuntimeStatusResponse**](IntegrationRuntimeStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesStop

> integrationRuntimesStop(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Stops a ManagedReserved type integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesStop(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesSyncCredentials

> integrationRuntimesSyncCredentials(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Force the integration runtime to synchronize credentials across integration runtime nodes, and this will override the credentials across all worker nodes with those available on the dispatcher node. If you already have the latest credential backup file, you should manually import it (preferred) on any self-hosted integration runtime node than using this API directly.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesSyncCredentials(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationRuntimesUpdate

> IntegrationRuntimeResource integrationRuntimesUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, updateIntegrationRuntimeRequest)



Updates an integration runtime.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
let updateIntegrationRuntimeRequest = new DataFactoryManagementClient.UpdateIntegrationRuntimeRequest(); // UpdateIntegrationRuntimeRequest | The parameters for updating an integration runtime.
apiInstance.integrationRuntimesUpdate(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, updateIntegrationRuntimeRequest, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 
 **updateIntegrationRuntimeRequest** | [**UpdateIntegrationRuntimeRequest**](UpdateIntegrationRuntimeRequest.md)| The parameters for updating an integration runtime. | 

### Return type

[**IntegrationRuntimeResource**](IntegrationRuntimeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationRuntimesUpgrade

> integrationRuntimesUpgrade(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion)



Upgrade self-hosted integration runtime to latest version if availability.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.IntegrationRuntimesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let integrationRuntimeName = "integrationRuntimeName_example"; // String | The integration runtime name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationRuntimesUpgrade(subscriptionId, resourceGroupName, factoryName, integrationRuntimeName, apiVersion, (error, data, response) => {
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
 **integrationRuntimeName** | **String**| The integration runtime name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

