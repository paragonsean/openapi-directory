# LanguageApi

All URIs are relative to *https://api.digitallinguistics.io/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addLanguage**](LanguageApi.md#addLanguage) | **POST** /languages | Add a new Language |
| [**addLexemeByLanguage**](LanguageApi.md#addLexemeByLanguage) | **POST** /languages/{languageID}/lexemes | Add a new Lexeme to a Language |
| [**deleteLanguage**](LanguageApi.md#deleteLanguage) | **DELETE** /languages/{languageID} | Delete a Language by ID |
| [**deleteLexemeByLanguage**](LanguageApi.md#deleteLexemeByLanguage) | **DELETE** /languages/{languageID}/lexemes/{lexemeID} | Delete a Lexeme by ID |
| [**getLanguage**](LanguageApi.md#getLanguage) | **GET** /languages/{languageID} | Retrieve a Language by ID |
| [**getLanguages**](LanguageApi.md#getLanguages) | **GET** /languages | Get all Languages |
| [**getLexemeByLanguage**](LanguageApi.md#getLexemeByLanguage) | **GET** /languages/{languageID}/lexemes/{lexemeID} | Get a Lexeme by ID |
| [**getLexemesByLanguage**](LanguageApi.md#getLexemesByLanguage) | **GET** /languages/{languageID}/lexemes | Get all Lexemes for a Language |
| [**updateLanguage**](LanguageApi.md#updateLanguage) | **PATCH** /languages/{languageID} | Perform a partial update on a Language |
| [**upsertLanguage**](LanguageApi.md#upsertLanguage) | **PUT** /languages | Upsert (create or replace) a Language |
| [**upsertLexemeByLanguage**](LanguageApi.md#upsertLexemeByLanguage) | **PUT** /languages/{languageID}/lexemes | Upsert (add or replace) a Lexeme |


<a id="addLanguage"></a>
# **addLanguage**
> addLanguage(body)

Add a new Language

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    Object body = null; // Object | A database resource to upsert
    try {
      apiInstance.addLanguage(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#addLanguage");
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
| **body** | **Object**| A database resource to upsert | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | 201: The resource was created successfully. |  * Last-Modified - The time that the item was last modified <br>  |

<a id="addLexemeByLanguage"></a>
# **addLexemeByLanguage**
> addLexemeByLanguage(languageID)

Add a new Lexeme to a Language

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    try {
      apiInstance.addLexemeByLanguage(languageID);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#addLexemeByLanguage");
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

<a id="deleteLanguage"></a>
# **deleteLanguage**
> deleteLanguage(languageID, ifMatch)

Delete a Language by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.deleteLanguage(languageID, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#deleteLanguage");
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
| **204** | 204: Delete operation successful. |  -  |

<a id="deleteLexemeByLanguage"></a>
# **deleteLexemeByLanguage**
> deleteLexemeByLanguage(languageID, lexemeID, ifMatch)

Delete a Lexeme by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.deleteLexemeByLanguage(languageID, lexemeID, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#deleteLexemeByLanguage");
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

<a id="getLanguage"></a>
# **getLanguage**
> getLanguage(languageID, deleted, ifNoneMatch)

Retrieve a Language by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    Boolean deleted = false; // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    String ifNoneMatch = "ifNoneMatch_example"; // String | If `If-None-Match` header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the `If-None-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
    try {
      apiInstance.getLanguage(languageID, deleted, ifNoneMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#getLanguage");
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

<a id="getLanguages"></a>
# **getLanguages**
> getLanguages(continuation, deleted, ifModifiedSince, maxItemCount, _public)

Get all Languages

Retrieves all the Languages that the authenticated user or client has permission to access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    String continuation = "continuation_example"; // String | The `dlx-continuation` header is used to send a continuation token with the request, when retrieving the next page of results.
    Boolean deleted = false; // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    String ifModifiedSince = "ifModifiedSince_example"; // String | The `If-Modified-Since` header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
    String maxItemCount = "maxItemCount_example"; // String | The `dlx-max-item-count` header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the `dlx-continuation` header.
    String _public = "false"; // String | Set this parameter to `true` to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
    try {
      apiInstance.getLanguages(continuation, deleted, ifModifiedSince, maxItemCount, _public);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#getLanguages");
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

<a id="getLexemeByLanguage"></a>
# **getLexemeByLanguage**
> getLexemeByLanguage(languageID, lexemeID, deleted, ifNoneMatch)

Get a Lexeme by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String lexemeID = "lexemeID_example"; // String | The ID of the Lexeme to perform the operation on
    Boolean deleted = false; // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    String ifNoneMatch = "ifNoneMatch_example"; // String | If `If-None-Match` header is used with GET requests to check whether you already have the most up-to-date version of the resource, and therefore do not need the resource sent again. The value of the `If-None-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to reduce bandwidth.
    try {
      apiInstance.getLexemeByLanguage(languageID, lexemeID, deleted, ifNoneMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#getLexemeByLanguage");
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

<a id="getLexemesByLanguage"></a>
# **getLexemesByLanguage**
> getLexemesByLanguage(languageID, continuation, deleted, ifModifiedSince, maxItemCount, _public)

Get all Lexemes for a Language

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String continuation = "continuation_example"; // String | The `dlx-continuation` header is used to send a continuation token with the request, when retrieving the next page of results.
    Boolean deleted = false; // Boolean | Setting the `deleted` option to `true` will return results that have been marked for deletion, but not yet deleted from the database. Otherwise requests for a resource marked for deletion will return a 410 error.
    String ifModifiedSince = "ifModifiedSince_example"; // String | The `If-Modified-Since` header is used to retrieve only results modified since a given time. The value of this header must be a valid date string.
    String maxItemCount = "maxItemCount_example"; // String | The `dlx-max-item-count` header is used to limit the number of results to a certain amount at a time (by default all results will be returned). If there are more results to be returned, a continuation token will also be sent in the `dlx-continuation` header.
    String _public = "false"; // String | Set this parameter to `true` to include all publicly-accessible resources, not just those that the user is listed as an Owner, Contributor, or Viewer for.
    try {
      apiInstance.getLexemesByLanguage(languageID, continuation, deleted, ifModifiedSince, maxItemCount, _public);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#getLexemesByLanguage");
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

<a id="updateLanguage"></a>
# **updateLanguage**
> updateLanguage(languageID, body, ifMatch)

Perform a partial update on a Language

Performs a partial update the Language whose ID is specified in the URL. If the Language object has an &#x60;id&#x60; property, is ignored in favor of the ID in the URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    Object body = null; // Object | A database resource to upsert
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.updateLanguage(languageID, body, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#updateLanguage");
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
| **body** | **Object**| A database resource to upsert | |
| **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200: Update successful. |  * Last-Modified - The time that the item was last modified <br>  |

<a id="upsertLanguage"></a>
# **upsertLanguage**
> upsertLanguage(body, ifMatch)

Upsert (create or replace) a Language

Creates a Language if it does not yet exist (i.e. if the resource does not have an &#x60;id&#x60; property yet), or replaces the existing Language resource if it does. Note that this replaces the *entire* Language. It is not a partial update.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    Object body = null; // Object | A database resource to upsert
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.upsertLanguage(body, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#upsertLanguage");
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
| **body** | **Object**| A database resource to upsert | |
| **ifMatch** | **String**| The &#x60;If-Match&#x60; header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the &#x60;If-Match&#x60; header is the ETag (&#x60;_etag&#x60;) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts. | [optional] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | 201: Upsert successful. |  * Last-Modified - The time that the item was last modified <br>  |

<a id="upsertLexemeByLanguage"></a>
# **upsertLexemeByLanguage**
> upsertLexemeByLanguage(languageID, ifMatch)

Upsert (add or replace) a Lexeme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digitallinguistics.io/v0");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    String languageID = "languageID_example"; // String | The ID of the Language to perform the operation on
    String ifMatch = "ifMatch_example"; // String | The `If-Match` header is used with PUT and DELETE requests to check whether you have the most up-to-date version of the resource before updating or deleting it. The value of the `If-Match` header is the ETag (`_etag`) property of the resource. It is recommended that your application use this header whenever possible to avoid data conflicts.
    try {
      apiInstance.upsertLexemeByLanguage(languageID, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#upsertLexemeByLanguage");
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

