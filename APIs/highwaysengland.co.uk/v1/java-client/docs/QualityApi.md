# QualityApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**qualityGetDailyDataQualityForSite**](QualityApi.md#qualityGetDailyDataQualityForSite) | **GET** /v{version}/quality/daily | Get Site DailyQuality |
| [**qualityGetOverallDataQualityForSites**](QualityApi.md#qualityGetOverallDataQualityForSites) | **GET** /v{version}/quality/overall | Get Site OverallQuality |


<a id="qualityGetDailyDataQualityForSite"></a>
# **qualityGetDailyDataQualityForSite**
> DailyQualityResponse qualityGetDailyDataQualityForSite(siteId, startDate, endDate, version)

Get Site DailyQuality

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    QualityApi apiInstance = new QualityApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String startDate = "startDate_example"; // String | The start date of the report in the format ddmmyyyy (i.e 31012016)
    String endDate = "endDate_example"; // String | The end date of the report in the format ddmmyyyy (i.e 31012016)
    String version = "version_example"; // String | 
    try {
      DailyQualityResponse result = apiInstance.qualityGetDailyDataQualityForSite(siteId, startDate, endDate, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QualityApi#qualityGetDailyDataQualityForSite");
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
| **siteId** | **String**|  | |
| **startDate** | **String**| The start date of the report in the format ddmmyyyy (i.e 31012016) | |
| **endDate** | **String**| The end date of the report in the format ddmmyyyy (i.e 31012016) | |
| **version** | **String**|  | |

### Return type

[**DailyQualityResponse**](DailyQualityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request |  -  |
| **500** | Internal Server Error |  -  |

<a id="qualityGetOverallDataQualityForSites"></a>
# **qualityGetOverallDataQualityForSites**
> OverallQualityResponse qualityGetOverallDataQualityForSites(sites, startDate, endDate, version)

Get Site OverallQuality

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    QualityApi apiInstance = new QualityApi(defaultClient);
    String sites = "sites_example"; // String | Get site quality by site id delimited by ,
    String startDate = "startDate_example"; // String | The start date of the report in the format ddmmyyyy (i.e 31012016)
    String endDate = "endDate_example"; // String | The end date of the report in the format ddmmyyyy (i.e 31012016)
    String version = "version_example"; // String | 
    try {
      OverallQualityResponse result = apiInstance.qualityGetOverallDataQualityForSites(sites, startDate, endDate, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QualityApi#qualityGetOverallDataQualityForSites");
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
| **sites** | **String**| Get site quality by site id delimited by , | |
| **startDate** | **String**| The start date of the report in the format ddmmyyyy (i.e 31012016) | |
| **endDate** | **String**| The end date of the report in the format ddmmyyyy (i.e 31012016) | |
| **version** | **String**|  | |

### Return type

[**OverallQualityResponse**](OverallQualityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request |  -  |
| **500** | Internal Server Error |  -  |

