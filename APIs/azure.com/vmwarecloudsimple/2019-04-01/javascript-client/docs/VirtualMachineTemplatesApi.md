# VMwareCloudSimple.VirtualMachineTemplatesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualMachineTemplatesGet**](VirtualMachineTemplatesApi.md#virtualMachineTemplatesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/virtualMachineTemplates/{virtualMachineTemplateName} | Implements virtual machine template GET method
[**virtualMachineTemplatesList**](VirtualMachineTemplatesApi.md#virtualMachineTemplatesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/virtualMachineTemplates | Implements list of available VM templates



## virtualMachineTemplatesGet

> VirtualMachineTemplate virtualMachineTemplatesGet(subscriptionId, regionId, pcName, virtualMachineTemplateName, apiVersion)

Implements virtual machine template GET method

Returns virtual machine templates by its name

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachineTemplatesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let pcName = "pcName_example"; // String | The private cloud name
let virtualMachineTemplateName = "virtualMachineTemplateName_example"; // String | virtual machine template id (vsphereId)
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.virtualMachineTemplatesGet(subscriptionId, regionId, pcName, virtualMachineTemplateName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **pcName** | **String**| The private cloud name | 
 **virtualMachineTemplateName** | **String**| virtual machine template id (vsphereId) | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**VirtualMachineTemplate**](VirtualMachineTemplate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualMachineTemplatesList

> VirtualMachineTemplateListResponse virtualMachineTemplatesList(subscriptionId, apiVersion, pcName, regionId, resourcePoolName)

Implements list of available VM templates

Returns list of virtual machine templates in region for private cloud

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualMachineTemplatesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "apiVersion_example"; // String | Client API version.
let pcName = "pcName_example"; // String | The private cloud name
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let resourcePoolName = "resourcePoolName_example"; // String | Resource pool used to derive vSphere cluster which contains VM templates
apiInstance.virtualMachineTemplatesList(subscriptionId, apiVersion, pcName, regionId, resourcePoolName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **apiVersion** | **String**| Client API version. | 
 **pcName** | **String**| The private cloud name | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **resourcePoolName** | **String**| Resource pool used to derive vSphere cluster which contains VM templates | 

### Return type

[**VirtualMachineTemplateListResponse**](VirtualMachineTemplateListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

