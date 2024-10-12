# KeyVaultClient.StorageApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupStorageAccount**](StorageApi.md#backupStorageAccount) | **POST** /storage/{storage-account-name}/backup | Backs up the specified storage account.
[**deleteSasDefinition**](StorageApi.md#deleteSasDefinition) | **DELETE** /storage/{storage-account-name}/sas/{sas-definition-name} | 
[**deleteStorageAccount**](StorageApi.md#deleteStorageAccount) | **DELETE** /storage/{storage-account-name} | 
[**getSasDefinition**](StorageApi.md#getSasDefinition) | **GET** /storage/{storage-account-name}/sas/{sas-definition-name} | 
[**getSasDefinitions**](StorageApi.md#getSasDefinitions) | **GET** /storage/{storage-account-name}/sas | 
[**getStorageAccount**](StorageApi.md#getStorageAccount) | **GET** /storage/{storage-account-name} | 
[**getStorageAccounts**](StorageApi.md#getStorageAccounts) | **GET** /storage | 
[**regenerateStorageAccountKey**](StorageApi.md#regenerateStorageAccountKey) | **POST** /storage/{storage-account-name}/regeneratekey | 
[**restoreStorageAccount**](StorageApi.md#restoreStorageAccount) | **POST** /storage/restore | Restores a backed up storage account to a vault.
[**setSasDefinition**](StorageApi.md#setSasDefinition) | **PUT** /storage/{storage-account-name}/sas/{sas-definition-name} | 
[**setStorageAccount**](StorageApi.md#setStorageAccount) | **PUT** /storage/{storage-account-name} | 
[**updateSasDefinition**](StorageApi.md#updateSasDefinition) | **PATCH** /storage/{storage-account-name}/sas/{sas-definition-name} | 
[**updateStorageAccount**](StorageApi.md#updateStorageAccount) | **PATCH** /storage/{storage-account-name} | 



## backupStorageAccount

> BackupStorageResult backupStorageAccount(storageAccountName, apiVersion)

Backs up the specified storage account.

Requests that a backup of the specified storage account be downloaded to the client. This operation requires the storage/backup permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.backupStorageAccount(storageAccountName, apiVersion, (error, data, response) => {
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

[**BackupStorageResult**](BackupStorageResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSasDefinition

> DeletedSasDefinitionBundle deleteSasDefinition(storageAccountName, sasDefinitionName, apiVersion)



Deletes a SAS definition from a specified storage account. This operation requires the storage/deletesas permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.deleteSasDefinition(storageAccountName, sasDefinitionName, apiVersion, (error, data, response) => {
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


## deleteStorageAccount

> DeletedStorageBundle deleteStorageAccount(storageAccountName, apiVersion)



Deletes a storage account. This operation requires the storage/delete permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.deleteStorageAccount(storageAccountName, apiVersion, (error, data, response) => {
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


## getSasDefinition

> SasDefinitionBundle getSasDefinition(storageAccountName, sasDefinitionName, apiVersion)



Gets information about a SAS definition for the specified storage account. This operation requires the storage/getsas permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getSasDefinition(storageAccountName, sasDefinitionName, apiVersion, (error, data, response) => {
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


## getSasDefinitions

> SasDefinitionListResult getSasDefinitions(storageAccountName, apiVersion, opts)



List storage SAS definitions for the given storage account. This operation requires the storage/listsas permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
};
apiInstance.getSasDefinitions(storageAccountName, apiVersion, opts, (error, data, response) => {
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

[**SasDefinitionListResult**](SasDefinitionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStorageAccount

> StorageBundle getStorageAccount(storageAccountName, apiVersion)



Gets information about a specified storage account. This operation requires the storage/get permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getStorageAccount(storageAccountName, apiVersion, (error, data, response) => {
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


## getStorageAccounts

> StorageListResult getStorageAccounts(apiVersion, opts)



List storage accounts managed by the specified key vault. This operation requires the storage/list permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
};
apiInstance.getStorageAccounts(apiVersion, opts, (error, data, response) => {
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

[**StorageListResult**](StorageListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regenerateStorageAccountKey

> StorageBundle regenerateStorageAccountKey(storageAccountName, apiVersion, parameters)



Regenerates the specified key value for the given storage account. This operation requires the storage/regeneratekey permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.StorageAccountRegenerteKeyParameters(); // StorageAccountRegenerteKeyParameters | The parameters to regenerate storage account key.
apiInstance.regenerateStorageAccountKey(storageAccountName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**StorageAccountRegenerteKeyParameters**](StorageAccountRegenerteKeyParameters.md)| The parameters to regenerate storage account key. | 

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## restoreStorageAccount

> StorageBundle restoreStorageAccount(apiVersion, parameters)

Restores a backed up storage account to a vault.

Restores a backed up storage account to a vault. This operation requires the storage/restore permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.StorageRestoreParameters(); // StorageRestoreParameters | The parameters to restore the storage account.
apiInstance.restoreStorageAccount(apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**StorageRestoreParameters**](StorageRestoreParameters.md)| The parameters to restore the storage account. | 

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setSasDefinition

> SasDefinitionBundle setSasDefinition(storageAccountName, sasDefinitionName, apiVersion, parameters)



Creates or updates a new SAS definition for the specified storage account. This operation requires the storage/setsas permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.SasDefinitionCreateParameters(); // SasDefinitionCreateParameters | The parameters to create a SAS definition.
apiInstance.setSasDefinition(storageAccountName, sasDefinitionName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**SasDefinitionCreateParameters**](SasDefinitionCreateParameters.md)| The parameters to create a SAS definition. | 

### Return type

[**SasDefinitionBundle**](SasDefinitionBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setStorageAccount

> StorageBundle setStorageAccount(storageAccountName, apiVersion, parameters)



Creates or updates a new storage account. This operation requires the storage/set permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.StorageAccountCreateParameters(); // StorageAccountCreateParameters | The parameters to create a storage account.
apiInstance.setStorageAccount(storageAccountName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**StorageAccountCreateParameters**](StorageAccountCreateParameters.md)| The parameters to create a storage account. | 

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSasDefinition

> SasDefinitionBundle updateSasDefinition(storageAccountName, sasDefinitionName, apiVersion, parameters)



Updates the specified attributes associated with the given SAS definition. This operation requires the storage/setsas permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let sasDefinitionName = "sasDefinitionName_example"; // String | The name of the SAS definition.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.SasDefinitionUpdateParameters(); // SasDefinitionUpdateParameters | The parameters to update a SAS definition.
apiInstance.updateSasDefinition(storageAccountName, sasDefinitionName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**SasDefinitionUpdateParameters**](SasDefinitionUpdateParameters.md)| The parameters to update a SAS definition. | 

### Return type

[**SasDefinitionBundle**](SasDefinitionBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateStorageAccount

> StorageBundle updateStorageAccount(storageAccountName, apiVersion, parameters)



Updates the specified attributes associated with the given storage account. This operation requires the storage/set/update permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.StorageApi();
let storageAccountName = "storageAccountName_example"; // String | The name of the storage account.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.StorageAccountUpdateParameters(); // StorageAccountUpdateParameters | The parameters to update a storage account.
apiInstance.updateStorageAccount(storageAccountName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**StorageAccountUpdateParameters**](StorageAccountUpdateParameters.md)| The parameters to update a storage account. | 

### Return type

[**StorageBundle**](StorageBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

