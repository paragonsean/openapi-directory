# SalesLoftPlatform.GroupsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2GroupsIdJsonGet**](GroupsApi.md#v2GroupsIdJsonGet) | **GET** /v2/groups/{id}.json | Fetch a group
[**v2GroupsJsonGet**](GroupsApi.md#v2GroupsJsonGet) | **GET** /v2/groups.json | List groups



## v2GroupsIdJsonGet

> Group v2GroupsIdJsonGet(id)

Fetch a group

Fetches a group, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.GroupsApi();
let id = "id_example"; // String | Group ID
apiInstance.v2GroupsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Group ID | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2GroupsJsonGet

> [Group] v2GroupsJsonGet(opts)

List groups

Fetches multiple group records. The records can be filtered, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.GroupsApi();
let opts = {
  'ids': [null], // [Number] | IDs of groups to fetch.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
  'sortDirection': "sortDirection_example" // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
};
apiInstance.v2GroupsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of groups to fetch. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 

### Return type

[**[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

