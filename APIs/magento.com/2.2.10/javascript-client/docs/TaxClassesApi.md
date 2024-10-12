# MagentoB2B.TaxClassesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxTaxClassRepositoryV1SavePost**](TaxClassesApi.md#taxTaxClassRepositoryV1SavePost) | **POST** /V1/taxClasses | taxClasses



## taxTaxClassRepositoryV1SavePost

> String taxTaxClassRepositoryV1SavePost(opts)

taxClasses

Create a Tax Class

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxClassesApi();
let opts = {
  'taxTaxClassRepositoryV1SavePostRequest': new MagentoB2B.TaxTaxClassRepositoryV1SavePostRequest() // TaxTaxClassRepositoryV1SavePostRequest | 
};
apiInstance.taxTaxClassRepositoryV1SavePost(opts, (error, data, response) => {
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
 **taxTaxClassRepositoryV1SavePostRequest** | [**TaxTaxClassRepositoryV1SavePostRequest**](TaxTaxClassRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

