# RouteFilterRulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**routeFilterRulesCreateOrUpdate**](RouteFilterRulesApi.md#routeFilterRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName} |  |
| [**routeFilterRulesDelete**](RouteFilterRulesApi.md#routeFilterRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName} |  |
| [**routeFilterRulesGet**](RouteFilterRulesApi.md#routeFilterRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName} |  |
| [**routeFilterRulesListByRouteFilter**](RouteFilterRulesApi.md#routeFilterRulesListByRouteFilter) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules |  |
| [**routeFilterRulesUpdate**](RouteFilterRulesApi.md#routeFilterRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/routeFilters/{routeFilterName}/routeFilterRules/{ruleName} |  |


<a id="routeFilterRulesCreateOrUpdate"></a>
# **routeFilterRulesCreateOrUpdate**
> RouteFilterRule routeFilterRulesCreateOrUpdate(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, routeFilterRuleParameters)



Creates or updates a route in the specified route filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteFilterRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RouteFilterRulesApi apiInstance = new RouteFilterRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
    String ruleName = "ruleName_example"; // String | The name of the route filter rule.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RouteFilterRule routeFilterRuleParameters = new RouteFilterRule(); // RouteFilterRule | Parameters supplied to the create or update route filter rule operation.
    try {
      RouteFilterRule result = apiInstance.routeFilterRulesCreateOrUpdate(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, routeFilterRuleParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteFilterRulesApi#routeFilterRulesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **routeFilterName** | **String**| The name of the route filter. | |
| **ruleName** | **String**| The name of the route filter rule. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **routeFilterRuleParameters** | [**RouteFilterRule**](RouteFilterRule.md)| Parameters supplied to the create or update route filter rule operation. | |

### Return type

[**RouteFilterRule**](RouteFilterRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting Route Filter Rule resource. |  -  |
| **201** | Create successful. The operation returns the resulting Route Filter Rule resource. |  -  |

<a id="routeFilterRulesDelete"></a>
# **routeFilterRulesDelete**
> routeFilterRulesDelete(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId)



Deletes the specified rule from a route filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteFilterRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RouteFilterRulesApi apiInstance = new RouteFilterRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.routeFilterRulesDelete(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteFilterRulesApi#routeFilterRulesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **routeFilterName** | **String**| The name of the route filter. | |
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Accepted. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Rule was deleted or not found. |  -  |

<a id="routeFilterRulesGet"></a>
# **routeFilterRulesGet**
> RouteFilterRule routeFilterRulesGet(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId)



Gets the specified rule from a route filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteFilterRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RouteFilterRulesApi apiInstance = new RouteFilterRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      RouteFilterRule result = apiInstance.routeFilterRulesGet(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteFilterRulesApi#routeFilterRulesGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **routeFilterName** | **String**| The name of the route filter. | |
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**RouteFilterRule**](RouteFilterRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting Route Filter Rule resource. |  -  |

<a id="routeFilterRulesListByRouteFilter"></a>
# **routeFilterRulesListByRouteFilter**
> RouteFilterRuleListResult routeFilterRulesListByRouteFilter(resourceGroupName, routeFilterName, apiVersion, subscriptionId)



Gets all RouteFilterRules in a route filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteFilterRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RouteFilterRulesApi apiInstance = new RouteFilterRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      RouteFilterRuleListResult result = apiInstance.routeFilterRulesListByRouteFilter(resourceGroupName, routeFilterName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteFilterRulesApi#routeFilterRulesListByRouteFilter");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **routeFilterName** | **String**| The name of the route filter. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**RouteFilterRuleListResult**](RouteFilterRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of Route Filter Rule resources. |  -  |

<a id="routeFilterRulesUpdate"></a>
# **routeFilterRulesUpdate**
> RouteFilterRule routeFilterRulesUpdate(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, routeFilterRuleParameters)



Updates a route in the specified route filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RouteFilterRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RouteFilterRulesApi apiInstance = new RouteFilterRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String routeFilterName = "routeFilterName_example"; // String | The name of the route filter.
    String ruleName = "ruleName_example"; // String | The name of the route filter rule.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    PatchRouteFilterRule routeFilterRuleParameters = new PatchRouteFilterRule(); // PatchRouteFilterRule | Parameters supplied to the update route filter rule operation.
    try {
      RouteFilterRule result = apiInstance.routeFilterRulesUpdate(resourceGroupName, routeFilterName, ruleName, apiVersion, subscriptionId, routeFilterRuleParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RouteFilterRulesApi#routeFilterRulesUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **routeFilterName** | **String**| The name of the route filter. | |
| **ruleName** | **String**| The name of the route filter rule. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **routeFilterRuleParameters** | [**PatchRouteFilterRule**](PatchRouteFilterRule.md)| Parameters supplied to the update route filter rule operation. | |

### Return type

[**RouteFilterRule**](RouteFilterRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting Route Filter Rule resource. |  -  |

