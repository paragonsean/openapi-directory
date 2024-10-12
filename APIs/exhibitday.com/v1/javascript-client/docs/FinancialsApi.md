# TestTheExhibitDayApiWithSwagger.FinancialsApi

All URIs are relative to *https://api.exhibitday.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**financialsEventCosts0Get**](FinancialsApi.md#financialsEventCosts0Get) | **GET** /v1/financials/event_costs | 
[**financialsMiscAnnualExpenseCosts0Get**](FinancialsApi.md#financialsMiscAnnualExpenseCosts0Get) | **GET** /v1/financials/misc_annual_expense_costs | 



## financialsEventCosts0Get

> String financialsEventCosts0Get(apiKey, opts)



Retrieve event costs

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.FinancialsApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'filterByEventId': 3.4, // Number | Id of a specific event that you would like to retrieve costs for.
  'filterByEventStartDateGreaterThanOrEqualTo': new Date("2013-10-20"), // Date | Only include costs for events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
  'filterByEventStartDateSmallerThanOrEqualTo': new Date("2013-10-20"), // Date | Only include costs for events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
  'filterByEventEndDateGreaterThanOrEqualTo': new Date("2013-10-20"), // Date | Only include costs for events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
  'filterByEventEndDateSmallerThanOrEqualTo': new Date("2013-10-20") // Date | Only include costs for events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD
};
apiInstance.financialsEventCosts0Get(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **filterByEventId** | **Number**| Id of a specific event that you would like to retrieve costs for. | [optional] 
 **filterByEventStartDateGreaterThanOrEqualTo** | **Date**| Only include costs for events that have their start date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] 
 **filterByEventStartDateSmallerThanOrEqualTo** | **Date**| Only include costs for events that have their start date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] 
 **filterByEventEndDateGreaterThanOrEqualTo** | **Date**| Only include costs for events that have their end date greater than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] 
 **filterByEventEndDateSmallerThanOrEqualTo** | **Date**| Only include costs for events that have their end date smaller than or equal to the value passed in for this filter parameter. Use this date format: YYYY-MM-DD | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## financialsMiscAnnualExpenseCosts0Get

> String financialsMiscAnnualExpenseCosts0Get(apiKey, opts)



Retrieve Miscellaneous Annual Expense Costs

### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.FinancialsApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'budgetYear': 3.4 // Number | The specific budget year that you would like to retrieve miscellaneous annual expense costs for (e.g., 2023).
};
apiInstance.financialsMiscAnnualExpenseCosts0Get(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **budgetYear** | **Number**| The specific budget year that you would like to retrieve miscellaneous annual expense costs for (e.g., 2023). | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

