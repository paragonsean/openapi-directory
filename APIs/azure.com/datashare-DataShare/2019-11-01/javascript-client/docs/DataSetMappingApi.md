# DataShareManagementClient.DataSetMappingApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataSetMappingsCreate**](DataSetMappingApi.md#dataSetMappingsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings/{dataSetMappingName} | Maps a source data set in the source share to a sink data set in the share subscription.  Enables copying the data set from source to destination.
[**dataSetMappingsDelete**](DataSetMappingApi.md#dataSetMappingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings/{dataSetMappingName} | Delete DataSetMapping in a shareSubscription.
[**dataSetMappingsGet**](DataSetMappingApi.md#dataSetMappingsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings/{dataSetMappingName} | Get DataSetMapping in a shareSubscription.
[**dataSetMappingsListByShareSubscription**](DataSetMappingApi.md#dataSetMappingsListByShareSubscription) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/dataSetMappings | List DataSetMappings in a share subscription.



## dataSetMappingsCreate

> DataSetMapping dataSetMappingsCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion, dataSetMapping)

Maps a source data set in the source share to a sink data set in the share subscription.  Enables copying the data set from source to destination.

Create a DataSetMapping 

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.DataSetMappingApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription which will hold the data set sink.
let dataSetMappingName = "dataSetMappingName_example"; // String | The name of the data set mapping to be created.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let dataSetMapping = new DataShareManagementClient.DataSetMapping(); // DataSetMapping | Destination data set configuration details.
apiInstance.dataSetMappingsCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion, dataSetMapping, (error, data, response) => {
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
 **shareSubscriptionName** | **String**| The name of the share subscription which will hold the data set sink. | 
 **dataSetMappingName** | **String**| The name of the data set mapping to be created. | 
 **apiVersion** | **String**| The api version to use. | 
 **dataSetMapping** | [**DataSetMapping**](DataSetMapping.md)| Destination data set configuration details. | 

### Return type

[**DataSetMapping**](DataSetMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataSetMappingsDelete

> dataSetMappingsDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion)

Delete DataSetMapping in a shareSubscription.

Delete a DataSetMapping in a shareSubscription

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.DataSetMappingApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let dataSetMappingName = "dataSetMappingName_example"; // String | The name of the dataSetMapping.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.dataSetMappingsDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion, (error, data, response) => {
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
 **shareSubscriptionName** | **String**| The name of the shareSubscription. | 
 **dataSetMappingName** | **String**| The name of the dataSetMapping. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataSetMappingsGet

> DataSetMapping dataSetMappingsGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion)

Get DataSetMapping in a shareSubscription.

Get a DataSetMapping in a shareSubscription

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.DataSetMappingApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
let dataSetMappingName = "dataSetMappingName_example"; // String | The name of the dataSetMapping.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.dataSetMappingsGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, dataSetMappingName, apiVersion, (error, data, response) => {
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
 **shareSubscriptionName** | **String**| The name of the shareSubscription. | 
 **dataSetMappingName** | **String**| The name of the dataSetMapping. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**DataSetMapping**](DataSetMapping.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataSetMappingsListByShareSubscription

> DataSetMappingList dataSetMappingsListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts)

List DataSetMappings in a share subscription.

List DataSetMappings in a share subscription

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.DataSetMappingApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | Continuation token
};
apiInstance.dataSetMappingsListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, opts, (error, data, response) => {
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
 **shareSubscriptionName** | **String**| The name of the share subscription. | 
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| Continuation token | [optional] 

### Return type

[**DataSetMappingList**](DataSetMappingList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

