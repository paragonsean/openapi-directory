# VaultExtendedInfoApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vaultExtendedInfoCreateOrUpdate**](VaultExtendedInfoApi.md#vaultExtendedInfoCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/extendedInformation/vaultExtendedInfo |  |
| [**vaultExtendedInfoGet**](VaultExtendedInfoApi.md#vaultExtendedInfoGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/extendedInformation/vaultExtendedInfo |  |
| [**vaultExtendedInfoUpdate**](VaultExtendedInfoApi.md#vaultExtendedInfoUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/extendedInformation/vaultExtendedInfo |  |


<a id="vaultExtendedInfoCreateOrUpdate"></a>
# **vaultExtendedInfoCreateOrUpdate**
> VaultExtendedInfoResource vaultExtendedInfoCreateOrUpdate(subscriptionId, resourceGroupName, vaultName, apiVersion, resourceResourceExtendedInfoDetails)



Create vault extended info.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultExtendedInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VaultExtendedInfoApi apiInstance = new VaultExtendedInfoApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    VaultExtendedInfoResource resourceResourceExtendedInfoDetails = new VaultExtendedInfoResource(); // VaultExtendedInfoResource | Details of ResourceExtendedInfo
    try {
      VaultExtendedInfoResource result = apiInstance.vaultExtendedInfoCreateOrUpdate(subscriptionId, resourceGroupName, vaultName, apiVersion, resourceResourceExtendedInfoDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultExtendedInfoApi#vaultExtendedInfoCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **apiVersion** | **String**| Client Api Version. | |
| **resourceResourceExtendedInfoDetails** | [**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)| Details of ResourceExtendedInfo | |

### Return type

[**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vaultExtendedInfoGet"></a>
# **vaultExtendedInfoGet**
> VaultExtendedInfoResource vaultExtendedInfoGet(subscriptionId, apiVersion, resourceGroupName, vaultName)



Get the vault extended info.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultExtendedInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VaultExtendedInfoApi apiInstance = new VaultExtendedInfoApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    try {
      VaultExtendedInfoResource result = apiInstance.vaultExtendedInfoGet(subscriptionId, apiVersion, resourceGroupName, vaultName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultExtendedInfoApi#vaultExtendedInfoGet");
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
| **subscriptionId** | **String**| The subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **vaultName** | **String**| The name of the recovery services vault. | |

### Return type

[**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vaultExtendedInfoUpdate"></a>
# **vaultExtendedInfoUpdate**
> VaultExtendedInfoResource vaultExtendedInfoUpdate(subscriptionId, resourceGroupName, vaultName, apiVersion, resourceResourceExtendedInfoDetails)



Update vault extended info.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultExtendedInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VaultExtendedInfoApi apiInstance = new VaultExtendedInfoApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    VaultExtendedInfoResource resourceResourceExtendedInfoDetails = new VaultExtendedInfoResource(); // VaultExtendedInfoResource | Details of ResourceExtendedInfo
    try {
      VaultExtendedInfoResource result = apiInstance.vaultExtendedInfoUpdate(subscriptionId, resourceGroupName, vaultName, apiVersion, resourceResourceExtendedInfoDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultExtendedInfoApi#vaultExtendedInfoUpdate");
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
| **subscriptionId** | **String**| The subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **apiVersion** | **String**| Client Api Version. | |
| **resourceResourceExtendedInfoDetails** | [**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)| Details of ResourceExtendedInfo | |

### Return type

[**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

