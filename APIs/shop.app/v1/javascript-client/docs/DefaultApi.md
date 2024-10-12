# Shop.DefaultApi

All URIs are relative to *https://server.shop.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**details**](DefaultApi.md#details) | **GET** /openai/details | Return more details about a list of products.
[**search**](DefaultApi.md#search) | **GET** /openai/search | Search for products



## details

> SearchResponse details(ids)

Return more details about a list of products.

### Example

```javascript
import Shop from 'shop';

let apiInstance = new Shop.DefaultApi();
let ids = "ids_example"; // String | Comma separated list of product ids
apiInstance.details(ids, (error, data, response) => {
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
 **ids** | **String**| Comma separated list of product ids | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## search

> SearchResponse search(opts)

Search for products

### Example

```javascript
import Shop from 'shop';

let apiInstance = new Shop.DefaultApi();
let opts = {
  'query': "query_example", // String | Query string to search for items.
  'priceMin': 3.4, // Number | The minimum price to filter by.
  'priceMax': 3.4, // Number | The maximum price to filter by.
  'similarToId': "similarToId_example", // String | A product id that you want to find similar products for. (Only include one)
  'numResults': "numResults_example" // String | How many results to return. Defaults to 5. It can be a number between 1 and 10.
};
apiInstance.search(opts, (error, data, response) => {
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
 **query** | **String**| Query string to search for items. | [optional] 
 **priceMin** | **Number**| The minimum price to filter by. | [optional] 
 **priceMax** | **Number**| The maximum price to filter by. | [optional] 
 **similarToId** | **String**| A product id that you want to find similar products for. (Only include one) | [optional] 
 **numResults** | **String**| How many results to return. Defaults to 5. It can be a number between 1 and 10. | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

