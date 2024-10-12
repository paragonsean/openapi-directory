# GeneralApi

All URIs are relative to *http://192.168.1.5:8990*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connectionDetailsPost**](GeneralApi.md#connectionDetailsPost) | **POST** /ConnectionDetails | Get user&#39;s login details |
| [**isAlivePost**](GeneralApi.md#isAlivePost) | **POST** /IsAlive | Get server status |


<a id="connectionDetailsPost"></a>
# **connectionDetailsPost**
> ConnectionDetailsResult connectionDetailsPost(body)

Get user&#39;s login details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://192.168.1.5:8990");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    ConnectionDetailsRequest body = new ConnectionDetailsRequest(); // ConnectionDetailsRequest | 
    try {
      ConnectionDetailsResult result = apiInstance.connectionDetailsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#connectionDetailsPost");
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
| **body** | [**ConnectionDetailsRequest**](ConnectionDetailsRequest.md)|  | |

### Return type

[**ConnectionDetailsResult**](ConnectionDetailsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ConnectionDetailsResult |  -  |

<a id="isAlivePost"></a>
# **isAlivePost**
> IsAliveResult isAlivePost(body)

Get server status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://192.168.1.5:8990");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    IsAliveRequest body = new IsAliveRequest(); // IsAliveRequest | 
    try {
      IsAliveResult result = apiInstance.isAlivePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#isAlivePost");
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
| **body** | [**IsAliveRequest**](IsAliveRequest.md)|  | |

### Return type

[**IsAliveResult**](IsAliveResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IsAliveResult |  -  |

