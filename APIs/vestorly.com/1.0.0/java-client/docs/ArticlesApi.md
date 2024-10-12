# ArticlesApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findArticleByID**](ArticlesApi.md#findArticleByID) | **GET** /articles/{id} |  |
| [**findArticles**](ArticlesApi.md#findArticles) | **GET** /articles |  |


<a id="findArticleByID"></a>
# **findArticleByID**
> Articleresponse findArticleByID(vestorlyAuth, id, accessToken)



Returns a single article

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | Article Id to fetch
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Articleresponse result = apiInstance.findArticleByID(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#findArticleByID");
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
| **id** | **String**| Article Id to fetch | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Articleresponse**](Articleresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article response |  -  |

<a id="findArticles"></a>
# **findArticles**
> Articles findArticles(vestorlyAuth, accessToken, limit, textQuery, sortDirection, sortBy)



Returns all articles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    Integer limit = 56; // Integer | Limit on the number of articles to return
    String textQuery = "textQuery_example"; // String | Search query parameter
    String sortDirection = "sortDirection_example"; // String | Direction of sort (used with sort_by parameter)
    String sortBy = "sortBy_example"; // String | Field on model to sort by
    try {
      Articles result = apiInstance.findArticles(vestorlyAuth, accessToken, limit, textQuery, sortDirection, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#findArticles");
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
| **limit** | **Integer**| Limit on the number of articles to return | [optional] |
| **textQuery** | **String**| Search query parameter | [optional] |
| **sortDirection** | **String**| Direction of sort (used with sort_by parameter) | [optional] |
| **sortBy** | **String**| Field on model to sort by | [optional] |

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

