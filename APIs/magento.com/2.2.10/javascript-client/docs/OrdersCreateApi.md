# MagentoB2B.OrdersCreateApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderRepositoryV1SavePut**](OrdersCreateApi.md#salesOrderRepositoryV1SavePut) | **PUT** /V1/orders/create | orders/create



## salesOrderRepositoryV1SavePut

> SalesDataOrderInterface salesOrderRepositoryV1SavePut(opts)

orders/create

Performs persist operations for a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersCreateApi();
let opts = {
  'salesOrderRepositoryV1SavePostRequest': new MagentoB2B.SalesOrderRepositoryV1SavePostRequest() // SalesOrderRepositoryV1SavePostRequest | 
};
apiInstance.salesOrderRepositoryV1SavePut(opts, (error, data, response) => {
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
 **salesOrderRepositoryV1SavePostRequest** | [**SalesOrderRepositoryV1SavePostRequest**](SalesOrderRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesDataOrderInterface**](SalesDataOrderInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

