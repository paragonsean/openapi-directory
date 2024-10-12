# AcquiredPlansApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acquiredPlansCreate**](AcquiredPlansApi.md#acquiredPlansCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans/{planAcquisitionId} |  |
| [**acquiredPlansDelete**](AcquiredPlansApi.md#acquiredPlansDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans/{planAcquisitionId} |  |
| [**acquiredPlansGet**](AcquiredPlansApi.md#acquiredPlansGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans/{planAcquisitionId} |  |
| [**acquiredPlansList**](AcquiredPlansApi.md#acquiredPlansList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans |  |


<a id="acquiredPlansCreate"></a>
# **acquiredPlansCreate**
> PlanAcquisition acquiredPlansCreate(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion, newAcquiredPlan)



Creates an acquired plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AcquiredPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AcquiredPlansApi apiInstance = new AcquiredPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String targetSubscriptionId = "targetSubscriptionId_example"; // String | The target subscription ID.
    String planAcquisitionId = "planAcquisitionId_example"; // String | The plan acquisition Identifier
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    PlanAcquisition newAcquiredPlan = new PlanAcquisition(); // PlanAcquisition | The new acquired plan.
    try {
      PlanAcquisition result = apiInstance.acquiredPlansCreate(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion, newAcquiredPlan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AcquiredPlansApi#acquiredPlansCreate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **targetSubscriptionId** | **String**| The target subscription ID. | |
| **planAcquisitionId** | **String**| The plan acquisition Identifier | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |
| **newAcquiredPlan** | [**PlanAcquisition**](PlanAcquisition.md)| The new acquired plan. | |

### Return type

[**PlanAcquisition**](PlanAcquisition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="acquiredPlansDelete"></a>
# **acquiredPlansDelete**
> acquiredPlansDelete(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion)



Deletes an acquired plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AcquiredPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AcquiredPlansApi apiInstance = new AcquiredPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String targetSubscriptionId = "targetSubscriptionId_example"; // String | The target subscription ID.
    String planAcquisitionId = "planAcquisitionId_example"; // String | The plan acquisition Identifier
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      apiInstance.acquiredPlansDelete(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AcquiredPlansApi#acquiredPlansDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **targetSubscriptionId** | **String**| The target subscription ID. | |
| **planAcquisitionId** | **String**| The plan acquisition Identifier | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

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
| **200** | OK |  -  |
| **204** | No Content |  -  |

<a id="acquiredPlansGet"></a>
# **acquiredPlansGet**
> PlanAcquisition acquiredPlansGet(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion)



Gets the specified plan acquired by a subscription consuming the offer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AcquiredPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AcquiredPlansApi apiInstance = new AcquiredPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String targetSubscriptionId = "targetSubscriptionId_example"; // String | The target subscription ID.
    String planAcquisitionId = "planAcquisitionId_example"; // String | The plan acquisition Identifier
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      PlanAcquisition result = apiInstance.acquiredPlansGet(subscriptionId, targetSubscriptionId, planAcquisitionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AcquiredPlansApi#acquiredPlansGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **targetSubscriptionId** | **String**| The target subscription ID. | |
| **planAcquisitionId** | **String**| The plan acquisition Identifier | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**PlanAcquisition**](PlanAcquisition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="acquiredPlansList"></a>
# **acquiredPlansList**
> PlanAcquisitionList acquiredPlansList(subscriptionId, targetSubscriptionId, apiVersion)



Get a collection of all acquired plans that subscription has access to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AcquiredPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AcquiredPlansApi apiInstance = new AcquiredPlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String targetSubscriptionId = "targetSubscriptionId_example"; // String | The target subscription ID.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      PlanAcquisitionList result = apiInstance.acquiredPlansList(subscriptionId, targetSubscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AcquiredPlansApi#acquiredPlansList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **targetSubscriptionId** | **String**| The target subscription ID. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**PlanAcquisitionList**](PlanAcquisitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

