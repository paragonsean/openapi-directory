# AuthorsApi

All URIs are relative to *https://api.figshare.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateAuthorDetails**](AuthorsApi.md#privateAuthorDetails) | **GET** /account/authors/{author_id} | Author details |
| [**privateAuthorsSearch**](AuthorsApi.md#privateAuthorsSearch) | **POST** /account/authors/search | Search Authors |


<a id="privateAuthorDetails"></a>
# **privateAuthorDetails**
> AuthorComplete privateAuthorDetails(authorId)

Author details

View author details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AuthorsApi apiInstance = new AuthorsApi(defaultClient);
    Long authorId = 56L; // Long | Author unique identifier
    try {
      AuthorComplete result = apiInstance.privateAuthorDetails(authorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorsApi#privateAuthorDetails");
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
| **authorId** | **Long**| Author unique identifier | |

### Return type

[**AuthorComplete**](AuthorComplete.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article representation |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateAuthorsSearch"></a>
# **privateAuthorsSearch**
> List&lt;Author&gt; privateAuthorsSearch(privateAuthorsSearch)

Search Authors

Search for authors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AuthorsApi apiInstance = new AuthorsApi(defaultClient);
    PrivateAuthorsSearch privateAuthorsSearch = new PrivateAuthorsSearch(); // PrivateAuthorsSearch | Search Parameters
    try {
      List<Author> result = apiInstance.privateAuthorsSearch(privateAuthorsSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorsApi#privateAuthorsSearch");
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
| **privateAuthorsSearch** | [**PrivateAuthorsSearch**](PrivateAuthorsSearch.md)| Search Parameters | [optional] |

### Return type

[**List&lt;Author&gt;**](Author.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of authors |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

