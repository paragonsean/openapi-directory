# OnThisDayApi

All URIs are relative to *https://api.fungenerators.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**factOnthisdayBornGet**](OnThisDayApi.md#factOnthisdayBornGet) | **GET** /fact/onthisday/born |  |
| [**factOnthisdayDiedGet**](OnThisDayApi.md#factOnthisdayDiedGet) | **GET** /fact/onthisday/died |  |
| [**factOnthisdayEventGet**](OnThisDayApi.md#factOnthisdayEventGet) | **GET** /fact/onthisday/event |  |


<a id="factOnthisdayBornGet"></a>
# **factOnthisdayBornGet**
> factOnthisdayBornGet(month, day)



Returns a random ( famous/ relatively famous ) person born on a given day and month

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnThisDayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    OnThisDayApi apiInstance = new OnThisDayApi(defaultClient);
    String month = "month_example"; // String | Optional month (1-12). Defaults to current month
    String day = "day_example"; // String | Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month.
    try {
      apiInstance.factOnthisdayBornGet(month, day);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnThisDayApi#factOnthisdayBornGet");
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
| **month** | **String**| Optional month (1-12). Defaults to current month | [optional] |
| **day** | **String**| Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month. | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="factOnthisdayDiedGet"></a>
# **factOnthisdayDiedGet**
> factOnthisdayDiedGet(month, day)



Returns a random ( famous/ relatively famous ) person died on a given day and month

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnThisDayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    OnThisDayApi apiInstance = new OnThisDayApi(defaultClient);
    String month = "month_example"; // String | Optional month (1-12). Defaults to current month
    String day = "day_example"; // String | Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month.
    try {
      apiInstance.factOnthisdayDiedGet(month, day);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnThisDayApi#factOnthisdayDiedGet");
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
| **month** | **String**| Optional month (1-12). Defaults to current month | [optional] |
| **day** | **String**| Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month. | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="factOnthisdayEventGet"></a>
# **factOnthisdayEventGet**
> factOnthisdayEventGet(month, day)



Returns a random ( famous/ relatively famous ) historic event on a given day and month

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnThisDayApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    OnThisDayApi apiInstance = new OnThisDayApi(defaultClient);
    String month = "month_example"; // String | Optional month (1-12). Defaults to current month
    String day = "day_example"; // String | Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month.
    try {
      apiInstance.factOnthisdayEventGet(month, day);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnThisDayApi#factOnthisdayEventGet");
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
| **month** | **String**| Optional month (1-12). Defaults to current month | [optional] |
| **day** | **String**| Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month. | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

