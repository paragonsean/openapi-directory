# ImageStoreApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**copyImageStoreContent**](ImageStoreApi.md#copyImageStoreContent) | **POST** /ImageStore/$/Copy | Copies image store content internally |
| [**deleteImageStoreContent**](ImageStoreApi.md#deleteImageStoreContent) | **DELETE** /ImageStore/{contentPath} | Deletes existing image store content. |
| [**getImageStoreContent**](ImageStoreApi.md#getImageStoreContent) | **GET** /ImageStore/{contentPath} | Gets the image store content information. |
| [**getImageStoreRootContent**](ImageStoreApi.md#getImageStoreRootContent) | **GET** /ImageStore | Gets the content information at the root of the image store. |
| [**uploadFile**](ImageStoreApi.md#uploadFile) | **PUT** /ImageStore/{contentPath} | Uploads contents of the file to the image store. |


<a id="copyImageStoreContent"></a>
# **copyImageStoreContent**
> copyImageStoreContent(apiVersion, imageStoreCopyDescription, timeout)

Copies image store content internally

Copies the image store content from the source image store relative path to the destination image store relative path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ImageStoreApi apiInstance = new ImageStoreApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    ImageStoreCopyDescription imageStoreCopyDescription = new ImageStoreCopyDescription(); // ImageStoreCopyDescription | Describes the copy description for the image store.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.copyImageStoreContent(apiVersion, imageStoreCopyDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageStoreApi#copyImageStoreContent");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **imageStoreCopyDescription** | [**ImageStoreCopyDescription**](ImageStoreCopyDescription.md)| Describes the copy description for the image store. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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
| **200** | A successful operation will return 200 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="deleteImageStoreContent"></a>
# **deleteImageStoreContent**
> deleteImageStoreContent(apiVersion, contentPath, timeout)

Deletes existing image store content.

Deletes existing image store content being found within the given image store relative path. This can be used to delete uploaded application packages once they are provisioned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ImageStoreApi apiInstance = new ImageStoreApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String contentPath = "contentPath_example"; // String | Relative path to file or folder in the image store from its root.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.deleteImageStoreContent(apiVersion, contentPath, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageStoreApi#deleteImageStoreContent");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **contentPath** | **String**| Relative path to file or folder in the image store from its root. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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
| **200** | A successful operation will return 200 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getImageStoreContent"></a>
# **getImageStoreContent**
> ImageStoreContent getImageStoreContent(apiVersion, contentPath, timeout)

Gets the image store content information.

Returns the information about the image store content at the specified contentPath relative to the root of the image store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ImageStoreApi apiInstance = new ImageStoreApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String contentPath = "contentPath_example"; // String | Relative path to file or folder in the image store from its root.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      ImageStoreContent result = apiInstance.getImageStoreContent(apiVersion, contentPath, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageStoreApi#getImageStoreContent");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **contentPath** | **String**| Relative path to file or folder in the image store from its root. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**ImageStoreContent**](ImageStoreContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the requested image store content information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getImageStoreRootContent"></a>
# **getImageStoreRootContent**
> ImageStoreContent getImageStoreRootContent(apiVersion, timeout)

Gets the content information at the root of the image store.

Returns the information about the image store content at the root of the image store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ImageStoreApi apiInstance = new ImageStoreApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      ImageStoreContent result = apiInstance.getImageStoreRootContent(apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageStoreApi#getImageStoreRootContent");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**ImageStoreContent**](ImageStoreContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the requested image store content information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="uploadFile"></a>
# **uploadFile**
> uploadFile(apiVersion, contentPath, timeout)

Uploads contents of the file to the image store.

Uploads contents of the file to the image store. Use this API if the file is small enough to upload again if the connection fails. The file&#39;s data needs to be added to the request body. The contents will be uploaded to the specified path. Image store service uses a mark file to indicate the availability of the folder. The mark file is an empty file named \&quot;_.dir\&quot;. The mark file is generated by the image store service when all files in a folder are uploaded. When using File-by-File approach to upload application package in REST, the image store service isn&#39;t aware of the file hierarchy of the application package; you need to create a mark file per folder and upload it last, to let the image store service know that the folder is complete. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ImageStoreApi apiInstance = new ImageStoreApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This is a required parameter and it's value must be \"6.0\".
    String contentPath = "contentPath_example"; // String | Relative path to file or folder in the image store from its root.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.uploadFile(apiVersion, contentPath, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageStoreApi#uploadFile");
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
| **apiVersion** | **String**| The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;. | [default to 6.0] [enum: 6.0] |
| **contentPath** | **String**| Relative path to file or folder in the image store from its root. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

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
| **200** | If the upload request succeeds, the server returns the HTTP 200 OK status code. |  -  |
| **0** | The detailed error response. |  -  |

