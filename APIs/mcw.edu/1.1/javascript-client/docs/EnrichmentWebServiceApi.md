# RatGenomeDatabaseRestApi.EnrichmentWebServiceApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEnrichmentDataUsingPOST**](EnrichmentWebServiceApi.md#getEnrichmentDataUsingPOST) | **POST** /enrichment/annotatedGenes | Return a list of genes annotated to the term.Genes are rgdids separated by comma.Species type is an integer value.term is the ontology
[**getEnrichmentDataUsingPOST1**](EnrichmentWebServiceApi.md#getEnrichmentDataUsingPOST1) | **POST** /enrichment/data | Return a chart of ontology terms annotated to the genes.Genes are rgdids separated by comma.Species type is an integer value.Aspect is the Ontology group



## getEnrichmentDataUsingPOST

> Object getEnrichmentDataUsingPOST(enrichmentGeneRequest)

Return a list of genes annotated to the term.Genes are rgdids separated by comma.Species type is an integer value.term is the ontology

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.EnrichmentWebServiceApi();
let enrichmentGeneRequest = new RatGenomeDatabaseRestApi.EnrichmentGeneRequest(); // EnrichmentGeneRequest | geneRequest
apiInstance.getEnrichmentDataUsingPOST(enrichmentGeneRequest, (error, data, response) => {
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
 **enrichmentGeneRequest** | [**EnrichmentGeneRequest**](EnrichmentGeneRequest.md)| geneRequest | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getEnrichmentDataUsingPOST1

> Object getEnrichmentDataUsingPOST1(enrichmentRequest)

Return a chart of ontology terms annotated to the genes.Genes are rgdids separated by comma.Species type is an integer value.Aspect is the Ontology group

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.EnrichmentWebServiceApi();
let enrichmentRequest = new RatGenomeDatabaseRestApi.EnrichmentRequest(); // EnrichmentRequest | enrichmentRequest
apiInstance.getEnrichmentDataUsingPOST1(enrichmentRequest, (error, data, response) => {
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
 **enrichmentRequest** | [**EnrichmentRequest**](EnrichmentRequest.md)| enrichmentRequest | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

