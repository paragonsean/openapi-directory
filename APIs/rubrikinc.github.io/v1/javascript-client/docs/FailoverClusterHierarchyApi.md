# RubrikRestApi.FailoverClusterHierarchyApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFailoverClusterHierarchyChildren**](FailoverClusterHierarchyApi.md#getFailoverClusterHierarchyChildren) | **GET** /failover_cluster/hierarchy/{id}/children | Get list of immediate descendant objects
[**getFailoverClusterHierarchyDescendants**](FailoverClusterHierarchyApi.md#getFailoverClusterHierarchyDescendants) | **GET** /failover_cluster/hierarchy/{id}/descendants | Get list of descendant objects
[**getFailoverClusterHierarchyObject**](FailoverClusterHierarchyApi.md#getFailoverClusterHierarchyObject) | **GET** /failover_cluster/hierarchy/{id} | Get summary of a hierarchy object



## getFailoverClusterHierarchyChildren

> FailoverClusterHierarchyObjectSummaryListResponse getFailoverClusterHierarchyChildren(id, opts)

Get list of immediate descendant objects

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

let apiInstance = new RubrikRestApi.FailoverClusterHierarchyApi();
let id = "id_example"; // String | ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID.
let opts = {
  'name': "name_example", // String | Filter a response by making an infix comparison of the failover cluster name or failover cluster app name.
  'operatingSystemType': "operatingSystemType_example", // String | Filter a response based on the failover cluster operating system type.
  'objectType': "objectType_example", // String | Filter by node object type.
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster ID, or **local**.
  'limit': 56, // Number | An integer that specifies the maximum number of matches to return.
  'offset': 56, // Number | An integer that specifies a number of initial matches to ignore.
  'configuredSlaDomainId': "configuredSlaDomainId_example", // String | Filter by configured SLA domain.
  'slaAssignment': "slaAssignment_example", // String | Filter by SLA assignment type.
  'sortBy': "sortBy_example", // String | Attribute to sort the results on.
  'sortOrder': "sortOrder_example" // String | Sort order, either ascending or descending.
};
apiInstance.getFailoverClusterHierarchyChildren(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID. | 
 **name** | **String**| Filter a response by making an infix comparison of the failover cluster name or failover cluster app name. | [optional] 
 **operatingSystemType** | **String**| Filter a response based on the failover cluster operating system type. | [optional] 
 **objectType** | **String**| Filter by node object type. | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] 
 **limit** | **Number**| An integer that specifies the maximum number of matches to return. | [optional] 
 **offset** | **Number**| An integer that specifies a number of initial matches to ignore. | [optional] 
 **configuredSlaDomainId** | **String**| Filter by configured SLA domain. | [optional] 
 **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] 
 **sortBy** | **String**| Attribute to sort the results on. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 

### Return type

[**FailoverClusterHierarchyObjectSummaryListResponse**](FailoverClusterHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFailoverClusterHierarchyDescendants

> FailoverClusterHierarchyObjectSummaryListResponse getFailoverClusterHierarchyDescendants(id, opts)

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

let apiInstance = new RubrikRestApi.FailoverClusterHierarchyApi();
let id = "id_example"; // String | ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID.
let opts = {
  'name': "name_example", // String | Filter a response by making an infix comparison of the failover cluster name or failover cluster app name.
  'operatingSystemType': "operatingSystemType_example", // String | Filter a response based on the failover cluster operating system type.
  'objectType': "objectType_example", // String | Filter by node object type.
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster ID, or **local**.
  'limit': 56, // Number | An integer that specifies the maximum number of matches to return.
  'offset': 56, // Number | An integer that specifies a number of initial matches to ignore.
  'configuredSlaDomainId': "configuredSlaDomainId_example", // String | Filter by configured SLA domain.
  'slaAssignment': "slaAssignment_example", // String | Filter by SLA assignment type.
  'sortBy': "sortBy_example", // String | Attribute to sort the results on.
  'sortOrder': "sortOrder_example" // String | Sort order, either ascending or descending.
};
apiInstance.getFailoverClusterHierarchyDescendants(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the parent failover cluster hierarchy object. To get top-level nodes, use **root** as the ID. | 
 **name** | **String**| Filter a response by making an infix comparison of the failover cluster name or failover cluster app name. | [optional] 
 **operatingSystemType** | **String**| Filter a response based on the failover cluster operating system type. | [optional] 
 **objectType** | **String**| Filter by node object type. | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] 
 **limit** | **Number**| An integer that specifies the maximum number of matches to return. | [optional] 
 **offset** | **Number**| An integer that specifies a number of initial matches to ignore. | [optional] 
 **configuredSlaDomainId** | **String**| Filter by configured SLA domain. | [optional] 
 **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] 
 **sortBy** | **String**| Attribute to sort the results on. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 

### Return type

[**FailoverClusterHierarchyObjectSummaryListResponse**](FailoverClusterHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFailoverClusterHierarchyObject

> FailoverClusterHierarchyObjectSummary getFailoverClusterHierarchyObject(id)

Get summary of a hierarchy object

Retrieve details for the specified hierarchy object.

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

let apiInstance = new RubrikRestApi.FailoverClusterHierarchyApi();
let id = "id_example"; // String | ID of the hierarchy object.
apiInstance.getFailoverClusterHierarchyObject(id, (error, data, response) => {
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
 **id** | **String**| ID of the hierarchy object. | 

### Return type

[**FailoverClusterHierarchyObjectSummary**](FailoverClusterHierarchyObjectSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

