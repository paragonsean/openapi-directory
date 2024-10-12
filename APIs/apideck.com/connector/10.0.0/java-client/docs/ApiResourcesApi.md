# ApiResourcesApi

All URIs are relative to *https://unify.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiResourceCoverageOne**](ApiResourcesApi.md#apiResourceCoverageOne) | **GET** /connector/apis/{id}/resources/{resource_id}/coverage | Get API Resource Coverage |
| [**apiResourcesOne**](ApiResourcesApi.md#apiResourcesOne) | **GET** /connector/apis/{id}/resources/{resource_id} | Get API Resource |


<a id="apiResourceCoverageOne"></a>
# **apiResourceCoverageOne**
> GetApiResourceCoverageResponse apiResourceCoverageOne(xApideckAppId, id, resourceId)

Get API Resource Coverage

Get API Resource Coverage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ApiResourcesApi apiInstance = new ApiResourcesApi(defaultClient);
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String id = "id_example"; // String | ID of the record you are acting upon.
    String resourceId = "resourceId_example"; // String | ID of the resource you are acting upon.
    try {
      GetApiResourceCoverageResponse result = apiInstance.apiResourceCoverageOne(xApideckAppId, id, resourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiResourcesApi#apiResourceCoverageOne");
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
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **id** | **String**| ID of the record you are acting upon. | |
| **resourceId** | **String**| ID of the resource you are acting upon. | |

### Return type

[**GetApiResourceCoverageResponse**](GetApiResourceCoverageResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ApiResources |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **0** | Unexpected error |  -  |

<a id="apiResourcesOne"></a>
# **apiResourcesOne**
> GetApiResourceResponse apiResourcesOne(xApideckAppId, id, resourceId)

Get API Resource

Get API Resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ApiResourcesApi apiInstance = new ApiResourcesApi(defaultClient);
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String id = "id_example"; // String | ID of the record you are acting upon.
    String resourceId = "resourceId_example"; // String | ID of the resource you are acting upon.
    try {
      GetApiResourceResponse result = apiInstance.apiResourcesOne(xApideckAppId, id, resourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiResourcesApi#apiResourcesOne");
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
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **id** | **String**| ID of the record you are acting upon. | |
| **resourceId** | **String**| ID of the resource you are acting upon. | |

### Return type

[**GetApiResourceResponse**](GetApiResourceResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ApiResources |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **0** | Unexpected error |  -  |

