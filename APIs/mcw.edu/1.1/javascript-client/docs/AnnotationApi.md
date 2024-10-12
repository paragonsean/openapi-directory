# RatGenomeDatabaseRestApi.AnnotationApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAnnotationCountByAccIdAndObjectTypeUsingGET**](AnnotationApi.md#getAnnotationCountByAccIdAndObjectTypeUsingGET) | **GET** /annotations/count/{accId}/{speciesTypeKey}/{includeChildren}/{objectType} | Returns annotation count for ontology accession ID and object type
[**getAnnotationCountByAccIdAndSpeciesUsingGET**](AnnotationApi.md#getAnnotationCountByAccIdAndSpeciesUsingGET) | **GET** /annotations/count/{accId}/{speciesTypeKey}/{includeChildren} | Returns annotation count for ontology accession ID and speicies
[**getAnnotationCountByAccIdUsingGET**](AnnotationApi.md#getAnnotationCountByAccIdUsingGET) | **GET** /annotations/count/{accId}/{includeChildren} | Returns annotation count for ontology accession ID
[**getAnnotationsByAccIdAndRgdIdUsingGET**](AnnotationApi.md#getAnnotationsByAccIdAndRgdIdUsingGET) | **GET** /annotations/{accId}/{rgdId} | Returns a list of annotations by RGD ID and ontology term accession ID
[**getAnnotationsByRgdIdAndOntologyUsingGET**](AnnotationApi.md#getAnnotationsByRgdIdAndOntologyUsingGET) | **GET** /annotations/rgdId/{rgdId}/{ontologyPrefix} | Returns a list of annotations by RGD ID and ontology prefix
[**getAnnotationsByRgdIdUsingGET**](AnnotationApi.md#getAnnotationsByRgdIdUsingGET) | **GET** /annotations/rgdId/{rgdId} | Returns a list of annotations by RGD ID
[**getAnnotationsUsingGET**](AnnotationApi.md#getAnnotationsUsingGET) | **GET** /annotations/{accId}/{speciesTypeKey}/{includeChildren} | Returns a list annotations for an ontology term or a term and it&#39;s children
[**getAnnotationsUsingPOST**](AnnotationApi.md#getAnnotationsUsingPOST) | **POST** /annotations/ | Return a list of genes annotated to an ontology term
[**getAnnotsByRefrerenceUsingGET**](AnnotationApi.md#getAnnotsByRefrerenceUsingGET) | **GET** /annotations/reference/{refRgdId} | Returns a list of annotations for a reference
[**getTermAccIdsUsingGET**](AnnotationApi.md#getTermAccIdsUsingGET) | **GET** /annotations/accId/{rgdId} | Returns a list ontology term accession IDs annotated to an rgd object



## getAnnotationCountByAccIdAndObjectTypeUsingGET

> Number getAnnotationCountByAccIdAndObjectTypeUsingGET(accId, speciesTypeKey, includeChildren, objectType)

Returns annotation count for ontology accession ID and object type

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let accId = "accId_example"; // String | Ontology term accession ID
let speciesTypeKey = 56; // Number | A list of species type keys can be found using the lookup service
let includeChildren = true; // Boolean | true: return annotations for the term and children, false: return annotations for the term only 
let objectType = 56; // Number | A list of object types can be found using the lookup service
apiInstance.getAnnotationCountByAccIdAndObjectTypeUsingGET(accId, speciesTypeKey, includeChildren, objectType, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| A list of species type keys can be found using the lookup service | 
 **includeChildren** | **Boolean**| true: return annotations for the term and children, false: return annotations for the term only  | 
 **objectType** | **Number**| A list of object types can be found using the lookup service | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAnnotationCountByAccIdAndSpeciesUsingGET

> Number getAnnotationCountByAccIdAndSpeciesUsingGET(accId, speciesTypeKey, includeChildren)

Returns annotation count for ontology accession ID and speicies

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let accId = "accId_example"; // String | Ontology term accession ID
let speciesTypeKey = 56; // Number | A list of species type keys can be found using the lookup service
let includeChildren = true; // Boolean | true: return annotations for the term and children, false: return annotations for the term only 
apiInstance.getAnnotationCountByAccIdAndSpeciesUsingGET(accId, speciesTypeKey, includeChildren, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| A list of species type keys can be found using the lookup service | 
 **includeChildren** | **Boolean**| true: return annotations for the term and children, false: return annotations for the term only  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAnnotationCountByAccIdUsingGET

> Number getAnnotationCountByAccIdUsingGET(accId, includeChildren)

Returns annotation count for ontology accession ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let accId = "accId_example"; // String | Ontology term accession ID
let includeChildren = true; // Boolean | true: return annotations for the term and children, false: return annotations for the term only 
apiInstance.getAnnotationCountByAccIdUsingGET(accId, includeChildren, (error, data, response) => {
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
 **includeChildren** | **Boolean**| true: return annotations for the term and children, false: return annotations for the term only  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAnnotationsByAccIdAndRgdIdUsingGET

> [Annotation] getAnnotationsByAccIdAndRgdIdUsingGET(accId, rgdId)

Returns a list of annotations by RGD ID and ontology term accession ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let accId = "accId_example"; // String | Ontology Term Accession ID
let rgdId = 56; // Number | RGD ID
apiInstance.getAnnotationsByAccIdAndRgdIdUsingGET(accId, rgdId, (error, data, response) => {
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
 **accId** | **String**| Ontology Term Accession ID | 
 **rgdId** | **Number**| RGD ID | 

### Return type

[**[Annotation]**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAnnotationsByRgdIdAndOntologyUsingGET

> [Annotation] getAnnotationsByRgdIdAndOntologyUsingGET(rgdId, ontologyPrefix)

Returns a list of annotations by RGD ID and ontology prefix

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let rgdId = 56; // Number | RGD ID
let ontologyPrefix = "ontologyPrefix_example"; // String | Ontology Prefix.  The prefix can be found left of the semicolon in an ontology term accession ID.  As an example, term accession PW:0000034 has the ontology prefix PW
apiInstance.getAnnotationsByRgdIdAndOntologyUsingGET(rgdId, ontologyPrefix, (error, data, response) => {
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
 **ontologyPrefix** | **String**| Ontology Prefix.  The prefix can be found left of the semicolon in an ontology term accession ID.  As an example, term accession PW:0000034 has the ontology prefix PW | 

### Return type

[**[Annotation]**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAnnotationsByRgdIdUsingGET

> [Annotation] getAnnotationsByRgdIdUsingGET(rgdId)

Returns a list of annotations by RGD ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getAnnotationsByRgdIdUsingGET(rgdId, (error, data, response) => {
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

[**[Annotation]**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAnnotationsUsingGET

> [Annotation] getAnnotationsUsingGET(accId, speciesTypeKey, includeChildren)

Returns a list annotations for an ontology term or a term and it&#39;s children

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let accId = "accId_example"; // String | Ontology term accession ID
let speciesTypeKey = 56; // Number | A list of species type keys can be found using the lookup service
let includeChildren = true; // Boolean | true: return annotations for the term and children, false: return annotations for the term only 
apiInstance.getAnnotationsUsingGET(accId, speciesTypeKey, includeChildren, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| A list of species type keys can be found using the lookup service | 
 **includeChildren** | **Boolean**| true: return annotations for the term and children, false: return annotations for the term only  | 

### Return type

[**[Annotation]**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getAnnotationsUsingPOST

> [Annotation] getAnnotationsUsingPOST(opts)

Return a list of genes annotated to an ontology term

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let opts = {
  'annotationRequest': new RatGenomeDatabaseRestApi.AnnotationRequest() // AnnotationRequest | data
};
apiInstance.getAnnotationsUsingPOST(opts, (error, data, response) => {
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
 **annotationRequest** | [**AnnotationRequest**](AnnotationRequest.md)| data | [optional] 

### Return type

[**[Annotation]**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## getAnnotsByRefrerenceUsingGET

> [Annotation] getAnnotsByRefrerenceUsingGET(refRgdId)

Returns a list of annotations for a reference

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let refRgdId = 56; // Number | Reference RGD ID
apiInstance.getAnnotsByRefrerenceUsingGET(refRgdId, (error, data, response) => {
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
 **refRgdId** | **Number**| Reference RGD ID | 

### Return type

[**[Annotation]**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getTermAccIdsUsingGET

> [MapPair] getTermAccIdsUsingGET(rgdId)

Returns a list ontology term accession IDs annotated to an rgd object

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.AnnotationApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getTermAccIdsUsingGET(rgdId, (error, data, response) => {
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

[**[MapPair]**](MapPair.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

