# DomainsApi

All URIs are relative to *https://api.zalando.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainsGet**](DomainsApi.md#domainsGet) | **GET** /domains | Shop Domains |


<a id="domainsGet"></a>
# **domainsGet**
> List&lt;Domain&gt; domainsGet()

Shop Domains

Zalando API Domains Schema

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.zalando.com");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    try {
      List<Domain> result = apiInstance.domainsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsGet");
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

[**List&lt;Domain&gt;**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domains response. |  -  |

