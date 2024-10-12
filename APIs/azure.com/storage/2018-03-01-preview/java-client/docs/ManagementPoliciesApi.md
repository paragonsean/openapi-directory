# ManagementPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageAccountsCreateOrUpdateManagementPolicies**](ManagementPoliciesApi.md#storageAccountsCreateOrUpdateManagementPolicies) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName} |  |
| [**storageAccountsDeleteManagementPolicies**](ManagementPoliciesApi.md#storageAccountsDeleteManagementPolicies) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName} |  |
| [**storageAccountsGetManagementPolicies**](ManagementPoliciesApi.md#storageAccountsGetManagementPolicies) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName} |  |


<a id="storageAccountsCreateOrUpdateManagementPolicies"></a>
# **storageAccountsCreateOrUpdateManagementPolicies**
> StorageAccountManagementPolicies storageAccountsCreateOrUpdateManagementPolicies(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName, properties)



Sets the data policy rules associated with the specified storage account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementPoliciesApi apiInstance = new ManagementPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String managementPolicyName = "default"; // String | The name of the Storage Account Management Policy. It should always be 'default'
    ManagementPoliciesRulesSetParameter properties = new ManagementPoliciesRulesSetParameter(); // ManagementPoliciesRulesSetParameter | The data policy rules to set to a storage account.
    try {
      StorageAccountManagementPolicies result = apiInstance.storageAccountsCreateOrUpdateManagementPolicies(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementPoliciesApi#storageAccountsCreateOrUpdateManagementPolicies");
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
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **accountName** | **String**| The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **managementPolicyName** | **String**| The name of the Storage Account Management Policy. It should always be &#39;default&#39; | [enum: default] |
| **properties** | [**ManagementPoliciesRulesSetParameter**](ManagementPoliciesRulesSetParameter.md)| The data policy rules to set to a storage account. | |

### Return type

[**StorageAccountManagementPolicies**](StorageAccountManagementPolicies.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Get management policies successfully. |  -  |

<a id="storageAccountsDeleteManagementPolicies"></a>
# **storageAccountsDeleteManagementPolicies**
> storageAccountsDeleteManagementPolicies(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName)



Deletes the data policy rules associated with the specified storage account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementPoliciesApi apiInstance = new ManagementPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String managementPolicyName = "default"; // String | The name of the Storage Account Management Policy. It should always be 'default'
    try {
      apiInstance.storageAccountsDeleteManagementPolicies(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementPoliciesApi#storageAccountsDeleteManagementPolicies");
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
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **accountName** | **String**| The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **managementPolicyName** | **String**| The name of the Storage Account Management Policy. It should always be &#39;default&#39; | [enum: default] |

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
| **200** | OK -- Delete management policies successfully. |  -  |
| **204** | No Content -- The management policies does not exist. |  -  |

<a id="storageAccountsGetManagementPolicies"></a>
# **storageAccountsGetManagementPolicies**
> StorageAccountManagementPolicies storageAccountsGetManagementPolicies(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName)



Gets the data policy rules associated with the specified storage account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagementPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagementPoliciesApi apiInstance = new ManagementPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String managementPolicyName = "default"; // String | The name of the Storage Account Management Policy. It should always be 'default'
    try {
      StorageAccountManagementPolicies result = apiInstance.storageAccountsGetManagementPolicies(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementPoliciesApi#storageAccountsGetManagementPolicies");
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
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **accountName** | **String**| The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **managementPolicyName** | **String**| The name of the Storage Account Management Policy. It should always be &#39;default&#39; | [enum: default] |

### Return type

[**StorageAccountManagementPolicies**](StorageAccountManagementPolicies.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Get management policies successfully. |  -  |

