# SharedEffectsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedEffectsGetId**](SharedEffectsApi.md#sharedEffectsGetId) | **GET** /Shared/Effects/{id} | Effects: Get by Id |


<a id="sharedEffectsGetId"></a>
# **sharedEffectsGetId**
> SharedEffects sharedEffectsGetId(id)

Effects: Get by Id

Get by Id: Use this method to retrieve a Effects object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedEffectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    SharedEffectsApi apiInstance = new SharedEffectsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      SharedEffects result = apiInstance.sharedEffectsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedEffectsApi#sharedEffectsGetId");
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
| **id** | **UUID**|  | |

### Return type

[**SharedEffects**](SharedEffects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

