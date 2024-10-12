# DeletedKeysApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeletedKey**](DeletedKeysApi.md#getDeletedKey) | **GET** /deletedkeys/{key-name} | Gets the public part of a deleted key. |
| [**getDeletedKeys**](DeletedKeysApi.md#getDeletedKeys) | **GET** /deletedkeys | Lists the deleted keys in the specified vault. |
| [**purgeDeletedKey**](DeletedKeysApi.md#purgeDeletedKey) | **DELETE** /deletedkeys/{key-name} | Permanently deletes the specified key. |
| [**recoverDeletedKey**](DeletedKeysApi.md#recoverDeletedKey) | **POST** /deletedkeys/{key-name}/recover | Recovers the deleted key to its latest version. |


<a id="getDeletedKey"></a>
# **getDeletedKey**
> DeletedKeyBundle getDeletedKey(keyName, apiVersion)

Gets the public part of a deleted key.

The Get Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/get permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedKeysApi apiInstance = new DeletedKeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedKeyBundle result = apiInstance.getDeletedKey(keyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedKeysApi#getDeletedKey");
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

[**DeletedKeyBundle**](DeletedKeyBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A DeletedKeyBundle consisting of a WebKey plus its Attributes and deletion information. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getDeletedKeys"></a>
# **getDeletedKeys**
> DeletedKeyListResult getDeletedKeys(apiVersion, maxresults)

Lists the deleted keys in the specified vault.

Retrieves a list of the keys in the Key Vault as JSON Web Key structures that contain the public part of a deleted key. This operation includes deletion-specific information. The Get Deleted Keys operation is applicable for vaults enabled for soft-delete. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedKeysApi apiInstance = new DeletedKeysApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      DeletedKeyListResult result = apiInstance.getDeletedKeys(apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedKeysApi#getDeletedKeys");
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

[**DeletedKeyListResult**](DeletedKeyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of deleted keys in the vault along with a link to the next page of deleted keys. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="purgeDeletedKey"></a>
# **purgeDeletedKey**
> purgeDeletedKey(keyName, apiVersion)

Permanently deletes the specified key.

The Purge Deleted Key operation is applicable for soft-delete enabled vaults. While the operation can be invoked on any vault, it will return an error if invoked on a non soft-delete enabled vault. This operation requires the keys/purge permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedKeysApi apiInstance = new DeletedKeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the key
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.purgeDeletedKey(keyName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedKeysApi#purgeDeletedKey");
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
| **keyName** | **String**| The name of the key | |
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
| **204** | No content, signaling that the key was permanently purged. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="recoverDeletedKey"></a>
# **recoverDeletedKey**
> KeyBundle recoverDeletedKey(keyName, apiVersion)

Recovers the deleted key to its latest version.

The Recover Deleted Key operation is applicable for deleted keys in soft-delete enabled vaults. It recovers the deleted key back to its latest version under /keys. An attempt to recover an non-deleted key will return an error. Consider this the inverse of the delete operation on soft-delete enabled vaults. This operation requires the keys/recover permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedKeysApi apiInstance = new DeletedKeysApi(defaultClient);
    String keyName = "keyName_example"; // String | The name of the deleted key.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      KeyBundle result = apiInstance.recoverDeletedKey(keyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedKeysApi#recoverDeletedKey");
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
| **keyName** | **String**| The name of the deleted key. | |
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
| **200** | A Key bundle of the original key and its attributes |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

