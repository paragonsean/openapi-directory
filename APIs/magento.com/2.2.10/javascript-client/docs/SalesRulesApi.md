# MagentoB2B.SalesRulesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRuleRuleRepositoryV1SavePost**](SalesRulesApi.md#salesRuleRuleRepositoryV1SavePost) | **POST** /V1/salesRules | salesRules



## salesRuleRuleRepositoryV1SavePost

> SalesRuleDataRuleInterface salesRuleRuleRepositoryV1SavePost(opts)

salesRules

Save sales rule.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SalesRulesApi();
let opts = {
  'salesRuleRuleRepositoryV1SavePostRequest': new MagentoB2B.SalesRuleRuleRepositoryV1SavePostRequest() // SalesRuleRuleRepositoryV1SavePostRequest | 
};
apiInstance.salesRuleRuleRepositoryV1SavePost(opts, (error, data, response) => {
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
 **salesRuleRuleRepositoryV1SavePostRequest** | [**SalesRuleRuleRepositoryV1SavePostRequest**](SalesRuleRuleRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesRuleDataRuleInterface**](SalesRuleDataRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

