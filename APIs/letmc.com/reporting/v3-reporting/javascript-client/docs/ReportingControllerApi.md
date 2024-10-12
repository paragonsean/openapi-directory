# LetMcApiV3Reporting.ReportingControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportingControllerMortgagesByCreatedDate**](ReportingControllerApi.md#reportingControllerMortgagesByCreatedDate) | **GET** /v3/reporting/{shortName}/mortgagesbycreateddate | Return a collection of mortgages by created date from a specific date
[**reportingControllerMortgagesByUpdatedDate**](ReportingControllerApi.md#reportingControllerMortgagesByUpdatedDate) | **GET** /v3/reporting/{shortName}/mortgagesbyupdateddate | Return a collection of all mortgages updated from a specific date
[**reportingControllerRepossessionsByCreatedDate**](ReportingControllerApi.md#reportingControllerRepossessionsByCreatedDate) | **GET** /v3/reporting/{shortName}/repossesionsbycreateddate | Return a collection of repossessions by created date from a specific date
[**reportingControllerRepossessionsByUpdatedDate**](ReportingControllerApi.md#reportingControllerRepossessionsByUpdatedDate) | **GET** /v3/reporting/{shortName}/repossesionsbyupdateddate | Return a collection of all reposessions updated from a specific date



## reportingControllerMortgagesByCreatedDate

> ReportingPropertyMortgageModelResults reportingControllerMortgagesByCreatedDate(shortName, branchID, startDate, offset, count)

Return a collection of mortgages by created date from a specific date

### Example

```javascript
import LetMcApiV3Reporting from 'let_mc_api_v3_reporting';

let apiInstance = new LetMcApiV3Reporting.ReportingControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The date to search from.
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.reportingControllerMortgagesByCreatedDate(shortName, branchID, startDate, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **branchID** | **String**| The unique ID of the Branch | 
 **startDate** | **Date**| The date to search from. | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**ReportingPropertyMortgageModelResults**](ReportingPropertyMortgageModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## reportingControllerMortgagesByUpdatedDate

> ReportingPropertyMortgageModelResults reportingControllerMortgagesByUpdatedDate(shortName, branchID, startDate, offset, count)

Return a collection of all mortgages updated from a specific date

### Example

```javascript
import LetMcApiV3Reporting from 'let_mc_api_v3_reporting';

let apiInstance = new LetMcApiV3Reporting.ReportingControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The date to search from.
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.reportingControllerMortgagesByUpdatedDate(shortName, branchID, startDate, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **branchID** | **String**| The unique ID of the Branch | 
 **startDate** | **Date**| The date to search from. | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**ReportingPropertyMortgageModelResults**](ReportingPropertyMortgageModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## reportingControllerRepossessionsByCreatedDate

> ReportingReceivershipCaseModelResults reportingControllerRepossessionsByCreatedDate(shortName, branchID, startDate, offset, count)

Return a collection of repossessions by created date from a specific date

### Example

```javascript
import LetMcApiV3Reporting from 'let_mc_api_v3_reporting';

let apiInstance = new LetMcApiV3Reporting.ReportingControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The date to search from.
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.reportingControllerRepossessionsByCreatedDate(shortName, branchID, startDate, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **branchID** | **String**| The unique ID of the Branch | 
 **startDate** | **Date**| The date to search from. | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**ReportingReceivershipCaseModelResults**](ReportingReceivershipCaseModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## reportingControllerRepossessionsByUpdatedDate

> ReportingReceivershipCaseModelResults reportingControllerRepossessionsByUpdatedDate(shortName, branchID, startDate, offset, count)

Return a collection of all reposessions updated from a specific date

### Example

```javascript
import LetMcApiV3Reporting from 'let_mc_api_v3_reporting';

let apiInstance = new LetMcApiV3Reporting.ReportingControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The date to search from.
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.reportingControllerRepossessionsByUpdatedDate(shortName, branchID, startDate, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **branchID** | **String**| The unique ID of the Branch | 
 **startDate** | **Date**| The date to search from. | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**ReportingReceivershipCaseModelResults**](ReportingReceivershipCaseModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

