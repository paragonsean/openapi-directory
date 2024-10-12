# DashboardApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dashboardsCreateOrUpdate**](DashboardApi.md#dashboardsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName} |  |
| [**dashboardsDelete**](DashboardApi.md#dashboardsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName} |  |
| [**dashboardsGet**](DashboardApi.md#dashboardsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName} |  |
| [**dashboardsListByResourceGroup**](DashboardApi.md#dashboardsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards |  |
| [**dashboardsListBySubscription**](DashboardApi.md#dashboardsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Portal/dashboards |  |
| [**dashboardsUpdate**](DashboardApi.md#dashboardsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName} |  |


<a id="dashboardsCreateOrUpdate"></a>
# **dashboardsCreateOrUpdate**
> Dashboard dashboardsCreateOrUpdate(subscriptionId, resourceGroupName, dashboardName, apiVersion, dashboard)



Creates or updates a Dashboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DashboardApi apiInstance = new DashboardApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String dashboardName = "dashboardName_example"; // String | The name of the dashboard.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    Dashboard dashboard = new Dashboard(); // Dashboard | The parameters required to create or update a dashboard.
    try {
      Dashboard result = apiInstance.dashboardsCreateOrUpdate(subscriptionId, resourceGroupName, dashboardName, apiVersion, dashboard);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardApi#dashboardsCreateOrUpdate");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **dashboardName** | **String**| The name of the dashboard. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **dashboard** | [**Dashboard**](Dashboard.md)| The parameters required to create or update a dashboard. | |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Resource already exists. |  -  |
| **201** | Created response definition. Resource has been created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dashboardsDelete"></a>
# **dashboardsDelete**
> dashboardsDelete(subscriptionId, resourceGroupName, dashboardName, apiVersion)



Deletes the Dashboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DashboardApi apiInstance = new DashboardApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String dashboardName = "dashboardName_example"; // String | The name of the dashboard.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      apiInstance.dashboardsDelete(subscriptionId, resourceGroupName, dashboardName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardApi#dashboardsDelete");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **dashboardName** | **String**| The name of the dashboard. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

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
| **200** | OK response definition. |  -  |
| **204** | OK resource was not found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dashboardsGet"></a>
# **dashboardsGet**
> Dashboard dashboardsGet(subscriptionId, resourceGroupName, dashboardName, apiVersion)



Gets the Dashboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DashboardApi apiInstance = new DashboardApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String dashboardName = "dashboardName_example"; // String | The name of the dashboard.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      Dashboard result = apiInstance.dashboardsGet(subscriptionId, resourceGroupName, dashboardName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardApi#dashboardsGet");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **dashboardName** | **String**| The name of the dashboard. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dashboardsListByResourceGroup"></a>
# **dashboardsListByResourceGroup**
> DashboardListResult dashboardsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Gets all the Dashboards within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DashboardApi apiInstance = new DashboardApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      DashboardListResult result = apiInstance.dashboardsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardApi#dashboardsListByResourceGroup");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

[**DashboardListResult**](DashboardListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of Dashboards. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dashboardsListBySubscription"></a>
# **dashboardsListBySubscription**
> DashboardListResult dashboardsListBySubscription(subscriptionId, apiVersion)



Gets all the dashboards within a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DashboardApi apiInstance = new DashboardApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    try {
      DashboardListResult result = apiInstance.dashboardsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardApi#dashboardsListBySubscription");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |

### Return type

[**DashboardListResult**](DashboardListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of dashboards. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dashboardsUpdate"></a>
# **dashboardsUpdate**
> Dashboard dashboardsUpdate(subscriptionId, resourceGroupName, dashboardName, apiVersion, dashboard)



Updates an existing Dashboard.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DashboardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DashboardApi apiInstance = new DashboardApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String dashboardName = "dashboardName_example"; // String | The name of the dashboard.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    PatchableDashboard dashboard = new PatchableDashboard(); // PatchableDashboard | The updatable fields of a Dashboard.
    try {
      Dashboard result = apiInstance.dashboardsUpdate(subscriptionId, resourceGroupName, dashboardName, apiVersion, dashboard);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DashboardApi#dashboardsUpdate");
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
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **dashboardName** | **String**| The name of the dashboard. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **dashboard** | [**PatchableDashboard**](PatchableDashboard.md)| The updatable fields of a Dashboard. | |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

