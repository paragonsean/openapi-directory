# KeysApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addKey**](KeysApi.md#addKey) | **POST** /addresses/{address}/keys | Add address key |
| [**deleteKey**](KeysApi.md#deleteKey) | **DELETE** /addresses/{address}/keys/{key} | Delete address key |
| [**getAllKeys**](KeysApi.md#getAllKeys) | **GET** /addresses/{address}/keys | List address keys |
| [**getKey**](KeysApi.md#getKey) | **GET** /addresses/{address}/keys/{key} | Get address key |
| [**updateKey**](KeysApi.md#updateKey) | **PUT** /addresses/{address}/keys/{key} | Update an address key |


<a id="addKey"></a>
# **addKey**
> AddKeyResponse addKey(address, addKeyRequest)

Add address key

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
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String address = "address_example"; // String | ID of address
    AddKeyRequest addKeyRequest = new AddKeyRequest(); // AddKeyRequest | Key body
    try {
      AddKeyResponse result = apiInstance.addKey(address, addKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#addKey");
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
| **address** | **String**| ID of address | |
| **addKeyRequest** | [**AddKeyRequest**](AddKeyRequest.md)| Key body | |

### Return type

[**AddKeyResponse**](AddKeyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **403** | Bad credentials |  -  |
| **404** | Address not found |  -  |

<a id="deleteKey"></a>
# **deleteKey**
> deleteKey(address, key)

Delete address key

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
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String address = "address_example"; // String | ID of address
    String key = "key_example"; // String | ID of key
    try {
      apiInstance.deleteKey(address, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#deleteKey");
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
| **address** | **String**| ID of address | |
| **key** | **String**| ID of key | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful delete operation |  -  |
| **400** | Failure |  -  |
| **403** | Bad credentials |  -  |
| **404** | Key not found |  -  |

<a id="getAllKeys"></a>
# **getAllKeys**
> GetAllKeysResponse getAllKeys(address)

List address keys

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
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String address = "address_example"; // String | ID of address
    try {
      GetAllKeysResponse result = apiInstance.getAllKeys(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#getAllKeys");
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
| **address** | **String**| ID of address | |

### Return type

[**GetAllKeysResponse**](GetAllKeysResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **403** | Bad credentials |  -  |
| **404** | Address not found |  -  |

<a id="getKey"></a>
# **getKey**
> Key getKey(address, key)

Get address key

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
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String address = "address_example"; // String | ID of address
    String key = "key_example"; // String | ID of key
    try {
      Key result = apiInstance.getKey(address, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#getKey");
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
| **address** | **String**| ID of address | |
| **key** | **String**| ID of key | |

### Return type

[**Key**](Key.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **403** | Bad credentials |  -  |
| **404** | Key not found |  -  |

<a id="updateKey"></a>
# **updateKey**
> Key updateKey(address, key, updateKeyRequest)

Update an address key

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
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    KeysApi apiInstance = new KeysApi(defaultClient);
    String address = "address_example"; // String | ID of address
    String key = "key_example"; // String | ID of key
    UpdateKeyRequest updateKeyRequest = new UpdateKeyRequest(); // UpdateKeyRequest | Key body
    try {
      Key result = apiInstance.updateKey(address, key, updateKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeysApi#updateKey");
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
| **address** | **String**| ID of address | |
| **key** | **String**| ID of key | |
| **updateKeyRequest** | [**UpdateKeyRequest**](UpdateKeyRequest.md)| Key body | |

### Return type

[**Key**](Key.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Failure |  -  |
| **403** | Bad credentials |  -  |
| **404** | Key not found |  -  |

