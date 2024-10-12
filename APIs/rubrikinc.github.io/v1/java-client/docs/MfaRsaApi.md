# MfaRsaApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRsaMfaServer**](MfaRsaApi.md#createRsaMfaServer) | **POST** /mfa/rsa/server | Register a new RSA server |
| [**deleteRsaMfaServer**](MfaRsaApi.md#deleteRsaMfaServer) | **DELETE** /mfa/rsa/server/{id} | Delete RSA server |
| [**getRsaMfaServer**](MfaRsaApi.md#getRsaMfaServer) | **GET** /mfa/rsa/server/{id} | Get RSA server configuration |
| [**queryRsaMfaServers**](MfaRsaApi.md#queryRsaMfaServers) | **GET** /mfa/rsa/server | Get RSA server configuration |
| [**updateRsaMfaServer**](MfaRsaApi.md#updateRsaMfaServer) | **PATCH** /mfa/rsa/server/{id} | Update RSA server configuration |


<a id="createRsaMfaServer"></a>
# **createRsaMfaServer**
> RsaMfaServerDetail createRsaMfaServer(rsaMfaServerConfig)

Register a new RSA server

Register a new RSA server using specified configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MfaRsaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    MfaRsaApi apiInstance = new MfaRsaApi(defaultClient);
    RsaMfaServerConfig rsaMfaServerConfig = new RsaMfaServerConfig(); // RsaMfaServerConfig | Configuration of RSA server.
    try {
      RsaMfaServerDetail result = apiInstance.createRsaMfaServer(rsaMfaServerConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MfaRsaApi#createRsaMfaServer");
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
| **rsaMfaServerConfig** | [**RsaMfaServerConfig**](RsaMfaServerConfig.md)| Configuration of RSA server. | |

### Return type

[**RsaMfaServerDetail**](RsaMfaServerDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added a new RSA server. |  -  |

<a id="deleteRsaMfaServer"></a>
# **deleteRsaMfaServer**
> deleteRsaMfaServer(id)

Delete RSA server

Delete RSA server configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MfaRsaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    MfaRsaApi apiInstance = new MfaRsaApi(defaultClient);
    String id = "id_example"; // String | ID of the RSA server.
    try {
      apiInstance.deleteRsaMfaServer(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MfaRsaApi#deleteRsaMfaServer");
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
| **id** | **String**| ID of the RSA server. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | RSA server configuration removed. |  -  |

<a id="getRsaMfaServer"></a>
# **getRsaMfaServer**
> RsaMfaServerDetail getRsaMfaServer(id)

Get RSA server configuration

Get RSA server configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MfaRsaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    MfaRsaApi apiInstance = new MfaRsaApi(defaultClient);
    String id = "id_example"; // String | ID of the RSA server.
    try {
      RsaMfaServerDetail result = apiInstance.getRsaMfaServer(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MfaRsaApi#getRsaMfaServer");
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
| **id** | **String**| ID of the RSA server. | |

### Return type

[**RsaMfaServerDetail**](RsaMfaServerDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Configuration summary of known RSA servers. |  -  |

<a id="queryRsaMfaServers"></a>
# **queryRsaMfaServers**
> RsaMfaServerDetailListResponse queryRsaMfaServers()

Get RSA server configuration

Get RSA server configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MfaRsaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    MfaRsaApi apiInstance = new MfaRsaApi(defaultClient);
    try {
      RsaMfaServerDetailListResponse result = apiInstance.queryRsaMfaServers();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MfaRsaApi#queryRsaMfaServers");
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

[**RsaMfaServerDetailListResponse**](RsaMfaServerDetailListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Configuration summary of known RSA servers. |  -  |

<a id="updateRsaMfaServer"></a>
# **updateRsaMfaServer**
> RsaMfaServerDetail updateRsaMfaServer(id, rsaMfaServerConfigUpdate)

Update RSA server configuration

Update an existing RSA server using specified configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MfaRsaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    MfaRsaApi apiInstance = new MfaRsaApi(defaultClient);
    String id = "id_example"; // String | ID of the RSA server.
    RsaMfaServerConfigUpdate rsaMfaServerConfigUpdate = new RsaMfaServerConfigUpdate(); // RsaMfaServerConfigUpdate | Configuration of RSA server.
    try {
      RsaMfaServerDetail result = apiInstance.updateRsaMfaServer(id, rsaMfaServerConfigUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MfaRsaApi#updateRsaMfaServer");
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
| **id** | **String**| ID of the RSA server. | |
| **rsaMfaServerConfigUpdate** | [**RsaMfaServerConfigUpdate**](RsaMfaServerConfigUpdate.md)| Configuration of RSA server. | |

### Return type

[**RsaMfaServerDetail**](RsaMfaServerDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated RSA server configuration. |  -  |

