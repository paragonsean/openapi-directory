# AxessoApi.AmzApi

All URIs are relative to *http://api.axesso.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keywordSearch**](AmzApi.md#keywordSearch) | **GET** /amz/amazon-search-by-keyword | fetch results auf a keyword search on Amazon
[**requestBuyRecommendation**](AmzApi.md#requestBuyRecommendation) | **GET** /amz/amazon-lookup-buy-recommendations | request buy recommendations to a given product
[**requestProduct**](AmzApi.md#requestProduct) | **GET** /amz/amazon-lookup-product | lookup product information
[**sortOptions**](AmzApi.md#sortOptions) | **GET** /amz/sort-options | request available sort options to use in keyword search



## keywordSearch

> KeywordSearchResponse keywordSearch(keyword, domainCode, opts)

fetch results auf a keyword search on Amazon



### Example

```javascript
import AxessoApi from 'axesso_api';

let apiInstance = new AxessoApi.AmzApi();
let keyword = "keyword_example"; // String | keyword to search
let domainCode = "domainCode_example"; // String | domain for the search
let opts = {
  'sortBy': "'relevanceblender'", // String | sort option
  'numberOfProducts': 56 // Number | number of the results (max 20)
};
apiInstance.keywordSearch(keyword, domainCode, opts, (error, data, response) => {
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
 **keyword** | **String**| keyword to search | 
 **domainCode** | **String**| domain for the search | 
 **sortBy** | **String**| sort option | [optional] [default to &#39;relevanceblender&#39;]
 **numberOfProducts** | **Number**| number of the results (max 20) | [optional] 

### Return type

[**KeywordSearchResponse**](KeywordSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestBuyRecommendation

> BuyRecommendationResponse requestBuyRecommendation(url)

request buy recommendations to a given product



### Example

```javascript
import AxessoApi from 'axesso_api';

let apiInstance = new AxessoApi.AmzApi();
let url = "url_example"; // String | The url of the requested product.
apiInstance.requestBuyRecommendation(url, (error, data, response) => {
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
 **url** | **String**| The url of the requested product. | 

### Return type

[**BuyRecommendationResponse**](BuyRecommendationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestProduct

> ProductDetailsResponse requestProduct(url, opts)

lookup product information



### Example

```javascript
import AxessoApi from 'axesso_api';

let apiInstance = new AxessoApi.AmzApi();
let url = "url_example"; // String | The url of the requested product.
let opts = {
  'size': "size_example" // String | Size parameter if available.
};
apiInstance.requestProduct(url, opts, (error, data, response) => {
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
 **url** | **String**| The url of the requested product. | 
 **size** | **String**| Size parameter if available. | [optional] 

### Return type

[**ProductDetailsResponse**](ProductDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sortOptions

> SortOptionResponse sortOptions()

request available sort options to use in keyword search



### Example

```javascript
import AxessoApi from 'axesso_api';

let apiInstance = new AxessoApi.AmzApi();
apiInstance.sortOptions((error, data, response) => {
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

[**SortOptionResponse**](SortOptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

