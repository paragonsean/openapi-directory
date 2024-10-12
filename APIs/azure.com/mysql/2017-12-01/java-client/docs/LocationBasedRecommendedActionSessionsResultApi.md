# LocationBasedRecommendedActionSessionsResultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationBasedRecommendedActionSessionsResultList**](LocationBasedRecommendedActionSessionsResultApi.md#locationBasedRecommendedActionSessionsResultList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DBforMySQL/locations/{locationName}/recommendedActionSessionsOperationResults/{operationId} |  |


<a id="locationBasedRecommendedActionSessionsResultList"></a>
# **locationBasedRecommendedActionSessionsResultList**
> RecommendationActionsResultList locationBasedRecommendedActionSessionsResultList(apiVersion, subscriptionId, locationName, operationId)



Recommendation action session operation result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationBasedRecommendedActionSessionsResultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationBasedRecommendedActionSessionsResultApi apiInstance = new LocationBasedRecommendedActionSessionsResultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String locationName = "locationName_example"; // String | The name of the location.
    String operationId = "operationId_example"; // String | The operation identifier.
    try {
      RecommendationActionsResultList result = apiInstance.locationBasedRecommendedActionSessionsResultList(apiVersion, subscriptionId, locationName, operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationBasedRecommendedActionSessionsResultApi#locationBasedRecommendedActionSessionsResultList");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **locationName** | **String**| The name of the location. | |
| **operationId** | **String**| The operation identifier. | |

### Return type

[**RecommendationActionsResultList**](RecommendationActionsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created |  -  |
| **201** | Created |  -  |

