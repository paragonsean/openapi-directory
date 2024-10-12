# ConsolidatedStatisticsApi

All URIs are relative to *https://api.telematicssdk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1StatisticsConsolidatedDaily_0**](ConsolidatedStatisticsApi.md#v1StatisticsConsolidatedDaily_0) | **GET** /statistics/v1/Statistics/consolidated/daily | /v1/Statistics/consolidated/daily |
| [**v1StatisticsConsolidated_0**](ConsolidatedStatisticsApi.md#v1StatisticsConsolidated_0) | **GET** /statistics/v1/Statistics/consolidated | /v1/Statistics/consolidated |


<a id="v1StatisticsConsolidatedDaily_0"></a>
# **v1StatisticsConsolidatedDaily_0**
> v1StatisticsConsolidatedDaily_0(deviceToken, startDate, endDate, tag, instanceId, appId, companyId)

/v1/Statistics/consolidated/daily

/v1/Statistics/consolidated/daily

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsolidatedStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    ConsolidatedStatisticsApi apiInstance = new ConsolidatedStatisticsApi(defaultClient);
    String deviceToken = ""; // String | 
    String startDate = "2021-01-17"; // String | 
    String endDate = "2021-01-18"; // String | 
    String tag = ""; // String | 
    String instanceId = ""; // String | 
    String appId = ""; // String | 
    String companyId = ""; // String | 
    try {
      apiInstance.v1StatisticsConsolidatedDaily_0(deviceToken, startDate, endDate, tag, instanceId, appId, companyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsolidatedStatisticsApi#v1StatisticsConsolidatedDaily_0");
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
| **deviceToken** | **String**|  | [optional] |
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **instanceId** | **String**|  | [optional] |
| **appId** | **String**|  | [optional] |
| **companyId** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * X-Powered-By -  <br>  * X-StackifyID -  <br>  |

<a id="v1StatisticsConsolidated_0"></a>
# **v1StatisticsConsolidated_0**
> v1StatisticsConsolidated_0(deviceToken, startDate, endDate, tag, instanceId, appId, companyId)

/v1/Statistics/consolidated

/v1/Statistics/consolidated

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsolidatedStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    ConsolidatedStatisticsApi apiInstance = new ConsolidatedStatisticsApi(defaultClient);
    String deviceToken = ""; // String | 
    String startDate = "2021-01-18"; // String | 
    String endDate = "2021-03-18"; // String | 
    String tag = ""; // String | 
    String instanceId = ""; // String | 
    String appId = ""; // String | 
    String companyId = ""; // String | 
    try {
      apiInstance.v1StatisticsConsolidated_0(deviceToken, startDate, endDate, tag, instanceId, appId, companyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsolidatedStatisticsApi#v1StatisticsConsolidated_0");
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
| **deviceToken** | **String**|  | [optional] |
| **startDate** | **String**|  | [optional] |
| **endDate** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **instanceId** | **String**|  | [optional] |
| **appId** | **String**|  | [optional] |
| **companyId** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * X-Powered-By -  <br>  * X-StackifyID -  <br>  |

