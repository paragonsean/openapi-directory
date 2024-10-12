# ArticlesApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createArticle**](ArticlesApi.md#createArticle) | **POST** /api/articles | Publish article |
| [**getArticleById**](ArticlesApi.md#getArticleById) | **GET** /api/articles/{id} | Published article by id |
| [**getArticleByPath**](ArticlesApi.md#getArticleByPath) | **GET** /api/articles/{username}/{slug} | Published article by path |
| [**getArticles**](ArticlesApi.md#getArticles) | **GET** /api/articles | Published articles |
| [**getLatestArticles**](ArticlesApi.md#getLatestArticles) | **GET** /api/articles/latest | Published articles sorted by published date |
| [**getOrgArticles_0**](ArticlesApi.md#getOrgArticles_0) | **GET** /api/organizations/{username}/articles | Organization&#39;s Articles |
| [**getUserAllArticles**](ArticlesApi.md#getUserAllArticles) | **GET** /api/articles/me/all | User&#39;s all articles |
| [**getUserArticles**](ArticlesApi.md#getUserArticles) | **GET** /api/articles/me | User&#39;s articles |
| [**getUserPublishedArticles**](ArticlesApi.md#getUserPublishedArticles) | **GET** /api/articles/me/published | User&#39;s published articles |
| [**getUserUnpublishedArticles**](ArticlesApi.md#getUserUnpublishedArticles) | **GET** /api/articles/me/unpublished | User&#39;s unpublished articles |
| [**unpublishArticle**](ArticlesApi.md#unpublishArticle) | **PUT** /api/articles/{id}/unpublish | Unpublish an article |
| [**updateArticle**](ArticlesApi.md#updateArticle) | **PUT** /api/articles/{id} | Update an article by id |
| [**videos_0**](ArticlesApi.md#videos_0) | **GET** /api/videos | Articles with a video |


<a id="createArticle"></a>
# **createArticle**
> createArticle(article)

Publish article

This endpoint allows the client to create a new article.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

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
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Article article = new Article(); // Article | 
    try {
      apiInstance.createArticle(article);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#createArticle");
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
| **article** | [**Article**](Article.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | An Article |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="getArticleById"></a>
# **getArticleById**
> List&lt;ArticleIndex&gt; getArticleById(id)

Published article by id

This endpoint allows the client to retrieve a single published article given its &#x60;id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      List<ArticleIndex> result = apiInstance.getArticleById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getArticleById");
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
| **id** | **Integer**|  | |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Article |  -  |
| **404** | Article Not Found |  -  |

<a id="getArticleByPath"></a>
# **getArticleByPath**
> List&lt;ArticleIndex&gt; getArticleByPath(username, slug)

Published article by path

This endpoint allows the client to retrieve a single published article given its &#x60;path&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String username = "username_example"; // String | 
    String slug = "slug_example"; // String | 
    try {
      List<ArticleIndex> result = apiInstance.getArticleByPath(username, slug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getArticleByPath");
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
| **username** | **String**|  | |
| **slug** | **String**|  | |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Article |  -  |
| **404** | Article Not Found |  -  |

<a id="getArticles"></a>
# **getArticles**
> List&lt;ArticleIndex&gt; getArticles(page, perPage, tag, tags, tagsExclude, username, state, top, collectionId)

Published articles

This endpoint allows the client to retrieve a list of articles.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  By default it will return featured, published articles ordered by descending popularity.  It supports pagination, each page will contain &#x60;30&#x60; articles by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    String tag = "discuss"; // String | Using this parameter will retrieve articles that contain the requested tag. Articles will be ordered by descending popularity.This parameter can be used in conjuction with `top`.
    String tags = "javascript, css"; // String | Using this parameter will retrieve articles with any of the comma-separated tags. Articles will be ordered by descending popularity.
    String tagsExclude = "node, java"; // String | Using this parameter will retrieve articles that do _not_ contain _any_ of comma-separated tags. Articles will be ordered by descending popularity.
    String username = "ben"; // String | Using this parameter will retrieve articles belonging             to a User or Organization ordered by descending publication date.             If `state=all` the number of items returned will be `1000` instead of the default `30`.             This parameter can be used in conjuction with `state`.
    String state = "fresh"; // String | Using this parameter will allow the client to check which articles are fresh or rising.             If `state=fresh` the server will return fresh articles.             If `state=rising` the server will return rising articles.             This param can be used in conjuction with `username`, only if set to `all`.
    Integer top = 2; // Integer | Using this parameter will allow the client to return the most popular articles in the last `N` days. `top` indicates the number of days since publication of the articles returned. This param can be used in conjuction with `tag`.
    Integer collectionId = 99; // Integer | Adding this will allow the client to return the list of articles belonging to the requested collection, ordered by ascending publication date.
    try {
      List<ArticleIndex> result = apiInstance.getArticles(page, perPage, tag, tags, tagsExclude, username, state, top, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getArticles");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |
| **tag** | **String**| Using this parameter will retrieve articles that contain the requested tag. Articles will be ordered by descending popularity.This parameter can be used in conjuction with &#x60;top&#x60;. | [optional] |
| **tags** | **String**| Using this parameter will retrieve articles with any of the comma-separated tags. Articles will be ordered by descending popularity. | [optional] |
| **tagsExclude** | **String**| Using this parameter will retrieve articles that do _not_ contain _any_ of comma-separated tags. Articles will be ordered by descending popularity. | [optional] |
| **username** | **String**| Using this parameter will retrieve articles belonging             to a User or Organization ordered by descending publication date.             If &#x60;state&#x3D;all&#x60; the number of items returned will be &#x60;1000&#x60; instead of the default &#x60;30&#x60;.             This parameter can be used in conjuction with &#x60;state&#x60;. | [optional] |
| **state** | **String**| Using this parameter will allow the client to check which articles are fresh or rising.             If &#x60;state&#x3D;fresh&#x60; the server will return fresh articles.             If &#x60;state&#x3D;rising&#x60; the server will return rising articles.             This param can be used in conjuction with &#x60;username&#x60;, only if set to &#x60;all&#x60;. | [optional] [enum: fresh, rising, all] |
| **top** | **Integer**| Using this parameter will allow the client to return the most popular articles in the last &#x60;N&#x60; days. &#x60;top&#x60; indicates the number of days since publication of the articles returned. This param can be used in conjuction with &#x60;tag&#x60;. | [optional] |
| **collectionId** | **Integer**| Adding this will allow the client to return the list of articles belonging to the requested collection, ordered by ascending publication date. | [optional] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of Articles |  -  |

<a id="getLatestArticles"></a>
# **getLatestArticles**
> List&lt;ArticleIndex&gt; getLatestArticles(page, perPage)

Published articles sorted by published date

This endpoint allows the client to retrieve a list of articles. ordered by descending publish date.  It supports pagination, each page will contain 30 articles by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getLatestArticles(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getLatestArticles");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of Articles |  -  |

<a id="getOrgArticles_0"></a>
# **getOrgArticles_0**
> List&lt;ArticleIndex&gt; getOrgArticles_0(username, page, perPage)

Organization&#39;s Articles

This endpoint allows the client to retrieve a list of Articles belonging to the organization  It supports pagination, each page will contain &#x60;30&#x60; users by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String username = "username_example"; // String | 
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getOrgArticles_0(username, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getOrgArticles_0");
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
| **username** | **String**|  | |
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Organization&#39;s Articles |  -  |
| **404** | Not Found |  -  |

<a id="getUserAllArticles"></a>
# **getUserAllArticles**
> List&lt;ArticleIndex&gt; getUserAllArticles(page, perPage)

User&#39;s all articles

This endpoint allows the client to retrieve a list of all articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  It will return both published and unpublished articles with pagination.  Unpublished articles will be at the top of the list in reverse chronological creation order. Published articles will follow in reverse chronological publication order.  By default a page will contain 30 articles.

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
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getUserAllArticles(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getUserAllArticles");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of the authenticated user&#39;s Articles |  -  |
| **401** | Unauthorized |  -  |

<a id="getUserArticles"></a>
# **getUserArticles**
> List&lt;ArticleIndex&gt; getUserArticles(page, perPage)

User&#39;s articles

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

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
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getUserArticles(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getUserArticles");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of the authenticated user&#39;s Articles |  -  |
| **401** | Unauthorized |  -  |

<a id="getUserPublishedArticles"></a>
# **getUserPublishedArticles**
> List&lt;ArticleIndex&gt; getUserPublishedArticles(page, perPage)

User&#39;s published articles

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

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
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getUserPublishedArticles(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getUserPublishedArticles");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of the authenticated user&#39;s Articles |  -  |
| **401** | Unauthorized |  -  |

<a id="getUserUnpublishedArticles"></a>
# **getUserUnpublishedArticles**
> List&lt;ArticleIndex&gt; getUserUnpublishedArticles(page, perPage)

User&#39;s unpublished articles

This endpoint allows the client to retrieve a list of unpublished articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Unpublished articles will be in reverse chronological creation order.  It will return unpublished articles with pagination. By default a page will contain 30 articles.

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
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getUserUnpublishedArticles(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getUserUnpublishedArticles");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of the authenticated user&#39;s Articles |  -  |
| **401** | Unauthorized |  -  |

<a id="unpublishArticle"></a>
# **unpublishArticle**
> unpublishArticle(id, note)

Unpublish an article

This endpoint allows the client to unpublish an article.  The user associated with the API key must have any &#39;admin&#39; or &#39;moderator&#39; role.  The article will be unpublished and will no longer be visible to the public. It will remain in the database and will set back to draft status on the author&#39;s posts dashboard. Any notifications associated with the article will be deleted. Any comments on the article will remain.

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
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer id = 1; // Integer | The ID of the article to unpublish.
    String note = "Admin requested unpublishing all articles via API"; // String | Content for the note that's created along with unpublishing
    try {
      apiInstance.unpublishArticle(id, note);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#unpublishArticle");
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
| **id** | **Integer**| The ID of the article to unpublish. | |
| **note** | **String**| Content for the note that&#39;s created along with unpublishing | [optional] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Article successfully unpublished |  -  |
| **401** | Unauthorized |  -  |
| **404** | Article Not Found |  -  |

<a id="updateArticle"></a>
# **updateArticle**
> updateArticle(id, article)

Update an article by id

This endpoint allows the client to update an existing article.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.

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
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer id = 123; // Integer | The ID of the user to unpublish.
    Article article = new Article(); // Article | 
    try {
      apiInstance.updateArticle(id, article);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#updateArticle");
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
| **id** | **Integer**| The ID of the user to unpublish. | |
| **article** | [**Article**](Article.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Article |  -  |
| **401** | Unauthorized |  -  |
| **404** | Article Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="videos_0"></a>
# **videos_0**
> List&lt;VideoArticle&gt; videos_0(page, perPage)

Articles with a video

This endpoint allows the client to retrieve a list of articles that are uploaded with a video.  It will only return published video articles ordered by descending popularity.  It supports pagination, each page will contain 24 articles by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 24; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<VideoArticle> result = apiInstance.videos_0(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#videos_0");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 24] |

### Return type

[**List&lt;VideoArticle&gt;**](VideoArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of all articles with videos |  -  |

