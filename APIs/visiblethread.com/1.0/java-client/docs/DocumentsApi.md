# DocumentsApi

All URIs are relative to *https://api.visiblethread.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dictionariesGet**](DocumentsApi.md#dictionariesGet) | **GET** /dictionaries | Get your list of dictionaries |
| [**documentsGet**](DocumentsApi.md#documentsGet) | **GET** /documents | Get your list of documents |
| [**getDocById**](DocumentsApi.md#getDocById) | **GET** /documents/{docId} | Get data from a previously submitted document |
| [**getSearchResults**](DocumentsApi.md#getSearchResults) | **GET** /searches/{docId}/{dictionaryId} | Gets search results for a particular document/dictionary |
| [**runSearch**](DocumentsApi.md#runSearch) | **POST** /searches | Run a search |
| [**searchesGet**](DocumentsApi.md#searchesGet) | **GET** /searches | Get your list of searches |
| [**uploadDictionary**](DocumentsApi.md#uploadDictionary) | **POST** /dictionaries | Upload a dictionary (CSV) |
| [**uploadDoc**](DocumentsApi.md#uploadDoc) | **POST** /documents | Upload a document |


<a id="dictionariesGet"></a>
# **dictionariesGet**
> dictionariesGet()

Get your list of dictionaries

Get your list of dictionaries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    try {
      apiInstance.dictionariesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#dictionariesGet");
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

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="documentsGet"></a>
# **documentsGet**
> List&lt;DocumentListSummary&gt; documentsGet()

Get your list of documents

Get your list of documents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    try {
      List<DocumentListSummary> result = apiInstance.documentsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsGet");
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

[**List&lt;DocumentListSummary&gt;**](DocumentListSummary.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="getDocById"></a>
# **getDocById**
> DocumentResponseDetailed getDocById(docId)

Get data from a previously submitted document

Get data from a previously submitted document identified by ***docId***

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    Long docId = 56L; // Long | Id of document to fetch
    try {
      DocumentResponseDetailed result = apiInstance.getDocById(docId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#getDocById");
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
| **docId** | **Long**| Id of document to fetch | |

### Return type

[**DocumentResponseDetailed**](DocumentResponseDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | document response contained readability details for the document |  -  |
| **404** | document not found |  -  |
| **415** | the document is an unsupported file type |  -  |
| **500** | an unknown error occurred processing the document |  -  |
| **503** | the document analysis has not yet completed, try again later |  -  |

<a id="getSearchResults"></a>
# **getSearchResults**
> getSearchResults(docId, dictionaryId, matchingOnly)

Gets search results for a particular document/dictionary

Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** &amp; **urlId**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    Long docId = 56L; // Long | Id of document
    Long dictionaryId = 56L; // Long | Id of dictionary
    Boolean matchingOnly = true; // Boolean | Only returning paragraphs containing a match
    try {
      apiInstance.getSearchResults(docId, dictionaryId, matchingOnly);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#getSearchResults");
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
| **docId** | **Long**| Id of document | |
| **dictionaryId** | **Long**| Id of dictionary | |
| **matchingOnly** | **Boolean**| Only returning paragraphs containing a match | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | scan response |  -  |

<a id="runSearch"></a>
# **runSearch**
> Object runSearch(body)

Run a search

Run a search on document **docId** using dictionary **dictId** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    Search body = new Search(); // Search | Run a search on document **docId** using dictionary**dictId**
    try {
      Object result = apiInstance.runSearch(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#runSearch");
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
| **body** | [**Search**](Search.md)| Run a search on document **docId** using dictionary**dictId** | |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **405** | Invalid input |  -  |

<a id="searchesGet"></a>
# **searchesGet**
> searchesGet()

Get your list of searches

Get your list of searches

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    try {
      apiInstance.searchesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#searchesGet");
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

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="uploadDictionary"></a>
# **uploadDictionary**
> uploadDictionary(_file)

Upload a dictionary (CSV)

Upload a dictionary (CSV format) to your VisibleThread account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The uploaded CSV dictionary
    try {
      apiInstance.uploadDictionary(_file);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#uploadDictionary");
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
| **_file** | **File**| The uploaded CSV dictionary | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **405** | Invalid input |  -  |

<a id="uploadDoc"></a>
# **uploadDoc**
> NewDocumentResponse uploadDoc(_file, longSentenceWordCount, veryLongSentenceWordCount)

Upload a document

Upload a document to your VisibleThread account.  We return a JSON response that contains a \&quot;docId\&quot; that represents your document.         You can use this id in other requests to check on the analysis status for the document and run a dictionary search and retrieve search results. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.visiblethread.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The uploaded file data
    Integer longSentenceWordCount = 56; // Integer | Optional setting what constitutes a long sentence (default 25)
    Integer veryLongSentenceWordCount = 56; // Integer | Optional setting what constitutes a very long sentence (default 30)
    try {
      NewDocumentResponse result = apiInstance.uploadDoc(_file, longSentenceWordCount, veryLongSentenceWordCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#uploadDoc");
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
| **_file** | **File**| The uploaded file data | |
| **longSentenceWordCount** | **Integer**| Optional setting what constitutes a long sentence (default 25) | [optional] |
| **veryLongSentenceWordCount** | **Integer**| Optional setting what constitutes a very long sentence (default 30) | [optional] |

### Return type

[**NewDocumentResponse**](NewDocumentResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **405** | Invalid input |  -  |
| **413** | The document exceeds the maximum supported file size (15mb) |  -  |

