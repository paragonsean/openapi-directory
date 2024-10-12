# CategoriesApi

All URIs are relative to *https://api.zalando.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesGet**](CategoriesApi.md#categoriesGet) | **GET** /categories | Shop Categories |
| [**categoriesKeyGet**](CategoriesApi.md#categoriesKeyGet) | **GET** /categories/{key} | Get Single Category by Key |


<a id="categoriesGet"></a>
# **categoriesGet**
> Categories categoriesGet(name, type, outlet, hidden, targetGroup, key, parentKey, childKey, suggestedFilter, page, pageSize, acceptLanguage, fields)

Shop Categories

Zalando API Categories Schema

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zalando.com");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    List<String> name = Arrays.asList(); // List<String> | Request Categories by names
    String type = "type_example"; // String | Request Categories by type
    String outlet = "outlet_example"; // String | Request Categories by outlet
    String hidden = "hidden_example"; // String | Request Categories by hidden
    String targetGroup = "targetGroup_example"; // String | Request Categories by target group
    List<String> key = Arrays.asList(); // List<String> | Request Categories by keys
    List<String> parentKey = Arrays.asList(); // List<String> | Request Categories by parent keys
    List<String> childKey = Arrays.asList(); // List<String> | Request Categories by child keys
    List<String> suggestedFilter = Arrays.asList(); // List<String> | Request Categories by suggested filters
    String page = "page_example"; // String | to request with required page number or pagination
    String pageSize = "pageSize_example"; // String | to request with required page size in a page
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      Categories result = apiInstance.categoriesGet(name, type, outlet, hidden, targetGroup, key, parentKey, childKey, suggestedFilter, page, pageSize, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesGet");
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
| **name** | [**List&lt;String&gt;**](String.md)| Request Categories by names | [optional] |
| **type** | **String**| Request Categories by type | [optional] |
| **outlet** | **String**| Request Categories by outlet | [optional] |
| **hidden** | **String**| Request Categories by hidden | [optional] |
| **targetGroup** | **String**| Request Categories by target group | [optional] |
| **key** | [**List&lt;String&gt;**](String.md)| Request Categories by keys | [optional] |
| **parentKey** | [**List&lt;String&gt;**](String.md)| Request Categories by parent keys | [optional] |
| **childKey** | [**List&lt;String&gt;**](String.md)| Request Categories by child keys | [optional] |
| **suggestedFilter** | [**List&lt;String&gt;**](String.md)| Request Categories by suggested filters | [optional] |
| **page** | **String**| to request with required page number or pagination | [optional] |
| **pageSize** | **String**| to request with required page size in a page | [optional] |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**Categories**](Categories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Categories response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Categories Not found. |  -  |

<a id="categoriesKeyGet"></a>
# **categoriesKeyGet**
> Category categoriesKeyGet(key, acceptLanguage, fields)

Get Single Category by Key

Zalando API Category Schema

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zalando.com");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    List<String> key = Arrays.asList(); // List<String> | To get unique Category by key.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      Category result = apiInstance.categoriesKeyGet(key, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesKeyGet");
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
| **key** | [**List&lt;String&gt;**](String.md)| To get unique Category by key. | |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Category Key response. |  -  |
| **404** | Category not found. |  -  |

