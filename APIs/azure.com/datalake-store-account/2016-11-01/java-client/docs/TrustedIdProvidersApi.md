# TrustedIdProvidersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**trustedIdProvidersCreateOrUpdate**](TrustedIdProvidersApi.md#trustedIdProvidersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders/{trustedIdProviderName} |  |
| [**trustedIdProvidersDelete**](TrustedIdProvidersApi.md#trustedIdProvidersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders/{trustedIdProviderName} |  |
| [**trustedIdProvidersGet**](TrustedIdProvidersApi.md#trustedIdProvidersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders/{trustedIdProviderName} |  |
| [**trustedIdProvidersListByAccount**](TrustedIdProvidersApi.md#trustedIdProvidersListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders |  |
| [**trustedIdProvidersUpdate**](TrustedIdProvidersApi.md#trustedIdProvidersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders/{trustedIdProviderName} |  |


<a id="trustedIdProvidersCreateOrUpdate"></a>
# **trustedIdProvidersCreateOrUpdate**
> TrustedIdProvider trustedIdProvidersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, parameters)



Creates or updates the specified trusted identity provider. During update, the trusted identity provider with the specified name will be replaced with this new provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrustedIdProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TrustedIdProvidersApi apiInstance = new TrustedIdProvidersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String trustedIdProviderName = "trustedIdProviderName_example"; // String | The name of the trusted identity provider. This is used for differentiation of providers in the account.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    CreateOrUpdateTrustedIdProviderParameters parameters = new CreateOrUpdateTrustedIdProviderParameters(); // CreateOrUpdateTrustedIdProviderParameters | Parameters supplied to create or replace the trusted identity provider.
    try {
      TrustedIdProvider result = apiInstance.trustedIdProvidersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrustedIdProvidersApi#trustedIdProvidersCreateOrUpdate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **trustedIdProviderName** | **String**| The name of the trusted identity provider. This is used for differentiation of providers in the account. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**CreateOrUpdateTrustedIdProviderParameters**](CreateOrUpdateTrustedIdProviderParameters.md)| Parameters supplied to create or replace the trusted identity provider. | |

### Return type

[**TrustedIdProvider**](TrustedIdProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added the trusted identity provider. |  -  |

<a id="trustedIdProvidersDelete"></a>
# **trustedIdProvidersDelete**
> trustedIdProvidersDelete(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion)



Deletes the specified trusted identity provider from the specified Data Lake Store account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrustedIdProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TrustedIdProvidersApi apiInstance = new TrustedIdProvidersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String trustedIdProviderName = "trustedIdProviderName_example"; // String | The name of the trusted identity provider to delete.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.trustedIdProvidersDelete(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrustedIdProvidersApi#trustedIdProvidersDelete");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **trustedIdProviderName** | **String**| The name of the trusted identity provider to delete. | |
| **apiVersion** | **String**| Client Api Version. | |

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
| **200** | Successfully deleted the specified trusted identity provider details. |  -  |
| **204** | The specified trusted identity provider was not found. |  -  |

<a id="trustedIdProvidersGet"></a>
# **trustedIdProvidersGet**
> TrustedIdProvider trustedIdProvidersGet(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion)



Gets the specified Data Lake Store trusted identity provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrustedIdProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TrustedIdProvidersApi apiInstance = new TrustedIdProvidersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String trustedIdProviderName = "trustedIdProviderName_example"; // String | The name of the trusted identity provider to retrieve.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      TrustedIdProvider result = apiInstance.trustedIdProvidersGet(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrustedIdProvidersApi#trustedIdProvidersGet");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **trustedIdProviderName** | **String**| The name of the trusted identity provider to retrieve. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**TrustedIdProvider**](TrustedIdProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved details of the specified trusted identity provider. |  -  |

<a id="trustedIdProvidersListByAccount"></a>
# **trustedIdProvidersListByAccount**
> TrustedIdProviderListResult trustedIdProvidersListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Data Lake Store trusted identity providers within the specified Data Lake Store account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrustedIdProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TrustedIdProvidersApi apiInstance = new TrustedIdProvidersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      TrustedIdProviderListResult result = apiInstance.trustedIdProvidersListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrustedIdProvidersApi#trustedIdProvidersListByAccount");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**TrustedIdProviderListResult**](TrustedIdProviderListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of trusted identity providers. |  -  |

<a id="trustedIdProvidersUpdate"></a>
# **trustedIdProvidersUpdate**
> TrustedIdProvider trustedIdProvidersUpdate(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, parameters)



Updates the specified trusted identity provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrustedIdProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TrustedIdProvidersApi apiInstance = new TrustedIdProvidersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
    String accountName = "accountName_example"; // String | The name of the Data Lake Store account.
    String trustedIdProviderName = "trustedIdProviderName_example"; // String | The name of the trusted identity provider. This is used for differentiation of providers in the account.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    UpdateTrustedIdProviderParameters parameters = new UpdateTrustedIdProviderParameters(); // UpdateTrustedIdProviderParameters | Parameters supplied to update the trusted identity provider.
    try {
      TrustedIdProvider result = apiInstance.trustedIdProvidersUpdate(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrustedIdProvidersApi#trustedIdProvidersUpdate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the Azure resource group. | |
| **accountName** | **String**| The name of the Data Lake Store account. | |
| **trustedIdProviderName** | **String**| The name of the trusted identity provider. This is used for differentiation of providers in the account. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**UpdateTrustedIdProviderParameters**](UpdateTrustedIdProviderParameters.md)| Parameters supplied to update the trusted identity provider. | [optional] |

### Return type

[**TrustedIdProvider**](TrustedIdProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added the trusted identity provider. |  -  |

