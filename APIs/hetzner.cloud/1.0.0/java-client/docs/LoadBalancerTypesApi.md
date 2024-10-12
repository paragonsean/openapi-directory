# LoadBalancerTypesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**loadBalancerTypesGet**](LoadBalancerTypesApi.md#loadBalancerTypesGet) | **GET** /load_balancer_types | Get all Load Balancer Types |
| [**loadBalancerTypesIdGet**](LoadBalancerTypesApi.md#loadBalancerTypesIdGet) | **GET** /load_balancer_types/{id} | Get a Load Balancer Type |


<a id="loadBalancerTypesGet"></a>
# **loadBalancerTypesGet**
> LoadBalancerTypesGet200Response loadBalancerTypesGet(name)

Get all Load Balancer Types

Gets all Load Balancer type objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerTypesApi apiInstance = new LoadBalancerTypesApi(defaultClient);
    String name = "name_example"; // String | Can be used to filter Load Balancer types by their name. The response will only contain the Load Balancer type matching the specified name.
    try {
      LoadBalancerTypesGet200Response result = apiInstance.loadBalancerTypesGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerTypesApi#loadBalancerTypesGet");
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
| **name** | **String**| Can be used to filter Load Balancer types by their name. The response will only contain the Load Balancer type matching the specified name. | [optional] |

### Return type

[**LoadBalancerTypesGet200Response**](LoadBalancerTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;load_balancer_types&#x60; key in the reply contains an array of Load Balancer type objects with this structure |  -  |

<a id="loadBalancerTypesIdGet"></a>
# **loadBalancerTypesIdGet**
> LoadBalancerTypesIdGet200Response loadBalancerTypesIdGet(id)

Get a Load Balancer Type

Gets a specific Load Balancer type object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoadBalancerTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    LoadBalancerTypesApi apiInstance = new LoadBalancerTypesApi(defaultClient);
    Integer id = 56; // Integer | ID of Load Balancer type
    try {
      LoadBalancerTypesIdGet200Response result = apiInstance.loadBalancerTypesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoadBalancerTypesApi#loadBalancerTypesIdGet");
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
| **id** | **Integer**| ID of Load Balancer type | |

### Return type

[**LoadBalancerTypesIdGet200Response**](LoadBalancerTypesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;load_balancer_type&#x60; key in the reply contains a Load Balancer type object with this structure |  -  |

