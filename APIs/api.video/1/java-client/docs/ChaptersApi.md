# ChaptersApi

All URIs are relative to *https://ws.api.video*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dELETEVideosVideoIdChaptersLanguage**](ChaptersApi.md#dELETEVideosVideoIdChaptersLanguage) | **DELETE** /videos/{videoId}/chapters/{language} | Delete a chapter |
| [**gETVideosVideoIdChapters**](ChaptersApi.md#gETVideosVideoIdChapters) | **GET** /videos/{videoId}/chapters | List video chapters |
| [**gETVideosVideoIdChaptersLanguage**](ChaptersApi.md#gETVideosVideoIdChaptersLanguage) | **GET** /videos/{videoId}/chapters/{language} | Show a chapter |
| [**pOSTVideosVideoIdChaptersLanguage**](ChaptersApi.md#pOSTVideosVideoIdChaptersLanguage) | **POST** /videos/{videoId}/chapters/{language} | Upload a chapter |


<a id="dELETEVideosVideoIdChaptersLanguage"></a>
# **dELETEVideosVideoIdChaptersLanguage**
> dELETEVideosVideoIdChaptersLanguage(videoId, language)

Delete a chapter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChaptersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ChaptersApi apiInstance = new ChaptersApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want to delete a chapter from. 
    String language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    try {
      apiInstance.dELETEVideosVideoIdChaptersLanguage(videoId, language);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChaptersApi#dELETEVideosVideoIdChaptersLanguage");
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
| **videoId** | **String**| The unique identifier for the video you want to delete a chapter from.  | |
| **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **404** | Not Found |  -  |

<a id="gETVideosVideoIdChapters"></a>
# **gETVideosVideoIdChapters**
> ChaptersListResponse gETVideosVideoIdChapters(videoId).currentPage(currentPage).pageSize(pageSize).execute();

List video chapters

Retrieve a list of all chapters for a specified video.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChaptersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ChaptersApi apiInstance = new ChaptersApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want to retrieve a list of chapters for.
    Integer currentPage = 1; // Integer | Choose the number of search results to return per page. Minimum value: 1
    Integer pageSize = 25; // Integer | Results per page. Allowed values 1-100, default is 25.
    try {
      ChaptersListResponse result = apiInstance.gETVideosVideoIdChapters(videoId)
            .currentPage(currentPage)
            .pageSize(pageSize)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChaptersApi#gETVideosVideoIdChapters");
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
| **videoId** | **String**| The unique identifier for the video you want to retrieve a list of chapters for. | |
| **currentPage** | **Integer**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1] |
| **pageSize** | **Integer**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25] |

### Return type

[**ChaptersListResponse**](ChaptersListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="gETVideosVideoIdChaptersLanguage"></a>
# **gETVideosVideoIdChaptersLanguage**
> Chapter gETVideosVideoIdChaptersLanguage(videoId, language)

Show a chapter

Chapters help your viewers find the sections of the video they are most interested in viewing. Tutorials that use the [chapters endpoint](https://api.video/blog/endpoints/chapters).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChaptersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ChaptersApi apiInstance = new ChaptersApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want to show a chapter for.
    String language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    try {
      Chapter result = apiInstance.gETVideosVideoIdChaptersLanguage(videoId, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChaptersApi#gETVideosVideoIdChaptersLanguage");
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
| **videoId** | **String**| The unique identifier for the video you want to show a chapter for. | |
| **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | |

### Return type

[**Chapter**](Chapter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Not Found |  -  |

<a id="pOSTVideosVideoIdChaptersLanguage"></a>
# **pOSTVideosVideoIdChaptersLanguage**
> Chapter pOSTVideosVideoIdChaptersLanguage(videoId, language, _file)

Upload a chapter

Chapters help break the video into sections. Read our [tutorial](https://api.video/blog/tutorials/adding-chapters-to-your-videos) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChaptersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ws.api.video");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ChaptersApi apiInstance = new ChaptersApi(defaultClient);
    String videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want to upload a chapter for.
    String language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    File _file = new File("/path/to/file"); // File | The VTT file describing the chapters you want to upload.
    try {
      Chapter result = apiInstance.pOSTVideosVideoIdChaptersLanguage(videoId, language, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChaptersApi#pOSTVideosVideoIdChaptersLanguage");
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
| **videoId** | **String**| The unique identifier for the video you want to upload a chapter for. | |
| **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | |
| **_file** | **File**| The VTT file describing the chapters you want to upload. | |

### Return type

[**Chapter**](Chapter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

