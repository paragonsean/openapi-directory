# StorSimpleManagementClient.AccessControlRecordsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accessControlRecordsCreateOrUpdate**](AccessControlRecordsApi.md#accessControlRecordsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/accessControlRecords/{accessControlRecordName} | 
[**accessControlRecordsDelete**](AccessControlRecordsApi.md#accessControlRecordsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/accessControlRecords/{accessControlRecordName} | 
[**accessControlRecordsGet**](AccessControlRecordsApi.md#accessControlRecordsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/accessControlRecords/{accessControlRecordName} | 
[**accessControlRecordsListByManager**](AccessControlRecordsApi.md#accessControlRecordsListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/accessControlRecords | 



## accessControlRecordsCreateOrUpdate

> AccessControlRecord accessControlRecordsCreateOrUpdate(accessControlRecordName, subscriptionId, resourceGroupName, managerName, apiVersion, accessControlRecord)



Creates or Updates an access control record.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.AccessControlRecordsApi();
let accessControlRecordName = "accessControlRecordName_example"; // String | The name of the access control record.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let accessControlRecord = new StorSimpleManagementClient.AccessControlRecord(); // AccessControlRecord | The access control record to be added or updated.
apiInstance.accessControlRecordsCreateOrUpdate(accessControlRecordName, subscriptionId, resourceGroupName, managerName, apiVersion, accessControlRecord, (error, data, response) => {
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
 **accessControlRecordName** | **String**| The name of the access control record. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **accessControlRecord** | [**AccessControlRecord**](AccessControlRecord.md)| The access control record to be added or updated. | 

### Return type

[**AccessControlRecord**](AccessControlRecord.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accessControlRecordsDelete

> accessControlRecordsDelete(accessControlRecordName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the access control record.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.AccessControlRecordsApi();
let accessControlRecordName = "accessControlRecordName_example"; // String | The name of the access control record to delete.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.accessControlRecordsDelete(accessControlRecordName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **accessControlRecordName** | **String**| The name of the access control record to delete. | 
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


## accessControlRecordsGet

> AccessControlRecord accessControlRecordsGet(accessControlRecordName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified access control record name.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.AccessControlRecordsApi();
let accessControlRecordName = "accessControlRecordName_example"; // String | Name of access control record to be fetched.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.accessControlRecordsGet(accessControlRecordName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **accessControlRecordName** | **String**| Name of access control record to be fetched. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**AccessControlRecord**](AccessControlRecord.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accessControlRecordsListByManager

> AccessControlRecordList accessControlRecordsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the access control records in a manager.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.AccessControlRecordsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.accessControlRecordsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**AccessControlRecordList**](AccessControlRecordList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

