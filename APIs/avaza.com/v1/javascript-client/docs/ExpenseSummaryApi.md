# AvazaApiDocumentation.ExpenseSummaryApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenseSummaryGet**](ExpenseSummaryApi.md#expenseSummaryGet) | **GET** /api/ExpenseSummary | Gets Basic Summary of Expense Statistics



## expenseSummaryGet

> ExpenseSummaryResult expenseSummaryGet(opts)

Gets Basic Summary of Expense Statistics

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseSummaryApi();
let opts = {
  'modelGroupBy': ["null"], // [String] | (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \"Category\", \"ChargeableStatus\", \"Merchant\", \"ApprovalStatus\", \"ReimbursementStatus\", \"Customer\", \"Project\", \"User\", \"Task\", \"Year\", \"Month\", \"Day\", \"Week\".
  'modelExpenseDateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | (Required) Filter for expenses with expense dates greater or equal to the specified date. e.g. 2019-01-25.
  'modelExpenseDateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | (Required) Filter for expenses with an expense date smaller or equal to the specified  date. e.g. 2019-01-25.
  'modelUserID': [null], // [Number] | (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose expenses should be retrieved. If the current user doesn't have impersonation rights, then they will only see their own data.
  'modelProjectID': 56 // Number | (Optional) Filter by Project
};
apiInstance.expenseSummaryGet(opts, (error, data, response) => {
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
 **modelGroupBy** | [**[String]**](String.md)| (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \&quot;Category\&quot;, \&quot;ChargeableStatus\&quot;, \&quot;Merchant\&quot;, \&quot;ApprovalStatus\&quot;, \&quot;ReimbursementStatus\&quot;, \&quot;Customer\&quot;, \&quot;Project\&quot;, \&quot;User\&quot;, \&quot;Task\&quot;, \&quot;Year\&quot;, \&quot;Month\&quot;, \&quot;Day\&quot;, \&quot;Week\&quot;. | [optional] 
 **modelExpenseDateFrom** | **Date**| (Required) Filter for expenses with expense dates greater or equal to the specified date. e.g. 2019-01-25. | [optional] 
 **modelExpenseDateTo** | **Date**| (Required) Filter for expenses with an expense date smaller or equal to the specified  date. e.g. 2019-01-25. | [optional] 
 **modelUserID** | [**[Number]**](Number.md)| (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose expenses should be retrieved. If the current user doesn&#39;t have impersonation rights, then they will only see their own data. | [optional] 
 **modelProjectID** | **Number**| (Optional) Filter by Project | [optional] 

### Return type

[**ExpenseSummaryResult**](ExpenseSummaryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

