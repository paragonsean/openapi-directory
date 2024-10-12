# NetAppAccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsCreateOrUpdate**](NetAppAccountsApi.md#accountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName} |  |
| [**accountsDelete**](NetAppAccountsApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName} |  |
| [**accountsGet**](NetAppAccountsApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName} |  |
| [**accountsList**](NetAppAccountsApi.md#accountsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts |  |
| [**accountsUpdate**](NetAppAccountsApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName} |  |


<a id="accountsCreateOrUpdate"></a>
# **accountsCreateOrUpdate**
> NetAppAccount accountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, body)



Create or update a NetApp account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetAppAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetAppAccountsApi apiInstance = new NetAppAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    NetAppAccount body = new NetAppAccount(); // NetAppAccount | NetApp Account object supplied in the body of the operation.
    try {
      NetAppAccount result = apiInstance.accountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetAppAccountsApi#accountsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |
| **body** | [**NetAppAccount**](NetAppAccount.md)| NetApp Account object supplied in the body of the operation. | |

### Return type

[**NetAppAccount**](NetAppAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - account updated |  -  |
| **201** | Account created |  -  |
| **202** | Accepted -- Create request accepted; operation will complete asynchronously |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="accountsDelete"></a>
# **accountsDelete**
> accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)



Delete a NetApp account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetAppAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetAppAccountsApi apiInstance = new NetAppAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetAppAccountsApi#accountsDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |

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
| **202** | Accepted -- Create or update request accepted; operation will complete asynchronously |  -  |
| **204** | NoContent -- Resource does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="accountsGet"></a>
# **accountsGet**
> NetAppAccount accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



Get the NetApp account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetAppAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetAppAccountsApi apiInstance = new NetAppAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    try {
      NetAppAccount result = apiInstance.accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetAppAccountsApi#accountsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |

### Return type

[**NetAppAccount**](NetAppAccount.md)

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

<a id="accountsList"></a>
# **accountsList**
> NetAppAccountList accountsList(subscriptionId, resourceGroupName, apiVersion)



Lists all NetApp accounts in the resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetAppAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetAppAccountsApi apiInstance = new NetAppAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    try {
      NetAppAccountList result = apiInstance.accountsList(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetAppAccountsApi#accountsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |

### Return type

[**NetAppAccountList**](NetAppAccountList.md)

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

<a id="accountsUpdate"></a>
# **accountsUpdate**
> NetAppAccount accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, body)



Patch a NetApp account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetAppAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetAppAccountsApi apiInstance = new NetAppAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    NetAppAccountPatch body = new NetAppAccountPatch(); // NetAppAccountPatch | NetApp Account object supplied in the body of the operation.
    try {
      NetAppAccount result = apiInstance.accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetAppAccountsApi#accountsUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |
| **body** | [**NetAppAccountPatch**](NetAppAccountPatch.md)| NetApp Account object supplied in the body of the operation. | |

### Return type

[**NetAppAccount**](NetAppAccount.md)

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

