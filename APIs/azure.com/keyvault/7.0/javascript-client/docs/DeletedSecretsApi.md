# KeyVaultClient.DeletedSecretsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeletedSecret**](DeletedSecretsApi.md#getDeletedSecret) | **GET** /deletedsecrets/{secret-name} | Gets the specified deleted secret.
[**getDeletedSecrets**](DeletedSecretsApi.md#getDeletedSecrets) | **GET** /deletedsecrets | Lists deleted secrets for the specified vault.
[**purgeDeletedSecret**](DeletedSecretsApi.md#purgeDeletedSecret) | **DELETE** /deletedsecrets/{secret-name} | Permanently deletes the specified secret.
[**recoverDeletedSecret**](DeletedSecretsApi.md#recoverDeletedSecret) | **POST** /deletedsecrets/{secret-name}/recover | Recovers the deleted secret to the latest version.



## getDeletedSecret

> DeletedSecretBundle getDeletedSecret(secretName, apiVersion)

Gets the specified deleted secret.

The Get Deleted Secret operation returns the specified deleted secret along with its attributes. This operation requires the secrets/get permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedSecretsApi();
let secretName = "secretName_example"; // String | The name of the secret.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getDeletedSecret(secretName, apiVersion, (error, data, response) => {
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
 **secretName** | **String**| The name of the secret. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**DeletedSecretBundle**](DeletedSecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeletedSecrets

> DeletedSecretListResult getDeletedSecrets(apiVersion, opts)

Lists deleted secrets for the specified vault.

The Get Deleted Secrets operation returns the secrets that have been deleted for a vault enabled for soft-delete. This operation requires the secrets/list permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedSecretsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
};
apiInstance.getDeletedSecrets(apiVersion, opts, (error, data, response) => {
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

[**DeletedSecretListResult**](DeletedSecretListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## purgeDeletedSecret

> purgeDeletedSecret(secretName, apiVersion)

Permanently deletes the specified secret.

The purge deleted secret operation removes the secret permanently, without the possibility of recovery. This operation can only be enabled on a soft-delete enabled vault. This operation requires the secrets/purge permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedSecretsApi();
let secretName = "secretName_example"; // String | The name of the secret.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.purgeDeletedSecret(secretName, apiVersion, (error, data, response) => {
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
 **secretName** | **String**| The name of the secret. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoverDeletedSecret

> SecretBundle recoverDeletedSecret(secretName, apiVersion)

Recovers the deleted secret to the latest version.

Recovers the deleted secret in the specified vault. This operation can only be performed on a soft-delete enabled vault. This operation requires the secrets/recover permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedSecretsApi();
let secretName = "secretName_example"; // String | The name of the deleted secret.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.recoverDeletedSecret(secretName, apiVersion, (error, data, response) => {
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
 **secretName** | **String**| The name of the deleted secret. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**SecretBundle**](SecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

