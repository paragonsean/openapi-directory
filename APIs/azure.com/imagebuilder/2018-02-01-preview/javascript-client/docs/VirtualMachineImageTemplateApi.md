# VirtualMachineImageTemplate.VirtualMachineImageTemplateApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineImageTemplateCreateOrUpdate**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplateCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} | 
[**virtualMachineImageTemplateDelete**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplateDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} | 
[**virtualMachineImageTemplateGet**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplateGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} | 
[**virtualMachineImageTemplateGetRunOutput**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplateGetRunOutput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}/runOutputs/{runOutputName} | 
[**virtualMachineImageTemplateList**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplateList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VirtualMachineImages/imageTemplates | 
[**virtualMachineImageTemplateListByResourceGroup**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplateListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates | 
[**virtualMachineImageTemplateListRunOutputs**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplateListRunOutputs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}/runOutputs | 
[**virtualMachineImageTemplateRun**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplateRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}/run | 
[**virtualMachineImageTemplateUpdate**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplateUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} | 



## virtualMachineImageTemplateCreateOrUpdate

> ImageTemplate virtualMachineImageTemplateCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, parameters)



Create or Update a Virtual Machine Image Template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
let parameters = new VirtualMachineImageTemplate.ImageTemplate(); // ImageTemplate | Parameters supplied to the Create Image Template
apiInstance.virtualMachineImageTemplateCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 
 **parameters** | [**ImageTemplate**](ImageTemplate.md)| Parameters supplied to the Create Image Template | 

### Return type

[**ImageTemplate**](ImageTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualMachineImageTemplateDelete

> virtualMachineImageTemplateDelete(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



Delete Virtual Machine Image Template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
apiInstance.virtualMachineImageTemplateDelete(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplateGet

> ImageTemplate virtualMachineImageTemplateGet(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



Get Information about Virtual Machine Image Template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
apiInstance.virtualMachineImageTemplateGet(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 

### Return type

[**ImageTemplate**](ImageTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplateGetRunOutput

> RunOutput virtualMachineImageTemplateGetRunOutput(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, runOutputName)



Get the specified run output for the specified Template resource

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
let runOutputName = "runOutputName_example"; // String | The name of the run output
apiInstance.virtualMachineImageTemplateGetRunOutput(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, runOutputName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 
 **runOutputName** | **String**| The name of the run output | 

### Return type

[**RunOutput**](RunOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplateList

> ImageTemplateListResult virtualMachineImageTemplateList(subscriptionId, apiVersion)



Gets information about the VM image templates associated with the subscription.

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.virtualMachineImageTemplateList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ImageTemplateListResult**](ImageTemplateListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplateListByResourceGroup

> ImageTemplateListResult virtualMachineImageTemplateListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Gets information about the VM image templates associated with the specified resource group.

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.virtualMachineImageTemplateListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ImageTemplateListResult**](ImageTemplateListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplateListRunOutputs

> RunOutputCollection virtualMachineImageTemplateListRunOutputs(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



List all run outputs for the specified Image Template resource

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
apiInstance.virtualMachineImageTemplateListRunOutputs(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 

### Return type

[**RunOutputCollection**](RunOutputCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplateRun

> virtualMachineImageTemplateRun(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



Create artifacts from a existing Image Template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
apiInstance.virtualMachineImageTemplateRun(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplateUpdate

> ImageTemplate virtualMachineImageTemplateUpdate(subscriptionId, resourceGroupName, imageTemplateName, apiVersion, parameters)



Update the tags for this Virtual Machine Image Template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new VirtualMachineImageTemplate.ImageTemplateUpdateParameters(); // ImageTemplateUpdateParameters | Additional parameters for Image Template update.
apiInstance.virtualMachineImageTemplateUpdate(subscriptionId, resourceGroupName, imageTemplateName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**ImageTemplateUpdateParameters**](ImageTemplateUpdateParameters.md)| Additional parameters for Image Template update. | 

### Return type

[**ImageTemplate**](ImageTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

