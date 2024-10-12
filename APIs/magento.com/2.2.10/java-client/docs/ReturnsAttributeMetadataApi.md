# ReturnsAttributeMetadataApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmaRmaAttributesManagementV1GetAllAttributesMetadataGet**](ReturnsAttributeMetadataApi.md#rmaRmaAttributesManagementV1GetAllAttributesMetadataGet) | **GET** /V1/returnsAttributeMetadata | returnsAttributeMetadata |


<a id="rmaRmaAttributesManagementV1GetAllAttributesMetadataGet"></a>
# **rmaRmaAttributesManagementV1GetAllAttributesMetadataGet**
> List&lt;CustomerDataAttributeMetadataInterface&gt; rmaRmaAttributesManagementV1GetAllAttributesMetadataGet()

returnsAttributeMetadata

Get all attribute metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsAttributeMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsAttributeMetadataApi apiInstance = new ReturnsAttributeMetadataApi(defaultClient);
    try {
      List<CustomerDataAttributeMetadataInterface> result = apiInstance.rmaRmaAttributesManagementV1GetAllAttributesMetadataGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsAttributeMetadataApi#rmaRmaAttributesManagementV1GetAllAttributesMetadataGet");
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

[**List&lt;CustomerDataAttributeMetadataInterface&gt;**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

