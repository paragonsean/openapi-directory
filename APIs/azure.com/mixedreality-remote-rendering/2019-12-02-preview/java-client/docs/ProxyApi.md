# ProxyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**remoteRenderingAccountsListBySubscription_0**](ProxyApi.md#remoteRenderingAccountsListBySubscription_0) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/remoteRenderingAccounts |  |


<a id="remoteRenderingAccountsListBySubscription_0"></a>
# **remoteRenderingAccountsListBySubscription_0**
> RemoteRenderingAccountPage remoteRenderingAccountsListBySubscription_0(subscriptionId, apiVersion)



List Remote Rendering Accounts by Subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      RemoteRenderingAccountPage result = apiInstance.remoteRenderingAccountsListBySubscription_0(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#remoteRenderingAccountsListBySubscription_0");
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

