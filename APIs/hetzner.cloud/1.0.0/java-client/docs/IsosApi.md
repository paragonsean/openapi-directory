# IsosApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**isosGet**](IsosApi.md#isosGet) | **GET** /isos | Get all ISOs |
| [**isosIdGet**](IsosApi.md#isosIdGet) | **GET** /isos/{id} | Get an ISO |


<a id="isosGet"></a>
# **isosGet**
> IsosGet200Response isosGet(name, architecture, includeArchitectureWildcard)

Get all ISOs

Returns all available ISO objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IsosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    IsosApi apiInstance = new IsosApi(defaultClient);
    String name = "name_example"; // String | Can be used to filter ISOs by their name. The response will only contain the ISO matching the specified name.
    String architecture = "architecture_example"; // String | Return only ISOs with the given architecture.
    Boolean includeArchitectureWildcard = true; // Boolean | Include Images with wildcard architecture (architecture is null). Works only if architecture filter is specified.
    try {
      IsosGet200Response result = apiInstance.isosGet(name, architecture, includeArchitectureWildcard);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IsosApi#isosGet");
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
| **name** | **String**| Can be used to filter ISOs by their name. The response will only contain the ISO matching the specified name. | [optional] |
| **architecture** | **String**| Return only ISOs with the given architecture. | [optional] |
| **includeArchitectureWildcard** | **Boolean**| Include Images with wildcard architecture (architecture is null). Works only if architecture filter is specified. | [optional] |

### Return type

[**IsosGet200Response**](IsosGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;isos&#x60; key in the reply contains an array of iso objects with this structure |  -  |

<a id="isosIdGet"></a>
# **isosIdGet**
> IsosIdGet200Response isosIdGet(id)

Get an ISO

Returns a specific ISO object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IsosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    IsosApi apiInstance = new IsosApi(defaultClient);
    Integer id = 56; // Integer | ID of the ISO
    try {
      IsosIdGet200Response result = apiInstance.isosIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IsosApi#isosIdGet");
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
| **id** | **Integer**| ID of the ISO | |

### Return type

[**IsosIdGet200Response**](IsosIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;iso&#x60; key in the reply contains an array of ISO objects with this structure |  -  |

