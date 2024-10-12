# Reverb.ProductsApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsReviewsIdGet**](ProductsApi.md#productsReviewsIdGet) | **GET** /products/reviews/{id} | View a review
[**productsReviewsIdPut**](ProductsApi.md#productsReviewsIdPut) | **PUT** /products/reviews/{id} | Update a review
[**productsSlugReviewsGet**](ProductsApi.md#productsSlugReviewsGet) | **GET** /products/{slug}/reviews | View reviews of a comparison shopping page
[**productsSlugReviewsPost**](ProductsApi.md#productsSlugReviewsPost) | **POST** /products/{slug}/reviews | Create a review for a product



## productsReviewsIdGet

> productsReviewsIdGet(id)

View a review

View a review

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ProductsApi();
let id = "id_example"; // String | 
apiInstance.productsReviewsIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsReviewsIdPut

> productsReviewsIdPut(id, opts)

Update a review

Update a review

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ProductsApi();
let id = "id_example"; // String | 
let opts = {
  'productsReviewsIdPutRequest': new Reverb.ProductsReviewsIdPutRequest() // ProductsReviewsIdPutRequest | the content of the request
};
apiInstance.productsReviewsIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **productsReviewsIdPutRequest** | [**ProductsReviewsIdPutRequest**](ProductsReviewsIdPutRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productsSlugReviewsGet

> productsSlugReviewsGet(slug)

View reviews of a comparison shopping page

View reviews of a comparison shopping page

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ProductsApi();
let slug = "slug_example"; // String | 
apiInstance.productsSlugReviewsGet(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsSlugReviewsPost

> productsSlugReviewsPost(slug)

Create a review for a product

Create a review for a product

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ProductsApi();
let slug = "slug_example"; // String | 
apiInstance.productsSlugReviewsPost(slug, (error, data, response) => {
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
 **slug** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

