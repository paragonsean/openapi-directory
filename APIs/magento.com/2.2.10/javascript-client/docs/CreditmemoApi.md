# MagentoB2B.CreditmemoApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesCreditmemoRepositoryV1SavePost**](CreditmemoApi.md#salesCreditmemoRepositoryV1SavePost) | **POST** /V1/creditmemo | creditmemo



## salesCreditmemoRepositoryV1SavePost

> SalesDataCreditmemoInterface salesCreditmemoRepositoryV1SavePost(opts)

creditmemo

Performs persist operations for a specified credit memo.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CreditmemoApi();
let opts = {
  'salesCreditmemoRepositoryV1SavePostRequest': new MagentoB2B.SalesCreditmemoRepositoryV1SavePostRequest() // SalesCreditmemoRepositoryV1SavePostRequest | 
};
apiInstance.salesCreditmemoRepositoryV1SavePost(opts, (error, data, response) => {
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
 **salesCreditmemoRepositoryV1SavePostRequest** | [**SalesCreditmemoRepositoryV1SavePostRequest**](SalesCreditmemoRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesDataCreditmemoInterface**](SalesDataCreditmemoInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

