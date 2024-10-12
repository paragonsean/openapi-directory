# DropX.LookUpApi

All URIs are relative to *http://dropx.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsLinkSearchGet**](LookUpApi.md#productsLinkSearchGet) | **GET** /products/link-search | Search for similar products by providing a link to any e-commerce product.
[**productsLinkSearchV2Get**](LookUpApi.md#productsLinkSearchV2Get) | **GET** /products/link-search-v2 | Search for similar products by providing a link to any e-commerce product.
[**productsSearchGet**](LookUpApi.md#productsSearchGet) | **GET** /products/search | Search for any product using title
[**productsSearchV2Get**](LookUpApi.md#productsSearchV2Get) | **GET** /products/search-v2 | Search for any product using title
[**productsTitleSearchGet**](LookUpApi.md#productsTitleSearchGet) | **GET** /products/title-search | Search for any product using title



## productsLinkSearchGet

> productsLinkSearchGet(url, opts)

Search for similar products by providing a link to any e-commerce product.

Returns list of e-commerce product that are close to the one provided -- one from each provider

### Example

```javascript
import DropX from 'drop_x';
let defaultClient = DropX.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DropX.LookUpApi();
let url = "url_example"; // String | URL must be a url encoded value
let opts = {
  'providers': "providers_example" // String | A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a ',' seperated values to filter response by required e-commerce providers
};
apiInstance.productsLinkSearchGet(url, opts, (error, data, response) => {
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
 **url** | **String**| URL must be a url encoded value | 
 **providers** | **String**| A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsLinkSearchV2Get

> productsLinkSearchV2Get(url, opts)

Search for similar products by providing a link to any e-commerce product.

Returns list of e-commerce product that are close to the one provided -- one from each provider

### Example

```javascript
import DropX from 'drop_x';
let defaultClient = DropX.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DropX.LookUpApi();
let url = "url_example"; // String | URL must be a url encoded value
let opts = {
  'providers': "providers_example" // String | A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a ',' seperated values to filter response by required e-commerce providers
};
apiInstance.productsLinkSearchV2Get(url, opts, (error, data, response) => {
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
 **url** | **String**| URL must be a url encoded value | 
 **providers** | **String**| A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsSearchGet

> productsSearchGet(term, opts)

Search for any product using title

Returns one unique result from every provider that dropx.io tracks

### Example

```javascript
import DropX from 'drop_x';
let defaultClient = DropX.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DropX.LookUpApi();
let term = "term_example"; // String | search terms giving any title of products that are sold online
let opts = {
  'providers': "providers_example" // String | A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a ',' seperated values to filter response by required e-commerce providers
};
apiInstance.productsSearchGet(term, opts, (error, data, response) => {
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
 **term** | **String**| search terms giving any title of products that are sold online | 
 **providers** | **String**| A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsSearchV2Get

> productsSearchV2Get(term, opts)

Search for any product using title

Returns one unique result from every provider that dropx.io tracks

### Example

```javascript
import DropX from 'drop_x';
let defaultClient = DropX.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DropX.LookUpApi();
let term = "term_example"; // String | search terms giving any title of products that are sold online
let opts = {
  'providers': "providers_example" // String | A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a ',' seperated values to filter response by required e-commerce providers
};
apiInstance.productsSearchV2Get(term, opts, (error, data, response) => {
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
 **term** | **String**| search terms giving any title of products that are sold online | 
 **providers** | **String**| A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsTitleSearchGet

> productsTitleSearchGet(term)

Search for any product using title

Returns list of product ids

### Example

```javascript
import DropX from 'drop_x';
let defaultClient = DropX.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DropX.LookUpApi();
let term = "term_example"; // String | search terms giving any title of products that are sold online
apiInstance.productsTitleSearchGet(term, (error, data, response) => {
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
 **term** | **String**| search terms giving any title of products that are sold online | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

