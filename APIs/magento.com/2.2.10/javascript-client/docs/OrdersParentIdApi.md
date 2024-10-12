# MagentoB2B.OrdersParentIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderAddressRepositoryV1SavePut**](OrdersParentIdApi.md#salesOrderAddressRepositoryV1SavePut) | **PUT** /V1/orders/{parent_id} | orders/{parent_id}



## salesOrderAddressRepositoryV1SavePut

> SalesDataOrderAddressInterface salesOrderAddressRepositoryV1SavePut(parentId, opts)

orders/{parent_id}

Performs persist operations for a specified order address.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersParentIdApi();
let parentId = "parentId_example"; // String | 
let opts = {
  'salesOrderAddressRepositoryV1SavePutRequest': new MagentoB2B.SalesOrderAddressRepositoryV1SavePutRequest() // SalesOrderAddressRepositoryV1SavePutRequest | 
};
apiInstance.salesOrderAddressRepositoryV1SavePut(parentId, opts, (error, data, response) => {
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
 **parentId** | **String**|  | 
 **salesOrderAddressRepositoryV1SavePutRequest** | [**SalesOrderAddressRepositoryV1SavePutRequest**](SalesOrderAddressRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**SalesDataOrderAddressInterface**](SalesDataOrderAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

