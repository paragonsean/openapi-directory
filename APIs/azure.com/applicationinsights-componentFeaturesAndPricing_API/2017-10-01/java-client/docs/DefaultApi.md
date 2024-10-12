# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**componentCurrentPricingPlanCreateAndUpdate**](DefaultApi.md#componentCurrentPricingPlanCreateAndUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/pricingPlans/current |  |
| [**componentCurrentPricingPlanGet**](DefaultApi.md#componentCurrentPricingPlanGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/pricingPlans/current |  |
| [**componentCurrentPricingPlanUpdate**](DefaultApi.md#componentCurrentPricingPlanUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/pricingPlans/current |  |


<a id="componentCurrentPricingPlanCreateAndUpdate"></a>
# **componentCurrentPricingPlanCreateAndUpdate**
> ApplicationInsightsComponentPricingPlan componentCurrentPricingPlanCreateAndUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, pricingPlanProperties)



Replace current pricing plan for an Application Insights component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    ApplicationInsightsComponentPricingPlan pricingPlanProperties = new ApplicationInsightsComponentPricingPlan(); // ApplicationInsightsComponentPricingPlan | Properties that need to be specified to update current pricing plan for an Application Insights component.
    try {
      ApplicationInsightsComponentPricingPlan result = apiInstance.componentCurrentPricingPlanCreateAndUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, pricingPlanProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#componentCurrentPricingPlanCreateAndUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **pricingPlanProperties** | [**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)| Properties that need to be specified to update current pricing plan for an Application Insights component. | |

### Return type

[**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request when updating billing features for an Application Insights component. The updated current billing features are returned. |  -  |

<a id="componentCurrentPricingPlanGet"></a>
# **componentCurrentPricingPlanGet**
> ApplicationInsightsComponentPricingPlan componentCurrentPricingPlanGet(resourceGroupName, apiVersion, subscriptionId, resourceName)



Returns the current pricing plan setting for an Application Insights component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    try {
      ApplicationInsightsComponentPricingPlan result = apiInstance.componentCurrentPricingPlanGet(resourceGroupName, apiVersion, subscriptionId, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#componentCurrentPricingPlanGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |

### Return type

[**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Application Insights component pricing plan definition. |  -  |

<a id="componentCurrentPricingPlanUpdate"></a>
# **componentCurrentPricingPlanUpdate**
> ApplicationInsightsComponentPricingPlan componentCurrentPricingPlanUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, pricingPlanProperties)



Update current pricing plan for an Application Insights component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
    ApplicationInsightsComponentPricingPlan pricingPlanProperties = new ApplicationInsightsComponentPricingPlan(); // ApplicationInsightsComponentPricingPlan | Properties that need to be specified to update current pricing plan for an Application Insights component.
    try {
      ApplicationInsightsComponentPricingPlan result = apiInstance.componentCurrentPricingPlanUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, pricingPlanProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#componentCurrentPricingPlanUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceName** | **String**| The name of the Application Insights component resource. | |
| **pricingPlanProperties** | [**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)| Properties that need to be specified to update current pricing plan for an Application Insights component. | |

### Return type

[**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request when updating billing features for an Application Insights component. The updated current billing features are returned. |  -  |

