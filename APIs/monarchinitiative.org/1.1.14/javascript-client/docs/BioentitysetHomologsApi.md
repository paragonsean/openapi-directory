# BioLinkApi.BioentitysetHomologsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEntitySetHomologs**](BioentitysetHomologsApi.md#getEntitySetHomologs) | **GET** /bioentityset/homologs/ | Returns homology associations for a given input set of genes



## getEntitySetHomologs

> [AssociationResults] getEntitySetHomologs(opts)

Returns homology associations for a given input set of genes

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.BioentitysetHomologsApi();
let opts = {
  'subject': ["null"] // [String] | Entity ids to be examined, e.g. NCBIGene:9342, NCBIGene:7227, NCBIGene:8131, NCBIGene:157570, NCBIGene:51164, NCBIGene:6689, NCBIGene:6387
};
apiInstance.getEntitySetHomologs(opts, (error, data, response) => {
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

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

