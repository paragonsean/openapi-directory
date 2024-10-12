# AccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsCheckNameAvailability**](AccountsApi.md#accountsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/microsoft.visualstudio/checkNameAvailability | Accounts_CheckNameAvailability |
| [**accountsCreateOrUpdate**](AccountsApi.md#accountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{resourceName} | Accounts_CreateOrUpdate |
| [**accountsDelete**](AccountsApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{resourceName} | Accounts_Delete |
| [**accountsGet**](AccountsApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account/{resourceName} | Accounts_Get |
| [**accountsListByResourceGroup**](AccountsApi.md#accountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.visualstudio/account | Accounts_ListByResourceGroup |


<a id="accountsCheckNameAvailability"></a>
# **accountsCheckNameAvailability**
> CheckNameAvailabilityResult accountsCheckNameAvailability(subscriptionId, apiVersion, body)

Accounts_CheckNameAvailability

Checks if the specified Visual Studio Team Services account name is available. Resource name can be either an account name or an account name and PUID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    CheckNameAvailabilityParameter body = new CheckNameAvailabilityParameter(); // CheckNameAvailabilityParameter | Parameters describing the name to check availability for.
    try {
      CheckNameAvailabilityResult result = apiInstance.accountsCheckNameAvailability(subscriptionId, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsCheckNameAvailability");
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
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **body** | [**CheckNameAvailabilityParameter**](CheckNameAvailabilityParameter.md)| Parameters describing the name to check availability for. | |

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response contains the result of the name availability check. |  -  |

<a id="accountsCreateOrUpdate"></a>
# **accountsCreateOrUpdate**
> AccountResource accountsCreateOrUpdate(resourceGroupName, subscriptionId, apiVersion, resourceName, body)

Accounts_CreateOrUpdate

Creates or updates a Visual Studio Team Services account resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String resourceName = "resourceName_example"; // String | Name of the resource.
    AccountResourceRequest body = new AccountResourceRequest(); // AccountResourceRequest | The request data.
    try {
      AccountResource result = apiInstance.accountsCreateOrUpdate(resourceGroupName, subscriptionId, apiVersion, resourceName, body);
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **resourceName** | **String**| Name of the resource. | |
| **body** | [**AccountResourceRequest**](AccountResourceRequest.md)| The request data. | |

### Return type

[**AccountResource**](AccountResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The Visual Studio Team Services account resource was created or updated. |  -  |
| **404** | The Visual Studio Team Services account does not exist. |  -  |

<a id="accountsDelete"></a>
# **accountsDelete**
> accountsDelete(resourceGroupName, subscriptionId, apiVersion, resourceName)

Accounts_Delete

Deletes a Visual Studio Team Services account resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String resourceName = "resourceName_example"; // String | Name of the resource.
    try {
      apiInstance.accountsDelete(resourceGroupName, subscriptionId, apiVersion, resourceName);
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **resourceName** | **String**| Name of the resource. | |

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
| **200** | The operation succeeded. The Visual Studio Team Services account resource was deleted. |  -  |

<a id="accountsGet"></a>
# **accountsGet**
> AccountResource accountsGet(resourceGroupName, subscriptionId, apiVersion, resourceName)

Accounts_Get

Gets the Visual Studio Team Services account resource details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    String resourceName = "resourceName_example"; // String | Name of the resource.
    try {
      AccountResource result = apiInstance.accountsGet(resourceGroupName, subscriptionId, apiVersion, resourceName);
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |
| **resourceName** | **String**| Name of the resource. | |

### Return type

[**AccountResource**](AccountResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response contains the details of the Visual Studio Team Services account resource. |  -  |
| **404** | The Visual Studio Team Services account does not exist. |  -  |

<a id="accountsListByResourceGroup"></a>
# **accountsListByResourceGroup**
> AccountResourceListResult accountsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Accounts_ListByResourceGroup

Gets all Visual Studio Team Services account resources under the resource group linked to the specified Azure subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription identifier.
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AccountResourceListResult result = apiInstance.accountsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
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
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The Azure subscription identifier. | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AccountResourceListResult**](AccountResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation succeeded. The response contains the details of the Visual Studio Team Services account resources linked to the Azure subscription. |  -  |

