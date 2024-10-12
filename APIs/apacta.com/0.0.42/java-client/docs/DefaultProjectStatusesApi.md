# DefaultProjectStatusesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectStatusesAddDefaultPost**](DefaultProjectStatusesApi.md#projectStatusesAddDefaultPost) | **POST** /project_statuses/add_default | Add default project statuses to company |


<a id="projectStatusesAddDefaultPost"></a>
# **projectStatusesAddDefaultPost**
> AddDefaultProjectStatusesError projectStatusesAddDefaultPost()

Add default project statuses to company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultProjectStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    DefaultProjectStatusesApi apiInstance = new DefaultProjectStatusesApi(defaultClient);
    try {
      AddDefaultProjectStatusesError result = apiInstance.projectStatusesAddDefaultPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultProjectStatusesApi#projectStatusesAddDefaultPost");
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

[**AddDefaultProjectStatusesError**](AddDefaultProjectStatusesError.md)

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

