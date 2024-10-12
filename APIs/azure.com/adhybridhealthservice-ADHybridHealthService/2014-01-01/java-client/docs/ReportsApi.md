# ReportsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicesListAllRiskyIpDownloadReport**](ReportsApi.md#servicesListAllRiskyIpDownloadReport) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/reports/riskyIp/blobUris |  |
| [**servicesListCurrentRiskyIpDownloadReport**](ReportsApi.md#servicesListCurrentRiskyIpDownloadReport) | **POST** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/reports/riskyIp/generateBlobUri |  |
| [**servicesListUserBadPasswordReport**](ReportsApi.md#servicesListUserBadPasswordReport) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/reports/badpassword/details/user |  |


<a id="servicesListAllRiskyIpDownloadReport"></a>
# **servicesListAllRiskyIpDownloadReport**
> RiskyIPBlobUris servicesListAllRiskyIpDownloadReport(serviceName, apiVersion)



Gets all Risky IP report URIs for the last 7 days.

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      RiskyIPBlobUris result = apiInstance.servicesListAllRiskyIpDownloadReport(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#servicesListAllRiskyIpDownloadReport");
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
| **serviceName** | **String**| The name of the service. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**RiskyIPBlobUris**](RiskyIPBlobUris.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Risky IP report URIs for the last 7 days. |  -  |

<a id="servicesListCurrentRiskyIpDownloadReport"></a>
# **servicesListCurrentRiskyIpDownloadReport**
> RiskyIPBlobUris servicesListCurrentRiskyIpDownloadReport(serviceName, apiVersion)



Initiate the generation of a new Risky IP report. Returns the URI for the new one.

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      RiskyIPBlobUris result = apiInstance.servicesListCurrentRiskyIpDownloadReport(serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#servicesListCurrentRiskyIpDownloadReport");
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
| **serviceName** | **String**| The name of the service. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**RiskyIPBlobUris**](RiskyIPBlobUris.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The URI of the Risky IP report that was requested. |  -  |

<a id="servicesListUserBadPasswordReport"></a>
# **servicesListUserBadPasswordReport**
> ErrorReportUsersEntries servicesListUserBadPasswordReport(serviceName, apiVersion, dataSource)



Gets the bad password login attempt report for an user

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String dataSource = "dataSource_example"; // String | The source of data, if its test data or customer data.
    try {
      ErrorReportUsersEntries result = apiInstance.servicesListUserBadPasswordReport(serviceName, apiVersion, dataSource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#servicesListUserBadPasswordReport");
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
| **serviceName** | **String**| The name of the service. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **dataSource** | **String**| The source of data, if its test data or customer data. | [optional] |

### Return type

[**ErrorReportUsersEntries**](ErrorReportUsersEntries.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of bad password login attempts. |  -  |

