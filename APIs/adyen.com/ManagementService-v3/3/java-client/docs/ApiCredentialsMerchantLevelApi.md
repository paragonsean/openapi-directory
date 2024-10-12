# ApiCredentialsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMerchantsMerchantIdApiCredentials**](ApiCredentialsMerchantLevelApi.md#getMerchantsMerchantIdApiCredentials) | **GET** /merchants/{merchantId}/apiCredentials | Get a list of API credentials |
| [**getMerchantsMerchantIdApiCredentialsApiCredentialId**](ApiCredentialsMerchantLevelApi.md#getMerchantsMerchantIdApiCredentialsApiCredentialId) | **GET** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Get an API credential |
| [**patchMerchantsMerchantIdApiCredentialsApiCredentialId**](ApiCredentialsMerchantLevelApi.md#patchMerchantsMerchantIdApiCredentialsApiCredentialId) | **PATCH** /merchants/{merchantId}/apiCredentials/{apiCredentialId} | Update an API credential |
| [**postMerchantsMerchantIdApiCredentials**](ApiCredentialsMerchantLevelApi.md#postMerchantsMerchantIdApiCredentials) | **POST** /merchants/{merchantId}/apiCredentials | Create an API credential |


<a id="getMerchantsMerchantIdApiCredentials"></a>
# **getMerchantsMerchantIdApiCredentials**
> ListMerchantApiCredentialsResponse getMerchantsMerchantIdApiCredentials(merchantId, pageNumber, pageSize)

Get a list of API credentials

Returns the list of [API credentials](https://docs.adyen.com/development-resources/api-credentials) for the merchant account. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiCredentialsMerchantLevelApi;

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

    ApiCredentialsMerchantLevelApi apiInstance = new ApiCredentialsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    Integer pageNumber = 56; // Integer | The number of the page to fetch.
    Integer pageSize = 56; // Integer | The number of items to have on a page, maximum 100. The default is 10 items on a page.
    try {
      ListMerchantApiCredentialsResponse result = apiInstance.getMerchantsMerchantIdApiCredentials(merchantId, pageNumber, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiCredentialsMerchantLevelApi#getMerchantsMerchantIdApiCredentials");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **pageNumber** | **Integer**| The number of the page to fetch. | [optional] |
| **pageSize** | **Integer**| The number of items to have on a page, maximum 100. The default is 10 items on a page. | [optional] |

### Return type

[**ListMerchantApiCredentialsResponse**](ListMerchantApiCredentialsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getMerchantsMerchantIdApiCredentialsApiCredentialId"></a>
# **getMerchantsMerchantIdApiCredentialsApiCredentialId**
> ApiCredential getMerchantsMerchantIdApiCredentialsApiCredentialId(merchantId, apiCredentialId)

Get an API credential

Returns the [API credential](https://docs.adyen.com/development-resources/api-credentials) identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiCredentialsMerchantLevelApi;

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

    ApiCredentialsMerchantLevelApi apiInstance = new ApiCredentialsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
    try {
      ApiCredential result = apiInstance.getMerchantsMerchantIdApiCredentialsApiCredentialId(merchantId, apiCredentialId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiCredentialsMerchantLevelApi#getMerchantsMerchantIdApiCredentialsApiCredentialId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **apiCredentialId** | **String**| Unique identifier of the API credential. | |

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchMerchantsMerchantIdApiCredentialsApiCredentialId"></a>
# **patchMerchantsMerchantIdApiCredentialsApiCredentialId**
> ApiCredential patchMerchantsMerchantIdApiCredentialsApiCredentialId(merchantId, apiCredentialId, updateMerchantApiCredentialRequest)

Update an API credential

Changes the API credential&#39;s roles, or allowed origins. The request has the new values for the fields you want to change. The response contains the full updated API credential, including the new values from the request.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiCredentialsMerchantLevelApi;

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

    ApiCredentialsMerchantLevelApi apiInstance = new ApiCredentialsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String apiCredentialId = "apiCredentialId_example"; // String | Unique identifier of the API credential.
    UpdateMerchantApiCredentialRequest updateMerchantApiCredentialRequest = new UpdateMerchantApiCredentialRequest(); // UpdateMerchantApiCredentialRequest | 
    try {
      ApiCredential result = apiInstance.patchMerchantsMerchantIdApiCredentialsApiCredentialId(merchantId, apiCredentialId, updateMerchantApiCredentialRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiCredentialsMerchantLevelApi#patchMerchantsMerchantIdApiCredentialsApiCredentialId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **apiCredentialId** | **String**| Unique identifier of the API credential. | |
| **updateMerchantApiCredentialRequest** | [**UpdateMerchantApiCredentialRequest**](UpdateMerchantApiCredentialRequest.md)|  | [optional] |

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postMerchantsMerchantIdApiCredentials"></a>
# **postMerchantsMerchantIdApiCredentials**
> CreateApiCredentialResponse postMerchantsMerchantIdApiCredentials(merchantId, createMerchantApiCredentialRequest)

Create an API credential

Creates an [API credential](https://docs.adyen.com/development-resources/api-credentials) for the company account identified in the path. In the request, you can specify the roles and allowed origins for the new API credential.  The response includes the: * [API key](https://docs.adyen.com/development-resources/api-authentication#api-key-authentication): used for API request authentication. * [Client key](https://docs.adyen.com/development-resources/client-side-authentication#how-it-works): public key used for client-side authentication. * [Username and password](https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication): used for basic authentication.  &gt; Make sure you store the API key securely in your system. You won&#39;t be able to retrieve it later.  If your API key is lost or compromised, you need to [generate a new API key](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey).  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiCredentialsMerchantLevelApi;

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

    ApiCredentialsMerchantLevelApi apiInstance = new ApiCredentialsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    CreateMerchantApiCredentialRequest createMerchantApiCredentialRequest = new CreateMerchantApiCredentialRequest(); // CreateMerchantApiCredentialRequest | 
    try {
      CreateApiCredentialResponse result = apiInstance.postMerchantsMerchantIdApiCredentials(merchantId, createMerchantApiCredentialRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiCredentialsMerchantLevelApi#postMerchantsMerchantIdApiCredentials");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **createMerchantApiCredentialRequest** | [**CreateMerchantApiCredentialRequest**](CreateMerchantApiCredentialRequest.md)|  | [optional] |

### Return type

[**CreateApiCredentialResponse**](CreateApiCredentialResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

