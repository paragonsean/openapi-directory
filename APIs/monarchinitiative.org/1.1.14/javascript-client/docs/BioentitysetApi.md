# BioLinkApi.BioentitysetApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEntitySetAssociations**](BioentitysetApi.md#getEntitySetAssociations) | **GET** /bioentityset/associations | Returns compact associations for a given input set
[**getEntitySetGraphResource**](BioentitysetApi.md#getEntitySetGraphResource) | **GET** /bioentityset/graph | TODO Graph object spanning all entities
[**getEntitySetSummary**](BioentitysetApi.md#getEntitySetSummary) | **GET** /bioentityset/descriptor/counts | Summary statistics for objects associated
[**getOverRepresentation**](BioentitysetApi.md#getOverRepresentation) | **GET** /bioentityset/overrepresentation | Summary statistics for objects associated



## getEntitySetAssociations

> [AssociationResults] getEntitySetAssociations(opts)

Returns compact associations for a given input set

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentitysetApi();
let opts = {
  'subject': ["null"], // [String] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
  'background': ["null"], // [String] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
  'objectCategory': "objectCategory_example", // String | E.g. phenotype, function
  'objectSlim': "objectSlim_example" // String | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED
};
apiInstance.getEntitySetAssociations(opts, (error, data, response) => {
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
 **subject** | [**[String]**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **background** | [**[String]**](String.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **objectCategory** | **String**| E.g. phenotype, function | [optional] 
 **objectSlim** | **String**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEntitySetGraphResource

> getEntitySetGraphResource(opts)

TODO Graph object spanning all entities

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentitysetApi();
let opts = {
  'subject': ["null"], // [String] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
  'background': ["null"], // [String] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
  'objectCategory': "objectCategory_example", // String | E.g. phenotype, function
  'objectSlim': "objectSlim_example" // String | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED
};
apiInstance.getEntitySetGraphResource(opts, (error, data, response) => {
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
 **subject** | [**[String]**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **background** | [**[String]**](String.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **objectCategory** | **String**| E.g. phenotype, function | [optional] 
 **objectSlim** | **String**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getEntitySetSummary

> getEntitySetSummary(opts)

Summary statistics for objects associated

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentitysetApi();
let opts = {
  'subject': ["null"], // [String] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
  'background': ["null"], // [String] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
  'objectCategory': "objectCategory_example", // String | E.g. phenotype, function
  'objectSlim': "objectSlim_example" // String | Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED
};
apiInstance.getEntitySetSummary(opts, (error, data, response) => {
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
 **subject** | [**[String]**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **background** | [**[String]**](String.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **objectCategory** | **String**| E.g. phenotype, function | [optional] 
 **objectSlim** | **String**| Slim or subset to which the descriptors are to be mapped, NOT IMPLEMENTED | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOverRepresentation

> getOverRepresentation(opts)

Summary statistics for objects associated

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentitysetApi();
let opts = {
  'objectCategory': "objectCategory_example", // String | E.g. phenotype, function
  'subject': ["null"], // [String] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
  'background': ["null"], // [String] | Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests
  'subjectCategory': "'gene'", // String | Default: gene. Other types may be used e.g. disease but statistics may not make sense
  'maxPValue': "'0.05'", // String | Exclude results with p-value greater than this
  'ontology': "ontology_example", // String | ontology id. Must be obo id. Examples: go, mp, hp, uberon (optional: will be inferred if left blank)
  'taxon': "taxon_example" // String | must be NCBITaxon CURIE. Example: NCBITaxon:9606
};
apiInstance.getOverRepresentation(opts, (error, data, response) => {
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
 **objectCategory** | **String**| E.g. phenotype, function | [optional] 
 **subject** | [**[String]**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | [optional] 
 **background** | [**[String]**](String.md)| Entity ids in background set, e.g. NCBIGene:84570, NCBIGene:3630; used in over-representation tests | [optional] 
 **subjectCategory** | **String**| Default: gene. Other types may be used e.g. disease but statistics may not make sense | [optional] [default to &#39;gene&#39;]
 **maxPValue** | **String**| Exclude results with p-value greater than this | [optional] [default to &#39;0.05&#39;]
 **ontology** | **String**| ontology id. Must be obo id. Examples: go, mp, hp, uberon (optional: will be inferred if left blank) | [optional] 
 **taxon** | **String**| must be NCBITaxon CURIE. Example: NCBITaxon:9606 | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

