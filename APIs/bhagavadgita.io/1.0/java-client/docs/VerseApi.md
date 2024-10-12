# VerseApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1ChaptersChapterNumberVersesGet**](VerseApi.md#apiV1ChaptersChapterNumberVersesGet) | **GET** /api/v1/chapters/{chapter_number}/verses | Get all the Verses from a Chapter. |
| [**apiV1ChaptersChapterNumberVersesVerseNumberGet**](VerseApi.md#apiV1ChaptersChapterNumberVersesVerseNumberGet) | **GET** /api/v1/chapters/{chapter_number}/verses/{verse_number} | Get a particular verse from a chapter. |
| [**apiV1VersesGet**](VerseApi.md#apiV1VersesGet) | **GET** /api/v1/verses | Get all the Verses. |


<a id="apiV1ChaptersChapterNumberVersesGet"></a>
# **apiV1ChaptersChapterNumberVersesGet**
> VerseSchema apiV1ChaptersChapterNumberVersesGet(accessToken, chapterNumber, language)

Get all the Verses from a Chapter.

Get a list of all Verses from a particular Chapter.&lt;br/&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VerseApi apiInstance = new VerseApi(defaultClient);
    String accessToken = "accessToken_example"; // String | Your app's access token.
    Integer chapterNumber = 1; // Integer | Which Chapter Number to filter?
    String language = "hi"; // String | Language to query. Leave blank for english.
    try {
      VerseSchema result = apiInstance.apiV1ChaptersChapterNumberVersesGet(accessToken, chapterNumber, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerseApi#apiV1ChaptersChapterNumberVersesGet");
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

[**VerseSchema**](VerseSchema.md)

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

<a id="apiV1ChaptersChapterNumberVersesVerseNumberGet"></a>
# **apiV1ChaptersChapterNumberVersesVerseNumberGet**
> VerseSchema apiV1ChaptersChapterNumberVersesVerseNumberGet(accessToken, chapterNumber, verseNumber, language)

Get a particular verse from a chapter.

Get a specific verse from a specific chapter.&lt;br/&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VerseApi apiInstance = new VerseApi(defaultClient);
    String accessToken = "accessToken_example"; // String | Your app's access token.
    Integer chapterNumber = 1; // Integer | Which Chapter Number to filter?
    String verseNumber = "1"; // String | Which Verse Number to filter?
    String language = "hi"; // String | Language to query. Leave blank for english.
    try {
      VerseSchema result = apiInstance.apiV1ChaptersChapterNumberVersesVerseNumberGet(accessToken, chapterNumber, verseNumber, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerseApi#apiV1ChaptersChapterNumberVersesVerseNumberGet");
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
| **verseNumber** | **String**| Which Verse Number to filter? | [default to 1] [enum: 1, 2, 3] |
| **language** | **String**| Language to query. Leave blank for english. | [optional] [enum: hi] |

### Return type

[**VerseSchema**](VerseSchema.md)

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
| **404** | Not Found: The chapter/verse number you are looking for could not be found. |  -  |
| **500** | Server Error: Something went wrong on our end. |  -  |

<a id="apiV1VersesGet"></a>
# **apiV1VersesGet**
> VerseSchema apiV1VersesGet(accessToken, language)

Get all the Verses.

Get a list of all Verses.&lt;br/&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VerseApi apiInstance = new VerseApi(defaultClient);
    String accessToken = "accessToken_example"; // String | Your app's access token.
    String language = "hi"; // String | Language to query. Leave blank for english.
    try {
      VerseSchema result = apiInstance.apiV1VersesGet(accessToken, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerseApi#apiV1VersesGet");
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

[**VerseSchema**](VerseSchema.md)

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
| **401** | Unauthorized: Inavlid access_token used. |  -  |
| **402** | Request Failed. |  -  |
| **500** | Server Error: Something went wrong on our end. |  -  |

