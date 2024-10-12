# AccountApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsCreate**](AccountApi.md#accountsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName} | Create an account in the given resource group |
| [**accountsDelete**](AccountApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName} | Delete an account |
| [**accountsGet**](AccountApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName} | Get an account under a resource group |
| [**accountsListByResourceGroup**](AccountApi.md#accountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts | List Accounts in a resource group |
| [**accountsListBySubscription**](AccountApi.md#accountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataShare/accounts | List Accounts in a subscription |
| [**accountsUpdate**](AccountApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName} | Patch a given account |


<a id="accountsCreate"></a>
# **accountsCreate**
> Account accountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, account)

Create an account in the given resource group

Create an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    Account account = new Account(); // Account | The account payload.
    try {
      Account result = apiInstance.accountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountsCreate");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **apiVersion** | **String**| The api version to use. | |
| **account** | [**Account**](Account.md)| The account payload. | |

### Return type

[**Account**](Account.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **201** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="accountsDelete"></a>
# **accountsDelete**
> OperationResponse accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)

Delete an account

DeleteAccount

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      OperationResponse result = apiInstance.accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountsDelete");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**OperationResponse**](OperationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **202** | Accepted |  -  |
| **204** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="accountsGet"></a>
# **accountsGet**
> Account accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)

Get an account under a resource group

Get an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      Account result = apiInstance.accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountsGet");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**Account**](Account.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="accountsListByResourceGroup"></a>
# **accountsListByResourceGroup**
> AccountList accountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $skipToken)

List Accounts in a resource group

List Accounts in ResourceGroup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      AccountList result = apiInstance.accountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountsListByResourceGroup");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| Continuation token | [optional] |

### Return type

[**AccountList**](AccountList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="accountsListBySubscription"></a>
# **accountsListBySubscription**
> AccountList accountsListBySubscription(subscriptionId, apiVersion, $skipToken)

List Accounts in a subscription

List Accounts in Subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      AccountList result = apiInstance.accountsListBySubscription(subscriptionId, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountsListBySubscription");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| Continuation token | [optional] |

### Return type

[**AccountList**](AccountList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="accountsUpdate"></a>
# **accountsUpdate**
> Account accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, accountUpdateParameters)

Patch a given account

Patch an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    AccountUpdateParameters accountUpdateParameters = new AccountUpdateParameters(); // AccountUpdateParameters | The account update parameters.
    try {
      Account result = apiInstance.accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, accountUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountsUpdate");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **apiVersion** | **String**| The api version to use. | |
| **accountUpdateParameters** | [**AccountUpdateParameters**](AccountUpdateParameters.md)| The account update parameters. | |

### Return type

[**Account**](Account.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

