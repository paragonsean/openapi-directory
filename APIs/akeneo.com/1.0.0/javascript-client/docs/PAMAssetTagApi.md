# AkeneoPimRestApi.PAMAssetTagApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssetTags**](PAMAssetTagApi.md#getAssetTags) | **GET** /api/rest/v1/asset-tags | Get list of PAM asset tags
[**getAssetTagsCode**](PAMAssetTagApi.md#getAssetTagsCode) | **GET** /api/rest/v1/asset-tags/{code} | Get a PAM asset tag
[**patchAssetTagsCode**](PAMAssetTagApi.md#patchAssetTagsCode) | **PATCH** /api/rest/v1/asset-tags/{code} | Update/create a PAM asset tag



## getAssetTags

> PAMAssetTags getAssetTags(opts)

Get list of PAM asset tags

This endpoint allows you to get a list of PAM asset tags. PAM asset tags are paginated.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetTagApi();
let opts = {
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.getAssetTags(opts, (error, data, response) => {
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
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**PAMAssetTags**](PAMAssetTags.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getAssetTagsCode

> GetAssetTagsCode200Response getAssetTagsCode(code)

Get a PAM asset tag

This endpoint allows you to get the information about a given PAM asset tag.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetTagApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getAssetTagsCode(code, (error, data, response) => {
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

[**GetAssetTagsCode200Response**](GetAssetTagsCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchAssetTagsCode

> patchAssetTagsCode(code, body)

Update/create a PAM asset tag

This endpoint allows you to update a given PAM asset tag. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no tag exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetTagApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.GetAssetTagsCode200Response(); // GetAssetTagsCode200Response | 
apiInstance.patchAssetTagsCode(code, body, (error, data, response) => {
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
 **body** | [**GetAssetTagsCode200Response**](GetAssetTagsCode200Response.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

