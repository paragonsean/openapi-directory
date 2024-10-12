# ResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**remoteRenderingAccountsCreate**](ResourceApi.md#remoteRenderingAccountsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName} |  |
| [**remoteRenderingAccountsDelete**](ResourceApi.md#remoteRenderingAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName} |  |
| [**remoteRenderingAccountsGet**](ResourceApi.md#remoteRenderingAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName} |  |
| [**remoteRenderingAccountsListByResourceGroup**](ResourceApi.md#remoteRenderingAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts |  |
| [**remoteRenderingAccountsListBySubscription**](ResourceApi.md#remoteRenderingAccountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/remoteRenderingAccounts |  |
| [**remoteRenderingAccountsUpdate**](ResourceApi.md#remoteRenderingAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName} |  |


<a id="remoteRenderingAccountsCreate"></a>
# **remoteRenderingAccountsCreate**
> RemoteRenderingAccount remoteRenderingAccountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, remoteRenderingAccount)



Creating or Updating a Remote Rendering Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    RemoteRenderingAccount remoteRenderingAccount = new RemoteRenderingAccount(); // RemoteRenderingAccount | Remote Rendering Account parameter.
    try {
      RemoteRenderingAccount result = apiInstance.remoteRenderingAccountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, remoteRenderingAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#remoteRenderingAccountsCreate");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Name of an Mixed Reality Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **remoteRenderingAccount** | [**RemoteRenderingAccount**](RemoteRenderingAccount.md)| Remote Rendering Account parameter. | |

### Return type

[**RemoteRenderingAccount**](RemoteRenderingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remoteRenderingAccountsDelete"></a>
# **remoteRenderingAccountsDelete**
> remoteRenderingAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)



Delete a Remote Rendering Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.remoteRenderingAccountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#remoteRenderingAccountsDelete");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Name of an Mixed Reality Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

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
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remoteRenderingAccountsGet"></a>
# **remoteRenderingAccountsGet**
> RemoteRenderingAccount remoteRenderingAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



Retrieve a Remote Rendering Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      RemoteRenderingAccount result = apiInstance.remoteRenderingAccountsGet(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#remoteRenderingAccountsGet");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Name of an Mixed Reality Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**RemoteRenderingAccount**](RemoteRenderingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remoteRenderingAccountsListByResourceGroup"></a>
# **remoteRenderingAccountsListByResourceGroup**
> RemoteRenderingAccountPage remoteRenderingAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



List Resources by Resource Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      RemoteRenderingAccountPage result = apiInstance.remoteRenderingAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#remoteRenderingAccountsListByResourceGroup");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**RemoteRenderingAccountPage**](RemoteRenderingAccountPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remoteRenderingAccountsListBySubscription"></a>
# **remoteRenderingAccountsListBySubscription**
> RemoteRenderingAccountPage remoteRenderingAccountsListBySubscription(subscriptionId, apiVersion)



List Remote Rendering Accounts by Subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      RemoteRenderingAccountPage result = apiInstance.remoteRenderingAccountsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#remoteRenderingAccountsListBySubscription");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**RemoteRenderingAccountPage**](RemoteRenderingAccountPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="remoteRenderingAccountsUpdate"></a>
# **remoteRenderingAccountsUpdate**
> RemoteRenderingAccount remoteRenderingAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, remoteRenderingAccount)



Updating a Remote Rendering Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ResourceApi apiInstance = new ResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    RemoteRenderingAccount remoteRenderingAccount = new RemoteRenderingAccount(); // RemoteRenderingAccount | Remote Rendering Account parameter.
    try {
      RemoteRenderingAccount result = apiInstance.remoteRenderingAccountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, remoteRenderingAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourceApi#remoteRenderingAccountsUpdate");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure resource group. | |
| **accountName** | **String**| Name of an Mixed Reality Account. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **remoteRenderingAccount** | [**RemoteRenderingAccount**](RemoteRenderingAccount.md)| Remote Rendering Account parameter. | |

### Return type

[**RemoteRenderingAccount**](RemoteRenderingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

