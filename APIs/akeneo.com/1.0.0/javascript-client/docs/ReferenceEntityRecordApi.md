# AkeneoPimRestApi.ReferenceEntityRecordApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReferenceEntityRecords**](ReferenceEntityRecordApi.md#getReferenceEntityRecords) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/records | Get the list of the records of a reference entity
[**getReferenceEntityRecordsCode**](ReferenceEntityRecordApi.md#getReferenceEntityRecordsCode) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/records/{code} | Get a record of a given reference entity
[**patchReferenceEntityRecords**](ReferenceEntityRecordApi.md#patchReferenceEntityRecords) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/records | Update/create several reference entity records
[**patchReferenceEntityRecordsCode**](ReferenceEntityRecordApi.md#patchReferenceEntityRecordsCode) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/records/{code} | Update/create a record of a given reference entity



## getReferenceEntityRecords

> ReferenceEntityRecord getReferenceEntityRecords(referenceEntityCode, opts)

Get the list of the records of a reference entity

This endpoint allows you to get a list of records of a given reference entity. Records are paginated and can be filtered.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityRecordApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
let opts = {
  'search': "search_example", // String | Filter records of the reference entity, for more details see the <a href=\"/documentation/filter.html#filter-reference-entity-records\">Filters</a> section
  'channel': "channel_example", // String | Filter attribute values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#record-values-by-channel\">Filter attribute values by channel</a> section
  'locales': "locales_example", // String | Filter attribute values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#record-values-by-locale\">Filter attribute values by locale</a> section
  'searchAfter': "'cursor to the first page'" // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
};
apiInstance.getReferenceEntityRecords(referenceEntityCode, opts, (error, data, response) => {
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
 **referenceEntityCode** | **String**| Code of the reference entity | 
 **search** | **String**| Filter records of the reference entity, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-reference-entity-records\&quot;&gt;Filters&lt;/a&gt; section | [optional] 
 **channel** | **String**| Filter attribute values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#record-values-by-channel\&quot;&gt;Filter attribute values by channel&lt;/a&gt; section | [optional] 
 **locales** | **String**| Filter attribute values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#record-values-by-locale\&quot;&gt;Filter attribute values by locale&lt;/a&gt; section | [optional] 
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]

### Return type

[**ReferenceEntityRecord**](ReferenceEntityRecord.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, code, message


## getReferenceEntityRecordsCode

> PatchReferenceEntityRecordsRequestInner getReferenceEntityRecordsCode(referenceEntityCode, code)

Get a record of a given reference entity

This endpoint allows you to get the information about a given record for a given reference entity.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityRecordApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
let code = "code_example"; // String | Code of the resource
apiInstance.getReferenceEntityRecordsCode(referenceEntityCode, code, (error, data, response) => {
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
 **referenceEntityCode** | **String**| Code of the reference entity | 
 **code** | **String**| Code of the resource | 

### Return type

[**PatchReferenceEntityRecordsRequestInner**](PatchReferenceEntityRecordsRequestInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchReferenceEntityRecords

> [PatchAssets200ResponseInner] patchReferenceEntityRecords(referenceEntityCode, body)

Update/create several reference entity records

This endpoint allows you to update and/or create several records of one given reference entity at once. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#patch-reference-entity-record-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the record does not already exist for the given reference entity, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityRecordApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
let body = [new AkeneoPimRestApi.PatchReferenceEntityRecordsRequestInner()]; // [PatchReferenceEntityRecordsRequestInner] | 
apiInstance.patchReferenceEntityRecords(referenceEntityCode, body, (error, data, response) => {
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
 **referenceEntityCode** | **String**| Code of the reference entity | 
 **body** | [**[PatchReferenceEntityRecordsRequestInner]**](PatchReferenceEntityRecordsRequestInner.md)|  | 

### Return type

[**[PatchAssets200ResponseInner]**](PatchAssets200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchReferenceEntityRecordsCode

> patchReferenceEntityRecordsCode(referenceEntityCode, code, body)

Update/create a record of a given reference entity

This endpoint allows you to update a given record of a given renference entity. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#patch-reference-entity-record-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the record does not already exist for the given reference entity, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityRecordApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PatchReferenceEntityRecordsCodeRequest(); // PatchReferenceEntityRecordsCodeRequest | 
apiInstance.patchReferenceEntityRecordsCode(referenceEntityCode, code, body, (error, data, response) => {
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
 **referenceEntityCode** | **String**| Code of the reference entity | 
 **code** | **String**| Code of the resource | 
 **body** | [**PatchReferenceEntityRecordsCodeRequest**](PatchReferenceEntityRecordsCodeRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

