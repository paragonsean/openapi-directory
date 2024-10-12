# PolicyApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policyGet**](PolicyApi.md#policyGet) | **GET** /operations/policy/current | Retrieves the current policy for a given kind of TEE. |
| [**policyPrepareToSet**](PolicyApi.md#policyPrepareToSet) | **POST** /operations/policy/updatepolicy | Accepts a new policy document and returns a JWT which expresses  used in preparation to set attestation policy. |
| [**policyReset**](PolicyApi.md#policyReset) | **POST** /operations/policy/current | Resets the attestation policy for the specified tenant and reverts to the default policy. |
| [**policySet**](PolicyApi.md#policySet) | **PUT** /operations/policy/current | Sets the policy for a given kind of TEE. |


<a id="policyGet"></a>
# **policyGet**
> AttestationPolicy policyGet(apiVersion, tee)

Retrieves the current policy for a given kind of TEE.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String apiVersion = "2018-09-01-preview"; // String | Client API version.
    String tee = "SgxEnclave"; // String | Specifies the trusted execution environment to be used to validate the evidence
    try {
      AttestationPolicy result = apiInstance.policyGet(apiVersion, tee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyGet");
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
| **apiVersion** | **String**| Client API version. | [enum: 2018-09-01-preview] |
| **tee** | **String**| Specifies the trusted execution environment to be used to validate the evidence | [enum: SgxEnclave, OpenEnclave, CyResComponent, AzureGuest] |

### Return type

[**AttestationPolicy**](AttestationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **401** | Request is unauthorized |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="policyPrepareToSet"></a>
# **policyPrepareToSet**
> String policyPrepareToSet(apiVersion, tee, policyJws)

Accepts a new policy document and returns a JWT which expresses  used in preparation to set attestation policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String apiVersion = "2018-09-01-preview"; // String | Client API version.
    String tee = "SgxEnclave"; // String | Specifies the trusted execution environment to be used to validate the evidence
    String policyJws = "policyJws_example"; // String | JSON Web Signature (See RFC7515) expressing the new policy
    try {
      String result = apiInstance.policyPrepareToSet(apiVersion, tee, policyJws);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyPrepareToSet");
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
| **apiVersion** | **String**| Client API version. | [enum: 2018-09-01-preview] |
| **tee** | **String**| Specifies the trusted execution environment to be used to validate the evidence | [enum: SgxEnclave, OpenEnclave, CyResComponent, AzureGuest] |
| **policyJws** | **String**| JSON Web Signature (See RFC7515) expressing the new policy | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - Returns a JWT signed by the metadata signing key that contains the hash of the supplied policy to be set. |  -  |
| **400** | Bad request |  -  |
| **401** | Request is unauthorized |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="policyReset"></a>
# **policyReset**
> String policyReset(apiVersion, tee, policyJws)

Resets the attestation policy for the specified tenant and reverts to the default policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String apiVersion = "2018-09-01-preview"; // String | Client API version.
    String tee = "SgxEnclave"; // String | Specifies the trusted execution environment to be used to validate the evidence
    String policyJws = "policyJws_example"; // String | JSON Web Signature with an empty policy document
    try {
      String result = apiInstance.policyReset(apiVersion, tee, policyJws);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policyReset");
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
| **apiVersion** | **String**| Client API version. | [enum: 2018-09-01-preview] |
| **tee** | **String**| Specifies the trusted execution environment to be used to validate the evidence | [enum: SgxEnclave, OpenEnclave, CyResComponent, AzureGuest] |
| **policyJws** | **String**| JSON Web Signature with an empty policy document | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - Returns a JWT signed by the metadata signing key that contains the hash of the supplied policy to be set. |  -  |
| **400** | Bad request |  -  |
| **401** | Request is unauthorized |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="policySet"></a>
# **policySet**
> policySet(apiVersion, tee, newAttestationPolicy)

Sets the policy for a given kind of TEE.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    PolicyApi apiInstance = new PolicyApi(defaultClient);
    String apiVersion = "2018-09-01-preview"; // String | Client API version.
    String tee = "SgxEnclave"; // String | Specifies the trusted execution environment to be used to validate the evidence
    String newAttestationPolicy = "newAttestationPolicy_example"; // String | JWT Expressing the new policy
    try {
      apiInstance.policySet(apiVersion, tee, newAttestationPolicy);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicyApi#policySet");
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
| **apiVersion** | **String**| Client API version. | [enum: 2018-09-01-preview] |
| **tee** | **String**| Specifies the trusted execution environment to be used to validate the evidence | [enum: SgxEnclave, OpenEnclave, CyResComponent, AzureGuest] |
| **newAttestationPolicy** | **String**| JWT Expressing the new policy | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **401** | Request is unauthorized |  -  |
| **0** | Error response describing why the operation failed |  -  |

