# FieldsApi

All URIs are relative to *https://platform.climate.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllFields**](FieldsApi.md#fetchAllFields) | **GET** /v4/fields/all | Retrieve list of all Fields the user has access to. |
| [**fetchFieldById**](FieldsApi.md#fetchFieldById) | **GET** /v4/fields/{fieldId} | Retrieve a specific Field by ID |
| [**fetchFields**](FieldsApi.md#fetchFields) | **GET** /v4/fields | Retrieve list of Fields |


<a id="fetchAllFields"></a>
# **fetchAllFields**
> Fields fetchAllFields(xNextToken, xLimit, fieldName)

Retrieve list of all Fields the user has access to.

Retrieve all fields the authenticated user has access to, including fields shared with the authenticated user from other resource owners. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified. A 409 will be returned if the X-Next-Token has expired. When receiving a 409, the client should discard the X-Next-Token, discard all currently persisted fields for the user, and re-fetch fields from /fields/all.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    FieldsApi apiInstance = new FieldsApi(defaultClient);
    String xNextToken = "xNextToken_example"; // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    Integer xLimit = 56; // Integer | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    String fieldName = "fieldName_example"; // String | Optional prefix filter for field name. Must be at least 3 characters.
    try {
      Fields result = apiInstance.fetchAllFields(xNextToken, xLimit, fieldName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldsApi#fetchAllFields");
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
| **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] |
| **xLimit** | **Integer**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] |
| **fieldName** | **String**| Optional prefix filter for field name. Must be at least 3 characters. | [optional] |

### Return type

[**Fields**](Fields.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **206** | Partial Result |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **409** | Conflict |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="fetchFieldById"></a>
# **fetchFieldById**
> Field fetchFieldById(fieldId)

Retrieve a specific Field by ID

Retrieve a given **Field** by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    FieldsApi apiInstance = new FieldsApi(defaultClient);
    UUID fieldId = UUID.randomUUID(); // UUID | Unique identifier of the Field.
    try {
      Field result = apiInstance.fetchFieldById(fieldId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldsApi#fetchFieldById");
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
| **fieldId** | **UUID**| Unique identifier of the Field. | |

### Return type

[**Field**](Field.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the requested Field. |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

<a id="fetchFields"></a>
# **fetchFields**
> Fields fetchFields(xNextToken, xLimit, fieldName)

Retrieve list of Fields

Retrieve list of **Fields**. Filter the results by field name if the &#x60;fieldName&#x60; query parameter is specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    FieldsApi apiInstance = new FieldsApi(defaultClient);
    String xNextToken = "xNextToken_example"; // String | Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
    Integer xLimit = 56; // Integer | Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
    String fieldName = "fieldName_example"; // String | Optional prefix filter for field name. Must be at least 3 characters.
    try {
      Fields result = apiInstance.fetchFields(xNextToken, xLimit, fieldName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FieldsApi#fetchFields");
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
| **xNextToken** | **String**| Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes. | [optional] |
| **xLimit** | **Integer**| Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100. | [optional] |
| **fieldName** | **String**| Optional prefix filter for field name. Must be at least 3 characters. | [optional] |

### Return type

[**Fields**](Fields.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **206** | Partial Result |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **304** | Not Modified |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  * X-Next-Token - A token which may be used to poll for updates. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

