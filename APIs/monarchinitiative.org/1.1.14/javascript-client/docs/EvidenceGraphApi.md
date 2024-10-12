# BioLinkApi.EvidenceGraphApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEvidenceGraphObject**](EvidenceGraphApi.md#getEvidenceGraphObject) | **GET** /evidence/graph/{id} | Returns evidence graph object for a given association
[**getEvidenceGraphTable**](EvidenceGraphApi.md#getEvidenceGraphTable) | **GET** /evidence/graph/{id}/table | Returns evidence as a association_results object given an association



## getEvidenceGraphObject

> [Graph] getEvidenceGraphObject(id)

Returns evidence graph object for a given association

Note that every association is assumed to have a unique ID

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.EvidenceGraphApi();
let id = "id_example"; // String | association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada
apiInstance.getEvidenceGraphObject(id, (error, data, response) => {
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
 **id** | **String**| association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada | 

### Return type

[**[Graph]**](Graph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvidenceGraphTable

> [AssociationResults] getEvidenceGraphTable(id, opts)

Returns evidence as a association_results object given an association

Note that every association is assumed to have a unique ID

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.EvidenceGraphApi();
let id = "id_example"; // String | association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada
let opts = {
  'isPublication': false // Boolean | If true, considers dc:source as edge
};
apiInstance.getEvidenceGraphTable(id, opts, (error, data, response) => {
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
 **id** | **String**| association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada | 
 **isPublication** | **Boolean**| If true, considers dc:source as edge | [optional] [default to false]

### Return type

[**[AssociationResults]**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

