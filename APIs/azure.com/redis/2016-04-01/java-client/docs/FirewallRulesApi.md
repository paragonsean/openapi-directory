# FirewallRulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**firewallRulesList_0**](FirewallRulesApi.md#firewallRulesList_0) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules |  |
| [**redisFirewallRuleCreateOrUpdate_0**](FirewallRulesApi.md#redisFirewallRuleCreateOrUpdate_0) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules/{ruleName} |  |
| [**redisFirewallRuleDelete_0**](FirewallRulesApi.md#redisFirewallRuleDelete_0) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules/{ruleName} |  |
| [**redisFirewallRuleGet_0**](FirewallRulesApi.md#redisFirewallRuleGet_0) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules/{ruleName} |  |


<a id="firewallRulesList_0"></a>
# **firewallRulesList_0**
> RedisFirewallRuleListResult firewallRulesList_0(apiVersion, subscriptionId, resourceGroupName, cacheName)



Gets all firewall rules in the specified redis cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FirewallRulesApi apiInstance = new FirewallRulesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String cacheName = "cacheName_example"; // String | The name of the Redis cache.
    try {
      RedisFirewallRuleListResult result = apiInstance.firewallRulesList_0(apiVersion, subscriptionId, resourceGroupName, cacheName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallRulesApi#firewallRulesList_0");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **cacheName** | **String**| The name of the Redis cache. | |

### Return type

[**RedisFirewallRuleListResult**](RedisFirewallRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully got the current rules |  -  |

<a id="redisFirewallRuleCreateOrUpdate_0"></a>
# **redisFirewallRuleCreateOrUpdate_0**
> RedisFirewallRule redisFirewallRuleCreateOrUpdate_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, parameters)



Create or update a redis cache firewall rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FirewallRulesApi apiInstance = new FirewallRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String cacheName = "cacheName_example"; // String | The name of the Redis cache.
    String ruleName = "ruleName_example"; // String | The name of the firewall rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RedisFirewallRule parameters = new RedisFirewallRule(); // RedisFirewallRule | Parameters supplied to the create or update redis firewall rule operation.
    try {
      RedisFirewallRule result = apiInstance.redisFirewallRuleCreateOrUpdate_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallRulesApi#redisFirewallRuleCreateOrUpdate_0");
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
| **cacheName** | **String**| The name of the Redis cache. | |
| **ruleName** | **String**| The name of the firewall rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**RedisFirewallRule**](RedisFirewallRule.md)| Parameters supplied to the create or update redis firewall rule operation. | |

### Return type

[**RedisFirewallRule**](RedisFirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Resource was successfully updated |  -  |
| **201** | Resource was successfully created |  -  |

<a id="redisFirewallRuleDelete_0"></a>
# **redisFirewallRuleDelete_0**
> redisFirewallRuleDelete_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId)



Deletes a single firewall rule in a specified redis cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FirewallRulesApi apiInstance = new FirewallRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String cacheName = "cacheName_example"; // String | The name of the Redis cache.
    String ruleName = "ruleName_example"; // String | The name of the firewall rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.redisFirewallRuleDelete_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallRulesApi#redisFirewallRuleDelete_0");
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
| **cacheName** | **String**| The name of the Redis cache. | |
| **ruleName** | **String**| The name of the firewall rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Successfully deleted the rule |  -  |
| **204** | Successfully deleted the rule |  -  |

<a id="redisFirewallRuleGet_0"></a>
# **redisFirewallRuleGet_0**
> RedisFirewallRule redisFirewallRuleGet_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId)



Gets a single firewall rule in a specified redis cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FirewallRulesApi apiInstance = new FirewallRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String cacheName = "cacheName_example"; // String | The name of the Redis cache.
    String ruleName = "ruleName_example"; // String | The name of the firewall rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      RedisFirewallRule result = apiInstance.redisFirewallRuleGet_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallRulesApi#redisFirewallRuleGet_0");
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
| **cacheName** | **String**| The name of the Redis cache. | |
| **ruleName** | **String**| The name of the firewall rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**RedisFirewallRule**](RedisFirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully found the rule |  -  |

