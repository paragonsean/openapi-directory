# MagentoB2B.ReturnsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rmaRmaManagementV1SaveRmaPost**](ReturnsApi.md#rmaRmaManagementV1SaveRmaPost) | **POST** /V1/returns | returns
[**rmaRmaManagementV1SearchGet**](ReturnsApi.md#rmaRmaManagementV1SearchGet) | **GET** /V1/returns | returns



## rmaRmaManagementV1SaveRmaPost

> RmaDataRmaInterface rmaRmaManagementV1SaveRmaPost(opts)

returns

Save RMA

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsApi();
let opts = {
  'rmaRmaManagementV1SaveRmaPostRequest': new MagentoB2B.RmaRmaManagementV1SaveRmaPostRequest() // RmaRmaManagementV1SaveRmaPostRequest | 
};
apiInstance.rmaRmaManagementV1SaveRmaPost(opts, (error, data, response) => {
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
 **rmaRmaManagementV1SaveRmaPostRequest** | [**RmaRmaManagementV1SaveRmaPostRequest**](RmaRmaManagementV1SaveRmaPostRequest.md)|  | [optional] 

### Return type

[**RmaDataRmaInterface**](RmaDataRmaInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## rmaRmaManagementV1SearchGet

> RmaDataRmaSearchResultInterface rmaRmaManagementV1SearchGet(opts)

returns

Return list of rma data objects based on search criteria

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsApi();
let opts = {
  'searchCriteriaFilterGroups0Filters0Field': "searchCriteriaFilterGroups0Filters0Field_example", // String | Field
  'searchCriteriaFilterGroups0Filters0Value': "searchCriteriaFilterGroups0Filters0Value_example", // String | Value
  'searchCriteriaFilterGroups0Filters0ConditionType': "searchCriteriaFilterGroups0Filters0ConditionType_example", // String | Condition type
  'searchCriteriaSortOrders0Field': "searchCriteriaSortOrders0Field_example", // String | Sorting field.
  'searchCriteriaSortOrders0Direction': "searchCriteriaSortOrders0Direction_example", // String | Sorting direction.
  'searchCriteriaPageSize': 56, // Number | Page size.
  'searchCriteriaCurrentPage': 56 // Number | Current page.
};
apiInstance.rmaRmaManagementV1SearchGet(opts, (error, data, response) => {
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
 **searchCriteriaFilterGroups0Filters0Field** | **String**| Field | [optional] 
 **searchCriteriaFilterGroups0Filters0Value** | **String**| Value | [optional] 
 **searchCriteriaFilterGroups0Filters0ConditionType** | **String**| Condition type | [optional] 
 **searchCriteriaSortOrders0Field** | **String**| Sorting field. | [optional] 
 **searchCriteriaSortOrders0Direction** | **String**| Sorting direction. | [optional] 
 **searchCriteriaPageSize** | **Number**| Page size. | [optional] 
 **searchCriteriaCurrentPage** | **Number**| Current page. | [optional] 

### Return type

[**RmaDataRmaSearchResultInterface**](RmaDataRmaSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

