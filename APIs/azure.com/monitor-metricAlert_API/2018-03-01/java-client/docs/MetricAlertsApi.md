# MetricAlertsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricAlertsCreateOrUpdate**](MetricAlertsApi.md#metricAlertsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName} |  |
| [**metricAlertsDelete**](MetricAlertsApi.md#metricAlertsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName} |  |
| [**metricAlertsGet**](MetricAlertsApi.md#metricAlertsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName} |  |
| [**metricAlertsListByResourceGroup**](MetricAlertsApi.md#metricAlertsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts |  |
| [**metricAlertsListBySubscription**](MetricAlertsApi.md#metricAlertsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Insights/metricAlerts |  |
| [**metricAlertsUpdate**](MetricAlertsApi.md#metricAlertsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName} |  |


<a id="metricAlertsCreateOrUpdate"></a>
# **metricAlertsCreateOrUpdate**
> MetricAlertResource metricAlertsCreateOrUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters)



Create or update an metric alert definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricAlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricAlertsApi apiInstance = new MetricAlertsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    MetricAlertResource parameters = new MetricAlertResource(); // MetricAlertResource | The parameters of the rule to create or update.
    try {
      MetricAlertResource result = apiInstance.metricAlertsCreateOrUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricAlertsApi#metricAlertsCreateOrUpdate");
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
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**MetricAlertResource**](MetricAlertResource.md)| The parameters of the rule to create or update. | |

### Return type

[**MetricAlertResource**](MetricAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="metricAlertsDelete"></a>
# **metricAlertsDelete**
> metricAlertsDelete(subscriptionId, resourceGroupName, ruleName, apiVersion)



Delete an alert rule definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricAlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricAlertsApi apiInstance = new MetricAlertsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.metricAlertsDelete(subscriptionId, resourceGroupName, ruleName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricAlertsApi#metricAlertsDelete");
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
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client Api Version. | |

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
| **200** | Successful request to delete an metric alert rule |  -  |
| **204** | No content: the request was successful, but the response is empty |  -  |

<a id="metricAlertsGet"></a>
# **metricAlertsGet**
> MetricAlertResource metricAlertsGet(subscriptionId, resourceGroupName, ruleName, apiVersion)



Retrieve an alert rule definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricAlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricAlertsApi apiInstance = new MetricAlertsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      MetricAlertResource result = apiInstance.metricAlertsGet(subscriptionId, resourceGroupName, ruleName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricAlertsApi#metricAlertsGet");
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
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**MetricAlertResource**](MetricAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of metric alerts |  -  |
| **0** | BadRequest |  -  |

<a id="metricAlertsListByResourceGroup"></a>
# **metricAlertsListByResourceGroup**
> MetricAlertResourceCollection metricAlertsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Retrieve alert rule definitions in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricAlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricAlertsApi apiInstance = new MetricAlertsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      MetricAlertResourceCollection result = apiInstance.metricAlertsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricAlertsApi#metricAlertsListByResourceGroup");
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

[**MetricAlertResourceCollection**](MetricAlertResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of metric alerts |  -  |
| **0** | BadRequest |  -  |

<a id="metricAlertsListBySubscription"></a>
# **metricAlertsListBySubscription**
> MetricAlertResourceCollection metricAlertsListBySubscription(subscriptionId, apiVersion)



Retrieve alert rule definitions in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricAlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricAlertsApi apiInstance = new MetricAlertsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      MetricAlertResourceCollection result = apiInstance.metricAlertsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricAlertsApi#metricAlertsListBySubscription");
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

[**MetricAlertResourceCollection**](MetricAlertResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of metric alerts |  -  |
| **0** | BadRequest |  -  |

<a id="metricAlertsUpdate"></a>
# **metricAlertsUpdate**
> MetricAlertResource metricAlertsUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters)



Update an metric alert definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricAlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricAlertsApi apiInstance = new MetricAlertsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    MetricAlertResourcePatch parameters = new MetricAlertResourcePatch(); // MetricAlertResourcePatch | The parameters of the rule to update.
    try {
      MetricAlertResource result = apiInstance.metricAlertsUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricAlertsApi#metricAlertsUpdate");
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
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**MetricAlertResourcePatch**](MetricAlertResourcePatch.md)| The parameters of the rule to update. | |

### Return type

[**MetricAlertResource**](MetricAlertResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

