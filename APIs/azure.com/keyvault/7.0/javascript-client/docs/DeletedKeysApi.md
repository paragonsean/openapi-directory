# KeyVaultClient.DeletedKeysApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeletedKey**](DeletedKeysApi.md#getDeletedKey) | **GET** /deletedkeys/{key-name} | Gets the public part of a deleted key.
[**getDeletedKeys**](DeletedKeysApi.md#getDeletedKeys) | **GET** /deletedkeys | Lists the deleted keys in the specified vault.
[**purgeDeletedKey**](DeletedKeysApi.md#purgeDeletedKey) | **DELETE** /deletedkeys/{key-name} | Permanently deletes the specified key.
[**recoverDeletedKey**](DeletedKeysApi.md#recoverDeletedKey) | **POST** /deletedkeys/{key-name}/recover | Recovers the deleted key to its latest version.



## getDeletedKey

> DeletedKeyBundle getDeletedKey(keyName, apiVersion)

Gets the public part of a deleted key.

The Get Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/get permission. 

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedKeysApi();
let keyName = "keyName_example"; // String | The name of the key.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getDeletedKey(keyName, apiVersion, (error, data, response) => {
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
 **keyName** | **String**| The name of the key. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**DeletedKeyBundle**](DeletedKeyBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeletedKeys

> DeletedKeyListResult getDeletedKeys(apiVersion, opts)

Lists the deleted keys in the specified vault.

Retrieves a list of the keys in the Key Vault as JSON Web Key structures that contain the public part of a deleted key. This operation includes deletion-specific information. The Get Deleted Keys operation is applicable for vaults enabled for soft-delete. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/list permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedKeysApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
};
apiInstance.getDeletedKeys(apiVersion, opts, (error, data, response) => {
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

[**DeletedKeyListResult**](DeletedKeyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## purgeDeletedKey

> purgeDeletedKey(keyName, apiVersion)

Permanently deletes the specified key.

The Purge Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/purge permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedKeysApi();
let keyName = "keyName_example"; // String | The name of the key
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.purgeDeletedKey(keyName, apiVersion, (error, data, response) => {
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
 **keyName** | **String**| The name of the key | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoverDeletedKey

> KeyBundle recoverDeletedKey(keyName, apiVersion)

Recovers the deleted key to its latest version.

The Recover Deleted Key operation is applicable for deleted keys in soft-delete enabled vaults. It recovers the deleted key back to its latest version under /keys. An attempt to recover an non-deleted key will return an error. Consider this the inverse of the delete operation on soft-delete enabled vaults. This operation requires the keys/recover permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedKeysApi();
let keyName = "keyName_example"; // String | The name of the deleted key.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.recoverDeletedKey(keyName, apiVersion, (error, data, response) => {
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
 **keyName** | **String**| The name of the deleted key. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**KeyBundle**](KeyBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

