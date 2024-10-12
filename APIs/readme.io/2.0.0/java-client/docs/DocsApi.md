# DocsApi

All URIs are relative to *https://dash.readme.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDoc**](DocsApi.md#createDoc) | **POST** /docs | Create doc |
| [**deleteDoc**](DocsApi.md#deleteDoc) | **DELETE** /docs/{slug} | Delete doc |
| [**getDoc**](DocsApi.md#getDoc) | **GET** /docs/{slug} | Get doc |
| [**searchDocs**](DocsApi.md#searchDocs) | **POST** /docs/search | Search docs |
| [**updateDoc**](DocsApi.md#updateDoc) | **PUT** /docs/{slug} | Update doc |


<a id="createDoc"></a>
# **createDoc**
> createDoc(xReadmeVersion, doc)

Create doc

Create a new doc inside of this project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    DocsApi apiInstance = new DocsApi(defaultClient);
    String xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    Doc doc = new Doc(); // Doc | Doc object
    try {
      apiInstance.createDoc(xReadmeVersion, doc);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocsApi#createDoc");
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
| **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | |
| **doc** | [**Doc**](Doc.md)| Doc object | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The doc has successfully been created |  -  |
| **400** | There was a validation error during creation |  -  |

<a id="deleteDoc"></a>
# **deleteDoc**
> deleteDoc(slug, xReadmeVersion)

Delete doc

Delete the doc with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    DocsApi apiInstance = new DocsApi(defaultClient);
    String slug = "new-features"; // String | Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \"New Features\", enter the slug \"new-features\"
    String xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    try {
      apiInstance.deleteDoc(slug, xReadmeVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocsApi#deleteDoc");
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
| **slug** | **String**| Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \&quot;New Features\&quot;, enter the slug \&quot;new-features\&quot; | |
| **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The doc has successfully been updated |  -  |
| **404** | There is no doc with that slug |  -  |

<a id="getDoc"></a>
# **getDoc**
> getDoc(slug, xReadmeVersion)

Get doc

Returns the doc with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    DocsApi apiInstance = new DocsApi(defaultClient);
    String slug = "new-features"; // String | Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \"New Features\", enter the slug \"new-features\"
    String xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    try {
      apiInstance.getDoc(slug, xReadmeVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocsApi#getDoc");
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
| **slug** | **String**| Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \&quot;New Features\&quot;, enter the slug \&quot;new-features\&quot; | |
| **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The doc exists and has been returned |  -  |
| **404** | There is no doc with that slug |  -  |

<a id="searchDocs"></a>
# **searchDocs**
> searchDocs(search, xReadmeVersion)

Search docs

Returns all docs that match the search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    DocsApi apiInstance = new DocsApi(defaultClient);
    String search = "search_example"; // String | Search string to look for
    String xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    try {
      apiInstance.searchDocs(search, xReadmeVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocsApi#searchDocs");
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
| **search** | **String**| Search string to look for | |
| **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The search was successful and results were returned |  -  |
| **500** | There is an internal error |  -  |

<a id="updateDoc"></a>
# **updateDoc**
> updateDoc(slug, xReadmeVersion, doc)

Update doc

Update a doc with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    DocsApi apiInstance = new DocsApi(defaultClient);
    String slug = "new-features"; // String | Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \"New Features\", enter the slug \"new-features\"
    String xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    Doc doc = new Doc(); // Doc | Doc object
    try {
      apiInstance.updateDoc(slug, xReadmeVersion, doc);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocsApi#updateDoc");
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
| **slug** | **String**| Slug of doc. must be lowercase, and replace spaces with hyphens. For example, for the page titled \&quot;New Features\&quot;, enter the slug \&quot;new-features\&quot; | |
| **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | |
| **doc** | [**Doc**](Doc.md)| Doc object | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The doc has successfully been updated |  -  |
| **400** | There was a validation error during update |  -  |
| **404** | There is no doc with that slug |  -  |

