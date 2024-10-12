# KeysApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupKey**](KeysApi.md#backupKey) | **POST** /keys/{key-name}/backup | Requests that a backup of the specified key be downloaded to the client. |
| [**createKey**](KeysApi.md#createKey) | **POST** /keys/{key-name}/create | Creates a new key, stores it, then returns key parameters and attributes to the client. |
| [**decrypt**](KeysApi.md#decrypt) | **POST** /keys/{key-name}/{key-version}/decrypt | Decrypts a single block of encrypted data. |
| [**deleteKey**](KeysApi.md#deleteKey) | **DELETE** /keys/{key-name} | Deletes a key of any type from storage in Azure Key Vault. |
| [**encrypt**](KeysApi.md#encrypt) | **POST** /keys/{key-name}/{key-version}/encrypt | Encrypts an arbitrary sequence of bytes using an encryption key that is stored in a key vault. |
| [**getKey**](KeysApi.md#getKey) | **GET** /keys/{key-name}/{key-version} | Gets the public part of a stored key. |
| [**getKeyVersions**](KeysApi.md#getKeyVersions) | **GET** /keys/{key-name}/versions | Retrieves a list of individual key versions with the same key name. |
| [**getKeys**](KeysApi.md#getKeys) | **GET** /keys | List keys in the specified vault. |
| [**importKey**](KeysApi.md#importKey) | **PUT** /keys/{key-name} | Imports an externally created key, stores it, and returns key parameters and attributes to the client. |
| [**restoreKey**](KeysApi.md#restoreKey) | **POST** /keys/restore | Restores a backed up key to a vault. |
| [**sign**](KeysApi.md#sign) | **POST** /keys/{key-name}/{key-version}/sign | Creates a signature from a digest using the specified key. |
| [**unwrapKey**](KeysApi.md#unwrapKey) | **POST** /keys/{key-name}/{key-version}/unwrapkey | Unwraps a symmetric key using the specified key that was initially used for wrapping that key. |
| [**updateKey**](KeysApi.md#updateKey) | **PATCH** /keys/{key-name}/{key-version} | The update key operation changes specified attributes of a stored key and can be applied to any key type and key version stored in Azure Key Vault. |
| [**verify**](KeysApi.md#verify) | **POST** /keys/{key-name}/{key-version}/verify | Verifies a signature using a specified key. |
| [**wrapKey**](KeysApi.md#wrapKey) | **POST** /keys/{key-name}/{key-version}/wrapkey | Wraps a symmetric key using a specified key. |


<a id="backupKey"></a>
# **backupKey**
> BackupKeyResult backupKey(keyName, apiVersion)

Requests that a backup of the specified key be downloaded to the client.

The Key Backup operation exports a key from Azure Key Vault in a protected form. Note that this operation does NOT return key material in a form that can be used outside the Azure Key Vault system, the returned key material is either protected to a Azure Key Vault HSM or to Azure Key Vault itself. The intent of this operation is to allow a client to GENERATE a key in one Azure Key Vault instance, BACKUP the key, and then RESTORE it into another Azure Key Vault instance. The BACKUP operation may be used to export, in protected form, any key type from Azure Key Vault. Individual versions of a key cannot be backed up. BACKUP / RESTORE can be performed within geographical boundaries only; meaning that a BACKUP from one geographical area cannot be restored to another geographical area. For example, a backup from the US geographical area cannot be restored in an EU geographical area. This operation requires the key/backup permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      BackupKeyResult result = apiInstance.backupKey(keyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#backupKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**BackupKeyResult**](BackupKeyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The backup blob containing the backed up key. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="createKey"></a>
# **createKey**
> KeyBundle createKey(keyName, apiVersion, parameters)

Creates a new key, stores it, then returns key parameters and attributes to the client.

The create key operation can be used to create any key type in Azure Key Vault. If the named key already exists, Azure Key Vault creates a new version of the key. It requires the keys/create permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name for the new key. The system will generate the version name for the new key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeyCreateParameters parameters = new KeyCreateParameters(); // KeyCreateParameters | The parameters to create a key.
    try {
      KeyBundle result = apiInstance.createKey(keyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#createKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name for the new key. The system will generate the version name for the new key. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeyCreateParameters**](KeyCreateParameters.md)| The parameters to create a key. | |

### Return type

[**KeyBundle**](KeyBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A key bundle containing the result of the create key request. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="decrypt"></a>
# **decrypt**
> KeyOperationResult decrypt(keyName, keyVersion, apiVersion, parameters)

Decrypts a single block of encrypted data.

The DECRYPT operation decrypts a well-formed block of ciphertext using the target encryption key and specified algorithm. This operation is the reverse of the ENCRYPT operation; only a single block of data may be decrypted, the size of this block is dependent on the target key and the algorithm to be used. The DECRYPT operation applies to asymmetric and symmetric keys stored in Azure Key Vault since it uses the private portion of the key. This operation requires the keys/decrypt permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key.
    String keyVersion = "keyVersion_example"; // String | The version of the key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeyOperationsParameters parameters = new KeyOperationsParameters(); // KeyOperationsParameters | The parameters for the decryption operation.
    try {
      KeyOperationResult result = apiInstance.decrypt(keyName, keyVersion, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#decrypt");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key. | |
| **keyVersion** | **String**| The version of the key. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeyOperationsParameters**](KeyOperationsParameters.md)| The parameters for the decryption operation. | |

### Return type

[**KeyOperationResult**](KeyOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The decryption result. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="deleteKey"></a>
# **deleteKey**
> DeletedKeyBundle deleteKey(keyName, apiVersion)

Deletes a key of any type from storage in Azure Key Vault.

The delete key operation cannot be used to remove individual versions of a key. This operation removes the cryptographic material associated with the key, which means the key is not usable for Sign/Verify, Wrap/Unwrap or Encrypt/Decrypt operations. This operation requires the keys/delete permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key to delete.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedKeyBundle result = apiInstance.deleteKey(keyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#deleteKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key to delete. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**DeletedKeyBundle**](DeletedKeyBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The public part of the deleted key and deletion information on when the key will be purged. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="encrypt"></a>
# **encrypt**
> KeyOperationResult encrypt(keyName, keyVersion, apiVersion, parameters)

Encrypts an arbitrary sequence of bytes using an encryption key that is stored in a key vault.

The ENCRYPT operation encrypts an arbitrary sequence of bytes using an encryption key that is stored in Azure Key Vault. Note that the ENCRYPT operation only supports a single block of data, the size of which is dependent on the target key and the encryption algorithm to be used. The ENCRYPT operation is only strictly necessary for symmetric keys stored in Azure Key Vault since protection with an asymmetric key can be performed using public portion of the key. This operation is supported for asymmetric keys as a convenience for callers that have a key-reference but do not have access to the public key material. This operation requires the keys/encrypt permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key.
    String keyVersion = "keyVersion_example"; // String | The version of the key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeyOperationsParameters parameters = new KeyOperationsParameters(); // KeyOperationsParameters | The parameters for the encryption operation.
    try {
      KeyOperationResult result = apiInstance.encrypt(keyName, keyVersion, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#encrypt");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key. | |
| **keyVersion** | **String**| The version of the key. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeyOperationsParameters**](KeyOperationsParameters.md)| The parameters for the encryption operation. | |

### Return type

[**KeyOperationResult**](KeyOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The encryption result. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getKey"></a>
# **getKey**
> KeyBundle getKey(keyName, keyVersion, apiVersion)

Gets the public part of a stored key.

The get key operation is applicable to all key types. If the requested key is symmetric, then no key material is released in the response. This operation requires the keys/get permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key to get.
    String keyVersion = "keyVersion_example"; // String | Adding the version parameter retrieves a specific version of a key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      KeyBundle result = apiInstance.getKey(keyName, keyVersion, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#getKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key to get. | |
| **keyVersion** | **String**| Adding the version parameter retrieves a specific version of a key. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**KeyBundle**](KeyBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A key bundle containing the key and its attributes. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getKeyVersions"></a>
# **getKeyVersions**
> KeyListResult getKeyVersions(keyName, apiVersion, maxresults)

Retrieves a list of individual key versions with the same key name.

The full key identifier, attributes, and tags are provided in the response. This operation requires the keys/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      KeyListResult result = apiInstance.getKeyVersions(keyName, apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#getKeyVersions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key. | |
| **apiVersion** | **String**| Client API version. | |
| **maxresults** | **Integer**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] |

### Return type

[**KeyListResult**](KeyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of keys along with a link to the next page of keys. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getKeys"></a>
# **getKeys**
> KeyListResult getKeys(apiVersion, maxresults)

List keys in the specified vault.

Retrieves a list of the keys in the Key Vault as JSON Web Key structures that contain the public part of a stored key. The LIST operation is applicable to all key types, however only the base key identifier, attributes, and tags are provided in the response. Individual versions of a key are not listed in the response. This operation requires the keys/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      KeyListResult result = apiInstance.getKeys(apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#getKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| Client API version. | |
| **maxresults** | **Integer**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] |

### Return type

[**KeyListResult**](KeyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of keys in the vault along with a link to the next page of keys. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="importKey"></a>
# **importKey**
> KeyBundle importKey(keyName, apiVersion, parameters)

Imports an externally created key, stores it, and returns key parameters and attributes to the client.

The import key operation may be used to import any key type into an Azure Key Vault. If the named key already exists, Azure Key Vault creates a new version of the key. This operation requires the keys/import permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | Name for the imported key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeyImportParameters parameters = new KeyImportParameters(); // KeyImportParameters | The parameters to import a key.
    try {
      KeyBundle result = apiInstance.importKey(keyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#importKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| Name for the imported key. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeyImportParameters**](KeyImportParameters.md)| The parameters to import a key. | |

### Return type

[**KeyBundle**](KeyBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Imported key bundle to the vault. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="restoreKey"></a>
# **restoreKey**
> KeyBundle restoreKey(apiVersion, parameters)

Restores a backed up key to a vault.

Imports a previously backed up key into Azure Key Vault, restoring the key, its key identifier, attributes and access control policies. The RESTORE operation may be used to import a previously backed up key. Individual versions of a key cannot be restored. The key is restored in its entirety with the same key name as it had when it was backed up. If the key name is not available in the target Key Vault, the RESTORE operation will be rejected. While the key name is retained during restore, the final key identifier will change if the key is restored to a different vault. Restore will restore all versions and preserve version identifiers. The RESTORE operation is subject to security constraints: The target Key Vault must be owned by the same Microsoft Azure Subscription as the source Key Vault The user must have RESTORE permission in the target Key Vault. This operation requires the keys/restore permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeyRestoreParameters parameters = new KeyRestoreParameters(); // KeyRestoreParameters | The parameters to restore the key.
    try {
      KeyBundle result = apiInstance.restoreKey(apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#restoreKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeyRestoreParameters**](KeyRestoreParameters.md)| The parameters to restore the key. | |

### Return type

[**KeyBundle**](KeyBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Restored key bundle in the vault. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="sign"></a>
# **sign**
> KeyOperationResult sign(keyName, keyVersion, apiVersion, parameters)

Creates a signature from a digest using the specified key.

The SIGN operation is applicable to asymmetric and symmetric keys stored in Azure Key Vault since this operation uses the private portion of the key. This operation requires the keys/sign permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key.
    String keyVersion = "keyVersion_example"; // String | The version of the key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeySignParameters parameters = new KeySignParameters(); // KeySignParameters | The parameters for the signing operation.
    try {
      KeyOperationResult result = apiInstance.sign(keyName, keyVersion, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#sign");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key. | |
| **keyVersion** | **String**| The version of the key. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeySignParameters**](KeySignParameters.md)| The parameters for the signing operation. | |

### Return type

[**KeyOperationResult**](KeyOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The signature value. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="unwrapKey"></a>
# **unwrapKey**
> KeyOperationResult unwrapKey(keyName, keyVersion, apiVersion, parameters)

Unwraps a symmetric key using the specified key that was initially used for wrapping that key.

The UNWRAP operation supports decryption of a symmetric key using the target key encryption key. This operation is the reverse of the WRAP operation. The UNWRAP operation applies to asymmetric and symmetric keys stored in Azure Key Vault since it uses the private portion of the key. This operation requires the keys/unwrapKey permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key.
    String keyVersion = "keyVersion_example"; // String | The version of the key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeyOperationsParameters parameters = new KeyOperationsParameters(); // KeyOperationsParameters | The parameters for the key operation.
    try {
      KeyOperationResult result = apiInstance.unwrapKey(keyName, keyVersion, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#unwrapKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key. | |
| **keyVersion** | **String**| The version of the key. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeyOperationsParameters**](KeyOperationsParameters.md)| The parameters for the key operation. | |

### Return type

[**KeyOperationResult**](KeyOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The unwrapped symmetric key. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="updateKey"></a>
# **updateKey**
> KeyBundle updateKey(keyName, keyVersion, apiVersion, parameters)

The update key operation changes specified attributes of a stored key and can be applied to any key type and key version stored in Azure Key Vault.

In order to perform this operation, the key must already exist in the Key Vault. Note: The cryptographic material of a key itself cannot be changed. This operation requires the keys/update permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of key to update.
    String keyVersion = "keyVersion_example"; // String | The version of the key to update.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeyUpdateParameters parameters = new KeyUpdateParameters(); // KeyUpdateParameters | The parameters of the key to update.
    try {
      KeyBundle result = apiInstance.updateKey(keyName, keyVersion, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#updateKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of key to update. | |
| **keyVersion** | **String**| The version of the key to update. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeyUpdateParameters**](KeyUpdateParameters.md)| The parameters of the key to update. | |

### Return type

[**KeyBundle**](KeyBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated key. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="verify"></a>
# **verify**
> KeyVerifyResult verify(keyName, keyVersion, apiVersion, parameters)

Verifies a signature using a specified key.

The VERIFY operation is applicable to symmetric keys stored in Azure Key Vault. VERIFY is not strictly necessary for asymmetric keys stored in Azure Key Vault since signature verification can be performed using the public portion of the key but this operation is supported as a convenience for callers that only have a key-reference and not the public portion of the key. This operation requires the keys/verify permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key.
    String keyVersion = "keyVersion_example"; // String | The version of the key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeyVerifyParameters parameters = new KeyVerifyParameters(); // KeyVerifyParameters | The parameters for verify operations.
    try {
      KeyVerifyResult result = apiInstance.verify(keyName, keyVersion, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#verify");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key. | |
| **keyVersion** | **String**| The version of the key. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeyVerifyParameters**](KeyVerifyParameters.md)| The parameters for verify operations. | |

### Return type

[**KeyVerifyResult**](KeyVerifyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The verification result. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="wrapKey"></a>
# **wrapKey**
> KeyOperationResult wrapKey(keyName, keyVersion, apiVersion, parameters)

Wraps a symmetric key using a specified key.

The WRAP operation supports encryption of a symmetric key using a key encryption key that has previously been stored in an Azure Key Vault. The WRAP operation is only strictly necessary for symmetric keys stored in Azure Key Vault since protection with an asymmetric key can be performed using the public portion of the key. This operation is supported for asymmetric keys as a convenience for callers that have a key-reference but do not have access to the public key material. This operation requires the keys/wrapKey permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key.
    String keyVersion = "keyVersion_example"; // String | The version of the key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    KeyOperationsParameters parameters = new KeyOperationsParameters(); // KeyOperationsParameters | The parameters for wrap operation.
    try {
      KeyOperationResult result = apiInstance.wrapKey(keyName, keyVersion, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#wrapKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyName** | **String**| The name of the key. | |
| **keyVersion** | **String**| The version of the key. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**KeyOperationsParameters**](KeyOperationsParameters.md)| The parameters for wrap operation. | |

### Return type

[**KeyOperationResult**](KeyOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The wrapped symmetric key. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

