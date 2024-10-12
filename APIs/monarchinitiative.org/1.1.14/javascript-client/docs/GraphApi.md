# BioLinkApi.GraphApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEdgeResource**](GraphApi.md#getEdgeResource) | **GET** /graph/edges/from/{id} | Returns edges emanating from a given node
[**getNodeResource**](GraphApi.md#getNodeResource) | **GET** /graph/node/{id} | Returns a graph node



## getEdgeResource

> [Graph] getEdgeResource(id, opts)

Returns edges emanating from a given node

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.GraphApi();
let id = "id_example"; // String | CURIE e.g. HP:0000465
let opts = {
  'depth': 1, // Number | How far to traverse for neighbors
  'direction': "'BOTH'", // String | Which direction to traverse (used only if relationship_type is defined)
  'relationshipType': ["null"], // [String] | Relationship type to traverse
  'entail': false, // Boolean | Include sub-properties and equivalent properties
  'graph': "'data'" // String | Which monarch graph to query
};
apiInstance.getEdgeResource(id, opts, (error, data, response) => {
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
 **id** | **String**| CURIE e.g. HP:0000465 | 
 **depth** | **Number**| How far to traverse for neighbors | [optional] [default to 1]
 **direction** | **String**| Which direction to traverse (used only if relationship_type is defined) | [optional] [default to &#39;BOTH&#39;]
 **relationshipType** | [**[String]**](String.md)| Relationship type to traverse | [optional] 
 **entail** | **Boolean**| Include sub-properties and equivalent properties | [optional] [default to false]
 **graph** | **String**| Which monarch graph to query | [optional] [default to &#39;data&#39;]

### Return type

[**[Graph]**](Graph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodeResource

> [BioObject] getNodeResource(id)

Returns a graph node

A node is an abstract representation of some kind of entity. The entity may be a physical thing such as a patient, a molecular entity such as a gene or protein, or a conceptual entity such as a class from an ontology.

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.GraphApi();
let id = "id_example"; // String | CURIE e.g. HP:0000465
apiInstance.getNodeResource(id, (error, data, response) => {
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
 **id** | **String**| CURIE e.g. HP:0000465 | 

### Return type

[**[BioObject]**](BioObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

