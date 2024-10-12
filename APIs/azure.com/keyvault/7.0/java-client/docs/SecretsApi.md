# SecretsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupSecret**](SecretsApi.md#backupSecret) | **POST** /secrets/{secret-name}/backup | Backs up the specified secret. |
| [**deleteSecret**](SecretsApi.md#deleteSecret) | **DELETE** /secrets/{secret-name} | Deletes a secret from a specified key vault. |
| [**getSecret**](SecretsApi.md#getSecret) | **GET** /secrets/{secret-name}/{secret-version} | Get a specified secret from a given key vault. |
| [**getSecretVersions**](SecretsApi.md#getSecretVersions) | **GET** /secrets/{secret-name}/versions | List all versions of the specified secret. |
| [**getSecrets**](SecretsApi.md#getSecrets) | **GET** /secrets | List secrets in a specified key vault. |
| [**restoreSecret**](SecretsApi.md#restoreSecret) | **POST** /secrets/restore | Restores a backed up secret to a vault. |
| [**setSecret**](SecretsApi.md#setSecret) | **PUT** /secrets/{secret-name} | Sets a secret in a specified key vault. |
| [**updateSecret**](SecretsApi.md#updateSecret) | **PATCH** /secrets/{secret-name}/{secret-version} | Updates the attributes associated with a specified secret in a given key vault. |


<a id="backupSecret"></a>
# **backupSecret**
> BackupSecretResult backupSecret(secretName, apiVersion)

Backs up the specified secret.

Requests that a backup of the specified secret be downloaded to the client. All versions of the secret will be downloaded. This operation requires the secrets/backup permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String secretName = "secretName_example"; // String | The name of the secret.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      BackupSecretResult result = apiInstance.backupSecret(secretName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#backupSecret");
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
| **secretName** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**BackupSecretResult**](BackupSecretResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The backup blob containing the backed up secret. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="deleteSecret"></a>
# **deleteSecret**
> DeletedSecretBundle deleteSecret(secretName, apiVersion)

Deletes a secret from a specified key vault.

The DELETE operation applies to any secret stored in Azure Key Vault. DELETE cannot be applied to an individual version of a secret. This operation requires the secrets/delete permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String secretName = "secretName_example"; // String | The name of the secret.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedSecretBundle result = apiInstance.deleteSecret(secretName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#deleteSecret");
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
| **secretName** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**DeletedSecretBundle**](DeletedSecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted secret and information on when the secret will be deleted, and how to recover the deleted secret. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getSecret"></a>
# **getSecret**
> SecretBundle getSecret(secretName, secretVersion, apiVersion)

Get a specified secret from a given key vault.

The GET operation is applicable to any secret stored in Azure Key Vault. This operation requires the secrets/get permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String secretName = "secretName_example"; // String | The name of the secret.
    String secretVersion = "secretVersion_example"; // String | The version of the secret.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      SecretBundle result = apiInstance.getSecret(secretName, secretVersion, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#getSecret");
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
| **secretName** | **String**| The name of the secret. | |
| **secretVersion** | **String**| The version of the secret. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**SecretBundle**](SecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The retrieved secret. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getSecretVersions"></a>
# **getSecretVersions**
> SecretListResult getSecretVersions(secretName, apiVersion, maxresults)

List all versions of the specified secret.

The full secret identifier and attributes are provided in the response. No values are returned for the secrets. This operations requires the secrets/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String secretName = "secretName_example"; // String | The name of the secret.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
    try {
      SecretListResult result = apiInstance.getSecretVersions(secretName, apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#getSecretVersions");
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
| **secretName** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client API version. | |
| **maxresults** | **Integer**| Maximum number of results to return in a page. If not specified, the service will return up to 25 results. | [optional] |

### Return type

[**SecretListResult**](SecretListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of secrets along with a link to the next page of secrets. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getSecrets"></a>
# **getSecrets**
> SecretListResult getSecrets(apiVersion, maxresults)

List secrets in a specified key vault.

The Get Secrets operation is applicable to the entire vault. However, only the base secret identifier and its attributes are provided in the response. Individual secret versions are not listed in the response. This operation requires the secrets/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
    try {
      SecretListResult result = apiInstance.getSecrets(apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#getSecrets");
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
| **maxresults** | **Integer**| Maximum number of results to return in a page. If not specified, the service will return up to 25 results. | [optional] |

### Return type

[**SecretListResult**](SecretListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of secrets in the vault along with a link to the next page of secrets. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="restoreSecret"></a>
# **restoreSecret**
> SecretBundle restoreSecret(apiVersion, parameters)

Restores a backed up secret to a vault.

Restores a backed up secret, and all its versions, to a vault. This operation requires the secrets/restore permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    SecretRestoreParameters parameters = new SecretRestoreParameters(); // SecretRestoreParameters | The parameters to restore the secret.
    try {
      SecretBundle result = apiInstance.restoreSecret(apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#restoreSecret");
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
| **parameters** | [**SecretRestoreParameters**](SecretRestoreParameters.md)| The parameters to restore the secret. | |

### Return type

[**SecretBundle**](SecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Restored secret bundle in the vault. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="setSecret"></a>
# **setSecret**
> SecretBundle setSecret(secretName, apiVersion, parameters)

Sets a secret in a specified key vault.

 The SET operation adds a secret to the Azure Key Vault. If the named secret already exists, Azure Key Vault creates a new version of that secret. This operation requires the secrets/set permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String secretName = "secretName_example"; // String | The name of the secret.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    SecretSetParameters parameters = new SecretSetParameters(); // SecretSetParameters | The parameters for setting the secret.
    try {
      SecretBundle result = apiInstance.setSecret(secretName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#setSecret");
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
| **secretName** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**SecretSetParameters**](SecretSetParameters.md)| The parameters for setting the secret. | |

### Return type

[**SecretBundle**](SecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A secret bundle containing the result of the set secret request. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="updateSecret"></a>
# **updateSecret**
> SecretBundle updateSecret(secretName, secretVersion, apiVersion, parameters)

Updates the attributes associated with a specified secret in a given key vault.

The UPDATE operation changes specified attributes of an existing stored secret. Attributes that are not specified in the request are left unchanged. The value of a secret itself cannot be changed. This operation requires the secrets/set permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String secretName = "secretName_example"; // String | The name of the secret.
    String secretVersion = "secretVersion_example"; // String | The version of the secret.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    SecretUpdateParameters parameters = new SecretUpdateParameters(); // SecretUpdateParameters | The parameters for update secret operation.
    try {
      SecretBundle result = apiInstance.updateSecret(secretName, secretVersion, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#updateSecret");
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
| **secretName** | **String**| The name of the secret. | |
| **secretVersion** | **String**| The version of the secret. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**SecretUpdateParameters**](SecretUpdateParameters.md)| The parameters for update secret operation. | |

### Return type

[**SecretBundle**](SecretBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated secret. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

