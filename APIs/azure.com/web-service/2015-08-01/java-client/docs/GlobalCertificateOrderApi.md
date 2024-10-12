# GlobalCertificateOrderApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalCertificateOrderGetAllCertificateOrders**](GlobalCertificateOrderApi.md#globalCertificateOrderGetAllCertificateOrders) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CertificateRegistration/certificateOrders | Lists all domains in a subscription |
| [**globalCertificateOrderValidateCertificatePurchaseInformation**](GlobalCertificateOrderApi.md#globalCertificateOrderValidateCertificatePurchaseInformation) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CertificateRegistration/validateCertificateRegistrationInformation | Validate certificate purchase information |


<a id="globalCertificateOrderGetAllCertificateOrders"></a>
# **globalCertificateOrderGetAllCertificateOrders**
> CertificateOrderCollection globalCertificateOrderGetAllCertificateOrders(subscriptionId, apiVersion)

Lists all domains in a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalCertificateOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalCertificateOrderApi apiInstance = new GlobalCertificateOrderApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      CertificateOrderCollection result = apiInstance.globalCertificateOrderGetAllCertificateOrders(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalCertificateOrderApi#globalCertificateOrderGetAllCertificateOrders");
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

<a id="globalCertificateOrderValidateCertificatePurchaseInformation"></a>
# **globalCertificateOrderValidateCertificatePurchaseInformation**
> Object globalCertificateOrderValidateCertificatePurchaseInformation(subscriptionId, apiVersion, certificateOrder)

Validate certificate purchase information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalCertificateOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GlobalCertificateOrderApi apiInstance = new GlobalCertificateOrderApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    CertificateOrder certificateOrder = new CertificateOrder(); // CertificateOrder | Certificate order
    try {
      Object result = apiInstance.globalCertificateOrderValidateCertificatePurchaseInformation(subscriptionId, apiVersion, certificateOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalCertificateOrderApi#globalCertificateOrderValidateCertificatePurchaseInformation");
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
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **certificateOrder** | [**CertificateOrder**](CertificateOrder.md)| Certificate order | |

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

