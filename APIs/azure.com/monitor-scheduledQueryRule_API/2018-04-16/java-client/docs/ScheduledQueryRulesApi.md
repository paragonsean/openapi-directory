# ScheduledQueryRulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scheduledQueryRulesCreateOrUpdate**](ScheduledQueryRulesApi.md#scheduledQueryRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules/{ruleName} |  |
| [**scheduledQueryRulesDelete**](ScheduledQueryRulesApi.md#scheduledQueryRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules/{ruleName} |  |
| [**scheduledQueryRulesGet**](ScheduledQueryRulesApi.md#scheduledQueryRulesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules/{ruleName} |  |
| [**scheduledQueryRulesListByResourceGroup**](ScheduledQueryRulesApi.md#scheduledQueryRulesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules |  |
| [**scheduledQueryRulesListBySubscription**](ScheduledQueryRulesApi.md#scheduledQueryRulesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/scheduledQueryRules |  |
| [**scheduledQueryRulesUpdate**](ScheduledQueryRulesApi.md#scheduledQueryRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/scheduledQueryRules/{ruleName} |  |


<a id="scheduledQueryRulesCreateOrUpdate"></a>
# **scheduledQueryRulesCreateOrUpdate**
> LogSearchRuleResource scheduledQueryRulesCreateOrUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters)



Creates or updates an log search rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledQueryRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScheduledQueryRulesApi apiInstance = new ScheduledQueryRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    LogSearchRuleResource parameters = new LogSearchRuleResource(); // LogSearchRuleResource | The parameters of the rule to create or update.
    try {
      LogSearchRuleResource result = apiInstance.scheduledQueryRulesCreateOrUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledQueryRulesApi#scheduledQueryRulesCreateOrUpdate");
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
| **parameters** | [**LogSearchRuleResource**](LogSearchRuleResource.md)| The parameters of the rule to create or update. | |

### Return type

[**LogSearchRuleResource**](LogSearchRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to update an Log Search rule |  -  |
| **201** | Created alert rule |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="scheduledQueryRulesDelete"></a>
# **scheduledQueryRulesDelete**
> scheduledQueryRulesDelete(resourceGroupName, ruleName, apiVersion, subscriptionId)



Deletes a Log Search rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledQueryRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScheduledQueryRulesApi apiInstance = new ScheduledQueryRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      apiInstance.scheduledQueryRulesDelete(resourceGroupName, ruleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledQueryRulesApi#scheduledQueryRulesDelete");
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
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |

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
| **200** | Successful request to delete a  Log Search rule |  -  |
| **204** | No Content. Resource not found |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="scheduledQueryRulesGet"></a>
# **scheduledQueryRulesGet**
> LogSearchRuleResource scheduledQueryRulesGet(resourceGroupName, ruleName, apiVersion, subscriptionId)



Gets an Log Search rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledQueryRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScheduledQueryRulesApi apiInstance = new ScheduledQueryRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      LogSearchRuleResource result = apiInstance.scheduledQueryRulesGet(resourceGroupName, ruleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledQueryRulesApi#scheduledQueryRulesGet");
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
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |

### Return type

[**LogSearchRuleResource**](LogSearchRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get a Log Search rule |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="scheduledQueryRulesListByResourceGroup"></a>
# **scheduledQueryRulesListByResourceGroup**
> LogSearchRuleResourceCollection scheduledQueryRulesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter)



List the Log Search rules within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledQueryRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScheduledQueryRulesApi apiInstance = new ScheduledQueryRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx
    try {
      LogSearchRuleResourceCollection result = apiInstance.scheduledQueryRulesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledQueryRulesApi#scheduledQueryRulesListByResourceGroup");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **$filter** | **String**| The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx | [optional] |

### Return type

[**LogSearchRuleResourceCollection**](LogSearchRuleResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of alert rules |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="scheduledQueryRulesListBySubscription"></a>
# **scheduledQueryRulesListBySubscription**
> LogSearchRuleResourceCollection scheduledQueryRulesListBySubscription(apiVersion, subscriptionId, $filter)



List the Log Search rules within a subscription group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledQueryRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScheduledQueryRulesApi apiInstance = new ScheduledQueryRulesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx
    try {
      LogSearchRuleResourceCollection result = apiInstance.scheduledQueryRulesListBySubscription(apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledQueryRulesApi#scheduledQueryRulesListBySubscription");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **$filter** | **String**| The filter to apply on the operation. For more information please see https://msdn.microsoft.com/en-us/library/azure/dn931934.aspx | [optional] |

### Return type

[**LogSearchRuleResourceCollection**](LogSearchRuleResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of alert rules |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="scheduledQueryRulesUpdate"></a>
# **scheduledQueryRulesUpdate**
> LogSearchRuleResource scheduledQueryRulesUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters)



Update log search Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduledQueryRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ScheduledQueryRulesApi apiInstance = new ScheduledQueryRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    LogSearchRuleResourcePatch parameters = new LogSearchRuleResourcePatch(); // LogSearchRuleResourcePatch | The parameters of the rule to update.
    try {
      LogSearchRuleResource result = apiInstance.scheduledQueryRulesUpdate(subscriptionId, resourceGroupName, ruleName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduledQueryRulesApi#scheduledQueryRulesUpdate");
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
| **parameters** | [**LogSearchRuleResourcePatch**](LogSearchRuleResourcePatch.md)| The parameters of the rule to update. | |

### Return type

[**LogSearchRuleResource**](LogSearchRuleResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to update an Log Search rule |  -  |
| **0** | Error response describing why the operation failed. |  -  |

