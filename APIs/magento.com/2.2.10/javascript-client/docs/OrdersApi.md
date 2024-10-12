# MagentoB2B.OrdersApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderRepositoryV1GetListGet**](OrdersApi.md#salesOrderRepositoryV1GetListGet) | **GET** /V1/orders | orders
[**salesOrderRepositoryV1SavePost**](OrdersApi.md#salesOrderRepositoryV1SavePost) | **POST** /V1/orders/ | orders/



## salesOrderRepositoryV1GetListGet

> SalesDataOrderSearchResultInterface salesOrderRepositoryV1GetListGet(opts)

orders

Lists orders that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#OrderRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersApi();
let opts = {
  'searchCriteriaFilterGroups0Filters0Field': "searchCriteriaFilterGroups0Filters0Field_example", // String | Field
  'searchCriteriaFilterGroups0Filters0Value': "searchCriteriaFilterGroups0Filters0Value_example", // String | Value
  'searchCriteriaFilterGroups0Filters0ConditionType': "searchCriteriaFilterGroups0Filters0ConditionType_example", // String | Condition type
  'searchCriteriaSortOrders0Field': "searchCriteriaSortOrders0Field_example", // String | Sorting field.
  'searchCriteriaSortOrders0Direction': "searchCriteriaSortOrders0Direction_example", // String | Sorting direction.
  'searchCriteriaPageSize': 56, // Number | Page size.
  'searchCriteriaCurrentPage': 56 // Number | Current page.
};
apiInstance.salesOrderRepositoryV1GetListGet(opts, (error, data, response) => {
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

[**SalesDataOrderSearchResultInterface**](SalesDataOrderSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## salesOrderRepositoryV1SavePost

> SalesDataOrderInterface salesOrderRepositoryV1SavePost(opts)

orders/

Performs persist operations for a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersApi();
let opts = {
  'salesOrderRepositoryV1SavePostRequest': new MagentoB2B.SalesOrderRepositoryV1SavePostRequest() // SalesOrderRepositoryV1SavePostRequest | 
};
apiInstance.salesOrderRepositoryV1SavePost(opts, (error, data, response) => {
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
 **salesOrderRepositoryV1SavePostRequest** | [**SalesOrderRepositoryV1SavePostRequest**](SalesOrderRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesDataOrderInterface**](SalesDataOrderInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

