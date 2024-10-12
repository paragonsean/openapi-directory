# FileServiceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileServicesGetServiceProperties**](FileServiceApi.md#fileServicesGetServiceProperties) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/{FileServicesName} |  |
| [**fileServicesList**](FileServiceApi.md#fileServicesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices |  |
| [**fileServicesSetServiceProperties**](FileServiceApi.md#fileServicesSetServiceProperties) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/{FileServicesName} |  |


<a id="fileServicesGetServiceProperties"></a>
# **fileServicesGetServiceProperties**
> FileServiceProperties fileServicesGetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, fileServicesName)



Gets the properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String fileServicesName = "default"; // String | The name of the file Service within the specified storage account. File Service Name must be \"default\"
    try {
      FileServiceProperties result = apiInstance.fileServicesGetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, fileServicesName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServicesGetServiceProperties");
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
| **fileServicesName** | **String**| The name of the file Service within the specified storage account. File Service Name must be \&quot;default\&quot; | [enum: default] |

### Return type

[**FileServiceProperties**](FileServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- returned the properties of a storage account’s File service. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="fileServicesList"></a>
# **fileServicesList**
> FileServiceItems fileServicesList(resourceGroupName, accountName, apiVersion, subscriptionId)



List all file services in storage accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      FileServiceItems result = apiInstance.fileServicesList(resourceGroupName, accountName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServicesList");
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

### Return type

[**FileServiceItems**](FileServiceItems.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- List file services operation completed successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="fileServicesSetServiceProperties"></a>
# **fileServicesSetServiceProperties**
> FileServiceProperties fileServicesSetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, fileServicesName, parameters)



Sets the properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileServiceApi apiInstance = new FileServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String fileServicesName = "default"; // String | The name of the file Service within the specified storage account. File Service Name must be \"default\"
    FileServiceProperties parameters = new FileServiceProperties(); // FileServiceProperties | The properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules.
    try {
      FileServiceProperties result = apiInstance.fileServicesSetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, fileServicesName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileServiceApi#fileServicesSetServiceProperties");
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
| **fileServicesName** | **String**| The name of the file Service within the specified storage account. File Service Name must be \&quot;default\&quot; | [enum: default] |
| **parameters** | [**FileServiceProperties**](FileServiceProperties.md)| The properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules. | |

### Return type

[**FileServiceProperties**](FileServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Sets The properties of a storage account’s File service successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

