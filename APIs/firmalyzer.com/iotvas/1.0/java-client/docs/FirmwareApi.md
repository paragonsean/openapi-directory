# FirmwareApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccounts**](FirmwareApi.md#getAccounts) | **GET** /firmware/{firmware_hash}/accounts | Get default accounts and password hashes of a firmware |
| [**getConfigIssues**](FirmwareApi.md#getConfigIssues) | **GET** /firmware/{firmware_hash}/config-issues | Get default OS configuration issues of a device firmware |
| [**getExpiredCerts**](FirmwareApi.md#getExpiredCerts) | **GET** /firmware/{firmware_hash}/expired-certs | Get expired digital certificates embedded in a device firmware |
| [**getPrivateKeys**](FirmwareApi.md#getPrivateKeys) | **GET** /firmware/{firmware_hash}/private-keys | Get private crypto keys embedded in a device firmware |
| [**getRisk**](FirmwareApi.md#getRisk) | **GET** /firmware/{firmware_hash}/risk | Get iot device firmware risk analysis |
| [**getWeakCerts**](FirmwareApi.md#getWeakCerts) | **GET** /firmware/{firmware_hash}/weak-certs | Get certificates with weak fingerprinting algorithms that are mebedded in a device firmware |
| [**getWeakKeys**](FirmwareApi.md#getWeakKeys) | **GET** /firmware/{firmware_hash}/weak-keys | Get weak crypto keys with short length |


<a id="getAccounts"></a>
# **getAccounts**
> List&lt;DefaultAccount&gt; getAccounts(firmwareHash)

Get default accounts and password hashes of a firmware

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: api-key-header
    ApiKeyAuth api-key-header = (ApiKeyAuth) defaultClient.getAuthentication("api-key-header");
    api-key-header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key-header.setApiKeyPrefix("Token");

    FirmwareApi apiInstance = new FirmwareApi(defaultClient);
    String firmwareHash = "af88b1aaac0b222df8539f3ae1479b5c8eaeae41f1776b5dd2fa805cb33a1175"; // String | SHA2 hash of device firmware
    try {
      List<DefaultAccount> result = apiInstance.getAccounts(firmwareHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareApi#getAccounts");
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
| **firmwareHash** | **String**| SHA2 hash of device firmware | |

### Return type

[**List&lt;DefaultAccount&gt;**](DefaultAccount.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getConfigIssues"></a>
# **getConfigIssues**
> List&lt;ConfigIssue&gt; getConfigIssues(firmwareHash)

Get default OS configuration issues of a device firmware

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: api-key-header
    ApiKeyAuth api-key-header = (ApiKeyAuth) defaultClient.getAuthentication("api-key-header");
    api-key-header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key-header.setApiKeyPrefix("Token");

    FirmwareApi apiInstance = new FirmwareApi(defaultClient);
    String firmwareHash = "aa96e4d41a4b0ceb3f1ae4d94f3cb445621b9501e3a9c69e6b9eb37c5888a03c"; // String | SHA2 hash of device firmware
    try {
      List<ConfigIssue> result = apiInstance.getConfigIssues(firmwareHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareApi#getConfigIssues");
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
| **firmwareHash** | **String**| SHA2 hash of device firmware | |

### Return type

[**List&lt;ConfigIssue&gt;**](ConfigIssue.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getExpiredCerts"></a>
# **getExpiredCerts**
> List&lt;ExpiredCert&gt; getExpiredCerts(firmwareHash)

Get expired digital certificates embedded in a device firmware

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: api-key-header
    ApiKeyAuth api-key-header = (ApiKeyAuth) defaultClient.getAuthentication("api-key-header");
    api-key-header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key-header.setApiKeyPrefix("Token");

    FirmwareApi apiInstance = new FirmwareApi(defaultClient);
    String firmwareHash = "ac7c090c34338ea6a3b335004755e24578e7e4eee739c5c33736f0822b64907e"; // String | SHA2 hash of device firmware
    try {
      List<ExpiredCert> result = apiInstance.getExpiredCerts(firmwareHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareApi#getExpiredCerts");
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
| **firmwareHash** | **String**| SHA2 hash of device firmware | |

### Return type

[**List&lt;ExpiredCert&gt;**](ExpiredCert.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getPrivateKeys"></a>
# **getPrivateKeys**
> List&lt;CryptoKey&gt; getPrivateKeys(firmwareHash)

Get private crypto keys embedded in a device firmware

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: api-key-header
    ApiKeyAuth api-key-header = (ApiKeyAuth) defaultClient.getAuthentication("api-key-header");
    api-key-header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key-header.setApiKeyPrefix("Token");

    FirmwareApi apiInstance = new FirmwareApi(defaultClient);
    String firmwareHash = "90e3e68e1c61850f20c50e551816d47d484d7feb46890f5bc0a0e0dab3e3ba0b"; // String | SHA2 hash of device firmware
    try {
      List<CryptoKey> result = apiInstance.getPrivateKeys(firmwareHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareApi#getPrivateKeys");
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
| **firmwareHash** | **String**| SHA2 hash of device firmware | |

### Return type

[**List&lt;CryptoKey&gt;**](CryptoKey.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getRisk"></a>
# **getRisk**
> FirmwareRisk getRisk(firmwareHash)

Get iot device firmware risk analysis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: api-key-header
    ApiKeyAuth api-key-header = (ApiKeyAuth) defaultClient.getAuthentication("api-key-header");
    api-key-header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key-header.setApiKeyPrefix("Token");

    FirmwareApi apiInstance = new FirmwareApi(defaultClient);
    String firmwareHash = "af88b1aaac0b222df8539f3ae1479b5c8eaeae41f1776b5dd2fa805cb33a1175"; // String | SHA2 hash of device firmware
    try {
      FirmwareRisk result = apiInstance.getRisk(firmwareHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareApi#getRisk");
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
| **firmwareHash** | **String**| SHA2 hash of device firmware | |

### Return type

[**FirmwareRisk**](FirmwareRisk.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getWeakCerts"></a>
# **getWeakCerts**
> List&lt;WeakCert&gt; getWeakCerts(firmwareHash)

Get certificates with weak fingerprinting algorithms that are mebedded in a device firmware

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: api-key-header
    ApiKeyAuth api-key-header = (ApiKeyAuth) defaultClient.getAuthentication("api-key-header");
    api-key-header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key-header.setApiKeyPrefix("Token");

    FirmwareApi apiInstance = new FirmwareApi(defaultClient);
    String firmwareHash = "52841661d61e00649451cc471e9b56d169df8041926b1252bb3fd0710c27b12c"; // String | SHA2 hash of device firmware
    try {
      List<WeakCert> result = apiInstance.getWeakCerts(firmwareHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareApi#getWeakCerts");
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
| **firmwareHash** | **String**| SHA2 hash of device firmware | |

### Return type

[**List&lt;WeakCert&gt;**](WeakCert.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getWeakKeys"></a>
# **getWeakKeys**
> List&lt;CryptoKey&gt; getWeakKeys(firmwareHash)

Get weak crypto keys with short length

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: api-key-header
    ApiKeyAuth api-key-header = (ApiKeyAuth) defaultClient.getAuthentication("api-key-header");
    api-key-header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key-header.setApiKeyPrefix("Token");

    FirmwareApi apiInstance = new FirmwareApi(defaultClient);
    String firmwareHash = "852031776c09f8152c90496f2c3fac85b46a938d20612d7fc03eea8aab46f23e"; // String | SHA2 hash of device firmware
    try {
      List<CryptoKey> result = apiInstance.getWeakKeys(firmwareHash);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareApi#getWeakKeys");
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
| **firmwareHash** | **String**| SHA2 hash of device firmware | |

### Return type

[**List&lt;CryptoKey&gt;**](CryptoKey.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

