# ForemApiV1.PagesApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPagesGet**](PagesApi.md#apiPagesGet) | **GET** /api/pages | show details for all pages
[**apiPagesIdDelete**](PagesApi.md#apiPagesIdDelete) | **DELETE** /api/pages/{id} | remove a page
[**apiPagesIdGet**](PagesApi.md#apiPagesIdGet) | **GET** /api/pages/{id} | show details for a page
[**apiPagesIdPut**](PagesApi.md#apiPagesIdPut) | **PUT** /api/pages/{id} | update details for a page
[**apiPagesPost**](PagesApi.md#apiPagesPost) | **POST** /api/pages | pages



## apiPagesGet

> [Page] apiPagesGet()

show details for all pages

This endpoint allows the client to retrieve details for all Page objects.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.PagesApi();
apiInstance.apiPagesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Page]**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPagesIdDelete

> Page apiPagesIdDelete(id)

remove a page

This endpoint allows the client to delete a single Page object, specified by ID.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.PagesApi();
let id = 1; // Number | The ID of the page.
apiInstance.apiPagesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the page. | 

### Return type

[**Page**](Page.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPagesIdGet

> Page apiPagesIdGet(id)

show details for a page

This endpoint allows the client to retrieve details for a single Page object, specified by ID.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.PagesApi();
let id = 1; // Number | The ID of the page.
apiInstance.apiPagesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the page. | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPagesIdPut

> Page apiPagesIdPut(id, opts)

update details for a page

This endpoint allows the client to retrieve details for a single Page object, specified by ID.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.PagesApi();
let id = 1; // Number | The ID of the page.
let opts = {
  'page': new ForemApiV1.Page() // Page | 
};
apiInstance.apiPagesIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The ID of the page. | 
 **page** | [**Page**](Page.md)|  | [optional] 

### Return type

[**Page**](Page.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiPagesPost

> apiPagesPost(opts)

pages

This endpoint allows the client to create a new page.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.PagesApi();
let opts = {
  'apiPagesPostRequest': new ForemApiV1.ApiPagesPostRequest() // ApiPagesPostRequest | 
};
apiInstance.apiPagesPost(opts, (error, data, response) => {
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
 **apiPagesPostRequest** | [**ApiPagesPostRequest**](ApiPagesPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

