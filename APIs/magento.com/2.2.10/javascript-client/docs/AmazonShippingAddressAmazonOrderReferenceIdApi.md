# MagentoB2B.AmazonShippingAddressAmazonOrderReferenceIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amazonPaymentAddressManagementV1GetShippingAddressPut**](AmazonShippingAddressAmazonOrderReferenceIdApi.md#amazonPaymentAddressManagementV1GetShippingAddressPut) | **PUT** /V1/amazon-shipping-address/{amazonOrderReferenceId} | amazon-shipping-address/{amazonOrderReferenceId}



## amazonPaymentAddressManagementV1GetShippingAddressPut

> String amazonPaymentAddressManagementV1GetShippingAddressPut(amazonOrderReferenceId, opts)

amazon-shipping-address/{amazonOrderReferenceId}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AmazonShippingAddressAmazonOrderReferenceIdApi();
let amazonOrderReferenceId = "amazonOrderReferenceId_example"; // String | 
let opts = {
  'amazonPaymentAddressManagementV1GetBillingAddressPutRequest': new MagentoB2B.AmazonPaymentAddressManagementV1GetBillingAddressPutRequest() // AmazonPaymentAddressManagementV1GetBillingAddressPutRequest | 
};
apiInstance.amazonPaymentAddressManagementV1GetShippingAddressPut(amazonOrderReferenceId, opts, (error, data, response) => {
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
 **amazonOrderReferenceId** | **String**|  | 
 **amazonPaymentAddressManagementV1GetBillingAddressPutRequest** | [**AmazonPaymentAddressManagementV1GetBillingAddressPutRequest**](AmazonPaymentAddressManagementV1GetBillingAddressPutRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

