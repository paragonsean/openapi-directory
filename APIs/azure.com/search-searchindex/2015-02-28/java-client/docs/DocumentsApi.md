# DocumentsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**documentsCount**](DocumentsApi.md#documentsCount) | **GET** /docs/$count |  |


<a id="documentsCount"></a>
# **documentsCount**
> Long documentsCount(apiVersion, clientRequestId)



Queries the number of documents in the Azure Search index.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    UUID clientRequestId = UUID.randomUUID(); // UUID | Tracking ID sent with the request to help with debugging.
    try {
      Long result = apiInstance.documentsCount(apiVersion, clientRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsCount");
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
| **apiVersion** | **String**| Client Api Version. | |
| **clientRequestId** | **UUID**| Tracking ID sent with the request to help with debugging. | [optional] |

### Return type

**Long**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

