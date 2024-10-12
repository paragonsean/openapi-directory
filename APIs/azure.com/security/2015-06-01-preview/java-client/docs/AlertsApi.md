# AlertsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**alertsGetResourceGroupLevelAlerts**](AlertsApi.md#alertsGetResourceGroupLevelAlerts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/alerts/{alertName} |  |
| [**alertsGetSubscriptionLevelAlert**](AlertsApi.md#alertsGetSubscriptionLevelAlert) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/alerts/{alertName} |  |
| [**alertsList**](AlertsApi.md#alertsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/alerts |  |
| [**alertsListByResourceGroup**](AlertsApi.md#alertsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/alerts |  |
| [**alertsListResourceGroupLevelAlertsByRegion**](AlertsApi.md#alertsListResourceGroupLevelAlertsByRegion) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/alerts |  |
| [**alertsListSubscriptionLevelAlertsByRegion**](AlertsApi.md#alertsListSubscriptionLevelAlertsByRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/alerts |  |
| [**alertsUpdateResourceGroupLevelAlertState**](AlertsApi.md#alertsUpdateResourceGroupLevelAlertState) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/alerts/{alertName}/{alertUpdateActionType} |  |
| [**alertsUpdateSubscriptionLevelAlertState**](AlertsApi.md#alertsUpdateSubscriptionLevelAlertState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/alerts/{alertName}/{alertUpdateActionType} |  |


<a id="alertsGetResourceGroupLevelAlerts"></a>
# **alertsGetResourceGroupLevelAlerts**
> Alert alertsGetResourceGroupLevelAlerts(apiVersion, subscriptionId, ascLocation, alertName, resourceGroupName)



Get an alert that is associated a resource group or a resource in a resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String alertName = "alertName_example"; // String | Name of the alert object
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    try {
      Alert result = apiInstance.alertsGetResourceGroupLevelAlerts(apiVersion, subscriptionId, ascLocation, alertName, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsGetResourceGroupLevelAlerts");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **alertName** | **String**| Name of the alert object | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsGetSubscriptionLevelAlert"></a>
# **alertsGetSubscriptionLevelAlert**
> Alert alertsGetSubscriptionLevelAlert(apiVersion, subscriptionId, ascLocation, alertName)



Get an alert that is associated with a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String alertName = "alertName_example"; // String | Name of the alert object
    try {
      Alert result = apiInstance.alertsGetSubscriptionLevelAlert(apiVersion, subscriptionId, ascLocation, alertName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsGetSubscriptionLevelAlert");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **alertName** | **String**| Name of the alert object | |

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsList"></a>
# **alertsList**
> AlertList alertsList(apiVersion, subscriptionId, $filter, $select, $expand)



List all the alerts that are associated with the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String $filter = "$filter_example"; // String | OData filter. Optional.
    String $select = "$select_example"; // String | OData select. Optional.
    String $expand = "$expand_example"; // String | OData expand. Optional.
    try {
      AlertList result = apiInstance.alertsList(apiVersion, subscriptionId, $filter, $select, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsList");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$select** | **String**| OData select. Optional. | [optional] |
| **$expand** | **String**| OData expand. Optional. | [optional] |

### Return type

[**AlertList**](AlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsListByResourceGroup"></a>
# **alertsListByResourceGroup**
> AlertList alertsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, $filter, $select, $expand)



List all the alerts that are associated with the resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    String $select = "$select_example"; // String | OData select. Optional.
    String $expand = "$expand_example"; // String | OData expand. Optional.
    try {
      AlertList result = apiInstance.alertsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, $filter, $select, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsListByResourceGroup");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$select** | **String**| OData select. Optional. | [optional] |
| **$expand** | **String**| OData expand. Optional. | [optional] |

### Return type

[**AlertList**](AlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsListResourceGroupLevelAlertsByRegion"></a>
# **alertsListResourceGroupLevelAlertsByRegion**
> AlertList alertsListResourceGroupLevelAlertsByRegion(apiVersion, subscriptionId, ascLocation, resourceGroupName, $filter, $select, $expand)



List all the alerts that are associated with the resource group that are stored in a specific location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String $filter = "$filter_example"; // String | OData filter. Optional.
    String $select = "$select_example"; // String | OData select. Optional.
    String $expand = "$expand_example"; // String | OData expand. Optional.
    try {
      AlertList result = apiInstance.alertsListResourceGroupLevelAlertsByRegion(apiVersion, subscriptionId, ascLocation, resourceGroupName, $filter, $select, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsListResourceGroupLevelAlertsByRegion");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$select** | **String**| OData select. Optional. | [optional] |
| **$expand** | **String**| OData expand. Optional. | [optional] |

### Return type

[**AlertList**](AlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsListSubscriptionLevelAlertsByRegion"></a>
# **alertsListSubscriptionLevelAlertsByRegion**
> AlertList alertsListSubscriptionLevelAlertsByRegion(apiVersion, subscriptionId, ascLocation, $filter, $select, $expand)



List all the alerts that are associated with the subscription that are stored in a specific location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String $filter = "$filter_example"; // String | OData filter. Optional.
    String $select = "$select_example"; // String | OData select. Optional.
    String $expand = "$expand_example"; // String | OData expand. Optional.
    try {
      AlertList result = apiInstance.alertsListSubscriptionLevelAlertsByRegion(apiVersion, subscriptionId, ascLocation, $filter, $select, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsListSubscriptionLevelAlertsByRegion");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **$filter** | **String**| OData filter. Optional. | [optional] |
| **$select** | **String**| OData select. Optional. | [optional] |
| **$expand** | **String**| OData expand. Optional. | [optional] |

### Return type

[**AlertList**](AlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsUpdateResourceGroupLevelAlertState"></a>
# **alertsUpdateResourceGroupLevelAlertState**
> alertsUpdateResourceGroupLevelAlertState(apiVersion, subscriptionId, ascLocation, alertName, alertUpdateActionType, resourceGroupName)



Update the alert&#39;s state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String alertName = "alertName_example"; // String | Name of the alert object
    String alertUpdateActionType = "Dismiss"; // String | Type of the action to do on the alert
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    try {
      apiInstance.alertsUpdateResourceGroupLevelAlertState(apiVersion, subscriptionId, ascLocation, alertName, alertUpdateActionType, resourceGroupName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUpdateResourceGroupLevelAlertState");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **alertName** | **String**| Name of the alert object | |
| **alertUpdateActionType** | **String**| Type of the action to do on the alert | [enum: Dismiss, Reactivate] |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsUpdateSubscriptionLevelAlertState"></a>
# **alertsUpdateSubscriptionLevelAlertState**
> alertsUpdateSubscriptionLevelAlertState(apiVersion, subscriptionId, ascLocation, alertName, alertUpdateActionType)



Update the alert&#39;s state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertsApi apiInstance = new AlertsApi(defaultClient);
    String apiVersion = "2015-06-01-preview"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String alertName = "alertName_example"; // String | Name of the alert object
    String alertUpdateActionType = "Dismiss"; // String | Type of the action to do on the alert
    try {
      apiInstance.alertsUpdateSubscriptionLevelAlertState(apiVersion, subscriptionId, ascLocation, alertName, alertUpdateActionType);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertsApi#alertsUpdateSubscriptionLevelAlertState");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2015-06-01-preview] |
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **alertName** | **String**| Name of the alert object | |
| **alertUpdateActionType** | **String**| Type of the action to do on the alert | [enum: Dismiss, Reactivate] |

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
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

