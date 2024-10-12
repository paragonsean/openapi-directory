# TenantAccessGitApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tenantAccessGitGet**](TenantAccessGitApi.md#tenantAccessGitGet) | **GET** /tenant/{accessName}/git |  |
| [**tenantAccessGitRegeneratePrimaryKey**](TenantAccessGitApi.md#tenantAccessGitRegeneratePrimaryKey) | **POST** /tenant/{accessName}/git/regeneratePrimaryKey |  |
| [**tenantAccessGitRegenerateSecondaryKey**](TenantAccessGitApi.md#tenantAccessGitRegenerateSecondaryKey) | **POST** /tenant/{accessName}/git/regenerateSecondaryKey |  |


<a id="tenantAccessGitGet"></a>
# **tenantAccessGitGet**
> AccessInformationContract tenantAccessGitGet(apiVersion, accessName)



Gets the Git access configuration for the tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantAccessGitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantAccessGitApi apiInstance = new TenantAccessGitApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String accessName = "access"; // String | The identifier of the Access configuration.
    try {
      AccessInformationContract result = apiInstance.tenantAccessGitGet(apiVersion, accessName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantAccessGitApi#tenantAccessGitGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **accessName** | **String**| The identifier of the Access configuration. | [enum: access] |

### Return type

[**AccessInformationContract**](AccessInformationContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Git Access Information for the Service. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tenantAccessGitRegeneratePrimaryKey"></a>
# **tenantAccessGitRegeneratePrimaryKey**
> tenantAccessGitRegeneratePrimaryKey(apiVersion, accessName)



Regenerate primary access key for GIT.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantAccessGitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantAccessGitApi apiInstance = new TenantAccessGitApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String accessName = "access"; // String | The identifier of the Access configuration.
    try {
      apiInstance.tenantAccessGitRegeneratePrimaryKey(apiVersion, accessName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantAccessGitApi#tenantAccessGitRegeneratePrimaryKey");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **accessName** | **String**| The identifier of the Access configuration. | [enum: access] |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The primary key was successfully regenerated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="tenantAccessGitRegenerateSecondaryKey"></a>
# **tenantAccessGitRegenerateSecondaryKey**
> tenantAccessGitRegenerateSecondaryKey(apiVersion, accessName)



Regenerate secondary access key for GIT.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantAccessGitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantAccessGitApi apiInstance = new TenantAccessGitApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String accessName = "access"; // String | The identifier of the Access configuration.
    try {
      apiInstance.tenantAccessGitRegenerateSecondaryKey(apiVersion, accessName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantAccessGitApi#tenantAccessGitRegenerateSecondaryKey");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **accessName** | **String**| The identifier of the Access configuration. | [enum: access] |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The secondary key was successfully regenerated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

