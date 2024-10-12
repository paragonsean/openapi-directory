# TenantAccessApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tenantAccessGet**](TenantAccessApi.md#tenantAccessGet) | **GET** /tenant/{accessName} |  |
| [**tenantAccessRegeneratePrimaryKey**](TenantAccessApi.md#tenantAccessRegeneratePrimaryKey) | **POST** /tenant/{accessName}/regeneratePrimaryKey |  |
| [**tenantAccessRegenerateSecondaryKey**](TenantAccessApi.md#tenantAccessRegenerateSecondaryKey) | **POST** /tenant/{accessName}/regenerateSecondaryKey |  |
| [**tenantAccessUpdate**](TenantAccessApi.md#tenantAccessUpdate) | **PATCH** /tenant/{accessName} |  |


<a id="tenantAccessGet"></a>
# **tenantAccessGet**
> AccessInformationContract tenantAccessGet(apiVersion, accessName)



Get tenant access information details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantAccessApi apiInstance = new TenantAccessApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String accessName = "access"; // String | The identifier of the Access configuration.
    try {
      AccessInformationContract result = apiInstance.tenantAccessGet(apiVersion, accessName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantAccessApi#tenantAccessGet");
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
| **200** | Tenant Access information. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |

<a id="tenantAccessRegeneratePrimaryKey"></a>
# **tenantAccessRegeneratePrimaryKey**
> tenantAccessRegeneratePrimaryKey(apiVersion, accessName)



Regenerate primary access key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantAccessApi apiInstance = new TenantAccessApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String accessName = "access"; // String | The identifier of the Access configuration.
    try {
      apiInstance.tenantAccessRegeneratePrimaryKey(apiVersion, accessName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantAccessApi#tenantAccessRegeneratePrimaryKey");
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

<a id="tenantAccessRegenerateSecondaryKey"></a>
# **tenantAccessRegenerateSecondaryKey**
> tenantAccessRegenerateSecondaryKey(apiVersion, accessName)



Regenerate secondary access key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantAccessApi apiInstance = new TenantAccessApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String accessName = "access"; // String | The identifier of the Access configuration.
    try {
      apiInstance.tenantAccessRegenerateSecondaryKey(apiVersion, accessName);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantAccessApi#tenantAccessRegenerateSecondaryKey");
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

<a id="tenantAccessUpdate"></a>
# **tenantAccessUpdate**
> tenantAccessUpdate(accessName, ifMatch, apiVersion, parameters)



Update tenant access information details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TenantAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    TenantAccessApi apiInstance = new TenantAccessApi(defaultClient);
    String accessName = "access"; // String | The identifier of the Access configuration.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the property to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    AccessInformationUpdateParameters parameters = new AccessInformationUpdateParameters(); // AccessInformationUpdateParameters | Parameters supplied to retrieve the Tenant Access Information.
    try {
      apiInstance.tenantAccessUpdate(accessName, ifMatch, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling TenantAccessApi#tenantAccessUpdate");
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
| **accessName** | **String**| The identifier of the Access configuration. | [enum: access] |
| **ifMatch** | **String**| The entity state (Etag) version of the property to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**AccessInformationUpdateParameters**](AccessInformationUpdateParameters.md)| Parameters supplied to retrieve the Tenant Access Information. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Tenant&#39;s access information updated successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

