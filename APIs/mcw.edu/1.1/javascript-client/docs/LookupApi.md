# RatGenomeDatabaseRestApi.LookupApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEnsemblGeneMappingUsingGET**](LookupApi.md#getEnsemblGeneMappingUsingGET) | **GET** /lookup/id/map/EnsemblGene/{rgdId} | Translate an RGD ID to an Ensembl Gene  ID
[**getEnsemblGeneMappingUsingPOST**](LookupApi.md#getEnsemblGeneMappingUsingPOST) | **POST** /lookup/id/map/EnsemblGene | Translate RGD IDs to Ensembl Gene IDs
[**getEnsemblProteinMappingUsingGET**](LookupApi.md#getEnsemblProteinMappingUsingGET) | **GET** /lookup/id/map/EnsemblProtein/{rgdId} | Translate an RGD ID to an Ensembl Protein ID
[**getEnsemblProteinMappingUsingPOST**](LookupApi.md#getEnsemblProteinMappingUsingPOST) | **POST** /lookup/id/map/EnsemblProtein | Translate RGD IDs to Ensembl Protein IDs
[**getEnsemblTranscriptMappingUsingGET**](LookupApi.md#getEnsemblTranscriptMappingUsingGET) | **GET** /lookup/id/map/EnsemblTranscript/{rgdId} | Translate an RGD ID to an Ensembl Transcript ID
[**getEnsemblTranscriptMappingUsingPOST**](LookupApi.md#getEnsemblTranscriptMappingUsingPOST) | **POST** /lookup/id/map/EnsemblTranscript | Translate RGD IDs to Ensembl Transcript IDs
[**getGTEXMappingUsingGET**](LookupApi.md#getGTEXMappingUsingGET) | **GET** /lookup/id/map/GTEx/{rgdId} | Translate an RGD ID to an GTEx ID
[**getGTEXMappingUsingPOST**](LookupApi.md#getGTEXMappingUsingPOST) | **POST** /lookup/id/map/GTEx | Translate RGD IDs to GTEx IDs
[**getGenBankNucleotideMappingUsingGET**](LookupApi.md#getGenBankNucleotideMappingUsingGET) | **GET** /lookup/id/map/GenBankNucleotide/{rgdId} | Translate an RGD ID to a GenBank Nucleotide ID
[**getGenBankNucleotideMappingUsingPOST**](LookupApi.md#getGenBankNucleotideMappingUsingPOST) | **POST** /lookup/id/map/GenBankNucleotide | Translate RGD IDs to GenBank Nucleotide IDs
[**getGenBankProteinMappingUsingGET**](LookupApi.md#getGenBankProteinMappingUsingGET) | **GET** /lookup/id/map/GenBankProtein/{rgdId} | Translate an RGD ID to a GenBank Protein ID
[**getGenBankProteinMappingUsingPOST**](LookupApi.md#getGenBankProteinMappingUsingPOST) | **POST** /lookup/id/map/GenBankProtein | Translate RGD IDs to GenBank Protein IDs
[**getGeneTypesUsingGET**](LookupApi.md#getGeneTypesUsingGET) | **GET** /lookup/geneTypes | Returns a list of gene types avialable in RGD
[**getHGNCMappingUsingGET**](LookupApi.md#getHGNCMappingUsingGET) | **GET** /lookup/id/map/HGNC/{rgdId} | Translate an RGD ID to an HGNC ID
[**getHGNCMappingUsingPOST**](LookupApi.md#getHGNCMappingUsingPOST) | **POST** /lookup/id/map/HGNC | Translate RGD IDs to HGNC IDs
[**getMGIMappingUsingGET**](LookupApi.md#getMGIMappingUsingGET) | **GET** /lookup/id/map/MGI/{rgdId} | Translate an RGD ID to an MGI ID
[**getMGIMappingUsingPOST**](LookupApi.md#getMGIMappingUsingPOST) | **POST** /lookup/id/map/MGI | Translate RGD IDs to MGI IDs
[**getMapsUsingGET**](LookupApi.md#getMapsUsingGET) | **GET** /lookup/maps/{speciesTypeKey} | Return a list assembly maps for a species
[**getMapsUsingGET1**](LookupApi.md#getMapsUsingGET1) | **GET** /lookup/standardUnit/{accId} | Return a standardUnit for an ontology if it exists
[**getNCBIGeneMappingUsingGET**](LookupApi.md#getNCBIGeneMappingUsingGET) | **GET** /lookup/id/map/NCBIGene/{rgdId} | Translate an RGD ID to an NCBI Gene ID
[**getNCBIGeneMappingUsingPOST**](LookupApi.md#getNCBIGeneMappingUsingPOST) | **POST** /lookup/id/map/NCBIGene | Translate RGD IDs to NCBI Gene IDs
[**getSpeciesTypesUsingGET**](LookupApi.md#getSpeciesTypesUsingGET) | **GET** /lookup/speciesTypeKeys | Return a Map of species type keys available in RGD
[**getUniProtMappingUsingGET**](LookupApi.md#getUniProtMappingUsingGET) | **GET** /lookup/id/map/UniProt/{rgdId} | Translate an RGD ID to a UniProt ID
[**getUniProtMappingUsingPOST**](LookupApi.md#getUniProtMappingUsingPOST) | **POST** /lookup/id/map/UniProt | Translate RGD IDs to UniProt IDs



## getEnsemblGeneMappingUsingGET

> {String: String} getEnsemblGeneMappingUsingGET(rgdId)

Translate an RGD ID to an Ensembl Gene  ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getEnsemblGeneMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getEnsemblGeneMappingUsingPOST

> {String: String} getEnsemblGeneMappingUsingPOST(opts)

Translate RGD IDs to Ensembl Gene IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getEnsemblGeneMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getEnsemblProteinMappingUsingGET

> {String: String} getEnsemblProteinMappingUsingGET(rgdId)

Translate an RGD ID to an Ensembl Protein ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getEnsemblProteinMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getEnsemblProteinMappingUsingPOST

> {String: String} getEnsemblProteinMappingUsingPOST(opts)

Translate RGD IDs to Ensembl Protein IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getEnsemblProteinMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getEnsemblTranscriptMappingUsingGET

> {String: String} getEnsemblTranscriptMappingUsingGET(rgdId)

Translate an RGD ID to an Ensembl Transcript ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getEnsemblTranscriptMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getEnsemblTranscriptMappingUsingPOST

> {String: String} getEnsemblTranscriptMappingUsingPOST(opts)

Translate RGD IDs to Ensembl Transcript IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getEnsemblTranscriptMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getGTEXMappingUsingGET

> {String: String} getGTEXMappingUsingGET(rgdId)

Translate an RGD ID to an GTEx ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getGTEXMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGTEXMappingUsingPOST

> {String: String} getGTEXMappingUsingPOST(opts)

Translate RGD IDs to GTEx IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getGTEXMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getGenBankNucleotideMappingUsingGET

> {String: String} getGenBankNucleotideMappingUsingGET(rgdId)

Translate an RGD ID to a GenBank Nucleotide ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getGenBankNucleotideMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenBankNucleotideMappingUsingPOST

> {String: String} getGenBankNucleotideMappingUsingPOST(opts)

Translate RGD IDs to GenBank Nucleotide IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getGenBankNucleotideMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getGenBankProteinMappingUsingGET

> {String: String} getGenBankProteinMappingUsingGET(rgdId)

Translate an RGD ID to a GenBank Protein ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getGenBankProteinMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGenBankProteinMappingUsingPOST

> {String: String} getGenBankProteinMappingUsingPOST(opts)

Translate RGD IDs to GenBank Protein IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getGenBankProteinMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getGeneTypesUsingGET

> [String] getGeneTypesUsingGET()

Returns a list of gene types avialable in RGD

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
apiInstance.getGeneTypesUsingGET((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getHGNCMappingUsingGET

> {String: String} getHGNCMappingUsingGET(rgdId)

Translate an RGD ID to an HGNC ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getHGNCMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getHGNCMappingUsingPOST

> {String: String} getHGNCMappingUsingPOST(opts)

Translate RGD IDs to HGNC IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getHGNCMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getMGIMappingUsingGET

> {String: String} getMGIMappingUsingGET(rgdId)

Translate an RGD ID to an MGI ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getMGIMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getMGIMappingUsingPOST

> {String: String} getMGIMappingUsingPOST(opts)

Translate RGD IDs to MGI IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getMGIMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getMapsUsingGET

> [Map] getMapsUsingGET(speciesTypeKey)

Return a list assembly maps for a species

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let speciesTypeKey = 56; // Number | RGD species type key. A full list of keys is available throught the lookup service.  1=human, 2=mouse, 3=rat,ect
apiInstance.getMapsUsingGET(speciesTypeKey, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| RGD species type key. A full list of keys is available throught the lookup service.  1&#x3D;human, 2&#x3D;mouse, 3&#x3D;rat,ect | 

### Return type

[**[Map]**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getMapsUsingGET1

> String getMapsUsingGET1(accId)

Return a standardUnit for an ontology if it exists

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let accId = "accId_example"; // String | RGD term acc
apiInstance.getMapsUsingGET1(accId, (error, data, response) => {
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
 **accId** | **String**| RGD term acc | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getNCBIGeneMappingUsingGET

> {String: String} getNCBIGeneMappingUsingGET(rgdId)

Translate an RGD ID to an NCBI Gene ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getNCBIGeneMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getNCBIGeneMappingUsingPOST

> {String: String} getNCBIGeneMappingUsingPOST(opts)

Translate RGD IDs to NCBI Gene IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getNCBIGeneMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getSpeciesTypesUsingGET

> Object getSpeciesTypesUsingGET()

Return a Map of species type keys available in RGD

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
apiInstance.getSpeciesTypesUsingGET((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getUniProtMappingUsingGET

> {String: String} getUniProtMappingUsingGET(rgdId)

Translate an RGD ID to a UniProt ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getUniProtMappingUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getUniProtMappingUsingPOST

> {String: String} getUniProtMappingUsingPOST(opts)

Translate RGD IDs to UniProt IDs

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.LookupApi();
let opts = {
  'rGDIDListRequest': new RatGenomeDatabaseRestApi.RGDIDListRequest() // RGDIDListRequest | data
};
apiInstance.getUniProtMappingUsingPOST(opts, (error, data, response) => {
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
 **rGDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

