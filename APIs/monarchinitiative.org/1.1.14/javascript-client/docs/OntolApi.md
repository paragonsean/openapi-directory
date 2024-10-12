# BioLinkApi.OntolApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getExtractOntologySubgraphResource**](OntolApi.md#getExtractOntologySubgraphResource) | **GET** /ontol/subgraph/{ontology}/{node} | Extract a subgraph from an ontology
[**getInformationContentResource**](OntolApi.md#getInformationContentResource) | **GET** /ontol/information_content/{subject_category}/{object_category}/{subject_taxon} | Returns information content (IC) for a set of relevant ontology classes
[**postExtractOntologySubgraphResource**](OntolApi.md#postExtractOntologySubgraphResource) | **POST** /ontol/subgraph/{ontology}/{node} | Extract a subgraph from an ontology



## getExtractOntologySubgraphResource

> getExtractOntologySubgraphResource(node, ontology, opts)

Extract a subgraph from an ontology

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntolApi();
let node = "node_example"; // String | class ID, e.g. HP:0001288
let ontology = "ontology_example"; // String | ontology ID, e.g. go, uberon, mp, hp
let opts = {
  'cnode': ["null"], // [String] | Additional classes
  'includeAncestors': true, // Boolean | Include Ancestors
  'includeDescendants': true, // Boolean | Include Descendants
  'relation': ["null"], // [String] | Additional classes
  'includeMeta': false // Boolean | Include metadata in response
};
apiInstance.getExtractOntologySubgraphResource(node, ontology, opts, (error, data, response) => {
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
 **node** | **String**| class ID, e.g. HP:0001288 | 
 **ontology** | **String**| ontology ID, e.g. go, uberon, mp, hp | 
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


## getInformationContentResource

> getInformationContentResource(subjectCategory, objectCategory, subjectTaxon, opts)

Returns information content (IC) for a set of relevant ontology classes

&#x60;&#x60;&#x60; IC &#x3D; -log2( freq(t) / popSize ) &#x60;&#x60;&#x60;  Here the frequency and population is calculated for a particular dataset: e.g. all human disease-phenotype associations

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntolApi();
let subjectCategory = "subjectCategory_example"; // String | 
let objectCategory = "objectCategory_example"; // String | 
let subjectTaxon = "subjectTaxon_example"; // String | 
let opts = {
  'evidence': "evidence_example" // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
};
apiInstance.getInformationContentResource(subjectCategory, objectCategory, subjectTaxon, opts, (error, data, response) => {
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
 **subjectCategory** | **String**|  | 
 **objectCategory** | **String**|  | 
 **subjectTaxon** | **String**|  | 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postExtractOntologySubgraphResource

> postExtractOntologySubgraphResource(node, ontology, opts)

Extract a subgraph from an ontology

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.OntolApi();
let node = "node_example"; // String | class ID, e.g. HP:0001288
let ontology = "ontology_example"; // String | ontology ID, e.g. go, uberon, mp, hp
let opts = {
  'cnode': ["null"], // [String] | Additional classes
  'includeAncestors': true, // Boolean | Include Ancestors
  'includeDescendants': true, // Boolean | Include Descendants
  'relation': ["null"], // [String] | Additional classes
  'includeMeta': false // Boolean | Include metadata in response
};
apiInstance.postExtractOntologySubgraphResource(node, ontology, opts, (error, data, response) => {
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
 **node** | **String**| class ID, e.g. HP:0001288 | 
 **ontology** | **String**| ontology ID, e.g. go, uberon, mp, hp | 
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

