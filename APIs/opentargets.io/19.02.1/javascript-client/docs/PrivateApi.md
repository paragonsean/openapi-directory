# OpenTargetsPlatformRestApi.PrivateApi

All URIs are relative to *http://platform-api.opentargets.io/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getApiDocs**](PrivateApi.md#getApiDocs) | **GET** /platform/docs | Browse API documentation
[**getApiSwaggerUI**](PrivateApi.md#getApiSwaggerUI) | **GET** /platform/docs/swagger-ui | Browse interactive API documentation
[**getAutocomplete**](PrivateApi.md#getAutocomplete) | **GET** /platform/private/autocomplete | Get &#x60;autocomplete&#x60; objects.
[**getDiseaseById**](PrivateApi.md#getDiseaseById) | **GET** /platform/private/disease/{disease} | Find information about a disease
[**getDrugByID**](PrivateApi.md#getDrugByID) | **GET** /platform/private/drug/{DRUG_ID} | Get drug by ID
[**getECObyID**](PrivateApi.md#getECObyID) | **GET** /platform/private/eco/{ECO_ID} | Get evidence code by ID
[**getQuickSearch**](PrivateApi.md#getQuickSearch) | **GET** /platform/private/quicksearch | Search most relevant results
[**getRelationByEFOID**](PrivateApi.md#getRelationByEFOID) | **GET** /platform/private/relation/disease/{disease} | Find related entities by disease
[**getRelationByENSGID**](PrivateApi.md#getRelationByENSGID) | **GET** /platform/private/relation/target/{target} | Find related entities by target
[**getSwagger**](PrivateApi.md#getSwagger) | **GET** /platform/swagger | Get OpenAPI schema
[**getTargetByENSGID**](PrivateApi.md#getTargetByENSGID) | **GET** /platform/private/target/{target} | Find information about a target
[**getTargetExpressionByENSGID**](PrivateApi.md#getTargetExpressionByENSGID) | **GET** /platform/private/target/expression | Query expression levels
[**postBestHitSearch**](PrivateApi.md#postBestHitSearch) | **POST** /platform/private/besthitsearch | Find the best hit
[**postDiseaseById**](PrivateApi.md#postDiseaseById) | **POST** /platform/private/disease | Find information about a list of diseases
[**postEnrichmentTarget**](PrivateApi.md#postEnrichmentTarget) | **POST** /platform/private/enrichment/targets | Enrichment analysis
[**postRelation**](PrivateApi.md#postRelation) | **POST** /platform/private/relation | Find related entities
[**postTargetByENSGID**](PrivateApi.md#postTargetByENSGID) | **POST** /platform/private/target | Find information about a list of targets
[**postTargetExpressionByENSGID**](PrivateApi.md#postTargetExpressionByENSGID) | **POST** /platform/private/target/expression | Batch query expression levels



## getApiDocs

> getApiDocs()

Browse API documentation

Access api docs as served by Redoc

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
apiInstance.getApiDocs((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getApiSwaggerUI

> getApiSwaggerUI()

Browse interactive API documentation

Interactive API docs using swagger-ui

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
apiInstance.getApiSwaggerUI((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAutocomplete

> getAutocomplete(q, opts)

Get &#x60;autocomplete&#x60; objects.

Search for the closest term to autocomplete in the search box. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let q = "q_example"; // String | A full text query.
let opts = {
  'size': "size_example" // String | Maximum amount of results to return. Defaults to 5.
};
apiInstance.getAutocomplete(q, opts, (error, data, response) => {
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
 **q** | **String**| A full text query. | 
 **size** | **String**| Maximum amount of results to return. Defaults to 5. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDiseaseById

> getDiseaseById(disease)

Find information about a disease

Get &#x60;disease&#x60; objects. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let disease = "disease_example"; // String | An EFO identifier.
apiInstance.getDiseaseById(disease, (error, data, response) => {
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
 **disease** | **String**| An EFO identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDrugByID

> getDrugByID(drugId, DRUG_ID)

Get drug by ID

Get &#x60;drug&#x60; objects. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let drugId = "drugId_example"; // String | An ID in the drug index.
let DRUG_ID = "DRUG_ID_example"; // String | Automatically added
apiInstance.getDrugByID(drugId, DRUG_ID, (error, data, response) => {
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
 **drugId** | **String**| An ID in the drug index. | 
 **DRUG_ID** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getECObyID

> getECObyID(ECO_ID)

Get evidence code by ID

Get &#x60;ECO&#x60; objects. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let ECO_ID = "ECO_ID_example"; // String | An [evidence code ontology](http://www.ebi.ac.uk/ols/v2/browse.do?ontName=ECO) ID.
apiInstance.getECObyID(ECO_ID, (error, data, response) => {
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
 **ECO_ID** | **String**| An [evidence code ontology](http://www.ebi.ac.uk/ols/v2/browse.do?ontName&#x3D;ECO) ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getQuickSearch

> getQuickSearch(q, opts)

Search most relevant results

Get &#x60;search-result&#x60; objects. Enables search bar functionality. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let q = "q_example"; // String | A full text query.
let opts = {
  'size': "size_example" // String | Maximum amount of results to return. Defaults to 5.
};
apiInstance.getQuickSearch(q, opts, (error, data, response) => {
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
 **q** | **String**| A full text query. | 
 **size** | **String**| Maximum amount of results to return. Defaults to 5. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRelationByEFOID

> getRelationByEFOID(disease)

Find related entities by disease

Get &#x60;relation&#x60; objects starting from diseases. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let disease = "disease_example"; // String | An EFO gene identifier.
apiInstance.getRelationByEFOID(disease, (error, data, response) => {
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
 **disease** | **String**| An EFO gene identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRelationByENSGID

> getRelationByENSGID(target)

Find related entities by target

Get &#x60;relation&#x60; objects starting from diseases. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let target = "target_example"; // String | An Ensembl gene identifier.
apiInstance.getRelationByENSGID(target, (error, data, response) => {
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
 **target** | **String**| An Ensembl gene identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSwagger

> getSwagger()

Get OpenAPI schema

Get swagger.yaml specs for the API

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
apiInstance.getSwagger((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTargetByENSGID

> getTargetByENSGID(target)

Find information about a target

Get &#x60;target&#x60; objects. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let target = "target_example"; // String | An Ensembl gene ID for the target of interest.
apiInstance.getTargetByENSGID(target, (error, data, response) => {
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
 **target** | **String**| An Ensembl gene ID for the target of interest. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTargetExpressionByENSGID

> getTargetExpressionByENSGID(gene)

Query expression levels

Get &#x60;gene-expression&#x60; objects. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let gene = "gene_example"; // String | An Ensembl gene identifier.
apiInstance.getTargetExpressionByENSGID(gene, (error, data, response) => {
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
 **gene** | **String**| An Ensembl gene identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postBestHitSearch

> postBestHitSearch(body)

Find the best hit

Fire the search method for multiple strings 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let body = "body_example"; // String | list of strings to search for
apiInstance.postBestHitSearch(body, (error, data, response) => {
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
 **body** | **String**| list of strings to search for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postDiseaseById

> postDiseaseById(body)

Find information about a list of diseases

Get &#x60;disease&#x60; objects. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let body = "body_example"; // String | An EFO identifier.
apiInstance.postDiseaseById(body, (error, data, response) => {
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
 **body** | **String**| An EFO identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postEnrichmentTarget

> postEnrichmentTarget(body)

Enrichment analysis

Returns an enrichment analysis for a list of targets passed in the body 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let body = "body_example"; // String | IDs of the targets to do the enrichment analysis for.
apiInstance.postEnrichmentTarget(body, (error, data, response) => {
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
 **body** | **String**| IDs of the targets to do the enrichment analysis for. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postRelation

> postRelation(body)

Find related entities

Get &#x60;relation&#x60; objects. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let body = "body_example"; // String | An Ensembl gene identifier.
apiInstance.postRelation(body, (error, data, response) => {
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
 **body** | **String**| An Ensembl gene identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postTargetByENSGID

> postTargetByENSGID(body)

Find information about a list of targets

Get &#x60;target&#x60; objects. Used for the target profile page. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let body = "body_example"; // String | An Ensembl gene identifier.
apiInstance.postTargetByENSGID(body, (error, data, response) => {
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
 **body** | **String**| An Ensembl gene identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postTargetExpressionByENSGID

> postTargetExpressionByENSGID(body)

Batch query expression levels

Get &#x60;gene-expression&#x60; objects. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.PrivateApi();
let body = "body_example"; // String | An Ensembl gene identifier.
apiInstance.postTargetExpressionByENSGID(body, (error, data, response) => {
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
 **body** | **String**| An Ensembl gene identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

