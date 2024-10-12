# DefaultApi

All URIs are relative to *https://www.wolframalpha.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWolframAlphaResults**](DefaultApi.md#getWolframAlphaResults) | **GET** /api/v1/llm-api | Get Wolfram|Alpha results |
| [**getWolframCloudResults**](DefaultApi.md#getWolframCloudResults) | **GET** /api/v1/cloud-plugin | Evaluate Wolfram Language code |


<a id="getWolframAlphaResults"></a>
# **getWolframAlphaResults**
> getWolframAlphaResults(input)

Get Wolfram|Alpha results

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
    defaultClient.setBasePath("https://www.wolframalpha.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String input = "input_example"; // String | the input
    try {
      apiInstance.getWolframAlphaResults(input);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getWolframAlphaResults");
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
| **input** | **String**| the input | |

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
| **200** | The result of the Wolfram|Alpha query |  -  |
| **400** | The request is missing the &#39;input&#39; parameter |  -  |
| **403** | Unauthorized |  -  |
| **500** | Wolfram|Alpha was unable to generate a result |  -  |
| **501** | Wolfram|Alpha was unable to generate a result |  -  |
| **503** | Service temporarily unavailable. This may be the result of too many requests. |  -  |

<a id="getWolframCloudResults"></a>
# **getWolframCloudResults**
> getWolframCloudResults(input)

Evaluate Wolfram Language code

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
    defaultClient.setBasePath("https://www.wolframalpha.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String input = "input_example"; // String | the input expression
    try {
      apiInstance.getWolframCloudResults(input);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getWolframCloudResults");
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
| **input** | **String**| the input expression | |

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
| **200** | The result of the Wolfram Language evaluation |  -  |
| **400** | The request is missing the &#39;input&#39; parameter |  -  |
| **403** | Unauthorized |  -  |
| **500** | Wolfram Cloud was unable to generate a result |  -  |
| **503** | Service temporarily unavailable. This may be the result of too many requests. |  -  |

