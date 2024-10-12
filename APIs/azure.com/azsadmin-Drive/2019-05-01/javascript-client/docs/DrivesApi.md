# FabricAdminClient.DrivesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drivesGet**](DrivesApi.md#drivesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit}/storageSubSystems/{storageSubSystem}/drives/{drive} | 
[**drivesList**](DrivesApi.md#drivesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/scaleUnits/{scaleUnit}/storageSubSystems/{storageSubSystem}/drives | 



## drivesGet

> Drive drivesGet(subscriptionId, resourceGroupName, location, scaleUnit, storageSubSystem, drive, apiVersion)



Return the requested a storage drive.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.DrivesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let scaleUnit = "scaleUnit_example"; // String | Name of the scale units.
let storageSubSystem = "storageSubSystem_example"; // String | Name of the storage system.
let drive = "drive_example"; // String | Name of the storage drive.
let apiVersion = "'2019-05-01'"; // String | Client API Version.
apiInstance.drivesGet(subscriptionId, resourceGroupName, location, scaleUnit, storageSubSystem, drive, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Location of the resource. | 
 **scaleUnit** | **String**| Name of the scale units. | 
 **storageSubSystem** | **String**| Name of the storage system. | 
 **drive** | **String**| Name of the storage drive. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-05-01&#39;]

### Return type

[**Drive**](Drive.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## drivesList

> DriveList drivesList(subscriptionId, resourceGroupName, location, scaleUnit, storageSubSystem, apiVersion, opts)



Returns a list of all storage drives at a location.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.DrivesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let scaleUnit = "scaleUnit_example"; // String | Name of the scale units.
let storageSubSystem = "storageSubSystem_example"; // String | Name of the storage system.
let apiVersion = "'2019-05-01'"; // String | Client API Version.
let opts = {
  'filter': "filter_example" // String | OData filter parameter.
};
apiInstance.drivesList(subscriptionId, resourceGroupName, location, scaleUnit, storageSubSystem, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Location of the resource. | 
 **scaleUnit** | **String**| Name of the scale units. | 
 **storageSubSystem** | **String**| Name of the storage system. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2019-05-01&#39;]
 **filter** | **String**| OData filter parameter. | [optional] 

### Return type

[**DriveList**](DriveList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

