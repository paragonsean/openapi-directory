# MagentoB2B.SalesRulesRuleIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRuleRuleRepositoryV1DeleteByIdDelete**](SalesRulesRuleIdApi.md#salesRuleRuleRepositoryV1DeleteByIdDelete) | **DELETE** /V1/salesRules/{ruleId} | salesRules/{ruleId}
[**salesRuleRuleRepositoryV1GetByIdGet**](SalesRulesRuleIdApi.md#salesRuleRuleRepositoryV1GetByIdGet) | **GET** /V1/salesRules/{ruleId} | salesRules/{ruleId}
[**salesRuleRuleRepositoryV1SavePut**](SalesRulesRuleIdApi.md#salesRuleRuleRepositoryV1SavePut) | **PUT** /V1/salesRules/{ruleId} | salesRules/{ruleId}



## salesRuleRuleRepositoryV1DeleteByIdDelete

> Boolean salesRuleRuleRepositoryV1DeleteByIdDelete(ruleId)

salesRules/{ruleId}

Delete rule by ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SalesRulesRuleIdApi();
let ruleId = 56; // Number | 
apiInstance.salesRuleRuleRepositoryV1DeleteByIdDelete(ruleId, (error, data, response) => {
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


## salesRuleRuleRepositoryV1GetByIdGet

> SalesRuleDataRuleInterface salesRuleRuleRepositoryV1GetByIdGet(ruleId)

salesRules/{ruleId}

Get rule by ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SalesRulesRuleIdApi();
let ruleId = 56; // Number | 
apiInstance.salesRuleRuleRepositoryV1GetByIdGet(ruleId, (error, data, response) => {
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

[**SalesRuleDataRuleInterface**](SalesRuleDataRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## salesRuleRuleRepositoryV1SavePut

> SalesRuleDataRuleInterface salesRuleRuleRepositoryV1SavePut(ruleId, opts)

salesRules/{ruleId}

Save sales rule.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SalesRulesRuleIdApi();
let ruleId = "ruleId_example"; // String | 
let opts = {
  'salesRuleRuleRepositoryV1SavePostRequest': new MagentoB2B.SalesRuleRuleRepositoryV1SavePostRequest() // SalesRuleRuleRepositoryV1SavePostRequest | 
};
apiInstance.salesRuleRuleRepositoryV1SavePut(ruleId, opts, (error, data, response) => {
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
 **ruleId** | **String**|  | 
 **salesRuleRuleRepositoryV1SavePostRequest** | [**SalesRuleRuleRepositoryV1SavePostRequest**](SalesRuleRuleRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesRuleDataRuleInterface**](SalesRuleDataRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

