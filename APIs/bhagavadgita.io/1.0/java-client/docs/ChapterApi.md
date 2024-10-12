# ChapterApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1ChaptersChapterNumberGet**](ChapterApi.md#apiV1ChaptersChapterNumberGet) | **GET** /api/v1/chapters/{chapter_number} | Get a specific chapter from the Bhagavad Gita. |
| [**apiV1ChaptersGet**](ChapterApi.md#apiV1ChaptersGet) | **GET** /api/v1/chapters | Get all the 18 Chapters of the Bhagavad Gita. |


<a id="apiV1ChaptersChapterNumberGet"></a>
# **apiV1ChaptersChapterNumberGet**
> ChapterSchema apiV1ChaptersChapterNumberGet(accessToken, chapterNumber, language)

Get a specific chapter from the Bhagavad Gita.

Get information about a specific chapter from the Bhagavad Gita.&lt;br/&gt;

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
    String accessToken = "accessToken_example"; // String | Your app's access token.
    Integer chapterNumber = 1; // Integer | Which Chapter Number to filter?
    String language = "hi"; // String | Language to query. Leave blank for english.
    try {
      ChapterSchema result = apiInstance.apiV1ChaptersChapterNumberGet(accessToken, chapterNumber, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChapterApi#apiV1ChaptersChapterNumberGet");
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
| **accessToken** | **String**| Your app&#39;s access token. | |
| **chapterNumber** | **Integer**| Which Chapter Number to filter? | [default to 1] [enum: 1, 2, 3] |
| **language** | **String**| Language to query. Leave blank for english. | [optional] [enum: hi] |

### Return type

[**ChapterSchema**](ChapterSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success: Everything worked as expected. |  -  |
| **400** | Bad Request: The request was unacceptable due to wrong parameter(s). |  -  |
| **401** | Unauthorized: Invalid access_token used. |  -  |
| **402** | Request Failed. |  -  |
| **404** | Not Found: The chapter number you are looking for could not be found. |  -  |
| **500** | Server Error: Something went wrong on our end. |  -  |

<a id="apiV1ChaptersGet"></a>
# **apiV1ChaptersGet**
> ChapterSchema apiV1ChaptersGet(accessToken, language)

Get all the 18 Chapters of the Bhagavad Gita.

Get a list of all the 18 Chapters of the Bhagavad Gita.&lt;br/&gt;

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
    String accessToken = "accessToken_example"; // String | Your app's access token.
    String language = "hi"; // String | Language to query. Leave blank for english.
    try {
      ChapterSchema result = apiInstance.apiV1ChaptersGet(accessToken, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChapterApi#apiV1ChaptersGet");
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
| **accessToken** | **String**| Your app&#39;s access token. | |
| **language** | **String**| Language to query. Leave blank for english. | [optional] [enum: hi] |

### Return type

[**ChapterSchema**](ChapterSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success: Everything worked as expected. |  -  |
| **400** | Bad Request: The request was unacceptable due to wrong parameter(s). |  -  |
| **401** | Unauthorized: Invalid access_token used. |  -  |
| **402** | Request Failed. |  -  |
| **500** | Server Error: Something went wrong on our end. |  -  |

