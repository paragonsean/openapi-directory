# SalesLoftPlatform.RolesApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CustomRolesIdJsonGet**](RolesApi.md#v2CustomRolesIdJsonGet) | **GET** /v2/custom_roles/{id}.json | Fetch a custom role
[**v2CustomRolesJsonGet**](RolesApi.md#v2CustomRolesJsonGet) | **GET** /v2/custom_roles.json | List custom roles



## v2CustomRolesIdJsonGet

> CustomRole v2CustomRolesIdJsonGet(id)

Fetch a custom role

Fetches a custom role, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.RolesApi();
let id = "id_example"; // String | Custom Role ID
apiInstance.v2CustomRolesIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Custom Role ID | 

### Return type

[**CustomRole**](CustomRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2CustomRolesJsonGet

> [CustomRole] v2CustomRolesJsonGet(opts)

List custom roles

Fetches multiple custom role records. The records can be filtered, and sorted according to the respective parameters. A custom role is any role that is not Admin or User. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.RolesApi();
let opts = {
  'ids': ["null"], // [String] | IDs of roles to fetch.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: id, name. Defaults to id
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2CustomRolesJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| IDs of roles to fetch. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: id, name. Defaults to id | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[CustomRole]**](CustomRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

