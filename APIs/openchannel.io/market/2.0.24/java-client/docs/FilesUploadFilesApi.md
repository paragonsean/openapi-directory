# FilesUploadFilesApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filesByIdOrUrlGet**](FilesUploadFilesApi.md#filesByIdOrUrlGet) | **GET** /files/byIdOrUrl | Get the details for a file. |
| [**filesDownloadGet**](FilesUploadFilesApi.md#filesDownloadGet) | **GET** /files/download | A signed URL for downloading a private file can be returned by providing the fileId. |
| [**filesGet**](FilesUploadFilesApi.md#filesGet) | **GET** /files | Returns a paginated list of files |
| [**filesPost**](FilesUploadFilesApi.md#filesPost) | **POST** /files | Uploads a file. |
| [**filesUrlPost**](FilesUploadFilesApi.md#filesUrlPost) | **POST** /files/url | Uploads a file from a URL |


<a id="filesByIdOrUrlGet"></a>
# **filesByIdOrUrlGet**
> ModelFile filesByIdOrUrlGet(fileIdOrUrl)

Get the details for a file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesUploadFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    FilesUploadFilesApi apiInstance = new FilesUploadFilesApi(defaultClient);
    String fileIdOrUrl = "fileIdOrUrl_example"; // String | The fileId or fileUrl of the file to be returned
    try {
      ModelFile result = apiInstance.filesByIdOrUrlGet(fileIdOrUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesUploadFilesApi#filesByIdOrUrlGet");
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
| **fileIdOrUrl** | **String**| The fileId or fileUrl of the file to be returned | |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="filesDownloadGet"></a>
# **filesDownloadGet**
> FileDownload filesDownloadGet(fileId, validSeconds)

A signed URL for downloading a private file can be returned by providing the fileId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesUploadFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    FilesUploadFilesApi apiInstance = new FilesUploadFilesApi(defaultClient);
    String fileId = "fileId_example"; // String | The URL of the file to be uploaded
    Integer validSeconds = 56; // Integer | The number of seconds that this signed URL should be valid for. The default is 60.
    try {
      FileDownload result = apiInstance.filesDownloadGet(fileId, validSeconds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesUploadFilesApi#filesDownloadGet");
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
| **fileId** | **String**| The URL of the file to be uploaded | |
| **validSeconds** | **Integer**| The number of seconds that this signed URL should be valid for. The default is 60. | [optional] |

### Return type

[**FileDownload**](FileDownload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The file was not found |  -  |
| **0** | OK |  -  |

<a id="filesGet"></a>
# **filesGet**
> ModelFile filesGet(query, sort, pageNumber, limit)

Returns a paginated list of files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesUploadFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    FilesUploadFilesApi apiInstance = new FilesUploadFilesApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'name':'file.txt'} matches all the files that have the name 'file.txt'
    String sort = "sort_example"; // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    try {
      ModelFile result = apiInstance.filesGet(query, sort, pageNumber, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesUploadFilesApi#filesGet");
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
| **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;file.txt&#39;} matches all the files that have the name &#39;file.txt&#39; | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="filesPost"></a>
# **filesPost**
> ModelFile filesPost(_file, isPrivate, hash)

Uploads a file.

- WARNING: File URLs or fileIds must be stored somewhere within the customData field for an app, review, developer or user. Unused files will be removed after a few days.  - This method is called on behalf of a developer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesUploadFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    FilesUploadFilesApi apiInstance = new FilesUploadFilesApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The file to be uploaded
    Boolean isPrivate = true; // Boolean | If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false.
    String hash = "hash_example"; // String | A comma separated list of hashes to return in order to verify file integrity.
    try {
      ModelFile result = apiInstance.filesPost(_file, isPrivate, hash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesUploadFilesApi#filesPost");
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
| **_file** | **File**| The file to be uploaded | |
| **isPrivate** | **Boolean**| If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false. | [optional] |
| **hash** | **String**| A comma separated list of hashes to return in order to verify file integrity. | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="filesUrlPost"></a>
# **filesUrlPost**
> ModelFile filesUrlPost(url, isPrivate)

Uploads a file from a URL

- WARNING: File URLs or fileIds must be stored somewhere within the customData field for an app, review, developer or user. Unused files will be removed after a few days. - This method is called on behalf of a developer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesUploadFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    FilesUploadFilesApi apiInstance = new FilesUploadFilesApi(defaultClient);
    String url = "url_example"; // String | The URL of the file to be uploaded
    Boolean isPrivate = true; // Boolean | If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false.
    try {
      ModelFile result = apiInstance.filesUrlPost(url, isPrivate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesUploadFilesApi#filesUrlPost");
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
| **url** | **String**| The URL of the file to be uploaded | |
| **isPrivate** | **Boolean**| If true, this file will be protected as a private file and require the generation of a signed URL in order to download using the Download File API. The default is false. | [optional] |

### Return type

[**ModelFile**](ModelFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

