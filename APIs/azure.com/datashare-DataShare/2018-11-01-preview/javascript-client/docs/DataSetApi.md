# DataShareManagementClient.DataSetApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataSetsCreate**](DataSetApi.md#dataSetsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/dataSets/{dataSetName} | Adds a new data set to an existing share or updates it if existing.
[**dataSetsDelete**](DataSetApi.md#dataSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/dataSets/{dataSetName} | Delete DataSet in a share.
[**dataSetsGet**](DataSetApi.md#dataSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/dataSets/{dataSetName} | Get DataSet in a share.
[**dataSetsListByShare**](DataSetApi.md#dataSetsListByShare) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/dataSets | List DataSets in a share.



## dataSetsCreate

> DataSet dataSetsCreate(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion, dataSet)

Adds a new data set to an existing share or updates it if existing.

Create a DataSet 

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.DataSetApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share to add the data set to.
let dataSetName = "dataSetName_example"; // String | The name of the dataSet.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let dataSet = new DataShareManagementClient.DataSet(); // DataSet | The new data set information.
apiInstance.dataSetsCreate(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion, dataSet, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareName** | **String**| The name of the share to add the data set to. | 
 **dataSetName** | **String**| The name of the dataSet. | 
 **apiVersion** | **String**| The api version to use. | 
 **dataSet** | [**DataSet**](DataSet.md)| The new data set information. | 

### Return type

[**DataSet**](DataSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataSetsDelete

> dataSetsDelete(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion)

Delete DataSet in a share.

Delete a DataSet in a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.DataSetApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let dataSetName = "dataSetName_example"; // String | The name of the dataSet.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.dataSetsDelete(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareName** | **String**| The name of the share. | 
 **dataSetName** | **String**| The name of the dataSet. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataSetsGet

> DataSet dataSetsGet(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion)

Get DataSet in a share.

Get a DataSet in a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.DataSetApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let dataSetName = "dataSetName_example"; // String | The name of the dataSet.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.dataSetsGet(subscriptionId, resourceGroupName, accountName, shareName, dataSetName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareName** | **String**| The name of the share. | 
 **dataSetName** | **String**| The name of the dataSet. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**DataSet**](DataSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataSetsListByShare

> DataSetList dataSetsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts)

List DataSets in a share.

List DataSets in a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.DataSetApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | continuation token
};
apiInstance.dataSetsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareName** | **String**| The name of the share. | 
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| continuation token | [optional] 

### Return type

[**DataSetList**](DataSetList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

