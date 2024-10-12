# DataFactoryManagementClient.DatasetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasetsCreateOrUpdate**](DatasetsApi.md#datasetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/datasets/{datasetName} | 
[**datasetsDelete**](DatasetsApi.md#datasetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/datasets/{datasetName} | 
[**datasetsGet**](DatasetsApi.md#datasetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/datasets/{datasetName} | 
[**datasetsListByFactory**](DatasetsApi.md#datasetsListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/datasets | 



## datasetsCreateOrUpdate

> DatasetResource datasetsCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion, dataset, opts)



Creates or updates a dataset.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DatasetsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let datasetName = "datasetName_example"; // String | The dataset name.
let apiVersion = "apiVersion_example"; // String | The API version.
let dataset = new DataFactoryManagementClient.DatasetResource(); // DatasetResource | Dataset resource definition.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the dataset entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
};
apiInstance.datasetsCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion, dataset, opts, (error, data, response) => {
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
 **datasetName** | **String**| The dataset name. | 
 **apiVersion** | **String**| The API version. | 
 **dataset** | [**DatasetResource**](DatasetResource.md)| Dataset resource definition. | 
 **ifMatch** | **String**| ETag of the dataset entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] 

### Return type

[**DatasetResource**](DatasetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## datasetsDelete

> datasetsDelete(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion)



Deletes a dataset.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DatasetsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let datasetName = "datasetName_example"; // String | The dataset name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.datasetsDelete(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion, (error, data, response) => {
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
 **datasetName** | **String**| The dataset name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## datasetsGet

> DatasetResource datasetsGet(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion)



Gets a dataset.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DatasetsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let datasetName = "datasetName_example"; // String | The dataset name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.datasetsGet(subscriptionId, resourceGroupName, factoryName, datasetName, apiVersion, (error, data, response) => {
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
 **datasetName** | **String**| The dataset name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**DatasetResource**](DatasetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## datasetsListByFactory

> DatasetListResponse datasetsListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists datasets.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DatasetsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.datasetsListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, (error, data, response) => {
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

[**DatasetListResponse**](DatasetListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

