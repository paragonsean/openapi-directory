# MagentoB2B.AmazonBillingAddressAmazonOrderReferenceIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amazonPaymentAddressManagementV1GetBillingAddressPut**](AmazonBillingAddressAmazonOrderReferenceIdApi.md#amazonPaymentAddressManagementV1GetBillingAddressPut) | **PUT** /V1/amazon-billing-address/{amazonOrderReferenceId} | amazon-billing-address/{amazonOrderReferenceId}



## amazonPaymentAddressManagementV1GetBillingAddressPut

> String amazonPaymentAddressManagementV1GetBillingAddressPut(amazonOrderReferenceId, opts)

amazon-billing-address/{amazonOrderReferenceId}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AmazonBillingAddressAmazonOrderReferenceIdApi();
let amazonOrderReferenceId = "amazonOrderReferenceId_example"; // String | 
let opts = {
  'amazonPaymentAddressManagementV1GetBillingAddressPutRequest': new MagentoB2B.AmazonPaymentAddressManagementV1GetBillingAddressPutRequest() // AmazonPaymentAddressManagementV1GetBillingAddressPutRequest | 
};
apiInstance.amazonPaymentAddressManagementV1GetBillingAddressPut(amazonOrderReferenceId, opts, (error, data, response) => {
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

