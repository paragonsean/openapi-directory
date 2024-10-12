# CustomPagesApi

All URIs are relative to *https://dash.readme.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomPage**](CustomPagesApi.md#createCustomPage) | **POST** /custompages | Create custom page |
| [**deleteCustomPage**](CustomPagesApi.md#deleteCustomPage) | **DELETE** /custompages/{slug} | Delete custom page |
| [**getCustomPage**](CustomPagesApi.md#getCustomPage) | **GET** /custompages/{slug} | Get custom page |
| [**getCustomPages**](CustomPagesApi.md#getCustomPages) | **GET** /custompages | Get custom pages |
| [**updateCustomPage**](CustomPagesApi.md#updateCustomPage) | **PUT** /custompages/{slug} | Update custom page |


<a id="createCustomPage"></a>
# **createCustomPage**
> createCustomPage(customPage)

Create custom page

Create a new custom page inside of this project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    CustomPagesApi apiInstance = new CustomPagesApi(defaultClient);
    CustomPage customPage = new CustomPage(); // CustomPage | CustomPage object
    try {
      apiInstance.createCustomPage(customPage);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPagesApi#createCustomPage");
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
| **customPage** | [**CustomPage**](CustomPage.md)| CustomPage object | |

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
| **201** | The custom page has successfully been created |  -  |
| **400** | There was a validation error during creation |  -  |

<a id="deleteCustomPage"></a>
# **deleteCustomPage**
> deleteCustomPage(slug)

Delete custom page

Delete the custom page with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    CustomPagesApi apiInstance = new CustomPagesApi(defaultClient);
    String slug = "slug_example"; // String | Slug of custom page
    try {
      apiInstance.deleteCustomPage(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPagesApi#deleteCustomPage");
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
| **slug** | **String**| Slug of custom page | |

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
| **204** | The custom page has successfully been updated |  -  |
| **404** | There is no custom page with that slug |  -  |

<a id="getCustomPage"></a>
# **getCustomPage**
> getCustomPage(slug)

Get custom page

Returns the custom page with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    CustomPagesApi apiInstance = new CustomPagesApi(defaultClient);
    String slug = "slug_example"; // String | Slug of custom page
    try {
      apiInstance.getCustomPage(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPagesApi#getCustomPage");
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
| **slug** | **String**| Slug of custom page | |

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
| **200** | The custom page exists and has been returned |  -  |
| **404** | There is no custom page with that slug |  -  |

<a id="getCustomPages"></a>
# **getCustomPages**
> getCustomPages(perPage, page)

Get custom pages

Returns a list of custom pages associated with the project API key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    CustomPagesApi apiInstance = new CustomPagesApi(defaultClient);
    Integer perPage = 10; // Integer | Number of items to include in pagination (up to 100, defaults to 10)
    Integer page = 1; // Integer | Used to specify further pages (starts at 1)
    try {
      apiInstance.getCustomPages(perPage, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPagesApi#getCustomPages");
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

<a id="updateCustomPage"></a>
# **updateCustomPage**
> updateCustomPage(slug, customPage)

Update custom page

Update a custom page with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    CustomPagesApi apiInstance = new CustomPagesApi(defaultClient);
    String slug = "slug_example"; // String | Slug of custom page
    CustomPage customPage = new CustomPage(); // CustomPage | CustomPage object
    try {
      apiInstance.updateCustomPage(slug, customPage);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomPagesApi#updateCustomPage");
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
| **slug** | **String**| Slug of custom page | |
| **customPage** | [**CustomPage**](CustomPage.md)| CustomPage object | |

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
| **200** | The custom page has successfully been updated |  -  |
| **400** | There was a validation error during update |  -  |
| **404** | There is no custom page with that slug |  -  |

