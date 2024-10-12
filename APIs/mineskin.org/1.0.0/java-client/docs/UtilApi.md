# UtilApi

All URIs are relative to *https://api.mineskin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**validateNameNameGet**](UtilApi.md#validateNameNameGet) | **GET** /validate/name/{name} |  |
| [**validateUuidUuidGet**](UtilApi.md#validateUuidUuidGet) | **GET** /validate/uuid/{uuid} |  |


<a id="validateNameNameGet"></a>
# **validateNameNameGet**
> UserValidation validateNameNameGet(name, userAgent)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mineskin.org");

    UtilApi apiInstance = new UtilApi(defaultClient);
    String name = "name_example"; // String | 
    String userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    try {
      UserValidation result = apiInstance.validateNameNameGet(name, userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilApi#validateNameNameGet");
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
| **name** | **String**|  | |
| **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | |

### Return type

[**UserValidation**](UserValidation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Validation info about the requested user |  -  |

<a id="validateUuidUuidGet"></a>
# **validateUuidUuidGet**
> UserValidation validateUuidUuidGet(uuid, userAgent)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mineskin.org");

    UtilApi apiInstance = new UtilApi(defaultClient);
    String uuid = "uuid_example"; // String | 
    String userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    try {
      UserValidation result = apiInstance.validateUuidUuidGet(uuid, userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilApi#validateUuidUuidGet");
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
| **uuid** | **String**|  | |
| **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | |

### Return type

[**UserValidation**](UserValidation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Validation info about the requested user |  -  |

