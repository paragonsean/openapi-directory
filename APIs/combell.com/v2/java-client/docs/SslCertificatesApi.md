# SslCertificatesApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadCertificate**](SslCertificatesApi.md#downloadCertificate) | **GET** /sslcertificates/{sha1Fingerprint}/download | Download a SSL certificate |
| [**getSslCertificate**](SslCertificatesApi.md#getSslCertificate) | **GET** /sslcertificates/{sha1Fingerprint} | Detail of a SSL certificate |
| [**getSslCertificates**](SslCertificatesApi.md#getSslCertificates) | **GET** /sslcertificates | Overview of SSL certificates |


<a id="downloadCertificate"></a>
# **downloadCertificate**
> File downloadCertificate(sha1Fingerprint, fileFormat, password, sha1Fingerprint2)

Download a SSL certificate

Returns the certifcate as binary data with the content-type and the filename information in the response headers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SslCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    SslCertificatesApi apiInstance = new SslCertificatesApi(defaultClient);
    String sha1Fingerprint = "sha1Fingerprint_example"; // String | The SHA-1 fingerprint of the certificate.
    SslCertificateFileFormat fileFormat = SslCertificateFileFormat.fromValue("pfx"); // SslCertificateFileFormat | The file format of the returned file stream:  <ul><li>PFX: Also known as PKCS #12, is a single, password protected certificate archive that contains the entire certificate chain plus the matching private key.</li></ul>
    String password = "password_example"; // String | The password used to protect the certificate file.<br />
    String sha1Fingerprint2 = "sha1Fingerprint_example"; // String | Automatically added
    try {
      File result = apiInstance.downloadCertificate(sha1Fingerprint, fileFormat, password, sha1Fingerprint2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SslCertificatesApi#downloadCertificate");
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
| **sha1Fingerprint** | **String**| The SHA-1 fingerprint of the certificate. | |
| **fileFormat** | [**SslCertificateFileFormat**](.md)| The file format of the returned file stream:  &lt;ul&gt;&lt;li&gt;PFX: Also known as PKCS #12, is a single, password protected certificate archive that contains the entire certificate chain plus the matching private key.&lt;/li&gt;&lt;/ul&gt; | [enum: pfx] |
| **password** | **String**| The password used to protect the certificate file.&lt;br /&gt; | |
| **sha1Fingerprint2** | **String**| Automatically added | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid file_format or invalid password |  -  |

<a id="getSslCertificate"></a>
# **getSslCertificate**
> SslCertificateDetail getSslCertificate(sha1Fingerprint, sha1Fingerprint2)

Detail of a SSL certificate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SslCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    SslCertificatesApi apiInstance = new SslCertificatesApi(defaultClient);
    String sha1Fingerprint = "sha1Fingerprint_example"; // String | The SHA-1 fingerprint of the certificate.
    String sha1Fingerprint2 = "sha1Fingerprint_example"; // String | Automatically added
    try {
      SslCertificateDetail result = apiInstance.getSslCertificate(sha1Fingerprint, sha1Fingerprint2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SslCertificatesApi#getSslCertificate");
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
| **sha1Fingerprint** | **String**| The SHA-1 fingerprint of the certificate. | |
| **sha1Fingerprint2** | **String**| Automatically added | |

### Return type

[**SslCertificateDetail**](SslCertificateDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getSslCertificates"></a>
# **getSslCertificates**
> List&lt;SslCertificate&gt; getSslCertificates(skip, take)

Overview of SSL certificates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SslCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    SslCertificatesApi apiInstance = new SslCertificatesApi(defaultClient);
    Integer skip = 56; // Integer | The number of items to skip in the resultset.
    Integer take = 56; // Integer | The number of items to return in the resultset. The returned count can be equal or less than this number.
    try {
      List<SslCertificate> result = apiInstance.getSslCertificates(skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SslCertificatesApi#getSslCertificates");
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
| **skip** | **Integer**| The number of items to skip in the resultset. | [optional] |
| **take** | **Integer**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] |

### Return type

[**List&lt;SslCertificate&gt;**](SslCertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  |

