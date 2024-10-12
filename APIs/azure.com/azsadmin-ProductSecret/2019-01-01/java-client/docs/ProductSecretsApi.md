# ProductSecretsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productSecretsGet**](ProductSecretsApi.md#productSecretsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productSecrets/{productId}/secrets/{secretName} |  |
| [**productSecretsImport**](ProductSecretsApi.md#productSecretsImport) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productSecrets/{productId}/secrets/{secretName}/import |  |
| [**productSecretsList**](ProductSecretsApi.md#productSecretsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productPackages/{productId}/secrets |  |
| [**productSecretsValidate**](ProductSecretsApi.md#productSecretsValidate) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productSecrets/{productId}/secrets/{secretName}/validate |  |


<a id="productSecretsGet"></a>
# **productSecretsGet**
> ProductSecret productSecretsGet(subscriptionId, productId, apiVersion, secretName)



Retrieves the specific product secret details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductSecretsApi apiInstance = new ProductSecretsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | The product identifier.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    String secretName = "secretName_example"; // String | The secret name.
    try {
      ProductSecret result = apiInstance.productSecretsGet(subscriptionId, productId, apiVersion, secretName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSecretsApi#productSecretsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| The product identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |
| **secretName** | **String**| The secret name. | |

### Return type

[**ProductSecret**](ProductSecret.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="productSecretsImport"></a>
# **productSecretsImport**
> productSecretsImport(subscriptionId, productId, secretName, apiVersion, secretParameters)



Imports a product secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductSecretsApi apiInstance = new ProductSecretsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | The product identifier.
    String secretName = "secretName_example"; // String | The secret name.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    SecretParameters secretParameters = new SecretParameters(); // SecretParameters | The parameters required for creating/updating a product secret.
    try {
      apiInstance.productSecretsImport(subscriptionId, productId, secretName, apiVersion, secretParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSecretsApi#productSecretsImport");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| The product identifier. | |
| **secretName** | **String**| The secret name. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |
| **secretParameters** | [**SecretParameters**](SecretParameters.md)| The parameters required for creating/updating a product secret. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accepted |  -  |
| **404** | Not Found |  -  |

<a id="productSecretsList"></a>
# **productSecretsList**
> ProductSecretsList productSecretsList(subscriptionId, apiVersion, productId)



Returns an array of product secrets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductSecretsApi apiInstance = new ProductSecretsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    String productId = "productId_example"; // String | The product identifier.
    try {
      ProductSecretsList result = apiInstance.productSecretsList(subscriptionId, apiVersion, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSecretsApi#productSecretsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |
| **productId** | **String**| The product identifier. | |

### Return type

[**ProductSecretsList**](ProductSecretsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productSecretsValidate"></a>
# **productSecretsValidate**
> productSecretsValidate(subscriptionId, productId, secretName, apiVersion, secretParameters)



Validates a product secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductSecretsApi apiInstance = new ProductSecretsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | The product identifier.
    String secretName = "secretName_example"; // String | The secret name.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    SecretParameters secretParameters = new SecretParameters(); // SecretParameters | The parameters required for creating/updating a product secret.
    try {
      apiInstance.productSecretsValidate(subscriptionId, productId, secretName, apiVersion, secretParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSecretsApi#productSecretsValidate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| The product identifier. | |
| **secretName** | **String**| The secret name. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |
| **secretParameters** | [**SecretParameters**](SecretParameters.md)| The parameters required for creating/updating a product secret. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accepted |  -  |
| **404** | Not Found |  -  |

