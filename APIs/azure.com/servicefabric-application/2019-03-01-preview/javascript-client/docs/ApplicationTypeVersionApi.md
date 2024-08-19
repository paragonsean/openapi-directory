# ServiceFabricManagementClient.ApplicationTypeVersionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationTypeVersionsCreate**](ApplicationTypeVersionApi.md#applicationTypeVersionsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName}/versions/{version} | Creates or updates a Service Fabric application type version resource.
[**applicationTypeVersionsDelete**](ApplicationTypeVersionApi.md#applicationTypeVersionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName}/versions/{version} | Deletes a Service Fabric application type version resource.
[**applicationTypeVersionsGet**](ApplicationTypeVersionApi.md#applicationTypeVersionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName}/versions/{version} | Gets a Service Fabric application type version resource.
[**applicationTypeVersionsList**](ApplicationTypeVersionApi.md#applicationTypeVersionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName}/versions | Gets the list of application type version resources created in the specified Service Fabric application type name resource.



## applicationTypeVersionsCreate

> ApplicationTypeVersionResource applicationTypeVersionsCreate(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion, parameters)

Creates or updates a Service Fabric application type version resource.

Create or update a Service Fabric application type version resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationTypeVersionApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
let version = "version_example"; // String | The application type version.
let apiVersion = "'2019-03-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
let parameters = new ServiceFabricManagementClient.ApplicationTypeVersionResource(); // ApplicationTypeVersionResource | The application type version resource.
apiInstance.applicationTypeVersionsCreate(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **applicationTypeName** | **String**| The name of the application type name resource. | 
 **version** | **String**| The application type version. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to &#39;2019-03-01-preview&#39;]
 **parameters** | [**ApplicationTypeVersionResource**](ApplicationTypeVersionResource.md)| The application type version resource. | 

### Return type

[**ApplicationTypeVersionResource**](ApplicationTypeVersionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationTypeVersionsDelete

> applicationTypeVersionsDelete(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion)

Deletes a Service Fabric application type version resource.

Delete a Service Fabric application type version resource with the specified name.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationTypeVersionApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
let version = "version_example"; // String | The application type version.
let apiVersion = "'2019-03-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
apiInstance.applicationTypeVersionsDelete(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **applicationTypeName** | **String**| The name of the application type name resource. | 
 **version** | **String**| The application type version. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to &#39;2019-03-01-preview&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationTypeVersionsGet

> ApplicationTypeVersionResource applicationTypeVersionsGet(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion)

Gets a Service Fabric application type version resource.

Get a Service Fabric application type version resource created or in the process of being created in the Service Fabric application type name resource.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationTypeVersionApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
let version = "version_example"; // String | The application type version.
let apiVersion = "'2019-03-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
apiInstance.applicationTypeVersionsGet(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **applicationTypeName** | **String**| The name of the application type name resource. | 
 **version** | **String**| The application type version. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to &#39;2019-03-01-preview&#39;]

### Return type

[**ApplicationTypeVersionResource**](ApplicationTypeVersionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationTypeVersionsList

> ApplicationTypeVersionResourceList applicationTypeVersionsList(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion)

Gets the list of application type version resources created in the specified Service Fabric application type name resource.

Gets all application type version resources created or in the process of being created in the Service Fabric application type name resource.

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ApplicationTypeVersionApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster resource.
let applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
let apiVersion = "'2019-03-01-preview'"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
apiInstance.applicationTypeVersionsList(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster resource. | 
 **applicationTypeName** | **String**| The name of the application type name resource. | 
 **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to &#39;2019-03-01-preview&#39;]

### Return type

[**ApplicationTypeVersionResourceList**](ApplicationTypeVersionResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

