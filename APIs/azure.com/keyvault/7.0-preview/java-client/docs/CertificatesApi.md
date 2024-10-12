# CertificatesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupCertificate**](CertificatesApi.md#backupCertificate) | **POST** /certificates/{certificate-name}/backup | Backs up the specified certificate. |
| [**createCertificate**](CertificatesApi.md#createCertificate) | **POST** /certificates/{certificate-name}/create | Creates a new certificate. |
| [**deleteCertificate**](CertificatesApi.md#deleteCertificate) | **DELETE** /certificates/{certificate-name} | Deletes a certificate from a specified key vault. |
| [**deleteCertificateContacts**](CertificatesApi.md#deleteCertificateContacts) | **DELETE** /certificates/contacts | Deletes the certificate contacts for a specified key vault. |
| [**deleteCertificateIssuer**](CertificatesApi.md#deleteCertificateIssuer) | **DELETE** /certificates/issuers/{issuer-name} | Deletes the specified certificate issuer. |
| [**deleteCertificateOperation**](CertificatesApi.md#deleteCertificateOperation) | **DELETE** /certificates/{certificate-name}/pending | Deletes the creation operation for a specific certificate. |
| [**getCertificate**](CertificatesApi.md#getCertificate) | **GET** /certificates/{certificate-name}/{certificate-version} | Gets information about a certificate. |
| [**getCertificateContacts**](CertificatesApi.md#getCertificateContacts) | **GET** /certificates/contacts | Lists the certificate contacts for a specified key vault. |
| [**getCertificateIssuer**](CertificatesApi.md#getCertificateIssuer) | **GET** /certificates/issuers/{issuer-name} | Lists the specified certificate issuer. |
| [**getCertificateIssuers**](CertificatesApi.md#getCertificateIssuers) | **GET** /certificates/issuers | List certificate issuers for a specified key vault. |
| [**getCertificateOperation**](CertificatesApi.md#getCertificateOperation) | **GET** /certificates/{certificate-name}/pending | Gets the creation operation of a certificate. |
| [**getCertificatePolicy**](CertificatesApi.md#getCertificatePolicy) | **GET** /certificates/{certificate-name}/policy | Lists the policy for a certificate. |
| [**getCertificateVersions**](CertificatesApi.md#getCertificateVersions) | **GET** /certificates/{certificate-name}/versions | List the versions of a certificate. |
| [**getCertificates**](CertificatesApi.md#getCertificates) | **GET** /certificates | List certificates in a specified key vault |
| [**importCertificate**](CertificatesApi.md#importCertificate) | **POST** /certificates/{certificate-name}/import | Imports a certificate into a specified key vault. |
| [**mergeCertificate**](CertificatesApi.md#mergeCertificate) | **POST** /certificates/{certificate-name}/pending/merge | Merges a certificate or a certificate chain with a key pair existing on the server. |
| [**restoreCertificate**](CertificatesApi.md#restoreCertificate) | **POST** /certificates/restore | Restores a backed up certificate to a vault. |
| [**setCertificateContacts**](CertificatesApi.md#setCertificateContacts) | **PUT** /certificates/contacts | Sets the certificate contacts for the specified key vault. |
| [**setCertificateIssuer**](CertificatesApi.md#setCertificateIssuer) | **PUT** /certificates/issuers/{issuer-name} | Sets the specified certificate issuer. |
| [**updateCertificate**](CertificatesApi.md#updateCertificate) | **PATCH** /certificates/{certificate-name}/{certificate-version} | Updates the specified attributes associated with the given certificate. |
| [**updateCertificateIssuer**](CertificatesApi.md#updateCertificateIssuer) | **PATCH** /certificates/issuers/{issuer-name} | Updates the specified certificate issuer. |
| [**updateCertificateOperation**](CertificatesApi.md#updateCertificateOperation) | **PATCH** /certificates/{certificate-name}/pending | Updates a certificate operation. |
| [**updateCertificatePolicy**](CertificatesApi.md#updateCertificatePolicy) | **PATCH** /certificates/{certificate-name}/policy | Updates the policy for a certificate. |


<a id="backupCertificate"></a>
# **backupCertificate**
> BackupCertificateResult backupCertificate(certificateName, apiVersion)

Backs up the specified certificate.

Requests that a backup of the specified certificate be downloaded to the client. All versions of the certificate will be downloaded. This operation requires the certificates/backup permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      BackupCertificateResult result = apiInstance.backupCertificate(certificateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#backupCertificate");
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
| **certificateName** | **String**| The name of the certificate. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**BackupCertificateResult**](BackupCertificateResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The backup blob containing the backed up certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="createCertificate"></a>
# **createCertificate**
> CertificateOperation createCertificate(certificateName, apiVersion, parameters)

Creates a new certificate.

If this is the first version, the certificate resource is created. This operation requires the certificates/create permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CertificateCreateParameters parameters = new CertificateCreateParameters(); // CertificateCreateParameters | The parameters to create a certificate.
    try {
      CertificateOperation result = apiInstance.createCertificate(certificateName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#createCertificate");
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
| **certificateName** | **String**| The name of the certificate. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**CertificateCreateParameters**](CertificateCreateParameters.md)| The parameters to create a certificate. | |

### Return type

[**CertificateOperation**](CertificateOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Created certificate bundle. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="deleteCertificate"></a>
# **deleteCertificate**
> DeletedCertificateBundle deleteCertificate(certificateName, apiVersion)

Deletes a certificate from a specified key vault.

Deletes all versions of a certificate object along with its associated policy. Delete certificate cannot be used to remove individual versions of a certificate object. This operation requires the certificates/delete permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      DeletedCertificateBundle result = apiInstance.deleteCertificate(certificateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#deleteCertificate");
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
| **certificateName** | **String**| The name of the certificate. | |
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
| **200** | The deleted certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="deleteCertificateContacts"></a>
# **deleteCertificateContacts**
> Contacts deleteCertificateContacts(apiVersion)

Deletes the certificate contacts for a specified key vault.

Deletes the certificate contacts for a specified key vault certificate. This operation requires the certificates/managecontacts permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      Contacts result = apiInstance.deleteCertificateContacts(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#deleteCertificateContacts");
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

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contacts for the key vault certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="deleteCertificateIssuer"></a>
# **deleteCertificateIssuer**
> IssuerBundle deleteCertificateIssuer(issuerName, apiVersion)

Deletes the specified certificate issuer.

The DeleteCertificateIssuer operation permanently removes the specified certificate issuer from the vault. This operation requires the certificates/manageissuers/deleteissuers permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String issuerName = "issuerName_example"; // String | The name of the issuer.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      IssuerBundle result = apiInstance.deleteCertificateIssuer(issuerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#deleteCertificateIssuer");
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
| **issuerName** | **String**| The name of the issuer. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**IssuerBundle**](IssuerBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The issuer for the key vault certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="deleteCertificateOperation"></a>
# **deleteCertificateOperation**
> CertificateOperation deleteCertificateOperation(certificateName, apiVersion)

Deletes the creation operation for a specific certificate.

Deletes the creation operation for a specified certificate that is in the process of being created. The certificate is no longer created. This operation requires the certificates/update permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      CertificateOperation result = apiInstance.deleteCertificateOperation(certificateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#deleteCertificateOperation");
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
| **certificateName** | **String**| The name of the certificate. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**CertificateOperation**](CertificateOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A message containing the certificate operation response. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getCertificate"></a>
# **getCertificate**
> CertificateBundle getCertificate(certificateName, certificateVersion, apiVersion)

Gets information about a certificate.

Gets information about a specific certificate. This operation requires the certificates/get permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate in the given vault.
    String certificateVersion = "certificateVersion_example"; // String | The version of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      CertificateBundle result = apiInstance.getCertificate(certificateName, certificateVersion, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#getCertificate");
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
| **certificateName** | **String**| The name of the certificate in the given vault. | |
| **certificateVersion** | **String**| The version of the certificate. | |
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
| **200** | The retrieved certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getCertificateContacts"></a>
# **getCertificateContacts**
> Contacts getCertificateContacts(apiVersion)

Lists the certificate contacts for a specified key vault.

The GetCertificateContacts operation returns the set of certificate contact resources in the specified key vault. This operation requires the certificates/managecontacts permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      Contacts result = apiInstance.getCertificateContacts(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#getCertificateContacts");
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

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contacts for the key vault certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getCertificateIssuer"></a>
# **getCertificateIssuer**
> IssuerBundle getCertificateIssuer(issuerName, apiVersion)

Lists the specified certificate issuer.

The GetCertificateIssuer operation returns the specified certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String issuerName = "issuerName_example"; // String | The name of the issuer.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      IssuerBundle result = apiInstance.getCertificateIssuer(issuerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#getCertificateIssuer");
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
| **issuerName** | **String**| The name of the issuer. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**IssuerBundle**](IssuerBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The issuer for the key vault certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getCertificateIssuers"></a>
# **getCertificateIssuers**
> CertificateIssuerListResult getCertificateIssuers(apiVersion, maxresults)

List certificate issuers for a specified key vault.

The GetCertificateIssuers operation returns the set of certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      CertificateIssuerListResult result = apiInstance.getCertificateIssuers(apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#getCertificateIssuers");
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

### Return type

[**CertificateIssuerListResult**](CertificateIssuerListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of certificate issuers in a key vault along with a link to the next page of certificate issuers. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getCertificateOperation"></a>
# **getCertificateOperation**
> CertificateOperation getCertificateOperation(certificateName, apiVersion)

Gets the creation operation of a certificate.

Gets the creation operation associated with a specified certificate. This operation requires the certificates/get permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      CertificateOperation result = apiInstance.getCertificateOperation(certificateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#getCertificateOperation");
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
| **certificateName** | **String**| The name of the certificate. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**CertificateOperation**](CertificateOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The certificate operation response. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getCertificatePolicy"></a>
# **getCertificatePolicy**
> CertificatePolicy getCertificatePolicy(certificateName, apiVersion)

Lists the policy for a certificate.

The GetCertificatePolicy operation returns the specified certificate policy resources in the specified key vault. This operation requires the certificates/get permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate in a given key vault.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      CertificatePolicy result = apiInstance.getCertificatePolicy(certificateName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#getCertificatePolicy");
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
| **certificateName** | **String**| The name of the certificate in a given key vault. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**CertificatePolicy**](CertificatePolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The certificate policy. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getCertificateVersions"></a>
# **getCertificateVersions**
> CertificateListResult getCertificateVersions(certificateName, apiVersion, maxresults)

List the versions of a certificate.

The GetCertificateVersions operation returns the versions of a certificate in the specified key vault. This operation requires the certificates/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    try {
      CertificateListResult result = apiInstance.getCertificateVersions(certificateName, apiVersion, maxresults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#getCertificateVersions");
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
| **certificateName** | **String**| The name of the certificate. | |
| **apiVersion** | **String**| Client API version. | |
| **maxresults** | **Integer**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] |

### Return type

[**CertificateListResult**](CertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of certificates in the key vault along with a link to the next page of keys. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="getCertificates"></a>
# **getCertificates**
> CertificateListResult getCertificates(apiVersion, maxresults, includePending)

List certificates in a specified key vault

The GetCertificates operation returns the set of certificates resources in the specified key vault. This operation requires the certificates/list permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Integer maxresults = 56; // Integer | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    Boolean includePending = true; // Boolean | Specifies whether to include certificates which are not completely provisioned.
    try {
      CertificateListResult result = apiInstance.getCertificates(apiVersion, maxresults, includePending);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#getCertificates");
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

[**CertificateListResult**](CertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response message containing a list of certificates along with a link to the next page of certificates. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="importCertificate"></a>
# **importCertificate**
> CertificateBundle importCertificate(certificateName, apiVersion, parameters)

Imports a certificate into a specified key vault.

Imports an existing valid certificate, containing a private key, into Azure Key Vault. The certificate to be imported can be in either PFX or PEM format. If the certificate is in PEM format the PEM file must contain the key as well as x509 certificates. This operation requires the certificates/import permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CertificateImportParameters parameters = new CertificateImportParameters(); // CertificateImportParameters | The parameters to import the certificate.
    try {
      CertificateBundle result = apiInstance.importCertificate(certificateName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#importCertificate");
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
| **certificateName** | **String**| The name of the certificate. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**CertificateImportParameters**](CertificateImportParameters.md)| The parameters to import the certificate. | |

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Imported certificate bundle to the vault. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="mergeCertificate"></a>
# **mergeCertificate**
> CertificateBundle mergeCertificate(certificateName, apiVersion, parameters)

Merges a certificate or a certificate chain with a key pair existing on the server.

The MergeCertificate operation performs the merging of a certificate or certificate chain with a key pair currently available in the service. This operation requires the certificates/create permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CertificateMergeParameters parameters = new CertificateMergeParameters(); // CertificateMergeParameters | The parameters to merge certificate.
    try {
      CertificateBundle result = apiInstance.mergeCertificate(certificateName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#mergeCertificate");
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
| **certificateName** | **String**| The name of the certificate. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**CertificateMergeParameters**](CertificateMergeParameters.md)| The parameters to merge certificate. | |

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Merged certificate bundle to the vault. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="restoreCertificate"></a>
# **restoreCertificate**
> CertificateBundle restoreCertificate(apiVersion, parameters)

Restores a backed up certificate to a vault.

Restores a backed up certificate, and all its versions, to a vault. This operation requires the certificates/restore permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CertificateRestoreParameters parameters = new CertificateRestoreParameters(); // CertificateRestoreParameters | The parameters to restore the certificate.
    try {
      CertificateBundle result = apiInstance.restoreCertificate(apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#restoreCertificate");
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
| **parameters** | [**CertificateRestoreParameters**](CertificateRestoreParameters.md)| The parameters to restore the certificate. | |

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Restored certificate bundle in the vault. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="setCertificateContacts"></a>
# **setCertificateContacts**
> Contacts setCertificateContacts(apiVersion, contacts)

Sets the certificate contacts for the specified key vault.

Sets the certificate contacts for the specified key vault. This operation requires the certificates/managecontacts permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    Contacts contacts = new Contacts(); // Contacts | The contacts for the key vault certificate.
    try {
      Contacts result = apiInstance.setCertificateContacts(apiVersion, contacts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#setCertificateContacts");
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
| **contacts** | [**Contacts**](Contacts.md)| The contacts for the key vault certificate. | |

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contacts for the key vault certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="setCertificateIssuer"></a>
# **setCertificateIssuer**
> IssuerBundle setCertificateIssuer(issuerName, apiVersion, parameter)

Sets the specified certificate issuer.

The SetCertificateIssuer operation adds or updates the specified certificate issuer. This operation requires the certificates/setissuers permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String issuerName = "issuerName_example"; // String | The name of the issuer.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CertificateIssuerSetParameters parameter = new CertificateIssuerSetParameters(); // CertificateIssuerSetParameters | Certificate issuer set parameter.
    try {
      IssuerBundle result = apiInstance.setCertificateIssuer(issuerName, apiVersion, parameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#setCertificateIssuer");
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
| **issuerName** | **String**| The name of the issuer. | |
| **apiVersion** | **String**| Client API version. | |
| **parameter** | [**CertificateIssuerSetParameters**](CertificateIssuerSetParameters.md)| Certificate issuer set parameter. | |

### Return type

[**IssuerBundle**](IssuerBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The issuer for the key vault certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="updateCertificate"></a>
# **updateCertificate**
> CertificateBundle updateCertificate(certificateName, certificateVersion, apiVersion, parameters)

Updates the specified attributes associated with the given certificate.

The UpdateCertificate operation applies the specified update on the given certificate; the only elements updated are the certificate&#39;s attributes. This operation requires the certificates/update permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate in the given key vault.
    String certificateVersion = "certificateVersion_example"; // String | The version of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CertificateUpdateParameters parameters = new CertificateUpdateParameters(); // CertificateUpdateParameters | The parameters for certificate update.
    try {
      CertificateBundle result = apiInstance.updateCertificate(certificateName, certificateVersion, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#updateCertificate");
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
| **certificateName** | **String**| The name of the certificate in the given key vault. | |
| **certificateVersion** | **String**| The version of the certificate. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**CertificateUpdateParameters**](CertificateUpdateParameters.md)| The parameters for certificate update. | |

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="updateCertificateIssuer"></a>
# **updateCertificateIssuer**
> IssuerBundle updateCertificateIssuer(issuerName, apiVersion, parameter)

Updates the specified certificate issuer.

The UpdateCertificateIssuer operation performs an update on the specified certificate issuer entity. This operation requires the certificates/setissuers permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String issuerName = "issuerName_example"; // String | The name of the issuer.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CertificateIssuerUpdateParameters parameter = new CertificateIssuerUpdateParameters(); // CertificateIssuerUpdateParameters | Certificate issuer update parameter.
    try {
      IssuerBundle result = apiInstance.updateCertificateIssuer(issuerName, apiVersion, parameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#updateCertificateIssuer");
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
| **issuerName** | **String**| The name of the issuer. | |
| **apiVersion** | **String**| Client API version. | |
| **parameter** | [**CertificateIssuerUpdateParameters**](CertificateIssuerUpdateParameters.md)| Certificate issuer update parameter. | |

### Return type

[**IssuerBundle**](IssuerBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The issuer for the key vault certificate. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="updateCertificateOperation"></a>
# **updateCertificateOperation**
> CertificateOperation updateCertificateOperation(certificateName, apiVersion, certificateOperation)

Updates a certificate operation.

Updates a certificate creation operation that is already in progress. This operation requires the certificates/update permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CertificateOperationUpdateParameter certificateOperation = new CertificateOperationUpdateParameter(); // CertificateOperationUpdateParameter | The certificate operation response.
    try {
      CertificateOperation result = apiInstance.updateCertificateOperation(certificateName, apiVersion, certificateOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#updateCertificateOperation");
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
| **certificateName** | **String**| The name of the certificate. | |
| **apiVersion** | **String**| Client API version. | |
| **certificateOperation** | [**CertificateOperationUpdateParameter**](CertificateOperationUpdateParameter.md)| The certificate operation response. | |

### Return type

[**CertificateOperation**](CertificateOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A message containing the certificate operation response. |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

<a id="updateCertificatePolicy"></a>
# **updateCertificatePolicy**
> CertificatePolicy updateCertificatePolicy(certificateName, apiVersion, certificatePolicy)

Updates the policy for a certificate.

Set specified members in the certificate policy. Leave others as null. This operation requires the certificates/update permission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The name of the certificate in the given vault.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CertificatePolicy certificatePolicy = new CertificatePolicy(); // CertificatePolicy | The policy for the certificate.
    try {
      CertificatePolicy result = apiInstance.updateCertificatePolicy(certificateName, apiVersion, certificatePolicy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#updateCertificatePolicy");
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
| **certificateName** | **String**| The name of the certificate in the given vault. | |
| **apiVersion** | **String**| Client API version. | |
| **certificatePolicy** | [**CertificatePolicy**](CertificatePolicy.md)| The policy for the certificate. | |

### Return type

[**CertificatePolicy**](CertificatePolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The certificate policy |  -  |
| **0** | Key Vault error response describing why the operation failed. |  -  |

