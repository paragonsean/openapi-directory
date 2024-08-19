# StorageAccountCredentialsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageAccountCredentialsCreateOrUpdate**](StorageAccountCredentialsApi.md#storageAccountCredentialsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials/{credentialName} |  |
| [**storageAccountCredentialsDelete**](StorageAccountCredentialsApi.md#storageAccountCredentialsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials/{credentialName} |  |
| [**storageAccountCredentialsGet**](StorageAccountCredentialsApi.md#storageAccountCredentialsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials/{credentialName} |  |
| [**storageAccountCredentialsListByManager**](StorageAccountCredentialsApi.md#storageAccountCredentialsListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials |  |


<a id="storageAccountCredentialsCreateOrUpdate"></a>
# **storageAccountCredentialsCreateOrUpdate**
> StorageAccountCredential storageAccountCredentialsCreateOrUpdate(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion, storageAccount)



Creates or updates the storage account credential

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageAccountCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageAccountCredentialsApi apiInstance = new StorageAccountCredentialsApi(defaultClient);
    String credentialName = "credentialName_example"; // String | The credential name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    StorageAccountCredential storageAccount = new StorageAccountCredential(); // StorageAccountCredential | The storage account credential to be added or updated.
    try {
      StorageAccountCredential result = apiInstance.storageAccountCredentialsCreateOrUpdate(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion, storageAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageAccountCredentialsApi#storageAccountCredentialsCreateOrUpdate");
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
| **credentialName** | **String**| The credential name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |
| **storageAccount** | [**StorageAccountCredential**](StorageAccountCredential.md)| The storage account credential to be added or updated. | |

### Return type

[**StorageAccountCredential**](StorageAccountCredential.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the storage account credential. |  -  |
| **202** | Accepted the request to create or update the storage account credential. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="storageAccountCredentialsDelete"></a>
# **storageAccountCredentialsDelete**
> storageAccountCredentialsDelete(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the storage account credential

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageAccountCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageAccountCredentialsApi apiInstance = new StorageAccountCredentialsApi(defaultClient);
    String credentialName = "credentialName_example"; // String | The name of the storage account credential.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      apiInstance.storageAccountCredentialsDelete(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageAccountCredentialsApi#storageAccountCredentialsDelete");
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
| **credentialName** | **String**| The name of the storage account credential. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

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
| **202** | Accepted the request to delete the storage account credential. |  -  |
| **204** | Successfully deleted the storage account credential. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="storageAccountCredentialsGet"></a>
# **storageAccountCredentialsGet**
> StorageAccountCredential storageAccountCredentialsGet(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified storage account credential name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageAccountCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageAccountCredentialsApi apiInstance = new StorageAccountCredentialsApi(defaultClient);
    String credentialName = "credentialName_example"; // String | The name of storage account credential to be fetched.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      StorageAccountCredential result = apiInstance.storageAccountCredentialsGet(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageAccountCredentialsApi#storageAccountCredentialsGet");
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
| **credentialName** | **String**| The name of storage account credential to be fetched. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**StorageAccountCredential**](StorageAccountCredential.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The storage account credential. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="storageAccountCredentialsListByManager"></a>
# **storageAccountCredentialsListByManager**
> StorageAccountCredentialList storageAccountCredentialsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the storage account credentials in a manager.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageAccountCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageAccountCredentialsApi apiInstance = new StorageAccountCredentialsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      StorageAccountCredentialList result = apiInstance.storageAccountCredentialsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageAccountCredentialsApi#storageAccountCredentialsListByManager");
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
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**StorageAccountCredentialList**](StorageAccountCredentialList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of storage account credentials. |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

