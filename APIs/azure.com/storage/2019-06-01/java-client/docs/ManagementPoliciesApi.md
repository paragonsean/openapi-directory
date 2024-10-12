# ManagementPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managementPoliciesCreateOrUpdate**](ManagementPoliciesApi.md#managementPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName} |  |
| [**managementPoliciesDelete**](ManagementPoliciesApi.md#managementPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName} |  |
| [**managementPoliciesGet**](ManagementPoliciesApi.md#managementPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName} |  |


<a id="managementPoliciesCreateOrUpdate"></a>
# **managementPoliciesCreateOrUpdate**
> ManagementPolicy managementPoliciesCreateOrUpdate(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName, properties)



Sets the managementpolicy to the specified storage account.

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
    ManagementPolicy properties = new ManagementPolicy(); // ManagementPolicy | The ManagementPolicy set to a storage account.
    try {
      ManagementPolicy result = apiInstance.managementPoliciesCreateOrUpdate(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementPoliciesApi#managementPoliciesCreateOrUpdate");
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
| **properties** | [**ManagementPolicy**](ManagementPolicy.md)| The ManagementPolicy set to a storage account. | |

### Return type

[**ManagementPolicy**](ManagementPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Put managementpolicy successfully. |  -  |

<a id="managementPoliciesDelete"></a>
# **managementPoliciesDelete**
> managementPoliciesDelete(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName)



Deletes the managementpolicy associated with the specified storage account.

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
      apiInstance.managementPoliciesDelete(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementPoliciesApi#managementPoliciesDelete");
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
| **200** | OK -- Delete the managementpolicy successfully. |  -  |
| **204** | No Content -- The managementpolicy does not exist. |  -  |

<a id="managementPoliciesGet"></a>
# **managementPoliciesGet**
> ManagementPolicy managementPoliciesGet(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName)



Gets the managementpolicy associated with the specified storage account.

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
      ManagementPolicy result = apiInstance.managementPoliciesGet(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagementPoliciesApi#managementPoliciesGet");
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

[**ManagementPolicy**](ManagementPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Get the managementpolicy successfully. |  -  |

