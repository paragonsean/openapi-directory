# DeletedCertificatesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeletedCertificate**](DeletedCertificatesApi.md#getDeletedCertificate) | **GET** /deletedcertificates/{certificate-name} | Retrieves information about the specified deleted certificate. |
| [**getDeletedCertificates**](DeletedCertificatesApi.md#getDeletedCertificates) | **GET** /deletedcertificates | Lists the deleted certificates in the specified vault currently available for recovery. |
| [**purgeDeletedCertificate**](DeletedCertificatesApi.md#purgeDeletedCertificate) | **DELETE** /deletedcertificates/{certificate-name} | Permanently deletes the specified deleted certificate. |
| [**recoverDeletedCertificate**](DeletedCertificatesApi.md#recoverDeletedCertificate) | **POST** /deletedcertificates/{certificate-name}/recover | Recovers the deleted certificate back to its current version under /certificates. |


<a id="getDeletedCertificate"></a>
# **getDeletedCertificate**
> DeletedCertificateBundle getDeletedCertificate(certificateName, apiVersion)

Retrieves information about the specified deleted certificate.

The GetDeletedCertificate operation retrieves the deleted certificate information plus its attributes, such as retention interval, scheduled permanent deletion and the current deletion recovery level. This operation requires the certificates/get permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedCertificatesApi apiInstance = new DeletedCertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedCertificateBundle result = apiInstance.getDeletedCertificate(certificateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedCertificatesApi#getDeletedCertificate");
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
| **certificateName** | **String**| The name of the certificate | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**DeletedCertificateBundle**](DeletedCertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Certificate bundle of the certificate and its attributes |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getDeletedCertificates"></a>
# **getDeletedCertificates**
> DeletedCertificateListResult getDeletedCertificates(apiVersion, maxresults, includePending)

Lists the deleted certificates in the specified vault currently available for recovery.

The GetDeletedCertificates operation retrieves the certificates in the current vault which are in a deleted state and ready for recovery or purging. This operation includes deletion-specific information. This operation requires the certificates/get/list permission. This operation can only be enabled on soft-delete enabled vaults.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedCertificatesApi apiInstance = new DeletedCertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    Boolean includePending = true; // Boolean | Specifies whether to include certificates which are not completely provisioned.
    try {
      DeletedCertificateListResult result = apiInstance.getDeletedCertificates(apiVersion, maxresults, includePending);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedCertificatesApi#getDeletedCertificates");
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
| **apiVersion** | **String**| Client API version. | |
| **maxresults** | **Integer**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] |
| **includePending** | **Boolean**| Specifies whether to include certificates which are not completely provisioned. | [optional] |

### Return type

[**DeletedCertificateListResult**](DeletedCertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of deleted certificates in the vault along with a link to the next page of deleted certificates |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="purgeDeletedCertificate"></a>
# **purgeDeletedCertificate**
> purgeDeletedCertificate(certificateName, apiVersion)

Permanently deletes the specified deleted certificate.

The PurgeDeletedCertificate operation performs an irreversible deletion of the specified certificate, without possibility for recovery. The operation is not available if the recovery level does not specify &#39;Purgeable&#39;. This operation requires the certificate/purge permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedCertificatesApi apiInstance = new DeletedCertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.purgeDeletedCertificate(certificateName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedCertificatesApi#purgeDeletedCertificate");
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
| **certificateName** | **String**| The name of the certificate | |
| **apiVersion** | **String**| Client API version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content signaling that the certificate was purged forever. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="recoverDeletedCertificate"></a>
# **recoverDeletedCertificate**
> CertificateBundle recoverDeletedCertificate(certificateName, apiVersion)

Recovers the deleted certificate back to its current version under /certificates.

The RecoverDeletedCertificate operation performs the reversal of the Delete operation. The operation is applicable in vaults enabled for soft-delete, and must be issued during the retention interval (available in the deleted certificate&#39;s attributes). This operation requires the certificates/recover permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeletedCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    DeletedCertificatesApi apiInstance = new DeletedCertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the deleted certificate
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      CertificateBundle result = apiInstance.recoverDeletedCertificate(certificateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeletedCertificatesApi#recoverDeletedCertificate");
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
| **certificateName** | **String**| The name of the deleted certificate | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Certificate bundle of the original certificate and its attributes |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

