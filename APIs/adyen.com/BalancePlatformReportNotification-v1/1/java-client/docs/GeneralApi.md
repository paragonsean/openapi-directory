# GeneralApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postBalancePlatformReportCreated**](GeneralApi.md#postBalancePlatformReportCreated) | **POST** /balancePlatform.report.created | Report generated |


<a id="postBalancePlatformReportCreated"></a>
# **postBalancePlatformReportCreated**
> BalancePlatformNotificationResponse postBalancePlatformReportCreated(reportNotificationRequest)

Report generated

Adyen sends this webhook after a report is generated and ready to be downloaded. The webhook contains the URL at which the report can be downloaded.  Before you download reports, ask your Adyen contact for your report credentials. You must use your the credentials to authenticate your GET request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    ReportNotificationRequest reportNotificationRequest = new ReportNotificationRequest(); // ReportNotificationRequest | 
    try {
      BalancePlatformNotificationResponse result = apiInstance.postBalancePlatformReportCreated(reportNotificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postBalancePlatformReportCreated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **reportNotificationRequest** | [**ReportNotificationRequest**](ReportNotificationRequest.md)|  | [optional] |

### Return type

[**BalancePlatformNotificationResponse**](BalancePlatformNotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

