# MagentoB2B.CompanyApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCompanyRepositoryV1GetListGet**](CompanyApi.md#companyCompanyRepositoryV1GetListGet) | **GET** /V1/company/ | company/
[**companyCompanyRepositoryV1SavePost**](CompanyApi.md#companyCompanyRepositoryV1SavePost) | **POST** /V1/company/ | company/



## companyCompanyRepositoryV1GetListGet

> CompanyDataCompanySearchResultsInterface companyCompanyRepositoryV1GetListGet(opts)

company/

Returns the list of companies. The list is an array of objects, and detailed information about item attributes might not be included.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyApi();
let opts = {
  'searchCriteriaFilterGroups0Filters0Field': "searchCriteriaFilterGroups0Filters0Field_example", // String | Field
  'searchCriteriaFilterGroups0Filters0Value': "searchCriteriaFilterGroups0Filters0Value_example", // String | Value
  'searchCriteriaFilterGroups0Filters0ConditionType': "searchCriteriaFilterGroups0Filters0ConditionType_example", // String | Condition type
  'searchCriteriaSortOrders0Field': "searchCriteriaSortOrders0Field_example", // String | Sorting field.
  'searchCriteriaSortOrders0Direction': "searchCriteriaSortOrders0Direction_example", // String | Sorting direction.
  'searchCriteriaPageSize': 56, // Number | Page size.
  'searchCriteriaCurrentPage': 56 // Number | Current page.
};
apiInstance.companyCompanyRepositoryV1GetListGet(opts, (error, data, response) => {
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

[**CompanyDataCompanySearchResultsInterface**](CompanyDataCompanySearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## companyCompanyRepositoryV1SavePost

> CompanyDataCompanyInterface companyCompanyRepositoryV1SavePost(opts)

company/

Create or update a company account.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CompanyApi();
let opts = {
  'companyCompanyRepositoryV1SavePostRequest': new MagentoB2B.CompanyCompanyRepositoryV1SavePostRequest() // CompanyCompanyRepositoryV1SavePostRequest | 
};
apiInstance.companyCompanyRepositoryV1SavePost(opts, (error, data, response) => {
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
 **companyCompanyRepositoryV1SavePostRequest** | [**CompanyCompanyRepositoryV1SavePostRequest**](CompanyCompanyRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CompanyDataCompanyInterface**](CompanyDataCompanyInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

