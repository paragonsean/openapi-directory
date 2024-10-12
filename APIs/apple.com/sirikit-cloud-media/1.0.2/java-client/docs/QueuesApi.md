# QueuesApi

All URIs are relative to *https://cloudextension-testservice.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**playMediaOnQueue**](QueuesApi.md#playMediaOnQueue) | **POST** /queues/playMedia | playMedia |
| [**updateActivityOnQueue**](QueuesApi.md#updateActivityOnQueue) | **POST** /queues/updateActivity | updateActivity |


<a id="playMediaOnQueue"></a>
# **playMediaOnQueue**
> Queue playMediaOnQueue(xApplecloudextensionSessionId, userAgent, acceptLanguage, xApplecloudextensionRetryCount, playMediaRequest)

playMedia

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudextension-testservice.local/api");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
    String userAgent = "userAgent_example"; // String | 
    String acceptLanguage = "acceptLanguage_example"; // String | 
    BigDecimal xApplecloudextensionRetryCount = new BigDecimal(78); // BigDecimal | 
    PlayMediaRequest playMediaRequest = new PlayMediaRequest(); // PlayMediaRequest | 
    try {
      Queue result = apiInstance.playMediaOnQueue(xApplecloudextensionSessionId, userAgent, acceptLanguage, xApplecloudextensionRetryCount, playMediaRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#playMediaOnQueue");
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
| **userAgent** | **String**|  | |
| **acceptLanguage** | **String**|  | |
| **xApplecloudextensionRetryCount** | **BigDecimal**|  | [optional] |
| **playMediaRequest** | [**PlayMediaRequest**](PlayMediaRequest.md)|  | [optional] |

### Return type

[**Queue**](Queue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **204** |  |  -  |
| **401** |  |  -  |
| **410** |  |  -  |

<a id="updateActivityOnQueue"></a>
# **updateActivityOnQueue**
> UpdateActivityResponse updateActivityOnQueue(xApplecloudextensionSessionId, userAgent, acceptLanguage, xApplecloudextensionRetryCount, updateActivityRequest)

updateActivity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudextension-testservice.local/api");

    QueuesApi apiInstance = new QueuesApi(defaultClient);
    String xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
    String userAgent = "userAgent_example"; // String | 
    String acceptLanguage = "acceptLanguage_example"; // String | 
    BigDecimal xApplecloudextensionRetryCount = new BigDecimal(78); // BigDecimal | 
    UpdateActivityRequest updateActivityRequest = new UpdateActivityRequest(); // UpdateActivityRequest | 
    try {
      UpdateActivityResponse result = apiInstance.updateActivityOnQueue(xApplecloudextensionSessionId, userAgent, acceptLanguage, xApplecloudextensionRetryCount, updateActivityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueuesApi#updateActivityOnQueue");
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
| **userAgent** | **String**|  | |
| **acceptLanguage** | **String**|  | |
| **xApplecloudextensionRetryCount** | **BigDecimal**|  | [optional] |
| **updateActivityRequest** | [**UpdateActivityRequest**](UpdateActivityRequest.md)|  | [optional] |

### Return type

[**UpdateActivityResponse**](UpdateActivityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **204** |  |  -  |
| **401** |  |  -  |
| **404** |  |  -  |
| **410** |  |  -  |

