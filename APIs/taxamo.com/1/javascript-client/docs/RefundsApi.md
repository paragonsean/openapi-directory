# Taxamo.RefundsApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRefund**](RefundsApi.md#createRefund) | **POST** /api/v1/transactions/{key}/refunds | Create a refund
[**listRefunds**](RefundsApi.md#listRefunds) | **GET** /api/v1/transactions/{key}/refunds | Get transaction refunds



## createRefund

> CreateRefundOut createRefund(key, input)

Create a refund

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.RefundsApi();
let key = "key_example"; // String | Transaction key.
let input = new Taxamo.CreateRefundIn(); // CreateRefundIn | Input
apiInstance.createRefund(key, input, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 
 **input** | [**CreateRefundIn**](CreateRefundIn.md)| Input | 

### Return type

[**CreateRefundOut**](CreateRefundOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRefunds

> ListRefundsOut listRefunds(key)

Get transaction refunds

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.RefundsApi();
let key = "key_example"; // String | Transaction key.
apiInstance.listRefunds(key, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 

### Return type

[**ListRefundsOut**](ListRefundsOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

