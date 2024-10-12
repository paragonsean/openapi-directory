# AnalyticsForPresenceAndAudienceApi

All URIs are relative to *https://visagecloud.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**counterUsingPOST**](AnalyticsForPresenceAndAudienceApi.md#counterUsingPOST) | **POST** /rest/v1.1/analytics/counting | Count individuals in streams or collections |
| [**presenceTimeseriesUsingPOST**](AnalyticsForPresenceAndAudienceApi.md#presenceTimeseriesUsingPOST) | **POST** /rest/v1.1/analytics/presence/timeseries | Show audience (based on number of occurrences of each person) breakdown per declared attribute (age, gender). |
| [**presenceTotalUsingPOST**](AnalyticsForPresenceAndAudienceApi.md#presenceTotalUsingPOST) | **POST** /rest/v1.1/analytics/presence/total | Show presence (based on number of occurences of each face) breakdown per declared attribute (age, gender) |


<a id="counterUsingPOST"></a>
# **counterUsingPOST**
> RestResponse counterUsingPOST(accessKey, secretKey, collectionIds, streamIds, startDateTime, endDateTime, visitDuration, maxIterations, maxBatchIterations, minNeighborsMergedPerIteration, mergingStep, shuffling)

Count individuals in streams or collections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsForPresenceAndAudienceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AnalyticsForPresenceAndAudienceApi apiInstance = new AnalyticsForPresenceAndAudienceApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    List<String> collectionIds = Arrays.asList(); // List<String> | Collection ids
    List<String> streamIds = Arrays.asList(); // List<String> | Stream Ids
    OffsetDateTime startDateTime = OffsetDateTime.now(); // OffsetDateTime | startDateTime
    OffsetDateTime endDateTime = OffsetDateTime.now(); // OffsetDateTime | endDateTime
    Long visitDuration = 3600000L; // Long | visitDuration
    Integer maxIterations = 1; // Integer | maxIterations
    Integer maxBatchIterations = 1; // Integer | maxBatchIterations
    Integer minNeighborsMergedPerIteration = 5; // Integer | minNeighborsMergedPerIteration
    Double mergingStep = 1.0D; // Double | mergingStep
    Boolean shuffling = false; // Boolean | shuffling
    try {
      RestResponse result = apiInstance.counterUsingPOST(accessKey, secretKey, collectionIds, streamIds, startDateTime, endDateTime, visitDuration, maxIterations, maxBatchIterations, minNeighborsMergedPerIteration, mergingStep, shuffling);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsForPresenceAndAudienceApi#counterUsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **collectionIds** | [**List&lt;String&gt;**](String.md)| Collection ids | [optional] |
| **streamIds** | [**List&lt;String&gt;**](String.md)| Stream Ids | [optional] |
| **startDateTime** | **OffsetDateTime**| startDateTime | [optional] |
| **endDateTime** | **OffsetDateTime**| endDateTime | [optional] |
| **visitDuration** | **Long**| visitDuration | [optional] [default to 3600000] |
| **maxIterations** | **Integer**| maxIterations | [optional] [default to 1] |
| **maxBatchIterations** | **Integer**| maxBatchIterations | [optional] [default to 1] |
| **minNeighborsMergedPerIteration** | **Integer**| minNeighborsMergedPerIteration | [optional] [default to 5] |
| **mergingStep** | **Double**| mergingStep | [optional] [default to 1.0] |
| **shuffling** | **Boolean**| shuffling | [optional] [default to false] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="presenceTimeseriesUsingPOST"></a>
# **presenceTimeseriesUsingPOST**
> RestResponse presenceTimeseriesUsingPOST(accessKey, secretKey, attributes, streamIds, startDateTime, endDateTime, step)

Show audience (based on number of occurrences of each person) breakdown per declared attribute (age, gender).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsForPresenceAndAudienceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AnalyticsForPresenceAndAudienceApi apiInstance = new AnalyticsForPresenceAndAudienceApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    List<String> attributes = Arrays.asList(); // List<String> | attributes
    List<String> streamIds = Arrays.asList(); // List<String> | Stream Ids
    OffsetDateTime startDateTime = OffsetDateTime.now(); // OffsetDateTime | startDateTime
    OffsetDateTime endDateTime = OffsetDateTime.now(); // OffsetDateTime | endDateTime
    Long step = 3600L; // Long | step
    try {
      RestResponse result = apiInstance.presenceTimeseriesUsingPOST(accessKey, secretKey, attributes, streamIds, startDateTime, endDateTime, step);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsForPresenceAndAudienceApi#presenceTimeseriesUsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **attributes** | [**List&lt;String&gt;**](String.md)| attributes | |
| **streamIds** | [**List&lt;String&gt;**](String.md)| Stream Ids | [optional] |
| **startDateTime** | **OffsetDateTime**| startDateTime | [optional] |
| **endDateTime** | **OffsetDateTime**| endDateTime | [optional] |
| **step** | **Long**| step | [optional] [default to 3600] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="presenceTotalUsingPOST"></a>
# **presenceTotalUsingPOST**
> RestResponse presenceTotalUsingPOST(accessKey, secretKey, streamIds, attributes, startDateTime, endDateTime)

Show presence (based on number of occurences of each face) breakdown per declared attribute (age, gender)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsForPresenceAndAudienceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AnalyticsForPresenceAndAudienceApi apiInstance = new AnalyticsForPresenceAndAudienceApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    List<String> streamIds = Arrays.asList(); // List<String> | Stream Ids
    List<String> attributes = Arrays.asList(); // List<String> | attributes
    OffsetDateTime startDateTime = OffsetDateTime.now(); // OffsetDateTime | startDateTime
    OffsetDateTime endDateTime = OffsetDateTime.now(); // OffsetDateTime | endDateTime
    try {
      RestResponse result = apiInstance.presenceTotalUsingPOST(accessKey, secretKey, streamIds, attributes, startDateTime, endDateTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsForPresenceAndAudienceApi#presenceTotalUsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **streamIds** | [**List&lt;String&gt;**](String.md)| Stream Ids | |
| **attributes** | [**List&lt;String&gt;**](String.md)| attributes | |
| **startDateTime** | **OffsetDateTime**| startDateTime | [optional] |
| **endDateTime** | **OffsetDateTime**| endDateTime | [optional] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

