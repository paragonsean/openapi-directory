# ContinuousApi

All URIs are relative to *https://api.truora.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createContinuousCheck**](ContinuousApi.md#createContinuousCheck) | **POST** /v1/continuous-checks |  |
| [**getContinuousCheck**](ContinuousApi.md#getContinuousCheck) | **GET** /v1/continuous-checks/{continuous_check_id} |  |
| [**listContinuousChecks**](ContinuousApi.md#listContinuousChecks) | **GET** /v1/continuous-checks |  |
| [**updateContinuousCheck**](ContinuousApi.md#updateContinuousCheck) | **PUT** /v1/continuous-checks/{continuous_check_id} |  |
| [**v1ContinuousChecksContinuousCheckIdHistoryGet**](ContinuousApi.md#v1ContinuousChecksContinuousCheckIdHistoryGet) | **GET** /v1/continuous-checks/{continuous_check_id}/history |  |


<a id="createContinuousCheck"></a>
# **createContinuousCheck**
> ContinuousCheck createContinuousCheck(checkId, frequency, status)



Creates a continuous check that will run background checks recurrently according to the frequency provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ContinuousApi apiInstance = new ContinuousApi(defaultClient);
    String checkId = "checkId_example"; // String | Background checks to be processed recurrently
    String frequency = "frequency_example"; // String | Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks
    String status = "status_example"; // String | Indicates whether the background checks must be processed recurrently (enabled | disabled)
    try {
      ContinuousCheck result = apiInstance.createContinuousCheck(checkId, frequency, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousApi#createContinuousCheck");
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
| **checkId** | **String**| Background checks to be processed recurrently | [optional] |
| **frequency** | **String**| Time between background checks. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks | [optional] |
| **status** | **String**| Indicates whether the background checks must be processed recurrently (enabled | disabled) | [optional] |

### Return type

[**ContinuousCheck**](ContinuousCheck.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |

<a id="getContinuousCheck"></a>
# **getContinuousCheck**
> ContinuousCheck getContinuousCheck(continuousCheckId)



Lists history associated with a Check. It can be paginated

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ContinuousApi apiInstance = new ContinuousApi(defaultClient);
    BigDecimal continuousCheckId = new BigDecimal(78); // BigDecimal | ID resulting from calling CreateContinuousCheck
    try {
      ContinuousCheck result = apiInstance.getContinuousCheck(continuousCheckId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousApi#getContinuousCheck");
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
| **continuousCheckId** | **BigDecimal**| ID resulting from calling CreateContinuousCheck | |

### Return type

[**ContinuousCheck**](ContinuousCheck.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listContinuousChecks"></a>
# **listContinuousChecks**
> ListContinuousChecksOutput listContinuousChecks()



Lists all continuous checks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ContinuousApi apiInstance = new ContinuousApi(defaultClient);
    try {
      ListContinuousChecksOutput result = apiInstance.listContinuousChecks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousApi#listContinuousChecks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListContinuousChecksOutput**](ListContinuousChecksOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateContinuousCheck"></a>
# **updateContinuousCheck**
> ContinuousCheck updateContinuousCheck(continuousCheckId, frequency, status)



Updates a continuous check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ContinuousApi apiInstance = new ContinuousApi(defaultClient);
    BigDecimal continuousCheckId = new BigDecimal(78); // BigDecimal | ID resulting from calling CreateContinuousCheck
    String frequency = "frequency_example"; // String | Time between background checks
    String status = "enabled"; // String | Indicates whether the background checks must be processed recurrently
    try {
      ContinuousCheck result = apiInstance.updateContinuousCheck(continuousCheckId, frequency, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousApi#updateContinuousCheck");
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
| **continuousCheckId** | **BigDecimal**| ID resulting from calling CreateContinuousCheck | |
| **frequency** | **String**| Time between background checks | |
| **status** | **String**| Indicates whether the background checks must be processed recurrently | [enum: enabled, disabled] |

### Return type

[**ContinuousCheck**](ContinuousCheck.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v1ContinuousChecksContinuousCheckIdHistoryGet"></a>
# **v1ContinuousChecksContinuousCheckIdHistoryGet**
> GetContiuousCheckHistoryOutput v1ContinuousChecksContinuousCheckIdHistoryGet(continuousCheckId)



Lists background check logs. It can be paginated  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ContinuousApi apiInstance = new ContinuousApi(defaultClient);
    String continuousCheckId = "continuousCheckId_example"; // String | 
    try {
      GetContiuousCheckHistoryOutput result = apiInstance.v1ContinuousChecksContinuousCheckIdHistoryGet(continuousCheckId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousApi#v1ContinuousChecksContinuousCheckIdHistoryGet");
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
| **continuousCheckId** | **String**|  | |

### Return type

[**GetContiuousCheckHistoryOutput**](GetContiuousCheckHistoryOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok |  -  |

