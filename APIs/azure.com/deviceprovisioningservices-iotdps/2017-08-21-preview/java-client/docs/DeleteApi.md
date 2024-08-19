# DeleteApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dpsCertificateDelete**](DeleteApi.md#dpsCertificateDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName} |  |
| [**iotDpsResourceDelete**](DeleteApi.md#iotDpsResourceDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName} |  |


<a id="dpsCertificateDelete"></a>
# **dpsCertificateDelete**
> dpsCertificateDelete(subscriptionId, resourceGroupName, ifMatch, provisioningServiceName, certificateName, apiVersion, certificateName2, certificateRawBytes, certificateIsVerified, certificatePurpose, certificateCreated, certificateLastUpdated, certificateHasPrivateKey, certificateNonce)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeleteApi apiInstance = new DeleteApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
    String ifMatch = "ifMatch_example"; // String | ETag of the certificate
    String provisioningServiceName = "provisioningServiceName_example"; // String | The name of the provisioning service.
    String certificateName = "certificateName_example"; // String | This is a mandatory field, and is the logical name of the certificate that the provisioning service will access by.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String certificateName2 = "certificateName_example"; // String | This is optional, and it is the Common Name of the certificate.
    byte[] certificateRawBytes = null; // byte[] | Raw data within the certificate.
    Boolean certificateIsVerified = true; // Boolean | Indicates if certificate has been verified by owner of the private key.
    String certificatePurpose = "clientAuthentication"; // String | A description that mentions the purpose of the certificate.
    OffsetDateTime certificateCreated = OffsetDateTime.now(); // OffsetDateTime | Time the certificate is created.
    OffsetDateTime certificateLastUpdated = OffsetDateTime.now(); // OffsetDateTime | Time the certificate is last updated.
    Boolean certificateHasPrivateKey = true; // Boolean | Indicates if the certificate contains a private key.
    String certificateNonce = "certificateNonce_example"; // String | Random number generated to indicate Proof of Possession.
    try {
      apiInstance.dpsCertificateDelete(subscriptionId, resourceGroupName, ifMatch, provisioningServiceName, certificateName, apiVersion, certificateName2, certificateRawBytes, certificateIsVerified, certificatePurpose, certificateCreated, certificateLastUpdated, certificateHasPrivateKey, certificateNonce);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeleteApi#dpsCertificateDelete");
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
| **ifMatch** | **String**| ETag of the certificate | |
| **provisioningServiceName** | **String**| The name of the provisioning service. | |
| **certificateName** | **String**| This is a mandatory field, and is the logical name of the certificate that the provisioning service will access by. | |
| **apiVersion** | **String**| The version of the API. | |
| **certificateName2** | **String**| This is optional, and it is the Common Name of the certificate. | [optional] |
| **certificateRawBytes** | **byte[]**| Raw data within the certificate. | [optional] |
| **certificateIsVerified** | **Boolean**| Indicates if certificate has been verified by owner of the private key. | [optional] |
| **certificatePurpose** | **String**| A description that mentions the purpose of the certificate. | [optional] [enum: clientAuthentication, serverAuthentication] |
| **certificateCreated** | **OffsetDateTime**| Time the certificate is created. | [optional] |
| **certificateLastUpdated** | **OffsetDateTime**| Time the certificate is last updated. | [optional] |
| **certificateHasPrivateKey** | **Boolean**| Indicates if the certificate contains a private key. | [optional] |
| **certificateNonce** | **String**| Random number generated to indicate Proof of Possession. | [optional] |

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
| **200** | OK. |  -  |
| **204** | No content. |  -  |
| **0** | Default error response. |  -  |

<a id="iotDpsResourceDelete"></a>
# **iotDpsResourceDelete**
> iotDpsResourceDelete(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeleteApi apiInstance = new DeleteApi(defaultClient);
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service to delete.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group identifier.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    try {
      apiInstance.iotDpsResourceDelete(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeleteApi#iotDpsResourceDelete");
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
| **provisioningServiceName** | **String**| Name of provisioning service to delete. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| Resource group identifier. | |
| **apiVersion** | **String**| The version of the API. | |

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
| **200** | This is returned as a response to the status polling request for the delete operation. The body contains the resource representation that indicates a transitional provisioning state. |  -  |
| **202** | The provisioning service resource provider always returns a 202 Accepted status code with valid Location and Retry-After headers. The resource provider also sets the Azure-AsyncOperation header with a URL that points to the operation resource for this operation. Subsequent GET attempts on the resource after a DELETE operation return a resource representation that indicates a transitional provisioning state (such as Terminating). To retrieve the status of the operation, a client can either poll the URL returned in the Location header after the Retry-After interval, get the provisioning service status directly, or query the operation resource. |  -  |
| **204** | Once the long running delete operation completes successfully, a 204 No Content status code is returned when the status polling request finds the provisioning service metadata in the service and the status of the delete operation is set to a completed state. |  -  |
| **404** | After the long running delete operation completes successfully, a 404 Not Found is returned when the status polling request no longer finds the provisioning service metadata in the service. |  -  |
| **0** | Default error response. |  -  |

