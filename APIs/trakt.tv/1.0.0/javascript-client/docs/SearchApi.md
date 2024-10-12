# TraktApi.SearchApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIDLookupResults**](SearchApi.md#getIDLookupResults) | **GET** /search/{id_type}/{id} | Get ID lookup results
[**getTextQueryResults**](SearchApi.md#getTextQueryResults) | **GET** /search/{type} | Get text query results



## getIDLookupResults

> getIDLookupResults(idType, id, opts)

Get ID lookup results

#### &amp;#128196; Pagination &amp;#10024; Extended Info  Lookup items by their Trakt, IMDB, TMDB, or TVDB ID. If you use the search url without a &#x60;type&#x60; it might return multiple items if the &#x60;id_type&#x60; is not globally unique. Specify the &#x60;type&#x60; of results by sending a single value or a comma delimited string for multiple types.  | Type | URL | |---|---| | &#x60;trakt&#x60; | &#x60;/search/trakt/:id&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;movie&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;show&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;episode&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;person&#x60; | | &#x60;imdb&#x60; | &#x60;/search/imdb/:id&#x60; | | &#x60;tmdb&#x60; | &#x60;/search/tmdb/:id&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;movie&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;show&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;episode&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;person&#x60; | | &#x60;tvdb&#x60; | &#x60;/search/tvdb/:id&#x60; | |  | &#x60;/search/tvdb/:id?type&#x3D;show&#x60; | |  | &#x60;/search/tvdb/:id?type&#x3D;episode&#x60; |

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SearchApi();
let idType = "imdb"; // String | Type of ID to lookup.
let id = "tt0848228"; // String | ID that matches with the type.
let opts = {
  'type': "movie", // String | Search type.
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getIDLookupResults(idType, id, opts, (error, data, response) => {
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
 **idType** | **String**| Type of ID to lookup. | 
 **id** | **String**| ID that matches with the type. | 
 **type** | **String**| Search type. | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTextQueryResults

> getTextQueryResults(type, query, opts)

Get text query results

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Search all text fields that a media object contains (i.e. title, overview, etc). Results are ordered by the most relevant score. Specify the &#x60;type&#x60; of results by sending a single value or a comma delimited string for multiple types.  #### Special Characters  Our search engine (Solr) gives the following characters special meaning when they appear in a query:  &#x60;+ - &amp;&amp; || ! ( ) { } [ ] ^ \&quot; ~ * ? : /&#x60;  To interpret any of these characters literally (and not as a special character), precede the character with a backslash &#x60;\\&#x60; character.  #### Search Fields  By default, all text fields are used to search for the &#x60;query&#x60;. You can optionally specify the &#x60;fields&#x60; parameter with a single value or comma delimited string for multiple fields. Each &#x60;type&#x60; has specific &#x60;fields&#x60; that can be specified. This can be useful if you want to support more strict searches (i.e. title only).  | Type | Field | |---|---| | &#x60;movie&#x60; | &#x60;title&#x60; | |  | &#x60;tagline&#x60; | |  | &#x60;overview&#x60; | |  | &#x60;people&#x60; | |  | &#x60;translations&#x60; | |  | &#x60;aliases&#x60; | | &#x60;show&#x60; | &#x60;title&#x60; | |  | &#x60;overview&#x60; | |  | &#x60;people&#x60; | |  | &#x60;translations&#x60; | |  | &#x60;aliases&#x60; | | &#x60;episode&#x60; | &#x60;title&#x60; | |  | &#x60;overview&#x60; | | &#x60;person&#x60; | &#x60;name&#x60; | |  | &#x60;biography&#x60; | | &#x60;list&#x60; | &#x60;name&#x60; | |  | &#x60;description&#x60; |

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SearchApi();
let type = "movie"; // String | Search type.
let query = "tron"; // String | Search all text based fields.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'body': "body_example" // String | Specific text fields.
};
apiInstance.getTextQueryResults(type, query, opts, (error, data, response) => {
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
 **type** | **String**| Search type. | 
 **query** | **String**| Search all text based fields. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **body** | **String**| Specific text fields. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

