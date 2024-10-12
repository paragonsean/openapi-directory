# TestApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**echo**](TestApi.md#echo) | **GET** /v2/test | Echo text |
| [**validate**](TestApi.md#validate) | **GET** /v2/test/validate | Validate input |


<a id="echo"></a>
# **echo**
> TestEcho echo(text)

Echo text

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");

    TestApi apiInstance = new TestApi(defaultClient);
    String text = "ok"; // String | Text to echo
    try {
      TestEcho result = apiInstance.echo(text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#echo");
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
| **text** | **String**| Text to echo | [optional] [default to ok] |

### Return type

[**TestEcho**](TestEcho.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="validate"></a>
# **validate**
> TestValidate validate(id, tag, userAgent)

Validate input

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");

    TestApi apiInstance = new TestApi(defaultClient);
    Integer id = 123; // Integer | Integer ID
    List<String> tag = Arrays.asList(); // List<String> | List of tags
    String userAgent = "userAgent_example"; // String | User agent
    try {
      TestValidate result = apiInstance.validate(id, tag, userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#validate");
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
| **id** | **Integer**| Integer ID | |
| **tag** | [**List&lt;String&gt;**](String.md)| List of tags | [optional] |
| **userAgent** | **String**| User agent | [optional] |

### Return type

[**TestValidate**](TestValidate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

