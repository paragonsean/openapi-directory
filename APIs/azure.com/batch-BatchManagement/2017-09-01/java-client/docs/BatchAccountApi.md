# BatchAccountApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchAccountCreate**](BatchAccountApi.md#batchAccountCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName} |  |
| [**batchAccountDelete**](BatchAccountApi.md#batchAccountDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName} |  |
| [**batchAccountGet**](BatchAccountApi.md#batchAccountGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName} |  |
| [**batchAccountGetKeys**](BatchAccountApi.md#batchAccountGetKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/listKeys | Gets the account keys for the specified Batch account. |
| [**batchAccountList**](BatchAccountApi.md#batchAccountList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Batch/batchAccounts |  |
| [**batchAccountListByResourceGroup**](BatchAccountApi.md#batchAccountListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts |  |
| [**batchAccountRegenerateKey**](BatchAccountApi.md#batchAccountRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/regenerateKeys |  |
| [**batchAccountSynchronizeAutoStorageKeys**](BatchAccountApi.md#batchAccountSynchronizeAutoStorageKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/syncAutoStorageKeys |  |
| [**batchAccountUpdate**](BatchAccountApi.md#batchAccountUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName} |  |


<a id="batchAccountCreate"></a>
# **batchAccountCreate**
> BatchAccount batchAccountCreate(resourceGroupName, accountName, apiVersion, subscriptionId, parameters)



Creates a new Batch account with the specified parameters. Existing accounts cannot be updated with this API and should instead be updated with the Update Batch Account API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BatchAccountApi apiInstance = new BatchAccountApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    BatchAccountCreateParameters parameters = new BatchAccountCreateParameters(); // BatchAccountCreateParameters | Additional parameters for account creation.
    try {
      BatchAccount result = apiInstance.batchAccountCreate(resourceGroupName, accountName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchAccountApi#batchAccountCreate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: http://accountname.region.batch.azure.com/. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**BatchAccountCreateParameters**](BatchAccountCreateParameters.md)| Additional parameters for account creation. | |

### Return type

[**BatchAccount**](BatchAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the Batch account entity. |  -  |
| **202** | The operation will be completed asynchronously. |  * Retry-After - Suggested delay to check the status of the asynchronous operation. The value is an integer that represents the seconds. <br>  * Location - The URL of the resource used to check the status of the asynchronous operation. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="batchAccountDelete"></a>
# **batchAccountDelete**
> batchAccountDelete(resourceGroupName, accountName, apiVersion, subscriptionId)



Deletes the specified Batch account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BatchAccountApi apiInstance = new BatchAccountApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      apiInstance.batchAccountDelete(resourceGroupName, accountName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchAccountApi#batchAccountDelete");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

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
| **200** | The operation was successful. |  -  |
| **202** | The operation will be completed asynchronously. |  * Retry-After - Suggested delay to check the status of the asynchronous operation. The value is an integer that represents the seconds. <br>  * Location - The URL of the resource used to check the status of the asynchronous operation. <br>  |
| **204** | NoContent -- account does not exist in the subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="batchAccountGet"></a>
# **batchAccountGet**
> BatchAccount batchAccountGet(resourceGroupName, accountName, apiVersion, subscriptionId)



Gets information about the specified Batch account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BatchAccountApi apiInstance = new BatchAccountApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      BatchAccount result = apiInstance.batchAccountGet(resourceGroupName, accountName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchAccountApi#batchAccountGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**BatchAccount**](BatchAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the Batch account entity. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="batchAccountGetKeys"></a>
# **batchAccountGetKeys**
> BatchAccountKeys batchAccountGetKeys(resourceGroupName, accountName, apiVersion, subscriptionId)

Gets the account keys for the specified Batch account.

This operation applies only to Batch accounts created with a poolAllocationMode of &#39;BatchService&#39;. If the Batch account was created with a poolAllocationMode of &#39;UserSubscription&#39;, clients cannot use access to keys to authenticate, and must use Azure Active Directory instead. In this case, getting the keys will fail.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BatchAccountApi apiInstance = new BatchAccountApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      BatchAccountKeys result = apiInstance.batchAccountGetKeys(resourceGroupName, accountName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchAccountApi#batchAccountGetKeys");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**BatchAccountKeys**](BatchAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the keys of the Batch account. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="batchAccountList"></a>
# **batchAccountList**
> BatchAccountListResult batchAccountList(apiVersion, subscriptionId)



Gets information about the Batch accounts associated with the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BatchAccountApi apiInstance = new BatchAccountApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      BatchAccountListResult result = apiInstance.batchAccountList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchAccountApi#batchAccountList");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**BatchAccountListResult**](BatchAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains a list of Batch account entities associated with the subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="batchAccountListByResourceGroup"></a>
# **batchAccountListByResourceGroup**
> BatchAccountListResult batchAccountListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets information about the Batch accounts associated with the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BatchAccountApi apiInstance = new BatchAccountApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      BatchAccountListResult result = apiInstance.batchAccountListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchAccountApi#batchAccountListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

### Return type

[**BatchAccountListResult**](BatchAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains a list of Batch account entities associated with the resource group. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="batchAccountRegenerateKey"></a>
# **batchAccountRegenerateKey**
> BatchAccountKeys batchAccountRegenerateKey(resourceGroupName, accountName, apiVersion, subscriptionId, parameters)



Regenerates the specified account key for the Batch account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BatchAccountApi apiInstance = new BatchAccountApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    BatchAccountRegenerateKeyParameters parameters = new BatchAccountRegenerateKeyParameters(); // BatchAccountRegenerateKeyParameters | The type of key to regenerate.
    try {
      BatchAccountKeys result = apiInstance.batchAccountRegenerateKey(resourceGroupName, accountName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchAccountApi#batchAccountRegenerateKey");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**BatchAccountRegenerateKeyParameters**](BatchAccountRegenerateKeyParameters.md)| The type of key to regenerate. | |

### Return type

[**BatchAccountKeys**](BatchAccountKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the Batch account keys. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="batchAccountSynchronizeAutoStorageKeys"></a>
# **batchAccountSynchronizeAutoStorageKeys**
> batchAccountSynchronizeAutoStorageKeys(resourceGroupName, accountName, apiVersion, subscriptionId)



Synchronizes access keys for the auto-storage account configured for the specified Batch account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BatchAccountApi apiInstance = new BatchAccountApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    try {
      apiInstance.batchAccountSynchronizeAutoStorageKeys(resourceGroupName, accountName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchAccountApi#batchAccountSynchronizeAutoStorageKeys");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |

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
| **204** | The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="batchAccountUpdate"></a>
# **batchAccountUpdate**
> BatchAccount batchAccountUpdate(resourceGroupName, accountName, apiVersion, subscriptionId, parameters)



Updates the properties of an existing Batch account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchAccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BatchAccountApi apiInstance = new BatchAccountApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
    String accountName = "accountName_example"; // String | The name of the Batch account.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    BatchAccountUpdateParameters parameters = new BatchAccountUpdateParameters(); // BatchAccountUpdateParameters | Additional parameters for account update.
    try {
      BatchAccount result = apiInstance.batchAccountUpdate(resourceGroupName, accountName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchAccountApi#batchAccountUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | |
| **accountName** | **String**| The name of the Batch account. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | |
| **parameters** | [**BatchAccountUpdateParameters**](BatchAccountUpdateParameters.md)| Additional parameters for account update. | |

### Return type

[**BatchAccount**](BatchAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation was successful. The response contains the Batch account entity. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

