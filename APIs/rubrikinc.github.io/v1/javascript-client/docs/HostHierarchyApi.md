# RubrikRestApi.HostHierarchyApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHostHierarchyChildren**](HostHierarchyApi.md#getHostHierarchyChildren) | **GET** /host/hierarchy/{id}/children | Get immediate descendant objects
[**getHostHierarchyObject**](HostHierarchyApi.md#getHostHierarchyObject) | **GET** /host/hierarchy/{id} | Get summary of a host/share hierarchy object



## getHostHierarchyChildren

> HostHierarchyObjectSummaryListResponse getHostHierarchyChildren(id, opts)

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

let apiInstance = new RubrikRestApi.HostHierarchyApi();
let id = "id_example"; // String | ID of the parent host hierarchy object. To get top-level nodes, use **root** as the ID.
let opts = {
  'name': "name_example", // String | Search object by object name.
  'objectType': "objectType_example", // String | Filter by node object type.
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter by ID of effective SLA domain.
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary cluster ID, or **local**.
  'slaAssignment': "slaAssignment_example", // String | Limit a response to the results that have the specified SLA Domain assignment type.
  'templateId': "templateId_example", // String | Filter by fileset template ID.
  'vendorType': "vendorType_example", // String | Filter by NAS vendor.
  'exportPoint': "exportPoint_example", // String | Search object by export point.
  'operatingSystemType': "operatingSystemType_example", // String | Filter the summary information based on the operating system type. Accepted values are 'Windows', 'UnixLike', 'ANY', 'NONE'. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set.
  'sortBy': "sortBy_example", // String | Attribute to sort the results on.
  'sortOrder': "'asc'", // String | Order for sorting the results, either ascending or descending.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56 // Number | Number of matches to ignore from the beginning of the results.
};
apiInstance.getHostHierarchyChildren(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the parent host hierarchy object. To get top-level nodes, use **root** as the ID. | 
 **name** | **String**| Search object by object name. | [optional] 
 **objectType** | **String**| Filter by node object type. | [optional] 
 **effectiveSlaDomainId** | **String**| Filter by ID of effective SLA domain. | [optional] 
 **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] 
 **slaAssignment** | **String**| Limit a response to the results that have the specified SLA Domain assignment type. | [optional] 
 **templateId** | **String**| Filter by fileset template ID. | [optional] 
 **vendorType** | **String**| Filter by NAS vendor. | [optional] 
 **exportPoint** | **String**| Search object by export point. | [optional] 
 **operatingSystemType** | **String**| Filter the summary information based on the operating system type. Accepted values are &#39;Windows&#39;, &#39;UnixLike&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set. | [optional] 
 **sortBy** | **String**| Attribute to sort the results on. | [optional] 
 **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to &#39;asc&#39;]
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Number of matches to ignore from the beginning of the results. | [optional] 

### Return type

[**HostHierarchyObjectSummaryListResponse**](HostHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHostHierarchyObject

> HostHierarchyObjectSummary getHostHierarchyObject(id)

Get summary of a host/share hierarchy object

Retrieve details for the specified object in the host/share hierarchy. 

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

let apiInstance = new RubrikRestApi.HostHierarchyApi();
let id = "id_example"; // String | ID of the host hierarchy object.
apiInstance.getHostHierarchyObject(id, (error, data, response) => {
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
 **id** | **String**| ID of the host hierarchy object. | 

### Return type

[**HostHierarchyObjectSummary**](HostHierarchyObjectSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

