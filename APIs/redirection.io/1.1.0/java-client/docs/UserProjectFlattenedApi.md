# UserProjectFlattenedApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUserProjectFlattenedItem**](UserProjectFlattenedApi.md#getUserProjectFlattenedItem) | **GET** /user-project-flatteneds/{id} | Retrieves a UserProjectFlattened resource. |


<a id="getUserProjectFlattenedItem"></a>
# **getUserProjectFlattenedItem**
> UserProjectFlattenedRead getUserProjectFlattenedItem(id)

Retrieves a UserProjectFlattened resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserProjectFlattenedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserProjectFlattenedApi apiInstance = new UserProjectFlattenedApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      UserProjectFlattenedRead result = apiInstance.getUserProjectFlattenedItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserProjectFlattenedApi#getUserProjectFlattenedItem");
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
| **id** | **String**|  | |

### Return type

[**UserProjectFlattenedRead**](UserProjectFlattenedRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserProjectFlattened resource response |  -  |
| **404** | Resource not found |  -  |

