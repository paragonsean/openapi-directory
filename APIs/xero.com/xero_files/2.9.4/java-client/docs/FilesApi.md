# FilesApi

All URIs are relative to *https://api.xero.com/files.xro/1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFileAssociation**](FilesApi.md#createFileAssociation) | **POST** /Files/{FileId}/Associations | Creates a new file association |
| [**createFolder**](FilesApi.md#createFolder) | **POST** /Folders | Creates a new folder |
| [**deleteFile**](FilesApi.md#deleteFile) | **DELETE** /Files/{FileId} | Deletes a specific file |
| [**deleteFileAssociation**](FilesApi.md#deleteFileAssociation) | **DELETE** /Files/{FileId}/Associations/{ObjectId} | Deletes an existing file association |
| [**deleteFolder**](FilesApi.md#deleteFolder) | **DELETE** /Folders/{FolderId} | Deletes a folder |
| [**getAssociationsByObject**](FilesApi.md#getAssociationsByObject) | **GET** /Associations/{ObjectId} | Retrieves an association object using a unique object ID |
| [**getFile**](FilesApi.md#getFile) | **GET** /Files/{FileId} | Retrieves a file by a unique file ID |
| [**getFileAssociations**](FilesApi.md#getFileAssociations) | **GET** /Files/{FileId}/Associations | Retrieves a specific file associations |
| [**getFileContent**](FilesApi.md#getFileContent) | **GET** /Files/{FileId}/Content | Retrieves the content of a specific file |
| [**getFiles**](FilesApi.md#getFiles) | **GET** /Files | Retrieves files |
| [**getFolder**](FilesApi.md#getFolder) | **GET** /Folders/{FolderId} | Retrieves specific folder by using a unique folder ID |
| [**getFolders**](FilesApi.md#getFolders) | **GET** /Folders | Retrieves folders |
| [**getInbox**](FilesApi.md#getInbox) | **GET** /Inbox | Retrieves inbox folder |
| [**updateFile**](FilesApi.md#updateFile) | **PUT** /Files/{FileId} | Update a file |
| [**updateFolder**](FilesApi.md#updateFolder) | **PUT** /Folders/{FolderId} | Updates an existing folder |
| [**uploadFile**](FilesApi.md#uploadFile) | **POST** /Files | Uploads a File |


<a id="createFileAssociation"></a>
# **createFileAssociation**
> Association createFileAssociation(xeroTenantId, fileId, association)

Creates a new file association

By passing in the appropriate options, you can create a new folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID fileId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | File id for single object
    Association association = new Association(); // Association | 
    try {
      Association result = apiInstance.createFileAssociation(xeroTenantId, fileId, association);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#createFileAssociation");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **fileId** | **UUID**| File id for single object | |
| **association** | [**Association**](Association.md)|  | [optional] |

### Return type

[**Association**](Association.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful request |  -  |
| **400** | invalid input, object invalid |  -  |

<a id="createFolder"></a>
# **createFolder**
> Folder createFolder(xeroTenantId, folder)

Creates a new folder

By passing in the appropriate properties, you can create a new folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Folder folder = new Folder(); // Folder | 
    try {
      Folder result = apiInstance.createFolder(xeroTenantId, folder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#createFolder");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **folder** | [**Folder**](Folder.md)|  | [optional] |

### Return type

[**Folder**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |
| **400** | invalid input, object invalid |  -  |

<a id="deleteFile"></a>
# **deleteFile**
> deleteFile(xeroTenantId, fileId)

Deletes a specific file

Delete a specific file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID fileId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | File id for single object
    try {
      apiInstance.deleteFile(xeroTenantId, fileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#deleteFile");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **fileId** | **UUID**| File id for single object | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful deletion - return response 204 no content |  -  |

<a id="deleteFileAssociation"></a>
# **deleteFileAssociation**
> deleteFileAssociation(xeroTenantId, fileId, objectId)

Deletes an existing file association

By passing in the appropriate options, you can create a new folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID fileId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | File id for single object
    UUID objectId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Object id for single object
    try {
      apiInstance.deleteFileAssociation(xeroTenantId, fileId, objectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#deleteFileAssociation");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **fileId** | **UUID**| File id for single object | |
| **objectId** | **UUID**| Object id for single object | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful deletion - return response 204 no content |  -  |

<a id="deleteFolder"></a>
# **deleteFolder**
> deleteFolder(xeroTenantId, folderId)

Deletes a folder

By passing in the appropriate ID, you can delete a folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID folderId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Folder id for single object
    try {
      apiInstance.deleteFolder(xeroTenantId, folderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#deleteFolder");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **folderId** | **UUID**| Folder id for single object | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful deletion - return response 204 no content |  -  |

<a id="getAssociationsByObject"></a>
# **getAssociationsByObject**
> List&lt;Association&gt; getAssociationsByObject(xeroTenantId, objectId)

Retrieves an association object using a unique object ID

By passing in the appropriate options,

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID objectId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Object id for single object
    try {
      List<Association> result = apiInstance.getAssociationsByObject(xeroTenantId, objectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getAssociationsByObject");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **objectId** | **UUID**| Object id for single object | |

### Return type

[**List&lt;Association&gt;**](Association.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getFile"></a>
# **getFile**
> FileObject getFile(xeroTenantId, fileId)

Retrieves a file by a unique file ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID fileId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | File id for single object
    try {
      FileObject result = apiInstance.getFile(xeroTenantId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFile");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **fileId** | **UUID**| File id for single object | |

### Return type

[**FileObject**](FileObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getFileAssociations"></a>
# **getFileAssociations**
> List&lt;Association&gt; getFileAssociations(xeroTenantId, fileId)

Retrieves a specific file associations

By passing in the appropriate options,  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID fileId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | File id for single object
    try {
      List<Association> result = apiInstance.getFileAssociations(xeroTenantId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFileAssociations");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **fileId** | **UUID**| File id for single object | |

### Return type

[**List&lt;Association&gt;**](Association.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getFileContent"></a>
# **getFileContent**
> File getFileContent(xeroTenantId, fileId)

Retrieves the content of a specific file

By passing in the appropriate options, retrieve data for specific file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID fileId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | File id for single object
    try {
      File result = apiInstance.getFileContent(xeroTenantId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFileContent");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **fileId** | **UUID**| File id for single object | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns the byte array of the specific file based on id |  -  |

<a id="getFiles"></a>
# **getFiles**
> Files getFiles(xeroTenantId, pagesize, page, sort)

Retrieves files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Integer pagesize = 50; // Integer | pass an optional page size value
    Integer page = 2; // Integer | number of records to skip for pagination
    String sort = "Name"; // String | values to sort by
    try {
      Files result = apiInstance.getFiles(xeroTenantId, pagesize, page, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFiles");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **pagesize** | **Integer**| pass an optional page size value | [optional] |
| **page** | **Integer**| number of records to skip for pagination | [optional] |
| **sort** | **String**| values to sort by | [optional] [enum: Name, Size, CreatedDateUTC] |

### Return type

[**Files**](Files.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getFolder"></a>
# **getFolder**
> Folder getFolder(xeroTenantId, folderId)

Retrieves specific folder by using a unique folder ID

By passing in the appropriate ID, you can search for specific folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID folderId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Folder id for single object
    try {
      Folder result = apiInstance.getFolder(xeroTenantId, folderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFolder");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **folderId** | **UUID**| Folder id for single object | |

### Return type

[**Folder**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getFolders"></a>
# **getFolders**
> List&lt;Folder&gt; getFolders(xeroTenantId, sort)

Retrieves folders

By passing in the appropriate options, you can search for available folders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String sort = "Name"; // String | values to sort by
    try {
      List<Folder> result = apiInstance.getFolders(xeroTenantId, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getFolders");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **sort** | **String**| values to sort by | [optional] [enum: Name, Size, CreatedDateUTC] |

### Return type

[**List&lt;Folder&gt;**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="getInbox"></a>
# **getInbox**
> Folder getInbox(xeroTenantId)

Retrieves inbox folder

Search for the user inbox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    try {
      Folder result = apiInstance.getInbox(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#getInbox");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**Folder**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results matching criteria |  -  |

<a id="updateFile"></a>
# **updateFile**
> FileObject updateFile(xeroTenantId, fileId, fileObject)

Update a file

Updates file properties of a single file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID fileId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | File id for single object
    FileObject fileObject = new FileObject(); // FileObject | 
    try {
      FileObject result = apiInstance.updateFile(xeroTenantId, fileId, fileObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#updateFile");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **fileId** | **UUID**| File id for single object | |
| **fileObject** | [**FileObject**](FileObject.md)|  | [optional] |

### Return type

[**FileObject**](FileObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful request |  -  |
| **400** | invalid input, object invalid |  -  |

<a id="updateFolder"></a>
# **updateFolder**
> Folder updateFolder(xeroTenantId, folderId, folder)

Updates an existing folder

By passing in the appropriate ID and properties, you can update a folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID folderId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | Folder id for single object
    Folder folder = new Folder(); // Folder | 
    try {
      Folder result = apiInstance.updateFolder(xeroTenantId, folderId, folder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#updateFolder");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **folderId** | **UUID**| Folder id for single object | |
| **folder** | [**Folder**](Folder.md)|  | |

### Return type

[**Folder**](Folder.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | return the updated object |  -  |
| **400** | invalid input, object invalid |  -  |

<a id="uploadFile"></a>
# **uploadFile**
> FileObject uploadFile(xeroTenantId, folderId, body, filename, mimeType, name)

Uploads a File

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/files.xro/1.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID folderId = UUID.fromString("4ff1e5cc-9835-40d5-bb18-09fdb118db9c"); // UUID | pass an optional folder id to save file to specific folder
    byte[] body = null; // byte[] | 
    String filename = "filename_example"; // String | 
    String mimeType = "mimeType_example"; // String | 
    String name = "name_example"; // String | exact name of the file you are uploading
    try {
      FileObject result = apiInstance.uploadFile(xeroTenantId, folderId, body, filename, mimeType, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#uploadFile");
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
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **folderId** | **UUID**| pass an optional folder id to save file to specific folder | [optional] |
| **body** | **byte[]**|  | [optional] |
| **filename** | **String**|  | [optional] |
| **mimeType** | **String**|  | [optional] |
| **name** | **String**| exact name of the file you are uploading | [optional] |

### Return type

[**FileObject**](FileObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful request |  -  |
| **400** | invalid input, object invalid |  -  |

