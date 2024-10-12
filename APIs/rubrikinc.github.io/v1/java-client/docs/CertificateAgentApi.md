# CertificateAgentApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**markAgentSecondaryCertificate**](CertificateAgentApi.md#markAgentSecondaryCertificate) | **POST** /certificate/agent | Mark a certificate to be added to agents |
| [**queryAgentSecondaryCertificate**](CertificateAgentApi.md#queryAgentSecondaryCertificate) | **GET** /certificate/agent | Get all potential agent secondary cluster certificates |
| [**unmarkAgentSecondaryCertificate**](CertificateAgentApi.md#unmarkAgentSecondaryCertificate) | **DELETE** /certificate/agent/{id} | Unmark a certificate that was previously marked |


<a id="markAgentSecondaryCertificate"></a>
# **markAgentSecondaryCertificate**
> AgentSecondaryCertificateInfo markAgentSecondaryCertificate(body)

Mark a certificate to be added to agents

Mark a secondary cluster certificate to be asynchronously synced to all Rubrik Backup Service instances for which this cluster is the primary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateAgentApi;

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

    CertificateAgentApi apiInstance = new CertificateAgentApi(defaultClient);
    String body = "body_example"; // String | ID of certificate to add.
    try {
      AgentSecondaryCertificateInfo result = apiInstance.markAgentSecondaryCertificate(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateAgentApi#markAgentSecondaryCertificate");
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
| **body** | **String**| ID of certificate to add. | |

### Return type

[**AgentSecondaryCertificateInfo**](AgentSecondaryCertificateInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Information about the certificate |  -  |

<a id="queryAgentSecondaryCertificate"></a>
# **queryAgentSecondaryCertificate**
> AgentSecondaryCertificateInfoListResponse queryAgentSecondaryCertificate(isAgentEnabled)

Get all potential agent secondary cluster certificates

Get all certificates that have been added to the cluster and qualify to be secondary cluster certificates for the Rubrik Backup Service. This call retrieves any certificates that are detected to be Rubrik cluster certificates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateAgentApi;

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

    CertificateAgentApi apiInstance = new CertificateAgentApi(defaultClient);
    Boolean isAgentEnabled = true; // Boolean | Filter based on whether or not certificates have been marked for use by agents.
    try {
      AgentSecondaryCertificateInfoListResponse result = apiInstance.queryAgentSecondaryCertificate(isAgentEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateAgentApi#queryAgentSecondaryCertificate");
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
| **isAgentEnabled** | **Boolean**| Filter based on whether or not certificates have been marked for use by agents. | [optional] |

### Return type

[**AgentSecondaryCertificateInfoListResponse**](AgentSecondaryCertificateInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of certificates. |  -  |

<a id="unmarkAgentSecondaryCertificate"></a>
# **unmarkAgentSecondaryCertificate**
> unmarkAgentSecondaryCertificate(id)

Unmark a certificate that was previously marked

Unmark a previously marked secondary cluster certificate to be asynchronously removed from all Rubrik Backup Service instances for which this cluster is the primary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateAgentApi;

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

    CertificateAgentApi apiInstance = new CertificateAgentApi(defaultClient);
    String id = "id_example"; // String | ID of certificate to remove.
    try {
      apiInstance.unmarkAgentSecondaryCertificate(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateAgentApi#unmarkAgentSecondaryCertificate");
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
| **id** | **String**| ID of certificate to remove. | |

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
| **204** | Successfully removed the certificate. |  -  |

