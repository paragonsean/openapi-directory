# MagentoB2B.ProductsRenderInfoApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductRenderListV1GetListGet**](ProductsRenderInfoApi.md#catalogProductRenderListV1GetListGet) | **GET** /V1/products-render-info | products-render-info



## catalogProductRenderListV1GetListGet

> CatalogDataProductRenderSearchResultsInterface catalogProductRenderListV1GetListGet(storeId, currencyCode, opts)

products-render-info

Collect and retrieve the list of product render info This info contains raw prices and formated prices, product name, stock status, store_id, etc

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsRenderInfoApi();
let storeId = 56; // Number | 
let currencyCode = "currencyCode_example"; // String | 
let opts = {
  'searchCriteriaFilterGroups0Filters0Field': "searchCriteriaFilterGroups0Filters0Field_example", // String | Field
  'searchCriteriaFilterGroups0Filters0Value': "searchCriteriaFilterGroups0Filters0Value_example", // String | Value
  'searchCriteriaFilterGroups0Filters0ConditionType': "searchCriteriaFilterGroups0Filters0ConditionType_example", // String | Condition type
  'searchCriteriaSortOrders0Field': "searchCriteriaSortOrders0Field_example", // String | Sorting field.
  'searchCriteriaSortOrders0Direction': "searchCriteriaSortOrders0Direction_example", // String | Sorting direction.
  'searchCriteriaPageSize': 56, // Number | Page size.
  'searchCriteriaCurrentPage': 56 // Number | Current page.
};
apiInstance.catalogProductRenderListV1GetListGet(storeId, currencyCode, opts, (error, data, response) => {
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
 **storeId** | **Number**|  | 
 **currencyCode** | **String**|  | 
 **searchCriteriaFilterGroups0Filters0Field** | **String**| Field | [optional] 
 **searchCriteriaFilterGroups0Filters0Value** | **String**| Value | [optional] 
 **searchCriteriaFilterGroups0Filters0ConditionType** | **String**| Condition type | [optional] 
 **searchCriteriaSortOrders0Field** | **String**| Sorting field. | [optional] 
 **searchCriteriaSortOrders0Direction** | **String**| Sorting direction. | [optional] 
 **searchCriteriaPageSize** | **Number**| Page size. | [optional] 
 **searchCriteriaCurrentPage** | **Number**| Current page. | [optional] 

### Return type

[**CatalogDataProductRenderSearchResultsInterface**](CatalogDataProductRenderSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

