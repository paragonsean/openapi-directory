# ServicepacksApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicepacks**](ServicepacksApi.md#servicepacks) | **GET** /servicepacks | Overview of service packs |


<a id="servicepacks"></a>
# **servicepacks**
> List&lt;Servicepack&gt; servicepacks()

Overview of service packs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicepacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    ServicepacksApi apiInstance = new ServicepacksApi(defaultClient);
    try {
      List<Servicepack> result = apiInstance.servicepacks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicepacksApi#servicepacks");
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

[**List&lt;Servicepack&gt;**](Servicepack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

