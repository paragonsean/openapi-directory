# MagentoB2B.ProductsAttributesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeRepositoryV1GetListGet**](ProductsAttributesApi.md#catalogProductAttributeRepositoryV1GetListGet) | **GET** /V1/products/attributes | products/attributes
[**catalogProductAttributeRepositoryV1SavePost**](ProductsAttributesApi.md#catalogProductAttributeRepositoryV1SavePost) | **POST** /V1/products/attributes | products/attributes



## catalogProductAttributeRepositoryV1GetListGet

> CatalogDataProductAttributeSearchResultsInterface catalogProductAttributeRepositoryV1GetListGet(opts)

products/attributes

Retrieve all attributes for entity type

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributesApi();
let opts = {
  'searchCriteriaFilterGroups0Filters0Field': "searchCriteriaFilterGroups0Filters0Field_example", // String | Field
  'searchCriteriaFilterGroups0Filters0Value': "searchCriteriaFilterGroups0Filters0Value_example", // String | Value
  'searchCriteriaFilterGroups0Filters0ConditionType': "searchCriteriaFilterGroups0Filters0ConditionType_example", // String | Condition type
  'searchCriteriaSortOrders0Field': "searchCriteriaSortOrders0Field_example", // String | Sorting field.
  'searchCriteriaSortOrders0Direction': "searchCriteriaSortOrders0Direction_example", // String | Sorting direction.
  'searchCriteriaPageSize': 56, // Number | Page size.
  'searchCriteriaCurrentPage': 56 // Number | Current page.
};
apiInstance.catalogProductAttributeRepositoryV1GetListGet(opts, (error, data, response) => {
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

[**CatalogDataProductAttributeSearchResultsInterface**](CatalogDataProductAttributeSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogProductAttributeRepositoryV1SavePost

> CatalogDataProductAttributeInterface catalogProductAttributeRepositoryV1SavePost(opts)

products/attributes

Save attribute data

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributesApi();
let opts = {
  'catalogProductAttributeRepositoryV1SavePostRequest': new MagentoB2B.CatalogProductAttributeRepositoryV1SavePostRequest() // CatalogProductAttributeRepositoryV1SavePostRequest | 
};
apiInstance.catalogProductAttributeRepositoryV1SavePost(opts, (error, data, response) => {
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
 **catalogProductAttributeRepositoryV1SavePostRequest** | [**CatalogProductAttributeRepositoryV1SavePostRequest**](CatalogProductAttributeRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CatalogDataProductAttributeInterface**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

