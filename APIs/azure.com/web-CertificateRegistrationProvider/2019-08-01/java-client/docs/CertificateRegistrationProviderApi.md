# CertificateRegistrationProviderApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certificateRegistrationProviderListOperations**](CertificateRegistrationProviderApi.md#certificateRegistrationProviderListOperations) | **GET** /providers/Microsoft.CertificateRegistration/operations | Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider |


<a id="certificateRegistrationProviderListOperations"></a>
# **certificateRegistrationProviderListOperations**
> CertificateRegistrationProviderListOperations200Response certificateRegistrationProviderListOperations(apiVersion)

Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider

Description for Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CertificateRegistrationProviderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CertificateRegistrationProviderApi apiInstance = new CertificateRegistrationProviderApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      CertificateRegistrationProviderListOperations200Response result = apiInstance.certificateRegistrationProviderListOperations(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CertificateRegistrationProviderApi#certificateRegistrationProviderListOperations");
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
| **apiVersion** | **String**| API Version | |

### Return type

[**CertificateRegistrationProviderListOperations200Response**](CertificateRegistrationProviderListOperations200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

