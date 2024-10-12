# NooshApiApplication.QuoteApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getQuote**](QuoteApi.md#getQuote) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/quotes/{quote_id} | Get a specific quote of project
[**getQuoteList**](QuoteApi.md#getQuoteList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/quotes | List the quotes
[**getQuoteStateList**](QuoteApi.md#getQuoteStateList) | **GET** /v1/workgroups/{workgroup_id}/quoteStates | List the quote states
[**putQuote**](QuoteApi.md#putQuote) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/quotes/{quote_id} | Accept / Reject a Quote
[**v1WorkgroupsWorkgroupIdQuotesGet**](QuoteApi.md#v1WorkgroupsWorkgroupIdQuotesGet) | **GET** /v1/workgroups/{workgroup_id}/quotes | List the quotes of workgroup level



## getQuote

> QuoteExpandVO getQuote(workgroupId, projectId, quoteId)

Get a specific quote of project

Get a specific quote of project

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.QuoteApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let quoteId = "quoteId_example"; // String | 
apiInstance.getQuote(workgroupId, projectId, quoteId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **quoteId** | **String**|  | 

### Return type

[**QuoteExpandVO**](QuoteExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getQuoteList

> QuoteListVO getQuoteList(workgroupId, projectId, opts)

List the quotes

List the quotes

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.QuoteApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'quoteStateIdUseFiltersquoteStateId111111': "quoteStateIdUseFiltersquoteStateId111111_example" // String | Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value
};
apiInstance.getQuoteList(workgroupId, projectId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **quoteStateIdUseFiltersquoteStateId111111** | **String**| Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value | [optional] 

### Return type

[**QuoteListVO**](QuoteListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getQuoteStateList

> ObjectStateListVO getQuoteStateList(workgroupId)

List the quote states

List the quote states

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.QuoteApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getQuoteStateList(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**ObjectStateListVO**](ObjectStateListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## putQuote

> HTTPStatusVO putQuote(workgroupId, projectId, quoteId, opts)

Accept / Reject a Quote

Accept / Reject a Quote

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.QuoteApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let quoteId = "quoteId_example"; // String | 
let opts = {
  'quotePutPersistVO': new NooshApiApplication.QuotePutPersistVO() // QuotePutPersistVO | 
};
apiInstance.putQuote(workgroupId, projectId, quoteId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **quoteId** | **String**|  | 
 **quotePutPersistVO** | [**QuotePutPersistVO**](QuotePutPersistVO.md)|  | [optional] 

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## v1WorkgroupsWorkgroupIdQuotesGet

> QuoteOfWgLevelSimpleVO v1WorkgroupsWorkgroupIdQuotesGet(workgroupId, opts)

List the quotes of workgroup level

List the quotes of workgroup level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.QuoteApi();
let workgroupId = "workgroupId_example"; // String | 
let opts = {
  'quoteStateIdUseFiltersquoteStateId111111': "quoteStateIdUseFiltersquoteStateId111111_example" // String | Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value
};
apiInstance.v1WorkgroupsWorkgroupIdQuotesGet(workgroupId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **quoteStateIdUseFiltersquoteStateId111111** | **String**| Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value | [optional] 

### Return type

[**QuoteOfWgLevelSimpleVO**](QuoteOfWgLevelSimpleVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

