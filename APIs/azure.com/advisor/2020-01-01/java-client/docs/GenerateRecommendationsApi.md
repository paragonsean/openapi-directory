# GenerateRecommendationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recommendationsGenerate**](GenerateRecommendationsApi.md#recommendationsGenerate) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/generateRecommendations |  |
| [**recommendationsGetGenerateStatus**](GenerateRecommendationsApi.md#recommendationsGetGenerateStatus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/generateRecommendations/{operationId} |  |


<a id="recommendationsGenerate"></a>
# **recommendationsGenerate**
> recommendationsGenerate(subscriptionId, apiVersion)



Initiates the recommendation generation or computation process for a subscription. This operation is asynchronous. The generated recommendations are stored in a cache in the Advisor service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenerateRecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GenerateRecommendationsApi apiInstance = new GenerateRecommendationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      apiInstance.recommendationsGenerate(subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenerateRecommendationsApi#recommendationsGenerate");
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
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

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
| **202** | Accepted. Recommendation generation has been accepted. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - The URL where the status of the asynchronous operation can be checked. <br>  |

<a id="recommendationsGetGenerateStatus"></a>
# **recommendationsGetGenerateStatus**
> recommendationsGetGenerateStatus(subscriptionId, operationId, apiVersion)



Retrieves the status of the recommendation computation or generation process. Invoke this API after calling the generation recommendation. The URI of this API is returned in the Location field of the response header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenerateRecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GenerateRecommendationsApi apiInstance = new GenerateRecommendationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    UUID operationId = UUID.randomUUID(); // UUID | The operation ID, which can be found from the Location field in the generate recommendation response header.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      apiInstance.recommendationsGetGenerateStatus(subscriptionId, operationId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenerateRecommendationsApi#recommendationsGetGenerateStatus");
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
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **operationId** | **UUID**| The operation ID, which can be found from the Location field in the generate recommendation response header. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

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
| **202** | Accepted. Recommendation generation is in progress. |  -  |
| **204** | NoContent. Recommendation generation has been completed. |  -  |

