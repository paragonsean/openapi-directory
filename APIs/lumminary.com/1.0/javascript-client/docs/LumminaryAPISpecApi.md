# LumminaryApi.LumminaryAPISpecApi

All URIs are relative to *http://api.lumminary.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuthorizationsQueue**](LumminaryAPISpecApi.md#getAuthorizationsQueue) | **GET** /products/{productId}/authorizations | 
[**getClientGene**](LumminaryAPISpecApi.md#getClientGene) | **GET** /clients/{clientId}/datasets/{datasetId}/genes/{geneSymbol} | Get gene by symbol
[**getClientSnp**](LumminaryAPISpecApi.md#getClientSnp) | **GET** /clients/{clientId}/datasets/{datasetId}/snps/{snpId} | Get SNP information
[**getClientSnpGroup**](LumminaryAPISpecApi.md#getClientSnpGroup) | **GET** /clients/{clientId}/datasets/{datasetId}/snps/ | 
[**getGene**](LumminaryAPISpecApi.md#getGene) | **GET** /reference/genes/databases/{databaseName}/accessions/{accession} | Generic gene information
[**getProduct**](LumminaryAPISpecApi.md#getProduct) | **GET** /products/{productId} | Get product details
[**getProductAuthorization**](LumminaryAPISpecApi.md#getProductAuthorization) | **GET** /products/{productId}/authorizations/{authorizationId} | 
[**getReferenceChromosome**](LumminaryAPISpecApi.md#getReferenceChromosome) | **GET** /reference/genomes/{genomeBuildAccession}/chromosomes/{chromosomeAccession} | Sequence for a region of the reference genome
[**getReferenceGenome**](LumminaryAPISpecApi.md#getReferenceGenome) | **GET** /reference/genomes/{genomeBuildAccession}/chromosomes | Reference genome metadata
[**getReferenceGenomesGroup**](LumminaryAPISpecApi.md#getReferenceGenomesGroup) | **GET** /reference/genomes/ | Reference genome builds
[**getReferenceSnp**](LumminaryAPISpecApi.md#getReferenceSnp) | **GET** /reference/snps/{snpAccession} | Reference SNP data
[**postAuthorizationResultCredentials**](LumminaryAPISpecApi.md#postAuthorizationResultCredentials) | **POST** /products/{productId}/authorizations/{authorizationId}/credentials | Provide a result for the authorization
[**postAuthorizationResultFile**](LumminaryAPISpecApi.md#postAuthorizationResultFile) | **POST** /products/{productId}/authorizations/{authorizationId}/file | Provide a file result to the authorization, e
[**postClientSnpGroup**](LumminaryAPISpecApi.md#postClientSnpGroup) | **POST** /clients/{clientId}/datasets/{datasetId}/snps/ | Get a large group of SNPs
[**postJwtAuth**](LumminaryAPISpecApi.md#postJwtAuth) | **POST** /auth/jwt | General-purpose authentication
[**postProductAuthorization**](LumminaryAPISpecApi.md#postProductAuthorization) | **POST** /products/{productId}/authorizations/{authorizationId} | Signal that processing is complete, without uploading any result
[**postProductAuthorizationUnfulfillable**](LumminaryAPISpecApi.md#postProductAuthorizationUnfulfillable) | **POST** /products/{productId}/authorizations/{authorizationId}/unfulfillable | Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons



## getAuthorizationsQueue

> [Authorization] getAuthorizationsQueue(productId, opts)



### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let productId = "productId_example"; // String | The UUID of the product
let opts = {
  'seqNumStart': "seqNumStart_example", // String | The first sequence number from which to fetch (the sequence number of the last processed authorization)
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getAuthorizationsQueue(productId, opts, (error, data, response) => {
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
 **productId** | **String**| The UUID of the product | 
 **seqNumStart** | **String**| The first sequence number from which to fetch (the sequence number of the last processed authorization) | [optional] 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**[Authorization]**](Authorization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClientGene

> ClientGene getClientGene(clientId, datasetId, geneSymbol, opts)

Get gene by symbol

Gets A gene by its symbol, which can be found by querying the reference/ resource.  Will return a 404 if a gene exists as a reference, but its genomic coordinates intersect no SNPs in the dataset

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let clientId = "clientId_example"; // String | The UUID of the client
let datasetId = "datasetId_example"; // String | The UUID of one of the client's dataset
let geneSymbol = "geneSymbol_example"; // String | The symbol of a gene to be fetched
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getClientGene(clientId, datasetId, geneSymbol, opts, (error, data, response) => {
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
 **clientId** | **String**| The UUID of the client | 
 **datasetId** | **String**| The UUID of one of the client&#39;s dataset | 
 **geneSymbol** | **String**| The symbol of a gene to be fetched | 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**ClientGene**](ClientGene.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClientSnp

> ClientSNP getClientSnp(clientId, datasetId, snpId, opts)

Get SNP information

Gets SNP information, as provided by the dataset.  If fetching this as an product, the client must have already granted access to the snip (see the &#39;products&#39; group)

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let clientId = "clientId_example"; // String | The UUID of the client
let datasetId = "datasetId_example"; // String | The UUID of one of the client's dataset
let snpId = "snpId_example"; // String | The rsId of a SNP to be fetched
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getClientSnp(clientId, datasetId, snpId, opts, (error, data, response) => {
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
 **clientId** | **String**| The UUID of the client | 
 **datasetId** | **String**| The UUID of one of the client&#39;s dataset | 
 **snpId** | **String**| The rsId of a SNP to be fetched | 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**ClientSNP**](ClientSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClientSnpGroup

> [ClientSNP] getClientSnpGroup(clientId, datasetId, opts)



### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let clientId = "clientId_example"; // String | The UUID of the client
let datasetId = "datasetId_example"; // String | The UUID of one of the client's dataset
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getClientSnpGroup(clientId, datasetId, opts, (error, data, response) => {
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
 **clientId** | **String**| The UUID of the client | 
 **datasetId** | **String**| The UUID of one of the client&#39;s dataset | 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**[ClientSNP]**](ClientSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGene

> PublicGene getGene(databaseName, accession, opts)

Generic gene information

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let databaseName = "databaseName_example"; // String | The name of the database to search. E.g: Genbank
let accession = "accession_example"; // String | The accession within the selected database
let opts = {
  'dbsnpBuild': 149, // Number | The dbSNP build for which to consider snps belonging to the gene. Defaults to 149
  'referenceGenome': "'GRCH37P13'", // String | The reference genome for which gene annotations will be returned. Defaults to GRCh37p13
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getGene(databaseName, accession, opts, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database to search. E.g: Genbank | 
 **accession** | **String**| The accession within the selected database | 
 **dbsnpBuild** | **Number**| The dbSNP build for which to consider snps belonging to the gene. Defaults to 149 | [optional] [default to 149]
 **referenceGenome** | **String**| The reference genome for which gene annotations will be returned. Defaults to GRCh37p13 | [optional] [default to &#39;GRCH37P13&#39;]
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**PublicGene**](PublicGene.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProduct

> Product getProduct(productId, opts)

Get product details

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let productId = "productId_example"; // String | The UUID of the product
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getProduct(productId, opts, (error, data, response) => {
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
 **productId** | **String**| The UUID of the product | 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductAuthorization

> Authorization getProductAuthorization(productId, authorizationId, opts)



### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let productId = "productId_example"; // String | The UUID of the product
let authorizationId = "authorizationId_example"; // String | The UUID of the authorization
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getProductAuthorization(productId, authorizationId, opts, (error, data, response) => {
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
 **productId** | **String**| The UUID of the product | 
 **authorizationId** | **String**| The UUID of the authorization | 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**Authorization**](Authorization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReferenceChromosome

> ReferenceSequence getReferenceChromosome(genomeBuildAccession, chromosomeAccession, rangeStart, rangeStop, opts)

Sequence for a region of the reference genome

Fetch a closed interval of nucleotides on a given chromosome. Includes start and stop positions

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let genomeBuildAccession = "genomeBuildAccession_example"; // String | The accession of the reference genome
let chromosomeAccession = "chromosomeAccession_example"; // String | The accession to the chromosome
let rangeStart = 56; // Number | Location on the chromosome
let rangeStop = 56; // Number | Location on the chromosome
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getReferenceChromosome(genomeBuildAccession, chromosomeAccession, rangeStart, rangeStop, opts, (error, data, response) => {
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
 **genomeBuildAccession** | **String**| The accession of the reference genome | 
 **chromosomeAccession** | **String**| The accession to the chromosome | 
 **rangeStart** | **Number**| Location on the chromosome | 
 **rangeStop** | **Number**| Location on the chromosome | 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**ReferenceSequence**](ReferenceSequence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReferenceGenome

> [ReferenceChromosomeOverview] getReferenceGenome(genomeBuildAccession, opts)

Reference genome metadata

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let genomeBuildAccession = "genomeBuildAccession_example"; // String | 
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getReferenceGenome(genomeBuildAccession, opts, (error, data, response) => {
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
 **genomeBuildAccession** | **String**|  | 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**[ReferenceChromosomeOverview]**](ReferenceChromosomeOverview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReferenceGenomesGroup

> [ReferenceGenomeOverview] getReferenceGenomesGroup(opts)

Reference genome builds

Lists reference genome builds that are available

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getReferenceGenomesGroup(opts, (error, data, response) => {
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
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**[ReferenceGenomeOverview]**](ReferenceGenomeOverview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReferenceSnp

> PublicSNP getReferenceSnp(snpAccession, opts)

Reference SNP data

Get reference SNP information, from dbSNP

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let snpAccession = "snpAccession_example"; // String | The rsId of the SNP
let opts = {
  'dbsnpVersion': 149, // Number | The dbSNP build. Defaults to 149
  'grchVersion': "'GRCH37P13'", // String | The GRCh build on which to place snips. Defaults to GRCh37p13
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.getReferenceSnp(snpAccession, opts, (error, data, response) => {
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
 **snpAccession** | **String**| The rsId of the SNP | 
 **dbsnpVersion** | **Number**| The dbSNP build. Defaults to 149 | [optional] [default to 149]
 **grchVersion** | **String**| The GRCh build on which to place snips. Defaults to GRCh37p13 | [optional] [default to &#39;GRCH37P13&#39;]
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**PublicSNP**](PublicSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postAuthorizationResultCredentials

> ReportCredentials postAuthorizationResultCredentials(productId, authorizationId, opts)

Provide a result for the authorization

These can be log-in credentials for a website where the result is available

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let productId = "productId_example"; // String | The UUID of the product
let authorizationId = "authorizationId_example"; // String | The UUID of the authorization
let opts = {
  'xFields': "xFields_example", // String | An optional fields mask
  'credentialsUsername': "credentialsUsername_example", // String | Credentials for accessing the result. Includes password, username and url
  'credentialsPassword': "credentialsPassword_example", // String | Credentials for accessing the result. Includes password, username and url
  'reportUrl': "reportUrl_example" // String | Credentials for accessing the result. Includes password, username and url
};
apiInstance.postAuthorizationResultCredentials(productId, authorizationId, opts, (error, data, response) => {
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
 **productId** | **String**| The UUID of the product | 
 **authorizationId** | **String**| The UUID of the authorization | 
 **xFields** | **String**| An optional fields mask | [optional] 
 **credentialsUsername** | **String**| Credentials for accessing the result. Includes password, username and url | [optional] 
 **credentialsPassword** | **String**| Credentials for accessing the result. Includes password, username and url | [optional] 
 **reportUrl** | **String**| Credentials for accessing the result. Includes password, username and url | [optional] 

### Return type

[**ReportCredentials**](ReportCredentials.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## postAuthorizationResultFile

> ReportFile postAuthorizationResultFile(productId, authorizationId, opts)

Provide a file result to the authorization, e

g. a pdf report

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let productId = "productId_example"; // String | The UUID of the product
let authorizationId = "authorizationId_example"; // String | The UUID of the authorization
let opts = {
  'originalFilename': "originalFilename_example", // String | Optional original filename for the report. If not provided, the filename of uploaded file will be used
  'xFields': "xFields_example", // String | An optional fields mask
  'fileReport': "/path/to/file" // File | A binary file (e.g. pdf) that contains the result of the authorization
};
apiInstance.postAuthorizationResultFile(productId, authorizationId, opts, (error, data, response) => {
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
 **productId** | **String**| The UUID of the product | 
 **authorizationId** | **String**| The UUID of the authorization | 
 **originalFilename** | **String**| Optional original filename for the report. If not provided, the filename of uploaded file will be used | [optional] 
 **xFields** | **String**| An optional fields mask | [optional] 
 **fileReport** | **File**| A binary file (e.g. pdf) that contains the result of the authorization | [optional] 

### Return type

[**ReportFile**](ReportFile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postClientSnpGroup

> [ClientSNP] postClientSnpGroup(clientId, datasetId, snps, opts)

Get a large group of SNPs

SNPs that are not present in the dataset are ignored, 404 is returned only if the dataset/client does not exist

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let clientId = "clientId_example"; // String | The UUID of the client
let datasetId = "datasetId_example"; // String | The UUID of one of the client's dataset
let snps = "snps_example"; // String | JSON-encoded list of snps to be fetched
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.postClientSnpGroup(clientId, datasetId, snps, opts, (error, data, response) => {
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
 **clientId** | **String**| The UUID of the client | 
 **datasetId** | **String**| The UUID of one of the client&#39;s dataset | 
 **snps** | **String**| JSON-encoded list of snps to be fetched | 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**[ClientSNP]**](ClientSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## postJwtAuth

> JavascriptWebToken postJwtAuth(username, password, role, opts)

General-purpose authentication

## Note: * The JWT tokens returned should be passed to any resource that requires authentication, in the Authentication header, in the format &#x60;Bearer: your-token-here&#x60; * Only JWT authentication tokens are provided (no refresh tokens). These tokens are valid for 30 seconds from the moment they were issued

### Example

```javascript
import LumminaryApi from 'lumminary_api';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let username = "username_example"; // String | The email for a Client, or the API for a partner product
let password = "password_example"; // String | The passowrd for a Client, or the API key for a service
let role = "role_example"; // String | The role for which authentication will be made. Value : role_product
let opts = {
  'xFields': "xFields_example" // String | An optional fields mask
};
apiInstance.postJwtAuth(username, password, role, opts, (error, data, response) => {
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
 **username** | **String**| The email for a Client, or the API for a partner product | 
 **password** | **String**| The passowrd for a Client, or the API key for a service | 
 **role** | **String**| The role for which authentication will be made. Value : role_product | 
 **xFields** | **String**| An optional fields mask | [optional] 

### Return type

[**JavascriptWebToken**](JavascriptWebToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## postProductAuthorization

> postProductAuthorization(productId, authorizationId)

Signal that processing is complete, without uploading any result

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let productId = "productId_example"; // String | The UUID of the product
let authorizationId = "authorizationId_example"; // String | The UUID of the authorization
apiInstance.postProductAuthorization(productId, authorizationId, (error, data, response) => {
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
 **productId** | **String**| The UUID of the product | 
 **authorizationId** | **String**| The UUID of the authorization | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postProductAuthorizationUnfulfillable

> postProductAuthorizationUnfulfillable(productId, authorizationId)

Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons

### Example

```javascript
import LumminaryApi from 'lumminary_api';
let defaultClient = LumminaryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new LumminaryApi.LumminaryAPISpecApi();
let productId = "productId_example"; // String | The UUID of the product
let authorizationId = "authorizationId_example"; // String | The UUID of the authorization
apiInstance.postProductAuthorizationUnfulfillable(productId, authorizationId, (error, data, response) => {
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
 **productId** | **String**| The UUID of the product | 
 **authorizationId** | **String**| The UUID of the authorization | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

