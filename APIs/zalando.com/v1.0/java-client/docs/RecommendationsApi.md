# RecommendationsApi

All URIs are relative to *https://api.zalando.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recommendationsArticleIdsGet**](RecommendationsApi.md#recommendationsArticleIdsGet) | **GET** /recommendations/{articleIds} | Get Recommendations by articleId |


<a id="recommendationsArticleIdsGet"></a>
# **recommendationsArticleIdsGet**
> List&lt;RecommendationsArticle&gt; recommendationsArticleIdsGet(articleIds, maxResults, acceptLanguage, fields)

Get Recommendations by articleId

Zalando API Recommendations Schema

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zalando.com");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    List<String> articleIds = Arrays.asList(); // List<String> | To get Recommendations by articleIds.
    String maxResults = "maxResults_example"; // String | To get maximum results of Recommendations by articleId.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      List<RecommendationsArticle> result = apiInstance.recommendationsArticleIdsGet(articleIds, maxResults, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsArticleIdsGet");
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
| **articleIds** | [**List&lt;String&gt;**](String.md)| To get Recommendations by articleIds. | |
| **maxResults** | **String**| To get maximum results of Recommendations by articleId. | [optional] |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**List&lt;RecommendationsArticle&gt;**](RecommendationsArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recommendations response. |  -  |
| **400** | Bad Request. |  -  |

