# MagentoB2B.CustomersMeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerCustomerRepositoryV1GetByIdGet**](CustomersMeApi.md#customerCustomerRepositoryV1GetByIdGet) | **GET** /V1/customers/me | customers/me
[**customerCustomerRepositoryV1SavePut**](CustomersMeApi.md#customerCustomerRepositoryV1SavePut) | **PUT** /V1/customers/me | customers/me



## customerCustomerRepositoryV1GetByIdGet

> CustomerDataCustomerInterface customerCustomerRepositoryV1GetByIdGet()

customers/me

Get customer by Customer ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersMeApi();
apiInstance.customerCustomerRepositoryV1GetByIdGet((error, data, response) => {
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

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## customerCustomerRepositoryV1SavePut

> CustomerDataCustomerInterface customerCustomerRepositoryV1SavePut(opts)

customers/me

Create or update a customer.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersMeApi();
let opts = {
  'customerCustomerRepositoryV1SavePutRequest': new MagentoB2B.CustomerCustomerRepositoryV1SavePutRequest() // CustomerCustomerRepositoryV1SavePutRequest | 
};
apiInstance.customerCustomerRepositoryV1SavePut(opts, (error, data, response) => {
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
 **customerCustomerRepositoryV1SavePutRequest** | [**CustomerCustomerRepositoryV1SavePutRequest**](CustomerCustomerRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

