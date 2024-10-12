# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activityLogAlertsCreateOrUpdate**](DefaultApi.md#activityLogAlertsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts/{activityLogAlertName} |  |
| [**activityLogAlertsDelete**](DefaultApi.md#activityLogAlertsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts/{activityLogAlertName} |  |
| [**activityLogAlertsGet**](DefaultApi.md#activityLogAlertsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts/{activityLogAlertName} |  |
| [**activityLogAlertsListByResourceGroup**](DefaultApi.md#activityLogAlertsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts |  |
| [**activityLogAlertsListBySubscriptionId**](DefaultApi.md#activityLogAlertsListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/activityLogAlerts |  |
| [**activityLogAlertsUpdate**](DefaultApi.md#activityLogAlertsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/activityLogAlerts/{activityLogAlertName} |  |


<a id="activityLogAlertsCreateOrUpdate"></a>
# **activityLogAlertsCreateOrUpdate**
> ActivityLogAlertResource activityLogAlertsCreateOrUpdate(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, activityLogAlert)



Create a new activity log alert or update an existing one.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String activityLogAlertName = "activityLogAlertName_example"; // String | The name of the activity log alert.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    ActivityLogAlertResource activityLogAlert = new ActivityLogAlertResource(); // ActivityLogAlertResource | The activity log alert to create or use for the update.
    try {
      ActivityLogAlertResource result = apiInstance.activityLogAlertsCreateOrUpdate(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, activityLogAlert);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#activityLogAlertsCreateOrUpdate");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **activityLogAlertName** | **String**| The name of the activity log alert. | |
| **apiVersion** | **String**| Client Api Version. | |
| **activityLogAlert** | [**ActivityLogAlertResource**](ActivityLogAlertResource.md)| The activity log alert to create or use for the update. | |

### Return type

[**ActivityLogAlertResource**](ActivityLogAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An existing activity log alert was successfully updated. |  -  |
| **201** | A new activity log alert was successfully created. |  -  |
| **0** | An error occurred and the activity log alert could not be created or updated. |  -  |

<a id="activityLogAlertsDelete"></a>
# **activityLogAlertsDelete**
> activityLogAlertsDelete(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion)



Delete an activity log alert.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String activityLogAlertName = "activityLogAlertName_example"; // String | The name of the activity log alert.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.activityLogAlertsDelete(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#activityLogAlertsDelete");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **activityLogAlertName** | **String**| The name of the activity log alert. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The activity log alert was successfully deleted. |  -  |
| **204** | The activity log alert does not exist. It may have already been deleted. |  -  |
| **0** | An error occurred and the activity log alert could not be deleted. |  -  |

<a id="activityLogAlertsGet"></a>
# **activityLogAlertsGet**
> ActivityLogAlertResource activityLogAlertsGet(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion)



Get an activity log alert.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String activityLogAlertName = "activityLogAlertName_example"; // String | The name of the activity log alert.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      ActivityLogAlertResource result = apiInstance.activityLogAlertsGet(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#activityLogAlertsGet");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **activityLogAlertName** | **String**| The name of the activity log alert. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**ActivityLogAlertResource**](ActivityLogAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request succeeded. |  -  |
| **0** | An error occurred and the activity log alert could not be retrieved. |  -  |

<a id="activityLogAlertsListByResourceGroup"></a>
# **activityLogAlertsListByResourceGroup**
> ActivityLogAlertList activityLogAlertsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Get a list of all activity log alerts in a resource group.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      ActivityLogAlertList result = apiInstance.activityLogAlertsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#activityLogAlertsListByResourceGroup");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**ActivityLogAlertList**](ActivityLogAlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request succeeded. |  -  |
| **0** | An error occurred and the list of activity log alerts could not be retrieved. |  -  |

<a id="activityLogAlertsListBySubscriptionId"></a>
# **activityLogAlertsListBySubscriptionId**
> ActivityLogAlertList activityLogAlertsListBySubscriptionId(subscriptionId, apiVersion)



Get a list of all activity log alerts in a subscription.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      ActivityLogAlertList result = apiInstance.activityLogAlertsListBySubscriptionId(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#activityLogAlertsListBySubscriptionId");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**ActivityLogAlertList**](ActivityLogAlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request succeeded. |  -  |
| **0** | An error occurred and the list of activity log alerts could not be retrieved. |  -  |

<a id="activityLogAlertsUpdate"></a>
# **activityLogAlertsUpdate**
> ActivityLogAlertResource activityLogAlertsUpdate(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, activityLogAlertPatch)



Updates an existing ActivityLogAlertResource&#39;s tags. To update other fields use the CreateOrUpdate method.

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
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String activityLogAlertName = "activityLogAlertName_example"; // String | The name of the activity log alert.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    ActivityLogAlertResourcePatch activityLogAlertPatch = new ActivityLogAlertResourcePatch(); // ActivityLogAlertResourcePatch | Parameters supplied to the operation.
    try {
      ActivityLogAlertResource result = apiInstance.activityLogAlertsUpdate(subscriptionId, resourceGroupName, activityLogAlertName, apiVersion, activityLogAlertPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#activityLogAlertsUpdate");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **activityLogAlertName** | **String**| The name of the activity log alert. | |
| **apiVersion** | **String**| Client Api Version. | |
| **activityLogAlertPatch** | [**ActivityLogAlertResourcePatch**](ActivityLogAlertResourcePatch.md)| Parameters supplied to the operation. | |

### Return type

[**ActivityLogAlertResource**](ActivityLogAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An existing activity log alert was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

