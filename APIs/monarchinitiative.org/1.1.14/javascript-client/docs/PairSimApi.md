# BioLinkApi.PairSimApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPairSimJaccardResource**](PairSimApi.md#getPairSimJaccardResource) | **GET** /pair/sim/jaccard/{id1}/{id2} | Get pairwise similarity



## getPairSimJaccardResource

> getPairSimJaccardResource(id2, id1, opts)

Get pairwise similarity

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.PairSimApi();
let id2 = "id2_example"; // String | id, e.g. NCBIGene:1200; ZFIN:ZDB-GENE-980528-2059; UniProtKB:P12644
let id1 = "id1_example"; // String | id, e.g. NCBIGene:10891; ZFIN:ZDB-GENE-980526-166; UniProtKB:Q15465
let opts = {
  'objectCategory': "objectCategory_example" // String | e.g. disease, phenotype, gene. Two subjects will be compared based on overlap between associations to objects in this category
};
apiInstance.getPairSimJaccardResource(id2, id1, opts, (error, data, response) => {
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
 **id2** | **String**| id, e.g. NCBIGene:1200; ZFIN:ZDB-GENE-980528-2059; UniProtKB:P12644 | 
 **id1** | **String**| id, e.g. NCBIGene:10891; ZFIN:ZDB-GENE-980526-166; UniProtKB:Q15465 | 
 **objectCategory** | **String**| e.g. disease, phenotype, gene. Two subjects will be compared based on overlap between associations to objects in this category | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

