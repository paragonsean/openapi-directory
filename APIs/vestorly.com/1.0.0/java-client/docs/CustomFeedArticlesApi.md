# CustomFeedArticlesApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findCustomFeedArticles**](CustomFeedArticlesApi.md#findCustomFeedArticles) | **GET** /custom_feeds/{id}/articles |  |


<a id="findCustomFeedArticles"></a>
# **findCustomFeedArticles**
> Articles findCustomFeedArticles(vestorlyAuth, id, accessToken, limit, sortBy, start, createdAtGteDaysAgo, textQuery)



Returns Articles by Category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedArticlesApi apiInstance = new CustomFeedArticlesApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | Category Id to fetch
    String accessToken = "accessToken_example"; // String | OAuth Token
    Integer limit = 56; // Integer | Limit on the number of articles to return
    String sortBy = "sortBy_example"; // String | Field on model to sort by
    Integer start = 56; // Integer | Field where the fetch will start from
    String createdAtGteDaysAgo = "createdAtGteDaysAgo_example"; // String | Filter retrieved articles since this date
    String textQuery = "textQuery_example"; // String | Search query parameter
    try {
      Articles result = apiInstance.findCustomFeedArticles(vestorlyAuth, id, accessToken, limit, sortBy, start, createdAtGteDaysAgo, textQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedArticlesApi#findCustomFeedArticles");
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
| **id** | **String**| Category Id to fetch | |
| **accessToken** | **String**| OAuth Token | [optional] |
| **limit** | **Integer**| Limit on the number of articles to return | [optional] |
| **sortBy** | **String**| Field on model to sort by | [optional] |
| **start** | **Integer**| Field where the fetch will start from | [optional] |
| **createdAtGteDaysAgo** | **String**| Filter retrieved articles since this date | [optional] |
| **textQuery** | **String**| Search query parameter | [optional] |

### Return type

[**Articles**](Articles.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

