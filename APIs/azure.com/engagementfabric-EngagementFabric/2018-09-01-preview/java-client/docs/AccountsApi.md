# AccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsCreateOrUpdate**](AccountsApi.md#accountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName} | Create or Update the EngagementFabric account |
| [**accountsDelete**](AccountsApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName} | Delete the EngagementFabric account |
| [**accountsGet**](AccountsApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName} | Get the EngagementFabric account |
| [**accountsList**](AccountsApi.md#accountsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EngagementFabric/Accounts | List the EngagementFabric accounts in given subscription |
| [**accountsListByResourceGroup**](AccountsApi.md#accountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts | List EngagementFabric accounts in given resource group |
| [**accountsListChannelTypes**](AccountsApi.md#accountsListChannelTypes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/listChannelTypes | List available EngagementFabric channel types and functions |
| [**accountsListKeys**](AccountsApi.md#accountsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/listKeys | List keys of the EngagementFabric account |
| [**accountsRegenerateKey**](AccountsApi.md#accountsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/regenerateKey | Regenerate key of the EngagementFabric account |
| [**accountsUpdate**](AccountsApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName} | Update EngagementFabric account |


<a id="accountsCreateOrUpdate"></a>
# **accountsCreateOrUpdate**
> Account accountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, account)

Create or Update the EngagementFabric account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String apiVersion = "apiVersion_example"; // String | API version
    Account account = new Account(); // Account | The EngagementFabric account description
    try {
      Account result = apiInstance.accountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **apiVersion** | **String**| API version | |
| **account** | [**Account**](Account.md)| The EngagementFabric account description | |

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="accountsDelete"></a>
# **accountsDelete**
> accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)

Delete the EngagementFabric account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      apiInstance.accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsDelete");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **apiVersion** | **String**| API version | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Error response |  -  |

<a id="accountsGet"></a>
# **accountsGet**
> Account accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)

Get the EngagementFabric account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      Account result = apiInstance.accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsGet");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **apiVersion** | **String**| API version | |

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="accountsList"></a>
# **accountsList**
> AccountList accountsList(subscriptionId, apiVersion)

List the EngagementFabric accounts in given subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      AccountList result = apiInstance.accountsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsList");
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
| **subscriptionId** | **String**| Subscription ID | |
| **apiVersion** | **String**| API version | |

### Return type

[**AccountList**](AccountList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="accountsListByResourceGroup"></a>
# **accountsListByResourceGroup**
> AccountList accountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)

List EngagementFabric accounts in given resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      AccountList result = apiInstance.accountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **apiVersion** | **String**| API version | |

### Return type

[**AccountList**](AccountList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="accountsListChannelTypes"></a>
# **accountsListChannelTypes**
> ChannelTypeDescriptionList accountsListChannelTypes(subscriptionId, resourceGroupName, accountName, apiVersion)

List available EngagementFabric channel types and functions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      ChannelTypeDescriptionList result = apiInstance.accountsListChannelTypes(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsListChannelTypes");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **apiVersion** | **String**| API version | |

### Return type

[**ChannelTypeDescriptionList**](ChannelTypeDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="accountsListKeys"></a>
# **accountsListKeys**
> KeyDescriptionList accountsListKeys(subscriptionId, resourceGroupName, accountName, apiVersion)

List keys of the EngagementFabric account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String apiVersion = "apiVersion_example"; // String | API version
    try {
      KeyDescriptionList result = apiInstance.accountsListKeys(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsListKeys");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **apiVersion** | **String**| API version | |

### Return type

[**KeyDescriptionList**](KeyDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="accountsRegenerateKey"></a>
# **accountsRegenerateKey**
> KeyDescription accountsRegenerateKey(subscriptionId, resourceGroupName, accountName, apiVersion, parameter)

Regenerate key of the EngagementFabric account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String apiVersion = "apiVersion_example"; // String | API version
    RegenerateKeyParameter parameter = new RegenerateKeyParameter(); // RegenerateKeyParameter | Parameters specifying the key to be regenerated
    try {
      KeyDescription result = apiInstance.accountsRegenerateKey(subscriptionId, resourceGroupName, accountName, apiVersion, parameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsRegenerateKey");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **apiVersion** | **String**| API version | |
| **parameter** | [**RegenerateKeyParameter**](RegenerateKeyParameter.md)| Parameters specifying the key to be regenerated | |

### Return type

[**KeyDescription**](KeyDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="accountsUpdate"></a>
# **accountsUpdate**
> Account accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, accountPatch)

Update EngagementFabric account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String accountName = "accountName_example"; // String | Account Name
    String apiVersion = "apiVersion_example"; // String | API version
    AccountPatch accountPatch = new AccountPatch(); // AccountPatch | The account patch
    try {
      Account result = apiInstance.accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, accountPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsUpdate");
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
| **subscriptionId** | **String**| Subscription ID | |
| **resourceGroupName** | **String**| Resource Group Name | |
| **accountName** | **String**| Account Name | |
| **apiVersion** | **String**| API version | |
| **accountPatch** | [**AccountPatch**](AccountPatch.md)| The account patch | |

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

