# MagentoB2B.TransactionsIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesTransactionRepositoryV1GetGet**](TransactionsIdApi.md#salesTransactionRepositoryV1GetGet) | **GET** /V1/transactions/{id} | transactions/{id}



## salesTransactionRepositoryV1GetGet

> SalesDataTransactionInterface salesTransactionRepositoryV1GetGet(id)

transactions/{id}

Loads a specified transaction.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TransactionsIdApi();
let id = 56; // Number | The transaction ID.
apiInstance.salesTransactionRepositoryV1GetGet(id, (error, data, response) => {
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
 **id** | **Number**| The transaction ID. | 

### Return type

[**SalesDataTransactionInterface**](SalesDataTransactionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

