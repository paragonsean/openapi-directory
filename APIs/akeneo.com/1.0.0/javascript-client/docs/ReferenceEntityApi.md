# AkeneoPimRestApi.ReferenceEntityApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReferenceEntities**](ReferenceEntityApi.md#getReferenceEntities) | **GET** /api/rest/v1/reference-entities | Get list of reference entities
[**getReferenceEntitiesCode**](ReferenceEntityApi.md#getReferenceEntitiesCode) | **GET** /api/rest/v1/reference-entities/{code} | Get a reference entity
[**patchReferenceEntityCode**](ReferenceEntityApi.md#patchReferenceEntityCode) | **PATCH** /api/rest/v1/reference-entities/{code} | Update/create a reference entity



## getReferenceEntities

> ReferenceEntities getReferenceEntities(opts)

Get list of reference entities

This endpoint allows you to get a list of reference entities. Reference entities are paginated.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityApi();
let opts = {
  'searchAfter': "'cursor to the first page'" // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
};
apiInstance.getReferenceEntities(opts, (error, data, response) => {
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
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]

### Return type

[**ReferenceEntities**](ReferenceEntities.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, code, message


## getReferenceEntitiesCode

> GetReferenceEntitiesCode200Response getReferenceEntitiesCode(code)

Get a reference entity

This endpoint allows you to get the information about a given reference entity.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getReferenceEntitiesCode(code, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 

### Return type

[**GetReferenceEntitiesCode200Response**](GetReferenceEntitiesCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchReferenceEntityCode

> patchReferenceEntityCode(code, body)

Update/create a reference entity

This endpoint allows you to update a given reference entity. Note that if the reference entity does not already exist, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PatchReferenceEntityCodeRequest(); // PatchReferenceEntityCodeRequest | 
apiInstance.patchReferenceEntityCode(code, body, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 
 **body** | [**PatchReferenceEntityCodeRequest**](PatchReferenceEntityCodeRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

