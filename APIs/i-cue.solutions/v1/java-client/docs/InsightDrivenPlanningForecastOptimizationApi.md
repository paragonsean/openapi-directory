# InsightDrivenPlanningForecastOptimizationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forecastAIHistoryAndForecastPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastAIHistoryAndForecastPost) | **POST** /forecast/AI/history-and-forecast | History and forecast utilizing advanced machine learning models |
| [**forecastAIPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastAIPost) | **POST** /forecast/AI | Forecast utilizing advanced machine learning models |
| [**forecastFileToForecastPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastFileToForecastPost) | **POST** /forecast/file-to-forecast | Forecast from file |
| [**forecastForecastBottomUpPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastForecastBottomUpPost) | **POST** /forecast/forecast-bottom-up | Bottom up forecasting |
| [**forecastForecastTopDownPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastForecastTopDownPost) | **POST** /forecast/forecast-top-down | Top down forecasting |
| [**forecastFullDetailPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastFullDetailPost) | **POST** /forecast/full-detail | Full forecast result details, including error, trend seasonality and outlier |
| [**forecastHistoryAndForecastPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastHistoryAndForecastPost) | **POST** /forecast/history-and-forecast | History and forecast for fast timeseries view |
| [**forecastOptimalParameterPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastOptimalParameterPost) | **POST** /forecast/optimal-parameter | Get optimal parameter per method |
| [**forecastPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastPost) | **POST** /forecast | Forecasts only, for faster results |
| [**forecastRerunPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastRerunPost) | **POST** /forecast/rerun | Rerun previously uploaded planning level |
| [**forecastResultJobIdGet**](InsightDrivenPlanningForecastOptimizationApi.md#forecastResultJobIdGet) | **GET** /forecast/result/{jobId} | Forecast result |
| [**forecastStatusJobIdGet**](InsightDrivenPlanningForecastOptimizationApi.md#forecastStatusJobIdGet) | **GET** /forecast/status/{jobId} | Forecast status |
| [**outlierPost**](InsightDrivenPlanningForecastOptimizationApi.md#outlierPost) | **POST** /outlier | Get outlier |


<a id="forecastAIHistoryAndForecastPost"></a>
# **forecastAIHistoryAndForecastPost**
> JobResponse forecastAIHistoryAndForecastPost(token, aiPlanningLevelRequest)

History and forecast utilizing advanced machine learning models

History and forecast utilizing advanced machine learning models. Please be mindful of enhanced execution times (~1-2s per timeseries).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    AiPlanningLevelRequest aiPlanningLevelRequest = new AiPlanningLevelRequest(); // AiPlanningLevelRequest | 
    try {
      JobResponse result = apiInstance.forecastAIHistoryAndForecastPost(token, aiPlanningLevelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastAIHistoryAndForecastPost");
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
| **aiPlanningLevelRequest** | [**AiPlanningLevelRequest**](AiPlanningLevelRequest.md)|  | [optional] |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastAIPost"></a>
# **forecastAIPost**
> JobResponse forecastAIPost(token, aiPlanningLevelRequest)

Forecast utilizing advanced machine learning models

Forecast AI is utilizing advanced machine learning models. Please be mindful of enhanced execution times (~1-2s per timeseries).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    AiPlanningLevelRequest aiPlanningLevelRequest = new AiPlanningLevelRequest(); // AiPlanningLevelRequest | 
    try {
      JobResponse result = apiInstance.forecastAIPost(token, aiPlanningLevelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastAIPost");
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
| **aiPlanningLevelRequest** | [**AiPlanningLevelRequest**](AiPlanningLevelRequest.md)|  | [optional] |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastFileToForecastPost"></a>
# **forecastFileToForecastPost**
> JobResponse forecastFileToForecastPost(_file, method, token, discardData, errorType, holdOutPeriod, noFcst, outlierDetection, periodicity)

Forecast from file

Forecast from file allows for quick analysis via Microsoft Excel and CSV file format. Please check documentation link for help.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    File _file = new File("/path/to/file"); // File | 
    String method = "AutoBestPick"; // String | 
    String token = "token_example"; // String | User Authentication Token
    Boolean discardData = true; // Boolean | 
    String errorType = "MeanAbsolutePercentageError"; // String | 
    Integer holdOutPeriod = 56; // Integer | 
    Integer noFcst = 56; // Integer | 
    Boolean outlierDetection = true; // Boolean | 
    Integer periodicity = 56; // Integer | 
    try {
      JobResponse result = apiInstance.forecastFileToForecastPost(_file, method, token, discardData, errorType, holdOutPeriod, noFcst, outlierDetection, periodicity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastFileToForecastPost");
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
| **_file** | **File**|  | |
| **method** | **String**|  | [enum: AutoBestPick, BoxJenkins, Croston, DoubleExponentialSmoothing, HoltWinters, SingleExponentialSmoothing, iCUE1, SimpleMovingAverage] |
| **token** | **String**| User Authentication Token | [optional] |
| **discardData** | **Boolean**|  | [optional] |
| **errorType** | **String**|  | [optional] [enum: MeanAbsolutePercentageError, MeanSquaredError, MeanAbsoluteError, MedianAbsoluteDeviation, None] |
| **holdOutPeriod** | **Integer**|  | [optional] |
| **noFcst** | **Integer**|  | [optional] |
| **outlierDetection** | **Boolean**|  | [optional] |
| **periodicity** | **Integer**|  | [optional] |

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastForecastBottomUpPost"></a>
# **forecastForecastBottomUpPost**
> ForecastBottomUpResponse forecastForecastBottomUpPost(token, planningLevelRequest)

Bottom up forecasting

Calculate forecast by timeseries and sum results up to establish forecast for top level timeseries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PlanningLevelRequest planningLevelRequest = new PlanningLevelRequest(); // PlanningLevelRequest | 
    try {
      ForecastBottomUpResponse result = apiInstance.forecastForecastBottomUpPost(token, planningLevelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastForecastBottomUpPost");
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
| **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] |

### Return type

[**ForecastBottomUpResponse**](ForecastBottomUpResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastForecastTopDownPost"></a>
# **forecastForecastTopDownPost**
> forecastForecastTopDownPost(token, planningLevelRequest)

Top down forecasting

Calculate forecast based on sum of of lower level timeseries and distribute forecast down based on ratios. Great feature for planning levels with dynamic timeseries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PlanningLevelRequest planningLevelRequest = new PlanningLevelRequest(); // PlanningLevelRequest | 
    try {
      apiInstance.forecastForecastTopDownPost(token, planningLevelRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastForecastTopDownPost");
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
| **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastFullDetailPost"></a>
# **forecastFullDetailPost**
> FullDetailsForecastResponse forecastFullDetailPost(token, planningLevelRequest)

Full forecast result details, including error, trend seasonality and outlier

Response provides full forecast result details, including error, trend seasonality and outlier. Great for advanced analysis.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PlanningLevelRequest planningLevelRequest = new PlanningLevelRequest(); // PlanningLevelRequest | 
    try {
      FullDetailsForecastResponse result = apiInstance.forecastFullDetailPost(token, planningLevelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastFullDetailPost");
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
| **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] |

### Return type

[**FullDetailsForecastResponse**](FullDetailsForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastHistoryAndForecastPost"></a>
# **forecastHistoryAndForecastPost**
> HistoryAndForecastResponse forecastHistoryAndForecastPost(token, planningLevelRequest)

History and forecast for fast timeseries view

Reponse provides history and forecast per timeseries. Great for visualizing results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PlanningLevelRequest planningLevelRequest = new PlanningLevelRequest(); // PlanningLevelRequest | 
    try {
      HistoryAndForecastResponse result = apiInstance.forecastHistoryAndForecastPost(token, planningLevelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastHistoryAndForecastPost");
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
| **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] |

### Return type

[**HistoryAndForecastResponse**](HistoryAndForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastOptimalParameterPost"></a>
# **forecastOptimalParameterPost**
> OptimalParameterResponse forecastOptimalParameterPost(token, planningLevelRequest)

Get optimal parameter per method

Use the optimal parameter sets created by iCUE to set the method parameters of your internal planning system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PlanningLevelRequest planningLevelRequest = new PlanningLevelRequest(); // PlanningLevelRequest | 
    try {
      OptimalParameterResponse result = apiInstance.forecastOptimalParameterPost(token, planningLevelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastOptimalParameterPost");
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
| **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] |

### Return type

[**OptimalParameterResponse**](OptimalParameterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastPost"></a>
# **forecastPost**
> ForecastResponse forecastPost(token, planningLevelRequest)

Forecasts only, for faster results

To support maximum operation and integration speed, this endpoint only returns the calculated forecast.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PlanningLevelRequest planningLevelRequest = new PlanningLevelRequest(); // PlanningLevelRequest | 
    try {
      ForecastResponse result = apiInstance.forecastPost(token, planningLevelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastPost");
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
| **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] |

### Return type

[**ForecastResponse**](ForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastRerunPost"></a>
# **forecastRerunPost**
> ForecastResponse forecastRerunPost(token, planningLevelReRunRequest)

Rerun previously uploaded planning level

Rerun previously uploaded planning level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PlanningLevelReRunRequest planningLevelReRunRequest = new PlanningLevelReRunRequest(); // PlanningLevelReRunRequest | 
    try {
      ForecastResponse result = apiInstance.forecastRerunPost(token, planningLevelReRunRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastRerunPost");
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
| **planningLevelReRunRequest** | [**PlanningLevelReRunRequest**](PlanningLevelReRunRequest.md)|  | [optional] |

### Return type

[**ForecastResponse**](ForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="forecastResultJobIdGet"></a>
# **forecastResultJobIdGet**
> forecastResultJobIdGet(jobId, token)

Forecast result

Get result for forecast job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    Integer jobId = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.forecastResultJobIdGet(jobId, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastResultJobIdGet");
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
| **jobId** | **Integer**|  | |
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

<a id="forecastStatusJobIdGet"></a>
# **forecastStatusJobIdGet**
> forecastStatusJobIdGet(jobId, token)

Forecast status

Get status for forecast job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    Integer jobId = 56; // Integer | 
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.forecastStatusJobIdGet(jobId, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#forecastStatusJobIdGet");
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
| **jobId** | **Integer**|  | |
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

<a id="outlierPost"></a>
# **outlierPost**
> List&lt;TimeSeriesOutliersResponse&gt; outlierPost(token, outliersRequest)

Get outlier

Identify outliers (single and repetitive spikes, seasonality, masked outliers, trend and level jumps, amongst other topics) and use for cleansing of the history stream prior to forecast claculation. Depending on math model used, this approach often improves results dramatically, as it removes disturbances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightDrivenPlanningForecastOptimizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InsightDrivenPlanningForecastOptimizationApi apiInstance = new InsightDrivenPlanningForecastOptimizationApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    OutliersRequest outliersRequest = new OutliersRequest(); // OutliersRequest | 
    try {
      List<TimeSeriesOutliersResponse> result = apiInstance.outlierPost(token, outliersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightDrivenPlanningForecastOptimizationApi#outlierPost");
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
| **outliersRequest** | [**OutliersRequest**](OutliersRequest.md)|  | [optional] |

### Return type

[**List&lt;TimeSeriesOutliersResponse&gt;**](TimeSeriesOutliersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

