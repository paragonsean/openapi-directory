# SpendingPulse.SpendingPulseReportApi

All URIs are relative to *https://api.mastercard.com/spendingpulse/v1/spulse.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spendingpulseGet**](SpendingPulseReportApi.md#spendingpulseGet) | **GET** /spendingpulse | Returns all Spending Pulse reports (with the exception of the gasoline weekly report, which has its own resource), that one is subscribed to.



## spendingpulseGet

> SpendingPulseListResponse spendingpulseGet(opts)

Returns all Spending Pulse reports (with the exception of the gasoline weekly report, which has its own resource), that one is subscribed to.

Returns all Spending Pulse reports (with the exception of the gasoline weekly report, which has its own resource), that one is subscribed to. 

### Example

```javascript
import SpendingPulse from 'spending_pulse';

let apiInstance = new SpendingPulse.SpendingPulseReportApi();
let opts = {
  'currentRow': "1", // String | Starting record number to return.
  'offset': "25", // String | Used to restrict the number of records returned if needed to be less than max.
  'productLine': "Weekly Sales", // String | Product Line.  Either ?US Executive Report? or ?Weekly Sales?
  'publicationCoveragePeriod': "March 2015", // String | Publication Coverage Period indicates what period is to be covered, often the current report will include the month prior.
  'country': "US", // String | Country code.
  'reportType': "reportA", // String | Report type name, today the only report supported is \"monitor\".
  'period': "Weekly", // String | Indicates the period covered by the data with possible values of - day, week, month, quarter, annual
  'sector': "sectorA", // String | Sector name.
  'ecomm': "Y" // String | Ecommerce indicator.
};
apiInstance.spendingpulseGet(opts, (error, data, response) => {
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
 **currentRow** | **String**| Starting record number to return. | [optional] 
 **offset** | **String**| Used to restrict the number of records returned if needed to be less than max. | [optional] 
 **productLine** | **String**| Product Line.  Either ?US Executive Report? or ?Weekly Sales? | [optional] 
 **publicationCoveragePeriod** | **String**| Publication Coverage Period indicates what period is to be covered, often the current report will include the month prior. | [optional] 
 **country** | **String**| Country code. | [optional] 
 **reportType** | **String**| Report type name, today the only report supported is \&quot;monitor\&quot;. | [optional] 
 **period** | **String**| Indicates the period covered by the data with possible values of - day, week, month, quarter, annual | [optional] 
 **sector** | **String**| Sector name. | [optional] 
 **ecomm** | **String**| Ecommerce indicator. | [optional] 

### Return type

[**SpendingPulseListResponse**](SpendingPulseListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

