# VisualStudioResourceProviderClient.ExtensionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extensionsCreate**](ExtensionsApi.md#extensionsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension/{extensionResourceName} | Extensions_Create
[**extensionsDelete**](ExtensionsApi.md#extensionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension/{extensionResourceName} | Extensions_Delete
[**extensionsGet**](ExtensionsApi.md#extensionsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension/{extensionResourceName} | Extensions_Get
[**extensionsListByAccount**](ExtensionsApi.md#extensionsListByAccount) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension | Extensions_ListByAccount
[**extensionsUpdate**](ExtensionsApi.md#extensionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{accountResourceName}/extension/{extensionResourceName} | Extensions_Update



## extensionsCreate

> ExtensionResource extensionsCreate(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, body)

Extensions_Create

Registers the extension with a Visual Studio Team Services account.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
let extensionResourceName = "extensionResourceName_example"; // String | The name of the extension.
let body = new VisualStudioResourceProviderClient.ExtensionResourceRequest(); // ExtensionResourceRequest | An object containing additional information related to the extension request.
apiInstance.extensionsCreate(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, body, (error, data, response) => {
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
 **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | 
 **extensionResourceName** | **String**| The name of the extension. | 
 **body** | [**ExtensionResourceRequest**](ExtensionResourceRequest.md)| An object containing additional information related to the extension request. | 

### Return type

[**ExtensionResource**](ExtensionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extensionsDelete

> extensionsDelete(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName)

Extensions_Delete

Removes an extension resource registration for a Visual Studio Team Services account.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
let extensionResourceName = "extensionResourceName_example"; // String | The name of the extension.
apiInstance.extensionsDelete(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, (error, data, response) => {
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
 **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | 
 **extensionResourceName** | **String**| The name of the extension. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extensionsGet

> ExtensionResource extensionsGet(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName)

Extensions_Get

Gets the details of an extension associated with a Visual Studio Team Services account resource.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
let extensionResourceName = "extensionResourceName_example"; // String | The name of the extension.
apiInstance.extensionsGet(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, (error, data, response) => {
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
 **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | 
 **extensionResourceName** | **String**| The name of the extension. | 

### Return type

[**ExtensionResource**](ExtensionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extensionsListByAccount

> ExtensionResourceListResult extensionsListByAccount(resourceGroupName, subscriptionId, apiVersion, accountResourceName)

Extensions_ListByAccount

Gets the details of the extension resources created within the resource group.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
apiInstance.extensionsListByAccount(resourceGroupName, subscriptionId, apiVersion, accountResourceName, (error, data, response) => {
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
 **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | 

### Return type

[**ExtensionResourceListResult**](ExtensionResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extensionsUpdate

> ExtensionResource extensionsUpdate(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, body)

Extensions_Update

Updates an existing extension registration for the Visual Studio Team Services account.

### Example

```javascript
import VisualStudioResourceProviderClient from 'visual_studio_resource_provider_client';
let defaultClient = VisualStudioResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VisualStudioResourceProviderClient.ExtensionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
let apiVersion = "apiVersion_example"; // String | API Version
let accountResourceName = "accountResourceName_example"; // String | The name of the Visual Studio Team Services account resource.
let extensionResourceName = "extensionResourceName_example"; // String | The name of the extension.
let body = new VisualStudioResourceProviderClient.ExtensionResourceRequest(); // ExtensionResourceRequest | An object containing additional information related to the extension request.
apiInstance.extensionsUpdate(resourceGroupName, subscriptionId, apiVersion, accountResourceName, extensionResourceName, body, (error, data, response) => {
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
 **accountResourceName** | **String**| The name of the Visual Studio Team Services account resource. | 
 **extensionResourceName** | **String**| The name of the extension. | 
 **body** | [**ExtensionResourceRequest**](ExtensionResourceRequest.md)| An object containing additional information related to the extension request. | 

### Return type

[**ExtensionResource**](ExtensionResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

