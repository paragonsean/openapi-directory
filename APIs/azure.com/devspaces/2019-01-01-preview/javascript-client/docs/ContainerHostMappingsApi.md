# DevSpacesManagement.ContainerHostMappingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**containerHostMappingsGetContainerHostMapping**](ContainerHostMappingsApi.md#containerHostMappingsGetContainerHostMapping) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/locations/{location}/checkContainerHostMapping | Returns container host mapping object for a container host resource ID if an associated controller exists.



## containerHostMappingsGetContainerHostMapping

> Object containerHostMappingsGetContainerHostMapping(apiVersion, subscriptionId, resourceGroupName, location, containerHostMapping)

Returns container host mapping object for a container host resource ID if an associated controller exists.

### Example

```javascript
import DevSpacesManagement from 'dev_spaces_management';

let apiInstance = new DevSpacesManagement.ContainerHostMappingsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
let location = "location_example"; // String | Location of the container host.
let containerHostMapping = new DevSpacesManagement.ContainerHostMapping(); // ContainerHostMapping | 
apiInstance.containerHostMappingsGetContainerHostMapping(apiVersion, subscriptionId, resourceGroupName, location, containerHostMapping, (error, data, response) => {
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
 **location** | **String**| Location of the container host. | 
 **containerHostMapping** | [**ContainerHostMapping**](ContainerHostMapping.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

