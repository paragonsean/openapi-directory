# VaultCertificatesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vaultCertificatesCreate**](VaultCertificatesApi.md#vaultCertificatesCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/certificates/{certificateName} |  |


<a id="vaultCertificatesCreate"></a>
# **vaultCertificatesCreate**
> VaultCertificateResponse vaultCertificatesCreate(subscriptionId, apiVersion, resourceGroupName, vaultName, certificateName, certificateRequest)



Uploads a certificate for a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VaultCertificatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VaultCertificatesApi apiInstance = new VaultCertificatesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String vaultName = "vaultName_example"; // String | The name of the recovery services vault.
    String certificateName = "certificateName_example"; // String | Certificate friendly name.
    CertificateRequest certificateRequest = new CertificateRequest(); // CertificateRequest | Input parameters for uploading the vault certificate.
    try {
      VaultCertificateResponse result = apiInstance.vaultCertificatesCreate(subscriptionId, apiVersion, resourceGroupName, vaultName, certificateName, certificateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VaultCertificatesApi#vaultCertificatesCreate");
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
| **subscriptionId** | **String**| The subscription Id. | |
| **apiVersion** | **String**| Client Api Version. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **vaultName** | **String**| The name of the recovery services vault. | |
| **certificateName** | **String**| Certificate friendly name. | |
| **certificateRequest** | [**CertificateRequest**](CertificateRequest.md)| Input parameters for uploading the vault certificate. | |

### Return type

[**VaultCertificateResponse**](VaultCertificateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

