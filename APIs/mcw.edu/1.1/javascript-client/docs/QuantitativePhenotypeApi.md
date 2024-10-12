# RatGenomeDatabaseRestApi.QuantitativePhenotypeApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChartInfoUsingGET**](QuantitativePhenotypeApi.md#getChartInfoUsingGET) | **GET** /phenotype/phenominer/chart/{speciesTypeKey}/{refRgdId}/{termString} | Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla).  Reference RGD ID for a study works like a filter.
[**getChartInfoUsingGET1**](QuantitativePhenotypeApi.md#getChartInfoUsingGET1) | **GET** /phenotype/phenominer/chart/{speciesTypeKey}/{termString} | Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla)



## getChartInfoUsingGET

> {String: Object} getChartInfoUsingGET(speciesTypeKey, refRgdId, termString)

Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla).  Reference RGD ID for a study works like a filter.

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.QuantitativePhenotypeApi();
let speciesTypeKey = 56; // Number | Species Type Key - 3=rat 4=chinchilla 
let refRgdId = 56; // Number | Reference RGD ID for a study
let termString = "termString_example"; // String | List of term accession IDs
apiInstance.getChartInfoUsingGET(speciesTypeKey, refRgdId, termString, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| Species Type Key - 3&#x3D;rat 4&#x3D;chinchilla  | 
 **refRgdId** | **Number**| Reference RGD ID for a study | 
 **termString** | **String**| List of term accession IDs | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getChartInfoUsingGET1

> {String: Object} getChartInfoUsingGET1(speciesTypeKey, termString)

Return a list of quantitative phenotypes values based on a combination of Clinical Measurement, Experimental Condition, Rat Strain, and/or Measurement Method ontology terms.  Results will be all records that match all terms submitted.  Ontology ids should be submitted as a comma delimited list (ex. RS:0000029,CMO:0000155,CMO:0000139).  Species type is an integer value (3&#x3D;rat, 4&#x3D;chinchilla)

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.QuantitativePhenotypeApi();
let speciesTypeKey = 56; // Number | Species Type Key - 3=rat 4=chinchilla 
let termString = "termString_example"; // String | List of term accession IDs
apiInstance.getChartInfoUsingGET1(speciesTypeKey, termString, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| Species Type Key - 3&#x3D;rat 4&#x3D;chinchilla  | 
 **termString** | **String**| List of term accession IDs | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

