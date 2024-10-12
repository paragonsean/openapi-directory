# DefaultApi

All URIs are relative to *https://football-prediction-api.p.rapidapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2ListFederationsGet**](DefaultApi.md#apiV2ListFederationsGet) | **GET** /api/v2/list-federations |  |
| [**apiV2ListMarketsGet**](DefaultApi.md#apiV2ListMarketsGet) | **GET** /api/v2/list-markets |  |
| [**apiV2PerformanceStatsGet**](DefaultApi.md#apiV2PerformanceStatsGet) | **GET** /api/v2/performance-stats |  |
| [**apiV2PredictionsGet**](DefaultApi.md#apiV2PredictionsGet) | **GET** /api/v2/predictions |  |
| [**apiV2PredictionsIdGet**](DefaultApi.md#apiV2PredictionsIdGet) | **GET** /api/v2/predictions/{id} |  |


<a id="apiV2ListFederationsGet"></a>
# **apiV2ListFederationsGet**
> ApiV2ListFederationsGet200Response apiV2ListFederationsGet(xRapidApiKey)



Returns an array of all the available federations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://football-prediction-api.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID xRapidApiKey = UUID.randomUUID(); // UUID | Your key obtained from https://boggio-analytics.com/fp-api/
    try {
      ApiV2ListFederationsGet200Response result = apiInstance.apiV2ListFederationsGet(xRapidApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV2ListFederationsGet");
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
| **xRapidApiKey** | **UUID**| Your key obtained from https://boggio-analytics.com/fp-api/ | [optional] |

### Return type

[**ApiV2ListFederationsGet200Response**](ApiV2ListFederationsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Static response, shows available federations. |  -  |
| **404** | Bad request, check response for detailed errors. |  -  |

<a id="apiV2ListMarketsGet"></a>
# **apiV2ListMarketsGet**
> ApiV2ListMarketsGet200Response apiV2ListMarketsGet(xRapidApiKey)



Returns an array of all the supported prediction markets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://football-prediction-api.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID xRapidApiKey = UUID.randomUUID(); // UUID | Your key obtained from https://boggio-analytics.com/fp-api/
    try {
      ApiV2ListMarketsGet200Response result = apiInstance.apiV2ListMarketsGet(xRapidApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV2ListMarketsGet");
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
| **xRapidApiKey** | **UUID**| Your key obtained from https://boggio-analytics.com/fp-api/ | [optional] |

### Return type

[**ApiV2ListMarketsGet200Response**](ApiV2ListMarketsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Static response, shows available markets for the current subscription and all available markets in general. |  -  |
| **404** | Bad request, check response for detailed errors. |  -  |

<a id="apiV2PerformanceStatsGet"></a>
# **apiV2PerformanceStatsGet**
> ApiV2PerformanceStatsGet200Response apiV2PerformanceStatsGet(xRapidApiKey)



Returns predictions accuracy in the last 1, 7, 14, 30 days.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://football-prediction-api.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID xRapidApiKey = UUID.randomUUID(); // UUID | Your key obtained from https://boggio-analytics.com/fp-api/
    try {
      ApiV2PerformanceStatsGet200Response result = apiInstance.apiV2PerformanceStatsGet(xRapidApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV2PerformanceStatsGet");
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
| **xRapidApiKey** | **UUID**| Your key obtained from https://boggio-analytics.com/fp-api/ | [optional] |

### Return type

[**ApiV2PerformanceStatsGet200Response**](ApiV2PerformanceStatsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Good request, returns object that contains accuracy and other datails about predictions. |  -  |
| **404** | Bad request, check response for detailed errors. |  -  |

<a id="apiV2PredictionsGet"></a>
# **apiV2PredictionsGet**
> apiV2PredictionsGet(xRapidApiKey)



This endpoint returns by default the next non-expired football predictions. URL parameters can be specified to show specific date in the past or future or to filter by federation and prediction market name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://football-prediction-api.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID xRapidApiKey = UUID.randomUUID(); // UUID | Your key obtained from https://boggio-analytics.com/fp-api/
    try {
      apiInstance.apiV2PredictionsGet(xRapidApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV2PredictionsGet");
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
| **xRapidApiKey** | **UUID**| Your key obtained from https://boggio-analytics.com/fp-api/ | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Good request, returns object that contains data array with all predictions. |  -  |
| **404** | Bad request, check response for detailed errors. |  -  |

<a id="apiV2PredictionsIdGet"></a>
# **apiV2PredictionsIdGet**
> ApiV2PredictionsIdGet200Response apiV2PredictionsIdGet(id)



Returns all predictions available for a match id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://football-prediction-api.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer id = 56; // Integer | ID of match
    try {
      ApiV2PredictionsIdGet200Response result = apiInstance.apiV2PredictionsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV2PredictionsIdGet");
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
| **id** | **Integer**| ID of match | |

### Return type

[**ApiV2PredictionsIdGet200Response**](ApiV2PredictionsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Good request, returns object that contains all the predictions for a certain event. |  -  |
| **404** | Bad request, check response for detailed errors. |  -  |

