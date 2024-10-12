# InfoApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20Get**](InfoApi.md#apiV20Get) | **GET** /api/v2.0 |  |


<a id="apiV20Get"></a>
# **apiV20Get**
> apiV20Get(name, prefix, description)



Top level information about EnteroBase databases

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    InfoApi apiInstance = new InfoApi(defaultClient);
    String name = "name_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String prefix = "prefix_example"; // String | Database prefix, e.g. SAL for Salmonella
    String description = "description_example"; // String | Database description
    try {
      apiInstance.apiV20Get(name, prefix, description);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#apiV20Get");
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
| **name** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | [optional] |
| **prefix** | **String**| Database prefix, e.g. SAL for Salmonella | [optional] |
| **description** | **String**| Database description | [optional] |

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
| **200** | A info object |  -  |
| **403** | Unauthorised access for this specific resource or data |  -  |

