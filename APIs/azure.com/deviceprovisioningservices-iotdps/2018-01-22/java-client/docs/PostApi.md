# PostApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dpsCertificateGenerateVerificationCode**](PostApi.md#dpsCertificateGenerateVerificationCode) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName}/generateVerificationCode |  |
| [**dpsCertificateVerifyCertificate**](PostApi.md#dpsCertificateVerifyCertificate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/certificates/{certificateName}/verify | Verify certificate&#39;s private key possession. |
| [**iotDpsResourceCheckProvisioningServiceNameAvailability**](PostApi.md#iotDpsResourceCheckProvisioningServiceNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Devices/checkProvisioningServiceNameAvailability | Check if a provisioning service name is available. |
| [**iotDpsResourceListKeys**](PostApi.md#iotDpsResourceListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/listkeys | Get the security metadata for a provisioning service. |
| [**iotDpsResourceListKeysForKeyName**](PostApi.md#iotDpsResourceListKeysForKeyName) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/provisioningServices/{provisioningServiceName}/keys/{keyName}/listkeys | Get a shared access policy by name from a provisioning service. |


<a id="dpsCertificateGenerateVerificationCode"></a>
# **dpsCertificateGenerateVerificationCode**
> VerificationCodeResponse dpsCertificateGenerateVerificationCode(certificateName, ifMatch, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, certificateName2, certificateRawBytes, certificateIsVerified, certificatePurpose, certificateCreated, certificateLastUpdated, certificateHasPrivateKey, certificateNonce)



Generate verification code for Proof of Possession.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The mandatory logical name of the certificate, that the provisioning service uses to access.
    String ifMatch = "ifMatch_example"; // String | ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | name of resource group.
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of provisioning service.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    String certificateName2 = "certificateName_example"; // String | Common Name for the certificate.
    byte[] certificateRawBytes = null; // byte[] | Raw data of certificate.
    Boolean certificateIsVerified = true; // Boolean | Indicates if the certificate has been verified by owner of the private key.
    String certificatePurpose = "clientAuthentication"; // String | Description mentioning the purpose of the certificate.
    OffsetDateTime certificateCreated = OffsetDateTime.now(); // OffsetDateTime | Certificate creation time.
    OffsetDateTime certificateLastUpdated = OffsetDateTime.now(); // OffsetDateTime | Certificate last updated time.
    Boolean certificateHasPrivateKey = true; // Boolean | Indicates if the certificate contains private key.
    String certificateNonce = "certificateNonce_example"; // String | Random number generated to indicate Proof of Possession.
    try {
      VerificationCodeResponse result = apiInstance.dpsCertificateGenerateVerificationCode(certificateName, ifMatch, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, certificateName2, certificateRawBytes, certificateIsVerified, certificatePurpose, certificateCreated, certificateLastUpdated, certificateHasPrivateKey, certificateNonce);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#dpsCertificateGenerateVerificationCode");
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
| **certificateName** | **String**| The mandatory logical name of the certificate, that the provisioning service uses to access. | |
| **ifMatch** | **String**| ETag of the certificate. This is required to update an existing certificate, and ignored while creating a brand new certificate. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| name of resource group. | |
| **provisioningServiceName** | **String**| Name of provisioning service. | |
| **apiVersion** | **String**| The version of the API. | |
| **certificateName2** | **String**| Common Name for the certificate. | [optional] |
| **certificateRawBytes** | **byte[]**| Raw data of certificate. | [optional] |
| **certificateIsVerified** | **Boolean**| Indicates if the certificate has been verified by owner of the private key. | [optional] |
| **certificatePurpose** | **String**| Description mentioning the purpose of the certificate. | [optional] [enum: clientAuthentication, serverAuthentication] |
| **certificateCreated** | **OffsetDateTime**| Certificate creation time. | [optional] |
| **certificateLastUpdated** | **OffsetDateTime**| Certificate last updated time. | [optional] |
| **certificateHasPrivateKey** | **Boolean**| Indicates if the certificate contains private key. | [optional] |
| **certificateNonce** | **String**| Random number generated to indicate Proof of Possession. | [optional] |

### Return type

[**VerificationCodeResponse**](VerificationCodeResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated verification code for that certificate is returned. |  -  |
| **0** | Default error response. |  -  |

<a id="dpsCertificateVerifyCertificate"></a>
# **dpsCertificateVerifyCertificate**
> CertificateResponse dpsCertificateVerifyCertificate(certificateName, ifMatch, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, request, certificateName2, certificateRawBytes, certificateIsVerified, certificatePurpose, certificateCreated, certificateLastUpdated, certificateHasPrivateKey, certificateNonce)

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
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String certificateName = "certificateName_example"; // String | The mandatory logical name of the certificate, that the provisioning service uses to access.
    String ifMatch = "ifMatch_example"; // String | ETag of the certificate.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String provisioningServiceName = "provisioningServiceName_example"; // String | Provisioning service name.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    VerificationCodeRequest request = new VerificationCodeRequest(); // VerificationCodeRequest | The name of the certificate
    String certificateName2 = "certificateName_example"; // String | Common Name for the certificate.
    byte[] certificateRawBytes = null; // byte[] | Raw data of certificate.
    Boolean certificateIsVerified = true; // Boolean | Indicates if the certificate has been verified by owner of the private key.
    String certificatePurpose = "clientAuthentication"; // String | Describe the purpose of the certificate.
    OffsetDateTime certificateCreated = OffsetDateTime.now(); // OffsetDateTime | Certificate creation time.
    OffsetDateTime certificateLastUpdated = OffsetDateTime.now(); // OffsetDateTime | Certificate last updated time.
    Boolean certificateHasPrivateKey = true; // Boolean | Indicates if the certificate contains private key.
    String certificateNonce = "certificateNonce_example"; // String | Random number generated to indicate Proof of Possession.
    try {
      CertificateResponse result = apiInstance.dpsCertificateVerifyCertificate(certificateName, ifMatch, subscriptionId, resourceGroupName, provisioningServiceName, apiVersion, request, certificateName2, certificateRawBytes, certificateIsVerified, certificatePurpose, certificateCreated, certificateLastUpdated, certificateHasPrivateKey, certificateNonce);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#dpsCertificateVerifyCertificate");
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
| **certificateName** | **String**| The mandatory logical name of the certificate, that the provisioning service uses to access. | |
| **ifMatch** | **String**| ETag of the certificate. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **provisioningServiceName** | **String**| Provisioning service name. | |
| **apiVersion** | **String**| The version of the API. | |
| **request** | [**VerificationCodeRequest**](VerificationCodeRequest.md)| The name of the certificate | |
| **certificateName2** | **String**| Common Name for the certificate. | [optional] |
| **certificateRawBytes** | **byte[]**| Raw data of certificate. | [optional] |
| **certificateIsVerified** | **Boolean**| Indicates if the certificate has been verified by owner of the private key. | [optional] |
| **certificatePurpose** | **String**| Describe the purpose of the certificate. | [optional] [enum: clientAuthentication, serverAuthentication] |
| **certificateCreated** | **OffsetDateTime**| Certificate creation time. | [optional] |
| **certificateLastUpdated** | **OffsetDateTime**| Certificate last updated time. | [optional] |
| **certificateHasPrivateKey** | **Boolean**| Indicates if the certificate contains private key. | [optional] |
| **certificateNonce** | **String**| Random number generated to indicate Proof of Possession. | [optional] |

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
| **200** | OK |  -  |
| **0** | Default error response. |  -  |

<a id="iotDpsResourceCheckProvisioningServiceNameAvailability"></a>
# **iotDpsResourceCheckProvisioningServiceNameAvailability**
> NameAvailabilityInfo iotDpsResourceCheckProvisioningServiceNameAvailability(subscriptionId, apiVersion, arguments)

Check if a provisioning service name is available.

Check if a provisioning service name is available. This will validate if the name is syntactically valid and if the name is usable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    OperationInputs arguments = new OperationInputs(); // OperationInputs | Set the name parameter in the OperationInputs structure to the name of the provisioning service to check.
    try {
      NameAvailabilityInfo result = apiInstance.iotDpsResourceCheckProvisioningServiceNameAvailability(subscriptionId, apiVersion, arguments);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotDpsResourceCheckProvisioningServiceNameAvailability");
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
| **apiVersion** | **String**| The version of the API. | |
| **arguments** | [**OperationInputs**](OperationInputs.md)| Set the name parameter in the OperationInputs structure to the name of the provisioning service to check. | |

### Return type

[**NameAvailabilityInfo**](NameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized response that specifies whether the provisioning service name is available. If the name is not available, the body contains the reason. |  -  |
| **0** | Default error response. |  -  |

<a id="iotDpsResourceListKeys"></a>
# **iotDpsResourceListKeys**
> SharedAccessSignatureAuthorizationRuleListResult iotDpsResourceListKeys(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion)

Get the security metadata for a provisioning service.

List the primary and secondary keys for a provisioning service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String provisioningServiceName = "provisioningServiceName_example"; // String | The provisioning service name to get the shared access keys for.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | resource group name
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    try {
      SharedAccessSignatureAuthorizationRuleListResult result = apiInstance.iotDpsResourceListKeys(provisioningServiceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotDpsResourceListKeys");
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
| **provisioningServiceName** | **String**| The provisioning service name to get the shared access keys for. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| resource group name | |
| **apiVersion** | **String**| The version of the API. | |

### Return type

[**SharedAccessSignatureAuthorizationRuleListResult**](SharedAccessSignatureAuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized array of shared access policies, including keys, that you can use to access the provisioning service endpoints. |  -  |
| **0** | Default error response. |  -  |

<a id="iotDpsResourceListKeysForKeyName"></a>
# **iotDpsResourceListKeysForKeyName**
> SharedAccessSignatureAuthorizationRuleAccessRightsDescription iotDpsResourceListKeysForKeyName(provisioningServiceName, keyName, subscriptionId, resourceGroupName, apiVersion)

Get a shared access policy by name from a provisioning service.

List primary and secondary keys for a specific key name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PostApi apiInstance = new PostApi(defaultClient);
    String provisioningServiceName = "provisioningServiceName_example"; // String | Name of the provisioning service.
    String keyName = "keyName_example"; // String | Logical key name to get key-values for.
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the provisioning service.
    String apiVersion = "apiVersion_example"; // String | The version of the API.
    try {
      SharedAccessSignatureAuthorizationRuleAccessRightsDescription result = apiInstance.iotDpsResourceListKeysForKeyName(provisioningServiceName, keyName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PostApi#iotDpsResourceListKeysForKeyName");
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
| **provisioningServiceName** | **String**| Name of the provisioning service. | |
| **keyName** | **String**| Logical key name to get key-values for. | |
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the provisioning service. | |
| **apiVersion** | **String**| The version of the API. | |

### Return type

[**SharedAccessSignatureAuthorizationRuleAccessRightsDescription**](SharedAccessSignatureAuthorizationRuleAccessRightsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This is a synchronous operation. The body contains a JSON-serialized shared access policy, including keys, that you can use to access one or more provisioning service endpoints. |  -  |
| **0** | Default error response. |  -  |

