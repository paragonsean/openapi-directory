# DataFactoryManagementClient.LinkedServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**linkedServicesCreateOrUpdate**](LinkedServicesApi.md#linkedServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices/{linkedServiceName} | 
[**linkedServicesDelete**](LinkedServicesApi.md#linkedServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices/{linkedServiceName} | 
[**linkedServicesGet**](LinkedServicesApi.md#linkedServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices/{linkedServiceName} | 
[**linkedServicesListByFactory**](LinkedServicesApi.md#linkedServicesListByFactory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/linkedservices | 



## linkedServicesCreateOrUpdate

> LinkedServiceResource linkedServicesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion, linkedService, opts)



Creates or updates a linked service.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.LinkedServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let linkedServiceName = "linkedServiceName_example"; // String | The linked service name.
let apiVersion = "apiVersion_example"; // String | The API version.
let linkedService = new DataFactoryManagementClient.LinkedServiceResource(); // LinkedServiceResource | Linked service resource definition.
let opts = {
  'ifMatch': "ifMatch_example" // String | ETag of the linkedService entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
};
apiInstance.linkedServicesCreateOrUpdate(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion, linkedService, opts, (error, data, response) => {
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
 **linkedServiceName** | **String**| The linked service name. | 
 **apiVersion** | **String**| The API version. | 
 **linkedService** | [**LinkedServiceResource**](LinkedServiceResource.md)| Linked service resource definition. | 
 **ifMatch** | **String**| ETag of the linkedService entity.  Should only be specified for update, for which it should match existing entity or can be * for unconditional update. | [optional] 

### Return type

[**LinkedServiceResource**](LinkedServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## linkedServicesDelete

> linkedServicesDelete(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion)



Deletes a linked service.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.LinkedServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let linkedServiceName = "linkedServiceName_example"; // String | The linked service name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.linkedServicesDelete(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion, (error, data, response) => {
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
 **linkedServiceName** | **String**| The linked service name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## linkedServicesGet

> LinkedServiceResource linkedServicesGet(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion, opts)



Gets a linked service.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.LinkedServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let linkedServiceName = "linkedServiceName_example"; // String | The linked service name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag of the linked service entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
};
apiInstance.linkedServicesGet(subscriptionId, resourceGroupName, factoryName, linkedServiceName, apiVersion, opts, (error, data, response) => {
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
 **linkedServiceName** | **String**| The linked service name. | 
 **apiVersion** | **String**| The API version. | 
 **ifNoneMatch** | **String**| ETag of the linked service entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. | [optional] 

### Return type

[**LinkedServiceResource**](LinkedServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## linkedServicesListByFactory

> LinkedServiceListResponse linkedServicesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Lists linked services.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.LinkedServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.linkedServicesListByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, (error, data, response) => {
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

[**LinkedServiceListResponse**](LinkedServiceListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

