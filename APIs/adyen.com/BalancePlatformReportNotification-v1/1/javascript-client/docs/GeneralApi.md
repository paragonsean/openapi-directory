# ReportWebhooks.GeneralApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postBalancePlatformReportCreated**](GeneralApi.md#postBalancePlatformReportCreated) | **POST** /balancePlatform.report.created | Report generated



## postBalancePlatformReportCreated

> BalancePlatformNotificationResponse postBalancePlatformReportCreated(opts)

Report generated

Adyen sends this webhook after a report is generated and ready to be downloaded. The webhook contains the URL at which the report can be downloaded.  Before you download reports, ask your Adyen contact for your report credentials. You must use your the credentials to authenticate your GET request.

### Example

```javascript
import ReportWebhooks from 'report_webhooks';
let defaultClient = ReportWebhooks.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ReportWebhooks.GeneralApi();
let opts = {
  'reportNotificationRequest': new ReportWebhooks.ReportNotificationRequest() // ReportNotificationRequest | 
};
apiInstance.postBalancePlatformReportCreated(opts, (error, data, response) => {
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
 **reportNotificationRequest** | [**ReportNotificationRequest**](ReportNotificationRequest.md)|  | [optional] 

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

