# WeGaApi.FacetsApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facetsFacetGet**](FacetsApi.md#facetsFacetGet) | **GET** /facets/{facet} | Returns facets



## facetsFacetGet

> [Facet] facetsFacetGet(facet, scope, docType, opts)

Returns facets

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.FacetsApi();
let facet = "facet_example"; // String | The facet to search for
let scope = "scope_example"; // String | The scope of the result set, i.e. 'indices' or a WeGA ID
let docType = ["null"]; // [String] | The WeGA document type
let opts = {
  'term': "term_example", // String | The search term to be looked for in the facet's label
  'offset': 1, // Number | Position of first item to retrieve (starting from 1)
  'limit': 10 // Number | Number of items to retrieve (200 max)
};
apiInstance.facetsFacetGet(facet, scope, docType, opts, (error, data, response) => {
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
 **facet** | **String**| The facet to search for | 
 **scope** | **String**| The scope of the result set, i.e. &#39;indices&#39; or a WeGA ID | 
 **docType** | [**[String]**](String.md)| The WeGA document type | 
 **term** | **String**| The search term to be looked for in the facet&#39;s label | [optional] 
 **offset** | **Number**| Position of first item to retrieve (starting from 1) | [optional] [default to 1]
 **limit** | **Number**| Number of items to retrieve (200 max) | [optional] [default to 10]

### Return type

[**[Facet]**](Facet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

