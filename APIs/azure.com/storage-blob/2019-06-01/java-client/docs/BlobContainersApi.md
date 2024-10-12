# BlobContainersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blobContainersClearLegalHold**](BlobContainersApi.md#blobContainersClearLegalHold) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/clearLegalHold |  |
| [**blobContainersCreate**](BlobContainersApi.md#blobContainersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName} |  |
| [**blobContainersCreateOrUpdateImmutabilityPolicy**](BlobContainersApi.md#blobContainersCreateOrUpdateImmutabilityPolicy) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/{immutabilityPolicyName} |  |
| [**blobContainersDelete**](BlobContainersApi.md#blobContainersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName} |  |
| [**blobContainersDeleteImmutabilityPolicy**](BlobContainersApi.md#blobContainersDeleteImmutabilityPolicy) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/{immutabilityPolicyName} |  |
| [**blobContainersExtendImmutabilityPolicy**](BlobContainersApi.md#blobContainersExtendImmutabilityPolicy) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/default/extend |  |
| [**blobContainersGet**](BlobContainersApi.md#blobContainersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName} |  |
| [**blobContainersGetImmutabilityPolicy**](BlobContainersApi.md#blobContainersGetImmutabilityPolicy) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/{immutabilityPolicyName} |  |
| [**blobContainersLease**](BlobContainersApi.md#blobContainersLease) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/lease |  |
| [**blobContainersList**](BlobContainersApi.md#blobContainersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers |  |
| [**blobContainersLockImmutabilityPolicy**](BlobContainersApi.md#blobContainersLockImmutabilityPolicy) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/default/lock |  |
| [**blobContainersSetLegalHold**](BlobContainersApi.md#blobContainersSetLegalHold) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/setLegalHold |  |
| [**blobContainersUpdate**](BlobContainersApi.md#blobContainersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName} |  |


<a id="blobContainersClearLegalHold"></a>
# **blobContainersClearLegalHold**
> LegalHold blobContainersClearLegalHold(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, legalHold)



Clears legal hold tags. Clearing the same or non-existent tag results in an idempotent operation. ClearLegalHold clears out only the specified tags in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    LegalHold legalHold = new LegalHold(); // LegalHold | The LegalHold property that will be clear from a blob container.
    try {
      LegalHold result = apiInstance.blobContainersClearLegalHold(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, legalHold);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersClearLegalHold");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **legalHold** | [**LegalHold**](LegalHold.md)| The LegalHold property that will be clear from a blob container. | |

### Return type

[**LegalHold**](LegalHold.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Clear legal hold tags for Container completed successfully. |  -  |

<a id="blobContainersCreate"></a>
# **blobContainersCreate**
> BlobContainer blobContainersCreate(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, blobContainer)



Creates a new container under the specified account as described by request body. The container resource includes metadata and properties for that container. It does not include a list of the blobs contained by the container. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    BlobContainer blobContainer = new BlobContainer(); // BlobContainer | Properties of the blob container to create.
    try {
      BlobContainer result = apiInstance.blobContainersCreate(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, blobContainer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersCreate");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **blobContainer** | [**BlobContainer**](BlobContainer.md)| Properties of the blob container to create. | |

### Return type

[**BlobContainer**](BlobContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- The Container is already created. |  -  |
| **201** | Created -- Create Container operation completed successfully. |  -  |

<a id="blobContainersCreateOrUpdateImmutabilityPolicy"></a>
# **blobContainersCreateOrUpdateImmutabilityPolicy**
> ImmutabilityPolicy blobContainersCreateOrUpdateImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, ifMatch, parameters)



Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String immutabilityPolicyName = "default"; // String | The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be 'default'
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    ImmutabilityPolicy parameters = new ImmutabilityPolicy(); // ImmutabilityPolicy | The ImmutabilityPolicy Properties that will be created or updated to a blob container.
    try {
      ImmutabilityPolicy result = apiInstance.blobContainersCreateOrUpdateImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, ifMatch, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersCreateOrUpdateImmutabilityPolicy");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **immutabilityPolicyName** | **String**| The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be &#39;default&#39; | [enum: default] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | [optional] |
| **parameters** | [**ImmutabilityPolicy**](ImmutabilityPolicy.md)| The ImmutabilityPolicy Properties that will be created or updated to a blob container. | [optional] |

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Creates or updates container ImmutabilityPolicy operation completed successfully. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |

<a id="blobContainersDelete"></a>
# **blobContainersDelete**
> blobContainersDelete(resourceGroupName, accountName, containerName, apiVersion, subscriptionId)



Deletes specified container under its account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.blobContainersDelete(resourceGroupName, accountName, containerName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersDelete");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **200** | OK -- Delete Container operation completed successfully. |  -  |
| **204** | No Content -- The Container not exist. |  -  |

<a id="blobContainersDeleteImmutabilityPolicy"></a>
# **blobContainersDeleteImmutabilityPolicy**
> ImmutabilityPolicy blobContainersDeleteImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, ifMatch)



Aborts an unlocked immutability policy. The response of delete has immutabilityPeriodSinceCreationInDays set to 0. ETag in If-Match is required for this operation. Deleting a locked immutability policy is not allowed, only way is to delete the container after deleting all blobs inside the container.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String immutabilityPolicyName = "default"; // String | The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be 'default'
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    try {
      ImmutabilityPolicy result = apiInstance.blobContainersDeleteImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersDeleteImmutabilityPolicy");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **immutabilityPolicyName** | **String**| The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be &#39;default&#39; | [enum: default] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | |

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Deletes container ImmutabilityPolicy operation completed successfully. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |

<a id="blobContainersExtendImmutabilityPolicy"></a>
# **blobContainersExtendImmutabilityPolicy**
> ImmutabilityPolicy blobContainersExtendImmutabilityPolicy(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, ifMatch, parameters)



Extends the immutabilityPeriodSinceCreationInDays of a locked immutabilityPolicy. The only action allowed on a Locked policy will be this action. ETag in If-Match is required for this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    ImmutabilityPolicy parameters = new ImmutabilityPolicy(); // ImmutabilityPolicy | The ImmutabilityPolicy Properties that will be extended for a blob container.
    try {
      ImmutabilityPolicy result = apiInstance.blobContainersExtendImmutabilityPolicy(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, ifMatch, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersExtendImmutabilityPolicy");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | |
| **parameters** | [**ImmutabilityPolicy**](ImmutabilityPolicy.md)| The ImmutabilityPolicy Properties that will be extended for a blob container. | [optional] |

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Extends container ImmutabilityPolicy operation completed successfully.. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |

<a id="blobContainersGet"></a>
# **blobContainersGet**
> BlobContainer blobContainersGet(resourceGroupName, accountName, containerName, apiVersion, subscriptionId)



Gets properties of a specified container. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      BlobContainer result = apiInstance.blobContainersGet(resourceGroupName, accountName, containerName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersGet");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**BlobContainer**](BlobContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Get Container operation completed successfully. |  -  |

<a id="blobContainersGetImmutabilityPolicy"></a>
# **blobContainersGetImmutabilityPolicy**
> ImmutabilityPolicy blobContainersGetImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, ifMatch)



Gets the existing immutability policy along with the corresponding ETag in response headers and body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String immutabilityPolicyName = "default"; // String | The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be 'default'
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    try {
      ImmutabilityPolicy result = apiInstance.blobContainersGetImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersGetImmutabilityPolicy");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **immutabilityPolicyName** | **String**| The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be &#39;default&#39; | [enum: default] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | [optional] |

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Gets container ImmutabilityPolicy operation completed successfully. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |

<a id="blobContainersLease"></a>
# **blobContainersLease**
> LeaseContainerResponse blobContainersLease(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, parameters)



The Lease Container operation establishes and manages a lock on a container for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    LeaseContainerRequest parameters = new LeaseContainerRequest(); // LeaseContainerRequest | Lease Container request body.
    try {
      LeaseContainerResponse result = apiInstance.blobContainersLease(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersLease");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**LeaseContainerRequest**](LeaseContainerRequest.md)| Lease Container request body. | [optional] |

### Return type

[**LeaseContainerResponse**](LeaseContainerResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Lease Container operation completed successfully. |  -  |

<a id="blobContainersList"></a>
# **blobContainersList**
> ListContainerItems blobContainersList(resourceGroupName, accountName, apiVersion, subscriptionId, $maxpagesize, $filter)



Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $maxpagesize = "$maxpagesize_example"; // String | Optional. Specified maximum number of containers that can be included in the list.
    String $filter = "$filter_example"; // String | Optional. When specified, only container names starting with the filter will be listed.
    try {
      ListContainerItems result = apiInstance.blobContainersList(resourceGroupName, accountName, apiVersion, subscriptionId, $maxpagesize, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersList");
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
| **$maxpagesize** | **String**| Optional. Specified maximum number of containers that can be included in the list. | [optional] |
| **$filter** | **String**| Optional. When specified, only container names starting with the filter will be listed. | [optional] |

### Return type

[**ListContainerItems**](ListContainerItems.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- List Container operation completed successfully. |  -  |

<a id="blobContainersLockImmutabilityPolicy"></a>
# **blobContainersLockImmutabilityPolicy**
> ImmutabilityPolicy blobContainersLockImmutabilityPolicy(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, ifMatch)



Sets the ImmutabilityPolicy to Locked state. The only action allowed on a Locked policy is ExtendImmutabilityPolicy action. ETag in If-Match is required for this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    try {
      ImmutabilityPolicy result = apiInstance.blobContainersLockImmutabilityPolicy(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersLockImmutabilityPolicy");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | |

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Locks container ImmutabilityPolicy operation completed successfully. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Match or If-None-Match headers. <br>  |

<a id="blobContainersSetLegalHold"></a>
# **blobContainersSetLegalHold**
> LegalHold blobContainersSetLegalHold(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, legalHold)



Sets legal hold tags. Setting the same tag results in an idempotent operation. SetLegalHold follows an append pattern and does not clear out the existing tags that are not specified in the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    LegalHold legalHold = new LegalHold(); // LegalHold | The LegalHold property that will be set to a blob container.
    try {
      LegalHold result = apiInstance.blobContainersSetLegalHold(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, legalHold);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersSetLegalHold");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **legalHold** | [**LegalHold**](LegalHold.md)| The LegalHold property that will be set to a blob container. | |

### Return type

[**LegalHold**](LegalHold.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Set legal hold tags for Container completed successfully. |  -  |

<a id="blobContainersUpdate"></a>
# **blobContainersUpdate**
> BlobContainer blobContainersUpdate(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, blobContainer)



Updates container properties as specified in request body. Properties not mentioned in the request will be unchanged. Update fails if the specified container doesn&#39;t already exist. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlobContainersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlobContainersApi apiInstance = new BlobContainersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    String containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    BlobContainer blobContainer = new BlobContainer(); // BlobContainer | Properties to update for the blob container.
    try {
      BlobContainer result = apiInstance.blobContainersUpdate(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, blobContainer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlobContainersApi#blobContainersUpdate");
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
| **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **blobContainer** | [**BlobContainer**](BlobContainer.md)| Properties to update for the blob container. | |

### Return type

[**BlobContainer**](BlobContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Update Container operation completed successfully. |  -  |

