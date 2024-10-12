# CollectionsApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCollectionMembers**](CollectionsApi.md#getCollectionMembers) | **GET** /collections/{pid}/members | Collection Members |


<a id="getCollectionMembers"></a>
# **getCollectionMembers**
> ProgrammesResponse getCollectionMembers(xAPIKey, pid, offset, limit)

Collection Members

Episodes and Clips from Collection 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String pid = "pid_example"; // String | pid
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      ProgrammesResponse result = apiInstance.getCollectionMembers(xAPIKey, pid, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#getCollectionMembers");
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
| **xAPIKey** | **String**| API_KEY | |
| **pid** | **String**| pid | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**ProgrammesResponse**](ProgrammesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Collection not found |  -  |
| **0** | Unexpected error |  -  |

