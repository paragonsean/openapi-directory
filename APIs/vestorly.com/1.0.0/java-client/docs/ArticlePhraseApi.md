# ArticlePhraseApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findArticlePhrases**](ArticlePhraseApi.md#findArticlePhrases) | **GET** /article_phrases |  |


<a id="findArticlePhrases"></a>
# **findArticlePhrases**
> ArticlePhrases findArticlePhrases(vestorlyAuth, accessToken, textSearch, size, from)



Returns phrases used in Categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlePhraseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    ArticlePhraseApi apiInstance = new ArticlePhraseApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    String textSearch = "textSearch_example"; // String | Text to search phrases
    Integer size = 56; // Integer | Number of returned phrases
    Integer from = 56; // Integer | Number of phrases to skip
    try {
      ArticlePhrases result = apiInstance.findArticlePhrases(vestorlyAuth, accessToken, textSearch, size, from);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlePhraseApi#findArticlePhrases");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **accessToken** | **String**| OAuth Token | [optional] |
| **textSearch** | **String**| Text to search phrases | [optional] |
| **size** | **Integer**| Number of returned phrases | [optional] |
| **from** | **Integer**| Number of phrases to skip | [optional] |

### Return type

[**ArticlePhrases**](ArticlePhrases.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

