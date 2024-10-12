# AllowedOriginsCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId**](AllowedOriginsCompanyLevelApi.md#deleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId) | **DELETE** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Delete an allowed origin |
| [**getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins**](AllowedOriginsCompanyLevelApi.md#getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | Get a list of allowed origins |
| [**getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId**](AllowedOriginsCompanyLevelApi.md#getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId) | **GET** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins/{originId} | Get an allowed origin |
| [**postCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins**](AllowedOriginsCompanyLevelApi.md#postCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins) | **POST** /companies/{companyId}/apiCredentials/{apiCredentialId}/allowedOrigins | Create an allowed origin |


<a id="deleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId"></a>
# **deleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId**
> deleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId(companyId, apiCredentialId, originId)

Delete an allowed origin

Removes the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path. As soon as an allowed origin is removed, we no longer accept client-side requests from that domain.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllowedOriginsCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AllowedOriginsCompanyLevelApi apiInstance = new AllowedOriginsCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
    String originId = "originId_example"; // String | Unique identifier of the allowed origin.
    try {
      apiInstance.deleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId(companyId, apiCredentialId, originId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllowedOriginsCompanyLevelApi#deleteCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **apiCredentialId** | **String**| Unique identifier of the API credential. | |
| **originId** | **String**| Unique identifier of the allowed origin. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content - look at the actual response code for the status of the request.  |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins"></a>
# **getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins**
> AllowedOriginsResponse getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins(companyId, apiCredentialId)

Get a list of allowed origins

Returns the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the API credential identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllowedOriginsCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AllowedOriginsCompanyLevelApi apiInstance = new AllowedOriginsCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
    try {
      AllowedOriginsResponse result = apiInstance.getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins(companyId, apiCredentialId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllowedOriginsCompanyLevelApi#getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **apiCredentialId** | **String**| Unique identifier of the API credential. | |

### Return type

[**AllowedOriginsResponse**](AllowedOriginsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId"></a>
# **getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId**
> AllowedOrigin getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId(companyId, apiCredentialId, originId)

Get an allowed origin

Returns the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllowedOriginsCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AllowedOriginsCompanyLevelApi apiInstance = new AllowedOriginsCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
    String originId = "originId_example"; // String | Unique identifier of the allowed origin.
    try {
      AllowedOrigin result = apiInstance.getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId(companyId, apiCredentialId, originId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllowedOriginsCompanyLevelApi#getCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOriginsOriginId");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **apiCredentialId** | **String**| Unique identifier of the API credential. | |
| **originId** | **String**| Unique identifier of the allowed origin. | |

### Return type

[**AllowedOrigin**](AllowedOrigin.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins"></a>
# **postCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins**
> AllowedOriginsResponse postCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins(companyId, apiCredentialId, allowedOrigin)

Create an allowed origin

Adds a new [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) to the API credential&#39;s list of allowed origins.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllowedOriginsCompanyLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AllowedOriginsCompanyLevelApi apiInstance = new AllowedOriginsCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
    AllowedOrigin allowedOrigin = new AllowedOrigin(); // AllowedOrigin | 
    try {
      AllowedOriginsResponse result = apiInstance.postCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins(companyId, apiCredentialId, allowedOrigin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllowedOriginsCompanyLevelApi#postCompaniesCompanyIdApiCredentialsApiCredentialIdAllowedOrigins");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **apiCredentialId** | **String**| Unique identifier of the API credential. | |
| **allowedOrigin** | [**AllowedOrigin**](AllowedOrigin.md)|  | [optional] |

### Return type

[**AllowedOriginsResponse**](AllowedOriginsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

