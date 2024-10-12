# BioLinkApi.OntologyApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOntologySubset**](OntologyApi.md#getOntologySubset) | **GET** /ontology/subset/{id} | Returns meta data of an ontology subset (slim)
[**getOntologyTerm**](OntologyApi.md#getOntologyTerm) | **GET** /ontology/term/{id} | Returns meta data of an ontology term
[**getOntologyTermGraph**](OntologyApi.md#getOntologyTermGraph) | **GET** /ontology/term/{id}/graph | Returns graph of an ontology term
[**getOntologyTermSubgraph**](OntologyApi.md#getOntologyTermSubgraph) | **GET** /ontology/term/{id}/subgraph | Extract a subgraph from an ontology term
[**getOntologyTermSubsets**](OntologyApi.md#getOntologyTermSubsets) | **GET** /ontology/term/{id}/subsets | Returns subsets (slims) associated to an ontology term
[**getOntologyTermsSharedAncestor**](OntologyApi.md#getOntologyTermsSharedAncestor) | **GET** /ontology/shared/{subject}/{object} | Returns the ancestor ontology terms shared by two ontology terms



## getOntologySubset

> getOntologySubset(id)

Returns meta data of an ontology subset (slim)

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntologyApi();
let id = "id_example"; // String | name of a slim subset, e.g. goslim_agr, goslim_generic
apiInstance.getOntologySubset(id, (error, data, response) => {
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
 **id** | **String**| name of a slim subset, e.g. goslim_agr, goslim_generic | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOntologyTerm

> getOntologyTerm(id)

Returns meta data of an ontology term

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntologyApi();
let id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0003677
apiInstance.getOntologyTerm(id, (error, data, response) => {
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
 **id** | **String**| CURIE identifier of a GO term, e.g. GO:0003677 | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOntologyTermGraph

> getOntologyTermGraph(id, opts)

Returns graph of an ontology term

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntologyApi();
let id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0000981
let opts = {
  'graphType': "'topology_graph'" // String | graph type ('topology_graph', 'regulates_transitivity_graph' or 'neighborhood_graph')
};
apiInstance.getOntologyTermGraph(id, opts, (error, data, response) => {
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
 **id** | **String**| CURIE identifier of a GO term, e.g. GO:0000981 | 
 **graphType** | **String**| graph type (&#39;topology_graph&#39;, &#39;regulates_transitivity_graph&#39; or &#39;neighborhood_graph&#39;) | [optional] [default to &#39;topology_graph&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOntologyTermSubgraph

> getOntologyTermSubgraph(id, opts)

Extract a subgraph from an ontology term

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntologyApi();
let id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0007275
let opts = {
  'cnode': ["null"], // [String] | Additional classes
  'includeAncestors': true, // Boolean | Include Ancestors
  'includeDescendants': true, // Boolean | Include Descendants
  'relation': ["null"], // [String] | Additional classes
  'includeMeta': false // Boolean | Include metadata in response
};
apiInstance.getOntologyTermSubgraph(id, opts, (error, data, response) => {
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
 **id** | **String**| CURIE identifier of a GO term, e.g. GO:0007275 | 
 **cnode** | [**[String]**](String.md)| Additional classes | [optional] 
 **includeAncestors** | **Boolean**| Include Ancestors | [optional] [default to true]
 **includeDescendants** | **Boolean**| Include Descendants | [optional] 
 **relation** | [**[String]**](String.md)| Additional classes | [optional] 
 **includeMeta** | **Boolean**| Include metadata in response | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOntologyTermSubsets

> getOntologyTermSubsets(id)

Returns subsets (slims) associated to an ontology term

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntologyApi();
let id = "id_example"; // String | CURIE identifier of a GO term, e.g. GO:0006259
apiInstance.getOntologyTermSubsets(id, (error, data, response) => {
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
 **id** | **String**| CURIE identifier of a GO term, e.g. GO:0006259 | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOntologyTermsSharedAncestor

> getOntologyTermsSharedAncestor(subject, object)

Returns the ancestor ontology terms shared by two ontology terms

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntologyApi();
let subject = "subject_example"; // String | CURIE identifier of a GO term, e.g. GO:0006259
let object = "object_example"; // String | CURIE identifier of a GO term, e.g. GO:0046483
apiInstance.getOntologyTermsSharedAncestor(subject, object, (error, data, response) => {
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
 **subject** | **String**| CURIE identifier of a GO term, e.g. GO:0006259 | 
 **object** | **String**| CURIE identifier of a GO term, e.g. GO:0046483 | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

