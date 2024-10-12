# AkeneoPimRestApi.AssociationTypeApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associationTypesGet**](AssociationTypeApi.md#associationTypesGet) | **GET** /api/rest/v1/association-types/{code} | Get an association type
[**associationTypesGetList**](AssociationTypeApi.md#associationTypesGetList) | **GET** /api/rest/v1/association-types | Get a list of association types
[**associationTypesPatch**](AssociationTypeApi.md#associationTypesPatch) | **PATCH** /api/rest/v1/association-types/{code} | Update/create an association type
[**associationTypesPost**](AssociationTypeApi.md#associationTypesPost) | **POST** /api/rest/v1/association-types | Create a new association type
[**severalAssociationTypesPatch**](AssociationTypeApi.md#severalAssociationTypesPatch) | **PATCH** /api/rest/v1/association-types | Update/create several association types



## associationTypesGet

> AssociationTypesPostRequest associationTypesGet(code)

Get an association type

This endpoint allows you to get the information about a given association type.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssociationTypeApi();
let code = "code_example"; // String | Code of the resource
apiInstance.associationTypesGet(code, (error, data, response) => {
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

[**AssociationTypesPostRequest**](AssociationTypesPostRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## associationTypesGetList

> AssociationTypes associationTypesGetList(opts)

Get a list of association types

This endpoint allows you to get a list of association types. Association types are paginated and sorted by code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssociationTypeApi();
let opts = {
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.associationTypesGetList(opts, (error, data, response) => {
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

[**AssociationTypes**](AssociationTypes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## associationTypesPatch

> associationTypesPatch(code, body)

Update/create an association type

This endpoint allows you to update a given association type. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no association type exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssociationTypeApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.AssociationTypesPostRequest(); // AssociationTypesPostRequest | 
apiInstance.associationTypesPatch(code, body, (error, data, response) => {
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
 **body** | [**AssociationTypesPostRequest**](AssociationTypesPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## associationTypesPost

> associationTypesPost(opts)

Create a new association type

This endpoint allows you to create a new association type.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssociationTypeApi();
let opts = {
  'body': new AkeneoPimRestApi.AssociationTypesPostRequest() // AssociationTypesPostRequest | 
};
apiInstance.associationTypesPost(opts, (error, data, response) => {
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
 **body** | [**AssociationTypesPostRequest**](AssociationTypesPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## severalAssociationTypesPatch

> PatchAssetCategories200Response severalAssociationTypesPatch(opts)

Update/create several association types

This endpoint allows you to update and/or create several association types at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssociationTypeApi();
let opts = {
  'body': new AkeneoPimRestApi.SeveralAssociationTypesPatchRequest() // SeveralAssociationTypesPatchRequest | 
};
apiInstance.severalAssociationTypesPatch(opts, (error, data, response) => {
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
 **body** | [**SeveralAssociationTypesPatchRequest**](SeveralAssociationTypesPatchRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

