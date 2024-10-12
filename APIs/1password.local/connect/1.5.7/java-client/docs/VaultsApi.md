# VaultsApi

All URIs are relative to *http://1password.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVaultById**](VaultsApi.md#getVaultById) | **GET** /vaults/{vaultUuid} | Get Vault details and metadata |
| [**getVaults**](VaultsApi.md#getVaults) | **GET** /vaults | Get all Vaults |


<a id="getVaultById"></a>
# **getVaultById**
> Vault getVaultById(vaultUuid)

Get Vault details and metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String vaultUuid = "vaultUuid_example"; // String | The UUID of the Vault to fetch Items from
    try {
      Vault result = apiInstance.getVaultById(vaultUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#getVaultById");
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
| **vaultUuid** | **String**| The UUID of the Vault to fetch Items from | |

### Return type

[**Vault**](Vault.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Invalid or missing token |  -  |
| **403** | Unauthorized access |  -  |
| **404** | Vault not found |  -  |

<a id="getVaults"></a>
# **getVaults**
> List&lt;Vault&gt; getVaults(filter)

Get all Vaults

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");
    
    // Configure HTTP bearer authorization: ConnectToken
    HttpBearerAuth ConnectToken = (HttpBearerAuth) defaultClient.getAuthentication("ConnectToken");
    ConnectToken.setBearerToken("BEARER TOKEN");

    VaultsApi apiInstance = new VaultsApi(defaultClient);
    String filter = "name eq \"Some Vault Name\""; // String | Filter the Vault collection based on Vault name using SCIM eq filter
    try {
      List<Vault> result = apiInstance.getVaults(filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultsApi#getVaults");
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
| **filter** | **String**| Filter the Vault collection based on Vault name using SCIM eq filter | [optional] |

### Return type

[**List&lt;Vault&gt;**](Vault.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Invalid or missing token |  -  |

