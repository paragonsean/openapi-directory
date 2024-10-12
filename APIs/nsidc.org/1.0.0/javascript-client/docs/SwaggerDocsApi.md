# NsidcWebServiceDocumentationIndex.SwaggerDocsApi

All URIs are relative to *http://nsidc.org/api/dataset/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facets**](SwaggerDocsApi.md#facets) | **GET** /Facets | View the facet information corresponding to a search
[**id**](SwaggerDocsApi.md#id) | **GET** /suggest | Suggest search terms based on a partial query
[**openSearch**](SwaggerDocsApi.md#openSearch) | **GET** /OpenSearch | Search documents using the OpenSearch 1.1 Specification
[**opensearchDescription**](SwaggerDocsApi.md#opensearchDescription) | **GET** /OpenSearchDescription | Describes the web interface of NSIDC&#39;s data search engine



## facets

> String facets(opts)

View the facet information corresponding to a search

In the NSIDC Search and Arctic Data Explorer interfaces, this endpoint is used in conjunction with /OpenSearch whenever a user submits a new search. Consequently, it has the same parameters as /OpenSearch.

### Example

```javascript
import NsidcWebServiceDocumentationIndex from 'nsidc_web_service_documentation_index';

let apiInstance = new NsidcWebServiceDocumentationIndex.SwaggerDocsApi();
let opts = {
  'searchTerms': "searchTerms_example", // String | URL-encoded keyword or keywords desired by the client; OpenSearch 1.1
  'count': 25, // Number | The number of search results per page desired by the client; OpenSearch 1.1
  'startIndex': 1, // Number | First search result desired by the search client; OpenSearch 1.1
  'spatial': "'-180.0,-90.0,180.0,90.0'", // String | 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \"box\" parameter
  'sortKeys': "'score,,desc'", // String | Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0
  'startDate': new Date("2013-10-20"), // Date | The start date in yyyy-mm-dd format
  'endDate': new Date("2013-10-20"), // Date | The end date in yyyy-mm-dd format
  'facetFilters': "facetFilters_example", // String | Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values
  'source': "'NSIDC'" // String | Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC
};
apiInstance.facets(opts, (error, data, response) => {
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
 **searchTerms** | **String**| URL-encoded keyword or keywords desired by the client; OpenSearch 1.1 | [optional] 
 **count** | **Number**| The number of search results per page desired by the client; OpenSearch 1.1 | [optional] [default to 25]
 **startIndex** | **Number**| First search result desired by the search client; OpenSearch 1.1 | [optional] [default to 1]
 **spatial** | **String**| 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \&quot;box\&quot; parameter | [optional] [default to &#39;-180.0,-90.0,180.0,90.0&#39;]
 **sortKeys** | **String**| Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0 | [optional] [default to &#39;score,,desc&#39;]
 **startDate** | **Date**| The start date in yyyy-mm-dd format | [optional] 
 **endDate** | **Date**| The end date in yyyy-mm-dd format | [optional] 
 **facetFilters** | **String**| Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values | [optional] 
 **source** | **String**| Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC | [optional] [default to &#39;NSIDC&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/nsidcfacets+xml


## id

> String id(q, source)

Suggest search terms based on a partial query

In NSIDC Search and the Arctic Data Explorer, this endpoint is queried whenever the user types into the search terms box, and the returned suggestions are displayed in a dropdown beneath the search terms box. The q parameter and returned JSON follow the specifications of the OpenSearch Suggestions 1.0 extension.

### Example

```javascript
import NsidcWebServiceDocumentationIndex from 'nsidc_web_service_documentation_index';

let apiInstance = new NsidcWebServiceDocumentationIndex.SwaggerDocsApi();
let q = "q_example"; // String | Search terms typed into the interface (minimum two characters)
let source = "'NSIDC'"; // String | Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC
apiInstance.id(q, source, (error, data, response) => {
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
 **q** | **String**| Search terms typed into the interface (minimum two characters) | 
 **source** | **String**| Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC | [default to &#39;NSIDC&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/x-suggestions+json


## openSearch

> String openSearch(opts)

Search documents using the OpenSearch 1.1 Specification

This endpoint uses parameters from the OpenSearch 1.1 specification, as well as parameters from the OpenSearch Geo (1.0) and SRU (1.0) extensions.

### Example

```javascript
import NsidcWebServiceDocumentationIndex from 'nsidc_web_service_documentation_index';

let apiInstance = new NsidcWebServiceDocumentationIndex.SwaggerDocsApi();
let opts = {
  'searchTerms': "searchTerms_example", // String | URL-encoded keyword or keywords desired by the client; OpenSearch 1.1
  'count': 25, // Number | The number of search results per page desired by the client; OpenSearch 1.1
  'startIndex': 1, // Number | First search result desired by the search client; OpenSearch 1.1
  'spatial': "'-180.0,-90.0,180.0,90.0'", // String | 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \"box\" parameter
  'sortKeys': "'score,,desc'", // String | Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0
  'startDate': new Date("2013-10-20"), // Date | The start date in yyyy-mm-dd format
  'endDate': new Date("2013-10-20"), // Date | The end date in yyyy-mm-dd format
  'facetFilters': "facetFilters_example", // String | Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values
  'source': "'NSIDC'" // String | Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC
};
apiInstance.openSearch(opts, (error, data, response) => {
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
 **searchTerms** | **String**| URL-encoded keyword or keywords desired by the client; OpenSearch 1.1 | [optional] 
 **count** | **Number**| The number of search results per page desired by the client; OpenSearch 1.1 | [optional] [default to 25]
 **startIndex** | **Number**| First search result desired by the search client; OpenSearch 1.1 | [optional] [default to 1]
 **spatial** | **String**| 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \&quot;box\&quot; parameter | [optional] [default to &#39;-180.0,-90.0,180.0,90.0&#39;]
 **sortKeys** | **String**| Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0 | [optional] [default to &#39;score,,desc&#39;]
 **startDate** | **Date**| The start date in yyyy-mm-dd format | [optional] 
 **endDate** | **Date**| The end date in yyyy-mm-dd format | [optional] 
 **facetFilters** | **String**| Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values | [optional] 
 **source** | **String**| Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC | [optional] [default to &#39;NSIDC&#39;]

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/atom+xml


## opensearchDescription

> String opensearchDescription()

Describes the web interface of NSIDC&#39;s data search engine

### Example

```javascript
import NsidcWebServiceDocumentationIndex from 'nsidc_web_service_documentation_index';

let apiInstance = new NsidcWebServiceDocumentationIndex.SwaggerDocsApi();
apiInstance.opensearchDescription((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/opensearchdescription+xml

