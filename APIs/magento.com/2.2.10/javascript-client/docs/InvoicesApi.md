# MagentoB2B.InvoicesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesInvoiceRepositoryV1GetListGet**](InvoicesApi.md#salesInvoiceRepositoryV1GetListGet) | **GET** /V1/invoices | invoices
[**salesInvoiceRepositoryV1SavePost**](InvoicesApi.md#salesInvoiceRepositoryV1SavePost) | **POST** /V1/invoices/ | invoices/



## salesInvoiceRepositoryV1GetListGet

> SalesDataInvoiceSearchResultInterface salesInvoiceRepositoryV1GetListGet(opts)

invoices

Lists invoices that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#InvoiceRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.InvoicesApi();
let opts = {
  'searchCriteriaFilterGroups0Filters0Field': "searchCriteriaFilterGroups0Filters0Field_example", // String | Field
  'searchCriteriaFilterGroups0Filters0Value': "searchCriteriaFilterGroups0Filters0Value_example", // String | Value
  'searchCriteriaFilterGroups0Filters0ConditionType': "searchCriteriaFilterGroups0Filters0ConditionType_example", // String | Condition type
  'searchCriteriaSortOrders0Field': "searchCriteriaSortOrders0Field_example", // String | Sorting field.
  'searchCriteriaSortOrders0Direction': "searchCriteriaSortOrders0Direction_example", // String | Sorting direction.
  'searchCriteriaPageSize': 56, // Number | Page size.
  'searchCriteriaCurrentPage': 56 // Number | Current page.
};
apiInstance.salesInvoiceRepositoryV1GetListGet(opts, (error, data, response) => {
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

[**SalesDataInvoiceSearchResultInterface**](SalesDataInvoiceSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## salesInvoiceRepositoryV1SavePost

> SalesDataInvoiceInterface salesInvoiceRepositoryV1SavePost(opts)

invoices/

Performs persist operations for a specified invoice.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.InvoicesApi();
let opts = {
  'salesInvoiceRepositoryV1SavePostRequest': new MagentoB2B.SalesInvoiceRepositoryV1SavePostRequest() // SalesInvoiceRepositoryV1SavePostRequest | 
};
apiInstance.salesInvoiceRepositoryV1SavePost(opts, (error, data, response) => {
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
 **salesInvoiceRepositoryV1SavePostRequest** | [**SalesInvoiceRepositoryV1SavePostRequest**](SalesInvoiceRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesDataInvoiceInterface**](SalesDataInvoiceInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

