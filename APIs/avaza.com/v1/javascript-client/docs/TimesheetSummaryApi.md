# AvazaApiDocumentation.TimesheetSummaryApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheetSummaryGet**](TimesheetSummaryApi.md#timesheetSummaryGet) | **GET** /api/TimesheetSummary | Gets Basic Summary of Timesheet Statistics



## timesheetSummaryGet

> TimesheetSummaryResult timesheetSummaryGet(opts)

Gets Basic Summary of Timesheet Statistics

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetSummaryApi();
let opts = {
  'modelGroupBy': ["null"], // [String] | (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \"Customer\", \"Project\", \"Category\", \"User\", \"Task\", \"Year\", \"Month\", \"Day\", \"Week\".
  'modelEntryDateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | (Required) Filter for timesheets greater or equal to the specified date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00
  'modelEntryDateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | (Required) Filter for timesheets with an entry date smaller or equal to the specified  date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00
  'modelUserID': [null], // [Number] | (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose timesheets should be retrieved. If the current user doesn't have impersonation rights, then they will only see their own data.
  'modelProjectID': 56, // Number | (Optional) Filter by Project
  'modelIsBillable': true, // Boolean | (Optional) Filter by the billable status of Timesheets.
  'modelIsInvoiced': true // Boolean | (Optional) Filter for timesheets by whether they have been Invoiced or not.
};
apiInstance.timesheetSummaryGet(opts, (error, data, response) => {
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
 **modelGroupBy** | [**[String]**](String.md)| (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \&quot;Customer\&quot;, \&quot;Project\&quot;, \&quot;Category\&quot;, \&quot;User\&quot;, \&quot;Task\&quot;, \&quot;Year\&quot;, \&quot;Month\&quot;, \&quot;Day\&quot;, \&quot;Week\&quot;. | [optional] 
 **modelEntryDateFrom** | **Date**| (Required) Filter for timesheets greater or equal to the specified date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00 | [optional] 
 **modelEntryDateTo** | **Date**| (Required) Filter for timesheets with an entry date smaller or equal to the specified  date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00 | [optional] 
 **modelUserID** | [**[Number]**](Number.md)| (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose timesheets should be retrieved. If the current user doesn&#39;t have impersonation rights, then they will only see their own data. | [optional] 
 **modelProjectID** | **Number**| (Optional) Filter by Project | [optional] 
 **modelIsBillable** | **Boolean**| (Optional) Filter by the billable status of Timesheets. | [optional] 
 **modelIsInvoiced** | **Boolean**| (Optional) Filter for timesheets by whether they have been Invoiced or not. | [optional] 

### Return type

[**TimesheetSummaryResult**](TimesheetSummaryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

