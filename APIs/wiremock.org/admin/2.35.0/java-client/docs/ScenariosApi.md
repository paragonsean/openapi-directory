# ScenariosApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminScenariosGet**](ScenariosApi.md#adminScenariosGet) | **GET** /__admin/scenarios | Get all scenarios |
| [**adminScenariosResetPost**](ScenariosApi.md#adminScenariosResetPost) | **POST** /__admin/scenarios/reset | Reset the state of all scenarios |


<a id="adminScenariosGet"></a>
# **adminScenariosGet**
> AdminScenariosGet200Response adminScenariosGet()

Get all scenarios

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScenariosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ScenariosApi apiInstance = new ScenariosApi(defaultClient);
    try {
      AdminScenariosGet200Response result = apiInstance.adminScenariosGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScenariosApi#adminScenariosGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminScenariosGet200Response**](AdminScenariosGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All scenarios |  -  |

<a id="adminScenariosResetPost"></a>
# **adminScenariosResetPost**
> adminScenariosResetPost()

Reset the state of all scenarios

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScenariosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ScenariosApi apiInstance = new ScenariosApi(defaultClient);
    try {
      apiInstance.adminScenariosResetPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling ScenariosApi#adminScenariosResetPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully reset |  -  |

