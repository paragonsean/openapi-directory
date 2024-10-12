# ArticlesApi

All URIs are relative to *https://api.zalando.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**articleReviewsGet**](ArticlesApi.md#articleReviewsGet) | **GET** /article-reviews | Get Article Reviews |
| [**articleReviewsReviewIdGet**](ArticlesApi.md#articleReviewsReviewIdGet) | **GET** /article-reviews/{reviewId} | Get Article Reviews by reviewId |
| [**articleReviewsSummariesArticleModelIdGet**](ArticlesApi.md#articleReviewsSummariesArticleModelIdGet) | **GET** /article-reviews-summaries/{articleModelId} | Get Article Reviews Summaries by articleModelId |
| [**articleReviewsSummariesGet**](ArticlesApi.md#articleReviewsSummariesGet) | **GET** /article-reviews-summaries | Get Article Reviews Summaries |
| [**articlesArticleIdGet**](ArticlesApi.md#articlesArticleIdGet) | **GET** /articles/{articleId} | Get Article by articleId |
| [**articlesArticleIdMediaGet**](ArticlesApi.md#articlesArticleIdMediaGet) | **GET** /articles/{articleId}/media | Get Article media by articleId |
| [**articlesArticleIdReviewsGet**](ArticlesApi.md#articlesArticleIdReviewsGet) | **GET** /articles/{articleId}/reviews | Get Article reviews by articleId |
| [**articlesArticleIdReviewsSummaryGet**](ArticlesApi.md#articlesArticleIdReviewsSummaryGet) | **GET** /articles/{articleId}/reviews-summary | Get Article reviews summary by articleId |
| [**articlesArticleIdUnitsGet**](ArticlesApi.md#articlesArticleIdUnitsGet) | **GET** /articles/{articleId}/units | Get Article units by articleId |
| [**articlesArticleIdUnitsUnitIdGet**](ArticlesApi.md#articlesArticleIdUnitsUnitIdGet) | **GET** /articles/{articleId}/units/{unitId} | Get Article units by articleId snd unitId |
| [**articlesGet**](ArticlesApi.md#articlesGet) | **GET** /articles | Search for Articles |


<a id="articleReviewsGet"></a>
# **articleReviewsGet**
> ArticleReviews articleReviewsGet(articleId, articleModelId, minStarRating, maxStarRating, sort, page, pageSize, acceptLanguage, fields)

Get Article Reviews

Zalando API Article Reviews Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    List<String> articleId = Arrays.asList(); // List<String> | Article IDs. A list of config SKUs for which the article reviews will be returned. Required if articleModelId is empty. 
    List<String> articleModelId = Arrays.asList(); // List<String> | Article model IDs. A list of model SKUs for which the article reviews will be returned. Required if articleId is empty. 
    String minStarRating = "minStarRating_example"; // String | To get reviews with minimum star rating.
    String maxStarRating = "maxStarRating_example"; // String | To get reviews with maximum star rating.
    String sort = "newest"; // String | articles are sorted on reviews provided by customers (eg: best)
    String page = "page_example"; // String | to request with required page number or pagination
    String pageSize = "pageSize_example"; // String | to request with required page size in a page
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      ArticleReviews result = apiInstance.articleReviewsGet(articleId, articleModelId, minStarRating, maxStarRating, sort, page, pageSize, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleReviewsGet");
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
| **articleId** | [**List&lt;String&gt;**](String.md)| Article IDs. A list of config SKUs for which the article reviews will be returned. Required if articleModelId is empty.  | [optional] |
| **articleModelId** | [**List&lt;String&gt;**](String.md)| Article model IDs. A list of model SKUs for which the article reviews will be returned. Required if articleId is empty.  | [optional] |
| **minStarRating** | **String**| To get reviews with minimum star rating. | [optional] |
| **maxStarRating** | **String**| To get reviews with maximum star rating. | [optional] |
| **sort** | **String**| articles are sorted on reviews provided by customers (eg: best) | [optional] [default to newest] [enum: newest, best, worst, most_helpful] |
| **page** | **String**| to request with required page number or pagination | [optional] |
| **pageSize** | **String**| to request with required page size in a page | [optional] |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**ArticleReviews**](ArticleReviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Articles Reviews response. |  -  |
| **400** | Bad request. |  -  |

<a id="articleReviewsReviewIdGet"></a>
# **articleReviewsReviewIdGet**
> ArticleReview articleReviewsReviewIdGet(reviewId, acceptLanguage, fields)

Get Article Reviews by reviewId

Zalando API ArticleReviews Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String reviewId = "reviewId_example"; // String | To get unique review by review Id.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      ArticleReview result = apiInstance.articleReviewsReviewIdGet(reviewId, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleReviewsReviewIdGet");
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
| **reviewId** | **String**| To get unique review by review Id. | |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**ArticleReview**](ArticleReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Articles Reviews by reviewId response. |  -  |
| **404** | Not found. |  -  |

<a id="articleReviewsSummariesArticleModelIdGet"></a>
# **articleReviewsSummariesArticleModelIdGet**
> ArticleReviewsSummary articleReviewsSummariesArticleModelIdGet(articleModelId, acceptLanguage, fields)

Get Article Reviews Summaries by articleModelId

Zalando API ArticleReviewsSummaries Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String articleModelId = "articleModelId_example"; // String | To get unique reviews summary from article model Id.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      ArticleReviewsSummary result = apiInstance.articleReviewsSummariesArticleModelIdGet(articleModelId, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleReviewsSummariesArticleModelIdGet");
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
| **articleModelId** | **String**| To get unique reviews summary from article model Id. | |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**ArticleReviewsSummary**](ArticleReviewsSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Articles Reviews Summaries by articleModelId response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |

<a id="articleReviewsSummariesGet"></a>
# **articleReviewsSummariesGet**
> ArticleReviewsSummaries articleReviewsSummariesGet(articleModelId, page, pageSize, acceptLanguage, fields)

Get Article Reviews Summaries

Zalando API Article Reviews Summaries Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    List<String> articleModelId = Arrays.asList(); // List<String> | Article model IDs. A list of model SKUs for which the article review summaries will be returned.
    String page = "page_example"; // String | to request with required page number or pagination
    String pageSize = "pageSize_example"; // String | to request with required page size in a page
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      ArticleReviewsSummaries result = apiInstance.articleReviewsSummariesGet(articleModelId, page, pageSize, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articleReviewsSummariesGet");
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
| **articleModelId** | [**List&lt;String&gt;**](String.md)| Article model IDs. A list of model SKUs for which the article review summaries will be returned. | |
| **page** | **String**| to request with required page number or pagination | [optional] |
| **pageSize** | **String**| to request with required page size in a page | [optional] |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**ArticleReviewsSummaries**](ArticleReviewsSummaries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Articles Reviews Summaries response. |  -  |
| **400** | Bad request. |  -  |

<a id="articlesArticleIdGet"></a>
# **articlesArticleIdGet**
> Article articlesArticleIdGet(articleId, acceptLanguage, fields)

Get Article by articleId

Zalando API Article Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String articleId = "articleId_example"; // String | To get unique article for article Id.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      Article result = apiInstance.articlesArticleIdGet(articleId, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesArticleIdGet");
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
| **articleId** | **String**| To get unique article for article Id. | |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**Article**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |

<a id="articlesArticleIdMediaGet"></a>
# **articlesArticleIdMediaGet**
> ArticleMedia articlesArticleIdMediaGet(articleId, acceptLanguage, fields)

Get Article media by articleId

Zalando API Article Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String articleId = "articleId_example"; // String | To get unique article for article Id media.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      ArticleMedia result = apiInstance.articlesArticleIdMediaGet(articleId, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesArticleIdMediaGet");
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
| **articleId** | **String**| To get unique article for article Id media. | |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**ArticleMedia**](ArticleMedia.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |

<a id="articlesArticleIdReviewsGet"></a>
# **articlesArticleIdReviewsGet**
> ArticleReviews articlesArticleIdReviewsGet(articleId, minStarRating, maxStarRating, sort, page, pageSize, acceptLanguage, fields)

Get Article reviews by articleId

Zalando API Article Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String articleId = "articleId_example"; // String | To get unique article for article Id reviews.
    String minStarRating = "minStarRating_example"; // String | To get reviews with minimum star rating.
    String maxStarRating = "maxStarRating_example"; // String | To get reviews with maximum star rating.
    String sort = "newest"; // String | articles are sorted on reviews provided by customers (eg: best)
    String page = "page_example"; // String | to request with required page number or pagination
    String pageSize = "pageSize_example"; // String | to request with required page size in a page
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      ArticleReviews result = apiInstance.articlesArticleIdReviewsGet(articleId, minStarRating, maxStarRating, sort, page, pageSize, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesArticleIdReviewsGet");
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
| **articleId** | **String**| To get unique article for article Id reviews. | |
| **minStarRating** | **String**| To get reviews with minimum star rating. | [optional] |
| **maxStarRating** | **String**| To get reviews with maximum star rating. | [optional] |
| **sort** | **String**| articles are sorted on reviews provided by customers (eg: best) | [optional] [default to newest] [enum: newest, best, worst, most_helpful] |
| **page** | **String**| to request with required page number or pagination | [optional] |
| **pageSize** | **String**| to request with required page size in a page | [optional] |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**ArticleReviews**](ArticleReviews.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |

<a id="articlesArticleIdReviewsSummaryGet"></a>
# **articlesArticleIdReviewsSummaryGet**
> ArticleReviewsSummary articlesArticleIdReviewsSummaryGet(articleId, acceptLanguage, fields)

Get Article reviews summary by articleId

Zalando API Article Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String articleId = "articleId_example"; // String | To get unique article for article Id reviews summary.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      ArticleReviewsSummary result = apiInstance.articlesArticleIdReviewsSummaryGet(articleId, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesArticleIdReviewsSummaryGet");
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
| **articleId** | **String**| To get unique article for article Id reviews summary. | |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**ArticleReviewsSummary**](ArticleReviewsSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |

<a id="articlesArticleIdUnitsGet"></a>
# **articlesArticleIdUnitsGet**
> List&lt;ArticleUnit&gt; articlesArticleIdUnitsGet(articleId, acceptLanguage, fields)

Get Article units by articleId

Zalando API Article Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String articleId = "articleId_example"; // String | To get unique article for article Id units.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      List<ArticleUnit> result = apiInstance.articlesArticleIdUnitsGet(articleId, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesArticleIdUnitsGet");
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
| **articleId** | **String**| To get unique article for article Id units. | |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**List&lt;ArticleUnit&gt;**](ArticleUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |

<a id="articlesArticleIdUnitsUnitIdGet"></a>
# **articlesArticleIdUnitsUnitIdGet**
> ArticleUnit articlesArticleIdUnitsUnitIdGet(articleId, unitId, acceptLanguage, fields)

Get Article units by articleId snd unitId

Zalando API Article Schema

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String articleId = "articleId_example"; // String | To get unique article for article Id.
    String unitId = "unitId_example"; // String | To get unique article for article Id unit.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      ArticleUnit result = apiInstance.articlesArticleIdUnitsUnitIdGet(articleId, unitId, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesArticleIdUnitsUnitIdGet");
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
| **articleId** | **String**| To get unique article for article Id. | |
| **unitId** | **String**| To get unique article for article Id unit. | |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**ArticleUnit**](ArticleUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Article response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |

<a id="articlesGet"></a>
# **articlesGet**
> Articles articlesGet(articleId, articleModelId, articleUnitId, activationDate, ageGroup, assortmentArea, brand, brandfamily, category, color, den, filling, fullText, gender, heelForm, heelHeight, length, occasion, pattern, price, sale, season, shaftHeight, shaftWidth, shirtCollar, shoeFastener, shoeToecap, shopArea, size, sports, technology, trouserRise, upperMaterial, volume, page, pageSize, sort, acceptLanguage, fields)

Search for Articles

Search for articles based on various different possible filter like e.g. the &#x60;brandFamily&#x60;, the &#x60;catagory&#x60; or a specific &#x60;color&#x60;. See [Filters](https://todo) for a list of all available filter options.  The default &#x60;pageSize&#x60; for responses is set to &#x60;20&#x60;. You can add a &#x60;pageSize&#x60; request parameter to adjust that. Please keep in mind that the maximum &#x60;pageSize&#x60; for this resource is &#x60;200&#x60;.  The endpoint also supports reducing the fields returned for each article via the &#x60;fields&#x60; parameter. Please refer to [fields parameter](https://todo) for more details.

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
    defaultClient.setBasePath("https://api.zalando.com");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    List<String> articleId = Arrays.asList(); // List<String> | The `articleIds` to use use for filtering.  One or more `articleIds` might be used as a filter criteria. Submit multiple `articleId` request parameters for more than one to be used. They will be treated as `OR` criteria.
    List<String> articleModelId = Arrays.asList(); // List<String> | filters by article ModelId
    List<String> articleUnitId = Arrays.asList(); // List<String> | filters by article's unit id
    List<String> activationDate = Arrays.asList(); // List<String> | period or time the articles are activated for selling in the shop
    List<String> ageGroup = Arrays.asList(); // List<String> | filters by age group (eg: kids)
    List<String> assortmentArea = Arrays.asList(); // List<String> | filters by classification of articles (eg: maternity) 
    List<String> brand = Arrays.asList(); // List<String> | filters by brand key given by user (eg: SA5)
    List<String> brandfamily = Arrays.asList(); // List<String> | filters by brand family key (eg: nike) 
    List<String> category = Arrays.asList(); // List<String> | filters by category (eg: Socks, Rain Coats)
    List<String> color = Arrays.asList(); // List<String> | filters by color (eg: red, blue)
    List<String> den = Arrays.asList(); // List<String> | filters by den 
    List<String> filling = Arrays.asList(); // List<String> | filters by different kinds of garment filling materials (eg: satin, wolle)
    String fullText = "fullText_example"; // String | filters by text (eg: search by 'as' gives result with articles of brand Sass)
    List<String> gender = Arrays.asList(); // List<String> | filters by gender
    List<String> heelForm = Arrays.asList(); // List<String> | filters by heel form (eg: flat)
    List<String> heelHeight = Arrays.asList(); // List<String> | filters by height of the heel size or length (eg: xs)
    String length = "length_example"; // String | filters by garments length (eg: 3/4 length, knee-length)
    List<String> occasion = Arrays.asList(); // List<String> | filters by type of occasion (eg: party, business)
    List<String> pattern = Arrays.asList(); // List<String> | filters by pattern on the garments (eg: animal print, plain)
    String price = "price_example"; // String | filters all articles in price range (eg: 9-90)
    List<String> sale = Arrays.asList(); // List<String> | filters discounted articles marked as sale
    List<String> season = Arrays.asList(); // List<String> | filters by season (Autumn/Winter or Spring/Summer)
    List<String> shaftHeight = Arrays.asList(); // List<String> | filters by shaft height (eg: s, xs)
    List<String> shaftWidth = Arrays.asList(); // List<String> | filters by shaft width (eg: s, l)
    List<String> shirtCollar = Arrays.asList(); // List<String> | filters by shirt collar styles (eg: low V neck, lined collar)
    List<String> shoeFastener = Arrays.asList(); // List<String> | filters by shoe fastener types (eg: buckle, lacing)
    List<String> shoeToecap = Arrays.asList(); // List<String> | filters by shoe toe cap variants (eg: pointed, square)
    List<String> shopArea = Arrays.asList(); // List<String> | filters by classification of articles
    String size = "size_example"; // String | filters by size
    List<String> sports = Arrays.asList(); // List<String> | filters by different sport activities (eg: football)
    List<String> technology = Arrays.asList(); // List<String> | filters by technology used to produce the articles
    List<String> trouserRise = Arrays.asList(); // List<String> | filters by trouser rise
    List<String> upperMaterial = Arrays.asList(); // List<String> | filters by different type of upper material used on garments (eg: lace)
    List<String> volume = Arrays.asList(); // List<String> | filters by volume
    String page = "page_example"; // String | to request with required page number or pagination
    String pageSize = "pageSize_example"; // String | to request with required page size in a page
    String sort = "popularity"; // String | sorting order (eg: popularity)
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      Articles result = apiInstance.articlesGet(articleId, articleModelId, articleUnitId, activationDate, ageGroup, assortmentArea, brand, brandfamily, category, color, den, filling, fullText, gender, heelForm, heelHeight, length, occasion, pattern, price, sale, season, shaftHeight, shaftWidth, shirtCollar, shoeFastener, shoeToecap, shopArea, size, sports, technology, trouserRise, upperMaterial, volume, page, pageSize, sort, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#articlesGet");
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
| **articleId** | [**List&lt;String&gt;**](String.md)| The &#x60;articleIds&#x60; to use use for filtering.  One or more &#x60;articleIds&#x60; might be used as a filter criteria. Submit multiple &#x60;articleId&#x60; request parameters for more than one to be used. They will be treated as &#x60;OR&#x60; criteria. | [optional] |
| **articleModelId** | [**List&lt;String&gt;**](String.md)| filters by article ModelId | [optional] |
| **articleUnitId** | [**List&lt;String&gt;**](String.md)| filters by article&#39;s unit id | [optional] |
| **activationDate** | [**List&lt;String&gt;**](String.md)| period or time the articles are activated for selling in the shop | [optional] [enum: thisWeek, lastWeek, lastMonth] |
| **ageGroup** | [**List&lt;String&gt;**](String.md)| filters by age group (eg: kids) | [optional] [enum: babies, kids, teen, adult] |
| **assortmentArea** | [**List&lt;String&gt;**](String.md)| filters by classification of articles (eg: maternity)  | [optional] [enum: standard, maternity, plusSize, petite] |
| **brand** | [**List&lt;String&gt;**](String.md)| filters by brand key given by user (eg: SA5) | [optional] |
| **brandfamily** | [**List&lt;String&gt;**](String.md)| filters by brand family key (eg: nike)  | [optional] |
| **category** | [**List&lt;String&gt;**](String.md)| filters by category (eg: Socks, Rain Coats) | [optional] |
| **color** | [**List&lt;String&gt;**](String.md)| filters by color (eg: red, blue) | [optional] [enum: black, brown, beige, gray, white, blue, petrol, turquoise, green, olive, yellow, orange, red, pink, purple, gold, silver, multicolored] |
| **den** | [**List&lt;String&gt;**](String.md)| filters by den  | [optional] [enum: den15, den20, den40, den60, den80, den100, den200, den120, den12, den50] |
| **filling** | [**List&lt;String&gt;**](String.md)| filters by different kinds of garment filling materials (eg: satin, wolle) | [optional] [enum: angora, baumwolle, daunen, fell, fleece, frottee, kaschmir, lammfell, leder, lederimitat, merinowolle, microfaser, mohair, satin, schurwolle, seide, sonstige, textil, warm, wolle] |
| **fullText** | **String**| filters by text (eg: search by &#39;as&#39; gives result with articles of brand Sass) | [optional] |
| **gender** | [**List&lt;String&gt;**](String.md)| filters by gender | [optional] [enum: male, female] |
| **heelForm** | [**List&lt;String&gt;**](String.md)| filters by heel form (eg: flat) | [optional] [enum: block, flat, wedge, penny, funnel, plateau, plateauBoots, wedgeHidden, plateauHidden, plateauHeels] |
| **heelHeight** | [**List&lt;String&gt;**](String.md)| filters by height of the heel size or length (eg: xs) | [optional] [enum: xs, s, m] |
| **length** | **String**| filters by garments length (eg: 3/4 length, knee-length) | [optional] |
| **occasion** | [**List&lt;String&gt;**](String.md)| filters by type of occasion (eg: party, business) | [optional] [enum: business, octoberFest, loungeWear, evening, party, leisure] |
| **pattern** | [**List&lt;String&gt;**](String.md)| filters by pattern on the garments (eg: animal print, plain) | [optional] [enum: animalPrint, checkered, colored, floral, polkaDot, striped, paisley, plain, print, burnout, herringBone, camouflage, flecked, pinstripe, gradient, photoPrint] |
| **price** | **String**| filters all articles in price range (eg: 9-90) | [optional] |
| **sale** | [**List&lt;String&gt;**](String.md)| filters discounted articles marked as sale | [optional] [enum: sale] |
| **season** | [**List&lt;String&gt;**](String.md)| filters by season (Autumn/Winter or Spring/Summer) | [optional] [enum: winter, summer] |
| **shaftHeight** | [**List&lt;String&gt;**](String.md)| filters by shaft height (eg: s, xs) | [optional] [enum: xs, s, m, l] |
| **shaftWidth** | [**List&lt;String&gt;**](String.md)| filters by shaft width (eg: s, l) | [optional] [enum: s, m, l] |
| **shirtCollar** | [**List&lt;String&gt;**](String.md)| filters by shirt collar styles (eg: low V neck, lined collar) | [optional] [enum: lapelCollar, mandarinCollar, hood, poloNeck, poloShirt, cowlNeck, roundNeck, scarfCollar, boatNeck, vNeck, buttonDown, turnDownCollar, highCollar, linedCollar, shirtCollar, cutawayCollar, doubleCollar, peterPanCollar, kentCollar, cupShapedCollar, contrastCollar, maoCollar, wingCollar, tabCollar, volantCollar, shawlCollar, envelope, lowVNeck, cacheCeour, lowRoundNeck, backless, henley, squareNeck, offTheShoulder] |
| **shoeFastener** | [**List&lt;String&gt;**](String.md)| filters by shoe fastener types (eg: buckle, lacing) | [optional] [enum: buckle, belt, lacing, open, zipper, velcro] |
| **shoeToecap** | [**List&lt;String&gt;**](String.md)| filters by shoe toe cap variants (eg: pointed, square) | [optional] [enum: round, pointed, open, square] |
| **shopArea** | [**List&lt;String&gt;**](String.md)| filters by classification of articles | [optional] [enum: shop, sale] |
| **size** | **String**| filters by size | [optional] |
| **sports** | [**List&lt;String&gt;**](String.md)| filters by different sport activities (eg: football) | [optional] [enum: outdoor, skiSnow, running, training, football, handball, basketball, volleyball, golf, tennis, beach, skate, riding, cycling, sailing, badminton, dancing, snowboard, swimming] |
| **technology** | [**List&lt;String&gt;**](String.md)| filters by technology used to produce the articles | [optional] [enum: clima365, climacool, climalite, climaproof, climawarm, driFit, flywire, formotion, omniHeat, polartec, primaloft, staywarm, techfit, thinsulate, venturi, h2no, dermizax, performanceShell, softShell, windstopper, proShell, hydratic, pacliteShell, activeShell, goreTex, hyvent, texapore, precip] |
| **trouserRise** | [**List&lt;String&gt;**](String.md)| filters by trouser rise | [optional] [enum: high, medium, low] |
| **upperMaterial** | [**List&lt;String&gt;**](String.md)| filters by different type of upper material used on garments (eg: lace) | [optional] [enum: batiste, caoutchouc, cashmere, damask, down, feathers, felt, flanelette, flannel, fleece, imitationLeather, jacquard, jersey, leather, linen, linon, mesh, microfiber, mohair, other, percale, polyester, renforce, satin, seersucker, silk, synthetic, textile, towelling, varnish, velours, viscose, wool, cord, denim, rib, braided, crocheted, hardshell, softshell, lace, sweat] |
| **volume** | [**List&lt;String&gt;**](String.md)| filters by volume | [optional] [enum: smallest, small, medium, large, largest] |
| **page** | **String**| to request with required page number or pagination | [optional] |
| **pageSize** | **String**| to request with required page size in a page | [optional] |
| **sort** | **String**| sorting order (eg: popularity) | [optional] [enum: popularity, activationdate, pricedesc, priceasc, sale] |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**Articles**](Articles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Articles response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |

