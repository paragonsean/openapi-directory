# StringsApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clearTranslationCache**](StringsApi.md#clearTranslationCache) | **DELETE** /continuous_projects/{projectId}/strings/cached | Clear translation cache |
| [**getContinuousProjectFileStrings**](StringsApi.md#getContinuousProjectFileStrings) | **GET** /continuous_projects/{projectId}/documents/{documentId}/strings | View strings their translations in a continuous document |
| [**getContinuousProjectStrings**](StringsApi.md#getContinuousProjectStrings) | **GET** /continuous_projects/{projectId}/strings | View strings and translations in continuous project |
| [**getDocumentTranslations**](StringsApi.md#getDocumentTranslations) | **GET** /projects/{projectId}/documents/{documentId}/translations | View strings and translations of a document |
| [**getDocumentTranslationsForLanguage**](StringsApi.md#getDocumentTranslationsForLanguage) | **GET** /projects/{projectId}/documents/{documentId}/translations/{language} | View strings and translations of a document for target language |
| [**getProjectStrings**](StringsApi.md#getProjectStrings) | **GET** /projects/{projectId}/strings | View project strings and translations |
| [**getProjectStringsForLanguage**](StringsApi.md#getProjectStringsForLanguage) | **GET** /projects/{projectId}/strings/{language} | View strings and translations for target language |
| [**getProjectTranslations**](StringsApi.md#getProjectTranslations) | **GET** /projects/{projectId}/translations | Deprecated. Use /projects/{projectId}/strings instead. |
| [**getProjectTranslationsForLanguage**](StringsApi.md#getProjectTranslationsForLanguage) | **GET** /projects/{projectId}/translations/{language} | Deprecated. use /projects/{projectId}/strings/{language} instead. |
| [**getStrings**](StringsApi.md#getStrings) | **GET** /strings | View account strings (translation memory) |
| [**getTranslationCache**](StringsApi.md#getTranslationCache) | **GET** /continuous_projects/{projectId}/strings/cached | View cached strings translations in continuous project |
| [**packageProjectTranslationMemory**](StringsApi.md#packageProjectTranslationMemory) | **POST** /projects/{projectId}/strings/package | Download project translation memory |
| [**packageProjectTranslationMemoryForLanguage**](StringsApi.md#packageProjectTranslationMemoryForLanguage) | **POST** /projects/{projectId}/strings/{languageCode}/package | Download language-specific project translation memory |
| [**packageProjectTranslationMemoryForLanguageStatus**](StringsApi.md#packageProjectTranslationMemoryForLanguageStatus) | **GET** /projects/{projectId}/strings/{languageCode}/package/status | Check language-specific translation memory packaging status |
| [**packageProjectTranslationMemoryStatus**](StringsApi.md#packageProjectTranslationMemoryStatus) | **GET** /projects/{projectId}/strings/package/status | Check translation memory packaging status |
| [**packageUserTranslationMemory**](StringsApi.md#packageUserTranslationMemory) | **POST** /strings/{languageCode}/package | Download account translation memory |
| [**packageUserTranslationMemoryForLanguageStatus**](StringsApi.md#packageUserTranslationMemoryForLanguageStatus) | **GET** /strings/{languageCode}/package/status | Check account translation memory packaging status |
| [**postContinuousProjectFileStrings**](StringsApi.md#postContinuousProjectFileStrings) | **POST** /continuous_projects/{projectId}/documents/strings | Get a list of strings and its translations in the project. |
| [**recacheTranslations**](StringsApi.md#recacheTranslations) | **POST** /continuous_projects/{projectId}/strings/recache-tms | Recache translations |
| [**updateTranslationMemoryUnit**](StringsApi.md#updateTranslationMemoryUnit) | **PUT** /strings | Update string translation |


<a id="clearTranslationCache"></a>
# **clearTranslationCache**
> OperationStatus clearTranslationCache(projectId, locale, fileId)

Clear translation cache

Clear/delete continuous project translation cache.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    String locale = "locale_example"; // String | Locale
    Long fileId = 56L; // Long | Continuous Project File ID
    try {
      OperationStatus result = apiInstance.clearTranslationCache(projectId, locale, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#clearTranslationCache");
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
| **projectId** | **Long**| Project ID | |
| **locale** | **String**| Locale | [optional] |
| **fileId** | **Long**| Continuous Project File ID | [optional] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Operation response |  -  |

<a id="getContinuousProjectFileStrings"></a>
# **getContinuousProjectFileStrings**
> StringList getContinuousProjectFileStrings(projectId, documentId)

View strings their translations in a continuous document

View the strings from a document and their translations in your continuous translation project, for all target languages. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long documentId = 179469L; // Long | Document ID/Name
    try {
      StringList result = apiInstance.getContinuousProjectFileStrings(projectId, documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getContinuousProjectFileStrings");
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
| **projectId** | **Long**| Project ID | |
| **documentId** | **Long**| Document ID/Name | |

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="getContinuousProjectStrings"></a>
# **getContinuousProjectStrings**
> StringList getContinuousProjectStrings(projectId)

View strings and translations in continuous project

View the strings and their translations in your continuous translation project, for all target languages. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    try {
      StringList result = apiInstance.getContinuousProjectStrings(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getContinuousProjectStrings");
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
| **projectId** | **Long**| Project ID | |

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="getDocumentTranslations"></a>
# **getDocumentTranslations**
> StringList getDocumentTranslations(projectId, documentId)

View strings and translations of a document

View the strings and their translations in your translation project for the specified source document. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long documentId = 179469L; // Long | Document ID
    try {
      StringList result = apiInstance.getDocumentTranslations(projectId, documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getDocumentTranslations");
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
| **projectId** | **Long**| Project ID | |
| **documentId** | **Long**| Document ID | |

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="getDocumentTranslationsForLanguage"></a>
# **getDocumentTranslationsForLanguage**
> StringList getDocumentTranslationsForLanguage(projectId, documentId, language)

View strings and translations of a document for target language

View the strings and their translations in the given target language for the specified source document. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long documentId = 179469L; // Long | Document ID
    String language = "en-US"; // String | Target language code.
    try {
      StringList result = apiInstance.getDocumentTranslationsForLanguage(projectId, documentId, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getDocumentTranslationsForLanguage");
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
| **projectId** | **Long**| Project ID | |
| **documentId** | **Long**| Document ID | |
| **language** | **String**| Target language code. | |

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="getProjectStrings"></a>
# **getProjectStrings**
> StringList getProjectStrings(projectId)

View project strings and translations

View the strings and their translations in your translation project, for all target languages. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    try {
      StringList result = apiInstance.getProjectStrings(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getProjectStrings");
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
| **projectId** | **Long**| Project ID | |

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="getProjectStringsForLanguage"></a>
# **getProjectStringsForLanguage**
> StringList getProjectStringsForLanguage(projectId, language)

View strings and translations for target language

View the strings and their translations in your translation project for the specified target language. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    String language = "en-US"; // String | Target language code
    try {
      StringList result = apiInstance.getProjectStringsForLanguage(projectId, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getProjectStringsForLanguage");
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
| **projectId** | **Long**| Project ID | |
| **language** | **String**| Target language code | |

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="getProjectTranslations"></a>
# **getProjectTranslations**
> StringList getProjectTranslations(projectId)

Deprecated. Use /projects/{projectId}/strings instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    try {
      StringList result = apiInstance.getProjectTranslations(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getProjectTranslations");
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
| **projectId** | **Long**| Project ID | |

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="getProjectTranslationsForLanguage"></a>
# **getProjectTranslationsForLanguage**
> StringList getProjectTranslationsForLanguage(projectId, language)

Deprecated. use /projects/{projectId}/strings/{language} instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    String language = "en-US"; // String | Target language code
    try {
      StringList result = apiInstance.getProjectTranslationsForLanguage(projectId, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getProjectTranslationsForLanguage");
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
| **projectId** | **Long**| Project ID | |
| **language** | **String**| Target language code | |

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="getStrings"></a>
# **getStrings**
> ClientStrings getStrings(sourceLanguage, page)

View account strings (translation memory)

Get a list of all strings and their translations under your account, from all projects. This is your MotaWord translation memory. If you have the related permission, this endpoint will also return strings from your company account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    String sourceLanguage = "sourceLanguage_example"; // String | Source Language Code
    Long page = 0L; // Long | Requested page
    try {
      ClientStrings result = apiInstance.getStrings(sourceLanguage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getStrings");
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
| **sourceLanguage** | **String**| Source Language Code | [optional] |
| **page** | **Long**| Requested page | [optional] [default to 0] |

### Return type

[**ClientStrings**](ClientStrings.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of strings in JSON |  -  |

<a id="getTranslationCache"></a>
# **getTranslationCache**
> ContinuousProjectCache getTranslationCache(projectId, flatten)

View cached strings translations in continuous project

MotaWord caches your account intensively (and in a smart way) in real-time translation environments. This endpoint will return the currently cached strings and translations in your continuous translation project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Boolean flatten = true; // Boolean | Flatten cache results and ignore document keys
    try {
      ContinuousProjectCache result = apiInstance.getTranslationCache(projectId, flatten);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#getTranslationCache");
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
| **projectId** | **Long**| Project ID | |
| **flatten** | **Boolean**| Flatten cache results and ignore document keys | [optional] |

### Return type

[**ContinuousProjectCache**](ContinuousProjectCache.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="packageProjectTranslationMemory"></a>
# **packageProjectTranslationMemory**
> AsyncOperationStatus packageProjectTranslationMemory(projectId, async, format)

Download project translation memory

Package and download project translation memory in TMX format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long async = 0L; // Long | If you want to package and download the translation memory synchronously, mark this parameter as '0'. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call.
    String format = "tmx"; // String | Translation Memory file format
    try {
      AsyncOperationStatus result = apiInstance.packageProjectTranslationMemory(projectId, async, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#packageProjectTranslationMemory");
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
| **projectId** | **Long**| Project ID | |
| **async** | **Long**| If you want to package and download the translation memory synchronously, mark this parameter as &#39;0&#39;. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call. | [optional] [default to 0] |
| **format** | **String**| Translation Memory file format | [optional] [default to tmx] |

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response in TMX or async request |  -  |

<a id="packageProjectTranslationMemoryForLanguage"></a>
# **packageProjectTranslationMemoryForLanguage**
> AsyncOperationStatus packageProjectTranslationMemoryForLanguage(projectId, languageCode, async, format)

Download language-specific project translation memory

Package and download project translation memory in TMX format for a specific target language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    String languageCode = "en-US"; // String | Language Code
    Long async = 0L; // Long | If you want to package and download the translation memory synchronously, mark this parameter as '0'. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call.
    String format = "tmx"; // String | Translation Memory file format
    try {
      AsyncOperationStatus result = apiInstance.packageProjectTranslationMemoryForLanguage(projectId, languageCode, async, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#packageProjectTranslationMemoryForLanguage");
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
| **projectId** | **Long**| Project ID | |
| **languageCode** | **String**| Language Code | |
| **async** | **Long**| If you want to package and download the translation memory synchronously, mark this parameter as &#39;0&#39;. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call. | [optional] [default to 0] |
| **format** | **String**| Translation Memory file format | [optional] [default to tmx] |

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response in TMX or async request |  -  |

<a id="packageProjectTranslationMemoryForLanguageStatus"></a>
# **packageProjectTranslationMemoryForLanguageStatus**
> AsyncOperationStatus packageProjectTranslationMemoryForLanguageStatus(projectId, languageCode, asyncRequestKey)

Check language-specific translation memory packaging status

Check translation memory packaging status for async packaging requests, using the key returned from strings/package call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    String languageCode = "en-US"; // String | Language Code
    String asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
    try {
      AsyncOperationStatus result = apiInstance.packageProjectTranslationMemoryForLanguageStatus(projectId, languageCode, asyncRequestKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#packageProjectTranslationMemoryForLanguageStatus");
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
| **projectId** | **Long**| Project ID | |
| **languageCode** | **String**| Language Code | |
| **asyncRequestKey** | **String**| Async operation key | |

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Async operation status. Use the key to query status of this operation. |  -  |

<a id="packageProjectTranslationMemoryStatus"></a>
# **packageProjectTranslationMemoryStatus**
> AsyncOperationStatus packageProjectTranslationMemoryStatus(projectId, asyncRequestKey)

Check translation memory packaging status

Check translation memory packaging status for async packaging requests, using the key returned from strings/package call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    String asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
    try {
      AsyncOperationStatus result = apiInstance.packageProjectTranslationMemoryStatus(projectId, asyncRequestKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#packageProjectTranslationMemoryStatus");
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
| **projectId** | **Long**| Project ID | |
| **asyncRequestKey** | **String**| Async operation key | |

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Async operation status. Use the key to query status of this operation. |  -  |

<a id="packageUserTranslationMemory"></a>
# **packageUserTranslationMemory**
> AsyncOperationStatus packageUserTranslationMemory(languageCode, async, email)

Download account translation memory

Package and download account translation memory in TMX format. If you have the related permission, this will also download your company translation memory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    String languageCode = "en-US"; // String | Source Language Code
    Long async = 0L; // Long | If you want to package and download the translation memory synchronously, mark this parameter as '0'. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call.
    Long email = 1L; // Long | If you don't need us to email the TMX, set this to '0'. Default is 1.
    try {
      AsyncOperationStatus result = apiInstance.packageUserTranslationMemory(languageCode, async, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#packageUserTranslationMemory");
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
| **languageCode** | **String**| Source Language Code | |
| **async** | **Long**| If you want to package and download the translation memory synchronously, mark this parameter as &#39;0&#39;. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call. | [optional] [default to 0] |
| **email** | **Long**| If you don&#39;t need us to email the TMX, set this to &#39;0&#39;. Default is 1. | [optional] [default to 1] |

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response in TMX or async request |  -  |

<a id="packageUserTranslationMemoryForLanguageStatus"></a>
# **packageUserTranslationMemoryForLanguageStatus**
> AsyncOperationStatus packageUserTranslationMemoryForLanguageStatus(languageCode, asyncRequestKey)

Check account translation memory packaging status

Check translation memory packaging status for async packaging requests, using the key returned from strings/package call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    String languageCode = "en-US"; // String | Language Code
    String asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
    try {
      AsyncOperationStatus result = apiInstance.packageUserTranslationMemoryForLanguageStatus(languageCode, asyncRequestKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#packageUserTranslationMemoryForLanguageStatus");
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
| **languageCode** | **String**| Language Code | |
| **asyncRequestKey** | **String**| Async operation key | |

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Async operation status. Use the key to query status of this operation. |  -  |

<a id="postContinuousProjectFileStrings"></a>
# **postContinuousProjectFileStrings**
> StringList postContinuousProjectFileStrings(projectId, continuousProjectDocumentStringsBody)

Get a list of strings and its translations in the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    ContinuousProjectDocumentStringsBody continuousProjectDocumentStringsBody = new ContinuousProjectDocumentStringsBody(); // ContinuousProjectDocumentStringsBody | 
    try {
      StringList result = apiInstance.postContinuousProjectFileStrings(projectId, continuousProjectDocumentStringsBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#postContinuousProjectFileStrings");
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
| **projectId** | **Long**| Project ID | |
| **continuousProjectDocumentStringsBody** | [**ContinuousProjectDocumentStringsBody**](ContinuousProjectDocumentStringsBody.md)|  | [optional] |

### Return type

[**StringList**](StringList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for strings and their translations |  -  |

<a id="recacheTranslations"></a>
# **recacheTranslations**
> OperationStatus recacheTranslations(projectId, locale, fileId)

Recache translations

Recache translations for the continuous project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    String locale = "locale_example"; // String | Locale
    Long fileId = 56L; // Long | Continuous Project File ID
    try {
      OperationStatus result = apiInstance.recacheTranslations(projectId, locale, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#recacheTranslations");
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
| **projectId** | **Long**| Project ID | |
| **locale** | **String**| Locale | [optional] |
| **fileId** | **Long**| Continuous Project File ID | [optional] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Operation response |  -  |

<a id="updateTranslationMemoryUnit"></a>
# **updateTranslationMemoryUnit**
> OperationStatus updateTranslationMemoryUnit(translationMemoryUnit)

Update string translation

Update the translation of a string from your account strings/translation memory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StringsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StringsApi apiInstance = new StringsApi(defaultClient);
    TranslationMemoryUnit translationMemoryUnit = new TranslationMemoryUnit(); // TranslationMemoryUnit | 
    try {
      OperationStatus result = apiInstance.updateTranslationMemoryUnit(translationMemoryUnit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StringsApi#updateTranslationMemoryUnit");
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
| **translationMemoryUnit** | [**TranslationMemoryUnit**](TranslationMemoryUnit.md)|  | [optional] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Translation updated by adding new translation memory unit |  -  |
| **400** | Corporate id, source language, target language, source string or target string is not provided |  -  |
| **404** | Source language or target language is not found |  -  |
| **500** | Something went wrong and translation unit is not updated |  -  |

