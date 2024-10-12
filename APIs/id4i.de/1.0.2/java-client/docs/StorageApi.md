# StorageApi

All URIs are relative to *http://backend.id4i.de*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDocument**](StorageApi.md#createDocument) | **POST** /api/v1/documents/{id4n}/{organizationId} | Create an document for an id4n |
| [**deleteDocument**](StorageApi.md#deleteDocument) | **DELETE** /api/v1/documents/{id4n}/{organizationId}/{fileName} | Delete a document |
| [**getDocument**](StorageApi.md#getDocument) | **GET** /api/v1/documents/{id4n}/{organizationId}/{fileName}/metadata | Retrieve a document (meta-data only, no content) |
| [**getPublicDocument_0**](StorageApi.md#getPublicDocument_0) | **GET** /api/v1/public/documents/{id4n}/{organizationId}/{fileName}/metadata | Retrieve a public document (meta-data only, no content) |
| [**listAllDocuments**](StorageApi.md#listAllDocuments) | **GET** /api/v1/documents/{id4n} | List documents |
| [**listAllPublicDocuments_0**](StorageApi.md#listAllPublicDocuments_0) | **GET** /api/v1/public/documents/{id4n} | List public documents |
| [**listDocuments**](StorageApi.md#listDocuments) | **GET** /api/v1/documents/{id4n}/{organizationId} | List organization specific documents |
| [**putDocument**](StorageApi.md#putDocument) | **PUT** /api/v1/documents/{id4n}/{organizationId} | Put an document for an id4n |
| [**readDocument**](StorageApi.md#readDocument) | **GET** /api/v1/documents/{id4n}/{organizationId}/{fileName} | Read document contents |
| [**readFromMicrostorage**](StorageApi.md#readFromMicrostorage) | **GET** /api/v1/microstorage/{id4n}/{organization} | Read data from microstorage |
| [**readPublicDocument_0**](StorageApi.md#readPublicDocument_0) | **GET** /api/v1/public/documents/{id4n}/{organizationId}/{fileName} | Read public document contents |
| [**updateDocumentMetadata**](StorageApi.md#updateDocumentMetadata) | **PATCH** /api/v1/documents/{id4n}/{organizationId}/{fileName}/metadata | Update a document |
| [**writeToMicrostorage**](StorageApi.md#writeToMicrostorage) | **PUT** /api/v1/microstorage/{id4n}/{organization} | Write data to microstorage |


<a id="createDocument"></a>
# **createDocument**
> Document createDocument(organizationId, id4n, content)

Create an document for an id4n

The documents&#39; mime type is suggested on octet-stream data. Otherwise the specified content mime type is used.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organizationId = "organizationId_example"; // String | organizationId
    String id4n = "id4n_example"; // String | id4n
    File content = new File("/path/to/file"); // File | content
    try {
      Document result = apiInstance.createDocument(organizationId, id4n, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#createDocument");
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
| **organizationId** | **String**| organizationId | |
| **id4n** | **String**| id4n | |
| **content** | **File**| content | |

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **409** | Conflict |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="deleteDocument"></a>
# **deleteDocument**
> deleteDocument(organizationId, id4n, fileName)

Delete a document

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organizationId = "organizationId_example"; // String | organizationId
    String id4n = "id4n_example"; // String | id4n
    String fileName = "fileName_example"; // String | fileName
    try {
      apiInstance.deleteDocument(organizationId, id4n, fileName);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#deleteDocument");
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
| **organizationId** | **String**| organizationId | |
| **id4n** | **String**| id4n | |
| **fileName** | **String**| fileName | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getDocument"></a>
# **getDocument**
> Document getDocument(organizationId, id4n, fileName)

Retrieve a document (meta-data only, no content)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organizationId = "organizationId_example"; // String | organizationId
    String id4n = "id4n_example"; // String | id4n
    String fileName = "fileName_example"; // String | fileName
    try {
      Document result = apiInstance.getDocument(organizationId, id4n, fileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#getDocument");
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
| **organizationId** | **String**| organizationId | |
| **id4n** | **String**| id4n | |
| **fileName** | **String**| fileName | |

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="getPublicDocument_0"></a>
# **getPublicDocument_0**
> Document getPublicDocument_0(organizationId, id4n, fileName)

Retrieve a public document (meta-data only, no content)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organizationId = "organizationId_example"; // String | organizationId
    String id4n = "id4n_example"; // String | id4n
    String fileName = "fileName_example"; // String | fileName
    try {
      Document result = apiInstance.getPublicDocument_0(organizationId, id4n, fileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#getPublicDocument_0");
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
| **organizationId** | **String**| organizationId | |
| **id4n** | **String**| id4n | |
| **fileName** | **String**| fileName | |

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="listAllDocuments"></a>
# **listAllDocuments**
> PaginatedResponseOfDocument listAllDocuments(id4n, owner, offset, limit)

List documents

Listing all documents of an id4n

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String id4n = "id4n_example"; // String | id4n
    String owner = "owner_example"; // String | Filter by owner organization
    Integer offset = 56; // Integer | Start with the n-th element
    Integer limit = 56; // Integer | The maximum count of returned elements
    try {
      PaginatedResponseOfDocument result = apiInstance.listAllDocuments(id4n, owner, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#listAllDocuments");
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
| **id4n** | **String**| id4n | |
| **owner** | **String**| Filter by owner organization | [optional] |
| **offset** | **Integer**| Start with the n-th element | [optional] |
| **limit** | **Integer**| The maximum count of returned elements | [optional] |

### Return type

[**PaginatedResponseOfDocument**](PaginatedResponseOfDocument.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="listAllPublicDocuments_0"></a>
# **listAllPublicDocuments_0**
> PaginatedResponseOfDocument listAllPublicDocuments_0(id4n, organizationId, owner, offset, limit)

List public documents

Listing all public documents of an id4n

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String id4n = "id4n_example"; // String | id4n
    String organizationId = "organizationId_example"; // String | organizationId
    String owner = "owner_example"; // String | Filter by owner organization
    Integer offset = 56; // Integer | Start with the n-th element
    Integer limit = 56; // Integer | The maximum count of returned elements
    try {
      PaginatedResponseOfDocument result = apiInstance.listAllPublicDocuments_0(id4n, organizationId, owner, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#listAllPublicDocuments_0");
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
| **id4n** | **String**| id4n | |
| **organizationId** | **String**| organizationId | [optional] |
| **owner** | **String**| Filter by owner organization | [optional] |
| **offset** | **Integer**| Start with the n-th element | [optional] |
| **limit** | **Integer**| The maximum count of returned elements | [optional] |

### Return type

[**PaginatedResponseOfDocument**](PaginatedResponseOfDocument.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="listDocuments"></a>
# **listDocuments**
> PaginatedResponseOfDocument listDocuments(organizationId, id4n, owner, offset, limit)

List organization specific documents

Listing documents of an id4n seen by a specified organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organizationId = "organizationId_example"; // String | organizationId
    String id4n = "id4n_example"; // String | id4n
    String owner = "owner_example"; // String | Filter by owner organization
    Integer offset = 56; // Integer | Start with the n-th element
    Integer limit = 56; // Integer | The maximum count of returned elements
    try {
      PaginatedResponseOfDocument result = apiInstance.listDocuments(organizationId, id4n, owner, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#listDocuments");
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
| **organizationId** | **String**| organizationId | |
| **id4n** | **String**| id4n | |
| **owner** | **String**| Filter by owner organization | [optional] |
| **offset** | **Integer**| Start with the n-th element | [optional] |
| **limit** | **Integer**| The maximum count of returned elements | [optional] |

### Return type

[**PaginatedResponseOfDocument**](PaginatedResponseOfDocument.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="putDocument"></a>
# **putDocument**
> Document putDocument(organizationId, id4n, content)

Put an document for an id4n

Creating or overwriting an existing document 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organizationId = "organizationId_example"; // String | organizationId
    String id4n = "id4n_example"; // String | id4n
    File content = new File("/path/to/file"); // File | content
    try {
      Document result = apiInstance.putDocument(organizationId, id4n, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#putDocument");
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
| **organizationId** | **String**| organizationId | |
| **id4n** | **String**| id4n | |
| **content** | **File**| content | |

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **409** | Conflict |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="readDocument"></a>
# **readDocument**
> byte[] readDocument(organizationId, id4n, fileName)

Read document contents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organizationId = "organizationId_example"; // String | organizationId
    String id4n = "id4n_example"; // String | id4n
    String fileName = "fileName_example"; // String | fileName
    try {
      byte[] result = apiInstance.readDocument(organizationId, id4n, fileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#readDocument");
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
| **organizationId** | **String**| organizationId | |
| **id4n** | **String**| id4n | |
| **fileName** | **String**| fileName | |

### Return type

**byte[]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="readFromMicrostorage"></a>
# **readFromMicrostorage**
> byte[] readFromMicrostorage(organization, id4n)

Read data from microstorage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organization = "organization_example"; // String | organization
    String id4n = "id4n_example"; // String | id4n
    try {
      byte[] result = apiInstance.readFromMicrostorage(organization, id4n);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#readFromMicrostorage");
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
| **organization** | **String**| organization | |
| **id4n** | **String**| id4n | |

### Return type

**byte[]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="readPublicDocument_0"></a>
# **readPublicDocument_0**
> byte[] readPublicDocument_0(organizationId, id4n, fileName)

Read public document contents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organizationId = "organizationId_example"; // String | organizationId
    String id4n = "id4n_example"; // String | id4n
    String fileName = "fileName_example"; // String | fileName
    try {
      byte[] result = apiInstance.readPublicDocument_0(organizationId, id4n, fileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#readPublicDocument_0");
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
| **organizationId** | **String**| organizationId | |
| **id4n** | **String**| id4n | |
| **fileName** | **String**| fileName | |

### Return type

**byte[]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="updateDocumentMetadata"></a>
# **updateDocumentMetadata**
> Document updateDocumentMetadata(organizationId, id4n, fileName, documentUpdate)

Update a document

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organizationId = "organizationId_example"; // String | organizationId
    String id4n = "id4n_example"; // String | id4n
    String fileName = "fileName_example"; // String | fileName
    DocumentUpdate documentUpdate = new DocumentUpdate(); // DocumentUpdate | document
    try {
      Document result = apiInstance.updateDocumentMetadata(organizationId, id4n, fileName, documentUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#updateDocumentMetadata");
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
| **organizationId** | **String**| organizationId | |
| **id4n** | **String**| id4n | |
| **fileName** | **String**| fileName | |
| **documentUpdate** | [**DocumentUpdate**](DocumentUpdate.md)| document | |

### Return type

[**Document**](Document.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="writeToMicrostorage"></a>
# **writeToMicrostorage**
> Object writeToMicrostorage(organization, id4n, contentType, contentLength, body)

Write data to microstorage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    StorageApi apiInstance = new StorageApi(defaultClient);
    String organization = "organization_example"; // String | organization
    String id4n = "id4n_example"; // String | id4n
    String contentType = "contentType_example"; // String | Content-Type
    Long contentLength = 56L; // Long | Content-Length
    byte[] body = null; // byte[] | body
    try {
      Object result = apiInstance.writeToMicrostorage(organization, id4n, contentType, contentLength, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageApi#writeToMicrostorage");
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
| **organization** | **String**| organization | |
| **id4n** | **String**| id4n | |
| **contentType** | **String**| Content-Type | [optional] |
| **contentLength** | **Long**| Content-Length | [optional] |
| **body** | **byte[]**| body | [optional] |

### Return type

**Object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **409** | Conflict |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

