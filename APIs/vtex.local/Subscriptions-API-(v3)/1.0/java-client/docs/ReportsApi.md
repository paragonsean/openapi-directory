# ReportsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRnsPvtReportsGet**](ReportsApi.md#apiRnsPvtReportsGet) | **GET** /api/rns/pvt/reports | List report templates |
| [**apiRnsPvtReportsReportNameDocumentsDocumentIdGet**](ReportsApi.md#apiRnsPvtReportsReportNameDocumentsDocumentIdGet) | **GET** /api/rns/pvt/reports/{reportName}/documents/{documentId} | Get report document details |
| [**apiRnsPvtReportsReportNameDocumentsPost**](ReportsApi.md#apiRnsPvtReportsReportNameDocumentsPost) | **POST** /api/rns/pvt/reports/{reportName}/documents | Generate report |


<a id="apiRnsPvtReportsGet"></a>
# **apiRnsPvtReportsGet**
> List&lt;SubscriptionReport&gt; apiRnsPvtReportsGet(contentType, accept)

List report templates

List all report templates available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      List<SubscriptionReport> result = apiInstance.apiRnsPvtReportsGet(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#apiRnsPvtReportsGet");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |

### Return type

[**List&lt;SubscriptionReport&gt;**](SubscriptionReport.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested report templates |  -  |

<a id="apiRnsPvtReportsReportNameDocumentsDocumentIdGet"></a>
# **apiRnsPvtReportsReportNameDocumentsDocumentIdGet**
> ReportResponse apiRnsPvtReportsReportNameDocumentsDocumentIdGet(reportName, documentId, contentType, accept)

Get report document details

Retrieve a specific report document by its Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String reportName = "reportName_example"; // String | Name of the report
    String documentId = "documentId_example"; // String | Id from the desired report document
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      ReportResponse result = apiInstance.apiRnsPvtReportsReportNameDocumentsDocumentIdGet(reportName, documentId, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#apiRnsPvtReportsReportNameDocumentsDocumentIdGet");
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
| **reportName** | **String**| Name of the report | |
| **documentId** | **String**| Id from the desired report document | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested report document |  -  |

<a id="apiRnsPvtReportsReportNameDocumentsPost"></a>
# **apiRnsPvtReportsReportNameDocumentsPost**
> ReportResponse apiRnsPvtReportsReportNameDocumentsPost(reportName, contentType, accept, email, beginDate, endDate)

Generate report

This endpoint creates a new report in the format of a CSV file and sends it via email. You can generate one of the following reports:    - subscriptionsWithStatus    - subscriptionsScheduledBetweenDate    - subscriptionsUpdatedBetweenDate    - subscriptionsCreatedBetweenDate    - executionsBetweenDate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String reportName = "reportName_example"; // String | Name of the type of report in wish to generate. The following values are accepted:    - `subscriptionsWithStatus`    - `subscriptionsScheduledBetweenDate`    - `subscriptionsUpdatedBetweenDate`    - `subscriptionsCreatedBetweenDate`    - `executionsBetweenDate`
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String email = "receiver@email.com"; // String | The report is sent to the email in this field.
    String beginDate = "2022-09-01"; // String | Start date of the report with the format `yyyy-mm-dd`. This field is required for any type of report.
    String endDate = "2022-10-01"; // String | End date of the report with the format `yyyy-mm-dd`. This field is required for any type of report.
    try {
      ReportResponse result = apiInstance.apiRnsPvtReportsReportNameDocumentsPost(reportName, contentType, accept, email, beginDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#apiRnsPvtReportsReportNameDocumentsPost");
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
| **reportName** | **String**| Name of the type of report in wish to generate. The following values are accepted:    - &#x60;subscriptionsWithStatus&#x60;    - &#x60;subscriptionsScheduledBetweenDate&#x60;    - &#x60;subscriptionsUpdatedBetweenDate&#x60;    - &#x60;subscriptionsCreatedBetweenDate&#x60;    - &#x60;executionsBetweenDate&#x60; | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **email** | **String**| The report is sent to the email in this field. | [optional] [default to receiver@email.com] |
| **beginDate** | **String**| Start date of the report with the format &#x60;yyyy-mm-dd&#x60;. This field is required for any type of report. | [optional] [default to 2022-09-01] |
| **endDate** | **String**| End date of the report with the format &#x60;yyyy-mm-dd&#x60;. This field is required for any type of report. | [optional] [default to 2022-10-01] |

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested report |  -  |

