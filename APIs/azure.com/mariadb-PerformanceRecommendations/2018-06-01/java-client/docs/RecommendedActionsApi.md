# RecommendedActionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recommendedActionsGet**](RecommendedActionsApi.md#recommendedActionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/advisors/{advisorName}/recommendedActions/{recommendedActionName} |  |
| [**recommendedActionsListByServer**](RecommendedActionsApi.md#recommendedActionsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/advisors/{advisorName}/recommendedActions |  |


<a id="recommendedActionsGet"></a>
# **recommendedActionsGet**
> RecommendationAction recommendedActionsGet(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, recommendedActionName)



Retrieve recommended actions from the advisor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendedActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendedActionsApi apiInstance = new RecommendedActionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String serverName = "serverName_example"; // String | The name of the server.
    String advisorName = "advisorName_example"; // String | The advisor name for recommendation action.
    String recommendedActionName = "recommendedActionName_example"; // String | The recommended action name.
    try {
      RecommendationAction result = apiInstance.recommendedActionsGet(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, recommendedActionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendedActionsApi#recommendedActionsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **serverName** | **String**| The name of the server. | |
| **advisorName** | **String**| The advisor name for recommendation action. | |
| **recommendedActionName** | **String**| The recommended action name. | |

### Return type

[**RecommendationAction**](RecommendationAction.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendedActionsListByServer"></a>
# **recommendedActionsListByServer**
> RecommendationActionsResultList recommendedActionsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, sessionId)



Retrieve recommended actions from the advisor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendedActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendedActionsApi apiInstance = new RecommendedActionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String serverName = "serverName_example"; // String | The name of the server.
    String advisorName = "advisorName_example"; // String | The advisor name for recommendation action.
    String sessionId = "sessionId_example"; // String | The recommendation action session identifier.
    try {
      RecommendationActionsResultList result = apiInstance.recommendedActionsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendedActionsApi#recommendedActionsListByServer");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **serverName** | **String**| The name of the server. | |
| **advisorName** | **String**| The advisor name for recommendation action. | |
| **sessionId** | **String**| The recommendation action session identifier. | [optional] |

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
| **200** | OK |  -  |

