# ZalandoShop.RecommendationsApi

All URIs are relative to *https://api.zalando.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendationsArticleIdsGet**](RecommendationsApi.md#recommendationsArticleIdsGet) | **GET** /recommendations/{articleIds} | Get Recommendations by articleId



## recommendationsArticleIdsGet

> [RecommendationsArticle] recommendationsArticleIdsGet(articleIds, opts)

Get Recommendations by articleId

Zalando API Recommendations Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.RecommendationsApi();
let articleIds = ["null"]; // [String] | To get Recommendations by articleIds.
let opts = {
  'maxResults': "maxResults_example", // String | To get maximum results of Recommendations by articleId.
  'acceptLanguage': "acceptLanguage_example", // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
  'fields': ["null"] // [String] | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
};
apiInstance.recommendationsArticleIdsGet(articleIds, opts, (error, data, response) => {
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
 **articleIds** | [**[String]**](String.md)| To get Recommendations by articleIds. | 
 **maxResults** | **String**| To get maximum results of Recommendations by articleId. | [optional] 
 **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] 
 **fields** | [**[String]**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] 

### Return type

[**[RecommendationsArticle]**](RecommendationsArticle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

