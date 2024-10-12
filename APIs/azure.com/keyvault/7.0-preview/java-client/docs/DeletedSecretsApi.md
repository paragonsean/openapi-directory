# DeletedSecretsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeletedSecret**](DeletedSecretsApi.md#getDeletedSecret) | **GET** /deletedsecrets/{secret-name} | Gets the specified deleted secret. |
| [**getDeletedSecrets**](DeletedSecretsApi.md#getDeletedSecrets) | **GET** /deletedsecrets | Lists deleted secrets for the specified vault. |
| [**purgeDeletedSecret**](DeletedSecretsApi.md#purgeDeletedSecret) | **DELETE** /deletedsecrets/{secret-name} | Permanently deletes the specified secret. |
| [**recoverDeletedSecret**](DeletedSecretsApi.md#recoverDeletedSecret) | **POST** /deletedsecrets/{secret-name}/recover | Recovers the deleted secret to the latest version. |


<a id="getDeletedSecret"></a>
# **getDeletedSecret**
> DeletedSecretBundle getDeletedSecret(secretName, apiVersion)

Gets the specified deleted secret.

The Get Deleted Secret operation returns the specified deleted secret along with its attributes. This operation requires the secrets/get permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedSecretsApi apiInstance = new DeletedSecretsApi(defaultClient);
    String secretName = "secretName_example"; // String | The name of the secret.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedSecretBundle result = apiInstance.getDeletedSecret(secretName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedSecretsApi#getDeletedSecret");
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
| **200** | A secret bundle of the secret and its attributes. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getDeletedSecrets"></a>
# **getDeletedSecrets**
> DeletedSecretListResult getDeletedSecrets(apiVersion, maxresults)

Lists deleted secrets for the specified vault.

The Get Deleted Secrets operation returns the secrets that have been deleted for a vault enabled for soft-delete. This operation requires the secrets/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedSecretsApi apiInstance = new DeletedSecretsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      DeletedSecretListResult result = apiInstance.getDeletedSecrets(apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedSecretsApi#getDeletedSecrets");
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

[**DeletedSecretListResult**](DeletedSecretListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of deleted secrets in the vault, along with a link to the next page of deleted secrets. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="purgeDeletedSecret"></a>
# **purgeDeletedSecret**
> purgeDeletedSecret(secretName, apiVersion)

Permanently deletes the specified secret.

The purge deleted secret operation removes the secret permanently, without the possibility of recovery. This operation can only be enabled on a soft-delete enabled vault. This operation requires the secrets/purge permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedSecretsApi apiInstance = new DeletedSecretsApi(defaultClient);
    String secretName = "secretName_example"; // String | The name of the secret.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.purgeDeletedSecret(secretName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedSecretsApi#purgeDeletedSecret");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content signaling that the secret was purged forever. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="recoverDeletedSecret"></a>
# **recoverDeletedSecret**
> SecretBundle recoverDeletedSecret(secretName, apiVersion)

Recovers the deleted secret to the latest version.

Recovers the deleted secret in the specified vault. This operation can only be performed on a soft-delete enabled vault. This operation requires the secrets/recover permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedSecretsApi apiInstance = new DeletedSecretsApi(defaultClient);
    String secretName = "secretName_example"; // String | The name of the deleted secret.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      SecretBundle result = apiInstance.recoverDeletedSecret(secretName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedSecretsApi#recoverDeletedSecret");
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
| **secretName** | **String**| The name of the deleted secret. | |
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
| **200** | A Secret bundle of the original secret and its attributes. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

