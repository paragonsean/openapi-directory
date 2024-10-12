# UploadsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelFileUploadByToken**](UploadsApi.md#cancelFileUploadByToken) | **DELETE** /v4/uploads/{token} | Cancel file upload |
| [**completeFileUploadByToken**](UploadsApi.md#completeFileUploadByToken) | **PUT** /v4/uploads/{token} | Complete file upload |
| [**uploadFileByTokenAsMultipart1**](UploadsApi.md#uploadFileByTokenAsMultipart1) | **POST** /v4/uploads/{token} | Upload file |


<a id="cancelFileUploadByToken"></a>
# **cancelFileUploadByToken**
> cancelFileUploadByToken(token)

Cancel file upload

### Description: Cancel file upload.  ### Precondition: Valid upload token.  ### Postcondition: Upload canceled, token invalidated and all already transfered chunks removed.  ### Further Information: It is recommended to notify the API about cancelled uploads if possible.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UploadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    UploadsApi apiInstance = new UploadsApi(defaultClient);
    String token = "token_example"; // String | Upload token
    try {
      apiInstance.cancelFileUploadByToken(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling UploadsApi#cancelFileUploadByToken");
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
| **token** | **String**| Upload token | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **507** | Insufficient Storage |  -  |

<a id="completeFileUploadByToken"></a>
# **completeFileUploadByToken**
> Node completeFileUploadByToken(token, xSdsDateFormat, completeUploadRequest)

Complete file upload

### Description: Finish uploading a file.  ### Precondition: Valid upload token.  ### Postcondition: File created.  ### Further Information: The provided file name might be changed in accordance with the resolution strategy:  * **autorename**: changes the file name and adds a number to avoid conflicts. * **overwrite**: deletes any old file with the same file name. * **fail**: returns an error; in this case, another &#x60;PUT&#x60; request with a different file name may be sent.  Please ensure that all chunks have been transferred correctly before finishing the upload.  Download share id (if exists) gets changed if: - node with the same name exists in the target container - &#x60;resolutionStrategy&#x60; is &#x60;overwrite&#x60; - &#x60;keepShareLinks&#x60; is &#x60;true&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UploadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    UploadsApi apiInstance = new UploadsApi(defaultClient);
    String token = "token_example"; // String | Upload token
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    CompleteUploadRequest completeUploadRequest = new CompleteUploadRequest(); // CompleteUploadRequest | 
    try {
      Node result = apiInstance.completeFileUploadByToken(token, xSdsDateFormat, completeUploadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UploadsApi#completeFileUploadByToken");
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
| **token** | **String**| Upload token | |
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **completeUploadRequest** | [**CompleteUploadRequest**](CompleteUploadRequest.md)|  | [optional] |

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **409** | Conflict |  -  |
| **507** | Insufficient Storage |  -  |

<a id="uploadFileByTokenAsMultipart1"></a>
# **uploadFileByTokenAsMultipart1**
> ChunkUploadResponse uploadFileByTokenAsMultipart1(token, _file, contentRange)

Upload file

### Description:   Upload a (chunk of a) file.  ### Precondition: Valid upload token.  ### Postcondition: Chunk uploaded.  ### Further Information: Range requests are supported.    Following &#x60;Content-Types&#x60; are supported by this API: * &#x60;multipart/form-data&#x60; * provided &#x60;Content-Type&#x60;  For both file upload types set the correct &#x60;Content-Type&#x60; header and body.    ### Examples:    * &#x60;multipart/form-data&#x60; &#x60;&#x60;&#x60; POST /api/v4/uploads/{token} HTTP/1.1  Header: ... Content-Type: multipart/form-data; boundary&#x3D;----WebKitFormBoundary7MA4YWxkTrZu0gW ...  Body: ------WebKitFormBoundary7MA4YWxkTrZu0gW Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;file.txt\&quot; Content-Type: text/plain  Content of file.txt ------WebKitFormBoundary7MA4YWxkTrZu0gW-- &#x60;&#x60;&#x60;  * any other &#x60;Content-Type&#x60;  &#x60;&#x60;&#x60; POST /api/v4/uploads/{token} HTTP/1.1  Header: ... Content-Type: { ... } ...  Body: raw content &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UploadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    UploadsApi apiInstance = new UploadsApi(defaultClient);
    String token = "token_example"; // String | Upload token
    File _file = new File("/path/to/file"); // File | File
    String contentRange = "contentRange_example"; // String | Content-Range   e.g. `bytes 0-999/3980`
    try {
      ChunkUploadResponse result = apiInstance.uploadFileByTokenAsMultipart1(token, _file, contentRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UploadsApi#uploadFileByTokenAsMultipart1");
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
| **token** | **String**| Upload token | |
| **_file** | **File**| File | |
| **contentRange** | **String**| Content-Range   e.g. &#x60;bytes 0-999/3980&#x60; | [optional] |

### Return type

[**ChunkUploadResponse**](ChunkUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **507** | Insufficient Storage |  -  |

