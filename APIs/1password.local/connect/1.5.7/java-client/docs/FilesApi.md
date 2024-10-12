# FilesApi

All URIs are relative to *http://1password.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadFileByID**](FilesApi.md#downloadFileByID) | **GET** /vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid}/content | Get the content of a File |
| [**getDetailsOfFileById**](FilesApi.md#getDetailsOfFileById) | **GET** /vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid} | Get the details of a File |
| [**getItemFiles**](FilesApi.md#getItemFiles) | **GET** /vaults/{vaultUuid}/items/{itemUuid}/files | Get all the files inside an Item |


<a id="downloadFileByID"></a>
# **downloadFileByID**
> File downloadFileByID(vaultUuid, itemUuid, fileUuid)

Get the content of a File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    UUID vaultUuid = UUID.randomUUID(); // UUID | The UUID of the Vault the item is in
    UUID itemUuid = UUID.randomUUID(); // UUID | The UUID of the Item the File is in
    String fileUuid = "fileUuid_example"; // String | UUID of the file to get content from
    try {
      File result = apiInstance.downloadFileByID(vaultUuid, itemUuid, fileUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#downloadFileByID");
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
| **vaultUuid** | **UUID**| The UUID of the Vault the item is in | |
| **itemUuid** | **UUID**| The UUID of the Item the File is in | |
| **fileUuid** | **String**| UUID of the file to get content from | |

### Return type

[**File**](File.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Content-Disposition -  <br>  * Content-Length -  <br>  |
| **401** | Invalid or missing token |  -  |
| **404** | File not found |  -  |

<a id="getDetailsOfFileById"></a>
# **getDetailsOfFileById**
> ModelFile getDetailsOfFileById(vaultUuid, itemUuid, fileUuid, inlineFiles)

Get the details of a File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    UUID vaultUuid = UUID.randomUUID(); // UUID | The UUID of the Vault to fetch Item from
    UUID itemUuid = UUID.randomUUID(); // UUID | The UUID of the Item to fetch File from
    UUID fileUuid = UUID.randomUUID(); // UUID | The UUID of the File to fetch
    Boolean inlineFiles = true; // Boolean | Tells server to return the base64-encoded file contents in the response.
    try {
      ModelFile result = apiInstance.getDetailsOfFileById(vaultUuid, itemUuid, fileUuid, inlineFiles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getDetailsOfFileById");
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
| **vaultUuid** | **UUID**| The UUID of the Vault to fetch Item from | |
| **itemUuid** | **UUID**| The UUID of the Item to fetch File from | |
| **fileUuid** | **UUID**| The UUID of the File to fetch | |
| **inlineFiles** | **Boolean**| Tells server to return the base64-encoded file contents in the response. | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Invalid or missing token |  -  |
| **403** | Unauthorized access |  -  |
| **404** | File not found |  -  |
| **413** | File content too large to display |  -  |

<a id="getItemFiles"></a>
# **getItemFiles**
> List&lt;ModelFile&gt; getItemFiles(vaultUuid, itemUuid, inlineFiles)

Get all the files inside an Item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    UUID vaultUuid = UUID.randomUUID(); // UUID | The UUID of the Vault to fetch Items from
    UUID itemUuid = UUID.randomUUID(); // UUID | The UUID of the Item to fetch files from
    Boolean inlineFiles = true; // Boolean | Tells server to return the base64-encoded file contents in the response.
    try {
      List<ModelFile> result = apiInstance.getItemFiles(vaultUuid, itemUuid, inlineFiles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getItemFiles");
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
| **vaultUuid** | **UUID**| The UUID of the Vault to fetch Items from | |
| **itemUuid** | **UUID**| The UUID of the Item to fetch files from | |
| **inlineFiles** | **Boolean**| Tells server to return the base64-encoded file contents in the response. | [optional] |

### Return type

[**List&lt;ModelFile&gt;**](ModelFile.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Invalid or missing token |  -  |
| **404** | Item not found |  -  |
| **413** | File content too large to display |  -  |

