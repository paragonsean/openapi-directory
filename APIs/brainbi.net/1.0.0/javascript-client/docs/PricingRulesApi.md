# Brainbi.PricingRulesApi

All URIs are relative to *http://,*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ruleData**](PricingRulesApi.md#ruleData) | **GET** /api/rule/ruleData/1 | Rule Data
[**ruleDataLatest**](PricingRulesApi.md#ruleDataLatest) | **GET** /api/rule/ruleData/1/latest | Rule Data Latest
[**rules**](PricingRulesApi.md#rules) | **GET** /api/rule | Rules



## ruleData

> ruleData(opts)

Rule Data

This resource lists all data that wa saved for pricing rules.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.PricingRulesApi();
let opts = {
  '': "" // String | 
};
apiInstance.ruleData(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ruleDataLatest

> ruleDataLatest(opts)

Rule Data Latest

This resource lists only the latest data point that wa saved for a pricing rule.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.PricingRulesApi();
let opts = {
  '': "" // String | 
};
apiInstance.ruleDataLatest(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## rules

> rules(opts)

Rules

This resource lists all pricing rules that are currently saved in you account.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.PricingRulesApi();
let opts = {
  '': "" // String | 
};
apiInstance.rules(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

