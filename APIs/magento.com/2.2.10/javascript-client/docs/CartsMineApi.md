# MagentoB2B.CartsMineApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteCartManagementV1CreateEmptyCartForCustomerPost**](CartsMineApi.md#quoteCartManagementV1CreateEmptyCartForCustomerPost) | **POST** /V1/carts/mine | carts/mine
[**quoteCartManagementV1GetCartForCustomerGet**](CartsMineApi.md#quoteCartManagementV1GetCartForCustomerGet) | **GET** /V1/carts/mine | carts/mine
[**quoteCartRepositoryV1SavePut**](CartsMineApi.md#quoteCartRepositoryV1SavePut) | **PUT** /V1/carts/mine | carts/mine



## quoteCartManagementV1CreateEmptyCartForCustomerPost

> Number quoteCartManagementV1CreateEmptyCartForCustomerPost()

carts/mine

Creates an empty cart and quote for a specified customer if customer does not have a cart yet.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineApi();
apiInstance.quoteCartManagementV1CreateEmptyCartForCustomerPost((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteCartManagementV1GetCartForCustomerGet

> QuoteDataCartInterface quoteCartManagementV1GetCartForCustomerGet()

carts/mine

Returns information for the cart for a specified customer.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineApi();
apiInstance.quoteCartManagementV1GetCartForCustomerGet((error, data, response) => {
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

[**QuoteDataCartInterface**](QuoteDataCartInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteCartRepositoryV1SavePut

> ErrorResponse quoteCartRepositoryV1SavePut(opts)

carts/mine

Save quote

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineApi();
let opts = {
  'quoteCartRepositoryV1SavePutRequest': new MagentoB2B.QuoteCartRepositoryV1SavePutRequest() // QuoteCartRepositoryV1SavePutRequest | 
};
apiInstance.quoteCartRepositoryV1SavePut(opts, (error, data, response) => {
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
 **quoteCartRepositoryV1SavePutRequest** | [**QuoteCartRepositoryV1SavePutRequest**](QuoteCartRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

