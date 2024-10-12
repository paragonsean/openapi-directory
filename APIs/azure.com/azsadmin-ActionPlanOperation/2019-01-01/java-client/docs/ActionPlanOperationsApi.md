# ActionPlanOperationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actionPlanOperationsGet**](ActionPlanOperationsApi.md#actionPlanOperationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans/{planId}/operations/{operationId} |  |
| [**actionPlanOperationsList**](ActionPlanOperationsApi.md#actionPlanOperationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/actionPlans/{planId}/operations |  |


<a id="actionPlanOperationsGet"></a>
# **actionPlanOperationsGet**
> ActionPlanOperationResourceEntity actionPlanOperationsGet(subscriptionId, planId, operationId, apiVersion)



Gets the specified action plan operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionPlanOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ActionPlanOperationsApi apiInstance = new ActionPlanOperationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String planId = "planId_example"; // String | Identifier of the action plan.
    String operationId = "operationId_example"; // String | Identifier of the action plan operation.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    try {
      ActionPlanOperationResourceEntity result = apiInstance.actionPlanOperationsGet(subscriptionId, planId, operationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionPlanOperationsApi#actionPlanOperationsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **planId** | **String**| Identifier of the action plan. | |
| **operationId** | **String**| Identifier of the action plan operation. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |

### Return type

[**ActionPlanOperationResourceEntity**](ActionPlanOperationResourceEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NOT FOUND |  -  |

<a id="actionPlanOperationsList"></a>
# **actionPlanOperationsList**
> ActionPlanOperationsList actionPlanOperationsList(subscriptionId, planId, apiVersion)



Lists the action plan operations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionPlanOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ActionPlanOperationsApi apiInstance = new ActionPlanOperationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String planId = "planId_example"; // String | Identifier of the action plan.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    try {
      ActionPlanOperationsList result = apiInstance.actionPlanOperationsList(subscriptionId, planId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionPlanOperationsApi#actionPlanOperationsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **planId** | **String**| Identifier of the action plan. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |

### Return type

[**ActionPlanOperationsList**](ActionPlanOperationsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

