# MagentoB2B.TaxClassesClassIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxTaxClassRepositoryV1SavePut**](TaxClassesClassIdApi.md#taxTaxClassRepositoryV1SavePut) | **PUT** /V1/taxClasses/{classId} | taxClasses/{classId}



## taxTaxClassRepositoryV1SavePut

> String taxTaxClassRepositoryV1SavePut(classId, opts)

taxClasses/{classId}

Create a Tax Class

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxClassesClassIdApi();
let classId = "classId_example"; // String | 
let opts = {
  'taxTaxClassRepositoryV1SavePostRequest': new MagentoB2B.TaxTaxClassRepositoryV1SavePostRequest() // TaxTaxClassRepositoryV1SavePostRequest | 
};
apiInstance.taxTaxClassRepositoryV1SavePut(classId, opts, (error, data, response) => {
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
 **classId** | **String**|  | 
 **taxTaxClassRepositoryV1SavePostRequest** | [**TaxTaxClassRepositoryV1SavePostRequest**](TaxTaxClassRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

