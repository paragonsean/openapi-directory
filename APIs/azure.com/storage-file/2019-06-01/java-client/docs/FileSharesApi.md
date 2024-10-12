# FileSharesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileSharesCreate**](FileSharesApi.md#fileSharesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName} |  |
| [**fileSharesDelete**](FileSharesApi.md#fileSharesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName} |  |
| [**fileSharesGet**](FileSharesApi.md#fileSharesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName} |  |
| [**fileSharesList**](FileSharesApi.md#fileSharesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares |  |
| [**fileSharesUpdate**](FileSharesApi.md#fileSharesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName} |  |


<a id="fileSharesCreate"></a>
# **fileSharesCreate**
> FileShare fileSharesCreate(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, fileShare)



Creates a new share under the specified account as described by request body. The share resource includes metadata and properties for that share. It does not include a list of the files contained by the share. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String shareName = "shareName_example"; // String | The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    FileShare fileShare = new FileShare(); // FileShare | Properties of the file share to create.
    try {
      FileShare result = apiInstance.fileSharesCreate(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, fileShare);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#fileSharesCreate");
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
| **shareName** | **String**| The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **fileShare** | [**FileShare**](FileShare.md)| Properties of the file share to create. | |

### Return type

[**FileShare**](FileShare.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The Share is already created. |  -  |
| **201** | Created -- Create Share operation completed successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="fileSharesDelete"></a>
# **fileSharesDelete**
> fileSharesDelete(resourceGroupName, accountName, shareName, apiVersion, subscriptionId)



Deletes specified share under its account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String shareName = "shareName_example"; // String | The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.fileSharesDelete(resourceGroupName, accountName, shareName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#fileSharesDelete");
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
| **shareName** | **String**| The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **200** | OK -- Delete Share operation completed successfully. |  -  |
| **204** | No Content -- The Share not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="fileSharesGet"></a>
# **fileSharesGet**
> FileShare fileSharesGet(resourceGroupName, accountName, shareName, apiVersion, subscriptionId)



Gets properties of a specified share.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String shareName = "shareName_example"; // String | The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      FileShare result = apiInstance.fileSharesGet(resourceGroupName, accountName, shareName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#fileSharesGet");
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
| **shareName** | **String**| The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**FileShare**](FileShare.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Get Share operation completed successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="fileSharesList"></a>
# **fileSharesList**
> FileShareItems fileSharesList(resourceGroupName, accountName, apiVersion, subscriptionId, $maxpagesize, $filter)



Lists all shares.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $maxpagesize = "$maxpagesize_example"; // String | Optional. Specified maximum number of shares that can be included in the list.
    String $filter = "$filter_example"; // String | Optional. When specified, only share names starting with the filter will be listed.
    try {
      FileShareItems result = apiInstance.fileSharesList(resourceGroupName, accountName, apiVersion, subscriptionId, $maxpagesize, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#fileSharesList");
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
| **$maxpagesize** | **String**| Optional. Specified maximum number of shares that can be included in the list. | [optional] |
| **$filter** | **String**| Optional. When specified, only share names starting with the filter will be listed. | [optional] |

### Return type

[**FileShareItems**](FileShareItems.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- List Shares operation completed successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="fileSharesUpdate"></a>
# **fileSharesUpdate**
> FileShare fileSharesUpdate(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, fileShare)



Updates share properties as specified in request body. Properties not mentioned in the request will not be changed. Update fails if the specified share does not already exist. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileSharesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FileSharesApi apiInstance = new FileSharesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String shareName = "shareName_example"; // String | The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    FileShare fileShare = new FileShare(); // FileShare | Properties to update for the file share.
    try {
      FileShare result = apiInstance.fileSharesUpdate(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, fileShare);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileSharesApi#fileSharesUpdate");
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
| **shareName** | **String**| The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **fileShare** | [**FileShare**](FileShare.md)| Properties to update for the file share. | |

### Return type

[**FileShare**](FileShare.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Update Share operation completed successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

