# FirewallRulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**firewallRulesCreateOrUpdate**](FirewallRulesApi.md#firewallRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} |  |
| [**firewallRulesDelete**](FirewallRulesApi.md#firewallRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} |  |
| [**firewallRulesGet**](FirewallRulesApi.md#firewallRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} |  |
| [**firewallRulesListByAccount**](FirewallRulesApi.md#firewallRulesListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules |  |
| [**firewallRulesUpdate**](FirewallRulesApi.md#firewallRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} |  |


<a id="firewallRulesCreateOrUpdate"></a>
# **firewallRulesCreateOrUpdate**
> FirewallRule firewallRulesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, parameters)



Creates or updates the specified firewall rule. During update, the firewall rule with the specified name will be replaced with this new firewall rule.

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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to create or update.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    CreateOrUpdateFirewallRuleParameters parameters = new CreateOrUpdateFirewallRuleParameters(); // CreateOrUpdateFirewallRuleParameters | Parameters supplied to create or update the firewall rule.
    try {
      FirewallRule result = apiInstance.firewallRulesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallRulesApi#firewallRulesCreateOrUpdate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **firewallRuleName** | **String**| The name of the firewall rule to create or update. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**CreateOrUpdateFirewallRuleParameters**](CreateOrUpdateFirewallRuleParameters.md)| Parameters supplied to create or update the firewall rule. | |

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the specified firewall rule. |  -  |

<a id="firewallRulesDelete"></a>
# **firewallRulesDelete**
> firewallRulesDelete(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion)



Deletes the specified firewall rule from the specified Data Lake Store account.

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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to delete.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.firewallRulesDelete(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallRulesApi#firewallRulesDelete");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **firewallRuleName** | **String**| The name of the firewall rule to delete. | |
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
| **200** | Successfully deleted the specified firewall rule. |  -  |
| **204** | The specified firewall rule does not exist or was already deleted. |  -  |

<a id="firewallRulesGet"></a>
# **firewallRulesGet**
> FirewallRule firewallRulesGet(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion)



Gets the specified Data Lake Store firewall rule.

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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to retrieve.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      FirewallRule result = apiInstance.firewallRulesGet(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallRulesApi#firewallRulesGet");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **firewallRuleName** | **String**| The name of the firewall rule to retrieve. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the firewall rule. |  -  |

<a id="firewallRulesListByAccount"></a>
# **firewallRulesListByAccount**
> FirewallRuleListResult firewallRulesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Data Lake Store firewall rules within the specified Data Lake Store account.

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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      FirewallRuleListResult result = apiInstance.firewallRulesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallRulesApi#firewallRulesListByAccount");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**FirewallRuleListResult**](FirewallRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of firewall rules. |  -  |

<a id="firewallRulesUpdate"></a>
# **firewallRulesUpdate**
> FirewallRule firewallRulesUpdate(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, parameters)



Updates the specified firewall rule.

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
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to update.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    UpdateFirewallRuleParameters parameters = new UpdateFirewallRuleParameters(); // UpdateFirewallRuleParameters | Parameters supplied to update the firewall rule.
    try {
      FirewallRule result = apiInstance.firewallRulesUpdate(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallRulesApi#firewallRulesUpdate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **firewallRuleName** | **String**| The name of the firewall rule to update. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**UpdateFirewallRuleParameters**](UpdateFirewallRuleParameters.md)| Parameters supplied to update the firewall rule. | [optional] |

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the specified firewall rule. |  -  |

