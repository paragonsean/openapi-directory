# BioLinkApi.OwlOntologyApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDlQuery**](OwlOntologyApi.md#getDlQuery) | **GET** /owl/ontology/dlquery/{query} | Placeholder - use OWLery for now
[**getSparqlQuery**](OwlOntologyApi.md#getSparqlQuery) | **GET** /owl/ontology/sparql/{query} | Placeholder - use direct SPARQL endpoint for now



## getDlQuery

> [Association] getDlQuery(query)

Placeholder - use OWLery for now

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OwlOntologyApi();
let query = "query_example"; // String | 
apiInstance.getDlQuery(query, (error, data, response) => {
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
 **query** | **String**|  | 

### Return type

[**[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSparqlQuery

> [Association] getSparqlQuery(query)

Placeholder - use direct SPARQL endpoint for now

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OwlOntologyApi();
let query = "query_example"; // String | 
apiInstance.getSparqlQuery(query, (error, data, response) => {
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
 **query** | **String**|  | 

### Return type

[**[Association]**](Association.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

