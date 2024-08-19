# ElevateAccessApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**elevateAccessPost**](ElevateAccessApi.md#elevateAccessPost) | **POST** /providers/Microsoft.Authorization/elevateAccess |  |


<a id="elevateAccessPost"></a>
# **elevateAccessPost**
> elevateAccessPost(apiVersion)



Elevates access for a Global Administrator.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ElevateAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ElevateAccessApi apiInstance = new ElevateAccessApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.elevateAccessPost(apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ElevateAccessApi#elevateAccessPost");
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
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an HttpResponseMessage with HttpStatusCode 200. |  -  |

