# SecretsApi

All URIs are relative to *http://conjur.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSecret**](SecretsApi.md#createSecret) | **POST** /secrets/{account}/{kind}/{identifier} | Creates a secret value within the specified variable. |
| [**getSecret**](SecretsApi.md#getSecret) | **GET** /secrets/{account}/{kind}/{identifier} | Fetches the value of a secret from the specified Secret. |
| [**getSecrets**](SecretsApi.md#getSecrets) | **GET** /secrets | Fetch multiple secrets |


<a id="createSecret"></a>
# **createSecret**
> createSecret(account, kind, identifier, xRequestId, expirations, body)

Creates a secret value within the specified variable.

Creates a secret value within the specified Secret.   Note: Conjur will allow you to add a secret to any resource, but the best practice is to store and retrieve secret data only using Secret resources. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String account = "account_example"; // String | Organization account name
    String kind = "kind_example"; // String | Type of resource - in almost all cases this should be `variable`
    String identifier = "identifier_example"; // String | URL-encoded variable ID
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    String expirations = "expirations_example"; // String | Tells the server to reset the variables expiration date
    String body = "body_example"; // String | Secret data
    try {
      apiInstance.createSecret(account, kind, identifier, xRequestId, expirations, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#createSecret");
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
| **account** | **String**| Organization account name | |
| **kind** | **String**| Type of resource - in almost all cases this should be &#x60;variable&#x60; | |
| **identifier** | **String**| URL-encoded variable ID | |
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |
| **expirations** | **String**| Tells the server to reset the variables expiration date | [optional] |
| **body** | **String**| Secret data | [optional] |

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The secret value was added successfully |  -  |
| **400** | The server cannot process the request due to malformed request syntax |  -  |
| **401** | Authentication information is missing or invalid |  -  |
| **403** | The authenticated user lacks the necessary privileges |  -  |
| **422** | A request parameter was either missing or invalid. |  -  |

<a id="getSecret"></a>
# **getSecret**
> String getSecret(account, kind, identifier, xRequestId, version)

Fetches the value of a secret from the specified Secret.

Fetches the value of a secret from the specified Secret. The latest version will be retrieved unless the version parameter is specified. The twenty most recent secret versions are retained.  The secret data is returned in the response body.  Note: Conjur will allow you to add a secret to any resource, but the best practice is to store and retrieve secret data only using Secret resources. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String account = "account_example"; // String | Organization account name
    String kind = "kind_example"; // String | Type of resource - in almost all cases this should be `variable`
    String identifier = "identifier_example"; // String | URL-encoded variable ID
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    Integer version = 56; // Integer | (**Optional**) Version you want to retrieve (Conjur keeps the last 20 versions of a secret)
    try {
      String result = apiInstance.getSecret(account, kind, identifier, xRequestId, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#getSecret");
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
| **account** | **String**| Organization account name | |
| **kind** | **String**| Type of resource - in almost all cases this should be &#x60;variable&#x60; | |
| **identifier** | **String**| URL-encoded variable ID | |
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |
| **version** | **Integer**| (**Optional**) Version you want to retrieve (Conjur keeps the last 20 versions of a secret) | [optional] |

### Return type

**String**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The secret value was added successfully |  -  |
| **400** | The server cannot process the request due to malformed request syntax |  -  |
| **401** | Authentication information is missing or invalid |  -  |
| **403** | The authenticated user lacks the necessary privileges |  -  |
| **404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
| **422** | A request parameter was either missing or invalid. |  -  |

<a id="getSecrets"></a>
# **getSecrets**
> Object getSecrets(variableIds, xRequestId, acceptEncoding)

Fetch multiple secrets

Fetches multiple secret values in one invocation. It’s faster to fetch secrets in batches than to fetch them one at a time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String variableIds = "myorg:variable:secret1,myorg:variable:secret1"; // String | Comma-delimited, URL-encoded resource IDs of the variables.
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    String acceptEncoding = "base64"; // String | Set the encoding of the response object
    try {
      Object result = apiInstance.getSecrets(variableIds, xRequestId, acceptEncoding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#getSecrets");
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
| **variableIds** | **String**| Comma-delimited, URL-encoded resource IDs of the variables. | |
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |
| **acceptEncoding** | **String**| Set the encoding of the response object | [optional] [enum: base64] |

### Return type

**Object**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The batch secret values |  -  |
| **401** | Authentication information is missing or invalid |  -  |
| **403** | The authenticated user lacks the necessary privileges |  -  |
| **404** | At least one resource was unable to be found |  -  |
| **406** | Issue encoding secret into JSON format |  -  |
| **422** | A request parameter was either missing or invalid. |  -  |

