# SalesLoftPlatform.PersonStagesApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2PersonStagesIdJsonDelete**](PersonStagesApi.md#v2PersonStagesIdJsonDelete) | **DELETE** /v2/person_stages/{id}.json | Delete an person stage
[**v2PersonStagesIdJsonGet**](PersonStagesApi.md#v2PersonStagesIdJsonGet) | **GET** /v2/person_stages/{id}.json | Fetch a person stage
[**v2PersonStagesIdJsonPut**](PersonStagesApi.md#v2PersonStagesIdJsonPut) | **PUT** /v2/person_stages/{id}.json | Update a person stage
[**v2PersonStagesJsonGet**](PersonStagesApi.md#v2PersonStagesJsonGet) | **GET** /v2/person_stages.json | List person stages
[**v2PersonStagesJsonPost**](PersonStagesApi.md#v2PersonStagesJsonPost) | **POST** /v2/person_stages.json | Create a person stage



## v2PersonStagesIdJsonDelete

> v2PersonStagesIdJsonDelete(id)

Delete an person stage

Deletes a person stage. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PersonStagesApi();
let id = "id_example"; // String | Stage ID
apiInstance.v2PersonStagesIdJsonDelete(id, (error, data, response) => {
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
 **id** | **String**| Stage ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2PersonStagesIdJsonGet

> PersonStage v2PersonStagesIdJsonGet(id)

Fetch a person stage

Fetches a person stage, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PersonStagesApi();
let id = "id_example"; // String | Stage ID
apiInstance.v2PersonStagesIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Stage ID | 

### Return type

[**PersonStage**](PersonStage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2PersonStagesIdJsonPut

> PersonStage v2PersonStagesIdJsonPut(id, name)

Update a person stage

Updates a person stage. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PersonStagesApi();
let id = "id_example"; // String | Stage ID
let name = "name_example"; // String | The name of the stage.
apiInstance.v2PersonStagesIdJsonPut(id, name, (error, data, response) => {
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
 **id** | **String**| Stage ID | 
 **name** | **String**| The name of the stage. | 

### Return type

[**PersonStage**](PersonStage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2PersonStagesJsonGet

> [PersonStage] v2PersonStagesJsonGet(opts)

List person stages

Fetches multiple person stage records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PersonStagesApi();
let opts = {
  'ids': [null], // [Number] | IDs of person stages to fetch.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2PersonStagesJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of person stages to fetch. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[PersonStage]**](PersonStage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2PersonStagesJsonPost

> PersonStage v2PersonStagesJsonPost(name)

Create a person stage

Creates a person stage. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.PersonStagesApi();
let name = "name_example"; // String | The name of the new stage
apiInstance.v2PersonStagesJsonPost(name, (error, data, response) => {
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
 **name** | **String**| The name of the new stage | 

### Return type

[**PersonStage**](PersonStage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

