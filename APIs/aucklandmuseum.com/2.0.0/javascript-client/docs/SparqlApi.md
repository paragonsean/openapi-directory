# AucklandMuseumApi.SparqlApi

All URIs are relative to *http://api.aucklandmuseum.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSparql**](SparqlApi.md#getSparql) | **GET** /sparql | Auckland Museum SPARQL endpoint
[**postSparql**](SparqlApi.md#postSparql) | **POST** /sparql | Auckland Museum SPARQL endpoint



## getSparql

> Object getSparql(query, opts)

Auckland Museum SPARQL endpoint

You can execute your [SPARQL](http://www.w3.org/TR/rdf-sparql-query/) queries against this endpoint.  The sparql query should be provided as the value of the request parameter &#x60;query&#x60;. Set the &#x60;Accept&#x60; header to &#x60;application/sparql-results+xml&#x60; to get results in XML. Set it to &#x60;application/sparql-results+json&#x60; to get results in JSON.   **Note:** This endpoints supports [JSON-P](http://json-p.org/). In order to get a JSON-P response, set the query parameter &#x60;callback&#x60; to your preferred callback function name. The default function name is &#x60;callback()&#x60;. When using JSON-P, there is no need to set the &#x60;Accept&#x60; header because the response will always be in &#x60;application/javascript&#x60;. 

### Example

```javascript
import AucklandMuseumApi from 'auckland_museum_api';

let apiInstance = new AucklandMuseumApi.SparqlApi();
let query = "query_example"; // String | sparql query
let opts = {
  'callback': "'callback'", // String | The [JSON-P](http://json-p.org/) callback parameter
  'infer': true // Boolean | Whether to get inferred results in the response
};
apiInstance.getSparql(query, opts, (error, data, response) => {
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
 **query** | **String**| sparql query | 
 **callback** | **String**| The [JSON-P](http://json-p.org/) callback parameter | [optional] [default to &#39;callback&#39;]
 **infer** | **Boolean**| Whether to get inferred results in the response | [optional] [default to true]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/sparql-results+json, application/sparql-results+xml, application/javascript


## postSparql

> postSparql(query, opts)

Auckland Museum SPARQL endpoint

You can execute your [SPARQL](http://www.w3.org/TR/rdf-sparql-query/) queries against this endpoint. The sparql query should be provided as the value of the request parameter &#x60;query&#x60;. Set the &#x60;Accept&#x60; header to &#x60;application/sparql-results+xml&#x60; to get results in XML. Set it to &#x60;application/sparql-results+json&#x60; to get results in JSON.  

### Example

```javascript
import AucklandMuseumApi from 'auckland_museum_api';

let apiInstance = new AucklandMuseumApi.SparqlApi();
let query = "query_example"; // String | sparql query
let opts = {
  'infer': true // Boolean | Whether to get inferred results in the response
};
apiInstance.postSparql(query, opts, (error, data, response) => {
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
 **query** | **String**| sparql query | 
 **infer** | **Boolean**| Whether to get inferred results in the response | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

