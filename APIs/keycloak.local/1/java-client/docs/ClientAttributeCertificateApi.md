# ClientAttributeCertificateApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmClientsIdCertificatesAttrDownloadPost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrDownloadPost) | **POST** /{realm}/clients/{id}/certificates/{attr}/download | Get a keystore file for the client, containing private key and public certificate |
| [**realmClientsIdCertificatesAttrGenerateAndDownloadPost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrGenerateAndDownloadPost) | **POST** /{realm}/clients/{id}/certificates/{attr}/generate-and-download | Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format. |
| [**realmClientsIdCertificatesAttrGeneratePost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrGeneratePost) | **POST** /{realm}/clients/{id}/certificates/{attr}/generate | Generate a new certificate with new key pair |
| [**realmClientsIdCertificatesAttrGet**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrGet) | **GET** /{realm}/clients/{id}/certificates/{attr} | Get key info |
| [**realmClientsIdCertificatesAttrUploadCertificatePost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrUploadCertificatePost) | **POST** /{realm}/clients/{id}/certificates/{attr}/upload-certificate | Upload only certificate, not private key |
| [**realmClientsIdCertificatesAttrUploadPost**](ClientAttributeCertificateApi.md#realmClientsIdCertificatesAttrUploadPost) | **POST** /{realm}/clients/{id}/certificates/{attr}/upload | Upload certificate and eventually private key |


<a id="realmClientsIdCertificatesAttrDownloadPost"></a>
# **realmClientsIdCertificatesAttrDownloadPost**
> byte[] realmClientsIdCertificatesAttrDownloadPost(realm, id, attr, keyStoreConfig)

Get a keystore file for the client, containing private key and public certificate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientAttributeCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientAttributeCertificateApi apiInstance = new ClientAttributeCertificateApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String attr = "attr_example"; // String | 
    KeyStoreConfig keyStoreConfig = new KeyStoreConfig(); // KeyStoreConfig | Keystore configuration as JSON
    try {
      byte[] result = apiInstance.realmClientsIdCertificatesAttrDownloadPost(realm, id, attr, keyStoreConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientAttributeCertificateApi#realmClientsIdCertificatesAttrDownloadPost");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**| id of client (not client-id) | |
| **attr** | **String**|  | |
| **keyStoreConfig** | [**KeyStoreConfig**](KeyStoreConfig.md)| Keystore configuration as JSON | |

### Return type

**byte[]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdCertificatesAttrGenerateAndDownloadPost"></a>
# **realmClientsIdCertificatesAttrGenerateAndDownloadPost**
> byte[] realmClientsIdCertificatesAttrGenerateAndDownloadPost(realm, id, attr, keyStoreConfig)

Generate a new keypair and certificate, and get the private key file   Generates a keypair and certificate and serves the private key in a specified keystore format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientAttributeCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientAttributeCertificateApi apiInstance = new ClientAttributeCertificateApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String attr = "attr_example"; // String | 
    KeyStoreConfig keyStoreConfig = new KeyStoreConfig(); // KeyStoreConfig | Keystore configuration as JSON
    try {
      byte[] result = apiInstance.realmClientsIdCertificatesAttrGenerateAndDownloadPost(realm, id, attr, keyStoreConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientAttributeCertificateApi#realmClientsIdCertificatesAttrGenerateAndDownloadPost");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**| id of client (not client-id) | |
| **attr** | **String**|  | |
| **keyStoreConfig** | [**KeyStoreConfig**](KeyStoreConfig.md)| Keystore configuration as JSON | |

### Return type

**byte[]**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdCertificatesAttrGeneratePost"></a>
# **realmClientsIdCertificatesAttrGeneratePost**
> CertificateRepresentation realmClientsIdCertificatesAttrGeneratePost(realm, id, attr)

Generate a new certificate with new key pair

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientAttributeCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientAttributeCertificateApi apiInstance = new ClientAttributeCertificateApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String attr = "attr_example"; // String | 
    try {
      CertificateRepresentation result = apiInstance.realmClientsIdCertificatesAttrGeneratePost(realm, id, attr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientAttributeCertificateApi#realmClientsIdCertificatesAttrGeneratePost");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**| id of client (not client-id) | |
| **attr** | **String**|  | |

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdCertificatesAttrGet"></a>
# **realmClientsIdCertificatesAttrGet**
> CertificateRepresentation realmClientsIdCertificatesAttrGet(realm, id, attr)

Get key info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientAttributeCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientAttributeCertificateApi apiInstance = new ClientAttributeCertificateApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String attr = "attr_example"; // String | 
    try {
      CertificateRepresentation result = apiInstance.realmClientsIdCertificatesAttrGet(realm, id, attr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientAttributeCertificateApi#realmClientsIdCertificatesAttrGet");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**| id of client (not client-id) | |
| **attr** | **String**|  | |

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdCertificatesAttrUploadCertificatePost"></a>
# **realmClientsIdCertificatesAttrUploadCertificatePost**
> CertificateRepresentation realmClientsIdCertificatesAttrUploadCertificatePost(realm, id, attr)

Upload only certificate, not private key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientAttributeCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientAttributeCertificateApi apiInstance = new ClientAttributeCertificateApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String attr = "attr_example"; // String | 
    try {
      CertificateRepresentation result = apiInstance.realmClientsIdCertificatesAttrUploadCertificatePost(realm, id, attr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientAttributeCertificateApi#realmClientsIdCertificatesAttrUploadCertificatePost");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**| id of client (not client-id) | |
| **attr** | **String**|  | |

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdCertificatesAttrUploadPost"></a>
# **realmClientsIdCertificatesAttrUploadPost**
> CertificateRepresentation realmClientsIdCertificatesAttrUploadPost(realm, id, attr)

Upload certificate and eventually private key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientAttributeCertificateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientAttributeCertificateApi apiInstance = new ClientAttributeCertificateApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String attr = "attr_example"; // String | 
    try {
      CertificateRepresentation result = apiInstance.realmClientsIdCertificatesAttrUploadPost(realm, id, attr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientAttributeCertificateApi#realmClientsIdCertificatesAttrUploadPost");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**| id of client (not client-id) | |
| **attr** | **String**|  | |

### Return type

[**CertificateRepresentation**](CertificateRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

