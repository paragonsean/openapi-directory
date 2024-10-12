# KeyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**remoteRenderingAccountsGetKeys**](KeyApi.md#remoteRenderingAccountsGetKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName}/keys |  |
| [**remoteRenderingAccountsRegenerateKeys**](KeyApi.md#remoteRenderingAccountsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName}/keys |  |


<a id="remoteRenderingAccountsGetKeys"></a>
# **remoteRenderingAccountsGetKeys**
> RemoteRenderingAccountsGetKeys200Response remoteRenderingAccountsGetKeys(subscriptionId, resourceGroupName, accountName, apiVersion)



Get Both of the 2 Keys of a Remote Rendering Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      RemoteRenderingAccountsGetKeys200Response result = apiInstance.remoteRenderingAccountsGetKeys(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#remoteRenderingAccountsGetKeys");
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

[**RemoteRenderingAccountsGetKeys200Response**](RemoteRenderingAccountsGetKeys200Response.md)

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

<a id="remoteRenderingAccountsRegenerateKeys"></a>
# **remoteRenderingAccountsRegenerateKeys**
> RemoteRenderingAccountsGetKeys200Response remoteRenderingAccountsRegenerateKeys(subscriptionId, resourceGroupName, accountName, apiVersion, regenerate)



Regenerate specified Key of a Remote Rendering Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
    String accountName = "accountName_example"; // String | Name of an Mixed Reality Account.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    RemoteRenderingAccountsRegenerateKeysRequest regenerate = new RemoteRenderingAccountsRegenerateKeysRequest(); // RemoteRenderingAccountsRegenerateKeysRequest | Required information for key regeneration.
    try {
      RemoteRenderingAccountsGetKeys200Response result = apiInstance.remoteRenderingAccountsRegenerateKeys(subscriptionId, resourceGroupName, accountName, apiVersion, regenerate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#remoteRenderingAccountsRegenerateKeys");
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
| **regenerate** | [**RemoteRenderingAccountsRegenerateKeysRequest**](RemoteRenderingAccountsRegenerateKeysRequest.md)| Required information for key regeneration. | |

### Return type

[**RemoteRenderingAccountsGetKeys200Response**](RemoteRenderingAccountsGetKeys200Response.md)

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

