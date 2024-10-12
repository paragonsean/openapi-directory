# AppServiceCertificateOrdersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appServiceCertificateOrdersCreateOrUpdate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName} | Create or update a certificate purchase order. |
| [**appServiceCertificateOrdersCreateOrUpdateCertificate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersCreateOrUpdateCertificate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Creates or updates a certificate and associates with key vault secret. |
| [**appServiceCertificateOrdersDelete**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName} | Delete an existing certificate order. |
| [**appServiceCertificateOrdersDeleteCertificate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersDeleteCertificate) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Delete the certificate associated with a certificate order. |
| [**appServiceCertificateOrdersGet**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName} | Get a certificate order. |
| [**appServiceCertificateOrdersGetCertificate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersGetCertificate) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Get the certificate associated with a certificate order. |
| [**appServiceCertificateOrdersList**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CertificateRegistration/certificateOrders | List all certificate orders in a subscription. |
| [**appServiceCertificateOrdersListByResourceGroup**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders | Get certificate orders in a resource group. |
| [**appServiceCertificateOrdersListCertificates**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersListCertificates) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates | List all certificates associated with a certificate order. |
| [**appServiceCertificateOrdersReissue**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersReissue) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/reissue | Reissue an existing certificate order. |
| [**appServiceCertificateOrdersRenew**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersRenew) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/renew | Renew an existing certificate order. |
| [**appServiceCertificateOrdersResendEmail**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersResendEmail) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/resendEmail | Resend certificate email. |
| [**appServiceCertificateOrdersResendRequestEmails**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersResendRequestEmails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/resendRequestEmails | Verify domain ownership for this certificate order. |
| [**appServiceCertificateOrdersRetrieveCertificateActions**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersRetrieveCertificateActions) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveCertificateActions | Retrieve the list of certificate actions. |
| [**appServiceCertificateOrdersRetrieveCertificateEmailHistory**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersRetrieveCertificateEmailHistory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{name}/retrieveEmailHistory | Retrieve email history. |
| [**appServiceCertificateOrdersRetrieveSiteSeal**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersRetrieveSiteSeal) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/retrieveSiteSeal | Verify domain ownership for this certificate order. |
| [**appServiceCertificateOrdersUpdate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName} | Create or update a certificate purchase order. |
| [**appServiceCertificateOrdersUpdateCertificate**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersUpdateCertificate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/certificates/{name} | Creates or updates a certificate and associates with key vault secret. |
| [**appServiceCertificateOrdersValidatePurchaseInformation**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersValidatePurchaseInformation) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CertificateRegistration/validateCertificateRegistrationInformation | Validate information for a certificate order. |
| [**appServiceCertificateOrdersVerifyDomainOwnership**](AppServiceCertificateOrdersApi.md#appServiceCertificateOrdersVerifyDomainOwnership) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CertificateRegistration/certificateOrders/{certificateOrderName}/verifyDomainOwnership | Verify domain ownership for this certificate order. |


<a id="appServiceCertificateOrdersCreateOrUpdate"></a>
# **appServiceCertificateOrdersCreateOrUpdate**
> AppServiceCertificateOrder appServiceCertificateOrdersCreateOrUpdate(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, certificateDistinguishedName)

Create or update a certificate purchase order.

Create or update a certificate purchase order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServiceCertificateOrder certificateDistinguishedName = new AppServiceCertificateOrder(); // AppServiceCertificateOrder | Distinguished name to use for the certificate order.
    try {
      AppServiceCertificateOrder result = apiInstance.appServiceCertificateOrdersCreateOrUpdate(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, certificateDistinguishedName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersCreateOrUpdate");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **certificateDistinguishedName** | [**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)| Distinguished name to use for the certificate order. | |

### Return type

[**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | App Service Certificate Order is created. |  -  |
| **201** | App Service Certificate Order creation operation is in progress |  -  |

<a id="appServiceCertificateOrdersCreateOrUpdateCertificate"></a>
# **appServiceCertificateOrdersCreateOrUpdateCertificate**
> AppServiceCertificateResource appServiceCertificateOrdersCreateOrUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate)

Creates or updates a certificate and associates with key vault secret.

Creates or updates a certificate and associates with key vault secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServiceCertificateResource keyVaultCertificate = new AppServiceCertificateResource(); // AppServiceCertificateResource | Key vault certificate resource Id.
    try {
      AppServiceCertificateResource result = apiInstance.appServiceCertificateOrdersCreateOrUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersCreateOrUpdateCertificate");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **keyVaultCertificate** | [**AppServiceCertificateResource**](AppServiceCertificateResource.md)| Key vault certificate resource Id. | |

### Return type

[**AppServiceCertificateResource**](AppServiceCertificateResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | App Service Certificate is created. |  -  |
| **201** | App Service Certificate creation operation is in progress |  -  |

<a id="appServiceCertificateOrdersDelete"></a>
# **appServiceCertificateOrdersDelete**
> appServiceCertificateOrdersDelete(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

Delete an existing certificate order.

Delete an existing certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.appServiceCertificateOrdersDelete(resourceGroupName, certificateOrderName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersDelete");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted certificate order. |  -  |
| **204** | Certificate order does not exist. |  -  |

<a id="appServiceCertificateOrdersDeleteCertificate"></a>
# **appServiceCertificateOrdersDeleteCertificate**
> appServiceCertificateOrdersDeleteCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion)

Delete the certificate associated with a certificate order.

Delete the certificate associated with a certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.appServiceCertificateOrdersDeleteCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersDeleteCertificate");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted certificate. |  -  |
| **204** | Certificate does not exist. |  -  |

<a id="appServiceCertificateOrdersGet"></a>
# **appServiceCertificateOrdersGet**
> AppServiceCertificateOrder appServiceCertificateOrdersGet(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

Get a certificate order.

Get a certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order..
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceCertificateOrder result = apiInstance.appServiceCertificateOrdersGet(resourceGroupName, certificateOrderName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersGet");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order.. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceCertificateOrdersGetCertificate"></a>
# **appServiceCertificateOrdersGetCertificate**
> AppServiceCertificateResource appServiceCertificateOrdersGetCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion)

Get the certificate associated with a certificate order.

Get the certificate associated with a certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceCertificateResource result = apiInstance.appServiceCertificateOrdersGetCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersGetCertificate");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceCertificateResource**](AppServiceCertificateResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceCertificateOrdersList"></a>
# **appServiceCertificateOrdersList**
> AppServiceCertificateOrderCollection appServiceCertificateOrdersList(subscriptionId, apiVersion)

List all certificate orders in a subscription.

List all certificate orders in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceCertificateOrderCollection result = apiInstance.appServiceCertificateOrdersList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersList");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceCertificateOrderCollection**](AppServiceCertificateOrderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceCertificateOrdersListByResourceGroup"></a>
# **appServiceCertificateOrdersListByResourceGroup**
> AppServiceCertificateOrderCollection appServiceCertificateOrdersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Get certificate orders in a resource group.

Get certificate orders in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceCertificateOrderCollection result = apiInstance.appServiceCertificateOrdersListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersListByResourceGroup");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceCertificateOrderCollection**](AppServiceCertificateOrderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceCertificateOrdersListCertificates"></a>
# **appServiceCertificateOrdersListCertificates**
> AppServiceCertificateCollection appServiceCertificateOrdersListCertificates(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

List all certificates associated with a certificate order.

List all certificates associated with a certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceCertificateCollection result = apiInstance.appServiceCertificateOrdersListCertificates(resourceGroupName, certificateOrderName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersListCertificates");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceCertificateCollection**](AppServiceCertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceCertificateOrdersReissue"></a>
# **appServiceCertificateOrdersReissue**
> appServiceCertificateOrdersReissue(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, reissueCertificateOrderRequest)

Reissue an existing certificate order.

Reissue an existing certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    ReissueCertificateOrderRequest reissueCertificateOrderRequest = new ReissueCertificateOrderRequest(); // ReissueCertificateOrderRequest | Parameters for the reissue.
    try {
      apiInstance.appServiceCertificateOrdersReissue(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, reissueCertificateOrderRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersReissue");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **reissueCertificateOrderRequest** | [**ReissueCertificateOrderRequest**](ReissueCertificateOrderRequest.md)| Parameters for the reissue. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="appServiceCertificateOrdersRenew"></a>
# **appServiceCertificateOrdersRenew**
> appServiceCertificateOrdersRenew(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, renewCertificateOrderRequest)

Renew an existing certificate order.

Renew an existing certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    RenewCertificateOrderRequest renewCertificateOrderRequest = new RenewCertificateOrderRequest(); // RenewCertificateOrderRequest | Renew parameters
    try {
      apiInstance.appServiceCertificateOrdersRenew(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, renewCertificateOrderRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersRenew");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **renewCertificateOrderRequest** | [**RenewCertificateOrderRequest**](RenewCertificateOrderRequest.md)| Renew parameters | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="appServiceCertificateOrdersResendEmail"></a>
# **appServiceCertificateOrdersResendEmail**
> appServiceCertificateOrdersResendEmail(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

Resend certificate email.

Resend certificate email.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.appServiceCertificateOrdersResendEmail(resourceGroupName, certificateOrderName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersResendEmail");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="appServiceCertificateOrdersResendRequestEmails"></a>
# **appServiceCertificateOrdersResendRequestEmails**
> appServiceCertificateOrdersResendRequestEmails(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, nameIdentifier)

Verify domain ownership for this certificate order.

Verify domain ownership for this certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServiceCertificateOrdersResendRequestEmailsRequest nameIdentifier = new AppServiceCertificateOrdersResendRequestEmailsRequest(); // AppServiceCertificateOrdersResendRequestEmailsRequest | Email address
    try {
      apiInstance.appServiceCertificateOrdersResendRequestEmails(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, nameIdentifier);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersResendRequestEmails");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **nameIdentifier** | [**AppServiceCertificateOrdersResendRequestEmailsRequest**](AppServiceCertificateOrdersResendRequestEmailsRequest.md)| Email address | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="appServiceCertificateOrdersRetrieveCertificateActions"></a>
# **appServiceCertificateOrdersRetrieveCertificateActions**
> List&lt;CertificateOrderAction&gt; appServiceCertificateOrdersRetrieveCertificateActions(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve the list of certificate actions.

Retrieve the list of certificate actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<CertificateOrderAction> result = apiInstance.appServiceCertificateOrdersRetrieveCertificateActions(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersRetrieveCertificateActions");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;CertificateOrderAction&gt;**](CertificateOrderAction.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceCertificateOrdersRetrieveCertificateEmailHistory"></a>
# **appServiceCertificateOrdersRetrieveCertificateEmailHistory**
> List&lt;CertificateEmail&gt; appServiceCertificateOrdersRetrieveCertificateEmailHistory(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve email history.

Retrieve email history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<CertificateEmail> result = apiInstance.appServiceCertificateOrdersRetrieveCertificateEmailHistory(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersRetrieveCertificateEmailHistory");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;CertificateEmail&gt;**](CertificateEmail.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceCertificateOrdersRetrieveSiteSeal"></a>
# **appServiceCertificateOrdersRetrieveSiteSeal**
> SiteSeal appServiceCertificateOrdersRetrieveSiteSeal(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, siteSealRequest)

Verify domain ownership for this certificate order.

Verify domain ownership for this certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    SiteSealRequest siteSealRequest = new SiteSealRequest(); // SiteSealRequest | Site seal request.
    try {
      SiteSeal result = apiInstance.appServiceCertificateOrdersRetrieveSiteSeal(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, siteSealRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersRetrieveSiteSeal");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **siteSealRequest** | [**SiteSealRequest**](SiteSealRequest.md)| Site seal request. | |

### Return type

[**SiteSeal**](SiteSeal.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceCertificateOrdersUpdate"></a>
# **appServiceCertificateOrdersUpdate**
> AppServiceCertificateOrder appServiceCertificateOrdersUpdate(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, certificateDistinguishedName)

Create or update a certificate purchase order.

Create or update a certificate purchase order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServiceCertificateOrderPatchResource certificateDistinguishedName = new AppServiceCertificateOrderPatchResource(); // AppServiceCertificateOrderPatchResource | Distinguished name to use for the certificate order.
    try {
      AppServiceCertificateOrder result = apiInstance.appServiceCertificateOrdersUpdate(resourceGroupName, certificateOrderName, subscriptionId, apiVersion, certificateDistinguishedName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersUpdate");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **certificateDistinguishedName** | [**AppServiceCertificateOrderPatchResource**](AppServiceCertificateOrderPatchResource.md)| Distinguished name to use for the certificate order. | |

### Return type

[**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | App Service Certificate Order is created. |  -  |
| **201** | App Service Certificate Order creation operation is in progress |  -  |

<a id="appServiceCertificateOrdersUpdateCertificate"></a>
# **appServiceCertificateOrdersUpdateCertificate**
> AppServiceCertificateResource appServiceCertificateOrdersUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate)

Creates or updates a certificate and associates with key vault secret.

Creates or updates a certificate and associates with key vault secret.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String name = "name_example"; // String | Name of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServiceCertificatePatchResource keyVaultCertificate = new AppServiceCertificatePatchResource(); // AppServiceCertificatePatchResource | Key vault certificate resource Id.
    try {
      AppServiceCertificateResource result = apiInstance.appServiceCertificateOrdersUpdateCertificate(resourceGroupName, certificateOrderName, name, subscriptionId, apiVersion, keyVaultCertificate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersUpdateCertificate");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **name** | **String**| Name of the certificate. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **keyVaultCertificate** | [**AppServiceCertificatePatchResource**](AppServiceCertificatePatchResource.md)| Key vault certificate resource Id. | |

### Return type

[**AppServiceCertificateResource**](AppServiceCertificateResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | App Service Certificate is created. |  -  |
| **201** | App Service Certificate creation operation is in progress |  -  |

<a id="appServiceCertificateOrdersValidatePurchaseInformation"></a>
# **appServiceCertificateOrdersValidatePurchaseInformation**
> appServiceCertificateOrdersValidatePurchaseInformation(subscriptionId, apiVersion, appServiceCertificateOrder)

Validate information for a certificate order.

Validate information for a certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServiceCertificateOrder appServiceCertificateOrder = new AppServiceCertificateOrder(); // AppServiceCertificateOrder | Information for a certificate order.
    try {
      apiInstance.appServiceCertificateOrdersValidatePurchaseInformation(subscriptionId, apiVersion, appServiceCertificateOrder);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersValidatePurchaseInformation");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **appServiceCertificateOrder** | [**AppServiceCertificateOrder**](AppServiceCertificateOrder.md)| Information for a certificate order. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="appServiceCertificateOrdersVerifyDomainOwnership"></a>
# **appServiceCertificateOrdersVerifyDomainOwnership**
> appServiceCertificateOrdersVerifyDomainOwnership(resourceGroupName, certificateOrderName, subscriptionId, apiVersion)

Verify domain ownership for this certificate order.

Verify domain ownership for this certificate order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceCertificateOrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceCertificateOrdersApi apiInstance = new AppServiceCertificateOrdersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String certificateOrderName = "certificateOrderName_example"; // String | Name of the certificate order.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.appServiceCertificateOrdersVerifyDomainOwnership(resourceGroupName, certificateOrderName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceCertificateOrdersApi#appServiceCertificateOrdersVerifyDomainOwnership");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **certificateOrderName** | **String**| Name of the certificate order. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

