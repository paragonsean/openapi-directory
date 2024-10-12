# BlobServiceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blobServicesGetServiceProperties**](BlobServiceApi.md#blobServicesGetServiceProperties) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/{BlobServicesName} |  |
| [**blobServicesList**](BlobServiceApi.md#blobServicesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices |  |
| [**blobServicesSetServiceProperties**](BlobServiceApi.md#blobServicesSetServiceProperties) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/{BlobServicesName} |  |


<a id="blobServicesGetServiceProperties"></a>
# **blobServicesGetServiceProperties**
> BlobServiceProperties blobServicesGetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, blobServicesName)



Gets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobServiceApi apiInstance = new BlobServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String blobServicesName = "default"; // String | The name of the blob Service within the specified storage account. Blob Service Name must be 'default'
    try {
      BlobServiceProperties result = apiInstance.blobServicesGetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, blobServicesName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobServiceApi#blobServicesGetServiceProperties");
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
| **blobServicesName** | **String**| The name of the blob Service within the specified storage account. Blob Service Name must be &#39;default&#39; | [enum: default] |

### Return type

[**BlobServiceProperties**](BlobServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- returned the properties of a storage account’s Blob service. |  -  |

<a id="blobServicesList"></a>
# **blobServicesList**
> BlobServiceItems blobServicesList(resourceGroupName, accountName, apiVersion, subscriptionId)



List blob services of storage account. It returns a collection of one object named default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobServiceApi apiInstance = new BlobServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      BlobServiceItems result = apiInstance.blobServicesList(resourceGroupName, accountName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobServiceApi#blobServicesList");
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

[**BlobServiceItems**](BlobServiceItems.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- List blob services operation completed successfully. |  -  |

<a id="blobServicesSetServiceProperties"></a>
# **blobServicesSetServiceProperties**
> BlobServiceProperties blobServicesSetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, blobServicesName, parameters)



Sets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobServiceApi apiInstance = new BlobServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String blobServicesName = "default"; // String | The name of the blob Service within the specified storage account. Blob Service Name must be 'default'
    BlobServiceProperties parameters = new BlobServiceProperties(); // BlobServiceProperties | The properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.
    try {
      BlobServiceProperties result = apiInstance.blobServicesSetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, blobServicesName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobServiceApi#blobServicesSetServiceProperties");
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
| **blobServicesName** | **String**| The name of the blob Service within the specified storage account. Blob Service Name must be &#39;default&#39; | [enum: default] |
| **parameters** | [**BlobServiceProperties**](BlobServiceProperties.md)| The properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules. | |

### Return type

[**BlobServiceProperties**](BlobServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Sets The properties of a storage account’s Blob service successfully. |  -  |

