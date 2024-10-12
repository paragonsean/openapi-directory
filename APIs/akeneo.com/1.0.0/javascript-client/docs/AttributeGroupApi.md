# AkeneoPimRestApi.AttributeGroupApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributeGroupsGet**](AttributeGroupApi.md#attributeGroupsGet) | **GET** /api/rest/v1/attribute-groups/{code} | Get an attribute group
[**attributeGroupsGetList**](AttributeGroupApi.md#attributeGroupsGetList) | **GET** /api/rest/v1/attribute-groups | Get list of attribute groups
[**attributeGroupsPatch**](AttributeGroupApi.md#attributeGroupsPatch) | **PATCH** /api/rest/v1/attribute-groups/{code} | Update/create an attribute group
[**attributeGroupsPost**](AttributeGroupApi.md#attributeGroupsPost) | **POST** /api/rest/v1/attribute-groups | Create a new attribute group
[**severalAttributeGroupsPatch**](AttributeGroupApi.md#severalAttributeGroupsPatch) | **PATCH** /api/rest/v1/attribute-groups | Update/create several attribute groups



## attributeGroupsGet

> AttributeGroupsPostRequest attributeGroupsGet(code)

Get an attribute group

This endpoint allows you to get the information about a given attribute group.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeGroupApi();
let code = "code_example"; // String | Code of the resource
apiInstance.attributeGroupsGet(code, (error, data, response) => {
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

[**AttributeGroupsPostRequest**](AttributeGroupsPostRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## attributeGroupsGetList

> AttributeGroups attributeGroupsGetList(opts)

Get list of attribute groups

This endpoint allows you to get a list of attribute groups. Attribute groups are paginated and sorted by code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeGroupApi();
let opts = {
  'search': "search_example", // String | Filter attribute groups, for more details see the <a href=\"/documentation/filter.html#filter-attribute-groups\">Filters</a> section.
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.attributeGroupsGetList(opts, (error, data, response) => {
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
 **search** | **String**| Filter attribute groups, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-attribute-groups\&quot;&gt;Filters&lt;/a&gt; section. | [optional] 
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**AttributeGroups**](AttributeGroups.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## attributeGroupsPatch

> attributeGroupsPatch(code, body)

Update/create an attribute group

This endpoint allows you to update a given attribute group. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no attribute group exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeGroupApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.AttributeGroupsPostRequest(); // AttributeGroupsPostRequest | 
apiInstance.attributeGroupsPatch(code, body, (error, data, response) => {
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
 **body** | [**AttributeGroupsPostRequest**](AttributeGroupsPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## attributeGroupsPost

> attributeGroupsPost(opts)

Create a new attribute group

This endpoint allows you to create a new attribute group.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeGroupApi();
let opts = {
  'body': new AkeneoPimRestApi.AttributeGroupsPostRequest() // AttributeGroupsPostRequest | 
};
apiInstance.attributeGroupsPost(opts, (error, data, response) => {
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
 **body** | [**AttributeGroupsPostRequest**](AttributeGroupsPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## severalAttributeGroupsPatch

> PatchAssetCategories200Response severalAttributeGroupsPatch(opts)

Update/create several attribute groups

This endpoint allows you to update and/or create several attribute groups at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeGroupApi();
let opts = {
  'body': new AkeneoPimRestApi.SeveralAttributeGroupsPatchRequest() // SeveralAttributeGroupsPatchRequest | 
};
apiInstance.severalAttributeGroupsPatch(opts, (error, data, response) => {
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
 **body** | [**SeveralAttributeGroupsPatchRequest**](SeveralAttributeGroupsPatchRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

