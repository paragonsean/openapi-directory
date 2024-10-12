# ServerTypesApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serverTypesGet**](ServerTypesApi.md#serverTypesGet) | **GET** /server_types | Get all Server Types |
| [**serverTypesIdGet**](ServerTypesApi.md#serverTypesIdGet) | **GET** /server_types/{id} | Get a Server Type |


<a id="serverTypesGet"></a>
# **serverTypesGet**
> ServerTypesGet200Response serverTypesGet(name)

Get all Server Types

Gets all Server type objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ServerTypesApi apiInstance = new ServerTypesApi(defaultClient);
    String name = "name_example"; // String | Can be used to filter Server types by their name. The response will only contain the Server type matching the specified name.
    try {
      ServerTypesGet200Response result = apiInstance.serverTypesGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerTypesApi#serverTypesGet");
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
| **name** | **String**| Can be used to filter Server types by their name. The response will only contain the Server type matching the specified name. | [optional] |

### Return type

[**ServerTypesGet200Response**](ServerTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;server_types&#x60; key in the reply contains an array of Server type objects with this structure |  -  |

<a id="serverTypesIdGet"></a>
# **serverTypesIdGet**
> ServerTypesIdGet200Response serverTypesIdGet(id)

Get a Server Type

Gets a specific Server type object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    ServerTypesApi apiInstance = new ServerTypesApi(defaultClient);
    Integer id = 56; // Integer | ID of Server Type
    try {
      ServerTypesIdGet200Response result = apiInstance.serverTypesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerTypesApi#serverTypesIdGet");
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
| **id** | **Integer**| ID of Server Type | |

### Return type

[**ServerTypesIdGet200Response**](ServerTypesIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;server_type&#x60; key in the reply contains a Server type object with this structure |  -  |

