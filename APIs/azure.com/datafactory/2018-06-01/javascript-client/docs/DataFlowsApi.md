# DataFactoryManagementClient.DataFlowsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataFlowsCreateOrUpdate**](DataFlowsApi.md#dataFlowsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/dataflows/{dataFlowName} | 
[**dataFlowsDelete**](DataFlowsApi.md#dataFlowsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/dataflows/{dataFlowName} | 
[**dataFlowsGet**](DataFlowsApi.md#dataFlowsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/dataflows/{dataFlowName} | 
[**dataFlowsListByFactory**](DataFlowsApi.md#dataFlowsListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/dataflows | 



## dataFlowsCreateOrUpdate

> DataFlowResource dataFlowsCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, dataFlowName, apiVersion, dataFlow, opts)



Creates or updates a data flow.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DataFlowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let dataFlowName = "dataFlowName_example"; // String | The data flow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let dataFlow = new DataFactoryManagementClient.DataFlowResource(); // DataFlowResource | Data flow resource definition.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the data flow entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
};
apiInstance.dataFlowsCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, dataFlowName, apiVersion, dataFlow, opts, (error, data, response) => {
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
 **dataFlowName** | **String**| The data flow name. | 
 **apiVersion** | **String**| The API version. | 
 **dataFlow** | [**DataFlowResource**](DataFlowResource.md)| Data flow resource definition. | 
 **ifMatch** | **String**| ETag of the data flow entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] 

### Return type

[**DataFlowResource**](DataFlowResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataFlowsDelete

> dataFlowsDelete(subscriptionId, resourceGroupName, factoryName, dataFlowName, apiVersion)



Deletes a data flow.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DataFlowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let dataFlowName = "dataFlowName_example"; // String | The data flow name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.dataFlowsDelete(subscriptionId, resourceGroupName, factoryName, dataFlowName, apiVersion, (error, data, response) => {
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
 **dataFlowName** | **String**| The data flow name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataFlowsGet

> DataFlowResource dataFlowsGet(subscriptionId, resourceGroupName, factoryName, dataFlowName, apiVersion, opts)



Gets a data flow.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DataFlowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let dataFlowName = "dataFlowName_example"; // String | The data flow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag of the data flow entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
};
apiInstance.dataFlowsGet(subscriptionId, resourceGroupName, factoryName, dataFlowName, apiVersion, opts, (error, data, response) => {
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
 **dataFlowName** | **String**| The data flow name. | 
 **apiVersion** | **String**| The API version. | 
 **ifNoneMatch** | **String**| ETag of the data flow entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. | [optional] 

### Return type

[**DataFlowResource**](DataFlowResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataFlowsListByFactory

> DataFlowListResponse dataFlowsListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists data flows.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DataFlowsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.dataFlowsListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, (error, data, response) => {
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

[**DataFlowListResponse**](DataFlowListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

