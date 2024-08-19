# StorSimpleManagementClient.IscsiDisksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iscsiDisksCreateOrUpdate**](IscsiDisksApi.md#iscsiDisksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName}/disks/{diskName} | 
[**iscsiDisksDelete**](IscsiDisksApi.md#iscsiDisksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName}/disks/{diskName} | 
[**iscsiDisksGet**](IscsiDisksApi.md#iscsiDisksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName}/disks/{diskName} | 
[**iscsiDisksListByDevice**](IscsiDisksApi.md#iscsiDisksListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/disks | 
[**iscsiDisksListByIscsiServer**](IscsiDisksApi.md#iscsiDisksListByIscsiServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName}/disks | 
[**iscsiDisksListMetricDefinition**](IscsiDisksApi.md#iscsiDisksListMetricDefinition) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName}/disks/{diskName}/metricsDefinitions | 
[**iscsiDisksListMetrics**](IscsiDisksApi.md#iscsiDisksListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/iscsiservers/{iscsiServerName}/disks/{diskName}/metrics | 



## iscsiDisksCreateOrUpdate

> ISCSIDisk iscsiDisksCreateOrUpdate(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion, iscsiDisk)



Creates or updates the iSCSI disk.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.IscsiDisksApi();
let deviceName = "deviceName_example"; // String | The device name.
let iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
let diskName = "diskName_example"; // String | The disk name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let iscsiDisk = new StorSimpleManagementClient.ISCSIDisk(); // ISCSIDisk | The iSCSI disk.
apiInstance.iscsiDisksCreateOrUpdate(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion, iscsiDisk, (error, data, response) => {
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
 **iscsiServerName** | **String**| The iSCSI server name. | 
 **diskName** | **String**| The disk name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **iscsiDisk** | [**ISCSIDisk**](ISCSIDisk.md)| The iSCSI disk. | 

### Return type

[**ISCSIDisk**](ISCSIDisk.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iscsiDisksDelete

> iscsiDisksDelete(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the iSCSI disk.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.IscsiDisksApi();
let deviceName = "deviceName_example"; // String | The device name.
let iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
let diskName = "diskName_example"; // String | The disk name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.iscsiDisksDelete(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **iscsiServerName** | **String**| The iSCSI server name. | 
 **diskName** | **String**| The disk name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iscsiDisksGet

> ISCSIDisk iscsiDisksGet(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified iSCSI disk name.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.IscsiDisksApi();
let deviceName = "deviceName_example"; // String | The device name.
let iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
let diskName = "diskName_example"; // String | The disk name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.iscsiDisksGet(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **iscsiServerName** | **String**| The iSCSI server name. | 
 **diskName** | **String**| The disk name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**ISCSIDisk**](ISCSIDisk.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iscsiDisksListByDevice

> ISCSIDiskList iscsiDisksListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the iSCSI disks in a device.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.IscsiDisksApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.iscsiDisksListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**ISCSIDiskList**](ISCSIDiskList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iscsiDisksListByIscsiServer

> ISCSIDiskList iscsiDisksListByIscsiServer(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the disks in a iSCSI server.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.IscsiDisksApi();
let deviceName = "deviceName_example"; // String | The device name.
let iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.iscsiDisksListByIscsiServer(deviceName, iscsiServerName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **iscsiServerName** | **String**| The iSCSI server name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**ISCSIDiskList**](ISCSIDiskList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iscsiDisksListMetricDefinition

> MetricDefinitionList iscsiDisksListMetricDefinition(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves metric definitions for all metric aggregated at the iSCSI disk.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.IscsiDisksApi();
let deviceName = "deviceName_example"; // String | The device name.
let iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
let diskName = "diskName_example"; // String | The iSCSI disk name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.iscsiDisksListMetricDefinition(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **iscsiServerName** | **String**| The iSCSI server name. | 
 **diskName** | **String**| The iSCSI disk name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**MetricDefinitionList**](MetricDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iscsiDisksListMetrics

> MetricList iscsiDisksListMetrics(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion, opts)



Gets the iSCSI disk metrics

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.IscsiDisksApi();
let deviceName = "deviceName_example"; // String | The device name.
let iscsiServerName = "iscsiServerName_example"; // String | The iSCSI server name.
let diskName = "diskName_example"; // String | The iSCSI disk name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let opts = {
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.iscsiDisksListMetrics(deviceName, iscsiServerName, diskName, subscriptionId, resourceGroupName, managerName, apiVersion, opts, (error, data, response) => {
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
 **iscsiServerName** | **String**| The iSCSI server name. | 
 **diskName** | **String**| The iSCSI disk name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **filter** | **String**| OData Filter options | [optional] 

### Return type

[**MetricList**](MetricList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

