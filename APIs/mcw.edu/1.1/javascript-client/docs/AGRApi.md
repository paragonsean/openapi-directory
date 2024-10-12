# RatGenomeDatabaseRestApi.AGRApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAffectedGenomicModelsUsingGET**](AGRApi.md#getAffectedGenomicModelsUsingGET) | **GET** /agr/affectedGenomicModels/{taxonId} | Get affected genomic models (rat strains with gene alleles) submitted by RGD to AGR by taxonId
[**getAllelesForTaxonUsingGET**](AGRApi.md#getAllelesForTaxonUsingGET) | **GET** /agr/alleles/{taxonId} | Get gene allele records submitted by RGD to AGR by taxonId
[**getExpressionForTaxonUsingGET**](AGRApi.md#getExpressionForTaxonUsingGET) | **GET** /agr/expression/{taxonId} | Get expression annotations submitted by RGD to AGR by taxonId
[**getGenesForLatestAssemblyUsingGET**](AGRApi.md#getGenesForLatestAssemblyUsingGET) | **GET** /agr/{taxonId} | Get gene records submitted by RGD to AGR by taxonId
[**getPhenotypesForTaxonUsingGET**](AGRApi.md#getPhenotypesForTaxonUsingGET) | **GET** /agr/phenotypes/{taxonId} | Get phenotype annotations submitted by RGD to AGR by taxonId
[**getVariantsForTaxonUsingGET**](AGRApi.md#getVariantsForTaxonUsingGET) | **GET** /agr/variants/{taxonId} | Get basic variant records submitted by RGD to AGR by taxonId



## getAffectedGenomicModelsUsingGET

> {String: Object} getAffectedGenomicModelsUsingGET(taxonId)

Get affected genomic models (rat strains with gene alleles) submitted by RGD to AGR by taxonId

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AGRApi();
let taxonId = "taxonId_example"; // String | The taxon ID for species
apiInstance.getAffectedGenomicModelsUsingGET(taxonId, (error, data, response) => {
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
 **taxonId** | **String**| The taxon ID for species | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAllelesForTaxonUsingGET

> {String: Object} getAllelesForTaxonUsingGET(taxonId)

Get gene allele records submitted by RGD to AGR by taxonId

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AGRApi();
let taxonId = "taxonId_example"; // String | The taxon ID for species
apiInstance.getAllelesForTaxonUsingGET(taxonId, (error, data, response) => {
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
 **taxonId** | **String**| The taxon ID for species | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getExpressionForTaxonUsingGET

> {String: Object} getExpressionForTaxonUsingGET(taxonId)

Get expression annotations submitted by RGD to AGR by taxonId

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AGRApi();
let taxonId = "taxonId_example"; // String | The taxon ID for species
apiInstance.getExpressionForTaxonUsingGET(taxonId, (error, data, response) => {
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
 **taxonId** | **String**| The taxon ID for species | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenesForLatestAssemblyUsingGET

> {String: Object} getGenesForLatestAssemblyUsingGET(taxonId)

Get gene records submitted by RGD to AGR by taxonId

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AGRApi();
let taxonId = "taxonId_example"; // String | The taxon ID for species
apiInstance.getGenesForLatestAssemblyUsingGET(taxonId, (error, data, response) => {
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
 **taxonId** | **String**| The taxon ID for species | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPhenotypesForTaxonUsingGET

> {String: Object} getPhenotypesForTaxonUsingGET(taxonId)

Get phenotype annotations submitted by RGD to AGR by taxonId

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AGRApi();
let taxonId = "taxonId_example"; // String | The taxon ID for species
apiInstance.getPhenotypesForTaxonUsingGET(taxonId, (error, data, response) => {
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
 **taxonId** | **String**| The taxon ID for species | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getVariantsForTaxonUsingGET

> {String: Object} getVariantsForTaxonUsingGET(taxonId)

Get basic variant records submitted by RGD to AGR by taxonId

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AGRApi();
let taxonId = "taxonId_example"; // String | The taxon ID for species
apiInstance.getVariantsForTaxonUsingGET(taxonId, (error, data, response) => {
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
 **taxonId** | **String**| The taxon ID for species | 

### Return type

**{String: Object}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

