# ReportsApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getComplianceSummarySLAV1**](ReportsApi.md#getComplianceSummarySLAV1) | **GET** /report/compliance_summary_sla | Get compliance summary information |
| [**getComplianceSummaryV1**](ReportsApi.md#getComplianceSummaryV1) | **GET** /report/compliance_summary | Get compliance summary information |
| [**setReportConfig**](ReportsApi.md#setReportConfig) | **PATCH** /report/config | Modify the report config |


<a id="getComplianceSummarySLAV1"></a>
# **getComplianceSummarySLAV1**
> ComplianceSummarySLAV1 getComplianceSummarySLAV1(snapshotRange)

Get compliance summary information

Returns the compliance summary information for all protected objects based on whether the last expected snapshot was successful. This requirement is based on the SLA Domain assigned to the objects.

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
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String snapshotRange = "LastSnapshot"; // String | An SLA Domain-based range of snapshots. Compliance is calculated for snapshots in the range.
    try {
      ComplianceSummarySLAV1 result = apiInstance.getComplianceSummarySLAV1(snapshotRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getComplianceSummarySLAV1");
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
| **snapshotRange** | **String**| An SLA Domain-based range of snapshots. Compliance is calculated for snapshots in the range. | [enum: LastSnapshot, Last2Snapshots, Last3Snapshots, AllSnapshots] |

### Return type

[**ComplianceSummarySLAV1**](ComplianceSummarySLAV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data from the report data source. |  -  |

<a id="getComplianceSummaryV1"></a>
# **getComplianceSummaryV1**
> ComplianceSummaryV1 getComplianceSummaryV1()

Get compliance summary information

Returns the compliance summary information for all protected objects based on a time-based requirement of at least one snapshot in each 24 hour report period. This view ignores the policies assigned to protected objects through SLA Domains.

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
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    try {
      ComplianceSummaryV1 result = apiInstance.getComplianceSummaryV1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#getComplianceSummaryV1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data from the report data source. |  -  |

<a id="setReportConfig"></a>
# **setReportConfig**
> ReportConfigResponse setReportConfig(reportConfigPatch)

Modify the report config

Set the different report config parameters.

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
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    ReportConfigPatch reportConfigPatch = new ReportConfigPatch(); // ReportConfigPatch | Specifies the new report config parameters.
    try {
      ReportConfigResponse result = apiInstance.setReportConfig(reportConfigPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#setReportConfig");
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
| **reportConfigPatch** | [**ReportConfigPatch**](ReportConfigPatch.md)| Specifies the new report config parameters. | |

### Return type

[**ReportConfigResponse**](ReportConfigResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new duration, in days, of the retention period for report job instances for log jobs. |  -  |

