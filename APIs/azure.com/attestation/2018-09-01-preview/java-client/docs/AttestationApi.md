# AttestationApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**certsGet**](AttestationApi.md#certsGet) | **GET** /certs | Retrieves the OpenID Configuration data for the Azure Attestation Service |
| [**metadataConfigurationGet**](AttestationApi.md#metadataConfigurationGet) | **GET** /.well-known/openid-configuration | Retrieves the OpenID Configuration data for the Azure Attestation Service |


<a id="certsGet"></a>
# **certsGet**
> Object certsGet()

Retrieves the OpenID Configuration data for the Azure Attestation Service

Retrieves attestation signing keys in use by the attestation service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttestationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    AttestationApi apiInstance = new AttestationApi(defaultClient);
    try {
      Object result = apiInstance.certsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttestationApi#certsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Error processing the request |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="metadataConfigurationGet"></a>
# **metadataConfigurationGet**
> Object metadataConfigurationGet()

Retrieves the OpenID Configuration data for the Azure Attestation Service

Retrieves metadata about the attestation signing keys in use by the  attestation service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttestationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    AttestationApi apiInstance = new AttestationApi(defaultClient);
    try {
      Object result = apiInstance.metadataConfigurationGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttestationApi#metadataConfigurationGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Error processing the request |  -  |
| **0** | Error response describing why the operation failed |  -  |

