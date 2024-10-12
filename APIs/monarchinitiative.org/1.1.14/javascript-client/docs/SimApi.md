# BioLinkApi.SimApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAnnotationScore**](SimApi.md#getAnnotationScore) | **GET** /sim/score | Get annotation score
[**getSimCompare**](SimApi.md#getSimCompare) | **GET** /sim/compare | Compare a reference profile vs one profiles
[**getSimSearch**](SimApi.md#getSimSearch) | **GET** /sim/search | Search for phenotypically similar diseases or model genes
[**postAnnotationScore**](SimApi.md#postAnnotationScore) | **POST** /sim/score | Get annotation score
[**postSimCompare**](SimApi.md#postSimCompare) | **POST** /sim/compare | Compare a reference profile vs one or more profiles



## getAnnotationScore

> SufficiencyOutput getAnnotationScore(opts)

Get annotation score

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.SimApi();
let opts = {
  'id': ["null"], // [String] | Phenotype identifier (eg HP:0004935)
  'absentId': ["null"] // [String] | absent phenotype (eg HP:0002828)
};
apiInstance.getAnnotationScore(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Phenotype identifier (eg HP:0004935) | [optional] 
 **absentId** | [**[String]**](String.md)| absent phenotype (eg HP:0002828) | [optional] 

### Return type

[**SufficiencyOutput**](SufficiencyOutput.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSimCompare

> SimResult getSimCompare(opts)

Compare a reference profile vs one profiles

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.SimApi();
let opts = {
  'isFeatureSet': true, // Boolean | set to true if *all* input ids are phenotypic features, else set to false
  'metric': "'phenodigm'", // String | Metric for computing similarity
  'refId': ["null"], // [String] | A phenotype or identifier that is composed of phenotypes (eg disease, gene)
  'queryId': ["null"] // [String] | A phenotype or identifier that is composed of phenotypes (eg disease, gene)
};
apiInstance.getSimCompare(opts, (error, data, response) => {
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
 **isFeatureSet** | **Boolean**| set to true if *all* input ids are phenotypic features, else set to false | [optional] [default to true]
 **metric** | **String**| Metric for computing similarity | [optional] [default to &#39;phenodigm&#39;]
 **refId** | [**[String]**](String.md)| A phenotype or identifier that is composed of phenotypes (eg disease, gene) | [optional] 
 **queryId** | [**[String]**](String.md)| A phenotype or identifier that is composed of phenotypes (eg disease, gene) | [optional] 

### Return type

[**SimResult**](SimResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSimSearch

> SimResult getSimSearch(opts)

Search for phenotypically similar diseases or model genes

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.SimApi();
let opts = {
  'isFeatureSet': true, // Boolean | set to true if *all* input ids are phenotypic features, else set to false
  'metric': "'phenodigm'", // String | Metric for computing similarity
  'id': ["null"], // [String] | A phenotype or identifier that is composed of phenotypes (eg disease, gene)
  'limit': 20, // Number | number of rows, max 500
  'taxon': "taxon_example" // String | ncbi taxon id
};
apiInstance.getSimSearch(opts, (error, data, response) => {
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
 **isFeatureSet** | **Boolean**| set to true if *all* input ids are phenotypic features, else set to false | [optional] [default to true]
 **metric** | **String**| Metric for computing similarity | [optional] [default to &#39;phenodigm&#39;]
 **id** | [**[String]**](String.md)| A phenotype or identifier that is composed of phenotypes (eg disease, gene) | [optional] 
 **limit** | **Number**| number of rows, max 500 | [optional] [default to 20]
 **taxon** | **String**| ncbi taxon id | [optional] 

### Return type

[**SimResult**](SimResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postAnnotationScore

> SufficiencyOutput postAnnotationScore(sufficiencyPostInput)

Get annotation score

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.SimApi();
let sufficiencyPostInput = new BioLinkApi.SufficiencyPostInput(); // SufficiencyPostInput | 
apiInstance.postAnnotationScore(sufficiencyPostInput, (error, data, response) => {
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
 **sufficiencyPostInput** | [**SufficiencyPostInput**](SufficiencyPostInput.md)|  | 

### Return type

[**SufficiencyOutput**](SufficiencyOutput.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSimCompare

> SimResult postSimCompare(compareInput)

Compare a reference profile vs one or more profiles

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.SimApi();
let compareInput = new BioLinkApi.CompareInput(); // CompareInput | 
apiInstance.postSimCompare(compareInput, (error, data, response) => {
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
 **compareInput** | [**CompareInput**](CompareInput.md)|  | 

### Return type

[**SimResult**](SimResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

