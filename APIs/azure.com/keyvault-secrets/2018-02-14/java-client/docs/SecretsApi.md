# SecretsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**secretsCreateOrUpdate**](SecretsApi.md#secretsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName} |  |
| [**secretsGet**](SecretsApi.md#secretsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName} |  |
| [**secretsList**](SecretsApi.md#secretsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets |  |
| [**secretsUpdate**](SecretsApi.md#secretsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName} |  |


<a id="secretsCreateOrUpdate"></a>
# **secretsCreateOrUpdate**
> Secret secretsCreateOrUpdate(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId, parameters)



Create or update a secret in a key vault in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
    String vaultName = "vaultName_example"; // String | Name of the vault
    String secretName = "secretName_example"; // String | Name of the secret
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SecretCreateOrUpdateParameters parameters = new SecretCreateOrUpdateParameters(); // SecretCreateOrUpdateParameters | Parameters to create or update the secret
    try {
      Secret result = apiInstance.secretsCreateOrUpdate(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | |
| **vaultName** | **String**| Name of the vault | |
| **secretName** | **String**| Name of the secret | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SecretCreateOrUpdateParameters**](SecretCreateOrUpdateParameters.md)| Parameters to create or update the secret | |

### Return type

[**Secret**](Secret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created or updated secret |  -  |
| **201** | Created or updated vault |  -  |

<a id="secretsGet"></a>
# **secretsGet**
> Secret secretsGet(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId)



Gets the specified secret.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String secretName = "secretName_example"; // String | The name of the secret.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      Secret result = apiInstance.secretsGet(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsGet");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | |
| **vaultName** | **String**| The name of the vault. | |
| **secretName** | **String**| The name of the secret. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**Secret**](Secret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieved secret |  -  |

<a id="secretsList"></a>
# **secretsList**
> SecretListResult secretsList(resourceGroupName, vaultName, apiVersion, subscriptionId, $top)



The List operation gets information about the secrets in a vault.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
    String vaultName = "vaultName_example"; // String | The name of the vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | Maximum number of results to return.
    try {
      SecretListResult result = apiInstance.secretsList(resourceGroupName, vaultName, apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsList");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | |
| **vaultName** | **String**| The name of the vault. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| Maximum number of results to return. | [optional] |

### Return type

[**SecretListResult**](SecretListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get information about secrets in the specified vault. |  -  |

<a id="secretsUpdate"></a>
# **secretsUpdate**
> Secret secretsUpdate(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId, parameters)



Update a secret in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments.  Users should use the data-plane REST service for interaction with vault secrets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
    String vaultName = "vaultName_example"; // String | Name of the vault
    String secretName = "secretName_example"; // String | Name of the secret
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    SecretPatchParameters parameters = new SecretPatchParameters(); // SecretPatchParameters | Parameters to patch the secret
    try {
      Secret result = apiInstance.secretsUpdate(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#secretsUpdate");
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
| **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | |
| **vaultName** | **String**| Name of the vault | |
| **secretName** | **String**| Name of the secret | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**SecretPatchParameters**](SecretPatchParameters.md)| Parameters to patch the secret | |

### Return type

[**Secret**](Secret.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Patched secret |  -  |
| **201** | Patched secret |  -  |

