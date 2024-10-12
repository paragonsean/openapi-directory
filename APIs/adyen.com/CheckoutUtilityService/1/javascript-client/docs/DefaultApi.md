# AdyenCheckoutUtilityService.DefaultApi

All URIs are relative to *https://checkout-test.adyen.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**originKeysPost**](DefaultApi.md#originKeysPost) | **POST** /originKeys | Create originKey values for one or more merchant domains.



## originKeysPost

> CheckoutUtilityResponse originKeysPost(opts)

Create originKey values for one or more merchant domains.

This operation takes the origin domains and returns a JSON object containing the corresponding origin keys for the domains.

### Example

```javascript
import AdyenCheckoutUtilityService from 'adyen_checkout_utility_service';

let apiInstance = new AdyenCheckoutUtilityService.DefaultApi();
let opts = {
  'checkoutUtilityRequest': new AdyenCheckoutUtilityService.CheckoutUtilityRequest() // CheckoutUtilityRequest | 
};
apiInstance.originKeysPost(opts, (error, data, response) => {
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
 **checkoutUtilityRequest** | [**CheckoutUtilityRequest**](CheckoutUtilityRequest.md)|  | [optional] 

### Return type

[**CheckoutUtilityResponse**](CheckoutUtilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

