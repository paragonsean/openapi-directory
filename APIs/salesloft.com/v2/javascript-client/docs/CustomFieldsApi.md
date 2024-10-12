# SalesLoftPlatform.CustomFieldsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2CustomFieldsIdJsonDelete**](CustomFieldsApi.md#v2CustomFieldsIdJsonDelete) | **DELETE** /v2/custom_fields/{id}.json | Delete a custom field
[**v2CustomFieldsIdJsonGet**](CustomFieldsApi.md#v2CustomFieldsIdJsonGet) | **GET** /v2/custom_fields/{id}.json | Fetch a custom field
[**v2CustomFieldsIdJsonPut**](CustomFieldsApi.md#v2CustomFieldsIdJsonPut) | **PUT** /v2/custom_fields/{id}.json | Update a custom field
[**v2CustomFieldsJsonGet**](CustomFieldsApi.md#v2CustomFieldsJsonGet) | **GET** /v2/custom_fields.json | List custom fields
[**v2CustomFieldsJsonPost**](CustomFieldsApi.md#v2CustomFieldsJsonPost) | **POST** /v2/custom_fields.json | Create a custom field



## v2CustomFieldsIdJsonDelete

> v2CustomFieldsIdJsonDelete(id)

Delete a custom field

Deletes a custom field. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CustomFieldsApi();
let id = "id_example"; // String | Custom Field ID
apiInstance.v2CustomFieldsIdJsonDelete(id, (error, data, response) => {
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
 **id** | **String**| Custom Field ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2CustomFieldsIdJsonGet

> CustomField v2CustomFieldsIdJsonGet(id)

Fetch a custom field

Fetches a custom field, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CustomFieldsApi();
let id = "id_example"; // String | Custom Field ID
apiInstance.v2CustomFieldsIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Custom Field ID | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2CustomFieldsIdJsonPut

> CustomField v2CustomFieldsIdJsonPut(id, opts)

Update a custom field

Update a custom field. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CustomFieldsApi();
let id = "id_example"; // String | Custom Field ID
let opts = {
  'fieldType': "fieldType_example", // String | The field type of the custom field. Value must be one of: person, company, opportunity
  'name': "name_example" // String | The name of the custom field
};
apiInstance.v2CustomFieldsIdJsonPut(id, opts, (error, data, response) => {
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
 **id** | **String**| Custom Field ID | 
 **fieldType** | **String**| The field type of the custom field. Value must be one of: person, company, opportunity | [optional] 
 **name** | **String**| The name of the custom field | [optional] 

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2CustomFieldsJsonGet

> [CustomField] v2CustomFieldsJsonGet(opts)

List custom fields

Fetches multiple custom field records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CustomFieldsApi();
let opts = {
  'ids': [null], // [Number] | IDs of custom fields to fetch.
  'fieldType': "fieldType_example", // String | Type of field to fetch. Value must be one of: person, company, opportunity
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at, name. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2CustomFieldsJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of custom fields to fetch. | [optional] 
 **fieldType** | **String**| Type of field to fetch. Value must be one of: person, company, opportunity | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at, name. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[CustomField]**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2CustomFieldsJsonPost

> CustomField v2CustomFieldsJsonPost(name, opts)

Create a custom field

Creates a custom field. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CustomFieldsApi();
let name = "name_example"; // String | The name of the custom field
let opts = {
  'fieldType': "fieldType_example" // String | The field type of the custom field. Value must be one of: person, company, opportunity
};
apiInstance.v2CustomFieldsJsonPost(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the custom field | 
 **fieldType** | **String**| The field type of the custom field. Value must be one of: person, company, opportunity | [optional] 

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

