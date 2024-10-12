# LexemeApi

All URIs are relative to *https://api.digitallinguistics.io/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addLexeme**](LexemeApi.md#addLexeme) | **POST** /lexemes | Add a new Lexeme |
| [**addLexemeByLanguage_0**](LexemeApi.md#addLexemeByLanguage_0) | **POST** /languages/{languageID}/lexemes | Add a new Lexeme to a Language |
| [**deleteLexeme**](LexemeApi.md#deleteLexeme) | **DELETE** /lexemes/{lexemeID} | Delete a Lexeme by ID |
| [**deleteLexemeByLanguage_0**](LexemeApi.md#deleteLexemeByLanguage_0) | **DELETE** /languages/{languageID}/lexemes/{lexemeID} | Delete a Lexeme by ID |
| [**getLexeme**](LexemeApi.md#getLexeme) | **GET** /lexemes/{lexemeID} | Get a Lexeme by ID |
| [**getLexemeByLanguage_0**](LexemeApi.md#getLexemeByLanguage_0) | **GET** /languages/{languageID}/lexemes/{lexemeID} | Get a Lexeme by ID |
| [**getLexemes**](LexemeApi.md#getLexemes) | **GET** /lexemes | Get all Lexemes |
| [**getLexemesByLanguage_0**](LexemeApi.md#getLexemesByLanguage_0) | **GET** /languages/{languageID}/lexemes | Get all Lexemes for a Language |
| [**updateLexeme**](LexemeApi.md#updateLexeme) | **PATCH** /lexemes/{lexemeID} | Perform a partial update on a Lexeme |
| [**updateLexemeByLanguage**](LexemeApi.md#updateLexemeByLanguage) | **PATCH** /languages/{languageID}/lexemes/{lexemeID} | Perform a partial update on a Lexeme |
| [**upsertLexeme**](LexemeApi.md#upsertLexeme) | **PUT** /lexemes | Upsert (add or replace) a Lexeme |
| [**upsertLexemeByLanguage_0**](LexemeApi.md#upsertLexemeByLanguage_0) | **PUT** /languages/{languageID}/lexemes | Upsert (add or replace) a Lexeme |


<a id="addLexeme"></a>
# **addLexeme**
> addLexeme(languageID)

Add a new Lexeme

Add a new Lexeme. A &#x60;languageID&#x60; must be provided either as a query parameter, or as an attribute on the Lexeme body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    try {
      apiInstance.addLexeme(languageID);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#addLexeme");
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
| **languageID** | **String**| The ID of the Language to perform the operation on | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | 201: The resource was created successfully. |  * Last-Modified - The time that the item was last modified <br>  |

<a id="addLexemeByLanguage_0"></a>
# **addLexemeByLanguage_0**
> addLexemeByLanguage_0(languageID)

Add a new Lexeme to a Language

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    try {
      apiInstance.addLexemeByLanguage_0(languageID);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#addLexemeByLanguage_0");
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
| **languageID** | **String**| The ID of the Language to perform the operation on | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | 201: The resource was created successfully. |  * Last-Modified - The time that the item was last modified <br>  |

<a id="deleteLexeme"></a>
# **deleteLexeme**
> deleteLexeme(lexemeID, ifMatch)

Delete a Lexeme by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.deleteLexeme(lexemeID, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#deleteLexeme");
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
| **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | |
| **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | 204: Delete operation successful. |  -  |

<a id="deleteLexemeByLanguage_0"></a>
# **deleteLexemeByLanguage_0**
> deleteLexemeByLanguage_0(languageID, lexemeID, ifMatch)

Delete a Lexeme by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.deleteLexemeByLanguage_0(languageID, lexemeID, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#deleteLexemeByLanguage_0");
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
| **languageID** | **String**| The ID of the Language to perform the operation on | |
| **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | |
| **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | 204: Delete operation successful. |  -  |

<a id="getLexeme"></a>
# **getLexeme**
> getLexeme(lexemeID, deleted, ifNoneMatch)

Get a Lexeme by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
    Boolean deleted = false; // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    String ifNoneMatch = "ifNoneMatch_example"; // String | If `If-None-Match` header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the `If-None-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
    try {
      apiInstance.getLexeme(lexemeID, deleted, ifNoneMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#getLexeme");
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
| **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | |
| **deleted** | **Boolean**| Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error. | [optional] [default to false] |
| **ifNoneMatch** | **String**| If &#x60;If-None-Match&#x60; header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the &#x60;If-None-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth. | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200: Operation successful. |  * dlx-continuation - A continuation token for retrieving more results <br>  * dlx-item-count - The number of items returned in the response <br>  * Last-Modified - The time that the item was last modified <br>  |
| **304** | 304: Not modified. |  -  |

<a id="getLexemeByLanguage_0"></a>
# **getLexemeByLanguage_0**
> getLexemeByLanguage_0(languageID, lexemeID, deleted, ifNoneMatch)

Get a Lexeme by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
    Boolean deleted = false; // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    String ifNoneMatch = "ifNoneMatch_example"; // String | If `If-None-Match` header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the `If-None-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
    try {
      apiInstance.getLexemeByLanguage_0(languageID, lexemeID, deleted, ifNoneMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#getLexemeByLanguage_0");
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
| **languageID** | **String**| The ID of the Language to perform the operation on | |
| **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | |
| **deleted** | **Boolean**| Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error. | [optional] [default to false] |
| **ifNoneMatch** | **String**| If &#x60;If-None-Match&#x60; header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the &#x60;If-None-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth. | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200: Operation successful. |  * dlx-continuation - A continuation token for retrieving more results <br>  * dlx-item-count - The number of items returned in the response <br>  * Last-Modified - The time that the item was last modified <br>  |
| **304** | 304: Not modified. |  -  |

<a id="getLexemes"></a>
# **getLexemes**
> getLexemes(continuation, deleted, ifModifiedSince, languageID, maxItemCount, _public)

Get all Lexemes

Retrieve all Lexemes that the authenticated user has permission to access. Include a &#x60;languageID&#x60; query parameter to limit results to Lexemes from a particular Language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String continuation = "continuation_example"; // String | The `dlx-continuation` header is used to send a continuation token with the request, when retrieving the next page of results.
    Boolean deleted = false; // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    String ifModifiedSince = "ifModifiedSince_example"; // String | The `If-Modified-Since` header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String maxItemCount = "maxItemCount_example"; // String | The `dlx-max-item-count` header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the `dlx-continuation` header.
    String _public = "false"; // String | Set this parameter to `true` to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
    try {
      apiInstance.getLexemes(continuation, deleted, ifModifiedSince, languageID, maxItemCount, _public);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#getLexemes");
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
| **continuation** | **String**| The &#x60;dlx-continuation&#x60; header is used to send a continuation token with the request, when retrieving the next page of results. | [optional] |
| **deleted** | **Boolean**| Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error. | [optional] [default to false] |
| **ifModifiedSince** | **String**| The &#x60;If-Modified-Since&#x60; header is used to retrieve only results modified since a given time. The value of this header must be a valid date string. | [optional] |
| **languageID** | **String**| The ID of the Language to perform the operation on | [optional] |
| **maxItemCount** | **String**| The &#x60;dlx-max-item-count&#x60; header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the &#x60;dlx-continuation&#x60; header. | [optional] |
| **_public** | **String**| Set this parameter to &#x60;true&#x60; to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200: Operation successful. |  * dlx-continuation - A continuation token for retrieving more results <br>  * dlx-item-count - The number of items returned in the response <br>  * Last-Modified - The time that the item was last modified <br>  |

<a id="getLexemesByLanguage_0"></a>
# **getLexemesByLanguage_0**
> getLexemesByLanguage_0(languageID, continuation, deleted, ifModifiedSince, maxItemCount, _public)

Get all Lexemes for a Language

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String continuation = "continuation_example"; // String | The `dlx-continuation` header is used to send a continuation token with the request, when retrieving the next page of results.
    Boolean deleted = false; // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    String ifModifiedSince = "ifModifiedSince_example"; // String | The `If-Modified-Since` header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
    String maxItemCount = "maxItemCount_example"; // String | The `dlx-max-item-count` header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the `dlx-continuation` header.
    String _public = "false"; // String | Set this parameter to `true` to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
    try {
      apiInstance.getLexemesByLanguage_0(languageID, continuation, deleted, ifModifiedSince, maxItemCount, _public);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#getLexemesByLanguage_0");
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
| **languageID** | **String**| The ID of the Language to perform the operation on | |
| **continuation** | **String**| The &#x60;dlx-continuation&#x60; header is used to send a continuation token with the request, when retrieving the next page of results. | [optional] |
| **deleted** | **Boolean**| Setting the &#x60;deleted&#x60; option to &#x60;true&#x60; will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error. | [optional] [default to false] |
| **ifModifiedSince** | **String**| The &#x60;If-Modified-Since&#x60; header is used to retrieve only results modified since a given time. The value of this header must be a valid date string. | [optional] |
| **maxItemCount** | **String**| The &#x60;dlx-max-item-count&#x60; header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the &#x60;dlx-continuation&#x60; header. | [optional] |
| **_public** | **String**| Set this parameter to &#x60;true&#x60; to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200: Operation successful. |  * dlx-continuation - A continuation token for retrieving more results <br>  * dlx-item-count - The number of items returned in the response <br>  * Last-Modified - The time that the item was last modified <br>  |

<a id="updateLexeme"></a>
# **updateLexeme**
> updateLexeme(lexemeID, ifMatch)

Perform a partial update on a Lexeme

Perform a partial update on a Lexeme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.updateLexeme(lexemeID, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#updateLexeme");
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
| **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | |
| **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200: Update successful. |  * Last-Modified - The time that the item was last modified <br>  |

<a id="updateLexemeByLanguage"></a>
# **updateLexemeByLanguage**
> updateLexemeByLanguage(languageID, lexemeID, ifMatch)

Perform a partial update on a Lexeme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.updateLexemeByLanguage(languageID, lexemeID, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#updateLexemeByLanguage");
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
| **languageID** | **String**| The ID of the Language to perform the operation on | |
| **lexemeID** | **String**| The ID of the Lexeme to perform the operation on | |
| **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200: Update successful. |  * Last-Modified - The time that the item was last modified <br>  |

<a id="upsertLexeme"></a>
# **upsertLexeme**
> upsertLexeme(ifMatch, languageID)

Upsert (add or replace) a Lexeme

Upsert (add or replace) a Lexeme. A &#x60;languageID&#x60; must be provided either as a query parameter, or as an attribute on the Lexeme body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    try {
      apiInstance.upsertLexeme(ifMatch, languageID);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#upsertLexeme");
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
| **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] |
| **languageID** | **String**| The ID of the Language to perform the operation on | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | 201: Upsert successful. |  * Last-Modified - The time that the item was last modified <br>  |

<a id="upsertLexemeByLanguage_0"></a>
# **upsertLexemeByLanguage_0**
> upsertLexemeByLanguage_0(languageID, ifMatch)

Upsert (add or replace) a Lexeme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LexemeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LexemeApi apiInstance = new LexemeApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.upsertLexemeByLanguage_0(languageID, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LexemeApi#upsertLexemeByLanguage_0");
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
| **languageID** | **String**| The ID of the Language to perform the operation on | |
| **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | 201: Upsert successful. |  * Last-Modified - The time that the item was last modified <br>  |

