# RubrikRestApi.VcdHierarchyApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVcdHierarchyChildrenV1**](VcdHierarchyApi.md#getVcdHierarchyChildrenV1) | **GET** /vcd/hierarchy/{id}/children | Get immediate descendant objects
[**getVcdHierarchyDescendantsV1**](VcdHierarchyApi.md#getVcdHierarchyDescendantsV1) | **GET** /vcd/hierarchy/{id}/descendants | Get list of descendant objects
[**getVcdHierarchyObjectV1**](VcdHierarchyApi.md#getVcdHierarchyObjectV1) | **GET** /vcd/hierarchy/{id} | Get summary of a vCD hierarchy object



## getVcdHierarchyChildrenV1

> VcdHierarchyObjectSummaryListResponse getVcdHierarchyChildrenV1(id, opts)

Get immediate descendant objects

Retrieve the list of immediate descendant objects for the specified parent.

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

let apiInstance = new RubrikRestApi.VcdHierarchyApi();
let id = "id_example"; // String | ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID.
let opts = {
  'sortBy': "sortBy_example", // String | Attribute to sort the results on.
  'sortOrder': "'asc'", // String | Order for sorting the results, either ascending or descending.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Number of matches to ignore from the beginning of the results.
  'name': "name_example", // String | Search object by object name.
  'isRelic': true, // Boolean | Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic children when this value is not specified.
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter by ID of effective SLA domain.
  'objectType': "objectType_example", // String | Filter by node object type.
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster ID, or **local**.
  'slaAssignment': "slaAssignment_example", // String | Filter by SLA assignment type.
  'snappableStatus': "snappableStatus_example" // String | Filters vCD hierarchy objects based on the specified query value.
};
apiInstance.getVcdHierarchyChildrenV1(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID. | 
 **sortBy** | **String**| Attribute to sort the results on. | [optional] 
 **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to &#39;asc&#39;]
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Number of matches to ignore from the beginning of the results. | [optional] 
 **name** | **String**| Search object by object name. | [optional] 
 **isRelic** | **Boolean**| Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic children when this value is not specified. | [optional] 
 **effectiveSlaDomainId** | **String**| Filter by ID of effective SLA domain. | [optional] 
 **objectType** | **String**| Filter by node object type. | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] 
 **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] 
 **snappableStatus** | **String**| Filters vCD hierarchy objects based on the specified query value. | [optional] 

### Return type

[**VcdHierarchyObjectSummaryListResponse**](VcdHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVcdHierarchyDescendantsV1

> VcdHierarchyObjectSummaryListResponse getVcdHierarchyDescendantsV1(id, opts)

Get list of descendant objects

Retrieve the list of descendant objects for the specified parent.

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

let apiInstance = new RubrikRestApi.VcdHierarchyApi();
let id = "id_example"; // String | ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID.
let opts = {
  'sortBy': "sortBy_example", // String | Attribute to sort the results on.
  'sortOrder': "'asc'", // String | Order for sorting the results, either ascending or descending.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Ignore these many matches in the beginning.
  'name': "name_example", // String | Search object by object name.
  'isRelic': true, // Boolean | Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic descendants if this query is not set.
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter by ID of effective SLA domain.
  'objectType': "objectType_example", // String | Filter by node object type.
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster ID, or **local**.
  'slaAssignment': "slaAssignment_example", // String | Filter by SLA assignment type.
  'snappableStatus': "snappableStatus_example" // String | Filters vCD hierarchy objects based on the specified query value.
};
apiInstance.getVcdHierarchyDescendantsV1(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID. | 
 **sortBy** | **String**| Attribute to sort the results on. | [optional] 
 **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to &#39;asc&#39;]
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Ignore these many matches in the beginning. | [optional] 
 **name** | **String**| Search object by object name. | [optional] 
 **isRelic** | **Boolean**| Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic descendants if this query is not set. | [optional] 
 **effectiveSlaDomainId** | **String**| Filter by ID of effective SLA domain. | [optional] 
 **objectType** | **String**| Filter by node object type. | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] 
 **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] 
 **snappableStatus** | **String**| Filters vCD hierarchy objects based on the specified query value. | [optional] 

### Return type

[**VcdHierarchyObjectSummaryListResponse**](VcdHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVcdHierarchyObjectV1

> VcdHierarchyObjectSummary getVcdHierarchyObjectV1(id)

Get summary of a vCD hierarchy object

Retrieve details for the specified object in the vCD hierarchy.

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

let apiInstance = new RubrikRestApi.VcdHierarchyApi();
let id = "id_example"; // String | ID of the vCD hierarchy object.
apiInstance.getVcdHierarchyObjectV1(id, (error, data, response) => {
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
 **id** | **String**| ID of the vCD hierarchy object. | 

### Return type

[**VcdHierarchyObjectSummary**](VcdHierarchyObjectSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

