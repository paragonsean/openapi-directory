# DataBoxEdgeManagementClient.DevicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicesCreateOrUpdate**](DevicesApi.md#devicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName} | 
[**devicesCreateOrUpdateSecuritySettings**](DevicesApi.md#devicesCreateOrUpdateSecuritySettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/securitySettings/default/update | 
[**devicesDelete**](DevicesApi.md#devicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName} | 
[**devicesDownloadUpdates**](DevicesApi.md#devicesDownloadUpdates) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/downloadUpdates | Downloads the updates on a Data Box Edge/Data Box Gateway device.
[**devicesGet**](DevicesApi.md#devicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName} | 
[**devicesGetExtendedInformation**](DevicesApi.md#devicesGetExtendedInformation) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/getExtendedInformation | 
[**devicesGetNetworkSettings**](DevicesApi.md#devicesGetNetworkSettings) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/networkSettings/default | 
[**devicesGetUpdateSummary**](DevicesApi.md#devicesGetUpdateSummary) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/updateSummary/default | Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device.
[**devicesInstallUpdates**](DevicesApi.md#devicesInstallUpdates) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/installUpdates | Installs the updates on the Data Box Edge/Data Box Gateway device.
[**devicesListByResourceGroup**](DevicesApi.md#devicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices | 
[**devicesListBySubscription**](DevicesApi.md#devicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices | 
[**devicesScanForUpdates**](DevicesApi.md#devicesScanForUpdates) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/scanForUpdates | Scans for updates on a Data Box Edge/Data Box Gateway device.
[**devicesUpdate**](DevicesApi.md#devicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName} | 
[**devicesUploadCertificate**](DevicesApi.md#devicesUploadCertificate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/uploadCertificate | 



## devicesCreateOrUpdate

> DataBoxEdgeDevice devicesCreateOrUpdate(deviceName, subscriptionId, resourceGroupName, apiVersion, dataBoxEdgeDevice)



Creates or updates a Data Box Edge/Data Box Gateway resource.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let dataBoxEdgeDevice = new DataBoxEdgeManagementClient.DataBoxEdgeDevice(); // DataBoxEdgeDevice | The resource object.
apiInstance.devicesCreateOrUpdate(deviceName, subscriptionId, resourceGroupName, apiVersion, dataBoxEdgeDevice, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 
 **dataBoxEdgeDevice** | [**DataBoxEdgeDevice**](DataBoxEdgeDevice.md)| The resource object. | 

### Return type

[**DataBoxEdgeDevice**](DataBoxEdgeDevice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## devicesCreateOrUpdateSecuritySettings

> devicesCreateOrUpdateSecuritySettings(deviceName, subscriptionId, resourceGroupName, apiVersion, securitySettings)



Updates the security settings on a Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let securitySettings = new DataBoxEdgeManagementClient.SecuritySettings(); // SecuritySettings | The security settings.
apiInstance.devicesCreateOrUpdateSecuritySettings(deviceName, subscriptionId, resourceGroupName, apiVersion, securitySettings, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 
 **securitySettings** | [**SecuritySettings**](SecuritySettings.md)| The security settings. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## devicesDelete

> devicesDelete(deviceName, subscriptionId, resourceGroupName, apiVersion)



Deletes the Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.devicesDelete(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesDownloadUpdates

> devicesDownloadUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion)

Downloads the updates on a Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.devicesDownloadUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGet

> DataBoxEdgeDevice devicesGet(deviceName, subscriptionId, resourceGroupName, apiVersion)



Gets the properties of the Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.devicesGet(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**DataBoxEdgeDevice**](DataBoxEdgeDevice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetExtendedInformation

> DataBoxEdgeDeviceExtendedInfo devicesGetExtendedInformation(deviceName, subscriptionId, resourceGroupName, apiVersion)



Gets additional information for the specified Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.devicesGetExtendedInformation(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**DataBoxEdgeDeviceExtendedInfo**](DataBoxEdgeDeviceExtendedInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetNetworkSettings

> NetworkSettings devicesGetNetworkSettings(deviceName, subscriptionId, resourceGroupName, apiVersion)



Gets the network settings of the specified Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.devicesGetNetworkSettings(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**NetworkSettings**](NetworkSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesGetUpdateSummary

> UpdateSummary devicesGetUpdateSummary(deviceName, subscriptionId, resourceGroupName, apiVersion)

Gets information about the availability of updates based on the last scan of the device. It also gets information about any ongoing download or install jobs on the device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.devicesGetUpdateSummary(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**UpdateSummary**](UpdateSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesInstallUpdates

> devicesInstallUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion)

Installs the updates on the Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.devicesInstallUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesListByResourceGroup

> DataBoxEdgeDeviceList devicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Gets all the Data Box Edge/Data Box Gateway devices in a resource group.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'expand': "expand_example" // String | Specify $expand=details to populate additional fields related to the resource or Specify $skipToken=<token> to populate the next page in the list.
};
apiInstance.devicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 
 **expand** | **String**| Specify $expand&#x3D;details to populate additional fields related to the resource or Specify $skipToken&#x3D;&lt;token&gt; to populate the next page in the list. | [optional] 

### Return type

[**DataBoxEdgeDeviceList**](DataBoxEdgeDeviceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesListBySubscription

> DataBoxEdgeDeviceList devicesListBySubscription(subscriptionId, apiVersion, opts)



Gets all the Data Box Edge/Data Box Gateway devices in a subscription.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'expand': "expand_example" // String | Specify $expand=details to populate additional fields related to the resource or Specify $skipToken=<token> to populate the next page in the list.
};
apiInstance.devicesListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **expand** | **String**| Specify $expand&#x3D;details to populate additional fields related to the resource or Specify $skipToken&#x3D;&lt;token&gt; to populate the next page in the list. | [optional] 

### Return type

[**DataBoxEdgeDeviceList**](DataBoxEdgeDeviceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesScanForUpdates

> devicesScanForUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion)

Scans for updates on a Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.devicesScanForUpdates(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## devicesUpdate

> DataBoxEdgeDevice devicesUpdate(deviceName, subscriptionId, resourceGroupName, apiVersion, parameters)



Modifies a Data Box Edge/Data Box Gateway resource.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let parameters = new DataBoxEdgeManagementClient.DataBoxEdgeDevicePatch(); // DataBoxEdgeDevicePatch | The resource parameters.
apiInstance.devicesUpdate(deviceName, subscriptionId, resourceGroupName, apiVersion, parameters, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 
 **parameters** | [**DataBoxEdgeDevicePatch**](DataBoxEdgeDevicePatch.md)| The resource parameters. | 

### Return type

[**DataBoxEdgeDevice**](DataBoxEdgeDevice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## devicesUploadCertificate

> UploadCertificateResponse devicesUploadCertificate(deviceName, subscriptionId, resourceGroupName, apiVersion, parameters)



Uploads registration certificate for the device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.DevicesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let parameters = new DataBoxEdgeManagementClient.UploadCertificateRequest(); // UploadCertificateRequest | The upload certificate request.
apiInstance.devicesUploadCertificate(deviceName, subscriptionId, resourceGroupName, apiVersion, parameters, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 
 **parameters** | [**UploadCertificateRequest**](UploadCertificateRequest.md)| The upload certificate request. | 

### Return type

[**UploadCertificateResponse**](UploadCertificateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

