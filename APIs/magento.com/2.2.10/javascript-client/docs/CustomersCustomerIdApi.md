# MagentoB2B.CustomersCustomerIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerCustomerRepositoryV1DeleteByIdDelete**](CustomersCustomerIdApi.md#customerCustomerRepositoryV1DeleteByIdDelete) | **DELETE** /V1/customers/{customerId} | customers/{customerId}
[**v1CustomersCustomerIdGet**](CustomersCustomerIdApi.md#v1CustomersCustomerIdGet) | **GET** /V1/customers/{customerId} | customers/{customerId}
[**v1CustomersCustomerIdPut**](CustomersCustomerIdApi.md#v1CustomersCustomerIdPut) | **PUT** /V1/customers/{customerId} | customers/{customerId}



## customerCustomerRepositoryV1DeleteByIdDelete

> Boolean customerCustomerRepositoryV1DeleteByIdDelete(customerId)

customers/{customerId}

Delete customer by Customer ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersCustomerIdApi();
let customerId = 56; // Number | 
apiInstance.customerCustomerRepositoryV1DeleteByIdDelete(customerId, (error, data, response) => {
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
 **customerId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CustomersCustomerIdGet

> CustomerDataCustomerInterface v1CustomersCustomerIdGet(customerId)

customers/{customerId}

Get customer by Customer ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersCustomerIdApi();
let customerId = 56; // Number | 
apiInstance.v1CustomersCustomerIdGet(customerId, (error, data, response) => {
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
 **customerId** | **Number**|  | 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CustomersCustomerIdPut

> CustomerDataCustomerInterface v1CustomersCustomerIdPut(customerId, opts)

customers/{customerId}

Create or update a customer.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersCustomerIdApi();
let customerId = "customerId_example"; // String | 
let opts = {
  'customerCustomerRepositoryV1SavePutRequest': new MagentoB2B.CustomerCustomerRepositoryV1SavePutRequest() // CustomerCustomerRepositoryV1SavePutRequest | 
};
apiInstance.v1CustomersCustomerIdPut(customerId, opts, (error, data, response) => {
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
 **customerId** | **String**|  | 
 **customerCustomerRepositoryV1SavePutRequest** | [**CustomerCustomerRepositoryV1SavePutRequest**](CustomerCustomerRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

