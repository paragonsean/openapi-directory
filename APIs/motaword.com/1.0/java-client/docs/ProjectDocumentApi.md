# ProjectDocumentApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProjectDocument**](ProjectDocumentApi.md#createProjectDocument) | **POST** /projects/{projectId}/documents | Upload a new document |
| [**deleteProjectDocument**](ProjectDocumentApi.md#deleteProjectDocument) | **DELETE** /projects/{projectId}/documents/{documentId} | Delete the document |
| [**downloadProjectDocument**](ProjectDocumentApi.md#downloadProjectDocument) | **GET** /projects/{projectId}/documents/{documentId}/download | Download a project source document |
| [**downloadTranslatedDocumentForLanguage**](ProjectDocumentApi.md#downloadTranslatedDocumentForLanguage) | **GET** /projects/{projectId}/documents/{documentId}/translations/download/{language} | Download translated document |
| [**getProjectDocument**](ProjectDocumentApi.md#getProjectDocument) | **GET** /projects/{projectId}/documents/{documentId} | View a project source document |
| [**getProjectDocuments**](ProjectDocumentApi.md#getProjectDocuments) | **GET** /projects/{projectId}/documents | View project source documents |
| [**updateProjectDocument**](ProjectDocumentApi.md#updateProjectDocument) | **POST** /projects/{projectId}/documents/{documentId} | Update the document. |


<a id="createProjectDocument"></a>
# **createProjectDocument**
> DocumentList createProjectDocument(projectId, documentUpdates)

Upload a new document

Upload a new document

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectDocumentApi;

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

    ProjectDocumentApi apiInstance = new ProjectDocumentApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    DocumentUpdates documentUpdates = new DocumentUpdates(); // DocumentUpdates | 
    try {
      DocumentList result = apiInstance.createProjectDocument(projectId, documentUpdates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectDocumentApi#createProjectDocument");
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
| **documentUpdates** | [**DocumentUpdates**](DocumentUpdates.md)|  | [optional] |

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of successfully added new documents. |  -  |
| **400** | FileTooLarge FileTooSmall FileWasAlreadyUploaded |  -  |
| **404** | ProjectNotFound |  -  |
| **405** | UnsupportedDocumentFormat |  -  |
| **406** | InvalidDocumentScheme |  -  |
| **409** | ProjectAlreadyStarted |  -  |

<a id="deleteProjectDocument"></a>
# **deleteProjectDocument**
> OperationStatus deleteProjectDocument(projectId, documentId)

Delete the document

Delete the document

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectDocumentApi;

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

    ProjectDocumentApi apiInstance = new ProjectDocumentApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long documentId = 179469L; // Long | Document ID
    try {
      OperationStatus result = apiInstance.deleteProjectDocument(projectId, documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectDocumentApi#deleteProjectDocument");
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

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document deleted successfully |  -  |
| **404** | DocumentNotFound |  -  |
| **409** | ProjectAlreadyStarted |  -  |

<a id="downloadProjectDocument"></a>
# **downloadProjectDocument**
> String downloadProjectDocument(projectId, documentId)

Download a project source document

Download an actual source file you uploaded to be translated in your project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectDocumentApi;

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

    ProjectDocumentApi apiInstance = new ProjectDocumentApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long documentId = 179469L; // Long | Document ID
    try {
      String result = apiInstance.downloadProjectDocument(projectId, documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectDocumentApi#downloadProjectDocument");
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

**String**

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document streamed |  -  |
| **404** | DocumentNotFound |  -  |

<a id="downloadTranslatedDocumentForLanguage"></a>
# **downloadTranslatedDocumentForLanguage**
> File downloadTranslatedDocumentForLanguage(projectId, documentId, language, certified)

Download translated document

Download translated document in the given target language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectDocumentApi;

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

    ProjectDocumentApi apiInstance = new ProjectDocumentApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long documentId = 179469L; // Long | Document ID
    String language = "en-US"; // String | Target language code.
    Boolean certified = true; // Boolean | Download certified translation
    try {
      File result = apiInstance.downloadTranslatedDocumentForLanguage(projectId, documentId, language, certified);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectDocumentApi#downloadTranslatedDocumentForLanguage");
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
| **certified** | **Boolean**| Download certified translation | [optional] |

### Return type

[**File**](File.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |
| **404** | DocumentNotFound |  -  |

<a id="getProjectDocument"></a>
# **getProjectDocument**
> Document getProjectDocument(projectId, documentId, with)

View a project source document

View the details of a source file you uploaded to be translated in your project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectDocumentApi;

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

    ProjectDocumentApi apiInstance = new ProjectDocumentApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long documentId = 179469L; // Long | Document ID
    List<String> with = Arrays.asList(); // List<String> | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
    try {
      Document result = apiInstance.getProjectDocument(projectId, documentId, with);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectDocumentApi#getProjectDocument");
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
| **with** | [**List&lt;String&gt;**](String.md)| Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls. | [optional] [enum: preview, editors] |

### Return type

[**Document**](Document.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document model |  -  |
| **404** | DocumentNotFound |  -  |

<a id="getProjectDocuments"></a>
# **getProjectDocuments**
> DocumentList getProjectDocuments(projectId, with)

View project source documents

Get a list of source files you uploaded to be translated in your project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectDocumentApi;

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

    ProjectDocumentApi apiInstance = new ProjectDocumentApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    List<String> with = Arrays.asList(); // List<String> | Attach further information. Possible values 'preview' to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]=preview for single document/style guide calls.
    try {
      DocumentList result = apiInstance.getProjectDocuments(projectId, with);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectDocumentApi#getProjectDocuments");
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
| **200** | A list of document models |  -  |
| **404** | ProjectNotFound |  -  |

<a id="updateProjectDocument"></a>
# **updateProjectDocument**
> Document updateProjectDocument(projectId, documentId, documentUploadRequest)

Update the document.

Update the document. File name and contents will replaced with the new one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectDocumentApi;

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

    ProjectDocumentApi apiInstance = new ProjectDocumentApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    Long documentId = 179469L; // Long | Document ID
    DocumentUploadRequest documentUploadRequest = new DocumentUploadRequest(); // DocumentUploadRequest | 
    try {
      Document result = apiInstance.updateProjectDocument(projectId, documentId, documentUploadRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectDocumentApi#updateProjectDocument");
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
| **documentUploadRequest** | [**DocumentUploadRequest**](DocumentUploadRequest.md)|  | [optional] |

### Return type

[**Document**](Document.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated document model |  -  |
| **400** | FileTooLarge FileTooSmall FileWasAlreadyUploaded |  -  |
| **404** | DocumentNotFound |  -  |
| **405** | UnsupportedDocumentFormat |  -  |
| **406** | InvalidDocumentScheme |  -  |
| **409** | ProjectAlreadyStarted |  -  |

