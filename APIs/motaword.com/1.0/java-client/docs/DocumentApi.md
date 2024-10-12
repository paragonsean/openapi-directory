# DocumentApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllDocumentSubjects**](DocumentApi.md#getAllDocumentSubjects) | **GET** /documents/subjects | Get a list of subjects of projects |
| [**getDocument**](DocumentApi.md#getDocument) | **GET** /documents/{documentId} | View a single document |
| [**getDocumentProgress**](DocumentApi.md#getDocumentProgress) | **GET** /documents/{documentId}/progress | View a document translation progress |
| [**getDocuments**](DocumentApi.md#getDocuments) | **GET** /documents | View your documents |
| [**getSimilarDocuments**](DocumentApi.md#getSimilarDocuments) | **GET** /documents/{documentId}/similars | Find documents similar to this document. |
| [**getUserDocuments**](DocumentApi.md#getUserDocuments) | **GET** /{userId}/documents | Get a list of your documents |
| [**regeneratePreview**](DocumentApi.md#regeneratePreview) | **POST** /documents/{documentId}/regenerate_preview | Regenerate preview and return preview URL for given file |
| [**useAsDraft**](DocumentApi.md#useAsDraft) | **POST** /documents/{documentId}/use_as_draft | Use the translation of given source manual document as manual draft source for the given target document. |
| [**useAsRegular**](DocumentApi.md#useAsRegular) | **POST** /documents/{documentId}/use_as_regular | Use the translation of the given manual document as a regular file. |


<a id="getAllDocumentSubjects"></a>
# **getAllDocumentSubjects**
> List&lt;DocumentSubjects&gt; getAllDocumentSubjects()

Get a list of subjects of projects

Get a list of subjects of projects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

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

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    try {
      List<DocumentSubjects> result = apiInstance.getAllDocumentSubjects();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#getAllDocumentSubjects");
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

[**List&lt;DocumentSubjects&gt;**](DocumentSubjects.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of subjects of all projects. |  -  |

<a id="getDocument"></a>
# **getDocument**
> ContinuousProjectDocument getDocument(documentId)

View a single document

View a single document from your MotaWord account with its translation info.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

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

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    String documentId = "179469"; // String | Document ID or filename
    try {
      ContinuousProjectDocument result = apiInstance.getDocument(documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#getDocument");
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
| **documentId** | **String**| Document ID or filename | |

### Return type

[**ContinuousProjectDocument**](ContinuousProjectDocument.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document |  -  |

<a id="getDocumentProgress"></a>
# **getDocumentProgress**
> Progress getDocumentProgress(documentId)

View a document translation progress

View the translation or proofreading progress of a document in your account. You can also track the progress of a document under the project that it was ordered with.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

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

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    BigDecimal documentId = new BigDecimal("179469"); // BigDecimal | Document ID
    try {
      Progress result = apiInstance.getDocumentProgress(documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#getDocumentProgress");
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
| **documentId** | **BigDecimal**| Document ID | |

### Return type

[**Progress**](Progress.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Progress information |  -  |
| **404** | DocumentNotFound |  -  |

<a id="getDocuments"></a>
# **getDocuments**
> DocumentList getDocuments(recent, search, typeFilter, languageCode, page, perPage, orderBy, orderType, with)

View your documents

View a list of files and documents that you have translations for. This endpoint lets you view your MotaWord account as a multilingual translated file repository, without needing to go through your projects to interact with files in them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

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

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    Boolean recent = true; // Boolean | When true, this will return the most 4 recent active documents.
    String search = "search_example"; // String | 
    String typeFilter = "ALL"; // String | 
    String languageCode = "languageCode_example"; // String | searches in source language of documents, in source and target languages of document's quote
    Long page = 1L; // Long | 
    Long perPage = 10L; // Long | 
    String orderBy = "id"; // String | 
    ListOrderType orderType = ListOrderType.fromValue("asc"); // ListOrderType | 
    List<String> with = Arrays.asList(); // List<String> | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
    try {
      DocumentList result = apiInstance.getDocuments(recent, search, typeFilter, languageCode, page, perPage, orderBy, orderType, with);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#getDocuments");
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
| **recent** | **Boolean**| When true, this will return the most 4 recent active documents. | [optional] |
| **search** | **String**|  | [optional] |
| **typeFilter** | **String**|  | [optional] [default to ALL] [enum: ALL, TEXT_DOCUMENTS, PRESENTATIONS, SPREADSHEETS, PDFS, IMAGES, SUBTITLES, DESIGNS, LOCALIZATION, WEB, STYLE_GUIDES, GLOSSARIES] |
| **languageCode** | **String**| searches in source language of documents, in source and target languages of document&#39;s quote | [optional] |
| **page** | **Long**|  | [optional] [default to 1] |
| **perPage** | **Long**|  | [optional] [default to 10] |
| **orderBy** | **String**|  | [optional] [default to updated_at] [enum: id, updated_at, created_at, name] |
| **orderType** | [**ListOrderType**](.md)|  | [optional] [enum: asc, desc] |
| **with** | [**List&lt;String&gt;**](String.md)| Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls. | [optional] [enum: preview, editors] |

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document list |  -  |

<a id="getSimilarDocuments"></a>
# **getSimilarDocuments**
> DocumentList getSimilarDocuments(documentId, perPage, with)

Find documents similar to this document.

Find documents similar to this document. Optionally, include translation information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

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

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    Long documentId = 179469L; // Long | Document ID
    Long perPage = 1L; // Long | Determines the number of similar documents to return.
    List<String> with = Arrays.asList(); // List<String> | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
    try {
      DocumentList result = apiInstance.getSimilarDocuments(documentId, perPage, with);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#getSimilarDocuments");
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
| **documentId** | **Long**| Document ID | |
| **perPage** | **Long**| Determines the number of similar documents to return. | [optional] [default to 1] |
| **with** | [**List&lt;String&gt;**](String.md)| Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls. | [optional] [enum: preview, editors] |

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document list |  -  |

<a id="getUserDocuments"></a>
# **getUserDocuments**
> DocumentList getUserDocuments(userId, recent, search, typeFilter, languageCode, page, perPage, orderBy, orderType)

Get a list of your documents

Get a list of your documents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

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

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    Long userId = 1L; // Long | User ID
    Boolean recent = true; // Boolean | When true, this will return the most 4 recent active documents.
    String search = "search_example"; // String | 
    String typeFilter = "ALL"; // String | 
    String languageCode = "languageCode_example"; // String | searches in source language of documents, in source and target languages of document's quote
    Long page = 1L; // Long | 
    Long perPage = 10L; // Long | 
    String orderBy = "id"; // String | 
    ListOrderType orderType = ListOrderType.fromValue("asc"); // ListOrderType | 
    try {
      DocumentList result = apiInstance.getUserDocuments(userId, recent, search, typeFilter, languageCode, page, perPage, orderBy, orderType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#getUserDocuments");
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
| **userId** | **Long**| User ID | |
| **recent** | **Boolean**| When true, this will return the most 4 recent active documents. | [optional] |
| **search** | **String**|  | [optional] |
| **typeFilter** | **String**|  | [optional] [default to ALL] [enum: ALL, TEXT_DOCUMENTS, PRESENTATIONS, SPREADSHEETS, PDFS, IMAGES, SUBTITLES, DESIGNS, LOCALIZATION, WEB, STYLE_GUIDES, GLOSSARIES] |
| **languageCode** | **String**| searches in source language of documents, in source and target languages of document&#39;s quote | [optional] |
| **page** | **Long**|  | [optional] [default to 1] |
| **perPage** | **Long**|  | [optional] [default to 10] |
| **orderBy** | **String**|  | [optional] [default to updated_at] [enum: id, updated_at, created_at, name] |
| **orderType** | [**ListOrderType**](.md)|  | [optional] [enum: asc, desc] |

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document list |  -  |

<a id="regeneratePreview"></a>
# **regeneratePreview**
> RegeneratePreviewResponse regeneratePreview(documentId)

Regenerate preview and return preview URL for given file

Regenerate preview and return preview URL for given file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

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

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    Long documentId = 179469L; // Long | Document ID
    try {
      RegeneratePreviewResponse result = apiInstance.regeneratePreview(documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#regeneratePreview");
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
| **documentId** | **Long**| Document ID | |

### Return type

[**RegeneratePreviewResponse**](RegeneratePreviewResponse.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RegeneratePreviewResponse |  -  |

<a id="useAsDraft"></a>
# **useAsDraft**
> OperationStatus useAsDraft(documentId, useAsDraftPayload)

Use the translation of given source manual document as manual draft source for the given target document.

Use the translation of given source manual document as manual draft source for the given target document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

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

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    Long documentId = 179469L; // Long | Document ID
    UseAsDraftPayload useAsDraftPayload = new UseAsDraftPayload(); // UseAsDraftPayload | 
    try {
      OperationStatus result = apiInstance.useAsDraft(documentId, useAsDraftPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#useAsDraft");
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
| **documentId** | **Long**| Document ID | |
| **useAsDraftPayload** | [**UseAsDraftPayload**](UseAsDraftPayload.md)|  | [optional] |

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
| **200** | Operation status |  -  |

<a id="useAsRegular"></a>
# **useAsRegular**
> OperationStatus useAsRegular(documentId, useAsRegularPayload)

Use the translation of the given manual document as a regular file.

Use the translation of the given manual document as a regular file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

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

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    Long documentId = 179469L; // Long | Document ID
    UseAsRegularPayload useAsRegularPayload = new UseAsRegularPayload(); // UseAsRegularPayload | 
    try {
      OperationStatus result = apiInstance.useAsRegular(documentId, useAsRegularPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#useAsRegular");
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
| **documentId** | **Long**| Document ID | |
| **useAsRegularPayload** | [**UseAsRegularPayload**](UseAsRegularPayload.md)|  | [optional] |

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
| **200** | Operation status |  -  |

