# DatabaseApi

All URIs are relative to *https://appwrite.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databaseCreateCollection**](DatabaseApi.md#databaseCreateCollection) | **POST** /database/collections | Create Collection |
| [**databaseCreateDocument**](DatabaseApi.md#databaseCreateDocument) | **POST** /database/collections/{collectionId}/documents | Create Document |
| [**databaseDeleteCollection**](DatabaseApi.md#databaseDeleteCollection) | **DELETE** /database/collections/{collectionId} | Delete Collection |
| [**databaseDeleteDocument**](DatabaseApi.md#databaseDeleteDocument) | **DELETE** /database/collections/{collectionId}/documents/{documentId} | Delete Document |
| [**databaseGetCollection**](DatabaseApi.md#databaseGetCollection) | **GET** /database/collections/{collectionId} | Get Collection |
| [**databaseGetDocument**](DatabaseApi.md#databaseGetDocument) | **GET** /database/collections/{collectionId}/documents/{documentId} | Get Document |
| [**databaseListCollections**](DatabaseApi.md#databaseListCollections) | **GET** /database/collections | List Collections |
| [**databaseListDocuments**](DatabaseApi.md#databaseListDocuments) | **GET** /database/collections/{collectionId}/documents | List Documents |
| [**databaseUpdateCollection**](DatabaseApi.md#databaseUpdateCollection) | **PUT** /database/collections/{collectionId} | Update Collection |
| [**databaseUpdateDocument**](DatabaseApi.md#databaseUpdateDocument) | **PATCH** /database/collections/{collectionId}/documents/{documentId} | Update Document |


<a id="databaseCreateCollection"></a>
# **databaseCreateCollection**
> Collection databaseCreateCollection(databaseCreateCollectionRequest)

Create Collection

Create a new Collection.

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    DatabaseCreateCollectionRequest databaseCreateCollectionRequest = new DatabaseCreateCollectionRequest(); // DatabaseCreateCollectionRequest | 
    try {
      Collection result = apiInstance.databaseCreateCollection(databaseCreateCollectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseCreateCollection");
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
| **databaseCreateCollectionRequest** | [**DatabaseCreateCollectionRequest**](DatabaseCreateCollectionRequest.md)|  | [optional] |

### Return type

[**Collection**](Collection.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Collection |  -  |

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

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

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Document |  -  |

<a id="databaseDeleteCollection"></a>
# **databaseDeleteCollection**
> databaseDeleteCollection(collectionId)

Delete Collection

Delete a collection by its unique ID. Only users with write permissions have access to delete this resource.

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection unique ID.
    try {
      apiInstance.databaseDeleteCollection(collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseDeleteCollection");
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
| **collectionId** | **String**| Collection unique ID. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

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

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="databaseGetCollection"></a>
# **databaseGetCollection**
> Collection databaseGetCollection(collectionId)

Get Collection

Get a collection by its unique ID. This endpoint response returns a JSON object with the collection metadata.

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection unique ID.
    try {
      Collection result = apiInstance.databaseGetCollection(collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseGetCollection");
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
| **collectionId** | **String**| Collection unique ID. | |

### Return type

[**Collection**](Collection.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection |  -  |

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

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

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document |  -  |

<a id="databaseListCollections"></a>
# **databaseListCollections**
> CollectionList databaseListCollections(search, limit, offset, orderType)

List Collections

Get a list of all the user collections. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s collections. [Learn more about different API modes](/docs/admin).

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    String search = ""; // String | Search term to filter your list results. Max length: 256 chars.
    Integer limit = 25; // Integer | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    Integer offset = 0; // Integer | Results offset. The default value is 0. Use this param to manage pagination.
    String orderType = "ASC"; // String | Order result by ASC or DESC order.
    try {
      CollectionList result = apiInstance.databaseListCollections(search, limit, offset, orderType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseListCollections");
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
| **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to ] |
| **limit** | **Integer**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25] |
| **offset** | **Integer**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0] |
| **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to ASC] |

### Return type

[**CollectionList**](CollectionList.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collections List |  -  |

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

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

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Documents List |  -  |

<a id="databaseUpdateCollection"></a>
# **databaseUpdateCollection**
> Collection databaseUpdateCollection(collectionId, databaseUpdateCollectionRequest)

Update Collection

Update a collection by its unique ID.

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection unique ID.
    DatabaseUpdateCollectionRequest databaseUpdateCollectionRequest = new DatabaseUpdateCollectionRequest(); // DatabaseUpdateCollectionRequest | 
    try {
      Collection result = apiInstance.databaseUpdateCollection(collectionId, databaseUpdateCollectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseUpdateCollection");
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
| **collectionId** | **String**| Collection unique ID. | |
| **databaseUpdateCollectionRequest** | [**DatabaseUpdateCollectionRequest**](DatabaseUpdateCollectionRequest.md)|  | [optional] |

### Return type

[**Collection**](Collection.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection |  -  |

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

    // Configure API key authorization: Key
    ApiKeyAuth Key = (ApiKeyAuth) defaultClient.getAuthentication("Key");
    Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Key.setApiKeyPrefix("Token");

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

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document |  -  |

