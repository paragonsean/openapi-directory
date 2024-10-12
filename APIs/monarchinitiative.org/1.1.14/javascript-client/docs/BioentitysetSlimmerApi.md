# BioLinkApi.BioentitysetSlimmerApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEntitySetAnatomySlimmer**](BioentitysetSlimmerApi.md#getEntitySetAnatomySlimmer) | **GET** /bioentityset/slimmer/anatomy | For a given gene(s), summarize its annotations over a defined set of slim
[**getEntitySetFunctionSlimmer**](BioentitysetSlimmerApi.md#getEntitySetFunctionSlimmer) | **GET** /bioentityset/slimmer/function | For a given gene(s), summarize its annotations over a defined set of slim
[**getEntitySetPhenotypeSlimmer**](BioentitysetSlimmerApi.md#getEntitySetPhenotypeSlimmer) | **GET** /bioentityset/slimmer/phenotype | For a given gene(s), summarize its annotations over a defined set of slim



## getEntitySetAnatomySlimmer

> getEntitySetAnatomySlimmer(subject, slim, opts)

For a given gene(s), summarize its annotations over a defined set of slim

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentitysetSlimmerApi();
let subject = ["null"]; // [String] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
let slim = ["null"]; // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
let opts = {
  'excludeAutomaticAssertions': false, // Boolean | If set, excludes associations that involve IEAs (ECO:0000501)
  'rows': 100, // Number | number of rows
  'start': 56 // Number | beginning row
};
apiInstance.getEntitySetAnatomySlimmer(subject, slim, opts, (error, data, response) => {
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
 **subject** | [**[String]**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | 
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | 
 **excludeAutomaticAssertions** | **Boolean**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getEntitySetFunctionSlimmer

> getEntitySetFunctionSlimmer(subject, slim, opts)

For a given gene(s), summarize its annotations over a defined set of slim

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentitysetSlimmerApi();
let subject = ["null"]; // [String] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
let slim = ["null"]; // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
let opts = {
  'relationshipType': "'acts_upstream_of_or_within'", // String | relationship type ('involved_in' or 'acts_upstream_of_or_within')
  'excludeAutomaticAssertions': false, // Boolean | If set, excludes associations that involve IEAs (ECO:0000501)
  'rows': 100, // Number | number of rows
  'start': 56 // Number | beginning row
};
apiInstance.getEntitySetFunctionSlimmer(subject, slim, opts, (error, data, response) => {
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
 **subject** | [**[String]**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | 
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | 
 **relationshipType** | **String**| relationship type (&#39;involved_in&#39; or &#39;acts_upstream_of_or_within&#39;) | [optional] [default to &#39;acts_upstream_of_or_within&#39;]
 **excludeAutomaticAssertions** | **Boolean**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getEntitySetPhenotypeSlimmer

> getEntitySetPhenotypeSlimmer(subject, slim, opts)

For a given gene(s), summarize its annotations over a defined set of slim

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentitysetSlimmerApi();
let subject = ["null"]; // [String] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
let slim = ["null"]; // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO)
let opts = {
  'excludeAutomaticAssertions': false, // Boolean | If set, excludes associations that involve IEAs (ECO:0000501)
  'rows': 100, // Number | number of rows
  'start': 56 // Number | beginning row
};
apiInstance.getEntitySetPhenotypeSlimmer(subject, slim, opts, (error, data, response) => {
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
 **subject** | [**[String]**](String.md)| Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387 | 
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID (IMPLEMENTED) or subset ID (TODO) | 
 **excludeAutomaticAssertions** | **Boolean**| If set, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

