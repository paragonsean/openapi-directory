# MagentoB2B.GuestCartsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestCartManagementV1CreateEmptyCartPost**](GuestCartsApi.md#quoteGuestCartManagementV1CreateEmptyCartPost) | **POST** /V1/guest-carts | guest-carts



## quoteGuestCartManagementV1CreateEmptyCartPost

> String quoteGuestCartManagementV1CreateEmptyCartPost()

guest-carts

Enable an customer or guest user to create an empty cart and quote for an anonymous customer.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsApi();
apiInstance.quoteGuestCartManagementV1CreateEmptyCartPost((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

