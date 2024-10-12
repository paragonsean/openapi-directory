# KeyVaultClient.DeletedStorageApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeletedSasDefinition**](DeletedStorageApi.md#getDeletedSasDefinition) | **GET** /deletedstorage/{storage-account-name}/sas/{sas-definition-name} | Gets the specified deleted sas definition.
[**getDeletedSasDefinitions**](DeletedStorageApi.md#getDeletedSasDefinitions) | **GET** /deletedstorage/{storage-account-name}/sas | Lists deleted SAS definitions for the specified vault and storage account.
[**getDeletedStorageAccount**](DeletedStorageApi.md#getDeletedStorageAccount) | **GET** /deletedstorage/{storage-account-name} | Gets the specified deleted storage account.
[**getDeletedStorageAccounts**](DeletedStorageApi.md#getDeletedStorageAccounts) | **GET** /deletedstorage | Lists deleted storage accounts for the specified vault.
[**purgeDeletedStorageAccount**](DeletedStorageApi.md#purgeDeletedStorageAccount) | **DELETE** /deletedstorage/{storage-account-name} | Permanently deletes the specified storage account.
[**recoverDeletedSasDefinition**](DeletedStorageApi.md#recoverDeletedSasDefinition) | **POST** /deletedstorage/{storage-account-name}/sas/{sas-definition-name}/recover | Recovers the deleted SAS definition.
[**recoverDeletedStorageAccount**](DeletedStorageApi.md#recoverDeletedStorageAccount) | **POST** /deletedstorage/{storage-account-name}/recover | Recovers the deleted storage account.



## getDeletedSasDefinition

> DeletedSasDefinitionBundle getDeletedSasDefinition(storageAccountName, sasDefinitionName, apiVersion)

Gets the specified deleted sas definition.

The Get Deleted SAS Definition operation returns the specified deleted SAS definition along with its attributes. This operation requires the storage/getsas permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedStorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getDeletedSasDefinition(storageAccountName, sasDefinitionName, apiVersion, (error, data, response) => {
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
 **storageAccountName** | **String**| The name of the storage account. | 
 **sasDefinitionName** | **String**| The name of the SAS definition. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**DeletedSasDefinitionBundle**](DeletedSasDefinitionBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeletedSasDefinitions

> DeletedSasDefinitionListResult getDeletedSasDefinitions(storageAccountName, apiVersion, opts)

Lists deleted SAS definitions for the specified vault and storage account.

The Get Deleted Sas Definitions operation returns the SAS definitions that have been deleted for a vault enabled for soft-delete. This operation requires the storage/listsas permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedStorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
};
apiInstance.getDeletedSasDefinitions(storageAccountName, apiVersion, opts, (error, data, response) => {
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
 **storageAccountName** | **String**| The name of the storage account. | 
 **apiVersion** | **String**| Client API version. | 
 **maxresults** | **Number**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] 

### Return type

[**DeletedSasDefinitionListResult**](DeletedSasDefinitionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeletedStorageAccount

> DeletedStorageBundle getDeletedStorageAccount(storageAccountName, apiVersion)

Gets the specified deleted storage account.

The Get Deleted Storage Account operation returns the specified deleted storage account along with its attributes. This operation requires the storage/get permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedStorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getDeletedStorageAccount(storageAccountName, apiVersion, (error, data, response) => {
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
 **storageAccountName** | **String**| The name of the storage account. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**DeletedStorageBundle**](DeletedStorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeletedStorageAccounts

> DeletedStorageListResult getDeletedStorageAccounts(apiVersion, opts)

Lists deleted storage accounts for the specified vault.

The Get Deleted Storage Accounts operation returns the storage accounts that have been deleted for a vault enabled for soft-delete. This operation requires the storage/list permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedStorageApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
};
apiInstance.getDeletedStorageAccounts(apiVersion, opts, (error, data, response) => {
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
 **maxresults** | **Number**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] 

### Return type

[**DeletedStorageListResult**](DeletedStorageListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## purgeDeletedStorageAccount

> purgeDeletedStorageAccount(storageAccountName, apiVersion)

Permanently deletes the specified storage account.

The purge deleted storage account operation removes the secret permanently, without the possibility of recovery. This operation can only be performed on a soft-delete enabled vault. This operation requires the storage/purge permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedStorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.purgeDeletedStorageAccount(storageAccountName, apiVersion, (error, data, response) => {
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
 **storageAccountName** | **String**| The name of the storage account. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoverDeletedSasDefinition

> SasDefinitionBundle recoverDeletedSasDefinition(storageAccountName, sasDefinitionName, apiVersion)

Recovers the deleted SAS definition.

Recovers the deleted SAS definition for the specified storage account. This operation can only be performed on a soft-delete enabled vault. This operation requires the storage/recover permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedStorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.recoverDeletedSasDefinition(storageAccountName, sasDefinitionName, apiVersion, (error, data, response) => {
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
 **storageAccountName** | **String**| The name of the storage account. | 
 **sasDefinitionName** | **String**| The name of the SAS definition. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**SasDefinitionBundle**](SasDefinitionBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoverDeletedStorageAccount

> StorageBundle recoverDeletedStorageAccount(storageAccountName, apiVersion)

Recovers the deleted storage account.

Recovers the deleted storage account in the specified vault. This operation can only be performed on a soft-delete enabled vault. This operation requires the storage/recover permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedStorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.recoverDeletedStorageAccount(storageAccountName, apiVersion, (error, data, response) => {
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
 **storageAccountName** | **String**| The name of the storage account. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

