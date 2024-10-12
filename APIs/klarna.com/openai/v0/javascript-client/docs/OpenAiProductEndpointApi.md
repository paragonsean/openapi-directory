# OpenAiKlarnaProductApi.OpenAiProductEndpointApi

All URIs are relative to *https://www.klarna.com/us/shopping*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsUsingGET**](OpenAiProductEndpointApi.md#productsUsingGET) | **GET** /public/openai/v0/products | API for fetching Klarna product information



## productsUsingGET

> ProductResponse productsUsingGET(q, opts)

API for fetching Klarna product information

### Example

```javascript
import OpenAiKlarnaProductApi from 'open_ai_klarna_product_api';

let apiInstance = new OpenAiKlarnaProductApi.OpenAiProductEndpointApi();
let q = "q_example"; // String | A precise query that matches one very small category or product that needs to be searched for to find the products the user is looking for. If the user explicitly stated what they want, use that as a query. The query is as specific as possible to the product name or category mentioned by the user in its singular form, and don't contain any clarifiers like latest, newest, cheapest, budget, premium, expensive or similar. The query is always taken from the latest topic, if there is a new topic a new query is started.
let opts = {
  'size': 56, // Number | number of products returned
  'budget': 56 // Number | maximum price of the matching product in local currency, filters results
};
apiInstance.productsUsingGET(q, opts, (error, data, response) => {
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
 **q** | **String**| A precise query that matches one very small category or product that needs to be searched for to find the products the user is looking for. If the user explicitly stated what they want, use that as a query. The query is as specific as possible to the product name or category mentioned by the user in its singular form, and don&#39;t contain any clarifiers like latest, newest, cheapest, budget, premium, expensive or similar. The query is always taken from the latest topic, if there is a new topic a new query is started. | 
 **size** | **Number**| number of products returned | [optional] 
 **budget** | **Number**| maximum price of the matching product in local currency, filters results | [optional] 

### Return type

[**ProductResponse**](ProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

