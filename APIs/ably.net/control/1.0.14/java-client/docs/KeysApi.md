# KeysApi

All URIs are relative to *https://control.ably.net/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsAppIdKeysGet**](KeysApi.md#appsAppIdKeysGet) | **GET** /apps/{app_id}/keys | Lists app keys |
| [**appsAppIdKeysKeyIdPatch**](KeysApi.md#appsAppIdKeysKeyIdPatch) | **PATCH** /apps/{app_id}/keys/{key_id} | Updates a key |
| [**appsAppIdKeysKeyIdRevokePost**](KeysApi.md#appsAppIdKeysKeyIdRevokePost) | **POST** /apps/{app_id}/keys/{key_id}/revoke | Revokes a key |
| [**appsAppIdKeysPost**](KeysApi.md#appsAppIdKeysPost) | **POST** /apps/{app_id}/keys | Creates a key |


<a id="appsAppIdKeysGet"></a>
# **appsAppIdKeysGet**
> List&lt;KeyResponse&gt; appsAppIdKeysGet(appId)

Lists app keys

Lists the API keys associated with the application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    try {
      List<KeyResponse> result = apiInstance.appsAppIdKeysGet(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#appsAppIdKeysGet");
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
| **appId** | **String**| The application ID. | |

### Return type

[**List&lt;KeyResponse&gt;**](KeyResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key list |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdKeysKeyIdPatch"></a>
# **appsAppIdKeysKeyIdPatch**
> KeyResponse appsAppIdKeysKeyIdPatch(appId, keyId, keyPatch)

Updates a key

Update the API key with the specified key ID, for the application with the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    String keyId = "keyId_example"; // String | The API key ID.
    KeyPatch keyPatch = new KeyPatch(); // KeyPatch | 
    try {
      KeyResponse result = apiInstance.appsAppIdKeysKeyIdPatch(appId, keyId, keyPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#appsAppIdKeysKeyIdPatch");
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
| **appId** | **String**| The application ID. | |
| **keyId** | **String**| The API key ID. | |
| **keyPatch** | [**KeyPatch**](KeyPatch.md)|  | [optional] |

### Return type

[**KeyResponse**](KeyResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key updated |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdKeysKeyIdRevokePost"></a>
# **appsAppIdKeysKeyIdRevokePost**
> appsAppIdKeysKeyIdRevokePost(appId, keyId)

Revokes a key

Revokes the API key with the specified ID, with the Application ID. This deletes the key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    String keyId = "keyId_example"; // String | The key ID.
    try {
      apiInstance.appsAppIdKeysKeyIdRevokePost(appId, keyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#appsAppIdKeysKeyIdRevokePost");
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
| **appId** | **String**| The application ID. | |
| **keyId** | **String**| The key ID. | |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key revoked |  -  |
| **401** | Authentication failed |  -  |
| **404** | Not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdKeysPost"></a>
# **appsAppIdKeysPost**
> KeyResponse appsAppIdKeysPost(appId, keyPost)

Creates a key

Creates an API key for the application specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    KeyPost keyPost = new KeyPost(); // KeyPost | 
    try {
      KeyResponse result = apiInstance.appsAppIdKeysPost(appId, keyPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#appsAppIdKeysPost");
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
| **appId** | **String**| The application ID. | |
| **keyPost** | [**KeyPost**](KeyPost.md)|  | [optional] |

### Return type

[**KeyResponse**](KeyResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Key created |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |

