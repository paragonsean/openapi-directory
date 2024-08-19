# DatabaseApi

All URIs are relative to *https://appwrite.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databaseCreateDocument**](DatabaseApi.md#databaseCreateDocument) | **POST** /database/collections/{collectionId}/documents | Create Document |
| [**databaseDeleteDocument**](DatabaseApi.md#databaseDeleteDocument) | **DELETE** /database/collections/{collectionId}/documents/{documentId} | Delete Document |
| [**databaseGetDocument**](DatabaseApi.md#databaseGetDocument) | **GET** /database/collections/{collectionId}/documents/{documentId} | Get Document |
| [**databaseListDocuments**](DatabaseApi.md#databaseListDocuments) | **GET** /database/collections/{collectionId}/documents | List Documents |
| [**databaseUpdateDocument**](DatabaseApi.md#databaseUpdateDocument) | **PATCH** /database/collections/{collectionId}/documents/{documentId} | Update Document |


<a id="databaseCreateDocument"></a>
# **databaseCreateDocument**
> Document databaseCreateDocument(collectionId, databaseCreateDocumentRequest)

Create Document

Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](/docs/server/database#databaseCreateCollection) API or directly from your database console.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    DatabaseCreateDocumentRequest databaseCreateDocumentRequest = new DatabaseCreateDocumentRequest(); // DatabaseCreateDocumentRequest | 
    try {
      Document result = apiInstance.databaseCreateDocument(collectionId, databaseCreateDocumentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseCreateDocument");
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
| **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | |
| **databaseCreateDocumentRequest** | [**DatabaseCreateDocumentRequest**](DatabaseCreateDocumentRequest.md)|  | [optional] |

### Return type

[**Document**](Document.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Document |  -  |

<a id="databaseDeleteDocument"></a>
# **databaseDeleteDocument**
> databaseDeleteDocument(collectionId, documentId)

Delete Document

Delete a document by its unique ID. This endpoint deletes only the parent documents, its attributes and relations to other documents. Child documents **will not** be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    String documentId = "documentId_example"; // String | Document unique ID.
    try {
      apiInstance.databaseDeleteDocument(collectionId, documentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseDeleteDocument");
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
| **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | |
| **documentId** | **String**| Document unique ID. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="databaseGetDocument"></a>
# **databaseGetDocument**
> Document databaseGetDocument(collectionId, documentId)

Get Document

Get a document by its unique ID. This endpoint response returns a JSON object with the document data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    String documentId = "documentId_example"; // String | Document unique ID.
    try {
      Document result = apiInstance.databaseGetDocument(collectionId, documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseGetDocument");
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
| **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | |
| **documentId** | **String**| Document unique ID. | |

### Return type

[**Document**](Document.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document |  -  |

<a id="databaseListDocuments"></a>
# **databaseListDocuments**
> DocumentList databaseListDocuments(collectionId, filters, limit, offset, orderField, orderType, orderCast, search)

List Documents

Get a list of all the user documents. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s documents. [Learn more about different API modes](/docs/admin).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    List<String> filters = Arrays.asList(); // List<String> | Array of filter strings. Each filter is constructed from a key name, comparison operator (=, !=, >, <, <=, >=) and a value. You can also use a dot (.) separator in attribute names to filter by child document attributes. Examples: 'name=John Doe' or 'category.$id>=5bed2d152c362'.
    Integer limit = 25; // Integer | Maximum number of documents to return in response.  Use this value to manage pagination. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    Integer offset = 0; // Integer | Offset value. The default value is 0. Use this param to manage pagination.
    String orderField = ""; // String | Document field that results will be sorted by.
    String orderType = "ASC"; // String | Order direction. Possible values are DESC for descending order, or ASC for ascending order.
    String orderCast = "string"; // String | Order field type casting. Possible values are int, string, date, time or datetime. The database will attempt to cast the order field to the value you pass here. The default value is a string.
    String search = ""; // String | Search query. Enter any free text search. The database will try to find a match against all document attributes and children. Max length: 256 chars.
    try {
      DocumentList result = apiInstance.databaseListDocuments(collectionId, filters, limit, offset, orderField, orderType, orderCast, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseListDocuments");
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
| **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | |
| **filters** | [**List&lt;String&gt;**](String.md)| Array of filter strings. Each filter is constructed from a key name, comparison operator (&#x3D;, !&#x3D;, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D;) and a value. You can also use a dot (.) separator in attribute names to filter by child document attributes. Examples: &#39;name&#x3D;John Doe&#39; or &#39;category.$id&gt;&#x3D;5bed2d152c362&#39;. | [optional] |
| **limit** | **Integer**| Maximum number of documents to return in response.  Use this value to manage pagination. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25] |
| **offset** | **Integer**| Offset value. The default value is 0. Use this param to manage pagination. | [optional] [default to 0] |
| **orderField** | **String**| Document field that results will be sorted by. | [optional] [default to ] |
| **orderType** | **String**| Order direction. Possible values are DESC for descending order, or ASC for ascending order. | [optional] [default to ASC] |
| **orderCast** | **String**| Order field type casting. Possible values are int, string, date, time or datetime. The database will attempt to cast the order field to the value you pass here. The default value is a string. | [optional] [default to string] |
| **search** | **String**| Search query. Enter any free text search. The database will try to find a match against all document attributes and children. Max length: 256 chars. | [optional] [default to ] |

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Documents List |  -  |

<a id="databaseUpdateDocument"></a>
# **databaseUpdateDocument**
> Document databaseUpdateDocument(collectionId, documentId, databaseUpdateDocumentRequest)

Update Document

Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    String documentId = "documentId_example"; // String | Document unique ID.
    DatabaseUpdateDocumentRequest databaseUpdateDocumentRequest = new DatabaseUpdateDocumentRequest(); // DatabaseUpdateDocumentRequest | 
    try {
      Document result = apiInstance.databaseUpdateDocument(collectionId, documentId, databaseUpdateDocumentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseUpdateDocument");
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
| **collectionId** | **String**| Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection). | |
| **documentId** | **String**| Document unique ID. | |
| **databaseUpdateDocumentRequest** | [**DatabaseUpdateDocumentRequest**](DatabaseUpdateDocumentRequest.md)|  | [optional] |

### Return type

[**Document**](Document.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document |  -  |

