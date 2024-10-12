# RubrikRestApi.HierarchyApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkHierarchySlaConflictsV1**](HierarchyApi.md#bulkHierarchySlaConflictsV1) | **POST** /hierarchy/bulk_sla_conflicts | Retrieve the list of descendant objects with SLA conflicts in bulk



## bulkHierarchySlaConflictsV1

> BulkSlaConflictsSummary bulkHierarchySlaConflictsV1(hierarchyObjectIds)

Retrieve the list of descendant objects with SLA conflicts in bulk

Retrieve the list of descendant objects with an explicitly configured SLA domain, or inherit an SLA domain from a different parent for each managed ID.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HierarchyApi();
let hierarchyObjectIds = new RubrikRestApi.HierarchyObjectIds(); // HierarchyObjectIds | List of hierarchy object IDs.
apiInstance.bulkHierarchySlaConflictsV1(hierarchyObjectIds, (error, data, response) => {
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
 **hierarchyObjectIds** | [**HierarchyObjectIds**](HierarchyObjectIds.md)| List of hierarchy object IDs. | 

### Return type

[**BulkSlaConflictsSummary**](BulkSlaConflictsSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

