# KeyVaultClient.SecretsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupSecret**](SecretsApi.md#backupSecret) | **POST** /secrets/{secret-name}/backup | Backs up the specified secret.
[**deleteSecret**](SecretsApi.md#deleteSecret) | **DELETE** /secrets/{secret-name} | Deletes a secret from a specified key vault.
[**getSecret**](SecretsApi.md#getSecret) | **GET** /secrets/{secret-name}/{secret-version} | Get a specified secret from a given key vault.
[**getSecretVersions**](SecretsApi.md#getSecretVersions) | **GET** /secrets/{secret-name}/versions | List all versions of the specified secret.
[**getSecrets**](SecretsApi.md#getSecrets) | **GET** /secrets | List secrets in a specified key vault.
[**restoreSecret**](SecretsApi.md#restoreSecret) | **POST** /secrets/restore | Restores a backed up secret to a vault.
[**setSecret**](SecretsApi.md#setSecret) | **PUT** /secrets/{secret-name} | Sets a secret in a specified key vault.
[**updateSecret**](SecretsApi.md#updateSecret) | **PATCH** /secrets/{secret-name}/{secret-version} | Updates the attributes associated with a specified secret in a given key vault.



## backupSecret

> BackupSecretResult backupSecret(secretName, apiVersion)

Backs up the specified secret.

Requests that a backup of the specified secret be downloaded to the client. All versions of the secret will be downloaded. This operation requires the secrets/backup permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.SecretsApi();
let secretName = "secretName_example"; // String | The name of the secret.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.backupSecret(secretName, apiVersion, (error, data, response) => {
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

[**BackupSecretResult**](BackupSecretResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSecret

> DeletedSecretBundle deleteSecret(secretName, apiVersion)

Deletes a secret from a specified key vault.

The DELETE operation applies to any secret stored in Azure Key Vault. DELETE cannot be applied to an individual version of a secret. This operation requires the secrets/delete permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.SecretsApi();
let secretName = "secretName_example"; // String | The name of the secret.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.deleteSecret(secretName, apiVersion, (error, data, response) => {
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


## getSecret

> SecretBundle getSecret(secretName, secretVersion, apiVersion)

Get a specified secret from a given key vault.

The GET operation is applicable to any secret stored in Azure Key Vault. This operation requires the secrets/get permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.SecretsApi();
let secretName = "secretName_example"; // String | The name of the secret.
let secretVersion = "secretVersion_example"; // String | The version of the secret.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getSecret(secretName, secretVersion, apiVersion, (error, data, response) => {
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
 **secretVersion** | **String**| The version of the secret. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**SecretBundle**](SecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSecretVersions

> SecretListResult getSecretVersions(secretName, apiVersion, opts)

List all versions of the specified secret.

The full secret identifier and attributes are provided in the response. No values are returned for the secrets. This operations requires the secrets/list permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.SecretsApi();
let secretName = "secretName_example"; // String | The name of the secret.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
};
apiInstance.getSecretVersions(secretName, apiVersion, opts, (error, data, response) => {
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
 **maxresults** | **Number**| Maximum number of results to return in a page. If not specified, the service will return up to 25 results. | [optional] 

### Return type

[**SecretListResult**](SecretListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSecrets

> SecretListResult getSecrets(apiVersion, opts)

List secrets in a specified key vault.

The Get Secrets operation is applicable to the entire vault. However, only the base secret identifier and its attributes are provided in the response. Individual secret versions are not listed in the response. This operation requires the secrets/list permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.SecretsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
};
apiInstance.getSecrets(apiVersion, opts, (error, data, response) => {
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
 **maxresults** | **Number**| Maximum number of results to return in a page. If not specified, the service will return up to 25 results. | [optional] 

### Return type

[**SecretListResult**](SecretListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restoreSecret

> SecretBundle restoreSecret(apiVersion, parameters)

Restores a backed up secret to a vault.

Restores a backed up secret, and all its versions, to a vault. This operation requires the secrets/restore permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.SecretsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.SecretRestoreParameters(); // SecretRestoreParameters | The parameters to restore the secret.
apiInstance.restoreSecret(apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**SecretRestoreParameters**](SecretRestoreParameters.md)| The parameters to restore the secret. | 

### Return type

[**SecretBundle**](SecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setSecret

> SecretBundle setSecret(secretName, apiVersion, parameters)

Sets a secret in a specified key vault.

 The SET operation adds a secret to the Azure Key Vault. If the named secret already exists, Azure Key Vault creates a new version of that secret. This operation requires the secrets/set permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.SecretsApi();
let secretName = "secretName_example"; // String | The name of the secret.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.SecretSetParameters(); // SecretSetParameters | The parameters for setting the secret.
apiInstance.setSecret(secretName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**SecretSetParameters**](SecretSetParameters.md)| The parameters for setting the secret. | 

### Return type

[**SecretBundle**](SecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSecret

> SecretBundle updateSecret(secretName, secretVersion, apiVersion, parameters)

Updates the attributes associated with a specified secret in a given key vault.

The UPDATE operation changes specified attributes of an existing stored secret. Attributes that are not specified in the request are left unchanged. The value of a secret itself cannot be changed. This operation requires the secrets/set permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.SecretsApi();
let secretName = "secretName_example"; // String | The name of the secret.
let secretVersion = "secretVersion_example"; // String | The version of the secret.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.SecretUpdateParameters(); // SecretUpdateParameters | The parameters for update secret operation.
apiInstance.updateSecret(secretName, secretVersion, apiVersion, parameters, (error, data, response) => {
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
 **secretVersion** | **String**| The version of the secret. | 
 **apiVersion** | **String**| Client API version. | 
 **parameters** | [**SecretUpdateParameters**](SecretUpdateParameters.md)| The parameters for update secret operation. | 

### Return type

[**SecretBundle**](SecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

