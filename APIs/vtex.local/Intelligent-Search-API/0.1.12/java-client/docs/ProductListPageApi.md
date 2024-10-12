# ProductListPageApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bannersFacetsGet**](ProductListPageApi.md#bannersFacetsGet) | **GET** /banners/{facets} | Get list of banners registered for query |
| [**correctionSearchGet**](ProductListPageApi.md#correctionSearchGet) | **GET** /correction_search | Get attempt of correction of a misspelled term |
| [**facetsFacetsGet**](ProductListPageApi.md#facetsFacetsGet) | **GET** /facets/{facets} | Get list of the possible facets for a given query |
| [**productSearchFacetsGet**](ProductListPageApi.md#productSearchFacetsGet) | **GET** /product_search/{facets} | Get list of products for a query |
| [**searchSuggestionsGet**](ProductListPageApi.md#searchSuggestionsGet) | **GET** /search_suggestions | Get list of suggested terms similar to the search term |


<a id="bannersFacetsGet"></a>
# **bannersFacetsGet**
> Banners bannersFacetsGet(facets, query, locale)

Get list of banners registered for query

Lists the banners registered for a given query. Check the [configuring banners documentation](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4ViKEivLJtJsvpaW0aqIQ5) for a full explanation of the banner feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductListPageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ProductListPageApi apiInstance = new ProductListPageApi(defaultClient);
    String facets = "/"; // String | # Format  The `facets` parameter follows the format : `/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}`.  The order in which the terms appear is not relevant to the search.  You can also repeat the same `facetKey` several times for different values. For example: `category-1/shoes/color/blue/color/red/color/yellow`  # General filters  The `facets` parameter also allows the following general filters.  | `facetKey`      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | `price`         | Filter the search by a price range. The facet value follows the format `${minPrice}:${maxPrice}` | `/color/blue/price/100:500?query=shirt`                                  | | `category-${n}` | Filter the search by category, where `n` represents the category tree level (1 = department, 2 = category, 3 = subcategory, and so on) | `category-1/clothing/category-2/shirts`                                  | | `region-id`     | Filter the search by a region id (aka regionalization). The value is the region id               | `/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query=shirt`. | 
    String query = "query_example"; // String | Search term. It can contain any character.
    String locale = "en-US"; // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    try {
      Banners result = apiInstance.bannersFacetsGet(facets, query, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductListPageApi#bannersFacetsGet");
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
| **facets** | **String**| # Format  The &#x60;facets&#x60; parameter follows the format : &#x60;/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}&#x60;.  The order in which the terms appear is not relevant to the search.  You can also repeat the same &#x60;facetKey&#x60; several times for different values. For example: &#x60;category-1/shoes/color/blue/color/red/color/yellow&#x60;  # General filters  The &#x60;facets&#x60; parameter also allows the following general filters.  | &#x60;facetKey&#x60;      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | &#x60;price&#x60;         | Filter the search by a price range. The facet value follows the format &#x60;${minPrice}:${maxPrice}&#x60; | &#x60;/color/blue/price/100:500?query&#x3D;shirt&#x60;                                  | | &#x60;category-${n}&#x60; | Filter the search by category, where &#x60;n&#x60; represents the category tree level (1 &#x3D; department, 2 &#x3D; category, 3 &#x3D; subcategory, and so on) | &#x60;category-1/clothing/category-2/shirts&#x60;                                  | | &#x60;region-id&#x60;     | Filter the search by a region id (aka regionalization). The value is the region id               | &#x60;/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query&#x3D;shirt&#x60;. |  | [default to /] |
| **query** | **String**| Search term. It can contain any character. | [optional] |
| **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] |

### Return type

[**Banners**](Banners.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="correctionSearchGet"></a>
# **correctionSearchGet**
> Correction correctionSearchGet(query, locale)

Get attempt of correction of a misspelled term

Tries to correct a misspelled term from the search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductListPageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ProductListPageApi apiInstance = new ProductListPageApi(defaultClient);
    String query = "query_example"; // String | Search term. It can contain any character.
    String locale = "en-US"; // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    try {
      Correction result = apiInstance.correctionSearchGet(query, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductListPageApi#correctionSearchGet");
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
| **query** | **String**| Search term. It can contain any character. | [optional] |
| **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] |

### Return type

[**Correction**](Correction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="facetsFacetsGet"></a>
# **facetsFacetsGet**
> Facets facetsFacetsGet(facets, query, locale, hideUnavailableItems)

Get list of the possible facets for a given query

Lists the possible facets for a given query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductListPageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ProductListPageApi apiInstance = new ProductListPageApi(defaultClient);
    String facets = "/"; // String | # Format  The `facets` parameter follows the format : `/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}`.  The order in which the terms appear is not relevant to the search.  You can also repeat the same `facetKey` several times for different values. For example: `category-1/shoes/color/blue/color/red/color/yellow`  # General filters  The `facets` parameter also allows the following general filters.  | `facetKey`      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | `price`         | Filter the search by a price range. The facet value follows the format `${minPrice}:${maxPrice}` | `/color/blue/price/100:500?query=shirt`                                  | | `category-${n}` | Filter the search by category, where `n` represents the category tree level (1 = department, 2 = category, 3 = subcategory, and so on) | `category-1/clothing/category-2/shirts`                                  | | `region-id`     | Filter the search by a region id (aka regionalization). The value is the region id               | `/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query=shirt`. | 
    String query = "query_example"; // String | Search term. It can contain any character.
    String locale = "en-US"; // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    Boolean hideUnavailableItems = false; // Boolean | Whether the result should hide unavailable items (`true`), or not (`false`)
    try {
      Facets result = apiInstance.facetsFacetsGet(facets, query, locale, hideUnavailableItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductListPageApi#facetsFacetsGet");
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
| **facets** | **String**| # Format  The &#x60;facets&#x60; parameter follows the format : &#x60;/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}&#x60;.  The order in which the terms appear is not relevant to the search.  You can also repeat the same &#x60;facetKey&#x60; several times for different values. For example: &#x60;category-1/shoes/color/blue/color/red/color/yellow&#x60;  # General filters  The &#x60;facets&#x60; parameter also allows the following general filters.  | &#x60;facetKey&#x60;      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | &#x60;price&#x60;         | Filter the search by a price range. The facet value follows the format &#x60;${minPrice}:${maxPrice}&#x60; | &#x60;/color/blue/price/100:500?query&#x3D;shirt&#x60;                                  | | &#x60;category-${n}&#x60; | Filter the search by category, where &#x60;n&#x60; represents the category tree level (1 &#x3D; department, 2 &#x3D; category, 3 &#x3D; subcategory, and so on) | &#x60;category-1/clothing/category-2/shirts&#x60;                                  | | &#x60;region-id&#x60;     | Filter the search by a region id (aka regionalization). The value is the region id               | &#x60;/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query&#x3D;shirt&#x60;. |  | [default to /] |
| **query** | **String**| Search term. It can contain any character. | [optional] |
| **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] |
| **hideUnavailableItems** | **Boolean**| Whether the result should hide unavailable items (&#x60;true&#x60;), or not (&#x60;false&#x60;) | [optional] [default to false] |

### Return type

[**Facets**](Facets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of facets for the given query. |  -  |

<a id="productSearchFacetsGet"></a>
# **productSearchFacetsGet**
> ProductSearch productSearchFacetsGet(facets, query, simulationBehavior, count, page, sort, locale, hideUnavailableItems)

Get list of products for a query

Lists the products for a given query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductListPageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ProductListPageApi apiInstance = new ProductListPageApi(defaultClient);
    String facets = "/"; // String | # Format  The `facets` parameter follows the format : `/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}`.  The order in which the terms appear is not relevant to the search.  You can also repeat the same `facetKey` several times for different values. For example: `category-1/shoes/color/blue/color/red/color/yellow`  # General filters  The `facets` parameter also allows the following general filters.  | `facetKey`      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | `price`         | Filter the search by a price range. The facet value follows the format `${minPrice}:${maxPrice}` | `/color/blue/price/100:500?query=shirt`                                  | | `category-${n}` | Filter the search by category, where `n` represents the category tree level (1 = department, 2 = category, 3 = subcategory, and so on) | `category-1/clothing/category-2/shirts`                                  | | `region-id`     | Filter the search by a region id (aka regionalization). The value is the region id               | `/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query=shirt`. | 
    String query = "query_example"; // String | Search term. It can contain any character.
    String simulationBehavior = "default"; // String | Defines the simulation behavior.   * `default` - Calls the simulation for every single seller.  * `skip` - Never calls the simulation.  * `only1P` - Only calls the simulation for first party sellers.
    BigDecimal count = new BigDecimal("24"); // BigDecimal | Number of products per page.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | Current search page.
    String sort = "price:desc"; // String | Defines the sort type. If null, the products will be sorted by relevance.
    String locale = "en-US"; // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    Boolean hideUnavailableItems = false; // Boolean | Whether the result should hide unavailable items (`true`), or not (`false`)
    try {
      ProductSearch result = apiInstance.productSearchFacetsGet(facets, query, simulationBehavior, count, page, sort, locale, hideUnavailableItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductListPageApi#productSearchFacetsGet");
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
| **facets** | **String**| # Format  The &#x60;facets&#x60; parameter follows the format : &#x60;/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}&#x60;.  The order in which the terms appear is not relevant to the search.  You can also repeat the same &#x60;facetKey&#x60; several times for different values. For example: &#x60;category-1/shoes/color/blue/color/red/color/yellow&#x60;  # General filters  The &#x60;facets&#x60; parameter also allows the following general filters.  | &#x60;facetKey&#x60;      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | &#x60;price&#x60;         | Filter the search by a price range. The facet value follows the format &#x60;${minPrice}:${maxPrice}&#x60; | &#x60;/color/blue/price/100:500?query&#x3D;shirt&#x60;                                  | | &#x60;category-${n}&#x60; | Filter the search by category, where &#x60;n&#x60; represents the category tree level (1 &#x3D; department, 2 &#x3D; category, 3 &#x3D; subcategory, and so on) | &#x60;category-1/clothing/category-2/shirts&#x60;                                  | | &#x60;region-id&#x60;     | Filter the search by a region id (aka regionalization). The value is the region id               | &#x60;/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query&#x3D;shirt&#x60;. |  | [default to /] |
| **query** | **String**| Search term. It can contain any character. | [optional] |
| **simulationBehavior** | **String**| Defines the simulation behavior.   * &#x60;default&#x60; - Calls the simulation for every single seller.  * &#x60;skip&#x60; - Never calls the simulation.  * &#x60;only1P&#x60; - Only calls the simulation for first party sellers. | [optional] [default to default] [enum: default, skip, only1P] |
| **count** | **BigDecimal**| Number of products per page. | [optional] [default to 24] |
| **page** | **BigDecimal**| Current search page. | [optional] [default to 1] |
| **sort** | **String**| Defines the sort type. If null, the products will be sorted by relevance. | [optional] [enum: price:desc, price:asc, orders:desc, name:desc, name:asc, release:desc, discount:desc] |
| **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] |
| **hideUnavailableItems** | **Boolean**| Whether the result should hide unavailable items (&#x60;true&#x60;), or not (&#x60;false&#x60;) | [optional] [default to false] |

### Return type

[**ProductSearch**](ProductSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of products for the given query. |  -  |

<a id="searchSuggestionsGet"></a>
# **searchSuggestionsGet**
> SearchSuggestions searchSuggestionsGet(query, locale)

Get list of suggested terms similar to the search term

Lists suggested terms similar to the search term.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductListPageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    ProductListPageApi apiInstance = new ProductListPageApi(defaultClient);
    String query = "query_example"; // String | Search term. It can contain any character.
    String locale = "en-US"; // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    try {
      SearchSuggestions result = apiInstance.searchSuggestionsGet(query, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductListPageApi#searchSuggestionsGet");
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
| **query** | **String**| Search term. It can contain any character. | [optional] |
| **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] |

### Return type

[**SearchSuggestions**](SearchSuggestions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **5XX** | Server error. |  -  |

