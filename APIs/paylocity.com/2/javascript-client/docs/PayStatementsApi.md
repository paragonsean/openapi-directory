# PaylocityApi.PayStatementsApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear**](PayStatementsApi.md#getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year} | Get employee pay statement details data for the specified year.
[**getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate**](PayStatementsApi.md#getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year}/{checkDate} | Get employee pay statement details data for the specified year and check date.
[**getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear**](PayStatementsApi.md#getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year} | Get employee pay statement summary data for the specified year.
[**getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate**](PayStatementsApi.md#getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}/{checkDate} | Get employee pay statement summary data for the specified year and check date.



## getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear

> [PayStatementDetails] getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear(companyId, employeeId, year, opts)

Get employee pay statement details data for the specified year.

Get pay statement details API will return employee pay statement details data currently available in Web Pay for the specified year.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.PayStatementsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let year = "year_example"; // String | The year for which to retrieve pay statement data
let opts = {
  'pagesize': 56, // Number | Number of records per page. Default value is 25.
  'pagenumber': 56, // Number | Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.
  'includetotalcount': true, // Boolean | Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.
  'codegroup': "codegroup_example" // String | Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
};
apiInstance.getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear(companyId, employeeId, year, opts, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **year** | **String**| The year for which to retrieve pay statement data | 
 **pagesize** | **Number**| Number of records per page. Default value is 25. | [optional] 
 **pagenumber** | **Number**| Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0. | [optional] 
 **includetotalcount** | **Boolean**| Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true. | [optional] 
 **codegroup** | **String**| Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW. | [optional] 

### Return type

[**[PayStatementDetails]**](PayStatementDetails.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate

> [PayStatementDetails] getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate(companyId, employeeId, year, checkDate, opts)

Get employee pay statement details data for the specified year and check date.

Get pay statement details API will return employee pay statement detail data currently available in Web Pay for the specified year and check date.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.PayStatementsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let year = "year_example"; // String | The year for which to retrieve pay statement data
let checkDate = "checkDate_example"; // String | The check date for which to retrieve pay statement data
let opts = {
  'pagesize': 56, // Number | Number of records per page. Default value is 25.
  'pagenumber': 56, // Number | Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.
  'includetotalcount': true, // Boolean | Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.
  'codegroup': "codegroup_example" // String | Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
};
apiInstance.getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate(companyId, employeeId, year, checkDate, opts, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **year** | **String**| The year for which to retrieve pay statement data | 
 **checkDate** | **String**| The check date for which to retrieve pay statement data | 
 **pagesize** | **Number**| Number of records per page. Default value is 25. | [optional] 
 **pagenumber** | **Number**| Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0. | [optional] 
 **includetotalcount** | **Boolean**| Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true. | [optional] 
 **codegroup** | **String**| Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW. | [optional] 

### Return type

[**[PayStatementDetails]**](PayStatementDetails.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear

> [PayStatementSummary] getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear(companyId, employeeId, year, opts)

Get employee pay statement summary data for the specified year.

Get pay statement summary API will return employee pay statement summary data currently available in Web Pay for the specified year.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.PayStatementsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let year = "year_example"; // String | The year for which to retrieve pay statement data
let opts = {
  'pagesize': 56, // Number | Number of records per page. Default value is 25.
  'pagenumber': 56, // Number | Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.
  'includetotalcount': true, // Boolean | Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.
  'codegroup': "codegroup_example" // String | Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
};
apiInstance.getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear(companyId, employeeId, year, opts, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **year** | **String**| The year for which to retrieve pay statement data | 
 **pagesize** | **Number**| Number of records per page. Default value is 25. | [optional] 
 **pagenumber** | **Number**| Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0. | [optional] 
 **includetotalcount** | **Boolean**| Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true. | [optional] 
 **codegroup** | **String**| Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW. | [optional] 

### Return type

[**[PayStatementSummary]**](PayStatementSummary.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate

> [PayStatementSummary] getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate(companyId, employeeId, year, checkDate, opts)

Get employee pay statement summary data for the specified year and check date.

Get pay statement summary API will return employee pay statement summary data currently available in Web Pay for the specified year and check date.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.PayStatementsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let year = "year_example"; // String | The year for which to retrieve pay statement data
let checkDate = "checkDate_example"; // String | The check date for which to retrieve pay statement data
let opts = {
  'pagesize': 56, // Number | Number of records per page. Default value is 25.
  'pagenumber': 56, // Number | Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.
  'includetotalcount': true, // Boolean | Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.
  'codegroup': "codegroup_example" // String | Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW.
};
apiInstance.getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate(companyId, employeeId, year, checkDate, opts, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **year** | **String**| The year for which to retrieve pay statement data | 
 **checkDate** | **String**| The check date for which to retrieve pay statement data | 
 **pagesize** | **Number**| Number of records per page. Default value is 25. | [optional] 
 **pagenumber** | **Number**| Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0. | [optional] 
 **includetotalcount** | **Boolean**| Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true. | [optional] 
 **codegroup** | **String**| Retrieve pay statement details related to specific deduction, earning or tax types. Common values include 401k, Memo, Reg, OT, Cash Tips, FED and SITW. | [optional] 

### Return type

[**[PayStatementSummary]**](PayStatementSummary.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

