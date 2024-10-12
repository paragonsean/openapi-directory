# DocumentsApi

All URIs are relative to *http://localhost:7700*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addOrReplaceDocuments**](DocumentsApi.md#addOrReplaceDocuments) | **POST** /indexes/books/documents | Add or replace documents |
| [**addOrUpdateDocuments**](DocumentsApi.md#addOrUpdateDocuments) | **PUT** /indexes/books/documents | Add or update documents |
| [**deleteAllDocuments**](DocumentsApi.md#deleteAllDocuments) | **DELETE** /indexes/books/documents | Delete all documents |
| [**deleteDocuments**](DocumentsApi.md#deleteDocuments) | **POST** /indexes/books/documents/delete-batch | Delete documents |
| [**deleteOneDocument**](DocumentsApi.md#deleteOneDocument) | **DELETE** /indexes/books/documents/1 | Delete one document |
| [**getDocuments**](DocumentsApi.md#getDocuments) | **GET** /indexes/books/documents | Get documents |
| [**getOneDocument**](DocumentsApi.md#getOneDocument) | **GET** /indexes/books/documents/2 | Get one document |


<a id="addOrReplaceDocuments"></a>
# **addOrReplaceDocuments**
> addOrReplaceDocuments(primaryKey, csvDelimiter, addOrReplaceDocumentsRequestInner)

Add or replace documents

Add or replace documents

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
    defaultClient.setBasePath("http://localhost:7700");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String primaryKey = "id"; // String | 
    String csvDelimiter = ";"; // String | 
    List<AddOrReplaceDocumentsRequestInner> addOrReplaceDocumentsRequestInner = Arrays.asList(); // List<AddOrReplaceDocumentsRequestInner> | 
    try {
      apiInstance.addOrReplaceDocuments(primaryKey, csvDelimiter, addOrReplaceDocumentsRequestInner);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#addOrReplaceDocuments");
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
| **primaryKey** | **String**|  | [optional] |
| **csvDelimiter** | **String**|  | [optional] |
| **addOrReplaceDocumentsRequestInner** | [**List&lt;AddOrReplaceDocumentsRequestInner&gt;**](AddOrReplaceDocumentsRequestInner.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="addOrUpdateDocuments"></a>
# **addOrUpdateDocuments**
> addOrUpdateDocuments(primaryKey, csvDelimiter, addOrUpdateDocumentsRequestInner)

Add or update documents

Add or update documents

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
    defaultClient.setBasePath("http://localhost:7700");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String primaryKey = "id"; // String | 
    String csvDelimiter = ";"; // String | 
    List<AddOrUpdateDocumentsRequestInner> addOrUpdateDocumentsRequestInner = Arrays.asList(); // List<AddOrUpdateDocumentsRequestInner> | 
    try {
      apiInstance.addOrUpdateDocuments(primaryKey, csvDelimiter, addOrUpdateDocumentsRequestInner);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#addOrUpdateDocuments");
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
| **primaryKey** | **String**|  | [optional] |
| **csvDelimiter** | **String**|  | [optional] |
| **addOrUpdateDocumentsRequestInner** | [**List&lt;AddOrUpdateDocumentsRequestInner&gt;**](AddOrUpdateDocumentsRequestInner.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deleteAllDocuments"></a>
# **deleteAllDocuments**
> deleteAllDocuments()

Delete all documents

Delete all documents

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
    defaultClient.setBasePath("http://localhost:7700");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    try {
      apiInstance.deleteAllDocuments();
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#deleteAllDocuments");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deleteDocuments"></a>
# **deleteDocuments**
> deleteDocuments(bigDecimal)

Delete documents

Delete documents

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
    defaultClient.setBasePath("http://localhost:7700");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    List<BigDecimal> bigDecimal = [1,2]; // List<BigDecimal> | 
    try {
      apiInstance.deleteDocuments(bigDecimal);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#deleteDocuments");
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
| **bigDecimal** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deleteOneDocument"></a>
# **deleteOneDocument**
> deleteOneDocument()

Delete one document

Delete one document

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
    defaultClient.setBasePath("http://localhost:7700");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    try {
      apiInstance.deleteOneDocument();
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#deleteOneDocument");
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

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getDocuments"></a>
# **getDocuments**
> getDocuments(limit, offset, fields)

Get documents

Get documents

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
    defaultClient.setBasePath("http://localhost:7700");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String limit = "1"; // String | 
    String offset = "10"; // String | 
    String fields = "id"; // String | 
    try {
      apiInstance.getDocuments(limit, offset, fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#getDocuments");
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
| **limit** | **String**|  | [optional] |
| **offset** | **String**|  | [optional] |
| **fields** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getOneDocument"></a>
# **getOneDocument**
> getOneDocument(fields)

Get one document

Get one document

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
    defaultClient.setBasePath("http://localhost:7700");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String fields = "id"; // String | 
    try {
      apiInstance.getOneDocument(fields);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#getOneDocument");
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
| **fields** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

