# ProductLifecycleManagementApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lifecycleManyToOnePost**](ProductLifecycleManagementApi.md#lifecycleManyToOnePost) | **POST** /lifecycle/many-to-one | Map from old product to new product to create artifical history |
| [**lifecycleOneToOnePost**](ProductLifecycleManagementApi.md#lifecycleOneToOnePost) | **POST** /lifecycle/one-to-one | Map from old product to new product to create artifical history |


<a id="lifecycleManyToOnePost"></a>
# **lifecycleManyToOnePost**
> PlanningLevelDataDto lifecycleManyToOnePost(token, lifecycleManyToOneRequest)

Map from old product to new product to create artifical history

Supports the creation of artificial startup history for new products, based on a flexible mapping of old to new. This is an Enterprise feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductLifecycleManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProductLifecycleManagementApi apiInstance = new ProductLifecycleManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    LifecycleManyToOneRequest lifecycleManyToOneRequest = new LifecycleManyToOneRequest(); // LifecycleManyToOneRequest | 
    try {
      PlanningLevelDataDto result = apiInstance.lifecycleManyToOnePost(token, lifecycleManyToOneRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductLifecycleManagementApi#lifecycleManyToOnePost");
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
| **token** | **String**| User Authentication Token | [optional] |
| **lifecycleManyToOneRequest** | [**LifecycleManyToOneRequest**](LifecycleManyToOneRequest.md)|  | [optional] |

### Return type

[**PlanningLevelDataDto**](PlanningLevelDataDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="lifecycleOneToOnePost"></a>
# **lifecycleOneToOnePost**
> PlanningLevelDataDto lifecycleOneToOnePost(token, lifecycleOneToOneRequest)

Map from old product to new product to create artifical history

Supports the creation of artificial startup history for new products, based on a flexible mapping of old to new. This is an Enterprise feature.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductLifecycleManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProductLifecycleManagementApi apiInstance = new ProductLifecycleManagementApi(defaultClient);
    String token = "token_example"; // String | User Authentication Token
    LifecycleOneToOneRequest lifecycleOneToOneRequest = new LifecycleOneToOneRequest(); // LifecycleOneToOneRequest | 
    try {
      PlanningLevelDataDto result = apiInstance.lifecycleOneToOnePost(token, lifecycleOneToOneRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductLifecycleManagementApi#lifecycleOneToOnePost");
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
| **token** | **String**| User Authentication Token | [optional] |
| **lifecycleOneToOneRequest** | [**LifecycleOneToOneRequest**](LifecycleOneToOneRequest.md)|  | [optional] |

### Return type

[**PlanningLevelDataDto**](PlanningLevelDataDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

