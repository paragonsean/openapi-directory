# CertificateApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteCertificate**](CertificateApi.md#deleteCertificate) | **DELETE** /certificate/{id} | Delete imported certificate object |
| [**exportCertificate**](CertificateApi.md#exportCertificate) | **GET** /certificate/{id} | Get a certificate summary to export |
| [**importCertificate**](CertificateApi.md#importCertificate) | **POST** /certificate | Import a certificate |
| [**queryCertificates**](CertificateApi.md#queryCertificates) | **GET** /certificate | Get all certificates |
| [**updateCertificate**](CertificateApi.md#updateCertificate) | **PATCH** /certificate/{id} | Update a certificate entry |


<a id="deleteCertificate"></a>
# **deleteCertificate**
> deleteCertificate(id)

Delete imported certificate object

Deletes an imported certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

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

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String id = "id_example"; // String | The certificate ID.
    try {
      apiInstance.deleteCertificate(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#deleteCertificate");
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
| **id** | **String**| The certificate ID. | |

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

<a id="exportCertificate"></a>
# **exportCertificate**
> CertificateSummary exportCertificate(id)

Get a certificate summary to export

Get a certificate summary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

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

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String id = "id_example"; // String | ID of certificate to export.
    try {
      CertificateSummary result = apiInstance.exportCertificate(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#exportCertificate");
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
| **id** | **String**| ID of certificate to export. | |

### Return type

[**CertificateSummary**](CertificateSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the certificate to export. |  -  |

<a id="importCertificate"></a>
# **importCertificate**
> CertificateSummary importCertificate(certificateImportRequest)

Import a certificate

Import a certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

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

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    CertificateImportRequest certificateImportRequest = new CertificateImportRequest(); // CertificateImportRequest | Request to import a certificate.
    try {
      CertificateSummary result = apiInstance.importCertificate(certificateImportRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#importCertificate");
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
| **certificateImportRequest** | [**CertificateImportRequest**](CertificateImportRequest.md)| Request to import a certificate. | |

### Return type

[**CertificateSummary**](CertificateSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the certificate. |  -  |

<a id="queryCertificates"></a>
# **queryCertificates**
> CertificateSummaryListResponse queryCertificates(name, hasKey, description, expiration, includeExpired, sortBy, sortOrder)

Get all certificates

Get all certificates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

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

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String name = "name_example"; // String | Search by certificate name.
    Boolean hasKey = true; // Boolean | Search certificates by whether or not they contain a private key. 
    String description = "description_example"; // String | Search certificates by description.
    String expiration = "expiration_example"; // String | Search certificates by expiration.
    Boolean includeExpired = true; // Boolean | Specifies whether to include expired certificates. The default is false.
    String sortBy = "name"; // String | Attribute by which the list of certificates is sorted.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      CertificateSummaryListResponse result = apiInstance.queryCertificates(name, hasKey, description, expiration, includeExpired, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#queryCertificates");
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
| **name** | **String**| Search by certificate name. | [optional] |
| **hasKey** | **Boolean**| Search certificates by whether or not they contain a private key.  | [optional] |
| **description** | **String**| Search certificates by description. | [optional] |
| **expiration** | **String**| Search certificates by expiration. | [optional] |
| **includeExpired** | **Boolean**| Specifies whether to include expired certificates. The default is false. | [optional] |
| **sortBy** | **String**| Attribute by which the list of certificates is sorted. | [optional] [default to Name] [enum: name, description, hasKey, expiration] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**CertificateSummaryListResponse**](CertificateSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of certificates. |  -  |

<a id="updateCertificate"></a>
# **updateCertificate**
> CertificateSummary updateCertificate(id, certificatePatchRequest)

Update a certificate entry

Provide updated information for a certificate object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateApi;

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

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    String id = "id_example"; // String | ID of certificate object to update.
    CertificatePatchRequest certificatePatchRequest = new CertificatePatchRequest(); // CertificatePatchRequest | Patch request to update a certificate object.
    try {
      CertificateSummary result = apiInstance.updateCertificate(id, certificatePatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#updateCertificate");
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
| **id** | **String**| ID of certificate object to update. | |
| **certificatePatchRequest** | [**CertificatePatchRequest**](CertificatePatchRequest.md)| Patch request to update a certificate object. | |

### Return type

[**CertificateSummary**](CertificateSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated certificate object. |  -  |

