# ReportingAndMonitoringApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportPerformancePlanningLevelIdGet**](ReportingAndMonitoringApi.md#reportPerformancePlanningLevelIdGet) | **GET** /report/performance/{planningLevelId} | Month over month performance per planning level |
| [**reportPerformanceSkuRationalizationPlanningLevelIdGet**](ReportingAndMonitoringApi.md#reportPerformanceSkuRationalizationPlanningLevelIdGet) | **GET** /report/performance/sku-rationalization/{planningLevelId} | SKU rationalization report |
| [**reportPlanningLevelOrganizationGet**](ReportingAndMonitoringApi.md#reportPlanningLevelOrganizationGet) | **GET** /report/planning-level/organization | Get list of plannign levels by organization |
| [**reportPlanningLevelUserGet**](ReportingAndMonitoringApi.md#reportPlanningLevelUserGet) | **GET** /report/planning-level/user | Get list of plannign levels by user |
| [**reportUserGet**](ReportingAndMonitoringApi.md#reportUserGet) | **GET** /report/user | Get usage statistics per user |


<a id="reportPerformancePlanningLevelIdGet"></a>
# **reportPerformancePlanningLevelIdGet**
> reportPerformancePlanningLevelIdGet(planningLevelId, token)

Month over month performance per planning level

Month over month performance per planning level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingAndMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReportingAndMonitoringApi apiInstance = new ReportingAndMonitoringApi(defaultClient);
    String planningLevelId = "planningLevelId_example"; // String | 
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.reportPerformancePlanningLevelIdGet(planningLevelId, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingAndMonitoringApi#reportPerformancePlanningLevelIdGet");
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
| **planningLevelId** | **String**|  | |
| **token** | **String**| User Authentication Token | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="reportPerformanceSkuRationalizationPlanningLevelIdGet"></a>
# **reportPerformanceSkuRationalizationPlanningLevelIdGet**
> List&lt;PortfolioModel&gt; reportPerformanceSkuRationalizationPlanningLevelIdGet(planningLevelId, token)

SKU rationalization report

SKU rationalization report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingAndMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReportingAndMonitoringApi apiInstance = new ReportingAndMonitoringApi(defaultClient);
    Integer planningLevelId = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    try {
      List<PortfolioModel> result = apiInstance.reportPerformanceSkuRationalizationPlanningLevelIdGet(planningLevelId, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingAndMonitoringApi#reportPerformanceSkuRationalizationPlanningLevelIdGet");
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
| **planningLevelId** | **Integer**|  | |
| **token** | **String**| User Authentication Token | [optional] |

### Return type

[**List&lt;PortfolioModel&gt;**](PortfolioModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="reportPlanningLevelOrganizationGet"></a>
# **reportPlanningLevelOrganizationGet**
> reportPlanningLevelOrganizationGet(token)

Get list of plannign levels by organization

Get list of plannign levels by organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingAndMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReportingAndMonitoringApi apiInstance = new ReportingAndMonitoringApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.reportPlanningLevelOrganizationGet(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingAndMonitoringApi#reportPlanningLevelOrganizationGet");
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
| **token** | **String**| User Authentication Token | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="reportPlanningLevelUserGet"></a>
# **reportPlanningLevelUserGet**
> reportPlanningLevelUserGet(token)

Get list of plannign levels by user

Get list of plannign levels by user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingAndMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReportingAndMonitoringApi apiInstance = new ReportingAndMonitoringApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.reportPlanningLevelUserGet(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingAndMonitoringApi#reportPlanningLevelUserGet");
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
| **token** | **String**| User Authentication Token | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="reportUserGet"></a>
# **reportUserGet**
> reportUserGet(token)

Get usage statistics per user

Get usage statistics per user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingAndMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReportingAndMonitoringApi apiInstance = new ReportingAndMonitoringApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.reportUserGet(token);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingAndMonitoringApi#reportUserGet");
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
| **token** | **String**| User Authentication Token | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

