# PackageReportsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2ClientsClientIDPackageReportsPut**](PackageReportsApi.md#apiV2ClientsClientIDPackageReportsPut) | **PUT** /api/v2/Clients/{ClientID}/PackageReports | Submit a package report |
| [**packageReportsBatch**](PackageReportsApi.md#packageReportsBatch) | **PUT** /api/v2/Clients/{ClientID}/PackageReports/Batch | Submit a batch of package reports |
| [**packageReportsDefault**](PackageReportsApi.md#packageReportsDefault) | **GET** /api/v2/Clients/{ClientID}/PackageReports | Get the package reports for a client. |


<a id="apiV2ClientsClientIDPackageReportsPut"></a>
# **apiV2ClientsClientIDPackageReportsPut**
> apiV2ClientsClientIDPackageReportsPut(clientID, updateSystemModelsPackageReport)

Submit a package report

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageReportsApi apiInstance = new PackageReportsApi(defaultClient);
    String clientID = "clientID_example"; // String | The Client ID
    UpdateSystemModelsPackageReport updateSystemModelsPackageReport = new UpdateSystemModelsPackageReport(); // UpdateSystemModelsPackageReport | The Package Report
    try {
      apiInstance.apiV2ClientsClientIDPackageReportsPut(clientID, updateSystemModelsPackageReport);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageReportsApi#apiV2ClientsClientIDPackageReportsPut");
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
| **clientID** | **String**| The Client ID | |
| **updateSystemModelsPackageReport** | [**UpdateSystemModelsPackageReport**](UpdateSystemModelsPackageReport.md)| The Package Report | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="packageReportsBatch"></a>
# **packageReportsBatch**
> packageReportsBatch(clientID, updateSystemModelsPackageReport)

Submit a batch of package reports

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageReportsApi apiInstance = new PackageReportsApi(defaultClient);
    String clientID = "clientID_example"; // String | The Client ID
    List<UpdateSystemModelsPackageReport> updateSystemModelsPackageReport = Arrays.asList(); // List<UpdateSystemModelsPackageReport> | The Package Reports
    try {
      apiInstance.packageReportsBatch(clientID, updateSystemModelsPackageReport);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageReportsApi#packageReportsBatch");
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
| **clientID** | **String**| The Client ID | |
| **updateSystemModelsPackageReport** | [**List&lt;UpdateSystemModelsPackageReport&gt;**](UpdateSystemModelsPackageReport.md)| The Package Reports | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="packageReportsDefault"></a>
# **packageReportsDefault**
> List&lt;UpdateSystemModelsPackageReport&gt; packageReportsDefault(clientID)

Get the package reports for a client.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PackageReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PackageReportsApi apiInstance = new PackageReportsApi(defaultClient);
    String clientID = "clientID_example"; // String | The Client ID
    try {
      List<UpdateSystemModelsPackageReport> result = apiInstance.packageReportsDefault(clientID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PackageReportsApi#packageReportsDefault");
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
| **clientID** | **String**| The Client ID | |

### Return type

[**List&lt;UpdateSystemModelsPackageReport&gt;**](UpdateSystemModelsPackageReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

