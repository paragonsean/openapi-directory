# TokenJayApiServices.TokenPricesApi

All URIs are relative to *https://api.tokenjay.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTokenPrice**](TokenPricesApi.md#getTokenPrice) | **GET** /tokens/prices/{tokenId} | Lists price and available volume for a certain token
[**getTokenPrices**](TokenPricesApi.md#getTokenPrices) | **GET** /tokens/prices/all | Lists all token prices and available volume



## getTokenPrice

> TokenPrice getTokenPrice(tokenId)

Lists price and available volume for a certain token

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.TokenPricesApi();
let tokenId = "tokenId_example"; // String | 
apiInstance.getTokenPrice(tokenId, (error, data, response) => {
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
 **tokenId** | **String**|  | 

### Return type

[**TokenPrice**](TokenPrice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getTokenPrices

> [TokenPrice] getTokenPrices()

Lists all token prices and available volume

### Example

```javascript
import TokenJayApiServices from 'token_jay_api_services';

let apiInstance = new TokenJayApiServices.TokenPricesApi();
apiInstance.getTokenPrices((error, data, response) => {
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

[**[TokenPrice]**](TokenPrice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

