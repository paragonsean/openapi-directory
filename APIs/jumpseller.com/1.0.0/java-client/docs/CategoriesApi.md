# CategoriesApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesCountJsonGet**](CategoriesApi.md#categoriesCountJsonGet) | **GET** /categories/count.json | Count all Categories. |
| [**categoriesIdJsonDelete**](CategoriesApi.md#categoriesIdJsonDelete) | **DELETE** /categories/{id}.json | Delete an existing Category. |
| [**categoriesIdJsonGet**](CategoriesApi.md#categoriesIdJsonGet) | **GET** /categories/{id}.json | Retrieve a single Category. |
| [**categoriesIdJsonPut**](CategoriesApi.md#categoriesIdJsonPut) | **PUT** /categories/{id}.json | Modify an existing Category. |
| [**categoriesJsonGet**](CategoriesApi.md#categoriesJsonGet) | **GET** /categories.json | Retrieve all Categories. |
| [**categoriesJsonPost**](CategoriesApi.md#categoriesJsonPost) | **POST** /categories.json | Create a new Category. |


<a id="categoriesCountJsonGet"></a>
# **categoriesCountJsonGet**
> Count categoriesCountJsonGet(login, authtoken)

Count all Categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    try {
      Count result = apiInstance.categoriesCountJsonGet(login, authtoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesCountJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="categoriesIdJsonDelete"></a>
# **categoriesIdJsonDelete**
> String categoriesIdJsonDelete(login, authtoken, id)

Delete an existing Category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Category
    try {
      String result = apiInstance.categoriesIdJsonDelete(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesIdJsonDelete");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Category | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Category Not Found. |  -  |

<a id="categoriesIdJsonGet"></a>
# **categoriesIdJsonGet**
> Category categoriesIdJsonGet(login, authtoken, id)

Retrieve a single Category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Category
    try {
      Category result = apiInstance.categoriesIdJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesIdJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Category | |

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The selected Category. |  -  |
| **404** | Category Not Found. |  -  |

<a id="categoriesIdJsonPut"></a>
# **categoriesIdJsonPut**
> Category categoriesIdJsonPut(login, authtoken, id, categoryEdit)

Modify an existing Category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Category
    CategoryEdit categoryEdit = new CategoryEdit(); // CategoryEdit | Category parameters.
    try {
      Category result = apiInstance.categoriesIdJsonPut(login, authtoken, id, categoryEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesIdJsonPut");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the Category | |
| **categoryEdit** | [**CategoryEdit**](CategoryEdit.md)| Category parameters. | |

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Category Not Found. |  -  |

<a id="categoriesJsonGet"></a>
# **categoriesJsonGet**
> Category categoriesJsonGet(login, authtoken)

Retrieve all Categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    try {
      Category result = apiInstance.categoriesJsonGet(login, authtoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="categoriesJsonPost"></a>
# **categoriesJsonPost**
> Category categoriesJsonPost(login, authtoken, categoryEdit)

Create a new Category.

Category&#39;s permalink is automatically generated from the given category&#39;s name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    CategoryEdit categoryEdit = new CategoryEdit(); // CategoryEdit | Category parameters.
    try {
      Category result = apiInstance.categoriesJsonPost(login, authtoken, categoryEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesJsonPost");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **categoryEdit** | [**CategoryEdit**](CategoryEdit.md)| Category parameters. | |

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

