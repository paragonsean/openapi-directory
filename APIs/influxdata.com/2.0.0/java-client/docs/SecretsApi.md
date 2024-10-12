# SecretsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrgsIDSecrets**](SecretsApi.md#getOrgsIDSecrets) | **GET** /orgs/{orgID}/secrets | List all secret keys for an organization |
| [**patchOrgsIDSecrets**](SecretsApi.md#patchOrgsIDSecrets) | **PATCH** /orgs/{orgID}/secrets | Update secrets in an organization |
| [**postOrgsIDSecrets**](SecretsApi.md#postOrgsIDSecrets) | **POST** /orgs/{orgID}/secrets/delete | Delete secrets from an organization |


<a id="getOrgsIDSecrets"></a>
# **getOrgsIDSecrets**
> SecretKeysResponse getOrgsIDSecrets(orgID, zapTraceSpan)

List all secret keys for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      SecretKeysResponse result = apiInstance.getOrgsIDSecrets(orgID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#getOrgsIDSecrets");
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
| **orgID** | **String**| The organization ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**SecretKeysResponse**](SecretKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all secret keys |  -  |
| **0** | Unexpected error |  -  |

<a id="patchOrgsIDSecrets"></a>
# **patchOrgsIDSecrets**
> patchOrgsIDSecrets(orgID, requestBody, zapTraceSpan)

Update secrets in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | Secret key value pairs to update/add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.patchOrgsIDSecrets(orgID, requestBody, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#patchOrgsIDSecrets");
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
| **orgID** | **String**| The organization ID. | |
| **requestBody** | [**Map&lt;String, String&gt;**](String.md)| Secret key value pairs to update/add | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Keys successfully patched |  -  |
| **0** | Unexpected error |  -  |

<a id="postOrgsIDSecrets"></a>
# **postOrgsIDSecrets**
> postOrgsIDSecrets(orgID, secretKeys, zapTraceSpan)

Delete secrets from an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    SecretsApi apiInstance = new SecretsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    SecretKeys secretKeys = new SecretKeys(); // SecretKeys | Secret key to delete
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.postOrgsIDSecrets(orgID, secretKeys, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretsApi#postOrgsIDSecrets");
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
| **orgID** | **String**| The organization ID. | |
| **secretKeys** | [**SecretKeys**](SecretKeys.md)| Secret key to delete | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Keys successfully patched |  -  |
| **0** | Unexpected error |  -  |

