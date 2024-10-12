# PortfolioPerformanceManagementApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**portfolioAbcPost**](PortfolioPerformanceManagementApi.md#portfolioAbcPost) | **POST** /portfolio/abc | ABC Analysis |
| [**portfolioFileToPortfolioPost**](PortfolioPerformanceManagementApi.md#portfolioFileToPortfolioPost) | **POST** /portfolio/file-to-portfolio | ABCxyz Analysis |
| [**portfolioForecastPerformanceRewindPost**](PortfolioPerformanceManagementApi.md#portfolioForecastPerformanceRewindPost) | **POST** /portfolio/forecast-performance-rewind | Planning level rewind to calculate and measure performance potential (internal versus iCUE). |
| [**portfolioPost**](PortfolioPerformanceManagementApi.md#portfolioPost) | **POST** /portfolio | ABCxyz Analysis |
| [**portfolioXyzPost**](PortfolioPerformanceManagementApi.md#portfolioXyzPost) | **POST** /portfolio/xyz | xyz Analysis |


<a id="portfolioAbcPost"></a>
# **portfolioAbcPost**
> List&lt;PortfolioAbcModel&gt; portfolioAbcPost(token, portfolioRequest)

ABC Analysis

Calculate and retrieve results of ABC (pareto analysis) per timeseries and planning level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfolioPerformanceManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PortfolioPerformanceManagementApi apiInstance = new PortfolioPerformanceManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PortfolioRequest portfolioRequest = new PortfolioRequest(); // PortfolioRequest | 
    try {
      List<PortfolioAbcModel> result = apiInstance.portfolioAbcPost(token, portfolioRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfolioPerformanceManagementApi#portfolioAbcPost");
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
| **portfolioRequest** | [**PortfolioRequest**](PortfolioRequest.md)|  | [optional] |

### Return type

[**List&lt;PortfolioAbcModel&gt;**](PortfolioAbcModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="portfolioFileToPortfolioPost"></a>
# **portfolioFileToPortfolioPost**
> portfolioFileToPortfolioPost(_file, token)

ABCxyz Analysis

Calculate and retrieve results of ABC (pareto analysis) and xyz (Coefficient of variation) per timeseries and planning level. This analysis is a powerful means to estbalish a proper planning cadence, best accuracy messures and optimal hyperparameters for the organization. It provides a balanced and actionable overview of the entire product portfolio.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfolioPerformanceManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PortfolioPerformanceManagementApi apiInstance = new PortfolioPerformanceManagementApi(defaultClient);
    File _file = new File("/path/to/file"); // File | 
    String token = "token_example"; // String | User Authentication Token
    try {
      apiInstance.portfolioFileToPortfolioPost(_file, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfolioPerformanceManagementApi#portfolioFileToPortfolioPost");
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
| **token** | **String**| User Authentication Token | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="portfolioForecastPerformanceRewindPost"></a>
# **portfolioForecastPerformanceRewindPost**
> RewindResponse portfolioForecastPerformanceRewindPost(token, forecastPerformanceRequest)

Planning level rewind to calculate and measure performance potential (internal versus iCUE).

Planning level rewind to calculate and measure performance potential (internal versus iCUE).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfolioPerformanceManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PortfolioPerformanceManagementApi apiInstance = new PortfolioPerformanceManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    ForecastPerformanceRequest forecastPerformanceRequest = new ForecastPerformanceRequest(); // ForecastPerformanceRequest | 
    try {
      RewindResponse result = apiInstance.portfolioForecastPerformanceRewindPost(token, forecastPerformanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfolioPerformanceManagementApi#portfolioForecastPerformanceRewindPost");
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
| **forecastPerformanceRequest** | [**ForecastPerformanceRequest**](ForecastPerformanceRequest.md)|  | [optional] |

### Return type

[**RewindResponse**](RewindResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="portfolioPost"></a>
# **portfolioPost**
> List&lt;PortfolioModel&gt; portfolioPost(token, portfolioRequest)

ABCxyz Analysis

Calculate and retrieve results of ABC (pareto analysis) and xyz (Coefficient of variation) per timeseries and planning level. This analysis is a powerful means to estbalish a proper planning cadence, best accuracy messures and optimal hyperparameters for the organization. It provides a balanced and actionable overview of the entire product portfolio.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfolioPerformanceManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PortfolioPerformanceManagementApi apiInstance = new PortfolioPerformanceManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PortfolioRequest portfolioRequest = new PortfolioRequest(); // PortfolioRequest | 
    try {
      List<PortfolioModel> result = apiInstance.portfolioPost(token, portfolioRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfolioPerformanceManagementApi#portfolioPost");
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
| **portfolioRequest** | [**PortfolioRequest**](PortfolioRequest.md)|  | [optional] |

### Return type

[**List&lt;PortfolioModel&gt;**](PortfolioModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="portfolioXyzPost"></a>
# **portfolioXyzPost**
> List&lt;PortfolioXyzModel&gt; portfolioXyzPost(token, portfolioRequest)

xyz Analysis

Calculate and retrieve results of xyz (Coefficient of variation) per timeseries and planning level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortfolioPerformanceManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PortfolioPerformanceManagementApi apiInstance = new PortfolioPerformanceManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    PortfolioRequest portfolioRequest = new PortfolioRequest(); // PortfolioRequest | 
    try {
      List<PortfolioXyzModel> result = apiInstance.portfolioXyzPost(token, portfolioRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortfolioPerformanceManagementApi#portfolioXyzPost");
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
| **portfolioRequest** | [**PortfolioRequest**](PortfolioRequest.md)|  | [optional] |

### Return type

[**List&lt;PortfolioXyzModel&gt;**](PortfolioXyzModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

