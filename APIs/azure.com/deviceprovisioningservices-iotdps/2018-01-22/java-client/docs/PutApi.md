# PutApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dpsCertificateCreateOrUpdate**](PutApi.md#dpsCertificateCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName} | Upload the certificate to the provisioning service. |
| [**iotDpsResourceCreateOrUpdate**](PutApi.md#iotDpsResourceCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName} | Create or update the metadata of the provisioning service. |


<a id="dpsCertificateCreateOrUpdate"></a>
# **dpsCertificateCreateOrUpdate**
> CertificateResponse dpsCertificateCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, provisioningServiceName, certificateName, certificateDescription, ifMatch)

Upload the certificate to the provisioning service.

Add new certificate or update an existing certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PutApi apiInstance = new PutApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
    String provisioningServiceName = "provisioningServiceName_example"; // String | The name of the provisioning service.
    String certificateName = "certificateName_example"; // String | The name of the certificate create or update.
    CertificateBodyDescription certificateDescription = new CertificateBodyDescription(); // CertificateBodyDescription | The certificate body.
    String ifMatch = "ifMatch_example"; // String | ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate.
    try {
      CertificateResponse result = apiInstance.dpsCertificateCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, provisioningServiceName, certificateName, certificateDescription, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PutApi#dpsCertificateCreateOrUpdate");
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
| **resourceGroupName** | **String**| Resource group identifier. | |
| **provisioningServiceName** | **String**| The name of the provisioning service. | |
| **certificateName** | **String**| The name of the certificate create or update. | |
| **certificateDescription** | [**CertificateBodyDescription**](CertificateBodyDescription.md)| The certificate body. | |
| **ifMatch** | **String**| ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate. | [optional] |

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If certificate already exist and update was successful, the operation returns HTTP status code of 201 (OK). |  -  |
| **0** | Default error response. |  -  |

<a id="iotDpsResourceCreateOrUpdate"></a>
# **iotDpsResourceCreateOrUpdate**
> ProvisioningServiceDescription iotDpsResourceCreateOrUpdate(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, iotDpsDescription)

Create or update the metadata of the provisioning service.

Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PutApi apiInstance = new PutApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service to create or update.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    ProvisioningServiceDescription iotDpsDescription = new ProvisioningServiceDescription(); // ProvisioningServiceDescription | Description of the provisioning service to create or update.
    try {
      ProvisioningServiceDescription result = apiInstance.iotDpsResourceCreateOrUpdate(subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, iotDpsDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PutApi#iotDpsResourceCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| Resource group identifier. | |
| **provisioningServiceName** | **String**| Name of provisioning service to create or update. | |
| **apiVersion** | **String**| The version of the API. | |
| **iotDpsDescription** | [**ProvisioningServiceDescription**](ProvisioningServiceDescription.md)| Description of the provisioning service to create or update. | |

### Return type

[**ProvisioningServiceDescription**](ProvisioningServiceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains all the non-security properties of the provisioning service. Security-related properties are set to null. |  -  |
| **201** | This is a long running operation. The operation returns a 201 if the validation is complete. The response includes an Azure-AsyncOperation header that contains a status URL. Clients are expected to poll the status URL for the status of the operation. If successful, the operation returns HTTP status code of 201 (OK). |  -  |
| **0** | Default error response. |  -  |

