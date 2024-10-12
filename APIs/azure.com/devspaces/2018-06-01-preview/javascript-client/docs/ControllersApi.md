# DevSpacesManagement.ControllersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controllersCreate**](ControllersApi.md#controllersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name} | Creates an Azure Dev Spaces Controller.
[**controllersDelete**](ControllersApi.md#controllersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name} | Deletes an Azure Dev Spaces Controller.
[**controllersGet**](ControllersApi.md#controllersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name} | Gets an Azure Dev Spaces Controller.
[**controllersList**](ControllersApi.md#controllersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DevSpaces/controllers | Lists the Azure Dev Spaces Controllers in a subscription.
[**controllersListByResourceGroup**](ControllersApi.md#controllersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers | Lists the Azure Dev Spaces Controllers in a resource group.
[**controllersListConnectionDetails**](ControllersApi.md#controllersListConnectionDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name}/listConnectionDetails | Lists connection details for an Azure Dev Spaces Controller.
[**controllersUpdate**](ControllersApi.md#controllersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name} | Updates an Azure Dev Spaces Controller.



## controllersCreate

> Controller controllersCreate(apiVersion, subscriptionId, resourceGroupName, name, controller)

Creates an Azure Dev Spaces Controller.

Creates an Azure Dev Spaces Controller with the specified create parameters.

### Example

```javascript
import DevSpacesManagement from 'dev_spaces_management';

let apiInstance = new DevSpacesManagement.ControllersApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
let name = "name_example"; // String | Name of the resource.
let controller = new DevSpacesManagement.Controller(); // Controller | Controller create parameters.
apiInstance.controllersCreate(apiVersion, subscriptionId, resourceGroupName, name, controller, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group to which the resource belongs. | 
 **name** | **String**| Name of the resource. | 
 **controller** | [**Controller**](Controller.md)| Controller create parameters. | 

### Return type

[**Controller**](Controller.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## controllersDelete

> controllersDelete(apiVersion, subscriptionId, resourceGroupName, name)

Deletes an Azure Dev Spaces Controller.

Deletes an existing Azure Dev Spaces Controller.

### Example

```javascript
import DevSpacesManagement from 'dev_spaces_management';

let apiInstance = new DevSpacesManagement.ControllersApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
let name = "name_example"; // String | Name of the resource.
apiInstance.controllersDelete(apiVersion, subscriptionId, resourceGroupName, name, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group to which the resource belongs. | 
 **name** | **String**| Name of the resource. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## controllersGet

> Controller controllersGet(apiVersion, subscriptionId, resourceGroupName, name)

Gets an Azure Dev Spaces Controller.

Gets the properties for an Azure Dev Spaces Controller.

### Example

```javascript
import DevSpacesManagement from 'dev_spaces_management';

let apiInstance = new DevSpacesManagement.ControllersApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
let name = "name_example"; // String | Name of the resource.
apiInstance.controllersGet(apiVersion, subscriptionId, resourceGroupName, name, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group to which the resource belongs. | 
 **name** | **String**| Name of the resource. | 

### Return type

[**Controller**](Controller.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## controllersList

> ControllerList controllersList(apiVersion, subscriptionId)

Lists the Azure Dev Spaces Controllers in a subscription.

Lists all the Azure Dev Spaces Controllers with their properties in the subscription.

### Example

```javascript
import DevSpacesManagement from 'dev_spaces_management';

let apiInstance = new DevSpacesManagement.ControllersApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
apiInstance.controllersList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Azure subscription ID. | 

### Return type

[**ControllerList**](ControllerList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## controllersListByResourceGroup

> ControllerList controllersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Lists the Azure Dev Spaces Controllers in a resource group.

Lists all the Azure Dev Spaces Controllers with their properties in the specified resource group and subscription.

### Example

```javascript
import DevSpacesManagement from 'dev_spaces_management';

let apiInstance = new DevSpacesManagement.ControllersApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
apiInstance.controllersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group to which the resource belongs. | 

### Return type

[**ControllerList**](ControllerList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## controllersListConnectionDetails

> ControllerConnectionDetailsList controllersListConnectionDetails(apiVersion, subscriptionId, resourceGroupName, name)

Lists connection details for an Azure Dev Spaces Controller.

Lists connection details for the underlying container resources of an Azure Dev Spaces Controller.

### Example

```javascript
import DevSpacesManagement from 'dev_spaces_management';

let apiInstance = new DevSpacesManagement.ControllersApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
let name = "name_example"; // String | Name of the resource.
apiInstance.controllersListConnectionDetails(apiVersion, subscriptionId, resourceGroupName, name, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group to which the resource belongs. | 
 **name** | **String**| Name of the resource. | 

### Return type

[**ControllerConnectionDetailsList**](ControllerConnectionDetailsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## controllersUpdate

> Controller controllersUpdate(apiVersion, subscriptionId, resourceGroupName, name, controllerUpdateParameters)

Updates an Azure Dev Spaces Controller.

Updates the properties of an existing Azure Dev Spaces Controller with the specified update parameters.

### Example

```javascript
import DevSpacesManagement from 'dev_spaces_management';

let apiInstance = new DevSpacesManagement.ControllersApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
let name = "name_example"; // String | Name of the resource.
let controllerUpdateParameters = new DevSpacesManagement.ControllerUpdateParameters(); // ControllerUpdateParameters | Parameters for updating the Azure Dev Spaces Controller.
apiInstance.controllersUpdate(apiVersion, subscriptionId, resourceGroupName, name, controllerUpdateParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group to which the resource belongs. | 
 **name** | **String**| Name of the resource. | 
 **controllerUpdateParameters** | [**ControllerUpdateParameters**](ControllerUpdateParameters.md)| Parameters for updating the Azure Dev Spaces Controller. | 

### Return type

[**Controller**](Controller.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

