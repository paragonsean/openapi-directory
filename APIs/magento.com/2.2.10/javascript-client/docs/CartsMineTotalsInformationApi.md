# MagentoB2B.CartsMineTotalsInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutTotalsInformationManagementV1CalculatePost**](CartsMineTotalsInformationApi.md#checkoutTotalsInformationManagementV1CalculatePost) | **POST** /V1/carts/mine/totals-information | carts/mine/totals-information



## checkoutTotalsInformationManagementV1CalculatePost

> QuoteDataTotalsInterface checkoutTotalsInformationManagementV1CalculatePost(opts)

carts/mine/totals-information

Calculate quote totals based on address and shipping method.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineTotalsInformationApi();
let opts = {
  'checkoutTotalsInformationManagementV1CalculatePostRequest': new MagentoB2B.CheckoutTotalsInformationManagementV1CalculatePostRequest() // CheckoutTotalsInformationManagementV1CalculatePostRequest | 
};
apiInstance.checkoutTotalsInformationManagementV1CalculatePost(opts, (error, data, response) => {
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
 **checkoutTotalsInformationManagementV1CalculatePostRequest** | [**CheckoutTotalsInformationManagementV1CalculatePostRequest**](CheckoutTotalsInformationManagementV1CalculatePostRequest.md)|  | [optional] 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

