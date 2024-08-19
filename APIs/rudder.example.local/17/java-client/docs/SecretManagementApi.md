# SecretManagementApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSecret**](SecretManagementApi.md#addSecret) | **PUT** /secret | Create a secret |
| [**deleteSecret**](SecretManagementApi.md#deleteSecret) | **DELETE** /secret/{name} | Delete a secret |
| [**getAllSecrets**](SecretManagementApi.md#getAllSecrets) | **GET** /secret | List all secrets |
| [**getSecret**](SecretManagementApi.md#getSecret) | **GET** /secret/{name} | Get one secret |
| [**updateSecret**](SecretManagementApi.md#updateSecret) | **POST** /secret | Update a secret |


<a id="addSecret"></a>
# **addSecret**
> AddSecret200Response addSecret(secrets)

Create a secret

Add a secret

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SecretManagementApi apiInstance = new SecretManagementApi(defaultClient);
    Secrets secrets = new Secrets(); // Secrets | 
    try {
      AddSecret200Response result = apiInstance.addSecret(secrets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretManagementApi#addSecret");
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
| **secrets** | [**Secrets**](Secrets.md)|  | |

### Return type

[**AddSecret200Response**](AddSecret200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Secrets information |  -  |

<a id="deleteSecret"></a>
# **deleteSecret**
> DeleteSecret200Response deleteSecret(name)

Delete a secret

Remove the secret by his unique name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SecretManagementApi apiInstance = new SecretManagementApi(defaultClient);
    String name = "name_example"; // String | Unique name of the secret
    try {
      DeleteSecret200Response result = apiInstance.deleteSecret(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretManagementApi#deleteSecret");
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
| **name** | **String**| Unique name of the secret | |

### Return type

[**DeleteSecret200Response**](DeleteSecret200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Secret information |  -  |

<a id="getAllSecrets"></a>
# **getAllSecrets**
> GetAllSecrets200Response getAllSecrets()

List all secrets

Get the list of all secrets without their value

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SecretManagementApi apiInstance = new SecretManagementApi(defaultClient);
    try {
      GetAllSecrets200Response result = apiInstance.getAllSecrets();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretManagementApi#getAllSecrets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAllSecrets200Response**](GetAllSecrets200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Secrets information |  -  |

<a id="getSecret"></a>
# **getSecret**
> GetSecret200Response getSecret(name)

Get one secret

Get one secret by his unique name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SecretManagementApi apiInstance = new SecretManagementApi(defaultClient);
    String name = "name_example"; // String | Unique name of the secret
    try {
      GetSecret200Response result = apiInstance.getSecret(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretManagementApi#getSecret");
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
| **name** | **String**| Unique name of the secret | |

### Return type

[**GetSecret200Response**](GetSecret200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Secret information |  -  |

<a id="updateSecret"></a>
# **updateSecret**
> UpdateSecret200Response updateSecret(secrets)

Update a secret

Update a secret and override the value, the name cannot be overridden

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    SecretManagementApi apiInstance = new SecretManagementApi(defaultClient);
    Secrets secrets = new Secrets(); // Secrets | 
    try {
      UpdateSecret200Response result = apiInstance.updateSecret(secrets);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretManagementApi#updateSecret");
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
| **secrets** | [**Secrets**](Secrets.md)|  | |

### Return type

[**UpdateSecret200Response**](UpdateSecret200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Secrets information |  -  |

