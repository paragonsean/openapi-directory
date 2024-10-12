# MagentoB2B.CartsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteCartManagementV1CreateEmptyCartPost**](CartsApi.md#quoteCartManagementV1CreateEmptyCartPost) | **POST** /V1/carts/ | carts/



## quoteCartManagementV1CreateEmptyCartPost

> Number quoteCartManagementV1CreateEmptyCartPost()

carts/

Creates an empty cart and quote for a guest.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsApi();
apiInstance.quoteCartManagementV1CreateEmptyCartPost((error, data, response) => {
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

