# DocumentsApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**documentsDocIDGet**](DocumentsApi.md#documentsDocIDGet) | **GET** /documents/{docID} | Returns documents by ID |
| [**documentsFindByAuthorAuthorIDGet**](DocumentsApi.md#documentsFindByAuthorAuthorIDGet) | **GET** /documents/findByAuthor/{authorID} | Finds documents by author |
| [**documentsFindByDateGet**](DocumentsApi.md#documentsFindByDateGet) | **GET** /documents/findByDate | Finds documents by date |
| [**documentsFindByMentionDocIDGet**](DocumentsApi.md#documentsFindByMentionDocIDGet) | **GET** /documents/findByMention/{docID} | Finds documents by reference |
| [**documentsGet**](DocumentsApi.md#documentsGet) | **GET** /documents | Lists all documents |


<a id="documentsDocIDGet"></a>
# **documentsDocIDGet**
> List&lt;Document&gt; documentsDocIDGet(docID)

Returns documents by ID

This endpoint returns documents, indicated by an ID.  Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String docID = "A002068"; // String | The document identifier to search for
    try {
      List<Document> result = apiInstance.documentsDocIDGet(docID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsDocIDGet");
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
| **docID** | **String**| The document identifier to search for | [default to A002068] |

### Return type

[**List&lt;Document&gt;**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of documents |  -  |
| **0** | Unexpected error |  -  |

<a id="documentsFindByAuthorAuthorIDGet"></a>
# **documentsFindByAuthorAuthorIDGet**
> List&lt;Document&gt; documentsFindByAuthorAuthorIDGet(authorID, docType, offset, limit)

Finds documents by author

This endpoint returns a list of documents by a given author – optionally filtered by document type  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String authorID = "A002068"; // String | The author ID to search for. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662 
    List<String> docType = Arrays.asList(); // List<String> | The WeGA document type
    Integer offset = 1; // Integer | Position of first item to retrieve (starting from 1)
    Integer limit = 10; // Integer | Number of items to retrieve (200 max)
    try {
      List<Document> result = apiInstance.documentsFindByAuthorAuthorIDGet(authorID, docType, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsFindByAuthorAuthorIDGet");
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
| **authorID** | **String**| The author ID to search for. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662  | [default to A002068] |
| **docType** | [**List&lt;String&gt;**](String.md)| The WeGA document type | [optional] [enum: biblio, diaries, documents, letters, news, orgs, persons, places, thematicCommentaries, var, works, writings] |
| **offset** | **Integer**| Position of first item to retrieve (starting from 1) | [optional] [default to 1] |
| **limit** | **Integer**| Number of items to retrieve (200 max) | [optional] [default to 10] |

### Return type

[**List&lt;Document&gt;**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of documents |  * totalrecordcount - The total size of the result set <br>  |
| **0** | Unexpected error |  -  |

<a id="documentsFindByDateGet"></a>
# **documentsFindByDateGet**
> List&lt;Document&gt; documentsFindByDateGet(fromDate, toDate, docType, offset, limit)

Finds documents by date

This endpoint returns a list of documents related to the given date – optionally filtered by document type.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    LocalDate fromDate = LocalDate.parse("1786-11-17"); // LocalDate | The min date to search for
    LocalDate toDate = LocalDate.now(); // LocalDate | The max date to search for
    List<String> docType = Arrays.asList(); // List<String> | The WeGA document type
    Integer offset = 1; // Integer | Position of first item to retrieve (starting from 1)
    Integer limit = 10; // Integer | Number of items to retrieve (200 max)
    try {
      List<Document> result = apiInstance.documentsFindByDateGet(fromDate, toDate, docType, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsFindByDateGet");
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
| **fromDate** | **LocalDate**| The min date to search for | [default to 1786-11-17] |
| **toDate** | **LocalDate**| The max date to search for | [optional] |
| **docType** | [**List&lt;String&gt;**](String.md)| The WeGA document type | [optional] [enum: biblio, diaries, documents, letters, news, orgs, persons, places, thematicCommentaries, var, works, writings] |
| **offset** | **Integer**| Position of first item to retrieve (starting from 1) | [optional] [default to 1] |
| **limit** | **Integer**| Number of items to retrieve (200 max) | [optional] [default to 10] |

### Return type

[**List&lt;Document&gt;**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of documents |  * totalrecordcount - The total size of the result set <br>  |
| **0** | Unexpected error |  -  |

<a id="documentsFindByMentionDocIDGet"></a>
# **documentsFindByMentionDocIDGet**
> List&lt;Document&gt; documentsFindByMentionDocIDGet(docID, docType, offset, limit)

Finds documents by reference

This endpoint returns a list of documents that reference a particular docID – optionally filtered by document type.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String docID = "A002068"; // String | The document ID that is to be mentioned. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662 
    List<String> docType = Arrays.asList(); // List<String> | The WeGA document type
    Integer offset = 1; // Integer | Position of first item to retrieve (starting from 1)
    Integer limit = 10; // Integer | Number of items to retrieve (200 max)
    try {
      List<Document> result = apiInstance.documentsFindByMentionDocIDGet(docID, docType, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#documentsFindByMentionDocIDGet");
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
| **docID** | **String**| The document ID that is to be mentioned. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662  | [default to A002068] |
| **docType** | [**List&lt;String&gt;**](String.md)| The WeGA document type | [optional] [enum: biblio, diaries, documents, letters, news, orgs, persons, places, thematicCommentaries, var, works, writings] |
| **offset** | **Integer**| Position of first item to retrieve (starting from 1) | [optional] [default to 1] |
| **limit** | **Integer**| Number of items to retrieve (200 max) | [optional] [default to 10] |

### Return type

[**List&lt;Document&gt;**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of documents |  * totalrecordcount - The total size of the result set <br>  |
| **0** | Unexpected error |  -  |

<a id="documentsGet"></a>
# **documentsGet**
> List&lt;Document&gt; documentsGet(docType, offset, limit)

Lists all documents

The Documents endpoint returns a list of all documents from the WeGA digital edition. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    List<String> docType = Arrays.asList(); // List<String> | The WeGA document type
    Integer offset = 1; // Integer | Position of first item to retrieve (starting from 1)
    Integer limit = 10; // Integer | Number of items to retrieve (200 max)
    try {
      List<Document> result = apiInstance.documentsGet(docType, offset, limit);
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

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **docType** | [**List&lt;String&gt;**](String.md)| The WeGA document type | [optional] [enum: biblio, diaries, documents, letters, news, orgs, persons, places, thematicCommentaries, var, works, writings] |
| **offset** | **Integer**| Position of first item to retrieve (starting from 1) | [optional] [default to 1] |
| **limit** | **Integer**| Number of items to retrieve (200 max) | [optional] [default to 10] |

### Return type

[**List&lt;Document&gt;**](Document.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of documents |  * totalrecordcount - The total size of the result set <br>  |
| **0** | Unexpected error |  -  |

