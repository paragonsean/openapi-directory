# SalesLoftPlatform.ImportsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2ImportsIdJsonDelete**](ImportsApi.md#v2ImportsIdJsonDelete) | **DELETE** /v2/imports/{id}.json | Delete an import
[**v2ImportsIdJsonGet**](ImportsApi.md#v2ImportsIdJsonGet) | **GET** /v2/imports/{id}.json | Fetch an import
[**v2ImportsIdJsonPut**](ImportsApi.md#v2ImportsIdJsonPut) | **PUT** /v2/imports/{id}.json | Update an import
[**v2ImportsJsonGet**](ImportsApi.md#v2ImportsJsonGet) | **GET** /v2/imports.json | List imports
[**v2ImportsJsonPost**](ImportsApi.md#v2ImportsJsonPost) | **POST** /v2/imports.json | Create an import



## v2ImportsIdJsonDelete

> v2ImportsIdJsonDelete(id, opts)

Delete an import

Deletes an import, by ID only. The associated people can be deleted as part of the deletion process.  Admin users can access imports for the entire team, but non-admin users can only access their own imports. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ImportsApi();
let id = "id_example"; // String | Import ID
let opts = {
  'undo': "undo_example" // String | Whether to delete people on this Import. Possible values are: [not present], all, single.  'single' will delete people who are only present in this Import. 'all' will delete people even if they are present in other Imports. Not specifying this parameter will not delete any people 
};
apiInstance.v2ImportsIdJsonDelete(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Import ID | 
 **undo** | **String**| Whether to delete people on this Import. Possible values are: [not present], all, single.  &#39;single&#39; will delete people who are only present in this Import. &#39;all&#39; will delete people even if they are present in other Imports. Not specifying this parameter will not delete any people  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2ImportsIdJsonGet

> Import v2ImportsIdJsonGet(id)

Fetch an import

Fetches an import, by ID only.  Admin users can access imports for the entire team, but non-admin users can only access their own imports. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ImportsApi();
let id = "id_example"; // String | Import ID
apiInstance.v2ImportsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Import ID | 

### Return type

[**Import**](Import.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2ImportsIdJsonPut

> Import v2ImportsIdJsonPut(id, opts)

Update an import

Updates an import, by ID only.  Admin users can access imports for the entire team, but non-admin users can only access their own imports. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ImportsApi();
let id = "id_example"; // String | Import ID
let opts = {
  'name': "name_example", // String | Name, recommended to be easily identifiable to a user
  'userId': 56 // Number | ID of the User that owns this Import
};
apiInstance.v2ImportsIdJsonPut(id, opts, (error, data, response) => {
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
 **id** | **String**| Import ID | 
 **name** | **String**| Name, recommended to be easily identifiable to a user | [optional] 
 **userId** | **Number**| ID of the User that owns this Import | [optional] 

### Return type

[**Import**](Import.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2ImportsJsonGet

> [Import] v2ImportsJsonGet(opts)

List imports

Fetches multiple imports. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ImportsApi();
let opts = {
  'ids': [null], // [Number] | IDs of imports to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'userIds': [null], // [Number] | ID of users to fetch imports for. Using this filter will return an empty array for non-admin users who request other user's imports
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at. Defaults to created_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2ImportsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of imports to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **userIds** | [**[Number]**](Number.md)| ID of users to fetch imports for. Using this filter will return an empty array for non-admin users who request other user&#39;s imports | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to created_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[Import]**](Import.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2ImportsJsonPost

> Import v2ImportsJsonPost(opts)

Create an import

Creates an import. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.ImportsApi();
let opts = {
  'name': "name_example", // String | Name, recommended to be easily identifiable to a user
  'userId': 56 // Number | ID of the User that owns this Import
};
apiInstance.v2ImportsJsonPost(opts, (error, data, response) => {
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
 **name** | **String**| Name, recommended to be easily identifiable to a user | [optional] 
 **userId** | **Number**| ID of the User that owns this Import | [optional] 

### Return type

[**Import**](Import.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

