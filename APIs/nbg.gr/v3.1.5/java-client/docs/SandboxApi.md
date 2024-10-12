# SandboxApi

All URIs are relative to *https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sandboxPost**](SandboxApi.md#sandboxPost) | **POST** /sandbox | Create Sandbox |
| [**sandboxPut**](SandboxApi.md#sandboxPut) | **PUT** /sandbox | Import Sandbox |
| [**sandboxSandboxIdDelete**](SandboxApi.md#sandboxSandboxIdDelete) | **DELETE** /sandbox/{sandboxId} | Delete Sandbox |
| [**sandboxSandboxIdGet**](SandboxApi.md#sandboxSandboxIdGet) | **GET** /sandbox/{sandboxId} | Export Sandbox |


<a id="sandboxPost"></a>
# **sandboxPost**
> Sandbox sandboxPost(sandboxRequest)

Create Sandbox

Create Sandbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5");
    
    // Configure OAuth2 access token for authorization: Authorization-Code-Token
    OAuth Authorization-Code-Token = (OAuth) defaultClient.getAuthentication("Authorization-Code-Token");
    Authorization-Code-Token.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Client-Id
    ApiKeyAuth Client-Id = (ApiKeyAuth) defaultClient.getAuthentication("Client-Id");
    Client-Id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Client-Id.setApiKeyPrefix("Token");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    SandboxRequest sandboxRequest = new SandboxRequest(); // SandboxRequest | SandboxRequest
    try {
      Sandbox result = apiInstance.sandboxPost(sandboxRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#sandboxPost");
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
| **sandboxRequest** | [**SandboxRequest**](SandboxRequest.md)| SandboxRequest | [optional] |

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: application/json, application/json; charset=utf-8
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **415** | Unsupported Media Type |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

<a id="sandboxPut"></a>
# **sandboxPut**
> sandboxPut(sandbox)

Import Sandbox

Import Sandbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5");
    
    // Configure OAuth2 access token for authorization: Authorization-Code-Token
    OAuth Authorization-Code-Token = (OAuth) defaultClient.getAuthentication("Authorization-Code-Token");
    Authorization-Code-Token.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Client-Id
    ApiKeyAuth Client-Id = (ApiKeyAuth) defaultClient.getAuthentication("Client-Id");
    Client-Id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Client-Id.setApiKeyPrefix("Token");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    Sandbox sandbox = new Sandbox(); // Sandbox | Sandbox
    try {
      apiInstance.sandboxPut(sandbox);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#sandboxPut");
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
| **sandbox** | [**Sandbox**](Sandbox.md)| Sandbox | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: application/json, application/json; charset=utf-8
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **415** | Unsupported Media Type |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

<a id="sandboxSandboxIdDelete"></a>
# **sandboxSandboxIdDelete**
> sandboxSandboxIdDelete(sandboxId)

Delete Sandbox

Delete Sandbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5");
    
    // Configure OAuth2 access token for authorization: Authorization-Code-Token
    OAuth Authorization-Code-Token = (OAuth) defaultClient.getAuthentication("Authorization-Code-Token");
    Authorization-Code-Token.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Client-Id
    ApiKeyAuth Client-Id = (ApiKeyAuth) defaultClient.getAuthentication("Client-Id");
    Client-Id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Client-Id.setApiKeyPrefix("Token");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String sandboxId = "sandboxId_example"; // String | Sandbox Id
    try {
      apiInstance.sandboxSandboxIdDelete(sandboxId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#sandboxSandboxIdDelete");
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
| **sandboxId** | **String**| Sandbox Id | |

### Return type

null (empty response body)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

<a id="sandboxSandboxIdGet"></a>
# **sandboxSandboxIdGet**
> Sandbox sandboxSandboxIdGet(sandboxId)

Export Sandbox

Export Sandbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SandboxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.nbg.gr/sandbox/uk.openbanking.accountinfo/oauth2/v3.1.5");
    
    // Configure OAuth2 access token for authorization: Authorization-Code-Token
    OAuth Authorization-Code-Token = (OAuth) defaultClient.getAuthentication("Authorization-Code-Token");
    Authorization-Code-Token.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Client-Id
    ApiKeyAuth Client-Id = (ApiKeyAuth) defaultClient.getAuthentication("Client-Id");
    Client-Id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Client-Id.setApiKeyPrefix("Token");

    SandboxApi apiInstance = new SandboxApi(defaultClient);
    String sandboxId = "sandboxId_example"; // String | Sandbox Id
    try {
      Sandbox result = apiInstance.sandboxSandboxIdGet(sandboxId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SandboxApi#sandboxSandboxIdGet");
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
| **sandboxId** | **String**| Sandbox Id | |

### Return type

[**Sandbox**](Sandbox.md)

### Authorization

[Authorization-Code-Token](../README.md#Authorization-Code-Token), [Client-Id](../README.md#Client-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **400** | Bad request |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **401** | Unauthorized |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **403** | Forbidden |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **404** | Not Found |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **405** | Method Not Allowed |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **406** | Not Acceptable |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |
| **500** | Internal Server Error |  * x-fapi-interaction-id - An RFC4122 UID used as a correlation id <br>  |

