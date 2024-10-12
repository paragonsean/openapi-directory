# ProductMediaFileApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMediaFiles**](ProductMediaFileApi.md#getMediaFiles) | **GET** /api/rest/v1/media-files | Get a list of product media files |
| [**getMediaFilesCode**](ProductMediaFileApi.md#getMediaFilesCode) | **GET** /api/rest/v1/media-files/{code} | Get a product media file |
| [**getMediaFilesCodeDownload**](ProductMediaFileApi.md#getMediaFilesCodeDownload) | **GET** /api/rest/v1/media-files/{code}/download | Download a product media file |
| [**postMediaFiles**](ProductMediaFileApi.md#postMediaFiles) | **POST** /api/rest/v1/media-files | Create a new product media file |


<a id="getMediaFiles"></a>
# **getMediaFiles**
> MediaFiles getMediaFiles(page, limit, withCount)

Get a list of product media files

This endpoint allows you to get a list of media files that are used as attribute values in products or product models.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductMediaFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ProductMediaFileApi apiInstance = new ProductMediaFileApi(defaultClient);
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 10; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Boolean withCount = false; // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    try {
      MediaFiles result = apiInstance.getMediaFiles(page, limit, withCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductMediaFileApi#getMediaFiles");
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
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10] |
| **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false] |

### Return type

[**MediaFiles**](MediaFiles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, current_page, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return media files paginated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **406** | Not Acceptable |  -  |

<a id="getMediaFilesCode"></a>
# **getMediaFilesCode**
> GetMediaFilesCode200Response getMediaFilesCode(code)

Get a product media file

This endpoint allows you to get the information about a given media file that is used as an attribute value of a product or a product model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductMediaFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ProductMediaFileApi apiInstance = new ProductMediaFileApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      GetMediaFilesCode200Response result = apiInstance.getMediaFilesCode(code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductMediaFileApi#getMediaFilesCode");
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
| **code** | **String**| Code of the resource | |

### Return type

[**GetMediaFilesCode200Response**](GetMediaFilesCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Resource not found |  -  |
| **406** | Not Acceptable |  -  |

<a id="getMediaFilesCodeDownload"></a>
# **getMediaFilesCodeDownload**
> getMediaFilesCodeDownload(code)

Download a product media file

This endpoint allows you to download a given media file that is used as an attribute value of a product or a product model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductMediaFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ProductMediaFileApi apiInstance = new ProductMediaFileApi(defaultClient);
    String code = "code_example"; // String | Code of the resource
    try {
      apiInstance.getMediaFilesCodeDownload(code);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductMediaFileApi#getMediaFilesCodeDownload");
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
| **code** | **String**| Code of the resource | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="postMediaFiles"></a>
# **postMediaFiles**
> postMediaFiles(contentType, body)

Create a new product media file

This endpoint allows you to create a new media file and associate it to an attribute value of a given product or product model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductMediaFileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ProductMediaFileApi apiInstance = new ProductMediaFileApi(defaultClient);
    String contentType = "contentType_example"; // String | Equal to 'multipart/form-data', no other value allowed
    PostMediaFilesRequest body = new PostMediaFilesRequest(); // PostMediaFilesRequest | 
    try {
      apiInstance.postMediaFiles(contentType, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductMediaFileApi#postMediaFiles");
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
| **contentType** | **String**| Equal to &#39;multipart/form-data&#39;, no other value allowed | |
| **body** | [**PostMediaFilesRequest**](PostMediaFilesRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - URI of the created resource <br>  |
| **400** | Bad request |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

