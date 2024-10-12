# Brainbi.ProductsApi

All URIs are relative to *http://,*

Method | HTTP request | Description
------------- | ------------- | -------------
[**betaScrapeProductCopy**](ProductsApi.md#betaScrapeProductCopy) | **GET** /api/analyze/pricing | [BETA] Scrape Product Copy
[**products**](ProductsApi.md#products) | **GET** /api/products | Products
[**products1**](ProductsApi.md#products1) | **DELETE** /api/products/1137 | Products



## betaScrapeProductCopy

> betaScrapeProductCopy(opts)

[BETA] Scrape Product Copy

To update a product, please use the listed attributes listed underneath. 

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.ProductsApi();
let opts = {
  'url': "https://www.apple.com/de/shop/buy-homepod/homepod-mini" // String | 
};
apiInstance.betaScrapeProductCopy(opts, (error, data, response) => {
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
 **url** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## products

> products(opts)

Products

This resource lists all products that are currently saved in you account.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.ProductsApi();
let opts = {
  '': "" // String | 
};
apiInstance.products(opts, (error, data, response) => {
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
 **** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## products1

> products1(opts)

Products

Products

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.ProductsApi();
let opts = {
  '': "" // String | 
};
apiInstance.products1(opts, (error, data, response) => {
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
 **** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined

