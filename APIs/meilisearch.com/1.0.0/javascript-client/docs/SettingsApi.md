# MeilisearchV11.SettingsApi

All URIs are relative to *http://localhost:7700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllSettings**](SettingsApi.md#getAllSettings) | **GET** /indexes/books/settings | Get all settings
[**getDisplayedAttributes**](SettingsApi.md#getDisplayedAttributes) | **GET** /indexes/books/settings/displayed-attributes | Get displayed attributes
[**getDistinctAttribute**](SettingsApi.md#getDistinctAttribute) | **GET** /indexes/books/settings/distinct-attribute | Get distinct attribute
[**getFaceting**](SettingsApi.md#getFaceting) | **GET** /indexes/books/settings/faceting | Get faceting
[**getFilterableAttributes**](SettingsApi.md#getFilterableAttributes) | **GET** /indexes/books/settings/filterable-attributes | Get filterable attributes
[**getPagination**](SettingsApi.md#getPagination) | **GET** /indexes/books/settings/pagination | Get pagination
[**getRankingRules**](SettingsApi.md#getRankingRules) | **GET** /indexes/books/settings/ranking-rules | Get ranking rules
[**getSearchableAttributes**](SettingsApi.md#getSearchableAttributes) | **GET** /indexes/books/settings/searchable-attributes | Get searchable attributes
[**getSortableAttributes**](SettingsApi.md#getSortableAttributes) | **GET** /indexes/books/settings/sortable-attributes | Get sortable attributes
[**getStopWords**](SettingsApi.md#getStopWords) | **GET** /indexes/books/settings/stop-words | Get stop-words
[**getSynonyms**](SettingsApi.md#getSynonyms) | **GET** /indexes/books/settings/synonyms | Get synonyms
[**getTypoTolerance**](SettingsApi.md#getTypoTolerance) | **GET** /indexes/books/settings/typo-tolerance | Get typo-tolerance
[**resetAllSettings**](SettingsApi.md#resetAllSettings) | **DELETE** /indexes/books/settings | Reset all settings
[**resetDisplayedAttributes**](SettingsApi.md#resetDisplayedAttributes) | **DELETE** /indexes/books/settings/displayed-attributes | Reset displayed attributes
[**resetDistinctAttribute**](SettingsApi.md#resetDistinctAttribute) | **DELETE** /indexes/books/settings/distinct-attribute | Reset distinct attribute
[**resetFaceting**](SettingsApi.md#resetFaceting) | **DELETE** /indexes/books/settings/faceting | Reset faceting
[**resetFilterableAttributes**](SettingsApi.md#resetFilterableAttributes) | **DELETE** /indexes/books/settings/filterable-attributes | Reset filterable attributes
[**resetPagination**](SettingsApi.md#resetPagination) | **DELETE** /indexes/books/settings/pagination | Reset pagination
[**resetRankingRules**](SettingsApi.md#resetRankingRules) | **DELETE** /indexes/books/settings/ranking-rules | Reset ranking rules
[**resetSearchableAttributes**](SettingsApi.md#resetSearchableAttributes) | **DELETE** /indexes/books/settings/searchable-attributes | Reset searchable attributes
[**resetSortableAttributes**](SettingsApi.md#resetSortableAttributes) | **DELETE** /indexes/books/settings/sortable-attributes | Reset sortable attributes
[**resetStopWords**](SettingsApi.md#resetStopWords) | **DELETE** /indexes/books/settings/stop-words | Reset stop-words
[**resetSynonyms**](SettingsApi.md#resetSynonyms) | **DELETE** /indexes/books/settings/synonyms | Reset synonyms
[**resetTypoTolerance**](SettingsApi.md#resetTypoTolerance) | **DELETE** /indexes/books/settings/typo-tolerance | Reset typo-tolerance
[**updateDisplayedAttributes**](SettingsApi.md#updateDisplayedAttributes) | **PUT** /indexes/books/settings/displayed-attributes | Update displayed attributes
[**updateDistinctAttribute**](SettingsApi.md#updateDistinctAttribute) | **PUT** /indexes/books/settings/distinct-attribute | Update distinct attribute
[**updateFaceting**](SettingsApi.md#updateFaceting) | **PATCH** /indexes/books/settings/faceting | Update faceting
[**updateFilterableAttributes**](SettingsApi.md#updateFilterableAttributes) | **PUT** /indexes/books/settings/filterable-attributes | Update filterable attributes
[**updatePagination**](SettingsApi.md#updatePagination) | **PATCH** /indexes/books/settings/pagination | Update pagination
[**updateRankingRules**](SettingsApi.md#updateRankingRules) | **PUT** /indexes/books/settings/ranking-rules | Update ranking rules
[**updateSearchableAttributes**](SettingsApi.md#updateSearchableAttributes) | **PUT** /indexes/books/settings/searchable-attributes | Update searchable attributes
[**updateSettings**](SettingsApi.md#updateSettings) | **PATCH** /indexes/books/settings | Update settings
[**updateSortableAttributes**](SettingsApi.md#updateSortableAttributes) | **PUT** /indexes/books/settings/sortable-attributes | Update sortable attributes
[**updateStopWords**](SettingsApi.md#updateStopWords) | **PUT** /indexes/books/settings/stop-words | Update stop-words
[**updateSynonyms**](SettingsApi.md#updateSynonyms) | **PUT** /indexes/books/settings/synonyms | Update synonyms
[**updateTypoTolerance**](SettingsApi.md#updateTypoTolerance) | **PATCH** /indexes/books/settings/typo-tolerance | Update typo-tolerance



## getAllSettings

> getAllSettings()

Get all settings

Get all settings

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getAllSettings((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDisplayedAttributes

> getDisplayedAttributes()

Get displayed attributes

Get displayed attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getDisplayedAttributes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDistinctAttribute

> getDistinctAttribute()

Get distinct attribute

Get distinct attribute

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getDistinctAttribute((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFaceting

> getFaceting()

Get faceting

Get faceting

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getFaceting((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFilterableAttributes

> getFilterableAttributes()

Get filterable attributes

Get filterable attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getFilterableAttributes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPagination

> getPagination()

Get pagination

Get pagination

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getPagination((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRankingRules

> getRankingRules()

Get ranking rules

Get ranking rules

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getRankingRules((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSearchableAttributes

> getSearchableAttributes()

Get searchable attributes

Get searchable attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getSearchableAttributes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSortableAttributes

> getSortableAttributes()

Get sortable attributes

Get sortable attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getSortableAttributes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getStopWords

> getStopWords(opts)

Get stop-words

Get stop-words

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'requestBody': ["the"] // [String] | 
};
apiInstance.getStopWords(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**[String]**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getSynonyms

> getSynonyms()

Get synonyms

Get synonyms

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getSynonyms((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTypoTolerance

> getTypoTolerance()

Get typo-tolerance

Get typo-tolerance

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.getTypoTolerance((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetAllSettings

> resetAllSettings()

Reset all settings

Reset all settings

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetAllSettings((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetDisplayedAttributes

> resetDisplayedAttributes()

Reset displayed attributes

Reset displayed attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetDisplayedAttributes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetDistinctAttribute

> resetDistinctAttribute()

Reset distinct attribute

Reset distinct attribute

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetDistinctAttribute((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetFaceting

> resetFaceting()

Reset faceting

Reset faceting

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetFaceting((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetFilterableAttributes

> resetFilterableAttributes()

Reset filterable attributes

Reset filterable attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetFilterableAttributes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetPagination

> resetPagination()

Reset pagination

Reset pagination

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetPagination((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetRankingRules

> resetRankingRules()

Reset ranking rules

Reset ranking rules

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetRankingRules((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetSearchableAttributes

> resetSearchableAttributes()

Reset searchable attributes

Reset searchable attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetSearchableAttributes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetSortableAttributes

> resetSortableAttributes()

Reset sortable attributes

Reset sortable attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetSortableAttributes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetStopWords

> resetStopWords()

Reset stop-words

Reset stop-words

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetStopWords((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resetSynonyms

> resetSynonyms()

Reset synonyms

Reset synonyms

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetSynonyms((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## resetTypoTolerance

> resetTypoTolerance()

Reset typo-tolerance

Reset typo-tolerance

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.resetTypoTolerance((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateDisplayedAttributes

> updateDisplayedAttributes(opts)

Update displayed attributes

Update displayed attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'requestBody': ["title"] // [String] | 
};
apiInstance.updateDisplayedAttributes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**[String]**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateDistinctAttribute

> updateDistinctAttribute()

Update distinct attribute

Update distinct attribute

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
apiInstance.updateDistinctAttribute((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## updateFaceting

> updateFaceting(opts)

Update faceting

Update faceting

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'updateFacetingRequest': {"maxValuesPerFacet":3000} // UpdateFacetingRequest | 
};
apiInstance.updateFaceting(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateFacetingRequest** | [**UpdateFacetingRequest**](UpdateFacetingRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateFilterableAttributes

> updateFilterableAttributes(opts)

Update filterable attributes

Update filterable attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'requestBody': ["genre"] // [String] | 
};
apiInstance.updateFilterableAttributes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**[String]**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updatePagination

> updatePagination(opts)

Update pagination

Update pagination

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'updatePaginationRequest': {"maxTotalHits":2000} // UpdatePaginationRequest | 
};
apiInstance.updatePagination(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updatePaginationRequest** | [**UpdatePaginationRequest**](UpdatePaginationRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateRankingRules

> updateRankingRules(opts)

Update ranking rules

Update ranking rules

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'requestBody': ["typo"] // [String] | 
};
apiInstance.updateRankingRules(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**[String]**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateSearchableAttributes

> updateSearchableAttributes(opts)

Update searchable attributes

Update searchable attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'requestBody': ["title","author"] // [String] | 
};
apiInstance.updateSearchableAttributes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**[String]**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateSettings

> updateSettings(opts)

Update settings

Update settings

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'updateSettingsRequest': {"displayedAttributes":["title","author","genre","price"],"filterableAttributes":["genre","price"],"searchableAttributes":["title","author"],"sortableAttributes":["price"],"stopWords":["of","the"]} // UpdateSettingsRequest | 
};
apiInstance.updateSettings(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateSettingsRequest** | [**UpdateSettingsRequest**](UpdateSettingsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateSortableAttributes

> updateSortableAttributes(opts)

Update sortable attributes

Update sortable attributes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'requestBody': ["price"] // [String] | 
};
apiInstance.updateSortableAttributes(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**[String]**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateStopWords

> updateStopWords(opts)

Update stop-words

Update stop-words

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'requestBody': ["the","of"] // [String] | 
};
apiInstance.updateStopWords(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | [**[String]**](String.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateSynonyms

> updateSynonyms(opts)

Update synonyms

Update synonyms

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'updateSynonymsRequest': {"harry potter":["hp"],"hp":["harry potter"]} // UpdateSynonymsRequest | 
};
apiInstance.updateSynonyms(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateSynonymsRequest** | [**UpdateSynonymsRequest**](UpdateSynonymsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateTypoTolerance

> updateTypoTolerance(opts)

Update typo-tolerance

Update typo-tolerance

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SettingsApi();
let opts = {
  'updateTypoToleranceRequest': {"disableOnAttributes":["genre"],"disableOnWords":["Prince"],"minWordSizeForTypos":{"oneTypo":2,"twoTypos":11}} // UpdateTypoToleranceRequest | 
};
apiInstance.updateTypoTolerance(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateTypoToleranceRequest** | [**UpdateTypoToleranceRequest**](UpdateTypoToleranceRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

