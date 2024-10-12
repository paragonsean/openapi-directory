# ChangelogApi

All URIs are relative to *https://dash.readme.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createChangelog**](ChangelogApi.md#createChangelog) | **POST** /changelogs | Create changelog |
| [**deleteChangelog**](ChangelogApi.md#deleteChangelog) | **DELETE** /changelogs/{slug} | Delete changelog |
| [**getChangelog**](ChangelogApi.md#getChangelog) | **GET** /changelogs/{slug} | Get changelog |
| [**getChangelogs**](ChangelogApi.md#getChangelogs) | **GET** /changelogs | Get changelogs |
| [**updateChangelog**](ChangelogApi.md#updateChangelog) | **PUT** /changelogs/{slug} | Update changelog |


<a id="createChangelog"></a>
# **createChangelog**
> createChangelog(changelog)

Create changelog

Create a new changelog inside of this project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangelogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ChangelogApi apiInstance = new ChangelogApi(defaultClient);
    Changelog changelog = new Changelog(); // Changelog | Changelog object
    try {
      apiInstance.createChangelog(changelog);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangelogApi#createChangelog");
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
| **changelog** | [**Changelog**](Changelog.md)| Changelog object | |

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
| **201** | The changelog has successfully been created |  -  |
| **400** | There was a validation error during creation |  -  |

<a id="deleteChangelog"></a>
# **deleteChangelog**
> deleteChangelog(slug)

Delete changelog

Delete the changelog with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangelogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ChangelogApi apiInstance = new ChangelogApi(defaultClient);
    String slug = "slug_example"; // String | Slug of changelog
    try {
      apiInstance.deleteChangelog(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangelogApi#deleteChangelog");
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
| **slug** | **String**| Slug of changelog | |

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
| **204** | The changelog has successfully been updated |  -  |
| **404** | There is no changelog with that slug |  -  |

<a id="getChangelog"></a>
# **getChangelog**
> getChangelog(slug)

Get changelog

Returns the changelog with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangelogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ChangelogApi apiInstance = new ChangelogApi(defaultClient);
    String slug = "slug_example"; // String | Slug of changelog
    try {
      apiInstance.getChangelog(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangelogApi#getChangelog");
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
| **slug** | **String**| Slug of changelog | |

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
| **200** | The changelog exists and has been returned |  -  |
| **404** | There is no changelog with that slug |  -  |

<a id="getChangelogs"></a>
# **getChangelogs**
> getChangelogs(perPage, page)

Get changelogs

Returns a list of changelogs associated with the project API key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangelogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ChangelogApi apiInstance = new ChangelogApi(defaultClient);
    Integer perPage = 10; // Integer | Number of items to include in pagination (up to 100, defaults to 10)
    Integer page = 1; // Integer | Used to specify further pages (starts at 1)
    try {
      apiInstance.getChangelogs(perPage, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangelogApi#getChangelogs");
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
| **perPage** | **Integer**| Number of items to include in pagination (up to 100, defaults to 10) | [optional] [default to 10] |
| **page** | **Integer**| Used to specify further pages (starts at 1) | [optional] [default to 1] |

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
| **200** | OK |  * Link -  <br>  |

<a id="updateChangelog"></a>
# **updateChangelog**
> updateChangelog(slug, changelog)

Update changelog

Update a changelog with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChangelogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    ChangelogApi apiInstance = new ChangelogApi(defaultClient);
    String slug = "slug_example"; // String | Slug of changelog
    Changelog changelog = new Changelog(); // Changelog | Changelog object
    try {
      apiInstance.updateChangelog(slug, changelog);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChangelogApi#updateChangelog");
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
| **slug** | **String**| Slug of changelog | |
| **changelog** | [**Changelog**](Changelog.md)| Changelog object | |

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
| **200** | The changelog has successfully been updated |  -  |
| **400** | There was a validation error during update |  -  |
| **404** | There is no changelog with that slug |  -  |

