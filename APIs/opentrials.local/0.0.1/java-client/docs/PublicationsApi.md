# PublicationsApi

All URIs are relative to *http://opentrials.local/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPublication**](PublicationsApi.md#getPublication) | **GET** /publications/{id} |  |


<a id="getPublication"></a>
# **getPublication**
> Publication getPublication(id)



Returns publication details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    PublicationsApi apiInstance = new PublicationsApi(defaultClient);
    String id = "id_example"; // String | ID of the publication
    try {
      Publication result = apiInstance.getPublication(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicationsApi#getPublication");
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
| **id** | **String**| ID of the publication | |

### Return type

[**Publication**](Publication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Publication not found |  -  |
| **0** | Error |  -  |

