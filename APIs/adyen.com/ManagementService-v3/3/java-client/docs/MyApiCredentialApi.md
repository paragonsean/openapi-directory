# MyApiCredentialApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMeAllowedOriginsOriginId**](MyApiCredentialApi.md#deleteMeAllowedOriginsOriginId) | **DELETE** /me/allowedOrigins/{originId} | Remove allowed origin |
| [**getMe**](MyApiCredentialApi.md#getMe) | **GET** /me | Get API credential details |
| [**getMeAllowedOrigins**](MyApiCredentialApi.md#getMeAllowedOrigins) | **GET** /me/allowedOrigins | Get allowed origins |
| [**getMeAllowedOriginsOriginId**](MyApiCredentialApi.md#getMeAllowedOriginsOriginId) | **GET** /me/allowedOrigins/{originId} | Get allowed origin details |
| [**postMeAllowedOrigins**](MyApiCredentialApi.md#postMeAllowedOrigins) | **POST** /me/allowedOrigins | Add allowed origin |
| [**postMeGenerateClientKey**](MyApiCredentialApi.md#postMeGenerateClientKey) | **POST** /me/generateClientKey | Generate a client key |


<a id="deleteMeAllowedOriginsOriginId"></a>
# **deleteMeAllowedOriginsOriginId**
> deleteMeAllowedOriginsOriginId(originId)

Remove allowed origin

Removes the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) specified in the path. The API key from the request is used to identify the [API credential](https://docs.adyen.com/development-resources/api-credentials).  You can make this request with any of the Management API roles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApiCredentialApi;

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

    MyApiCredentialApi apiInstance = new MyApiCredentialApi(defaultClient);
    String originId = "originId_example"; // String | Unique identifier of the allowed origin.
    try {
      apiInstance.deleteMeAllowedOriginsOriginId(originId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApiCredentialApi#deleteMeAllowedOriginsOriginId");
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

<a id="getMe"></a>
# **getMe**
> MeApiCredential getMe()

Get API credential details

Returns your [API credential](https://docs.adyen.com/development-resources/api-credentials) details based on the API Key you used in the request.  You can make this request with any of the Management API roles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApiCredentialApi;

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

    MyApiCredentialApi apiInstance = new MyApiCredentialApi(defaultClient);
    try {
      MeApiCredential result = apiInstance.getMe();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApiCredentialApi#getMe");
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

[**MeApiCredential**](MeApiCredential.md)

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

<a id="getMeAllowedOrigins"></a>
# **getMeAllowedOrigins**
> AllowedOriginsResponse getMeAllowedOrigins()

Get allowed origins

Returns the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) of your [API credential](https://docs.adyen.com/development-resources/api-credentials) based on the API key you used in the request.  You can make this request with any of the Management API roles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApiCredentialApi;

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

    MyApiCredentialApi apiInstance = new MyApiCredentialApi(defaultClient);
    try {
      AllowedOriginsResponse result = apiInstance.getMeAllowedOrigins();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApiCredentialApi#getMeAllowedOrigins");
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

<a id="getMeAllowedOriginsOriginId"></a>
# **getMeAllowedOriginsOriginId**
> AllowedOrigin getMeAllowedOriginsOriginId(originId)

Get allowed origin details

Returns the details of the [allowed origin](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) specified in the path. The API key from the request is used to identify the [API credential](https://docs.adyen.com/development-resources/api-credentials).  You can make this request with any of the Management API roles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApiCredentialApi;

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

    MyApiCredentialApi apiInstance = new MyApiCredentialApi(defaultClient);
    String originId = "originId_example"; // String | Unique identifier of the allowed origin.
    try {
      AllowedOrigin result = apiInstance.getMeAllowedOriginsOriginId(originId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApiCredentialApi#getMeAllowedOriginsOriginId");
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

<a id="postMeAllowedOrigins"></a>
# **postMeAllowedOrigins**
> AllowedOrigin postMeAllowedOrigins(createAllowedOriginRequest)

Add allowed origin

Adds an allowed origin to the list of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) of your API credential. The API key from the request is used to identify the [API credential](https://docs.adyen.com/development-resources/api-credentials).  You can make this request with any of the Management API roles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApiCredentialApi;

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

    MyApiCredentialApi apiInstance = new MyApiCredentialApi(defaultClient);
    CreateAllowedOriginRequest createAllowedOriginRequest = new CreateAllowedOriginRequest(); // CreateAllowedOriginRequest | 
    try {
      AllowedOrigin result = apiInstance.postMeAllowedOrigins(createAllowedOriginRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApiCredentialApi#postMeAllowedOrigins");
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
| **createAllowedOriginRequest** | [**CreateAllowedOriginRequest**](CreateAllowedOriginRequest.md)|  | [optional] |

### Return type

[**AllowedOrigin**](AllowedOrigin.md)

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

<a id="postMeGenerateClientKey"></a>
# **postMeGenerateClientKey**
> GenerateClientKeyResponse postMeGenerateClientKey()

Generate a client key

Generates a new [client key](https://docs.adyen.com/development-resources/client-side-authentication/) used to authenticate requests from your payment environment. You can use the new client key a few minutes after generating it. The old client key stops working 24 hours after generating a new one.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApiCredentialApi;

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

    MyApiCredentialApi apiInstance = new MyApiCredentialApi(defaultClient);
    try {
      GenerateClientKeyResponse result = apiInstance.postMeGenerateClientKey();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApiCredentialApi#postMeGenerateClientKey");
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

[**GenerateClientKeyResponse**](GenerateClientKeyResponse.md)

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

