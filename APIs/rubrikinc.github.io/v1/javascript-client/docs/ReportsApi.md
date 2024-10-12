# RubrikRestApi.ReportsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getComplianceSummarySLAV1**](ReportsApi.md#getComplianceSummarySLAV1) | **GET** /report/compliance_summary_sla | Get compliance summary information
[**getComplianceSummaryV1**](ReportsApi.md#getComplianceSummaryV1) | **GET** /report/compliance_summary | Get compliance summary information
[**setReportConfig**](ReportsApi.md#setReportConfig) | **PATCH** /report/config | Modify the report config



## getComplianceSummarySLAV1

> ComplianceSummarySLAV1 getComplianceSummarySLAV1(snapshotRange)

Get compliance summary information

Returns the compliance summary information for all protected objects based on whether the last expected snapshot was successful. This requirement is based on the SLA Domain assigned to the objects.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ReportsApi();
let snapshotRange = "snapshotRange_example"; // String | An SLA Domain-based range of snapshots. Compliance is calculated for snapshots in the range.
apiInstance.getComplianceSummarySLAV1(snapshotRange, (error, data, response) => {
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
 **snapshotRange** | **String**| An SLA Domain-based range of snapshots. Compliance is calculated for snapshots in the range. | 

### Return type

[**ComplianceSummarySLAV1**](ComplianceSummarySLAV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getComplianceSummaryV1

> ComplianceSummaryV1 getComplianceSummaryV1()

Get compliance summary information

Returns the compliance summary information for all protected objects based on a time-based requirement of at least one snapshot in each 24 hour report period. This view ignores the policies assigned to protected objects through SLA Domains.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ReportsApi();
apiInstance.getComplianceSummaryV1((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ComplianceSummaryV1**](ComplianceSummaryV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setReportConfig

> ReportConfigResponse setReportConfig(reportConfigPatch)

Modify the report config

Set the different report config parameters.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ReportsApi();
let reportConfigPatch = new RubrikRestApi.ReportConfigPatch(); // ReportConfigPatch | Specifies the new report config parameters.
apiInstance.setReportConfig(reportConfigPatch, (error, data, response) => {
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
 **reportConfigPatch** | [**ReportConfigPatch**](ReportConfigPatch.md)| Specifies the new report config parameters. | 

### Return type

[**ReportConfigResponse**](ReportConfigResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

