# VirtualNetworkRulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualNetworkRulesCreateOrUpdate**](VirtualNetworkRulesApi.md#virtualNetworkRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules/{virtualNetworkRuleName} |  |
| [**virtualNetworkRulesDelete**](VirtualNetworkRulesApi.md#virtualNetworkRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules/{virtualNetworkRuleName} |  |
| [**virtualNetworkRulesGet**](VirtualNetworkRulesApi.md#virtualNetworkRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules/{virtualNetworkRuleName} |  |
| [**virtualNetworkRulesListByAccount**](VirtualNetworkRulesApi.md#virtualNetworkRulesListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules |  |
| [**virtualNetworkRulesUpdate**](VirtualNetworkRulesApi.md#virtualNetworkRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules/{virtualNetworkRuleName} |  |


<a id="virtualNetworkRulesCreateOrUpdate"></a>
# **virtualNetworkRulesCreateOrUpdate**
> VirtualNetworkRule virtualNetworkRulesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, parameters)



Creates or updates the specified virtual network rule. During update, the virtual network rule with the specified name will be replaced with this new virtual network rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkRulesApi apiInstance = new VirtualNetworkRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule to create or update.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    CreateOrUpdateVirtualNetworkRuleParameters parameters = new CreateOrUpdateVirtualNetworkRuleParameters(); // CreateOrUpdateVirtualNetworkRuleParameters | Parameters supplied to create or update the virtual network rule.
    try {
      VirtualNetworkRule result = apiInstance.virtualNetworkRulesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkRulesApi#virtualNetworkRulesCreateOrUpdate");
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
| **virtualNetworkRuleName** | **String**| The name of the virtual network rule to create or update. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**CreateOrUpdateVirtualNetworkRuleParameters**](CreateOrUpdateVirtualNetworkRuleParameters.md)| Parameters supplied to create or update the virtual network rule. | |

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the specified virtual network rule. |  -  |

<a id="virtualNetworkRulesDelete"></a>
# **virtualNetworkRulesDelete**
> virtualNetworkRulesDelete(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion)



Deletes the specified virtual network rule from the specified Data Lake Store account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkRulesApi apiInstance = new VirtualNetworkRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule to delete.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.virtualNetworkRulesDelete(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkRulesApi#virtualNetworkRulesDelete");
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
| **virtualNetworkRuleName** | **String**| The name of the virtual network rule to delete. | |
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
| **200** | Successfully deleted the specified virtual network rule. |  -  |
| **204** | The specified virtual network rule does not exist or was already deleted. |  -  |

<a id="virtualNetworkRulesGet"></a>
# **virtualNetworkRulesGet**
> VirtualNetworkRule virtualNetworkRulesGet(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion)



Gets the specified Data Lake Store virtual network rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkRulesApi apiInstance = new VirtualNetworkRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule to retrieve.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      VirtualNetworkRule result = apiInstance.virtualNetworkRulesGet(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkRulesApi#virtualNetworkRulesGet");
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
| **virtualNetworkRuleName** | **String**| The name of the virtual network rule to retrieve. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the virtual network rule. |  -  |

<a id="virtualNetworkRulesListByAccount"></a>
# **virtualNetworkRulesListByAccount**
> VirtualNetworkRuleListResult virtualNetworkRulesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Data Lake Store virtual network rules within the specified Data Lake Store account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkRulesApi apiInstance = new VirtualNetworkRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      VirtualNetworkRuleListResult result = apiInstance.virtualNetworkRulesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkRulesApi#virtualNetworkRulesListByAccount");
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

[**VirtualNetworkRuleListResult**](VirtualNetworkRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of virtual network rules. |  -  |

<a id="virtualNetworkRulesUpdate"></a>
# **virtualNetworkRulesUpdate**
> VirtualNetworkRule virtualNetworkRulesUpdate(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, parameters)



Updates the specified virtual network rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkRulesApi apiInstance = new VirtualNetworkRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule to update.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    UpdateVirtualNetworkRuleParameters parameters = new UpdateVirtualNetworkRuleParameters(); // UpdateVirtualNetworkRuleParameters | Parameters supplied to update the virtual network rule.
    try {
      VirtualNetworkRule result = apiInstance.virtualNetworkRulesUpdate(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkRulesApi#virtualNetworkRulesUpdate");
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
| **virtualNetworkRuleName** | **String**| The name of the virtual network rule to update. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**UpdateVirtualNetworkRuleParameters**](UpdateVirtualNetworkRuleParameters.md)| Parameters supplied to update the virtual network rule. | [optional] |

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the specified virtual network rule. |  -  |

