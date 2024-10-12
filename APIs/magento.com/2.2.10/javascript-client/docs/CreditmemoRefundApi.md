# MagentoB2B.CreditmemoRefundApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesCreditmemoManagementV1RefundPost**](CreditmemoRefundApi.md#salesCreditmemoManagementV1RefundPost) | **POST** /V1/creditmemo/refund | creditmemo/refund



## salesCreditmemoManagementV1RefundPost

> SalesDataCreditmemoInterface salesCreditmemoManagementV1RefundPost(opts)

creditmemo/refund

Prepare creditmemo to refund and save it.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CreditmemoRefundApi();
let opts = {
  'salesCreditmemoManagementV1RefundPostRequest': new MagentoB2B.SalesCreditmemoManagementV1RefundPostRequest() // SalesCreditmemoManagementV1RefundPostRequest | 
};
apiInstance.salesCreditmemoManagementV1RefundPost(opts, (error, data, response) => {
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
 **salesCreditmemoManagementV1RefundPostRequest** | [**SalesCreditmemoManagementV1RefundPostRequest**](SalesCreditmemoManagementV1RefundPostRequest.md)|  | [optional] 

### Return type

[**SalesDataCreditmemoInterface**](SalesDataCreditmemoInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

