# MagentoB2B.SearchApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchV1SearchGet**](SearchApi.md#searchV1SearchGet) | **GET** /V1/search | search



## searchV1SearchGet

> FrameworkSearchSearchResultInterface searchV1SearchGet(opts)

search

Make Full Text Search and return found Documents

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SearchApi();
let opts = {
  'searchCriteriaRequestName': "searchCriteriaRequestName_example", // String | 
  'searchCriteriaFilterGroups0Filters0Field': "searchCriteriaFilterGroups0Filters0Field_example", // String | Field
  'searchCriteriaFilterGroups0Filters0Value': "searchCriteriaFilterGroups0Filters0Value_example", // String | Value
  'searchCriteriaFilterGroups0Filters0ConditionType': "searchCriteriaFilterGroups0Filters0ConditionType_example", // String | Condition type
  'searchCriteriaSortOrders0Field': "searchCriteriaSortOrders0Field_example", // String | Sorting field.
  'searchCriteriaSortOrders0Direction': "searchCriteriaSortOrders0Direction_example", // String | Sorting direction.
  'searchCriteriaPageSize': 56, // Number | Page size.
  'searchCriteriaCurrentPage': 56 // Number | Current page.
};
apiInstance.searchV1SearchGet(opts, (error, data, response) => {
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
 **searchCriteriaRequestName** | **String**|  | [optional] 
 **searchCriteriaFilterGroups0Filters0Field** | **String**| Field | [optional] 
 **searchCriteriaFilterGroups0Filters0Value** | **String**| Value | [optional] 
 **searchCriteriaFilterGroups0Filters0ConditionType** | **String**| Condition type | [optional] 
 **searchCriteriaSortOrders0Field** | **String**| Sorting field. | [optional] 
 **searchCriteriaSortOrders0Direction** | **String**| Sorting direction. | [optional] 
 **searchCriteriaPageSize** | **Number**| Page size. | [optional] 
 **searchCriteriaCurrentPage** | **Number**| Current page. | [optional] 

### Return type

[**FrameworkSearchSearchResultInterface**](FrameworkSearchSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

