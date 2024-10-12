# MetadataApi

All URIs are relative to *https://discovery.gsa.gov*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metadataGET**](MetadataApi.md#metadataGET) | **GET** /api/metadata/ | This endpoint returns metadata for the most recent data loads of SAM and FPDS data |


<a id="metadataGET"></a>
# **metadataGET**
> Object metadataGET()

This endpoint returns metadata for the most recent data loads of SAM and FPDS data

&lt;p&gt;This endpoint returns metadata for the most recent data loads of SAM and FPDS data. It takes no parameters.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://discovery.gsa.gov");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    try {
      Object result = apiInstance.metadataGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#metadataGET");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

