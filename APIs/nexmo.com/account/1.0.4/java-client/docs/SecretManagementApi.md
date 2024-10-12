# SecretManagementApi

All URIs are relative to *https://api.nexmo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAPISecret**](SecretManagementApi.md#createAPISecret) | **POST** /accounts/{api_key}/secrets | Create API Secret |
| [**retrieveAPISecret**](SecretManagementApi.md#retrieveAPISecret) | **GET** /accounts/{api_key}/secrets/{secret_id} | Retrieve one API Secret |
| [**retrieveAPISecrets**](SecretManagementApi.md#retrieveAPISecrets) | **GET** /accounts/{api_key}/secrets | Retrieve API Secrets |
| [**revokeAPISecret**](SecretManagementApi.md#revokeAPISecret) | **DELETE** /accounts/{api_key}/secrets/{secret_id} | Revoke an API Secret |


<a id="createAPISecret"></a>
# **createAPISecret**
> SecretInfo createAPISecret(apiKey, createSecretRequest)

Create API Secret

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SecretManagementApi apiInstance = new SecretManagementApi(defaultClient);
    String apiKey = "abcd1234"; // String | The API key to manage secrets for
    CreateSecretRequest createSecretRequest = new CreateSecretRequest(); // CreateSecretRequest | 
    try {
      SecretInfo result = apiInstance.createAPISecret(apiKey, createSecretRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretManagementApi#createAPISecret");
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
| **apiKey** | **String**| The API key to manage secrets for | |
| **createSecretRequest** | [**CreateSecretRequest**](CreateSecretRequest.md)|  | |

### Return type

[**SecretInfo**](SecretInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Secret created |  -  |
| **400** | Bad request. This usually indicates valid data but can also occur when a user has exceeded the allowed number of secrets on their account. |  -  |
| **401** | Credentials are missing or invalid |  -  |
| **404** | Item not found |  -  |

<a id="retrieveAPISecret"></a>
# **retrieveAPISecret**
> SecretInfo retrieveAPISecret(apiKey, secretId)

Retrieve one API Secret

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SecretManagementApi apiInstance = new SecretManagementApi(defaultClient);
    String apiKey = "abcd1234"; // String | The API key to manage secrets for
    String secretId = "01234567-aaaa-bbbb-cccc-defdefdefdef"; // String | ID of the API Secret
    try {
      SecretInfo result = apiInstance.retrieveAPISecret(apiKey, secretId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretManagementApi#retrieveAPISecret");
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
| **apiKey** | **String**| The API key to manage secrets for | |
| **secretId** | **String**| ID of the API Secret | |

### Return type

[**SecretInfo**](SecretInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API secret response |  -  |
| **401** | Credentials are missing or invalid |  -  |
| **404** | Item not found |  -  |

<a id="retrieveAPISecrets"></a>
# **retrieveAPISecrets**
> RetrieveAPISecrets200Response retrieveAPISecrets(apiKey)

Retrieve API Secrets

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SecretManagementApi apiInstance = new SecretManagementApi(defaultClient);
    String apiKey = "abcd1234"; // String | The API key to manage secrets for
    try {
      RetrieveAPISecrets200Response result = apiInstance.retrieveAPISecrets(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretManagementApi#retrieveAPISecrets");
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
| **apiKey** | **String**| The API key to manage secrets for | |

### Return type

[**RetrieveAPISecrets200Response**](RetrieveAPISecrets200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of your current API secrets |  -  |
| **401** | Credentials are missing or invalid |  -  |
| **404** | Item not found |  -  |

<a id="revokeAPISecret"></a>
# **revokeAPISecret**
> revokeAPISecret(apiKey, secretId)

Revoke an API Secret

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
    defaultClient.setBasePath("https://api.nexmo.com");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    SecretManagementApi apiInstance = new SecretManagementApi(defaultClient);
    String apiKey = "abcd1234"; // String | The API key to manage secrets for
    String secretId = "01234567-aaaa-bbbb-cccc-defdefdefdef"; // String | ID of the API Secret
    try {
      apiInstance.revokeAPISecret(apiKey, secretId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretManagementApi#revokeAPISecret");
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
| **apiKey** | **String**| The API key to manage secrets for | |
| **secretId** | **String**| ID of the API Secret | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Revoked secret response (without body content) |  -  |
| **401** | Credentials are missing or invalid |  -  |
| **403** | Operation forbidden by permissions or because this is the only API secret and you are required to have at least one. |  -  |
| **404** | Item not found |  -  |

