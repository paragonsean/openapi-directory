# VersionsApi

All URIs are relative to *http://optimade.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVersionsVersionsGet**](VersionsApi.md#getVersionsVersionsGet) | **GET** /versions | Get Versions |


<a id="getVersionsVersionsGet"></a>
# **getVersionsVersionsGet**
> String getVersionsVersionsGet()

Get Versions

Respond with the text/csv representation for the served versions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://optimade.local");

    VersionsApi apiInstance = new VersionsApi(defaultClient);
    try {
      String result = apiInstance.getVersionsVersionsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VersionsApi#getVersionsVersionsGet");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv; header=present

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

