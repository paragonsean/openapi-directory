# CertificateOrdersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificateOrdersCreateOrUpdateCertificate**](CertificateOrdersApi.md#certificateOrdersCreateOrUpdateCertificate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready |
| [**certificateOrdersCreateOrUpdateCertificateOrder**](CertificateOrdersApi.md#certificateOrdersCreateOrUpdateCertificateOrder) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name} | Create or update a certificate purchase order |
| [**certificateOrdersDeleteCertificate**](CertificateOrdersApi.md#certificateOrdersDeleteCertificate) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Deletes the certificate associated with the certificate order |
| [**certificateOrdersDeleteCertificateOrder**](CertificateOrdersApi.md#certificateOrdersDeleteCertificateOrder) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name} | Delete an existing certificate order |
| [**certificateOrdersGetCertificate**](CertificateOrdersApi.md#certificateOrdersGetCertificate) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Get certificate associated with the certificate order |
| [**certificateOrdersGetCertificateOrder**](CertificateOrdersApi.md#certificateOrdersGetCertificateOrder) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name} | Get a certificate order |
| [**certificateOrdersGetCertificateOrders**](CertificateOrdersApi.md#certificateOrdersGetCertificateOrders) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders | Get certificate orders in a resource group |
| [**certificateOrdersGetCertificates**](CertificateOrdersApi.md#certificateOrdersGetCertificates) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates | List all certificates associated with a certificate order (only one certificate can be associated with an order at a time) |
| [**certificateOrdersReissueCertificateOrder**](CertificateOrdersApi.md#certificateOrdersReissueCertificateOrder) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/reissue | Reissue an existing certificate order |
| [**certificateOrdersRenewCertificateOrder**](CertificateOrdersApi.md#certificateOrdersRenewCertificateOrder) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/renew | Renew an existing certificate order |
| [**certificateOrdersResendCertificateEmail**](CertificateOrdersApi.md#certificateOrdersResendCertificateEmail) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/resendEmail | Resend certificate email |
| [**certificateOrdersRetrieveCertificateActions**](CertificateOrdersApi.md#certificateOrdersRetrieveCertificateActions) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveCertificateActions | Retrieve the list of certificate actions |
| [**certificateOrdersRetrieveCertificateEmailHistory**](CertificateOrdersApi.md#certificateOrdersRetrieveCertificateEmailHistory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveEmailHistory | Retrieve email history |
| [**certificateOrdersUpdateCertificate**](CertificateOrdersApi.md#certificateOrdersUpdateCertificate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready |
| [**certificateOrdersUpdateCertificateOrder**](CertificateOrdersApi.md#certificateOrdersUpdateCertificateOrder) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name} | Create or update a certificate purchase order |
| [**certificateOrdersVerifyDomainOwnership**](CertificateOrdersApi.md#certificateOrdersVerifyDomainOwnership) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/verifyDomainOwnership | Verify domain ownership for this certificate order |


<a id="certificateOrdersCreateOrUpdateCertificate"></a>
# **certificateOrdersCreateOrUpdateCertificate**
> CertificateOrderCertificate certificateOrdersCreateOrUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate)

Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String certificateOrderName = "certificateOrderName_example"; // String | Certificate name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CertificateOrderCertificate keyVaultCertificate = new CertificateOrderCertificate(); // CertificateOrderCertificate | Key Vault secret csm Id
    try {
      CertificateOrderCertificate result = apiInstance.certificateOrdersCreateOrUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersCreateOrUpdateCertificate");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **certificateOrderName** | **String**| Certificate name | |
| **name** | **String**| Certificate name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **keyVaultCertificate** | [**CertificateOrderCertificate**](CertificateOrderCertificate.md)| Key Vault secret csm Id | |

### Return type

[**CertificateOrderCertificate**](CertificateOrderCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersCreateOrUpdateCertificateOrder"></a>
# **certificateOrdersCreateOrUpdateCertificateOrder**
> CertificateOrder certificateOrdersCreateOrUpdateCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, certificateDistinguishedName)

Create or update a certificate purchase order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CertificateOrder certificateDistinguishedName = new CertificateOrder(); // CertificateOrder | Distinguished name to be used for purchasing certificate
    try {
      CertificateOrder result = apiInstance.certificateOrdersCreateOrUpdateCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, certificateDistinguishedName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersCreateOrUpdateCertificateOrder");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **certificateDistinguishedName** | [**CertificateOrder**](CertificateOrder.md)| Distinguished name to be used for purchasing certificate | |

### Return type

[**CertificateOrder**](CertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersDeleteCertificate"></a>
# **certificateOrdersDeleteCertificate**
> Object certificateOrdersDeleteCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion)

Deletes the certificate associated with the certificate order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String certificateOrderName = "certificateOrderName_example"; // String | Certificate name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.certificateOrdersDeleteCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersDeleteCertificate");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **certificateOrderName** | **String**| Certificate name | |
| **name** | **String**| Certificate name | |
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

<a id="certificateOrdersDeleteCertificateOrder"></a>
# **certificateOrdersDeleteCertificateOrder**
> Object certificateOrdersDeleteCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion)

Delete an existing certificate order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.certificateOrdersDeleteCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersDeleteCertificateOrder");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate name | |
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

<a id="certificateOrdersGetCertificate"></a>
# **certificateOrdersGetCertificate**
> CertificateOrderCertificate certificateOrdersGetCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion)

Get certificate associated with the certificate order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String certificateOrderName = "certificateOrderName_example"; // String | Certificate name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      CertificateOrderCertificate result = apiInstance.certificateOrdersGetCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersGetCertificate");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **certificateOrderName** | **String**| Certificate name | |
| **name** | **String**| Certificate name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**CertificateOrderCertificate**](CertificateOrderCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersGetCertificateOrder"></a>
# **certificateOrdersGetCertificateOrder**
> CertificateOrder certificateOrdersGetCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion)

Get a certificate order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      CertificateOrder result = apiInstance.certificateOrdersGetCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersGetCertificateOrder");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**CertificateOrder**](CertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersGetCertificateOrders"></a>
# **certificateOrdersGetCertificateOrders**
> CertificateOrderCollection certificateOrdersGetCertificateOrders(resourceGroupName, subscriptionId, apiVersion)

Get certificate orders in a resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      CertificateOrderCollection result = apiInstance.certificateOrdersGetCertificateOrders(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersGetCertificateOrders");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**CertificateOrderCollection**](CertificateOrderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersGetCertificates"></a>
# **certificateOrdersGetCertificates**
> CertificateOrderCertificateCollection certificateOrdersGetCertificates(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

List all certificates associated with a certificate order (only one certificate can be associated with an order at a time)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String certificateOrderName = "certificateOrderName_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      CertificateOrderCertificateCollection result = apiInstance.certificateOrdersGetCertificates(resourceGroupName, certificateOrderName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersGetCertificates");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **certificateOrderName** | **String**| Certificate name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**CertificateOrderCertificateCollection**](CertificateOrderCertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersReissueCertificateOrder"></a>
# **certificateOrdersReissueCertificateOrder**
> Object certificateOrdersReissueCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, reissueCertificateOrderRequest)

Reissue an existing certificate order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    ReissueCertificateOrderRequest reissueCertificateOrderRequest = new ReissueCertificateOrderRequest(); // ReissueCertificateOrderRequest | Reissue parameters
    try {
      Object result = apiInstance.certificateOrdersReissueCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, reissueCertificateOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersReissueCertificateOrder");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **reissueCertificateOrderRequest** | [**ReissueCertificateOrderRequest**](ReissueCertificateOrderRequest.md)| Reissue parameters | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersRenewCertificateOrder"></a>
# **certificateOrdersRenewCertificateOrder**
> Object certificateOrdersRenewCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, renewCertificateOrderRequest)

Renew an existing certificate order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    RenewCertificateOrderRequest renewCertificateOrderRequest = new RenewCertificateOrderRequest(); // RenewCertificateOrderRequest | Renew parameters
    try {
      Object result = apiInstance.certificateOrdersRenewCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, renewCertificateOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersRenewCertificateOrder");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **renewCertificateOrderRequest** | [**RenewCertificateOrderRequest**](RenewCertificateOrderRequest.md)| Renew parameters | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersResendCertificateEmail"></a>
# **certificateOrdersResendCertificateEmail**
> Object certificateOrdersResendCertificateEmail(resourceGroupName, name, subscriptionId, apiVersion)

Resend certificate email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate order name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.certificateOrdersResendCertificateEmail(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersResendCertificateEmail");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate order name | |
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

<a id="certificateOrdersRetrieveCertificateActions"></a>
# **certificateOrdersRetrieveCertificateActions**
> List&lt;CertificateOrderAction&gt; certificateOrdersRetrieveCertificateActions(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve the list of certificate actions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate order name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<CertificateOrderAction> result = apiInstance.certificateOrdersRetrieveCertificateActions(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersRetrieveCertificateActions");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate order name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;CertificateOrderAction&gt;**](CertificateOrderAction.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersRetrieveCertificateEmailHistory"></a>
# **certificateOrdersRetrieveCertificateEmailHistory**
> List&lt;CertificateEmail&gt; certificateOrdersRetrieveCertificateEmailHistory(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve email history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate order name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<CertificateEmail> result = apiInstance.certificateOrdersRetrieveCertificateEmailHistory(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersRetrieveCertificateEmailHistory");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate order name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;CertificateEmail&gt;**](CertificateEmail.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersUpdateCertificate"></a>
# **certificateOrdersUpdateCertificate**
> CertificateOrderCertificate certificateOrdersUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate)

Associates a Key Vault secret to a certificate store that will be used for storing the certificate once it&#39;s ready

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String certificateOrderName = "certificateOrderName_example"; // String | Certificate name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CertificateOrderCertificate keyVaultCertificate = new CertificateOrderCertificate(); // CertificateOrderCertificate | Key Vault secret csm Id
    try {
      CertificateOrderCertificate result = apiInstance.certificateOrdersUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersUpdateCertificate");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **certificateOrderName** | **String**| Certificate name | |
| **name** | **String**| Certificate name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **keyVaultCertificate** | [**CertificateOrderCertificate**](CertificateOrderCertificate.md)| Key Vault secret csm Id | |

### Return type

[**CertificateOrderCertificate**](CertificateOrderCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersUpdateCertificateOrder"></a>
# **certificateOrdersUpdateCertificateOrder**
> CertificateOrder certificateOrdersUpdateCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, certificateDistinguishedName)

Create or update a certificate purchase order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CertificateOrder certificateDistinguishedName = new CertificateOrder(); // CertificateOrder | Distinguished name to be used for purchasing certificate
    try {
      CertificateOrder result = apiInstance.certificateOrdersUpdateCertificateOrder(resourceGroupName, name, subscriptionId, apiVersion, certificateDistinguishedName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersUpdateCertificateOrder");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **certificateDistinguishedName** | [**CertificateOrder**](CertificateOrder.md)| Distinguished name to be used for purchasing certificate | |

### Return type

[**CertificateOrder**](CertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="certificateOrdersVerifyDomainOwnership"></a>
# **certificateOrdersVerifyDomainOwnership**
> Object certificateOrdersVerifyDomainOwnership(resourceGroupName, name, subscriptionId, apiVersion)

Verify domain ownership for this certificate order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateOrdersApi apiInstance = new CertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
    String name = "name_example"; // String | Certificate order name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.certificateOrdersVerifyDomainOwnership(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateOrdersApi#certificateOrdersVerifyDomainOwnership");
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
| **resourceGroupName** | **String**| Azure resource group name | |
| **name** | **String**| Certificate order name | |
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

