# BioLinkApi.SearchApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAutocomplete**](SearchApi.md#getAutocomplete) | **GET** /search/entity/autocomplete/{term} | Returns list of matching concepts or entities using lexical search
[**getSearchEntities**](SearchApi.md#getSearchEntities) | **GET** /search/entity/{term} | Returns list of matching concepts or entities using lexical search
[**getSearchHpoEntities**](SearchApi.md#getSearchHpoEntities) | **GET** /search/entity/hpo-pl/{term} | Returns list of matching concepts or entities using lexical search



## getAutocomplete

> AutocompleteResults getAutocomplete(term, opts)

Returns list of matching concepts or entities using lexical search

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.SearchApi();
let term = "term_example"; // String | 
let opts = {
  'fq': ["null"], // [String] | fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior.
  'category': ["null"], // [String] | e.g. gene, disease
  'prefix': ["null"], // [String] | ontology prefix: HP, -MONDO
  'includeEqs': false, // Boolean | Include equivalent ids in prefix filter
  'boostFx': ["null"], // [String] | boost function e.g. pow(edges,0.334)
  'boostQ': ["null"], // [String] | boost query e.g. category:genotype^-10
  'taxon': ["null"], // [String] | taxon filter, eg NCBITaxon:9606, includes inferred taxa
  'rows': 20, // Number | number of rows
  'start': "'0'", // String | row number to start from
  'highlightClass': "highlightClass_example", // String | highlight class
  'minMatch': "minMatch_example", // String | minimum should match parameter, see solr docs for details
  'excludeGroups': false, // Boolean | Exclude grouping classes (classes with subclasses)
  'minimalTokenizer': false // Boolean | set to true to use the minimal tokenizer, good for variants and genotypes
};
apiInstance.getAutocomplete(term, opts, (error, data, response) => {
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
 **term** | **String**|  | 
 **fq** | [**[String]**](String.md)| fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior. | [optional] 
 **category** | [**[String]**](String.md)| e.g. gene, disease | [optional] 
 **prefix** | [**[String]**](String.md)| ontology prefix: HP, -MONDO | [optional] 
 **includeEqs** | **Boolean**| Include equivalent ids in prefix filter | [optional] [default to false]
 **boostFx** | [**[String]**](String.md)| boost function e.g. pow(edges,0.334) | [optional] 
 **boostQ** | [**[String]**](String.md)| boost query e.g. category:genotype^-10 | [optional] 
 **taxon** | [**[String]**](String.md)| taxon filter, eg NCBITaxon:9606, includes inferred taxa | [optional] 
 **rows** | **Number**| number of rows | [optional] [default to 20]
 **start** | **String**| row number to start from | [optional] [default to &#39;0&#39;]
 **highlightClass** | **String**| highlight class | [optional] 
 **minMatch** | **String**| minimum should match parameter, see solr docs for details | [optional] 
 **excludeGroups** | **Boolean**| Exclude grouping classes (classes with subclasses) | [optional] [default to false]
 **minimalTokenizer** | **Boolean**| set to true to use the minimal tokenizer, good for variants and genotypes | [optional] [default to false]

### Return type

[**AutocompleteResults**](AutocompleteResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSearchEntities

> SearchResult getSearchEntities(term, opts)

Returns list of matching concepts or entities using lexical search

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.SearchApi();
let term = "term_example"; // String | search string, e.g. shh, parkinson, femur
let opts = {
  'fq': ["null"], // [String] | fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior.
  'category': ["null"], // [String] | e.g. gene, disease
  'prefix': ["null"], // [String] | ontology prefix: HP, -MONDO
  'includeEqs': false, // Boolean | Include equivalent ids in prefix filter
  'boostFx': ["null"], // [String] | boost function e.g. pow(edges,0.334)
  'boostQ': ["null"], // [String] | boost query e.g. category:genotype^-10
  'taxon': ["null"], // [String] | taxon filter, eg NCBITaxon:9606, includes inferred taxa
  'rows': 20, // Number | number of rows
  'start': "'0'", // String | row number to start from
  'highlightClass': "highlightClass_example", // String | highlight class
  'minMatch': "minMatch_example", // String | minimum should match parameter, see solr docs for details
  'excludeGroups': false, // Boolean | Exclude grouping classes (classes with subclasses)
  'minimalTokenizer': false // Boolean | set to true to use the minimal tokenizer, good for variants and genotypes
};
apiInstance.getSearchEntities(term, opts, (error, data, response) => {
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
 **term** | **String**| search string, e.g. shh, parkinson, femur | 
 **fq** | [**[String]**](String.md)| fq string passed directly to solr, note that multiple filters will be combined with an AND operator. Combining fq_string with other parameters may result in unexpected behavior. | [optional] 
 **category** | [**[String]**](String.md)| e.g. gene, disease | [optional] 
 **prefix** | [**[String]**](String.md)| ontology prefix: HP, -MONDO | [optional] 
 **includeEqs** | **Boolean**| Include equivalent ids in prefix filter | [optional] [default to false]
 **boostFx** | [**[String]**](String.md)| boost function e.g. pow(edges,0.334) | [optional] 
 **boostQ** | [**[String]**](String.md)| boost query e.g. category:genotype^-10 | [optional] 
 **taxon** | [**[String]**](String.md)| taxon filter, eg NCBITaxon:9606, includes inferred taxa | [optional] 
 **rows** | **Number**| number of rows | [optional] [default to 20]
 **start** | **String**| row number to start from | [optional] [default to &#39;0&#39;]
 **highlightClass** | **String**| highlight class | [optional] 
 **minMatch** | **String**| minimum should match parameter, see solr docs for details | [optional] 
 **excludeGroups** | **Boolean**| Exclude grouping classes (classes with subclasses) | [optional] [default to false]
 **minimalTokenizer** | **Boolean**| set to true to use the minimal tokenizer, good for variants and genotypes | [optional] [default to false]

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSearchHpoEntities

> LayResults getSearchHpoEntities(term, opts)

Returns list of matching concepts or entities using lexical search

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.SearchApi();
let term = "term_example"; // String | search string, e.g. muscle atrophy, frequent infections
let opts = {
  'rows': 10, // Number | number of rows
  'start': "'0'", // String | row number to start from
  'phenotypeGroup': "phenotypeGroup_example", // String | phenotype group id
  'phenotypeGroupLabel': "phenotypeGroupLabel_example", // String | phenotype group label
  'anatomicalSystem': "anatomicalSystem_example", // String | anatomical system id
  'anatomicalSystemLabel': "anatomicalSystemLabel_example", // String | anatomical system label
  'highlightClass': "highlightClass_example" // String | highlight class
};
apiInstance.getSearchHpoEntities(term, opts, (error, data, response) => {
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
 **term** | **String**| search string, e.g. muscle atrophy, frequent infections | 
 **rows** | **Number**| number of rows | [optional] [default to 10]
 **start** | **String**| row number to start from | [optional] [default to &#39;0&#39;]
 **phenotypeGroup** | **String**| phenotype group id | [optional] 
 **phenotypeGroupLabel** | **String**| phenotype group label | [optional] 
 **anatomicalSystem** | **String**| anatomical system id | [optional] 
 **anatomicalSystemLabel** | **String**| anatomical system label | [optional] 
 **highlightClass** | **String**| highlight class | [optional] 

### Return type

[**LayResults**](LayResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

