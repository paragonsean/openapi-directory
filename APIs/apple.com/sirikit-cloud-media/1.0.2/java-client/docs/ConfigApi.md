# ConfigApi

All URIs are relative to *https://cloudextension-testservice.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extensionConfiguration**](ConfigApi.md#extensionConfiguration) | **GET** /configuration | Configuration Resource |


<a id="extensionConfiguration"></a>
# **extensionConfiguration**
> ExtensionConfig extensionConfiguration(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, cacheControl, xApplecloudextensionRetryCount, ifNoneMatch)

Configuration Resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudextension-testservice.local/api");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
    BigDecimal requestTimeout = new BigDecimal(78); // BigDecimal | 
    String userAgent = "userAgent_example"; // String | 
    String acceptLanguage = "acceptLanguage_example"; // String | 
    String cacheControl = "cacheControl_example"; // String | 
    BigDecimal xApplecloudextensionRetryCount = new BigDecimal(78); // BigDecimal | 
    String ifNoneMatch = "ifNoneMatch_example"; // String | 
    try {
      ExtensionConfig result = apiInstance.extensionConfiguration(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, cacheControl, xApplecloudextensionRetryCount, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#extensionConfiguration");
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
| **cacheControl** | **String**|  | |
| **xApplecloudextensionRetryCount** | **BigDecimal**|  | [optional] |
| **ifNoneMatch** | **String**|  | [optional] |

### Return type

[**ExtensionConfig**](ExtensionConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jose

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Cache-Control -  <br>  * ETag -  <br>  * x-applecloudextension-session-id -  <br>  |
| **304** |  |  * Cache-Control -  <br>  * x-applecloudextension-session-id -  <br>  |

