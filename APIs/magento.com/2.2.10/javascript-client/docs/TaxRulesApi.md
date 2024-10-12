# MagentoB2B.TaxRulesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxTaxRuleRepositoryV1SavePost**](TaxRulesApi.md#taxTaxRuleRepositoryV1SavePost) | **POST** /V1/taxRules | taxRules
[**taxTaxRuleRepositoryV1SavePut**](TaxRulesApi.md#taxTaxRuleRepositoryV1SavePut) | **PUT** /V1/taxRules | taxRules



## taxTaxRuleRepositoryV1SavePost

> TaxDataTaxRuleInterface taxTaxRuleRepositoryV1SavePost(opts)

taxRules

Save TaxRule

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxRulesApi();
let opts = {
  'taxTaxRuleRepositoryV1SavePutRequest': new MagentoB2B.TaxTaxRuleRepositoryV1SavePutRequest() // TaxTaxRuleRepositoryV1SavePutRequest | 
};
apiInstance.taxTaxRuleRepositoryV1SavePost(opts, (error, data, response) => {
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
 **taxTaxRuleRepositoryV1SavePutRequest** | [**TaxTaxRuleRepositoryV1SavePutRequest**](TaxTaxRuleRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**TaxDataTaxRuleInterface**](TaxDataTaxRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## taxTaxRuleRepositoryV1SavePut

> TaxDataTaxRuleInterface taxTaxRuleRepositoryV1SavePut(opts)

taxRules

Save TaxRule

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxRulesApi();
let opts = {
  'taxTaxRuleRepositoryV1SavePutRequest': new MagentoB2B.TaxTaxRuleRepositoryV1SavePutRequest() // TaxTaxRuleRepositoryV1SavePutRequest | 
};
apiInstance.taxTaxRuleRepositoryV1SavePut(opts, (error, data, response) => {
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
 **taxTaxRuleRepositoryV1SavePutRequest** | [**TaxTaxRuleRepositoryV1SavePutRequest**](TaxTaxRuleRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**TaxDataTaxRuleInterface**](TaxDataTaxRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

