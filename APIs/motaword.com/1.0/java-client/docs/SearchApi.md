# SearchApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkDocumentsReindex**](SearchApi.md#checkDocumentsReindex) | **GET** /search/documents/reindex/status | Check reindex status of the client source and translation documents. |
| [**reindexDocuments**](SearchApi.md#reindexDocuments) | **POST** /search/documents/reindex | Reindex for search all of the client source and translation documents. |
| [**searchEverywhere**](SearchApi.md#searchEverywhere) | **GET** /search | Search everything in your account |


<a id="checkDocumentsReindex"></a>
# **checkDocumentsReindex**
> AsyncOperationStatus checkDocumentsReindex(asyncRequestKey)

Check reindex status of the client source and translation documents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
    try {
      AsyncOperationStatus result = apiInstance.checkDocumentsReindex(asyncRequestKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#checkDocumentsReindex");
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

<a id="reindexDocuments"></a>
# **reindexDocuments**
> AsyncOperationStatus reindexDocuments()

Reindex for search all of the client source and translation documents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    try {
      AsyncOperationStatus result = apiInstance.reindexDocuments();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#reindexDocuments");
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

<a id="searchEverywhere"></a>
# **searchEverywhere**
> SearchEverywhereResult searchEverywhere(query, include, page, perPage)

Search everything in your account

Search through everything in your account, from projects to documents, from source strings to translations...

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String query = "en-US"; // String | Search query term
    List<String> include = Arrays.asList(); // List<String> | Search in these entities. Current oprions are projects, documents, strings. Can be multiple. When not provided, we'll search through all entities.
    Long page = 1L; // Long | 
    Long perPage = 10L; // Long | 
    try {
      SearchEverywhereResult result = apiInstance.searchEverywhere(query, include, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchEverywhere");
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
| **query** | **String**| Search query term | |
| **include** | [**List&lt;String&gt;**](String.md)| Search in these entities. Current oprions are projects, documents, strings. Can be multiple. When not provided, we&#39;ll search through all entities. | [optional] [enum: projects, documents, strings] |
| **page** | **Long**|  | [optional] [default to 1] |
| **perPage** | **Long**|  | [optional] [default to 10] |

### Return type

[**SearchEverywhereResult**](SearchEverywhereResult.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search result for multiple entities and paging |  -  |

