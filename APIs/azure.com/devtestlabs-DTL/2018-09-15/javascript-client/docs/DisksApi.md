# DevTestLabsClient.DisksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disksAttach**](DisksApi.md#disksAttach) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name}/attach | 
[**disksCreateOrUpdate**](DisksApi.md#disksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name} | 
[**disksDelete**](DisksApi.md#disksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name} | 
[**disksDetach**](DisksApi.md#disksDetach) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name}/detach | 
[**disksGet**](DisksApi.md#disksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name} | 
[**disksList**](DisksApi.md#disksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks | 
[**disksUpdate**](DisksApi.md#disksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/disks/{name} | 



## disksAttach

> disksAttach(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, attachDiskProperties)



Attach and create the lease of the disk to the virtual machine. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the disk.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let attachDiskProperties = new DevTestLabsClient.AttachDiskProperties(); // AttachDiskProperties | Properties of the disk to attach.
apiInstance.disksAttach(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, attachDiskProperties, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the disk. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **attachDiskProperties** | [**AttachDiskProperties**](AttachDiskProperties.md)| Properties of the disk to attach. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disksCreateOrUpdate

> Disk disksCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, disk)



Create or replace an existing disk. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the disk.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let disk = new DevTestLabsClient.Disk(); // Disk | A Disk.
apiInstance.disksCreateOrUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, disk, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the disk. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **disk** | [**Disk**](Disk.md)| A Disk. | 

### Return type

[**Disk**](Disk.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disksDelete

> disksDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion)



Delete disk. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the disk.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.disksDelete(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the disk. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disksDetach

> disksDetach(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, detachDiskProperties)



Detach and break the lease of the disk attached to the virtual machine. This operation can take a while to complete.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the disk.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let detachDiskProperties = new DevTestLabsClient.DetachDiskProperties(); // DetachDiskProperties | Properties of the disk to detach.
apiInstance.disksDetach(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, detachDiskProperties, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the disk. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **detachDiskProperties** | [**DetachDiskProperties**](DetachDiskProperties.md)| Properties of the disk to detach. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disksGet

> Disk disksGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, opts)



Get disk.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the disk.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=diskType)'
};
apiInstance.disksGet(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the disk. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;diskType)&#39; | [optional] 

### Return type

[**Disk**](Disk.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disksList

> DiskList disksList(subscriptionId, resourceGroupName, labName, userName, apiVersion, opts)



List disks in a given user profile.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=diskType)'
  'filter': "filter_example", // String | The filter to apply to the operation. Example: '$filter=contains(name,'myName')
  'top': 56, // Number | The maximum number of resources to return from the operation. Example: '$top=10'
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation. Example: '$orderby=name desc'
};
apiInstance.disksList(subscriptionId, resourceGroupName, labName, userName, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;diskType)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;) | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39; | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39; | [optional] 

### Return type

[**DiskList**](DiskList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disksUpdate

> Disk disksUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, disk)



Allows modifying tags of disks. All other properties will be ignored.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labName = "labName_example"; // String | The name of the lab.
let userName = "userName_example"; // String | The name of the user profile.
let name = "name_example"; // String | The name of the disk.
let apiVersion = "'2018-09-15'"; // String | Client API version.
let disk = new DevTestLabsClient.DiskFragment(); // DiskFragment | A Disk.
apiInstance.disksUpdate(subscriptionId, resourceGroupName, labName, userName, name, apiVersion, disk, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labName** | **String**| The name of the lab. | 
 **userName** | **String**| The name of the user profile. | 
 **name** | **String**| The name of the disk. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]
 **disk** | [**DiskFragment**](DiskFragment.md)| A Disk. | 

### Return type

[**Disk**](Disk.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

