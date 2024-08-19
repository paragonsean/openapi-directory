# VirtualMachineImageTemplate.VirtualMachineImageTemplateApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineImageTemplatesCreateOrUpdate**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} | 
[**virtualMachineImageTemplatesDelete**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} | 
[**virtualMachineImageTemplatesGet**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} | 
[**virtualMachineImageTemplatesGetRunOutput**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesGetRunOutput) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}/runOutputs/{runOutputName} | 
[**virtualMachineImageTemplatesList**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VirtualMachineImages/imageTemplates | 
[**virtualMachineImageTemplatesListByResourceGroup**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates | 
[**virtualMachineImageTemplatesListRunOutputs**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesListRunOutputs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}/runOutputs | 
[**virtualMachineImageTemplatesRun**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName}/run | 
[**virtualMachineImageTemplatesUpdate**](VirtualMachineImageTemplateApi.md#virtualMachineImageTemplatesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VirtualMachineImages/imageTemplates/{imageTemplateName} | 



## virtualMachineImageTemplatesCreateOrUpdate

> ImageTemplate virtualMachineImageTemplatesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, parameters)



Create or update a virtual machine image template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
let parameters = new VirtualMachineImageTemplate.ImageTemplate(); // ImageTemplate | Parameters supplied to the CreateImageTemplate operation
apiInstance.virtualMachineImageTemplatesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 
 **parameters** | [**ImageTemplate**](ImageTemplate.md)| Parameters supplied to the CreateImageTemplate operation | 

### Return type

[**ImageTemplate**](ImageTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualMachineImageTemplatesDelete

> virtualMachineImageTemplatesDelete(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



Delete a virtual machine image template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
apiInstance.virtualMachineImageTemplatesDelete(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplatesGet

> ImageTemplate virtualMachineImageTemplatesGet(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



Get information about a virtual machine image template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
apiInstance.virtualMachineImageTemplatesGet(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 

### Return type

[**ImageTemplate**](ImageTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplatesGetRunOutput

> RunOutput virtualMachineImageTemplatesGetRunOutput(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, runOutputName)



Get the specified run output for the specified image template resource

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
let runOutputName = "runOutputName_example"; // String | The name of the run output
apiInstance.virtualMachineImageTemplatesGetRunOutput(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, runOutputName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | 
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


## virtualMachineImageTemplatesList

> ImageTemplateListResult virtualMachineImageTemplatesList(subscriptionId, apiVersion)



Gets information about the VM image templates associated with the subscription.

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.virtualMachineImageTemplatesList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ImageTemplateListResult**](ImageTemplateListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplatesListByResourceGroup

> ImageTemplateListResult virtualMachineImageTemplatesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



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
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.virtualMachineImageTemplatesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ImageTemplateListResult**](ImageTemplateListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplatesListRunOutputs

> RunOutputCollection virtualMachineImageTemplatesListRunOutputs(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



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
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
apiInstance.virtualMachineImageTemplatesListRunOutputs(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 

### Return type

[**RunOutputCollection**](RunOutputCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplatesRun

> virtualMachineImageTemplatesRun(apiVersion, subscriptionId, resourceGroupName, imageTemplateName)



Create artifacts from a existing image template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
apiInstance.virtualMachineImageTemplatesRun(apiVersion, subscriptionId, resourceGroupName, imageTemplateName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **imageTemplateName** | **String**| The name of the image Template | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineImageTemplatesUpdate

> ImageTemplate virtualMachineImageTemplatesUpdate(subscriptionId, resourceGroupName, imageTemplateName, apiVersion, parameters)



Update the tags for this Virtual Machine Image Template

### Example

```javascript
import VirtualMachineImageTemplate from 'virtual_machine_image_template';
let defaultClient = VirtualMachineImageTemplate.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualMachineImageTemplate.VirtualMachineImageTemplateApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let imageTemplateName = "imageTemplateName_example"; // String | The name of the image Template
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new VirtualMachineImageTemplate.ImageTemplateUpdateParameters(); // ImageTemplateUpdateParameters | Additional parameters for Image Template update.
apiInstance.virtualMachineImageTemplatesUpdate(subscriptionId, resourceGroupName, imageTemplateName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription Id forms part of the URI for every service call. | 
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

