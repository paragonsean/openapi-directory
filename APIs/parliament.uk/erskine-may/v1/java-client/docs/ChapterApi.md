# ChapterApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiChapterChapterNumberGet**](ChapterApi.md#apiChapterChapterNumberGet) | **GET** /api/Chapter/{chapterNumber} | Returns a single chapter overview by chapter number. |


<a id="apiChapterChapterNumberGet"></a>
# **apiChapterChapterNumberGet**
> ErskineMayChapterOverview apiChapterChapterNumberGet(chapterNumber)

Returns a single chapter overview by chapter number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChapterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ChapterApi apiInstance = new ChapterApi(defaultClient);
    Integer chapterNumber = 56; // Integer | Chapter overview with the chapter number specified
    try {
      ErskineMayChapterOverview result = apiInstance.apiChapterChapterNumberGet(chapterNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChapterApi#apiChapterChapterNumberGet");
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
| **chapterNumber** | **Integer**| Chapter overview with the chapter number specified | |

### Return type

[**ErskineMayChapterOverview**](ErskineMayChapterOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

