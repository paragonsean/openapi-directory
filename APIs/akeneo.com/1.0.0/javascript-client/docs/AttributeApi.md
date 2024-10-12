# AkeneoPimRestApi.AttributeApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAttributes**](AttributeApi.md#getAttributes) | **GET** /api/rest/v1/attributes | Get list of attributes
[**getAttributesCode**](AttributeApi.md#getAttributesCode) | **GET** /api/rest/v1/attributes/{code} | Get an attribute
[**patchAttributes**](AttributeApi.md#patchAttributes) | **PATCH** /api/rest/v1/attributes | Update/create several attributes
[**patchAttributesCode**](AttributeApi.md#patchAttributesCode) | **PATCH** /api/rest/v1/attributes/{code} | Update/create an attribute
[**postAttributes**](AttributeApi.md#postAttributes) | **POST** /api/rest/v1/attributes | Create a new attribute



## getAttributes

> Attributes getAttributes(opts)

Get list of attributes

This endpoint allows you to get a list of attributes. Attributes are paginated and sorted by code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeApi();
let opts = {
  'search': "search_example", // String | Filter attributes, for more details see the <a href=\"/documentation/filter.html#filter-attributes\">Filters</a> section.
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false, // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
  'withTableSelectOptions': false // Boolean | Return the options of 'select' column types (of a table attribute) in the response. (Only available since the 7.0 version)
};
apiInstance.getAttributes(opts, (error, data, response) => {
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
 **search** | **String**| Filter attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-attributes\&quot;&gt;Filters&lt;/a&gt; section. | [optional] 
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]
 **withTableSelectOptions** | **Boolean**| Return the options of &#39;select&#39; column types (of a table attribute) in the response. (Only available since the 7.0 version) | [optional] [default to false]

### Return type

[**Attributes**](Attributes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getAttributesCode

> PostAttributesRequest getAttributesCode(code, opts)

Get an attribute

This endpoint allows you to get the information about a given attribute.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeApi();
let code = "code_example"; // String | Code of the resource
let opts = {
  'withTableSelectOptions': false // Boolean | Return the options of 'select' column types (of a table attribute) in the response. (Only available since the 7.0 version)
};
apiInstance.getAttributesCode(code, opts, (error, data, response) => {
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
 **withTableSelectOptions** | **Boolean**| Return the options of &#39;select&#39; column types (of a table attribute) in the response. (Only available since the 7.0 version) | [optional] [default to false]

### Return type

[**PostAttributesRequest**](PostAttributesRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchAttributes

> PatchAssetCategories200Response patchAttributes(opts)

Update/create several attributes

This endpoint allows you to update and/or create several attributes at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeApi();
let opts = {
  'body': new AkeneoPimRestApi.PatchAttributesRequest() // PatchAttributesRequest | 
};
apiInstance.patchAttributes(opts, (error, data, response) => {
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
 **body** | [**PatchAttributesRequest**](PatchAttributesRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message


## patchAttributesCode

> patchAttributesCode(code, body)

Update/create an attribute

This endpoint allows you to update a given attribute. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no attribute exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PostAttributesRequest(); // PostAttributesRequest | 
apiInstance.patchAttributesCode(code, body, (error, data, response) => {
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
 **body** | [**PostAttributesRequest**](PostAttributesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postAttributes

> postAttributes(opts)

Create a new attribute

This endpoint allows you to create a new attribute.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeApi();
let opts = {
  'body': new AkeneoPimRestApi.PostAttributesRequest() // PostAttributesRequest | 
};
apiInstance.postAttributes(opts, (error, data, response) => {
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
 **body** | [**PostAttributesRequest**](PostAttributesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

