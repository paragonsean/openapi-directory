# RatGenomeDatabaseRestApi.GeneApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllAnnotatedGenesUsingGET**](GeneApi.md#getAllAnnotatedGenesUsingGET) | **GET** /genes/annotation/{accId} | Return a list of genes annotated to an ontology term
[**getAnnotatedGenesUsingPOST**](GeneApi.md#getAnnotatedGenesUsingPOST) | **POST** /genes/annotation | Return a list of genes annotated to an ontology term
[**getGeneAllelesUsingGET**](GeneApi.md#getGeneAllelesUsingGET) | **GET** /genes/allele/{rgdId} | Return a list of gene alleles
[**getGeneByMapKeyUsingGET**](GeneApi.md#getGeneByMapKeyUsingGET) | **GET** /genes/map/{mapKey} | Return a list of all genes with position information for an assembly
[**getGeneByRgdIdUsingGET**](GeneApi.md#getGeneByRgdIdUsingGET) | **GET** /genes/{rgdId} | Get a gene record by RGD ID
[**getGeneBySymbolUsingGET**](GeneApi.md#getGeneBySymbolUsingGET) | **GET** /genes/{symbol}/{speciesTypeKey} | Get a gene record by symbol and species type key
[**getGeneOrthologsUsingGET**](GeneApi.md#getGeneOrthologsUsingGET) | **GET** /genes/orthologs/{rgdId} | Return a list of gene orthologs
[**getGenesAnnotatedUsingGET**](GeneApi.md#getGenesAnnotatedUsingGET) | **GET** /genes/annotation/{accId}/{speciesTypeKey} | Return a list of genes annotated to an ontology term
[**getGenesByAffyIdUsingGET**](GeneApi.md#getGenesByAffyIdUsingGET) | **GET** /genes/affyId/{affyId}/{speciesTypeKey} | Return a list of genes for an affymetrix ID
[**getGenesByAliasSymbolUsingGET**](GeneApi.md#getGenesByAliasSymbolUsingGET) | **GET** /genes/alias/{aliasSymbol}/{speciesTypeKey} | Return a list of genes for an alias and species
[**getGenesByKeywordUsingGET**](GeneApi.md#getGenesByKeywordUsingGET) | **GET** /genes/keyword/{keyword}/{speciesTypeKey} | Return a list of genes by keyword and species type key
[**getGenesByPositionUsingGET**](GeneApi.md#getGenesByPositionUsingGET) | **GET** /genes/{chr}/{start}/{stop}/{mapKey} | Return a list of genes position and map key
[**getGenesBySpeciesUsingGET**](GeneApi.md#getGenesBySpeciesUsingGET) | **GET** /genes/species/{speciesTypeKey} | Return a list of all genes for a species in RGD
[**getGenesInRegionUsingGET**](GeneApi.md#getGenesInRegionUsingGET) | **GET** /genes/region/{chr}/{start}/{stop}/{mapKey} | Return a list of genes in region
[**getMappedGenesByPositionUsingGET**](GeneApi.md#getMappedGenesByPositionUsingGET) | **GET** /genes/mapped/{chr}/{start}/{stop}/{mapKey} | Return a list of genes position and map key
[**getOrthologsByListUsingPOST**](GeneApi.md#getOrthologsByListUsingPOST) | **POST** /genes/orthologs | Return a list of gene orthologs



## getAllAnnotatedGenesUsingGET

> [Gene] getAllAnnotatedGenesUsingGET(accId)

Return a list of genes annotated to an ontology term

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let accId = "accId_example"; // String | Accesstion ID
apiInstance.getAllAnnotatedGenesUsingGET(accId, (error, data, response) => {
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
 **accId** | **String**| Accesstion ID | 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAnnotatedGenesUsingPOST

> [Gene] getAnnotatedGenesUsingPOST(opts)

Return a list of genes annotated to an ontology term

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let opts = {
  'annotatedGeneRequest': new RatGenomeDatabaseRestApi.AnnotatedGeneRequest() // AnnotatedGeneRequest | data
};
apiInstance.getAnnotatedGenesUsingPOST(opts, (error, data, response) => {
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
 **annotatedGeneRequest** | [**AnnotatedGeneRequest**](AnnotatedGeneRequest.md)| data | [optional] 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getGeneAllelesUsingGET

> [Gene] getGeneAllelesUsingGET(rgdId)

Return a list of gene alleles

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let rgdId = 56; // Number | RGD ID of gene
apiInstance.getGeneAllelesUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID of gene | 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGeneByMapKeyUsingGET

> [MappedGene] getGeneByMapKeyUsingGET(mapKey)

Return a list of all genes with position information for an assembly

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let mapKey = 56; // Number | A list of RGD assembly map keys can be found in the lookup service
apiInstance.getGeneByMapKeyUsingGET(mapKey, (error, data, response) => {
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
 **mapKey** | **Number**| A list of RGD assembly map keys can be found in the lookup service | 

### Return type

[**[MappedGene]**](MappedGene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGeneByRgdIdUsingGET

> Gene getGeneByRgdIdUsingGET(rgdId)

Get a gene record by RGD ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let rgdId = 56; // Number | The RGD ID of a Gene in RGD
apiInstance.getGeneByRgdIdUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| The RGD ID of a Gene in RGD | 

### Return type

[**Gene**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGeneBySymbolUsingGET

> Gene getGeneBySymbolUsingGET(symbol, speciesTypeKey)

Get a gene record by symbol and species type key

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let symbol = "symbol_example"; // String | Gene Symbol
let speciesTypeKey = 56; // Number | Species type key.  A list of species type keys can be found in the lookup service
apiInstance.getGeneBySymbolUsingGET(symbol, speciesTypeKey, (error, data, response) => {
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
 **symbol** | **String**| Gene Symbol | 
 **speciesTypeKey** | **Number**| Species type key.  A list of species type keys can be found in the lookup service | 

### Return type

[**Gene**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGeneOrthologsUsingGET

> [Gene] getGeneOrthologsUsingGET(rgdId)

Return a list of gene orthologs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let rgdId = 56; // Number | RGD ID of a gene
apiInstance.getGeneOrthologsUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID of a gene | 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenesAnnotatedUsingGET

> [Gene] getGenesAnnotatedUsingGET(accId, speciesTypeKey)

Return a list of genes annotated to an ontology term

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let accId = "accId_example"; // String | Ontology term accession ID
let speciesTypeKey = 56; // Number | Species type key.  A list of species type keys can be found in the lookup service
apiInstance.getGenesAnnotatedUsingGET(accId, speciesTypeKey, (error, data, response) => {
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
 **accId** | **String**| Ontology term accession ID | 
 **speciesTypeKey** | **Number**| Species type key.  A list of species type keys can be found in the lookup service | 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenesByAffyIdUsingGET

> [Gene] getGenesByAffyIdUsingGET(affyId, speciesTypeKey)

Return a list of genes for an affymetrix ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let affyId = "affyId_example"; // String | Affymetrix ID
let speciesTypeKey = 56; // Number | A list of RGD species type keys can be found in the lookup service
apiInstance.getGenesByAffyIdUsingGET(affyId, speciesTypeKey, (error, data, response) => {
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
 **affyId** | **String**| Affymetrix ID | 
 **speciesTypeKey** | **Number**| A list of RGD species type keys can be found in the lookup service | 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenesByAliasSymbolUsingGET

> [Gene] getGenesByAliasSymbolUsingGET(aliasSymbol, speciesTypeKey)

Return a list of genes for an alias and species

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let aliasSymbol = "aliasSymbol_example"; // String | Gene alias symbol
let speciesTypeKey = 56; // Number | A list of RGD species type keys can be found in the lookup service
apiInstance.getGenesByAliasSymbolUsingGET(aliasSymbol, speciesTypeKey, (error, data, response) => {
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
 **aliasSymbol** | **String**| Gene alias symbol | 
 **speciesTypeKey** | **Number**| A list of RGD species type keys can be found in the lookup service | 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenesByKeywordUsingGET

> [Gene] getGenesByKeywordUsingGET(keyword, speciesTypeKey)

Return a list of genes by keyword and species type key

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let keyword = "keyword_example"; // String | Search keyword
let speciesTypeKey = 56; // Number | Species type key.  A list of species type keys can be found in the lookup service
apiInstance.getGenesByKeywordUsingGET(keyword, speciesTypeKey, (error, data, response) => {
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
 **keyword** | **String**| Search keyword | 
 **speciesTypeKey** | **Number**| Species type key.  A list of species type keys can be found in the lookup service | 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenesByPositionUsingGET

> [Gene] getGenesByPositionUsingGET(chr, start, stop, mapKey)

Return a list of genes position and map key

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let chr = "chr_example"; // String | Chromosome
let start = 789; // Number | Start Position
let stop = 789; // Number | Stop Position
let mapKey = 56; // Number | A list of RGD assembly map keys can be found in the lookup service
apiInstance.getGenesByPositionUsingGET(chr, start, stop, mapKey, (error, data, response) => {
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
 **chr** | **String**| Chromosome | 
 **start** | **Number**| Start Position | 
 **stop** | **Number**| Stop Position | 
 **mapKey** | **Number**| A list of RGD assembly map keys can be found in the lookup service | 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenesBySpeciesUsingGET

> [Gene] getGenesBySpeciesUsingGET(speciesTypeKey)

Return a list of all genes for a species in RGD

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let speciesTypeKey = 56; // Number | A list of RGD species type keys can be found in the lookup service
apiInstance.getGenesBySpeciesUsingGET(speciesTypeKey, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| A list of RGD species type keys can be found in the lookup service | 

### Return type

[**[Gene]**](Gene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenesInRegionUsingGET

> [MappedGenePosition] getGenesInRegionUsingGET(chr, start, stop, mapKey)

Return a list of genes in region

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let chr = "chr_example"; // String | Chromosome
let start = 789; // Number | Start Position
let stop = 789; // Number | Stop Position
let mapKey = 56; // Number | A list of RGD assembly map keys can be found in the lookup service
apiInstance.getGenesInRegionUsingGET(chr, start, stop, mapKey, (error, data, response) => {
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
 **chr** | **String**| Chromosome | 
 **start** | **Number**| Start Position | 
 **stop** | **Number**| Stop Position | 
 **mapKey** | **Number**| A list of RGD assembly map keys can be found in the lookup service | 

### Return type

[**[MappedGenePosition]**](MappedGenePosition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getMappedGenesByPositionUsingGET

> [MappedGene] getMappedGenesByPositionUsingGET(chr, start, stop, mapKey)

Return a list of genes position and map key

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let chr = "chr_example"; // String | Chromosome
let start = 789; // Number | Start Position
let stop = 789; // Number | Stop Position
let mapKey = 56; // Number | A list of RGD assembly map keys can be found in the lookup service
apiInstance.getMappedGenesByPositionUsingGET(chr, start, stop, mapKey, (error, data, response) => {
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
 **chr** | **String**| Chromosome | 
 **start** | **Number**| Start Position | 
 **stop** | **Number**| Stop Position | 
 **mapKey** | **Number**| A list of RGD assembly map keys can be found in the lookup service | 

### Return type

[**[MappedGene]**](MappedGene.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getOrthologsByListUsingPOST

> {String: [Gene]} getOrthologsByListUsingPOST(orthologRequest)

Return a list of gene orthologs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.GeneApi();
let orthologRequest = new RatGenomeDatabaseRestApi.OrthologRequest(); // OrthologRequest | orthologRequest
apiInstance.getOrthologsByListUsingPOST(orthologRequest, (error, data, response) => {
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
 **orthologRequest** | [**OrthologRequest**](OrthologRequest.md)| orthologRequest | 

### Return type

**{String: [Gene]}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

