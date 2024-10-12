# ZalandoShop.ArticlesApi

All URIs are relative to *https://api.zalando.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**articleReviewsGet**](ArticlesApi.md#articleReviewsGet) | **GET** /article-reviews | Get Article Reviews
[**articleReviewsReviewIdGet**](ArticlesApi.md#articleReviewsReviewIdGet) | **GET** /article-reviews/{reviewId} | Get Article Reviews by reviewId
[**articleReviewsSummariesArticleModelIdGet**](ArticlesApi.md#articleReviewsSummariesArticleModelIdGet) | **GET** /article-reviews-summaries/{articleModelId} | Get Article Reviews Summaries by articleModelId
[**articleReviewsSummariesGet**](ArticlesApi.md#articleReviewsSummariesGet) | **GET** /article-reviews-summaries | Get Article Reviews Summaries
[**articlesArticleIdGet**](ArticlesApi.md#articlesArticleIdGet) | **GET** /articles/{articleId} | Get Article by articleId
[**articlesArticleIdMediaGet**](ArticlesApi.md#articlesArticleIdMediaGet) | **GET** /articles/{articleId}/media | Get Article media by articleId
[**articlesArticleIdReviewsGet**](ArticlesApi.md#articlesArticleIdReviewsGet) | **GET** /articles/{articleId}/reviews | Get Article reviews by articleId
[**articlesArticleIdReviewsSummaryGet**](ArticlesApi.md#articlesArticleIdReviewsSummaryGet) | **GET** /articles/{articleId}/reviews-summary | Get Article reviews summary by articleId
[**articlesArticleIdUnitsGet**](ArticlesApi.md#articlesArticleIdUnitsGet) | **GET** /articles/{articleId}/units | Get Article units by articleId
[**articlesArticleIdUnitsUnitIdGet**](ArticlesApi.md#articlesArticleIdUnitsUnitIdGet) | **GET** /articles/{articleId}/units/{unitId} | Get Article units by articleId snd unitId
[**articlesGet**](ArticlesApi.md#articlesGet) | **GET** /articles | Search for Articles



## articleReviewsGet

> ArticleReviews articleReviewsGet(opts)

Get Article Reviews

Zalando API Article Reviews Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let opts = {
  'articleId': ["null"], // [String] | Article IDs. A list of config SKUs for which the article reviews will be returned. Required if articleModelId is empty. 
  'articleModelId': ["null"], // [String] | Article model IDs. A list of model SKUs for which the article reviews will be returned. Required if articleId is empty. 
  'minStarRating': "minStarRating_example", // String | To get reviews with minimum star rating.
  'maxStarRating': "maxStarRating_example", // String | To get reviews with maximum star rating.
  'sort': "'newest'", // String | articles are sorted on reviews provided by customers (eg: best)
  'page': "page_example", // String | to request with required page number or pagination
  'pageSize': "pageSize_example", // String | to request with required page size in a page
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articleReviewsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleId** | [**[String]**](String.md)| Article IDs. A list of config SKUs for which the article reviews will be returned. Required if articleModelId is empty.  | [optional] 
 **articleModelId** | [**[String]**](String.md)| Article model IDs. A list of model SKUs for which the article reviews will be returned. Required if articleId is empty.  | [optional] 
 **minStarRating** | **String**| To get reviews with minimum star rating. | [optional] 
 **maxStarRating** | **String**| To get reviews with maximum star rating. | [optional] 
 **sort** | **String**| articles are sorted on reviews provided by customers (eg: best) | [optional] [default to &#39;newest&#39;]
 **page** | **String**| to request with required page number or pagination | [optional] 
 **pageSize** | **String**| to request with required page size in a page | [optional] 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**ArticleReviews**](ArticleReviews.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleReviewsReviewIdGet

> ArticleReview articleReviewsReviewIdGet(reviewId, opts)

Get Article Reviews by reviewId

Zalando API ArticleReviews Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let reviewId = "reviewId_example"; // String | To get unique review by review Id.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articleReviewsReviewIdGet(reviewId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reviewId** | **String**| To get unique review by review Id. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**ArticleReview**](ArticleReview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleReviewsSummariesArticleModelIdGet

> ArticleReviewsSummary articleReviewsSummariesArticleModelIdGet(articleModelId, opts)

Get Article Reviews Summaries by articleModelId

Zalando API ArticleReviewsSummaries Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let articleModelId = "articleModelId_example"; // String | To get unique reviews summary from article model Id.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articleReviewsSummariesArticleModelIdGet(articleModelId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleModelId** | **String**| To get unique reviews summary from article model Id. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**ArticleReviewsSummary**](ArticleReviewsSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleReviewsSummariesGet

> ArticleReviewsSummaries articleReviewsSummariesGet(articleModelId, opts)

Get Article Reviews Summaries

Zalando API Article Reviews Summaries Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let articleModelId = ["null"]; // [String] | Article model IDs. A list of model SKUs for which the article review summaries will be returned.
let opts = {
  'page': "page_example", // String | to request with required page number or pagination
  'pageSize': "pageSize_example", // String | to request with required page size in a page
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articleReviewsSummariesGet(articleModelId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleModelId** | [**[String]**](String.md)| Article model IDs. A list of model SKUs for which the article review summaries will be returned. | 
 **page** | **String**| to request with required page number or pagination | [optional] 
 **pageSize** | **String**| to request with required page size in a page | [optional] 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**ArticleReviewsSummaries**](ArticleReviewsSummaries.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlesArticleIdGet

> Article articlesArticleIdGet(articleId, opts)

Get Article by articleId

Zalando API Article Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let articleId = "articleId_example"; // String | To get unique article for article Id.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articlesArticleIdGet(articleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleId** | **String**| To get unique article for article Id. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**Article**](Article.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlesArticleIdMediaGet

> ArticleMedia articlesArticleIdMediaGet(articleId, opts)

Get Article media by articleId

Zalando API Article Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let articleId = "articleId_example"; // String | To get unique article for article Id media.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articlesArticleIdMediaGet(articleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleId** | **String**| To get unique article for article Id media. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**ArticleMedia**](ArticleMedia.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlesArticleIdReviewsGet

> ArticleReviews articlesArticleIdReviewsGet(articleId, opts)

Get Article reviews by articleId

Zalando API Article Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let articleId = "articleId_example"; // String | To get unique article for article Id reviews.
let opts = {
  'minStarRating': "minStarRating_example", // String | To get reviews with minimum star rating.
  'maxStarRating': "maxStarRating_example", // String | To get reviews with maximum star rating.
  'sort': "'newest'", // String | articles are sorted on reviews provided by customers (eg: best)
  'page': "page_example", // String | to request with required page number or pagination
  'pageSize': "pageSize_example", // String | to request with required page size in a page
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articlesArticleIdReviewsGet(articleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleId** | **String**| To get unique article for article Id reviews. | 
 **minStarRating** | **String**| To get reviews with minimum star rating. | [optional] 
 **maxStarRating** | **String**| To get reviews with maximum star rating. | [optional] 
 **sort** | **String**| articles are sorted on reviews provided by customers (eg: best) | [optional] [default to &#39;newest&#39;]
 **page** | **String**| to request with required page number or pagination | [optional] 
 **pageSize** | **String**| to request with required page size in a page | [optional] 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**ArticleReviews**](ArticleReviews.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlesArticleIdReviewsSummaryGet

> ArticleReviewsSummary articlesArticleIdReviewsSummaryGet(articleId, opts)

Get Article reviews summary by articleId

Zalando API Article Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let articleId = "articleId_example"; // String | To get unique article for article Id reviews summary.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articlesArticleIdReviewsSummaryGet(articleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleId** | **String**| To get unique article for article Id reviews summary. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**ArticleReviewsSummary**](ArticleReviewsSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlesArticleIdUnitsGet

> [ArticleUnit] articlesArticleIdUnitsGet(articleId, opts)

Get Article units by articleId

Zalando API Article Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let articleId = "articleId_example"; // String | To get unique article for article Id units.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articlesArticleIdUnitsGet(articleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleId** | **String**| To get unique article for article Id units. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**[ArticleUnit]**](ArticleUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlesArticleIdUnitsUnitIdGet

> ArticleUnit articlesArticleIdUnitsUnitIdGet(articleId, unitId, opts)

Get Article units by articleId snd unitId

Zalando API Article Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let articleId = "articleId_example"; // String | To get unique article for article Id.
let unitId = "unitId_example"; // String | To get unique article for article Id unit.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articlesArticleIdUnitsUnitIdGet(articleId, unitId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleId** | **String**| To get unique article for article Id. | 
 **unitId** | **String**| To get unique article for article Id unit. | 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**ArticleUnit**](ArticleUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlesGet

> Articles articlesGet(opts)

Search for Articles

Search for articles based on various different possible filter like e.g. the &#x60;brandFamily&#x60;, the &#x60;catagory&#x60; or a specific &#x60;color&#x60;. See [Filters](https://todo) for a list of all available filter options.  The default &#x60;pageSize&#x60; for responses is set to &#x60;20&#x60;. You can add a &#x60;pageSize&#x60; request parameter to adjust that. Please keep in mind that the maximum &#x60;pageSize&#x60; for this resource is &#x60;200&#x60;.  The endpoint also supports reducing the fields returned for each article via the &#x60;fields&#x60; parameter. Please refer to [fields parameter](https://todo) for more details.

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.ArticlesApi();
let opts = {
  'articleId': ["null"], // [String] | The `articleIds` to use use for filtering.  One or more `articleIds` might be used as a filter criteria. Submit multiple `articleId` request parameters for more than one to be used. They will be treated as `OR` criteria.
  'articleModelId': ["null"], // [String] | filters by article ModelId
  'articleUnitId': ["null"], // [String] | filters by article's unit id
  'activationDate': ["null"], // [String] | period or time the articles are activated for selling in the shop
  'ageGroup': ["null"], // [String] | filters by age group (eg: kids)
  'assortmentArea': ["null"], // [String] | filters by classification of articles (eg: maternity) 
  'brand': ["null"], // [String] | filters by brand key given by user (eg: SA5)
  'brandfamily': ["null"], // [String] | filters by brand family key (eg: nike) 
  'category': ["null"], // [String] | filters by category (eg: Socks, Rain Coats)
  'color': ["null"], // [String] | filters by color (eg: red, blue)
  'den': ["null"], // [String] | filters by den 
  'filling': ["null"], // [String] | filters by different kinds of garment filling materials (eg: satin, wolle)
  'fullText': "fullText_example", // String | filters by text (eg: search by 'as' gives result with articles of brand Sass)
  'gender': ["null"], // [String] | filters by gender
  'heelForm': ["null"], // [String] | filters by heel form (eg: flat)
  'heelHeight': ["null"], // [String] | filters by height of the heel size or length (eg: xs)
  'length': "length_example", // String | filters by garments length (eg: 3/4 length, knee-length)
  'occasion': ["null"], // [String] | filters by type of occasion (eg: party, business)
  'pattern': ["null"], // [String] | filters by pattern on the garments (eg: animal print, plain)
  'price': "price_example", // String | filters all articles in price range (eg: 9-90)
  'sale': ["null"], // [String] | filters discounted articles marked as sale
  'season': ["null"], // [String] | filters by season (Autumn/Winter or Spring/Summer)
  'shaftHeight': ["null"], // [String] | filters by shaft height (eg: s, xs)
  'shaftWidth': ["null"], // [String] | filters by shaft width (eg: s, l)
  'shirtCollar': ["null"], // [String] | filters by shirt collar styles (eg: low V neck, lined collar)
  'shoeFastener': ["null"], // [String] | filters by shoe fastener types (eg: buckle, lacing)
  'shoeToecap': ["null"], // [String] | filters by shoe toe cap variants (eg: pointed, square)
  'shopArea': ["null"], // [String] | filters by classification of articles
  'size': "size_example", // String | filters by size
  'sports': ["null"], // [String] | filters by different sport activities (eg: football)
  'technology': ["null"], // [String] | filters by technology used to produce the articles
  'trouserRise': ["null"], // [String] | filters by trouser rise
  'upperMaterial': ["null"], // [String] | filters by different type of upper material used on garments (eg: lace)
  'volume': ["null"], // [String] | filters by volume
  'page': "page_example", // String | to request with required page number or pagination
  'pageSize': "pageSize_example", // String | to request with required page size in a page
  'sort': "sort_example", // String | sorting order (eg: popularity)
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.articlesGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **articleId** | [**[String]**](String.md)| The &#x60;articleIds&#x60; to use use for filtering.  One or more &#x60;articleIds&#x60; might be used as a filter criteria. Submit multiple &#x60;articleId&#x60; request parameters for more than one to be used. They will be treated as &#x60;OR&#x60; criteria. | [optional] 
 **articleModelId** | [**[String]**](String.md)| filters by article ModelId | [optional] 
 **articleUnitId** | [**[String]**](String.md)| filters by article&#39;s unit id | [optional] 
 **activationDate** | [**[String]**](String.md)| period or time the articles are activated for selling in the shop | [optional] 
 **ageGroup** | [**[String]**](String.md)| filters by age group (eg: kids) | [optional] 
 **assortmentArea** | [**[String]**](String.md)| filters by classification of articles (eg: maternity)  | [optional] 
 **brand** | [**[String]**](String.md)| filters by brand key given by user (eg: SA5) | [optional] 
 **brandfamily** | [**[String]**](String.md)| filters by brand family key (eg: nike)  | [optional] 
 **category** | [**[String]**](String.md)| filters by category (eg: Socks, Rain Coats) | [optional] 
 **color** | [**[String]**](String.md)| filters by color (eg: red, blue) | [optional] 
 **den** | [**[String]**](String.md)| filters by den  | [optional] 
 **filling** | [**[String]**](String.md)| filters by different kinds of garment filling materials (eg: satin, wolle) | [optional] 
 **fullText** | **String**| filters by text (eg: search by &#39;as&#39; gives result with articles of brand Sass) | [optional] 
 **gender** | [**[String]**](String.md)| filters by gender | [optional] 
 **heelForm** | [**[String]**](String.md)| filters by heel form (eg: flat) | [optional] 
 **heelHeight** | [**[String]**](String.md)| filters by height of the heel size or length (eg: xs) | [optional] 
 **length** | **String**| filters by garments length (eg: 3/4 length, knee-length) | [optional] 
 **occasion** | [**[String]**](String.md)| filters by type of occasion (eg: party, business) | [optional] 
 **pattern** | [**[String]**](String.md)| filters by pattern on the garments (eg: animal print, plain) | [optional] 
 **price** | **String**| filters all articles in price range (eg: 9-90) | [optional] 
 **sale** | [**[String]**](String.md)| filters discounted articles marked as sale | [optional] 
 **season** | [**[String]**](String.md)| filters by season (Autumn/Winter or Spring/Summer) | [optional] 
 **shaftHeight** | [**[String]**](String.md)| filters by shaft height (eg: s, xs) | [optional] 
 **shaftWidth** | [**[String]**](String.md)| filters by shaft width (eg: s, l) | [optional] 
 **shirtCollar** | [**[String]**](String.md)| filters by shirt collar styles (eg: low V neck, lined collar) | [optional] 
 **shoeFastener** | [**[String]**](String.md)| filters by shoe fastener types (eg: buckle, lacing) | [optional] 
 **shoeToecap** | [**[String]**](String.md)| filters by shoe toe cap variants (eg: pointed, square) | [optional] 
 **shopArea** | [**[String]**](String.md)| filters by classification of articles | [optional] 
 **size** | **String**| filters by size | [optional] 
 **sports** | [**[String]**](String.md)| filters by different sport activities (eg: football) | [optional] 
 **technology** | [**[String]**](String.md)| filters by technology used to produce the articles | [optional] 
 **trouserRise** | [**[String]**](String.md)| filters by trouser rise | [optional] 
 **upperMaterial** | [**[String]**](String.md)| filters by different type of upper material used on garments (eg: lace) | [optional] 
 **volume** | [**[String]**](String.md)| filters by volume | [optional] 
 **page** | **String**| to request with required page number or pagination | [optional] 
 **pageSize** | **String**| to request with required page size in a page | [optional] 
 **sort** | **String**| sorting order (eg: popularity) | [optional] 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**Articles**](Articles.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

