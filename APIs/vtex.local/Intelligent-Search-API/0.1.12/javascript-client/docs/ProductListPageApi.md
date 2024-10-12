# IntelligentSearchApi.ProductListPageApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bannersFacetsGet**](ProductListPageApi.md#bannersFacetsGet) | **GET** /banners/{facets} | Get list of banners registered for query
[**correctionSearchGet**](ProductListPageApi.md#correctionSearchGet) | **GET** /correction_search | Get attempt of correction of a misspelled term
[**facetsFacetsGet**](ProductListPageApi.md#facetsFacetsGet) | **GET** /facets/{facets} | Get list of the possible facets for a given query
[**productSearchFacetsGet**](ProductListPageApi.md#productSearchFacetsGet) | **GET** /product_search/{facets} | Get list of products for a query
[**searchSuggestionsGet**](ProductListPageApi.md#searchSuggestionsGet) | **GET** /search_suggestions | Get list of suggested terms similar to the search term



## bannersFacetsGet

> Banners bannersFacetsGet(facets, opts)

Get list of banners registered for query

Lists the banners registered for a given query. Check the [configuring banners documentation](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4ViKEivLJtJsvpaW0aqIQ5) for a full explanation of the banner feature.

### Example

```javascript
import IntelligentSearchApi from 'intelligent_search_api';

let apiInstance = new IntelligentSearchApi.ProductListPageApi();
let facets = "category-1/clothing/category-2/shirt/category-3/man"; // String | # Format  The `facets` parameter follows the format : `/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}`.  The order in which the terms appear is not relevant to the search.  You can also repeat the same `facetKey` several times for different values. For example: `category-1/shoes/color/blue/color/red/color/yellow`  # General filters  The `facets` parameter also allows the following general filters.  | `facetKey`      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | `price`         | Filter the search by a price range. The facet value follows the format `${minPrice}:${maxPrice}` | `/color/blue/price/100:500?query=shirt`                                  | | `category-${n}` | Filter the search by category, where `n` represents the category tree level (1 = department, 2 = category, 3 = subcategory, and so on) | `category-1/clothing/category-2/shirts`                                  | | `region-id`     | Filter the search by a region id (aka regionalization). The value is the region id               | `/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query=shirt`. | 
let opts = {
  'query': "query_example", // String | Search term. It can contain any character.
  'locale': "en-US" // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
};
apiInstance.bannersFacetsGet(facets, opts, (error, data, response) => {
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
 **facets** | **String**| # Format  The &#x60;facets&#x60; parameter follows the format : &#x60;/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}&#x60;.  The order in which the terms appear is not relevant to the search.  You can also repeat the same &#x60;facetKey&#x60; several times for different values. For example: &#x60;category-1/shoes/color/blue/color/red/color/yellow&#x60;  # General filters  The &#x60;facets&#x60; parameter also allows the following general filters.  | &#x60;facetKey&#x60;      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | &#x60;price&#x60;         | Filter the search by a price range. The facet value follows the format &#x60;${minPrice}:${maxPrice}&#x60; | &#x60;/color/blue/price/100:500?query&#x3D;shirt&#x60;                                  | | &#x60;category-${n}&#x60; | Filter the search by category, where &#x60;n&#x60; represents the category tree level (1 &#x3D; department, 2 &#x3D; category, 3 &#x3D; subcategory, and so on) | &#x60;category-1/clothing/category-2/shirts&#x60;                                  | | &#x60;region-id&#x60;     | Filter the search by a region id (aka regionalization). The value is the region id               | &#x60;/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query&#x3D;shirt&#x60;. |  | [default to &#39;/&#39;]
 **query** | **String**| Search term. It can contain any character. | [optional] 
 **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] 

### Return type

[**Banners**](Banners.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## correctionSearchGet

> Correction correctionSearchGet(opts)

Get attempt of correction of a misspelled term

Tries to correct a misspelled term from the search.

### Example

```javascript
import IntelligentSearchApi from 'intelligent_search_api';

let apiInstance = new IntelligentSearchApi.ProductListPageApi();
let opts = {
  'query': "query_example", // String | Search term. It can contain any character.
  'locale': "en-US" // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
};
apiInstance.correctionSearchGet(opts, (error, data, response) => {
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
 **query** | **String**| Search term. It can contain any character. | [optional] 
 **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] 

### Return type

[**Correction**](Correction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## facetsFacetsGet

> Facets facetsFacetsGet(facets, opts)

Get list of the possible facets for a given query

Lists the possible facets for a given query

### Example

```javascript
import IntelligentSearchApi from 'intelligent_search_api';

let apiInstance = new IntelligentSearchApi.ProductListPageApi();
let facets = "category-1/clothing/category-2/shirt/category-3/man"; // String | # Format  The `facets` parameter follows the format : `/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}`.  The order in which the terms appear is not relevant to the search.  You can also repeat the same `facetKey` several times for different values. For example: `category-1/shoes/color/blue/color/red/color/yellow`  # General filters  The `facets` parameter also allows the following general filters.  | `facetKey`      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | `price`         | Filter the search by a price range. The facet value follows the format `${minPrice}:${maxPrice}` | `/color/blue/price/100:500?query=shirt`                                  | | `category-${n}` | Filter the search by category, where `n` represents the category tree level (1 = department, 2 = category, 3 = subcategory, and so on) | `category-1/clothing/category-2/shirts`                                  | | `region-id`     | Filter the search by a region id (aka regionalization). The value is the region id               | `/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query=shirt`. | 
let opts = {
  'query': "query_example", // String | Search term. It can contain any character.
  'locale': "en-US", // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
  'hideUnavailableItems': false // Boolean | Whether the result should hide unavailable items (`true`), or not (`false`)
};
apiInstance.facetsFacetsGet(facets, opts, (error, data, response) => {
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
 **facets** | **String**| # Format  The &#x60;facets&#x60; parameter follows the format : &#x60;/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}&#x60;.  The order in which the terms appear is not relevant to the search.  You can also repeat the same &#x60;facetKey&#x60; several times for different values. For example: &#x60;category-1/shoes/color/blue/color/red/color/yellow&#x60;  # General filters  The &#x60;facets&#x60; parameter also allows the following general filters.  | &#x60;facetKey&#x60;      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | &#x60;price&#x60;         | Filter the search by a price range. The facet value follows the format &#x60;${minPrice}:${maxPrice}&#x60; | &#x60;/color/blue/price/100:500?query&#x3D;shirt&#x60;                                  | | &#x60;category-${n}&#x60; | Filter the search by category, where &#x60;n&#x60; represents the category tree level (1 &#x3D; department, 2 &#x3D; category, 3 &#x3D; subcategory, and so on) | &#x60;category-1/clothing/category-2/shirts&#x60;                                  | | &#x60;region-id&#x60;     | Filter the search by a region id (aka regionalization). The value is the region id               | &#x60;/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query&#x3D;shirt&#x60;. |  | [default to &#39;/&#39;]
 **query** | **String**| Search term. It can contain any character. | [optional] 
 **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] 
 **hideUnavailableItems** | **Boolean**| Whether the result should hide unavailable items (&#x60;true&#x60;), or not (&#x60;false&#x60;) | [optional] [default to false]

### Return type

[**Facets**](Facets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productSearchFacetsGet

> ProductSearch productSearchFacetsGet(facets, opts)

Get list of products for a query

Lists the products for a given query.

### Example

```javascript
import IntelligentSearchApi from 'intelligent_search_api';

let apiInstance = new IntelligentSearchApi.ProductListPageApi();
let facets = "category-1/clothing/category-2/shirt/category-3/man"; // String | # Format  The `facets` parameter follows the format : `/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}`.  The order in which the terms appear is not relevant to the search.  You can also repeat the same `facetKey` several times for different values. For example: `category-1/shoes/color/blue/color/red/color/yellow`  # General filters  The `facets` parameter also allows the following general filters.  | `facetKey`      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | `price`         | Filter the search by a price range. The facet value follows the format `${minPrice}:${maxPrice}` | `/color/blue/price/100:500?query=shirt`                                  | | `category-${n}` | Filter the search by category, where `n` represents the category tree level (1 = department, 2 = category, 3 = subcategory, and so on) | `category-1/clothing/category-2/shirts`                                  | | `region-id`     | Filter the search by a region id (aka regionalization). The value is the region id               | `/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query=shirt`. | 
let opts = {
  'query': "query_example", // String | Search term. It can contain any character.
  'simulationBehavior': "'default'", // String | Defines the simulation behavior.   * `default` - Calls the simulation for every single seller.  * `skip` - Never calls the simulation.  * `only1P` - Only calls the simulation for first party sellers.
  'count': 24, // Number | Number of products per page.
  'page': 1, // Number | Current search page.
  'sort': "sort_example", // String | Defines the sort type. If null, the products will be sorted by relevance.
  'locale': "en-US", // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
  'hideUnavailableItems': false // Boolean | Whether the result should hide unavailable items (`true`), or not (`false`)
};
apiInstance.productSearchFacetsGet(facets, opts, (error, data, response) => {
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
 **facets** | **String**| # Format  The &#x60;facets&#x60; parameter follows the format : &#x60;/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}&#x60;.  The order in which the terms appear is not relevant to the search.  You can also repeat the same &#x60;facetKey&#x60; several times for different values. For example: &#x60;category-1/shoes/color/blue/color/red/color/yellow&#x60;  # General filters  The &#x60;facets&#x60; parameter also allows the following general filters.  | &#x60;facetKey&#x60;      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | &#x60;price&#x60;         | Filter the search by a price range. The facet value follows the format &#x60;${minPrice}:${maxPrice}&#x60; | &#x60;/color/blue/price/100:500?query&#x3D;shirt&#x60;                                  | | &#x60;category-${n}&#x60; | Filter the search by category, where &#x60;n&#x60; represents the category tree level (1 &#x3D; department, 2 &#x3D; category, 3 &#x3D; subcategory, and so on) | &#x60;category-1/clothing/category-2/shirts&#x60;                                  | | &#x60;region-id&#x60;     | Filter the search by a region id (aka regionalization). The value is the region id               | &#x60;/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query&#x3D;shirt&#x60;. |  | [default to &#39;/&#39;]
 **query** | **String**| Search term. It can contain any character. | [optional] 
 **simulationBehavior** | **String**| Defines the simulation behavior.   * &#x60;default&#x60; - Calls the simulation for every single seller.  * &#x60;skip&#x60; - Never calls the simulation.  * &#x60;only1P&#x60; - Only calls the simulation for first party sellers. | [optional] [default to &#39;default&#39;]
 **count** | **Number**| Number of products per page. | [optional] [default to 24]
 **page** | **Number**| Current search page. | [optional] [default to 1]
 **sort** | **String**| Defines the sort type. If null, the products will be sorted by relevance. | [optional] 
 **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] 
 **hideUnavailableItems** | **Boolean**| Whether the result should hide unavailable items (&#x60;true&#x60;), or not (&#x60;false&#x60;) | [optional] [default to false]

### Return type

[**ProductSearch**](ProductSearch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchSuggestionsGet

> SearchSuggestions searchSuggestionsGet(opts)

Get list of suggested terms similar to the search term

Lists suggested terms similar to the search term.

### Example

```javascript
import IntelligentSearchApi from 'intelligent_search_api';

let apiInstance = new IntelligentSearchApi.ProductListPageApi();
let opts = {
  'query': "query_example", // String | Search term. It can contain any character.
  'locale': "en-US" // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
};
apiInstance.searchSuggestionsGet(opts, (error, data, response) => {
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
 **query** | **String**| Search term. It can contain any character. | [optional] 
 **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] 

### Return type

[**SearchSuggestions**](SearchSuggestions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

