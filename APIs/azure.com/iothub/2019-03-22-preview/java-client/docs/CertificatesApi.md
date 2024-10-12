# CertificatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificatesCreateOrUpdate**](CertificatesApi.md#certificatesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName} | Upload the certificate to the IoT hub. |
| [**certificatesDelete**](CertificatesApi.md#certificatesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName} | Delete an X509 certificate. |
| [**certificatesGenerateVerificationCode**](CertificatesApi.md#certificatesGenerateVerificationCode) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/generateVerificationCode | Generate verification code for proof of possession flow. |
| [**certificatesGet**](CertificatesApi.md#certificatesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName} | Get the certificate. |
| [**certificatesListByIotHub**](CertificatesApi.md#certificatesListByIotHub) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates | Get the certificate list. |
| [**certificatesVerify**](CertificatesApi.md#certificatesVerify) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/certificates/{certificateName}/verify | Verify certificate&#39;s private key possession. |


<a id="certificatesCreateOrUpdate"></a>
# **certificatesCreateOrUpdate**
> CertificateDescription certificatesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, certificateDescription, ifMatch)

Upload the certificate to the IoT hub.

Adds new or replaces existing certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String certificateName = "certificateName_example"; // String | The name of the certificate
    CertificateBodyDescription certificateDescription = new CertificateBodyDescription(); // CertificateBodyDescription | The certificate body.
    String ifMatch = "ifMatch_example"; // String | ETag of the Certificate. Do not specify for creating a brand new certificate. Required to update an existing certificate.
    try {
      CertificateDescription result = apiInstance.certificatesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, certificateDescription, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesCreateOrUpdate");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |
| **certificateName** | **String**| The name of the certificate | |
| **certificateDescription** | [**CertificateBodyDescription**](CertificateBodyDescription.md)| The certificate body. | |
| **ifMatch** | **String**| ETag of the Certificate. Do not specify for creating a brand new certificate. Required to update an existing certificate. | [optional] |

### Return type

[**CertificateDescription**](CertificateDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If certificate already exist and update was successful, the operation returns HTTP status code of 201 (OK). |  -  |
| **201** | If certificate didn&#39;t exist creation was successful, the operation returns HTTP status code of 201 (OK). |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="certificatesDelete"></a>
# **certificatesDelete**
> certificatesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch)

Delete an X509 certificate.

Deletes an existing X509 certificate or does nothing if it does not exist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String certificateName = "certificateName_example"; // String | The name of the certificate
    String ifMatch = "ifMatch_example"; // String | ETag of the Certificate.
    try {
      apiInstance.certificatesDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesDelete");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |
| **certificateName** | **String**| The name of the certificate | |
| **ifMatch** | **String**| ETag of the Certificate. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Certificate has been deleted. |  -  |
| **204** | Certificate does not exist. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="certificatesGenerateVerificationCode"></a>
# **certificatesGenerateVerificationCode**
> CertificateWithNonceDescription certificatesGenerateVerificationCode(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch)

Generate verification code for proof of possession flow.

Generates verification code for proof of possession flow. The verification code will be used to generate a leaf certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String certificateName = "certificateName_example"; // String | The name of the certificate
    String ifMatch = "ifMatch_example"; // String | ETag of the Certificate.
    try {
      CertificateWithNonceDescription result = apiInstance.certificatesGenerateVerificationCode(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesGenerateVerificationCode");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |
| **certificateName** | **String**| The name of the certificate | |
| **ifMatch** | **String**| ETag of the Certificate. | |

### Return type

[**CertificateWithNonceDescription**](CertificateWithNonceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains the certificate. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="certificatesGet"></a>
# **certificatesGet**
> CertificateDescription certificatesGet(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName)

Get the certificate.

Returns the certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String certificateName = "certificateName_example"; // String | The name of the certificate
    try {
      CertificateDescription result = apiInstance.certificatesGet(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesGet");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |
| **certificateName** | **String**| The name of the certificate | |

### Return type

[**CertificateDescription**](CertificateDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains the certificate. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="certificatesListByIotHub"></a>
# **certificatesListByIotHub**
> CertificateListDescription certificatesListByIotHub(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the certificate list.

Returns the list of certificates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    try {
      CertificateListDescription result = apiInstance.certificatesListByIotHub(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesListByIotHub");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |

### Return type

[**CertificateListDescription**](CertificateListDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all the certificate list. |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="certificatesVerify"></a>
# **certificatesVerify**
> CertificateDescription certificatesVerify(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch, certificateVerificationBody)

Verify certificate&#39;s private key possession.

Verifies the certificate&#39;s private key possession by providing the leaf cert issued by the verifying pre uploaded certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificatesApi apiInstance = new CertificatesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
    String resourceName = "resourceName_example"; // String | The name of the IoT hub.
    String certificateName = "certificateName_example"; // String | The name of the certificate
    String ifMatch = "ifMatch_example"; // String | ETag of the Certificate.
    CertificateVerificationDescription certificateVerificationBody = new CertificateVerificationDescription(); // CertificateVerificationDescription | The name of the certificate
    try {
      CertificateDescription result = apiInstance.certificatesVerify(apiVersion, subscriptionId, resourceGroupName, resourceName, certificateName, ifMatch, certificateVerificationBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesVerify");
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
| **apiVersion** | **String**| The version of the API. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | |
| **resourceName** | **String**| The name of the IoT hub. | |
| **certificateName** | **String**| The name of the certificate | |
| **ifMatch** | **String**| ETag of the Certificate. | |
| **certificateVerificationBody** | [**CertificateVerificationDescription**](CertificateVerificationDescription.md)| The name of the certificate | |

### Return type

[**CertificateDescription**](CertificateDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains the certificate. |  -  |
| **0** | DefaultErrorResponse |  -  |

