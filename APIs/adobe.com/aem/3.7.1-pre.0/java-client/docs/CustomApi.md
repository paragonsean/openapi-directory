# CustomApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAemHealthCheck**](CustomApi.md#getAemHealthCheck) | **GET** /system/health |  |
| [**postConfigAemHealthCheckServlet**](CustomApi.md#postConfigAemHealthCheckServlet) | **POST** /apps/system/config/com.shinesolutions.healthcheck.hc.impl.ActiveBundleHealthCheck |  |
| [**postConfigAemPasswordReset**](CustomApi.md#postConfigAemPasswordReset) | **POST** /apps/system/config/com.shinesolutions.aem.passwordreset.Activator |  |


<a id="getAemHealthCheck"></a>
# **getAemHealthCheck**
> String getAemHealthCheck(tags, combineTagsOr)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: aemAuth
    HttpBasicAuth aemAuth = (HttpBasicAuth) defaultClient.getAuthentication("aemAuth");
    aemAuth.setUsername("YOUR USERNAME");
    aemAuth.setPassword("YOUR PASSWORD");

    CustomApi apiInstance = new CustomApi(defaultClient);
    String tags = "tags_example"; // String | 
    Boolean combineTagsOr = true; // Boolean | 
    try {
      String result = apiInstance.getAemHealthCheck(tags, combineTagsOr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApi#getAemHealthCheck");
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
| **tags** | **String**|  | [optional] |
| **combineTagsOr** | **Boolean**|  | [optional] |

### Return type

**String**

### Authorization

[aemAuth](../README.md#aemAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

<a id="postConfigAemHealthCheckServlet"></a>
# **postConfigAemHealthCheckServlet**
> postConfigAemHealthCheckServlet(bundlesIgnored, bundlesIgnoredAtTypeHint)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: aemAuth
    HttpBasicAuth aemAuth = (HttpBasicAuth) defaultClient.getAuthentication("aemAuth");
    aemAuth.setUsername("YOUR USERNAME");
    aemAuth.setPassword("YOUR PASSWORD");

    CustomApi apiInstance = new CustomApi(defaultClient);
    List<String> bundlesIgnored = Arrays.asList(); // List<String> | 
    String bundlesIgnoredAtTypeHint = "bundlesIgnoredAtTypeHint_example"; // String | 
    try {
      apiInstance.postConfigAemHealthCheckServlet(bundlesIgnored, bundlesIgnoredAtTypeHint);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApi#postConfigAemHealthCheckServlet");
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
| **bundlesIgnored** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **bundlesIgnoredAtTypeHint** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[aemAuth](../README.md#aemAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

<a id="postConfigAemPasswordReset"></a>
# **postConfigAemPasswordReset**
> postConfigAemPasswordReset(pwdresetAuthorizables, pwdresetAuthorizablesAtTypeHint)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: aemAuth
    HttpBasicAuth aemAuth = (HttpBasicAuth) defaultClient.getAuthentication("aemAuth");
    aemAuth.setUsername("YOUR USERNAME");
    aemAuth.setPassword("YOUR PASSWORD");

    CustomApi apiInstance = new CustomApi(defaultClient);
    List<String> pwdresetAuthorizables = Arrays.asList(); // List<String> | 
    String pwdresetAuthorizablesAtTypeHint = "pwdresetAuthorizablesAtTypeHint_example"; // String | 
    try {
      apiInstance.postConfigAemPasswordReset(pwdresetAuthorizables, pwdresetAuthorizablesAtTypeHint);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomApi#postConfigAemPasswordReset");
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
| **pwdresetAuthorizables** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **pwdresetAuthorizablesAtTypeHint** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[aemAuth](../README.md#aemAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

