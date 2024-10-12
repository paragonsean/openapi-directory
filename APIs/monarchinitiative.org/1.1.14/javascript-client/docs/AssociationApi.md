# BioLinkApi.AssociationApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssociationBySubjectAndAssocType**](AssociationApi.md#getAssociationBySubjectAndAssocType) | **GET** /association/type/{association_type} | Returns list of matching associations of a given type
[**getAssociationBySubjectAndObjectCategorySearch**](AssociationApi.md#getAssociationBySubjectAndObjectCategorySearch) | **GET** /association/find/{subject_category}/{object_category} | Returns list of matching associations between a given subject and object category
[**getAssociationBySubjectCategorySearch**](AssociationApi.md#getAssociationBySubjectCategorySearch) | **GET** /association/find/{subject_category} | Returns list of matching associations for a given subject category
[**getAssociationObject**](AssociationApi.md#getAssociationObject) | **GET** /association/{id} | Returns the association with a given identifier
[**getAssociationsBetween**](AssociationApi.md#getAssociationsBetween) | **GET** /association/between/{subject}/{object} | Returns associations connecting two entities
[**getAssociationsFrom**](AssociationApi.md#getAssociationsFrom) | **GET** /association/from/{subject} | Returns list of matching associations starting from a given subject (source)
[**getAssociationsTo**](AssociationApi.md#getAssociationsTo) | **GET** /association/to/{object} | Returns list of matching associations pointing to a given object (target)



## getAssociationBySubjectAndAssocType

> [AssociationResults] getAssociationBySubjectAndAssocType(associationType, opts)

Returns list of matching associations of a given type

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.AssociationApi();
let associationType = "associationType_example"; // String | Association type, eg gene_phenotype
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'subject': "subject_example", // String | Subject CURIE
  'object': "object_example" // String | Object CURIE
};
apiInstance.getAssociationBySubjectAndAssocType(associationType, opts, (error, data, response) => {
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
 **associationType** | **String**| Association type, eg gene_phenotype | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **subject** | **String**| Subject CURIE | [optional] 
 **object** | **String**| Object CURIE | [optional] 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssociationBySubjectAndObjectCategorySearch

> [AssociationResults] getAssociationBySubjectAndObjectCategorySearch(objectCategory, subjectCategory, opts)

Returns list of matching associations between a given subject and object category

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.AssociationApi();
let objectCategory = "objectCategory_example"; // String | Category of entity at link Object (target), e.g. gene, disease, phenotype
let subjectCategory = "subjectCategory_example"; // String | Category of entity at link Subject (source), e.g. gene, disease, phenotype
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'subject': "subject_example", // String | Subject CURIE
  'object': "object_example", // String | Object CURIE
  'subjectTaxon': "subjectTaxon_example", // String | Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default)
  'objectTaxon': "objectTaxon_example", // String | Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default)
  'relation': "relation_example" // String | Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc.
};
apiInstance.getAssociationBySubjectAndObjectCategorySearch(objectCategory, subjectCategory, opts, (error, data, response) => {
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
 **objectCategory** | **String**| Category of entity at link Object (target), e.g. gene, disease, phenotype | 
 **subjectCategory** | **String**| Category of entity at link Subject (source), e.g. gene, disease, phenotype | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **subject** | **String**| Subject CURIE | [optional] 
 **object** | **String**| Object CURIE | [optional] 
 **subjectTaxon** | **String**| Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default) | [optional] 
 **objectTaxon** | **String**| Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) | [optional] 
 **relation** | **String**| Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. | [optional] 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssociationBySubjectCategorySearch

> [AssociationResults] getAssociationBySubjectCategorySearch(subjectCategory, opts)

Returns list of matching associations for a given subject category

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.AssociationApi();
let subjectCategory = "subjectCategory_example"; // String | Category of entity at link Subject (source), e.g. gene, disease, phenotype
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'subjectTaxon': "subjectTaxon_example", // String | Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default)
  'objectTaxon': "objectTaxon_example", // String | Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default)
  'relation': "relation_example" // String | Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc.
};
apiInstance.getAssociationBySubjectCategorySearch(subjectCategory, opts, (error, data, response) => {
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
 **subjectCategory** | **String**| Category of entity at link Subject (source), e.g. gene, disease, phenotype | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **subjectTaxon** | **String**| Subject taxon ID, e.g. NCBITaxon:9606 (Includes inferred associations, by default) | [optional] 
 **objectTaxon** | **String**| Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) | [optional] 
 **relation** | **String**| Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. | [optional] 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssociationObject

> [AssociationResults] getAssociationObject(id)

Returns the association with a given identifier

An association connects, at a minimum, two things, designated subject and object, via some relationship. Associations also include evidence, provenance etc.

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.AssociationApi();
let id = "id_example"; // String | identifier for an association, e.g. f5ba436c-f851-41b3-9d9d-bb2b5fc879d4
apiInstance.getAssociationObject(id, (error, data, response) => {
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
 **id** | **String**| identifier for an association, e.g. f5ba436c-f851-41b3-9d9d-bb2b5fc879d4 | 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssociationsBetween

> [AssociationResults] getAssociationsBetween(object, subject, opts)

Returns associations connecting two entities

Given two entities (e.g. a particular gene and a particular disease), if these two entities are connected (directly or indirectly), then return the association objects describing the connection.

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.AssociationApi();
let object = "object_example"; // String | Return associations pointing to this node, e.g. MP:0013765. Can also be a biological entity such as a gene
let subject = "subject_example"; // String | Return associations emanating from this node, e.g. MGI:1342287 (If ID is from an ontology then results would include inferred associations, by default)
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'useCompactAssociations': false // Boolean | If true, returns results in compact associations format
};
apiInstance.getAssociationsBetween(object, subject, opts, (error, data, response) => {
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
 **object** | **String**| Return associations pointing to this node, e.g. MP:0013765. Can also be a biological entity such as a gene | 
 **subject** | **String**| Return associations emanating from this node, e.g. MGI:1342287 (If ID is from an ontology then results would include inferred associations, by default) | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssociationsFrom

> [AssociationResults] getAssociationsFrom(subject, opts)

Returns list of matching associations starting from a given subject (source)

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.AssociationApi();
let subject = "subject_example"; // String | Return associations emanating from this node, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357 (If ID is from an ontology then results would include inferred associations, by default)
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'useCompactAssociations': false, // Boolean | If true, returns results in compact associations format
  'objectTaxon': "objectTaxon_example", // String | Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default)
  'relation': "relation_example" // String | Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc.
};
apiInstance.getAssociationsFrom(subject, opts, (error, data, response) => {
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
 **subject** | **String**| Return associations emanating from this node, e.g. NCBIGene:84570, ZFIN:ZDB-GENE-050417-357 (If ID is from an ontology then results would include inferred associations, by default) | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]
 **objectTaxon** | **String**| Object taxon ID, e.g. NCBITaxon:10090 (Includes inferred associations, by default) | [optional] 
 **relation** | **String**| Filter by relation CURIE, e.g. RO:0002200 (has_phenotype), RO:0002607 (is marker for), RO:HOM0000017 (orthologous to), etc. | [optional] 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssociationsTo

> [AssociationResults] getAssociationsTo(object, opts)

Returns list of matching associations pointing to a given object (target)

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.AssociationApi();
let object = "object_example"; // String | Return associations pointing to this node, e.g. specifying MP:0013765 will return all genes, variants, strains, etc. annotated with this term. Can also be a biological entity such as a gene
let opts = {
  'rows': 100, // Number | number of rows
  'start': 56, // Number | beginning row
  'evidence': "evidence_example", // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2
  'unselectEvidence': false, // Boolean | If true, excludes evidence objects in response
  'excludeAutomaticAssertions': false, // Boolean | If true, excludes associations that involve IEAs (ECO:0000501)
  'useCompactAssociations': false // Boolean | If true, returns results in compact associations format
};
apiInstance.getAssociationsTo(object, opts, (error, data, response) => {
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
 **object** | **String**| Return associations pointing to this node, e.g. specifying MP:0013765 will return all genes, variants, strains, etc. annotated with this term. Can also be a biological entity such as a gene | 
 **rows** | **Number**| number of rows | [optional] [default to 100]
 **start** | **Number**| beginning row | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default) or a specific publication or other supporting object, e.g. ZFIN:ZDB-PUB-060503-2 | [optional] 
 **unselectEvidence** | **Boolean**| If true, excludes evidence objects in response | [optional] [default to false]
 **excludeAutomaticAssertions** | **Boolean**| If true, excludes associations that involve IEAs (ECO:0000501) | [optional] [default to false]
 **useCompactAssociations** | **Boolean**| If true, returns results in compact associations format | [optional] [default to false]

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

