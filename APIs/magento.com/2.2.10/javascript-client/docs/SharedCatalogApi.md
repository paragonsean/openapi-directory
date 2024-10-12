# MagentoB2B.SharedCatalogApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogSharedCatalogRepositoryV1GetListGet**](SharedCatalogApi.md#sharedCatalogSharedCatalogRepositoryV1GetListGet) | **GET** /V1/sharedCatalog/ | sharedCatalog/
[**sharedCatalogSharedCatalogRepositoryV1SavePost**](SharedCatalogApi.md#sharedCatalogSharedCatalogRepositoryV1SavePost) | **POST** /V1/sharedCatalog | sharedCatalog



## sharedCatalogSharedCatalogRepositoryV1GetListGet

> SharedCatalogDataSearchResultsInterface sharedCatalogSharedCatalogRepositoryV1GetListGet(opts)

sharedCatalog/

Return the list of shared catalogs and basic properties for each catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogApi();
let opts = {
  'searchCriteriaFilterGroups0Filters0Field': "searchCriteriaFilterGroups0Filters0Field_example", // String | Field
  'searchCriteriaFilterGroups0Filters0Value': "searchCriteriaFilterGroups0Filters0Value_example", // String | Value
  'searchCriteriaFilterGroups0Filters0ConditionType': "searchCriteriaFilterGroups0Filters0ConditionType_example", // String | Condition type
  'searchCriteriaSortOrders0Field': "searchCriteriaSortOrders0Field_example", // String | Sorting field.
  'searchCriteriaSortOrders0Direction': "searchCriteriaSortOrders0Direction_example", // String | Sorting direction.
  'searchCriteriaPageSize': 56, // Number | Page size.
  'searchCriteriaCurrentPage': 56 // Number | Current page.
};
apiInstance.sharedCatalogSharedCatalogRepositoryV1GetListGet(opts, (error, data, response) => {
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

[**SharedCatalogDataSearchResultsInterface**](SharedCatalogDataSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## sharedCatalogSharedCatalogRepositoryV1SavePost

> Number sharedCatalogSharedCatalogRepositoryV1SavePost(opts)

sharedCatalog

Create or update Shared Catalog service.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogApi();
let opts = {
  'sharedCatalogSharedCatalogRepositoryV1SavePostRequest': new MagentoB2B.SharedCatalogSharedCatalogRepositoryV1SavePostRequest() // SharedCatalogSharedCatalogRepositoryV1SavePostRequest | 
};
apiInstance.sharedCatalogSharedCatalogRepositoryV1SavePost(opts, (error, data, response) => {
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
 **sharedCatalogSharedCatalogRepositoryV1SavePostRequest** | [**SharedCatalogSharedCatalogRepositoryV1SavePostRequest**](SharedCatalogSharedCatalogRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

