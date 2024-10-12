# DescriptionApi

All URIs are relative to *https://api.parliament.uk/search*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**descriptionGet**](DescriptionApi.md#descriptionGet) | **GET** /description | OpenSearch description document |


<a id="descriptionGet"></a>
# **descriptionGet**
> descriptionGet()

OpenSearch description document

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DescriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.parliament.uk/search");

    DescriptionApi apiInstance = new DescriptionApi(defaultClient);
    try {
      apiInstance.descriptionGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DescriptionApi#descriptionGet");
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
 - **Accept**: application/opensearchdescription+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Open Search Description |  -  |

