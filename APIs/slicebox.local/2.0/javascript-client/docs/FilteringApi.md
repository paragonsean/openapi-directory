# SliceboxApi.FilteringApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filteringAssociationsGet**](FilteringApi.md#filteringAssociationsGet) | **GET** /filtering/associations | 
[**filteringAssociationsIdDelete**](FilteringApi.md#filteringAssociationsIdDelete) | **DELETE** /filtering/associations/{id} | 
[**filteringAssociationsPost**](FilteringApi.md#filteringAssociationsPost) | **POST** /filtering/associations | 
[**filteringFiltersGet**](FilteringApi.md#filteringFiltersGet) | **GET** /filtering/filters | 
[**filteringFiltersIdDelete**](FilteringApi.md#filteringFiltersIdDelete) | **DELETE** /filtering/filters/{id} | 
[**filteringFiltersIdTagpathsGet**](FilteringApi.md#filteringFiltersIdTagpathsGet) | **GET** /filtering/filters/{id}/tagpaths | 
[**filteringFiltersIdTagpathsPost**](FilteringApi.md#filteringFiltersIdTagpathsPost) | **POST** /filtering/filters/{id}/tagpaths | 
[**filteringFiltersIdTagpathsTagpathidDelete**](FilteringApi.md#filteringFiltersIdTagpathsTagpathidDelete) | **DELETE** /filtering/filters/{id}/tagpaths/{tagpathid} | 
[**filteringFiltersPost**](FilteringApi.md#filteringFiltersPost) | **POST** /filtering/filters | 



## filteringAssociationsGet

> [SourceTagFilter] filteringAssociationsGet(opts)



Get a list of source to filter associations.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.FilteringApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of source <-> filter associations
  'count': 20 // Number | size of returned slice of source <-> filter associations
};
apiInstance.filteringAssociationsGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of source &lt;-&gt; filter associations | [optional] [default to 0]
 **count** | **Number**| size of returned slice of source &lt;-&gt; filter associations | [optional] [default to 20]

### Return type

[**[SourceTagFilter]**](SourceTagFilter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## filteringAssociationsIdDelete

> filteringAssociationsIdDelete(id)



remove the source &lt;-&gt; filter association corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.FilteringApi();
let id = 789; // Number | id of source <-> filter association to remove
apiInstance.filteringAssociationsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| id of source &lt;-&gt; filter association to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## filteringAssociationsPost

> filteringAssociationsPost(sourcetagfilter)



Inserts or updates a source &lt;-&gt; filter associations. If the specified Source already  has an association this is updated, otherwise a new is inserted.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.FilteringApi();
let sourcetagfilter = new SliceboxApi.SourceTagFilter(); // SourceTagFilter | Source to Filter association
apiInstance.filteringAssociationsPost(sourcetagfilter, (error, data, response) => {
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
 **sourcetagfilter** | [**SourceTagFilter**](SourceTagFilter.md)| Source to Filter association | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## filteringFiltersGet

> [Filter] filteringFiltersGet(opts)



List defined filters

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.FilteringApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of filters
  'count': 20 // Number | size of returned slice of filters
};
apiInstance.filteringFiltersGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of filters | [optional] [default to 0]
 **count** | **Number**| size of returned slice of filters | [optional] [default to 20]

### Return type

[**[Filter]**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## filteringFiltersIdDelete

> filteringFiltersIdDelete(id)



remove the filter corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.FilteringApi();
let id = 789; // Number | id of filter to remove
apiInstance.filteringFiltersIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| id of filter to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## filteringFiltersIdTagpathsGet

> [TagPathTag] filteringFiltersIdTagpathsGet(id)



List tagpaths for the selected filter

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.FilteringApi();
let id = 789; // Number | id of filter
apiInstance.filteringFiltersIdTagpathsGet(id, (error, data, response) => {
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
 **id** | **Number**| id of filter | 

### Return type

[**[TagPathTag]**](TagPathTag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## filteringFiltersIdTagpathsPost

> filteringFiltersIdTagpathsPost(id, tagpath)



add a tagpath to a filter

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.FilteringApi();
let id = 789; // Number | id of filter to remove
let tagpath = new SliceboxApi.TagPathTag(); // TagPathTag | id of filter to remove
apiInstance.filteringFiltersIdTagpathsPost(id, tagpath, (error, data, response) => {
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
 **id** | **Number**| id of filter to remove | 
 **tagpath** | [**TagPathTag**](TagPathTag.md)| id of filter to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined


## filteringFiltersIdTagpathsTagpathidDelete

> filteringFiltersIdTagpathsTagpathidDelete(id, tagpathid)



remove the tagpath corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.FilteringApi();
let id = 789; // Number | id of filter
let tagpathid = 789; // Number | id of TagPath to remove
apiInstance.filteringFiltersIdTagpathsTagpathidDelete(id, tagpathid, (error, data, response) => {
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
 **id** | **Number**| id of filter | 
 **tagpathid** | **Number**| id of TagPath to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## filteringFiltersPost

> filteringFiltersPost(tagFilter)



Inserts or updates a filter. If a filter with same name as supplied filter exists this filter is updated, otherwise a new filter is inserted.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.FilteringApi();
let tagFilter = new SliceboxApi.Filter(); // Filter | Filter
apiInstance.filteringFiltersPost(tagFilter, (error, data, response) => {
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
 **tagFilter** | [**Filter**](Filter.md)| Filter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined

