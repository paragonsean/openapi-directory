# CertificatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificatesCreateOrUpdateCertificate**](CertificatesApi.md#certificatesCreateOrUpdateCertificate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Creates or modifies an existing certificate. |
| [**certificatesCreateOrUpdateCsr**](CertificatesApi.md#certificatesCreateOrUpdateCsr) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs/{name} | Creates or modifies an existing certificate signing request. |
| [**certificatesDeleteCertificate**](CertificatesApi.md#certificatesDeleteCertificate) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Delete a certificate by name in a specified subscription and resourcegroup. |
| [**certificatesDeleteCsr**](CertificatesApi.md#certificatesDeleteCsr) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs/{name} | Delete the certificate signing request. |
| [**certificatesGetCertificate**](CertificatesApi.md#certificatesGetCertificate) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Get a certificate by certificate name for a subscription in the specified resource group. |
| [**certificatesGetCertificates**](CertificatesApi.md#certificatesGetCertificates) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates | Get certificates for a subscription in the specified resource group. |
| [**certificatesGetCsr**](CertificatesApi.md#certificatesGetCsr) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs/{name} | Gets a certificate signing request by certificate name for a subscription in the specified resource group |
| [**certificatesGetCsrs**](CertificatesApi.md#certificatesGetCsrs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs | Gets the certificate signing requests for a subscription in the specified resource group |
| [**certificatesUpdateCertificate**](CertificatesApi.md#certificatesUpdateCertificate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/certificates/{name} | Creates or modifies an existing certificate. |
| [**certificatesUpdateCsr**](CertificatesApi.md#certificatesUpdateCsr) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/csrs/{name} | Creates or modifies an existing certificate signing request. |


<a id="certificatesCreateOrUpdateCertificate"></a>
# **certificatesCreateOrUpdateCertificate**
> Certificate certificatesCreateOrUpdateCertificate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope)

Creates or modifies an existing certificate.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Certificate certificateEnvelope = new Certificate(); // Certificate | Details of certificate if it exists already.
    try {
      Certificate result = apiInstance.certificatesCreateOrUpdateCertificate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesCreateOrUpdateCertificate");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **certificateEnvelope** | [**Certificate**](Certificate.md)| Details of certificate if it exists already. | |

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesCreateOrUpdateCsr"></a>
# **certificatesCreateOrUpdateCsr**
> Csr certificatesCreateOrUpdateCsr(resourceGroupName, name, subscriptionId, apiVersion, csrEnvelope)

Creates or modifies an existing certificate signing request.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Csr csrEnvelope = new Csr(); // Csr | Details of certificate signing request if it exists already.
    try {
      Csr result = apiInstance.certificatesCreateOrUpdateCsr(resourceGroupName, name, subscriptionId, apiVersion, csrEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesCreateOrUpdateCsr");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **csrEnvelope** | [**Csr**](Csr.md)| Details of certificate signing request if it exists already. | |

### Return type

[**Csr**](Csr.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesDeleteCertificate"></a>
# **certificatesDeleteCertificate**
> Object certificatesDeleteCertificate(resourceGroupName, name, subscriptionId, apiVersion)

Delete a certificate by name in a specified subscription and resourcegroup.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the certificate to be deleted.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.certificatesDeleteCertificate(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesDeleteCertificate");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the certificate to be deleted. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesDeleteCsr"></a>
# **certificatesDeleteCsr**
> Object certificatesDeleteCsr(resourceGroupName, name, subscriptionId, apiVersion)

Delete the certificate signing request.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the certificate signing request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.certificatesDeleteCsr(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesDeleteCsr");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the certificate signing request. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesGetCertificate"></a>
# **certificatesGetCertificate**
> Certificate certificatesGetCertificate(resourceGroupName, name, subscriptionId, apiVersion)

Get a certificate by certificate name for a subscription in the specified resource group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Certificate result = apiInstance.certificatesGetCertificate(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesGetCertificate");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesGetCertificates"></a>
# **certificatesGetCertificates**
> CertificateCollection certificatesGetCertificates(resourceGroupName, subscriptionId, apiVersion)

Get certificates for a subscription in the specified resource group.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      CertificateCollection result = apiInstance.certificatesGetCertificates(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesGetCertificates");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**CertificateCollection**](CertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesGetCsr"></a>
# **certificatesGetCsr**
> Csr certificatesGetCsr(resourceGroupName, name, subscriptionId, apiVersion)

Gets a certificate signing request by certificate name for a subscription in the specified resource group

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Csr result = apiInstance.certificatesGetCsr(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesGetCsr");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**Csr**](Csr.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesGetCsrs"></a>
# **certificatesGetCsrs**
> List&lt;Csr&gt; certificatesGetCsrs(resourceGroupName, subscriptionId, apiVersion)

Gets the certificate signing requests for a subscription in the specified resource group

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<Csr> result = apiInstance.certificatesGetCsrs(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesGetCsrs");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;Csr&gt;**](Csr.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesUpdateCertificate"></a>
# **certificatesUpdateCertificate**
> Certificate certificatesUpdateCertificate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope)

Creates or modifies an existing certificate.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Certificate certificateEnvelope = new Certificate(); // Certificate | Details of certificate if it exists already.
    try {
      Certificate result = apiInstance.certificatesUpdateCertificate(resourceGroupName, name, subscriptionId, apiVersion, certificateEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesUpdateCertificate");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **certificateEnvelope** | [**Certificate**](Certificate.md)| Details of certificate if it exists already. | |

### Return type

[**Certificate**](Certificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificatesUpdateCsr"></a>
# **certificatesUpdateCsr**
> Csr certificatesUpdateCsr(resourceGroupName, name, subscriptionId, apiVersion, csrEnvelope)

Creates or modifies an existing certificate signing request.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Csr csrEnvelope = new Csr(); // Csr | Details of certificate signing request if it exists already.
    try {
      Csr result = apiInstance.certificatesUpdateCsr(resourceGroupName, name, subscriptionId, apiVersion, csrEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificatesApi#certificatesUpdateCsr");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **csrEnvelope** | [**Csr**](Csr.md)| Details of certificate signing request if it exists already. | |

### Return type

[**Csr**](Csr.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

