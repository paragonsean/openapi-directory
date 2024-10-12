# BrandsApi

All URIs are relative to *https://api.zalando.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**brandsGet**](BrandsApi.md#brandsGet) | **GET** /brands | Shop Brands |
| [**brandsKeyGet**](BrandsApi.md#brandsKeyGet) | **GET** /brands/{key} | Get Single Brand by Key |


<a id="brandsGet"></a>
# **brandsGet**
> Brands brandsGet(key, name, brandFamilyName, brandFamilyKey, page, pageSize, acceptLanguage, fields)

Shop Brands

Zalando API Brands Schema

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zalando.com");

    BrandsApi apiInstance = new BrandsApi(defaultClient);
    List<String> key = Arrays.asList(); // List<String> | Request Brand by key
    List<String> name = Arrays.asList(); // List<String> | Request Brand by name
    List<String> brandFamilyName = Arrays.asList(); // List<String> | Request Brand by brandFamilyName
    List<String> brandFamilyKey = Arrays.asList(); // List<String> | Request Brand by brandFamilyKey
    String page = "page_example"; // String | to request with required page number or pagination
    String pageSize = "pageSize_example"; // String | to request with required page size in a page
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      Brands result = apiInstance.brandsGet(key, name, brandFamilyName, brandFamilyKey, page, pageSize, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandsApi#brandsGet");
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
| **key** | [**List&lt;String&gt;**](String.md)| Request Brand by key | [optional] |
| **name** | [**List&lt;String&gt;**](String.md)| Request Brand by name | [optional] |
| **brandFamilyName** | [**List&lt;String&gt;**](String.md)| Request Brand by brandFamilyName | [optional] |
| **brandFamilyKey** | [**List&lt;String&gt;**](String.md)| Request Brand by brandFamilyKey | [optional] |
| **page** | **String**| to request with required page number or pagination | [optional] |
| **pageSize** | **String**| to request with required page size in a page | [optional] |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**Brands**](Brands.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Brands response. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |

<a id="brandsKeyGet"></a>
# **brandsKeyGet**
> Brand brandsKeyGet(key, acceptLanguage, fields)

Get Single Brand by Key

Zalando API Brand Schema

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zalando.com");

    BrandsApi apiInstance = new BrandsApi(defaultClient);
    String key = "key_example"; // String | To get unique Brand by key.
    String acceptLanguage = "da-DK"; // String | Specify which Shop to use.  A standard `Accept-Language` header which specifies the shop that should be used. E.g. `de-DE` will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and `de-AT` will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    List<String> fields = Arrays.asList(); // List<String> | Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    try {
      Brand result = apiInstance.brandsKeyGet(key, acceptLanguage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandsApi#brandsKeyGet");
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
| **key** | **String**| To get unique Brand by key. | |
| **acceptLanguage** | **String**| Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries. | [optional] [enum: da-DK, de-AT, de-CH, de-DE, en-GB, es-ES, fi-FI, fr-BE, fr-CH, fr-FR, it-IT, nl-BE, nl-NL, no-NO, pl-PL, sv-SE] |
| **fields** | [**List&lt;String&gt;**](String.md)| Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted | [optional] |

### Return type

[**Brand**](Brand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Brand Key response. |  -  |
| **404** | Brand not found. |  -  |

