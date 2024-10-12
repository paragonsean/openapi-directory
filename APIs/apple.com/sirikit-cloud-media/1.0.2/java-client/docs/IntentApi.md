# IntentApi

All URIs are relative to *https://cloudextension-testservice.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addMediaIntentHandling**](IntentApi.md#addMediaIntentHandling) | **POST** /intent/addMedia | addMedia |
| [**playMediaIntentHandling**](IntentApi.md#playMediaIntentHandling) | **POST** /intent/playMedia | playMedia |
| [**updateMediaAffinityIntentHandling**](IntentApi.md#updateMediaAffinityIntentHandling) | **POST** /intent/updateMediaAffinity | updateMediaAffinity |


<a id="addMediaIntentHandling"></a>
# **addMediaIntentHandling**
> List&lt;AddMediaIntentHandlingInvocationResponse&gt; addMediaIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, xApplecloudextensionRetryCount, addMediaIntentHandlingInvocation)

addMedia

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudextension-testservice.local/api");

    IntentApi apiInstance = new IntentApi(defaultClient);
    String xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
    BigDecimal requestTimeout = new BigDecimal(78); // BigDecimal | 
    String userAgent = "userAgent_example"; // String | 
    String acceptLanguage = "acceptLanguage_example"; // String | 
    BigDecimal xApplecloudextensionRetryCount = new BigDecimal(78); // BigDecimal | 
    List<AddMediaIntentHandlingInvocation> addMediaIntentHandlingInvocation = Arrays.asList(); // List<AddMediaIntentHandlingInvocation> | 
    try {
      List<AddMediaIntentHandlingInvocationResponse> result = apiInstance.addMediaIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, xApplecloudextensionRetryCount, addMediaIntentHandlingInvocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntentApi#addMediaIntentHandling");
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
| **xApplecloudextensionSessionId** | **String**|  | |
| **requestTimeout** | **BigDecimal**|  | |
| **userAgent** | **String**|  | |
| **acceptLanguage** | **String**|  | |
| **xApplecloudextensionRetryCount** | **BigDecimal**|  | [optional] |
| **addMediaIntentHandlingInvocation** | [**List&lt;AddMediaIntentHandlingInvocation&gt;**](AddMediaIntentHandlingInvocation.md)|  | [optional] |

### Return type

[**List&lt;AddMediaIntentHandlingInvocationResponse&gt;**](AddMediaIntentHandlingInvocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * x-applecloudextension-session-id -  <br>  |

<a id="playMediaIntentHandling"></a>
# **playMediaIntentHandling**
> List&lt;PlayMediaIntentHandlingInvocationResponse&gt; playMediaIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, xApplecloudextensionRetryCount, playMediaIntentHandlingInvocation)

playMedia

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudextension-testservice.local/api");

    IntentApi apiInstance = new IntentApi(defaultClient);
    String xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
    BigDecimal requestTimeout = new BigDecimal(78); // BigDecimal | 
    String userAgent = "userAgent_example"; // String | 
    String acceptLanguage = "acceptLanguage_example"; // String | 
    BigDecimal xApplecloudextensionRetryCount = new BigDecimal(78); // BigDecimal | 
    List<PlayMediaIntentHandlingInvocation> playMediaIntentHandlingInvocation = Arrays.asList(); // List<PlayMediaIntentHandlingInvocation> | 
    try {
      List<PlayMediaIntentHandlingInvocationResponse> result = apiInstance.playMediaIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, xApplecloudextensionRetryCount, playMediaIntentHandlingInvocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntentApi#playMediaIntentHandling");
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
| **xApplecloudextensionSessionId** | **String**|  | |
| **requestTimeout** | **BigDecimal**|  | |
| **userAgent** | **String**|  | |
| **acceptLanguage** | **String**|  | |
| **xApplecloudextensionRetryCount** | **BigDecimal**|  | [optional] |
| **playMediaIntentHandlingInvocation** | [**List&lt;PlayMediaIntentHandlingInvocation&gt;**](PlayMediaIntentHandlingInvocation.md)|  | [optional] |

### Return type

[**List&lt;PlayMediaIntentHandlingInvocationResponse&gt;**](PlayMediaIntentHandlingInvocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * x-applecloudextension-session-id -  <br>  |

<a id="updateMediaAffinityIntentHandling"></a>
# **updateMediaAffinityIntentHandling**
> List&lt;UpdateMediaAffinityIntentHandlingInvocationResponse&gt; updateMediaAffinityIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, xApplecloudextensionRetryCount, updateMediaAffinityIntentHandlingInvocation)

updateMediaAffinity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudextension-testservice.local/api");

    IntentApi apiInstance = new IntentApi(defaultClient);
    String xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
    BigDecimal requestTimeout = new BigDecimal(78); // BigDecimal | 
    String userAgent = "userAgent_example"; // String | 
    String acceptLanguage = "acceptLanguage_example"; // String | 
    BigDecimal xApplecloudextensionRetryCount = new BigDecimal(78); // BigDecimal | 
    List<UpdateMediaAffinityIntentHandlingInvocation> updateMediaAffinityIntentHandlingInvocation = Arrays.asList(); // List<UpdateMediaAffinityIntentHandlingInvocation> | 
    try {
      List<UpdateMediaAffinityIntentHandlingInvocationResponse> result = apiInstance.updateMediaAffinityIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, xApplecloudextensionRetryCount, updateMediaAffinityIntentHandlingInvocation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntentApi#updateMediaAffinityIntentHandling");
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
| **xApplecloudextensionSessionId** | **String**|  | |
| **requestTimeout** | **BigDecimal**|  | |
| **userAgent** | **String**|  | |
| **acceptLanguage** | **String**|  | |
| **xApplecloudextensionRetryCount** | **BigDecimal**|  | [optional] |
| **updateMediaAffinityIntentHandlingInvocation** | [**List&lt;UpdateMediaAffinityIntentHandlingInvocation&gt;**](UpdateMediaAffinityIntentHandlingInvocation.md)|  | [optional] |

### Return type

[**List&lt;UpdateMediaAffinityIntentHandlingInvocationResponse&gt;**](UpdateMediaAffinityIntentHandlingInvocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * x-applecloudextension-session-id -  <br>  |

