# LocationBasedRecommendedActionSessionsOperationStatusApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationBasedRecommendedActionSessionsOperationStatusGet**](LocationBasedRecommendedActionSessionsOperationStatusApi.md#locationBasedRecommendedActionSessionsOperationStatusGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DBforMariaDB/locations/{locationName}/recommendedActionSessionsAzureAsyncOperation/{operationId} |  |


<a id="locationBasedRecommendedActionSessionsOperationStatusGet"></a>
# **locationBasedRecommendedActionSessionsOperationStatusGet**
> RecommendedActionSessionsOperationStatus locationBasedRecommendedActionSessionsOperationStatusGet(apiVersion, subscriptionId, locationName, operationId)



Recommendation action session operation status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationBasedRecommendedActionSessionsOperationStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationBasedRecommendedActionSessionsOperationStatusApi apiInstance = new LocationBasedRecommendedActionSessionsOperationStatusApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String locationName = "locationName_example"; // String | The name of the location.
    String operationId = "operationId_example"; // String | The operation identifier.
    try {
      RecommendedActionSessionsOperationStatus result = apiInstance.locationBasedRecommendedActionSessionsOperationStatusGet(apiVersion, subscriptionId, locationName, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationBasedRecommendedActionSessionsOperationStatusApi#locationBasedRecommendedActionSessionsOperationStatusGet");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **locationName** | **String**| The name of the location. | |
| **operationId** | **String**| The operation identifier. | |

### Return type

[**RecommendedActionSessionsOperationStatus**](RecommendedActionSessionsOperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |

