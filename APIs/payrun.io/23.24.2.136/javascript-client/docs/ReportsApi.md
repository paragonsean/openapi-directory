# PayRunIo.ReportsApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteReportDefinition**](ReportsApi.md#deleteReportDefinition) | **DELETE** /Report/{ReportDefinitionId} | Deletes a report definition
[**deleteTransformDefinition**](ReportsApi.md#deleteTransformDefinition) | **DELETE** /Transform/{TransformDefinitionId} | Deletes a transform definition
[**getActivePayInstructionsReportOutput**](ReportsApi.md#getActivePayInstructionsReportOutput) | **GET** /Report/ACTPAYINS/run | Runs the active pay instructions report
[**getAoeLiabilityReportOuput**](ReportsApi.md#getAoeLiabilityReportOuput) | **GET** /Report/AOELIABILITY/run | Runs the AOE liability report
[**getDpsMessageReportOutput**](ReportsApi.md#getDpsMessageReportOutput) | **GET** /Report/DPSMSG/run | Runs the DPS message report
[**getEmployerSummaryReportOuput**](ReportsApi.md#getEmployerSummaryReportOuput) | **GET** /Report/EMPSUM/run | Runs the employer summary report
[**getGrossToNetReportOutput**](ReportsApi.md#getGrossToNetReportOutput) | **GET** /Report/GRO2NET/run | Runs the gross to net report
[**getHolidayBalanceReportOutput**](ReportsApi.md#getHolidayBalanceReportOutput) | **GET** /Report/HOLBAL/run | Runs the holiday balance report
[**getJournalReportOuput**](ReportsApi.md#getJournalReportOuput) | **GET** /Report/JOURNAL/run | Runs the journal report
[**getLastPayDateReportOuput**](ReportsApi.md#getLastPayDateReportOuput) | **GET** /Report/LASTPAYDATE/run | Runs the last pay date report
[**getNetPayReportOutput**](ReportsApi.md#getNetPayReportOutput) | **GET** /Report/NETPAY/run | Runs the net pay report
[**getNextPayPeriodDatesReportOutput**](ReportsApi.md#getNextPayPeriodDatesReportOutput) | **GET** /Report/NEXTPERIOD/run | Runs the next pay period report
[**getP11SummaryReportOutput**](ReportsApi.md#getP11SummaryReportOutput) | **GET** /Report/P11SUM/run | Runs the P11 summary report
[**getP32NetReportOutput**](ReportsApi.md#getP32NetReportOutput) | **GET** /Report/P32/run | Runs the P32 report
[**getP32SummaryNetReportOutput**](ReportsApi.md#getP32SummaryNetReportOutput) | **GET** /Report/P32SUM/run | Runs the P32 summary report
[**getP45ReportOutput**](ReportsApi.md#getP45ReportOutput) | **GET** /Report/P45/run | Runs the P45 report
[**getP60ReportOutput**](ReportsApi.md#getP60ReportOutput) | **GET** /Report/P60/run | Runs the P60 report
[**getPapdisReportOuput**](ReportsApi.md#getPapdisReportOuput) | **GET** /Report/PAPDIS/run | Runs the PAPDIS report
[**getPassReportOuput**](ReportsApi.md#getPassReportOuput) | **GET** /Report/PASS/run | Runs the PASS report
[**getPayDashboardPayslipReportOuput**](ReportsApi.md#getPayDashboardPayslipReportOuput) | **GET** /Report/PAYDASHBOARD/run | Runs the Pay Dashboard payslips report
[**getPayslip3ReportOutput**](ReportsApi.md#getPayslip3ReportOutput) | **GET** /Report/PAYSLIP3/run | Runs the verbose payslip report
[**getPensionLiabilityReportOutput**](ReportsApi.md#getPensionLiabilityReportOutput) | **GET** /Report/PENLIABILITY/run | Runs the pension liability report
[**getReportDefinitionFromApplication**](ReportsApi.md#getReportDefinitionFromApplication) | **GET** /Report/{ReportDefinitionId} | Get the report definition
[**getReportDefinitionsFromApplication**](ReportsApi.md#getReportDefinitionsFromApplication) | **GET** /Reports | Gets all reports
[**getReportOutput**](ReportsApi.md#getReportOutput) | **GET** /Report/{ReportDefinitionId}/run | Runs the specified report definition
[**getTransformDefinitionFromApplication**](ReportsApi.md#getTransformDefinitionFromApplication) | **GET** /Transform/{TransformDefinitionId} | Get the transform definition
[**getTransformDefinitionsFromApplication**](ReportsApi.md#getTransformDefinitionsFromApplication) | **GET** /Transforms | Gets all transform definitions
[**postReportDefinition**](ReportsApi.md#postReportDefinition) | **POST** /Reports | Create a new report definition
[**postTransformDefinition**](ReportsApi.md#postTransformDefinition) | **POST** /Transforms | Create a new transform definition
[**putReportDefinition**](ReportsApi.md#putReportDefinition) | **PUT** /Report/{ReportDefinitionId} | Updates a report definition
[**putTransformDefinition**](ReportsApi.md#putTransformDefinition) | **PUT** /Transform/{TransformDefinitionId} | Updates a transform definition



## deleteReportDefinition

> deleteReportDefinition(reportDefinitionId, authorization, apiVersion)

Deletes a report definition

Delete the specified report definition

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let reportDefinitionId = "reportDefinitionId_example"; // String | The report definition unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteReportDefinition(reportDefinitionId, authorization, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reportDefinitionId** | **String**| The report definition unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTransformDefinition

> deleteTransformDefinition(transformDefinitionId, authorization, apiVersion)

Deletes a transform definition

Delete the specified transform definition

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let transformDefinitionId = "transformDefinitionId_example"; // String | The transform definition unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteTransformDefinition(transformDefinitionId, authorization, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transformDefinitionId** | **String**| The transform definition unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getActivePayInstructionsReportOutput

> File getActivePayInstructionsReportOutput(employerKey, employeeKey, fromDate, authorization, apiVersion, opts)

Runs the active pay instructions report

Returns the result of the executed active pay instructions report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let employeeKey = "employeeKey_example"; // String | The employee unique key. E.g. EE001
let fromDate = new Date("2013-10-20"); // Date | The lower filter date. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'activeOn': new Date("2013-10-20"), // Date | The active date to consider. E.g 2017-04-05
  'toDate': new Date("2013-10-20"), // Date | The upper filter date. E.g 2017-04-05
  'type': "type_example" // String | the data type to filter on. E.g. TaxPayInstruction
};
apiInstance.getActivePayInstructionsReportOutput(employerKey, employeeKey, fromDate, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **employeeKey** | **String**| The employee unique key. E.g. EE001 | 
 **fromDate** | **Date**| The lower filter date. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **activeOn** | **Date**| The active date to consider. E.g 2017-04-05 | [optional] 
 **toDate** | **Date**| The upper filter date. E.g 2017-04-05 | [optional] 
 **type** | **String**| the data type to filter on. E.g. TaxPayInstruction | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAoeLiabilityReportOuput

> File getAoeLiabilityReportOuput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts)

Runs the AOE liability report

Returns the result of the executed AOE liability report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'taxPeriod': "taxPeriod_example", // Number | The tax period number.
  'transformDefinitionKey': "transformDefinitionKey_example" // String | The transform definition unique key. E.g. P45-Pdf
};
apiInstance.getAoeLiabilityReportOuput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **taxPeriod** | **Number**| The tax period number. | [optional] 
 **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDpsMessageReportOutput

> File getDpsMessageReportOutput(employerKey, fromDate, authorization, apiVersion, opts)

Runs the DPS message report

Returns the result of the executed DPS message report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let fromDate = new Date("2013-10-20"); // Date | The lower filter date. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'toDate': new Date("2013-10-20"), // Date | The upper filter date. E.g 2017-04-05
  'messageTypes': "messageTypes_example", // String | The DPS message types as a CSV list. E.g. P6,P9,SL1,SL2
  'messageStatuses': "messageStatuses_example", // String | The DPS message status as a CSV list. E.g. Retrieved,Processed,Blocked,Ignored
  'startIndex': "startIndex_example", // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
  'maxIndex': "maxIndex_example" // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
};
apiInstance.getDpsMessageReportOutput(employerKey, fromDate, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **fromDate** | **Date**| The lower filter date. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **toDate** | **Date**| The upper filter date. E.g 2017-04-05 | [optional] 
 **messageTypes** | **String**| The DPS message types as a CSV list. E.g. P6,P9,SL1,SL2 | [optional] 
 **messageStatuses** | **String**| The DPS message status as a CSV list. E.g. Retrieved,Processed,Blocked,Ignored | [optional] 
 **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] 
 **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployerSummaryReportOuput

> File getEmployerSummaryReportOuput(employerKey, contextDate, authorization, apiVersion)

Runs the employer summary report

Returns the result of the employer summary report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let contextDate = new Date("2013-10-20"); // Date | The date context for the report. E.g. 2018-04-30
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerSummaryReportOuput(employerKey, contextDate, authorization, apiVersion, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **contextDate** | **Date**| The date context for the report. E.g. 2018-04-30 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGrossToNetReportOutput

> File getGrossToNetReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts)

Runs the gross to net report

Returns the result of the executed gross to net report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'taxPeriod': "taxPeriod_example", // Number | The tax period number.
  'startIndex': "startIndex_example", // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
  'maxIndex': "maxIndex_example" // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
};
apiInstance.getGrossToNetReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **taxPeriod** | **Number**| The tax period number. | [optional] 
 **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] 
 **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHolidayBalanceReportOutput

> File getHolidayBalanceReportOutput(employerKey, holidayYearEnd, authorization, apiVersion, opts)

Runs the holiday balance report

Returns the result of the executed holiday balance report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let holidayYearEnd = new Date("2013-10-20"); // Date | The holiday year end for the report. E.g. 2018-12-31
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'employeeCodes': "employeeCodes_example", // String | A comma separated list of the employee codes. E.g. EMP001,EMP002
  'startIndex': "startIndex_example", // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
  'maxIndex': "maxIndex_example" // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
};
apiInstance.getHolidayBalanceReportOutput(employerKey, holidayYearEnd, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **holidayYearEnd** | **Date**| The holiday year end for the report. E.g. 2018-12-31 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **employeeCodes** | **String**| A comma separated list of the employee codes. E.g. EMP001,EMP002 | [optional] 
 **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] 
 **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJournalReportOuput

> File getJournalReportOuput(employerKey, payFrequency, taxYear, ledgerTarget, authorization, apiVersion, opts)

Runs the journal report

Returns the result of the journal report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payFrequency = "payFrequency_example"; // String | The pay frequency option. E.g. Monthly
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let ledgerTarget = "ledgerTarget_example"; // String | Specific to JOURNAL report, a filter used to select the journal lines for the specified ledger target. E.g. [Default]
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'taxPeriod': "taxPeriod_example" // Number | The tax period number.
};
apiInstance.getJournalReportOuput(employerKey, payFrequency, taxYear, ledgerTarget, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payFrequency** | **String**| The pay frequency option. E.g. Monthly | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **ledgerTarget** | **String**| Specific to JOURNAL report, a filter used to select the journal lines for the specified ledger target. E.g. [Default] | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **taxPeriod** | **Number**| The tax period number. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLastPayDateReportOuput

> File getLastPayDateReportOuput(employerKey, employeeKey, authorization, apiVersion)

Runs the last pay date report

Returns the result of the executed last pay date report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let employeeKey = "employeeKey_example"; // String | The employee unique key. E.g. EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getLastPayDateReportOuput(employerKey, employeeKey, authorization, apiVersion, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **employeeKey** | **String**| The employee unique key. E.g. EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetPayReportOutput

> File getNetPayReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts)

Runs the net pay report

Returns the result of the executed net pay report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'taxPeriod': "taxPeriod_example", // Number | The tax period number.
  'startIndex': "startIndex_example", // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
  'maxIndex': "maxIndex_example" // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
};
apiInstance.getNetPayReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **taxPeriod** | **Number**| The tax period number. | [optional] 
 **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] 
 **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNextPayPeriodDatesReportOutput

> File getNextPayPeriodDatesReportOutput(employerKey, payScheduleKey, authorization, apiVersion)

Runs the next pay period report

Returns the result of the executed next pay period report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getNextPayPeriodDatesReportOutput(employerKey, payScheduleKey, authorization, apiVersion, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getP11SummaryReportOutput

> File getP11SummaryReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts)

Runs the P11 summary report

Returns the result of the executed P11 summary report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'startIndex': "startIndex_example", // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
  'maxIndex': "maxIndex_example" // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
};
apiInstance.getP11SummaryReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] 
 **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getP32NetReportOutput

> File getP32NetReportOutput(employerKey, taxYear, authorization, apiVersion)

Runs the P32 report

Returns the result of the executed P32 report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getP32NetReportOutput(employerKey, taxYear, authorization, apiVersion, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getP32SummaryNetReportOutput

> File getP32SummaryNetReportOutput(employerKey, taxYear, authorization, apiVersion)

Runs the P32 summary report

Returns the result of the executed P32 summary report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getP32SummaryNetReportOutput(employerKey, taxYear, authorization, apiVersion, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getP45ReportOutput

> File getP45ReportOutput(employerKey, employeeKey, authorization, apiVersion, opts)

Runs the P45 report

Returns the result of the executed P45 report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let employeeKey = "employeeKey_example"; // String | The employee unique key. E.g. EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'transformDefinitionKey': "transformDefinitionKey_example" // String | The transform definition unique key. E.g. P45-Pdf
};
apiInstance.getP45ReportOutput(employerKey, employeeKey, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **employeeKey** | **String**| The employee unique key. E.g. EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getP60ReportOutput

> File getP60ReportOutput(employerKey, taxYear, authorization, apiVersion, opts)

Runs the P60 report

Returns the result of the executed P60 report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'employeeCodes': "employeeCodes_example", // String | A comma separated list of the employee codes. E.g. EMP001,EMP002
  'transformDefinitionKey': "transformDefinitionKey_example", // String | The transform definition unique key. E.g. P45-Pdf
  'startIndex': "startIndex_example", // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
  'maxIndex': "maxIndex_example" // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
};
apiInstance.getP60ReportOutput(employerKey, taxYear, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **employeeCodes** | **String**| A comma separated list of the employee codes. E.g. EMP001,EMP002 | [optional] 
 **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] 
 **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] 
 **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPapdisReportOuput

> File getPapdisReportOuput(employerKey, payScheduleKey, taxYear, pensionKey, messageFunctionCode, authorization, apiVersion, opts)

Runs the PAPDIS report

Returns the result of the executed PAPDIS report. PAPDIS is a free and open data interface standard designed to allow payroll and middleware software developers to create a file that can be used by pension providers to exchange data. http://www.papdis.org/

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let pensionKey = "pensionKey_example"; // String | The pension scheme unique key. E.g. PENSCH001
let messageFunctionCode = "messageFunctionCode_example"; // String | Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions).
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'paymentDate': new Date("2013-10-20"), // Date | The payment date context for the report. E.g. 2018-04-30
  'transformDefinitionKey': "transformDefinitionKey_example" // String | The transform definition unique key. E.g. P45-Pdf
};
apiInstance.getPapdisReportOuput(employerKey, payScheduleKey, taxYear, pensionKey, messageFunctionCode, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **pensionKey** | **String**| The pension scheme unique key. E.g. PENSCH001 | 
 **messageFunctionCode** | **String**| Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions). | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **paymentDate** | **Date**| The payment date context for the report. E.g. 2018-04-30 | [optional] 
 **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPassReportOuput

> File getPassReportOuput(employerKey, payScheduleKey, taxYear, pensionKey, messageFunctionCode, intermediaryId, documentId, authorization, apiVersion, opts)

Runs the PASS report

Returns the result of the executed PASS report. PASS stands for Payroll and Systemsync. PASS 1.1 is an extension of the PAPDIS V1.1 schema. https://pensionsynckb.systemsyncsolutions.com/display/PKB/PASS+1.1

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let pensionKey = "pensionKey_example"; // String | The pension scheme unique key. E.g. PENSCH001
let messageFunctionCode = "messageFunctionCode_example"; // String | Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions).
let intermediaryId = "intermediaryId_example"; // String | Specific to PensionSync PASS report, a unique identifier for the Intermediary who is acting on behalf of the employer.
let documentId = "documentId_example"; // String | Specific to PensionSync PASS report, a document identifier unique for this document within the Intermediary.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'paymentDate': new Date("2013-10-20") // Date | The payment date context for the report. E.g. 2018-04-30
};
apiInstance.getPassReportOuput(employerKey, payScheduleKey, taxYear, pensionKey, messageFunctionCode, intermediaryId, documentId, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **pensionKey** | **String**| The pension scheme unique key. E.g. PENSCH001 | 
 **messageFunctionCode** | **String**| Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions). | 
 **intermediaryId** | **String**| Specific to PensionSync PASS report, a unique identifier for the Intermediary who is acting on behalf of the employer. | 
 **documentId** | **String**| Specific to PensionSync PASS report, a document identifier unique for this document within the Intermediary. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **paymentDate** | **Date**| The payment date context for the report. E.g. 2018-04-30 | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayDashboardPayslipReportOuput

> File getPayDashboardPayslipReportOuput(employerKey, payScheduleKey, taxYear, publicationDate, authorization, apiVersion, opts)

Runs the Pay Dashboard payslips report

Returns the result of the executed Pay Dashboard payslip report for the given query parameters. See https://api.paydashboard.com for details. For compatability should be returned as JSON with TransformDefinitionKey&#x3D;Json-Clean.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let publicationDate = new Date("2013-10-20"); // Date | Specific to the Pay Dashboard report, allows the specification of a future payslip publication date. E.g. 2018-12-31
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'employeeCodes': "employeeCodes_example", // String | A comma separated list of the employee codes. E.g. EMP001,EMP002
  'transformDefinitionKey': "transformDefinitionKey_example", // String | The transform definition unique key. E.g. P45-Pdf
  'startIndex': "startIndex_example", // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
  'maxIndex': "maxIndex_example", // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
  'paymentDate': new Date("2013-10-20") // Date | The payment date context for the report. E.g. 2018-04-30
};
apiInstance.getPayDashboardPayslipReportOuput(employerKey, payScheduleKey, taxYear, publicationDate, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **publicationDate** | **Date**| Specific to the Pay Dashboard report, allows the specification of a future payslip publication date. E.g. 2018-12-31 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **employeeCodes** | **String**| A comma separated list of the employee codes. E.g. EMP001,EMP002 | [optional] 
 **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] 
 **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] 
 **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] 
 **paymentDate** | **Date**| The payment date context for the report. E.g. 2018-04-30 | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayslip3ReportOutput

> File getPayslip3ReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts)

Runs the verbose payslip report

Returns the result of the executed verbose payslip report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let payScheduleKey = "payScheduleKey_example"; // String | The pay schedule unique key. E.g. SCH001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let opts = {
  'employeeCodes': "employeeCodes_example", // String | A comma separated list of the employee codes. E.g. EMP001,EMP002
  'transformDefinitionKey': "transformDefinitionKey_example", // String | The transform definition unique key. E.g. P45-Pdf
  'startIndex': "startIndex_example", // String | The element index to begin the report. Used to control paging within large data sets. E.g. 1
  'maxIndex': "maxIndex_example", // String | The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
  'paymentDate': new Date("2013-10-20") // Date | The payment date context for the report. E.g. 2018-04-30
};
apiInstance.getPayslip3ReportOutput(employerKey, payScheduleKey, taxYear, authorization, apiVersion, opts, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **payScheduleKey** | **String**| The pay schedule unique key. E.g. SCH001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **employeeCodes** | **String**| A comma separated list of the employee codes. E.g. EMP001,EMP002 | [optional] 
 **transformDefinitionKey** | **String**| The transform definition unique key. E.g. P45-Pdf | [optional] 
 **startIndex** | **String**| The element index to begin the report. Used to control paging within large data sets. E.g. 1 | [optional] 
 **maxIndex** | **String**| The highest element index to return from the report. Used to control paging within large data sets. E.g. 100 | [optional] 
 **paymentDate** | **Date**| The payment date context for the report. E.g. 2018-04-30 | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPensionLiabilityReportOutput

> File getPensionLiabilityReportOutput(employerKey, taxYear, pensionKey, authorization, apiVersion)

Runs the pension liability report

Returns the result of the executed pension liability report for the given query parameters

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let employerKey = "employerKey_example"; // String | The employer unique key. E.g. ER001
let taxYear = "taxYear_example"; // Number | The tax year. E.g. 2017 = 2017/18 year.
let pensionKey = "pensionKey_example"; // String | The pension scheme unique key. E.g. PENSCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPensionLiabilityReportOutput(employerKey, taxYear, pensionKey, authorization, apiVersion, (error, data, response) => {
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
 **employerKey** | **String**| The employer unique key. E.g. ER001 | 
 **taxYear** | **Number**| The tax year. E.g. 2017 &#x3D; 2017/18 year. | 
 **pensionKey** | **String**| The pension scheme unique key. E.g. PENSCH001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportDefinitionFromApplication

> ReportDefinition getReportDefinitionFromApplication(reportDefinitionId, authorization, apiVersion)

Get the report definition

Returns the specified report definition from the authroised application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let reportDefinitionId = "reportDefinitionId_example"; // String | The report definition unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getReportDefinitionFromApplication(reportDefinitionId, authorization, apiVersion, (error, data, response) => {
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
 **reportDefinitionId** | **String**| The report definition unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**ReportDefinition**](ReportDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportDefinitionsFromApplication

> LinkCollection getReportDefinitionsFromApplication(authorization, apiVersion)

Gets all reports

Get links to all saved report definitions under authorised application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getReportDefinitionsFromApplication(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportOutput

> File getReportOutput(reportDefinitionId, authorization, apiVersion)

Runs the specified report definition

Returns the result of the executed report definition

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let reportDefinitionId = "reportDefinitionId_example"; // String | The report definition unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getReportOutput(reportDefinitionId, authorization, apiVersion, (error, data, response) => {
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
 **reportDefinitionId** | **String**| The report definition unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransformDefinitionFromApplication

> TransformDefinition getTransformDefinitionFromApplication(transformDefinitionId, authorization, apiVersion)

Get the transform definition

Returns the specified transform definition from the authroised application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let transformDefinitionId = "transformDefinitionId_example"; // String | The transform definition unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTransformDefinitionFromApplication(transformDefinitionId, authorization, apiVersion, (error, data, response) => {
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
 **transformDefinitionId** | **String**| The transform definition unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**TransformDefinition**](TransformDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransformDefinitionsFromApplication

> LinkCollection getTransformDefinitionsFromApplication(authorization, apiVersion)

Gets all transform definitions

Get links to all saved transform definitions under authorised application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTransformDefinitionsFromApplication(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postReportDefinition

> Link postReportDefinition(authorization, apiVersion, reportDefinition)

Create a new report definition

Creates a new report defintion object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let reportDefinition = new PayRunIo.ReportDefinition(); // ReportDefinition | The report definition object.
apiInstance.postReportDefinition(authorization, apiVersion, reportDefinition, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **reportDefinition** | [**ReportDefinition**](ReportDefinition.md)| The report definition object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTransformDefinition

> Link postTransformDefinition(authorization, apiVersion, transformDefinition)

Create a new transform definition

Creates a new transform defintion object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let transformDefinition = new PayRunIo.TransformDefinition(); // TransformDefinition | The transform definition object to be executed against the report data.
apiInstance.postTransformDefinition(authorization, apiVersion, transformDefinition, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **transformDefinition** | [**TransformDefinition**](TransformDefinition.md)| The transform definition object to be executed against the report data. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putReportDefinition

> ReportDefinition putReportDefinition(reportDefinitionId, authorization, apiVersion, reportDefinition)

Updates a report definition

Updates the existing specified report definition object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let reportDefinitionId = "reportDefinitionId_example"; // String | The report definition unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let reportDefinition = new PayRunIo.ReportDefinition(); // ReportDefinition | The report definition object.
apiInstance.putReportDefinition(reportDefinitionId, authorization, apiVersion, reportDefinition, (error, data, response) => {
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
 **reportDefinitionId** | **String**| The report definition unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **reportDefinition** | [**ReportDefinition**](ReportDefinition.md)| The report definition object. | 

### Return type

[**ReportDefinition**](ReportDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putTransformDefinition

> TransformDefinition putTransformDefinition(transformDefinitionId, authorization, apiVersion, transformDefinition)

Updates a transform definition

Updates the existing specified transform definition object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportsApi();
let transformDefinitionId = "transformDefinitionId_example"; // String | The transform definition unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let transformDefinition = new PayRunIo.TransformDefinition(); // TransformDefinition | The transform definition object to be executed against the report data.
apiInstance.putTransformDefinition(transformDefinitionId, authorization, apiVersion, transformDefinition, (error, data, response) => {
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
 **transformDefinitionId** | **String**| The transform definition unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **transformDefinition** | [**TransformDefinition**](TransformDefinition.md)| The transform definition object to be executed against the report data. | 

### Return type

[**TransformDefinition**](TransformDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

