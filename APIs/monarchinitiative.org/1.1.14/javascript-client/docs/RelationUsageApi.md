# BioLinkApi.RelationUsageApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRelationUsageBetweenResource**](RelationUsageApi.md#getRelationUsageBetweenResource) | **GET** /relation/usage/between/{subject_category}/{object_category} | All relations used plus count of associations
[**getRelationUsagePivotLabelResource**](RelationUsageApi.md#getRelationUsagePivotLabelResource) | **GET** /relation/usage/pivot/label | Relation usage count for all subj x obj category combinations, showing label
[**getRelationUsagePivotResource**](RelationUsageApi.md#getRelationUsagePivotResource) | **GET** /relation/usage/pivot | Relation usage count for all subj x obj category combinations
[**getRelationUsageResource**](RelationUsageApi.md#getRelationUsageResource) | **GET** /relation/usage/ | All relations used plus count of associations



## getRelationUsageBetweenResource

> [AssociationResults] getRelationUsageBetweenResource(subjectCategory, objectCategory, opts)

All relations used plus count of associations

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.RelationUsageApi();
let subjectCategory = "subjectCategory_example"; // String | 
let objectCategory = "objectCategory_example"; // String | 
let opts = {
  'subjectTaxon': "subjectTaxon_example", // String | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
  'evidence': "evidence_example" // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
};
apiInstance.getRelationUsageBetweenResource(subjectCategory, objectCategory, opts, (error, data, response) => {
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
 **subjectCategory** | **String**|  | 
 **objectCategory** | **String**|  | 
 **subjectTaxon** | **String**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRelationUsagePivotLabelResource

> [AssociationResults] getRelationUsagePivotLabelResource(opts)

Relation usage count for all subj x obj category combinations, showing label

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.RelationUsageApi();
let opts = {
  'subjectTaxon': "subjectTaxon_example", // String | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
  'evidence': "evidence_example" // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
};
apiInstance.getRelationUsagePivotLabelResource(opts, (error, data, response) => {
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
 **subjectTaxon** | **String**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRelationUsagePivotResource

> [AssociationResults] getRelationUsagePivotResource(opts)

Relation usage count for all subj x obj category combinations

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.RelationUsageApi();
let opts = {
  'subjectTaxon': "subjectTaxon_example", // String | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
  'evidence': "evidence_example" // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
};
apiInstance.getRelationUsagePivotResource(opts, (error, data, response) => {
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
 **subjectTaxon** | **String**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRelationUsageResource

> [AssociationResults] getRelationUsageResource(opts)

All relations used plus count of associations

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.RelationUsageApi();
let opts = {
  'subjectTaxon': "subjectTaxon_example", // String | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
  'evidence': "evidence_example" // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
};
apiInstance.getRelationUsageResource(opts, (error, data, response) => {
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
 **subjectTaxon** | **String**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] 
 **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] 

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

