# BatchManagement.BatchAccountApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchAccountCreate**](BatchAccountApi.md#batchAccountCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName} | 
[**batchAccountDelete**](BatchAccountApi.md#batchAccountDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName} | 
[**batchAccountGet**](BatchAccountApi.md#batchAccountGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName} | 
[**batchAccountGetKeys**](BatchAccountApi.md#batchAccountGetKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/listKeys | Gets the account keys for the specified Batch account.
[**batchAccountList**](BatchAccountApi.md#batchAccountList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Batch/batchAccounts | 
[**batchAccountListByResourceGroup**](BatchAccountApi.md#batchAccountListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts | 
[**batchAccountRegenerateKey**](BatchAccountApi.md#batchAccountRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/regenerateKeys | 
[**batchAccountSynchronizeAutoStorageKeys**](BatchAccountApi.md#batchAccountSynchronizeAutoStorageKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/syncAutoStorageKeys | 
[**batchAccountUpdate**](BatchAccountApi.md#batchAccountUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName} | 



## batchAccountCreate

> BatchAccount batchAccountCreate(resourceGroupName, accountName, apiVersion, subscriptionId, parameters)



Creates a new Batch account with the specified parameters. Existing accounts cannot be updated with this API and should instead be updated with the Update Batch Account API.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.BatchAccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let parameters = new BatchManagement.BatchAccountCreateParameters(); // BatchAccountCreateParameters | Additional parameters for account creation.
apiInstance.batchAccountCreate(resourceGroupName, accountName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**BatchAccountCreateParameters**](BatchAccountCreateParameters.md)| Additional parameters for account creation. | 

### Return type

[**BatchAccount**](BatchAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchAccountDelete

> batchAccountDelete(resourceGroupName, accountName, apiVersion, subscriptionId)



Deletes the specified Batch account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.BatchAccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.batchAccountDelete(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## batchAccountGet

> BatchAccount batchAccountGet(resourceGroupName, accountName, apiVersion, subscriptionId)



Gets information about the specified Batch account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.BatchAccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.batchAccountGet(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**BatchAccount**](BatchAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## batchAccountGetKeys

> BatchAccountKeys batchAccountGetKeys(resourceGroupName, accountName, apiVersion, subscriptionId)

Gets the account keys for the specified Batch account.

This operation applies only to Batch accounts created with a poolAllocationMode of &#39;BatchService&#39;. If the Batch account was created with a poolAllocationMode of &#39;UserSubscription&#39;, clients cannot use access to keys to authenticate, and must use Azure Active Directory instead. In this case, getting the keys will fail.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.BatchAccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.batchAccountGetKeys(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**BatchAccountKeys**](BatchAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## batchAccountList

> BatchAccountListResult batchAccountList(apiVersion, subscriptionId)



Gets information about the Batch accounts associated with the subscription.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.BatchAccountApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.batchAccountList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**BatchAccountListResult**](BatchAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## batchAccountListByResourceGroup

> BatchAccountListResult batchAccountListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets information about the Batch accounts associated with the specified resource group.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.BatchAccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.batchAccountListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**BatchAccountListResult**](BatchAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## batchAccountRegenerateKey

> BatchAccountKeys batchAccountRegenerateKey(resourceGroupName, accountName, apiVersion, subscriptionId, parameters)



Regenerates the specified account key for the Batch account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.BatchAccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let parameters = new BatchManagement.BatchAccountRegenerateKeyParameters(); // BatchAccountRegenerateKeyParameters | The type of key to regenerate.
apiInstance.batchAccountRegenerateKey(resourceGroupName, accountName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**BatchAccountRegenerateKeyParameters**](BatchAccountRegenerateKeyParameters.md)| The type of key to regenerate. | 

### Return type

[**BatchAccountKeys**](BatchAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchAccountSynchronizeAutoStorageKeys

> batchAccountSynchronizeAutoStorageKeys(resourceGroupName, accountName, apiVersion, subscriptionId)



Synchronizes access keys for the auto-storage account configured for the specified Batch account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.BatchAccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.batchAccountSynchronizeAutoStorageKeys(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## batchAccountUpdate

> BatchAccount batchAccountUpdate(resourceGroupName, accountName, apiVersion, subscriptionId, parameters)



Updates the properties of an existing Batch account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.BatchAccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let parameters = new BatchManagement.BatchAccountUpdateParameters(); // BatchAccountUpdateParameters | Additional parameters for account update.
apiInstance.batchAccountUpdate(resourceGroupName, accountName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**BatchAccountUpdateParameters**](BatchAccountUpdateParameters.md)| Additional parameters for account update. | 

### Return type

[**BatchAccount**](BatchAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

