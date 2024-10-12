# CertificateApi

All URIs are relative to *https://cowin.gov.cin/cert/external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCertificatePdf**](CertificateApi.md#getCertificatePdf) | **POST** /pdf/certificate | Download the certificate in pdf format |


<a id="getCertificatePdf"></a>
# **getCertificatePdf**
> getCertificatePdf(body)

Download the certificate in pdf format

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
    defaultClient.setBasePath("https://cowin.gov.cin/cert/external");
    
    // Configure OAuth2 access token for authorization: cert_auth
    OAuth cert_auth = (OAuth) defaultClient.getAuthentication("cert_auth");
    cert_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateApi apiInstance = new CertificateApi(defaultClient);
    CertificateRequest body = new CertificateRequest(); // CertificateRequest | 
    try {
      apiInstance.getCertificatePdf(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateApi#getCertificatePdf");
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
| **body** | [**CertificateRequest**](CertificateRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[cert_auth](../README.md#cert_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad request |  -  |

