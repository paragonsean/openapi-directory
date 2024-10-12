# MagentoB2B.TaxRulesRuleIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxTaxRuleRepositoryV1DeleteByIdDelete**](TaxRulesRuleIdApi.md#taxTaxRuleRepositoryV1DeleteByIdDelete) | **DELETE** /V1/taxRules/{ruleId} | taxRules/{ruleId}
[**taxTaxRuleRepositoryV1GetGet**](TaxRulesRuleIdApi.md#taxTaxRuleRepositoryV1GetGet) | **GET** /V1/taxRules/{ruleId} | taxRules/{ruleId}



## taxTaxRuleRepositoryV1DeleteByIdDelete

> Boolean taxTaxRuleRepositoryV1DeleteByIdDelete(ruleId)

taxRules/{ruleId}

Delete TaxRule

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxRulesRuleIdApi();
let ruleId = 56; // Number | 
apiInstance.taxTaxRuleRepositoryV1DeleteByIdDelete(ruleId, (error, data, response) => {
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
 **ruleId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## taxTaxRuleRepositoryV1GetGet

> TaxDataTaxRuleInterface taxTaxRuleRepositoryV1GetGet(ruleId)

taxRules/{ruleId}

Get TaxRule

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxRulesRuleIdApi();
let ruleId = 56; // Number | 
apiInstance.taxTaxRuleRepositoryV1GetGet(ruleId, (error, data, response) => {
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
 **ruleId** | **Number**|  | 

### Return type

[**TaxDataTaxRuleInterface**](TaxDataTaxRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

