# SalesLoftPlatform.SavedListViewsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2SavedListViewsIdJsonDelete**](SavedListViewsApi.md#v2SavedListViewsIdJsonDelete) | **DELETE** /v2/saved_list_views/{id}.json | Delete a saved list view
[**v2SavedListViewsIdJsonGet**](SavedListViewsApi.md#v2SavedListViewsIdJsonGet) | **GET** /v2/saved_list_views/{id}.json | Fetch a saved list view
[**v2SavedListViewsIdJsonPut**](SavedListViewsApi.md#v2SavedListViewsIdJsonPut) | **PUT** /v2/saved_list_views/{id}.json | Update a saved list view
[**v2SavedListViewsJsonGet**](SavedListViewsApi.md#v2SavedListViewsJsonGet) | **GET** /v2/saved_list_views.json | List saved list views
[**v2SavedListViewsJsonPost**](SavedListViewsApi.md#v2SavedListViewsJsonPost) | **POST** /v2/saved_list_views.json | Create a saved list view



## v2SavedListViewsIdJsonDelete

> v2SavedListViewsIdJsonDelete(id)

Delete a saved list view

Deletes a saved list view. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.SavedListViewsApi();
let id = "id_example"; // String | Saved List View ID
apiInstance.v2SavedListViewsIdJsonDelete(id, (error, data, response) => {
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
 **id** | **String**| Saved List View ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2SavedListViewsIdJsonGet

> SavedListView v2SavedListViewsIdJsonGet(id)

Fetch a saved list view

Fetches a saved list view, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.SavedListViewsApi();
let id = "id_example"; // String | Saved List View ID
apiInstance.v2SavedListViewsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Saved List View ID | 

### Return type

[**SavedListView**](SavedListView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2SavedListViewsIdJsonPut

> SavedListView v2SavedListViewsIdJsonPut(id, opts)

Update a saved list view

Updates a saved list view. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.SavedListViewsApi();
let id = "id_example"; // String | Saved List View ID
let opts = {
  'isDefault': true, // Boolean | Whether the saved list view is the default
  'name': "name_example", // String | The name of the saved list view
  'viewParams': "viewParams_example" // String | JSON object of list view parameters
};
apiInstance.v2SavedListViewsIdJsonPut(id, opts, (error, data, response) => {
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
 **id** | **String**| Saved List View ID | 
 **isDefault** | **Boolean**| Whether the saved list view is the default | [optional] 
 **name** | **String**| The name of the saved list view | [optional] 
 **viewParams** | **String**| JSON object of list view parameters | [optional] 

### Return type

[**SavedListView**](SavedListView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2SavedListViewsJsonGet

> [SavedListView] v2SavedListViewsJsonGet(opts)

List saved list views

Fetches multiple saved list view records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.SavedListViewsApi();
let opts = {
  'ids': [null], // [Number] | IDs of saved list views to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'view': "view_example", // String | Type of saved list views to fetch.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: name. Defaults to name
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2SavedListViewsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of saved list views to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **view** | **String**| Type of saved list views to fetch. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: name. Defaults to name | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[SavedListView]**](SavedListView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2SavedListViewsJsonPost

> SavedListView v2SavedListViewsJsonPost(name, view, opts)

Create a saved list view

Creates a saved list view. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.SavedListViewsApi();
let name = "name_example"; // String | The name of the saved list view
let view = "view_example"; // String | The type of objects in the saved list view.  Value must be one of: people, companies, or recordings
let opts = {
  'isDefault': true, // Boolean | Whether the saved list view is the default
  'viewParams': "viewParams_example" // String | JSON object of list view parameters
};
apiInstance.v2SavedListViewsJsonPost(name, view, opts, (error, data, response) => {
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
 **name** | **String**| The name of the saved list view | 
 **view** | **String**| The type of objects in the saved list view.  Value must be one of: people, companies, or recordings | 
 **isDefault** | **Boolean**| Whether the saved list view is the default | [optional] 
 **viewParams** | **String**| JSON object of list view parameters | [optional] 

### Return type

[**SavedListView**](SavedListView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

