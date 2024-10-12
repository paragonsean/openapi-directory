# ConsolidatedSafeScoringApi

All URIs are relative to *https://api.telematicssdk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1ScoringsConsolidatedDaily_0**](ConsolidatedSafeScoringApi.md#v1ScoringsConsolidatedDaily_0) | **GET** /statistics/v1/Scorings/consolidated/daily | /v1/Scorings/consolidated/daily |
| [**v1ScoringsConsolidated_0**](ConsolidatedSafeScoringApi.md#v1ScoringsConsolidated_0) | **GET** /statistics/v1/Scorings/consolidated | /v1/Scorings/consolidated |


<a id="v1ScoringsConsolidatedDaily_0"></a>
# **v1ScoringsConsolidatedDaily_0**
> V1ScoringsConsolidatedDaily200Response v1ScoringsConsolidatedDaily_0(deviceToken, startDate, endDate, tag, instanceId, appId, companyId)

/v1/Scorings/consolidated/daily

/v1/Scorings/consolidated/daily

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsolidatedSafeScoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    ConsolidatedSafeScoringApi apiInstance = new ConsolidatedSafeScoringApi(defaultClient);
    String deviceToken = ""; // String | 
    String startDate = "2021-01-17T01:04:22.840Z"; // String | 
    String endDate = "2021-01-18T01:04:22.840Z"; // String | 
    String tag = ""; // String | 
    String instanceId = ""; // String | 
    String appId = ""; // String | 
    String companyId = ""; // String | 
    try {
      V1ScoringsConsolidatedDaily200Response result = apiInstance.v1ScoringsConsolidatedDaily_0(deviceToken, startDate, endDate, tag, instanceId, appId, companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsolidatedSafeScoringApi#v1ScoringsConsolidatedDaily_0");
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

<a id="v1ScoringsConsolidated_0"></a>
# **v1ScoringsConsolidated_0**
> v1ScoringsConsolidated_0(deviceToken, startDate, endDate, tag, instanceId, appId, companyId)

/v1/Scorings/consolidated

/v1/Scorings/consolidated

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsolidatedSafeScoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    ConsolidatedSafeScoringApi apiInstance = new ConsolidatedSafeScoringApi(defaultClient);
    String deviceToken = ""; // String | 
    String startDate = "2021-01-17T01:04:22.840Z"; // String | 
    String endDate = "2021-01-18T01:04:22.840Z"; // String | 
    String tag = ""; // String | 
    String instanceId = ""; // String | 
    String appId = ""; // String | 
    String companyId = ""; // String | 
    try {
      apiInstance.v1ScoringsConsolidated_0(deviceToken, startDate, endDate, tag, instanceId, appId, companyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsolidatedSafeScoringApi#v1ScoringsConsolidated_0");
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

