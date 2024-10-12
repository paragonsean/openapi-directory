# DataShareManagementClient.SynchronizationSettingApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**synchronizationSettingsCreate**](SynchronizationSettingApi.md#synchronizationSettingsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName} | Adds a new synchronization setting to an existing share or updates it if existing.
[**synchronizationSettingsDelete**](SynchronizationSettingApi.md#synchronizationSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName} | Delete synchronizationSetting in a share.
[**synchronizationSettingsGet**](SynchronizationSettingApi.md#synchronizationSettingsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings/{synchronizationSettingName} | Get synchronizationSetting in a share.
[**synchronizationSettingsListByShare**](SynchronizationSettingApi.md#synchronizationSettingsListByShare) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/synchronizationSettings | List synchronizationSettings in a share.



## synchronizationSettingsCreate

> SynchronizationSetting synchronizationSettingsCreate(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion, synchronizationSetting)

Adds a new synchronization setting to an existing share or updates it if existing.

Create or update a synchronizationSetting 

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.SynchronizationSettingApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share to add the synchronization setting to.
let synchronizationSettingName = "synchronizationSettingName_example"; // String | The name of the synchronizationSetting.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let synchronizationSetting = new DataShareManagementClient.SynchronizationSetting(); // SynchronizationSetting | The new synchronization setting information.
apiInstance.synchronizationSettingsCreate(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion, synchronizationSetting, (error, data, response) => {
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
 **shareName** | **String**| The name of the share to add the synchronization setting to. | 
 **synchronizationSettingName** | **String**| The name of the synchronizationSetting. | 
 **apiVersion** | **String**| The api version to use. | 
 **synchronizationSetting** | [**SynchronizationSetting**](SynchronizationSetting.md)| The new synchronization setting information. | 

### Return type

[**SynchronizationSetting**](SynchronizationSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## synchronizationSettingsDelete

> OperationResponse synchronizationSettingsDelete(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion)

Delete synchronizationSetting in a share.

Delete a synchronizationSetting in a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.SynchronizationSettingApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let synchronizationSettingName = "synchronizationSettingName_example"; // String | The name of the synchronizationSetting .
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.synchronizationSettingsDelete(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion, (error, data, response) => {
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
 **synchronizationSettingName** | **String**| The name of the synchronizationSetting . | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**OperationResponse**](OperationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## synchronizationSettingsGet

> SynchronizationSetting synchronizationSettingsGet(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion)

Get synchronizationSetting in a share.

Get a synchronizationSetting in a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.SynchronizationSettingApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let synchronizationSettingName = "synchronizationSettingName_example"; // String | The name of the synchronizationSetting.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.synchronizationSettingsGet(subscriptionId, resourceGroupName, accountName, shareName, synchronizationSettingName, apiVersion, (error, data, response) => {
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
 **synchronizationSettingName** | **String**| The name of the synchronizationSetting. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**SynchronizationSetting**](SynchronizationSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## synchronizationSettingsListByShare

> SynchronizationSettingList synchronizationSettingsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts)

List synchronizationSettings in a share.

List synchronizationSettings in a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.SynchronizationSettingApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | continuation token
};
apiInstance.synchronizationSettingsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts, (error, data, response) => {
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

[**SynchronizationSettingList**](SynchronizationSettingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

