# Class3ForBackEndOptionalApi

All URIs are relative to *https://api.telematicssdk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1ScoringsConsolidated**](Class3ForBackEndOptionalApi.md#v1ScoringsConsolidated) | **GET** /statistics/v1/Scorings/consolidated | /v1/Scorings/consolidated |
| [**v1ScoringsConsolidatedDaily**](Class3ForBackEndOptionalApi.md#v1ScoringsConsolidatedDaily) | **GET** /statistics/v1/Scorings/consolidated/daily | /v1/Scorings/consolidated/daily |
| [**v1StatisticsConsolidated**](Class3ForBackEndOptionalApi.md#v1StatisticsConsolidated) | **GET** /statistics/v1/Statistics/consolidated | /v1/Statistics/consolidated |
| [**v1StatisticsConsolidatedDaily**](Class3ForBackEndOptionalApi.md#v1StatisticsConsolidatedDaily) | **GET** /statistics/v1/Statistics/consolidated/daily | /v1/Statistics/consolidated/daily |


<a id="v1ScoringsConsolidated"></a>
# **v1ScoringsConsolidated**
> v1ScoringsConsolidated(deviceToken, startDate, endDate, tag, instanceId, appId, companyId)

/v1/Scorings/consolidated

/v1/Scorings/consolidated

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3ForBackEndOptionalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    Class3ForBackEndOptionalApi apiInstance = new Class3ForBackEndOptionalApi(defaultClient);
    String deviceToken = ""; // String | 
    String startDate = "2021-01-17T01:04:22.840Z"; // String | 
    String endDate = "2021-01-18T01:04:22.840Z"; // String | 
    String tag = ""; // String | 
    String instanceId = ""; // String | 
    String appId = ""; // String | 
    String companyId = ""; // String | 
    try {
      apiInstance.v1ScoringsConsolidated(deviceToken, startDate, endDate, tag, instanceId, appId, companyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3ForBackEndOptionalApi#v1ScoringsConsolidated");
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

<a id="v1ScoringsConsolidatedDaily"></a>
# **v1ScoringsConsolidatedDaily**
> V1ScoringsConsolidatedDaily200Response v1ScoringsConsolidatedDaily(deviceToken, startDate, endDate, tag, instanceId, appId, companyId)

/v1/Scorings/consolidated/daily

/v1/Scorings/consolidated/daily

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3ForBackEndOptionalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    Class3ForBackEndOptionalApi apiInstance = new Class3ForBackEndOptionalApi(defaultClient);
    String deviceToken = ""; // String | 
    String startDate = "2021-01-17T01:04:22.840Z"; // String | 
    String endDate = "2021-01-18T01:04:22.840Z"; // String | 
    String tag = ""; // String | 
    String instanceId = ""; // String | 
    String appId = ""; // String | 
    String companyId = ""; // String | 
    try {
      V1ScoringsConsolidatedDaily200Response result = apiInstance.v1ScoringsConsolidatedDaily(deviceToken, startDate, endDate, tag, instanceId, appId, companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3ForBackEndOptionalApi#v1ScoringsConsolidatedDaily");
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

[**V1ScoringsConsolidatedDaily200Response**](V1ScoringsConsolidatedDaily200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Strict-Transport-Security -  <br>  * X-Powered-By -  <br>  * X-StackifyID -  <br>  |

<a id="v1StatisticsConsolidated"></a>
# **v1StatisticsConsolidated**
> v1StatisticsConsolidated(deviceToken, startDate, endDate, tag, instanceId, appId, companyId)

/v1/Statistics/consolidated

/v1/Statistics/consolidated

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3ForBackEndOptionalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    Class3ForBackEndOptionalApi apiInstance = new Class3ForBackEndOptionalApi(defaultClient);
    String deviceToken = ""; // String | 
    String startDate = "2021-01-18"; // String | 
    String endDate = "2021-03-18"; // String | 
    String tag = ""; // String | 
    String instanceId = ""; // String | 
    String appId = ""; // String | 
    String companyId = ""; // String | 
    try {
      apiInstance.v1StatisticsConsolidated(deviceToken, startDate, endDate, tag, instanceId, appId, companyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3ForBackEndOptionalApi#v1StatisticsConsolidated");
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

<a id="v1StatisticsConsolidatedDaily"></a>
# **v1StatisticsConsolidatedDaily**
> v1StatisticsConsolidatedDaily(deviceToken, startDate, endDate, tag, instanceId, appId, companyId)

/v1/Statistics/consolidated/daily

/v1/Statistics/consolidated/daily

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3ForBackEndOptionalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    Class3ForBackEndOptionalApi apiInstance = new Class3ForBackEndOptionalApi(defaultClient);
    String deviceToken = ""; // String | 
    String startDate = "2021-01-17"; // String | 
    String endDate = "2021-01-18"; // String | 
    String tag = ""; // String | 
    String instanceId = ""; // String | 
    String appId = ""; // String | 
    String companyId = ""; // String | 
    try {
      apiInstance.v1StatisticsConsolidatedDaily(deviceToken, startDate, endDate, tag, instanceId, appId, companyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3ForBackEndOptionalApi#v1StatisticsConsolidatedDaily");
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

