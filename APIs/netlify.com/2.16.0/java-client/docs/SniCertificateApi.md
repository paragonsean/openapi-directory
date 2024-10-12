# SniCertificateApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**provisionSiteTLSCertificate**](SniCertificateApi.md#provisionSiteTLSCertificate) | **POST** /sites/{site_id}/ssl |  |
| [**showSiteTLSCertificate**](SniCertificateApi.md#showSiteTLSCertificate) | **GET** /sites/{site_id}/ssl |  |


<a id="provisionSiteTLSCertificate"></a>
# **provisionSiteTLSCertificate**
> SniCertificate provisionSiteTLSCertificate(siteId, certificate, key, caCertificates)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SniCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SniCertificateApi apiInstance = new SniCertificateApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String certificate = "certificate_example"; // String | 
    String key = "key_example"; // String | 
    String caCertificates = "caCertificates_example"; // String | 
    try {
      SniCertificate result = apiInstance.provisionSiteTLSCertificate(siteId, certificate, key, caCertificates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SniCertificateApi#provisionSiteTLSCertificate");
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
| **siteId** | **String**|  | |
| **certificate** | **String**|  | [optional] |
| **key** | **String**|  | [optional] |
| **caCertificates** | **String**|  | [optional] |

### Return type

[**SniCertificate**](SniCertificate.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="showSiteTLSCertificate"></a>
# **showSiteTLSCertificate**
> SniCertificate showSiteTLSCertificate(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SniCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    SniCertificateApi apiInstance = new SniCertificateApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      SniCertificate result = apiInstance.showSiteTLSCertificate(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SniCertificateApi#showSiteTLSCertificate");
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
| **siteId** | **String**|  | |

### Return type

[**SniCertificate**](SniCertificate.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

