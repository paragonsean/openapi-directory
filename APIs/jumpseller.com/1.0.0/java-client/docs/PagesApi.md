# PagesApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pagesCountJsonGet**](PagesApi.md#pagesCountJsonGet) | **GET** /pages/count.json | Count all Pages. |
| [**pagesIdJsonDelete**](PagesApi.md#pagesIdJsonDelete) | **DELETE** /pages/{id}.json | Delete an existing Page. |
| [**pagesIdJsonGet**](PagesApi.md#pagesIdJsonGet) | **GET** /pages/{id}.json | Retrieve a single Page by id. |
| [**pagesIdJsonPut**](PagesApi.md#pagesIdJsonPut) | **PUT** /pages/{id}.json | Update a Page. |
| [**pagesJsonGet**](PagesApi.md#pagesJsonGet) | **GET** /pages.json | Retrieve all Pages. |
| [**pagesJsonPost**](PagesApi.md#pagesJsonPost) | **POST** /pages.json | Create a new Page. |


<a id="pagesCountJsonGet"></a>
# **pagesCountJsonGet**
> Count pagesCountJsonGet(login, authtoken)

Count all Pages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    try {
      Count result = apiInstance.pagesCountJsonGet(login, authtoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#pagesCountJsonGet");
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
| **200** | Total number of pages |  -  |

<a id="pagesIdJsonDelete"></a>
# **pagesIdJsonDelete**
> String pagesIdJsonDelete(login, authtoken, id)

Delete an existing Page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Page
    try {
      String result = apiInstance.pagesIdJsonDelete(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#pagesIdJsonDelete");
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
| **id** | **Integer**| Id of the Page | |

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
| **404** | Page Not Found. |  -  |

<a id="pagesIdJsonGet"></a>
# **pagesIdJsonGet**
> Page pagesIdJsonGet(login, authtoken, id)

Retrieve a single Page by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Page
    try {
      Page result = apiInstance.pagesIdJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#pagesIdJsonGet");
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
| **id** | **Integer**| Id of the Page | |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Page Not Found. |  -  |

<a id="pagesIdJsonPut"></a>
# **pagesIdJsonPut**
> Page pagesIdJsonPut(login, authtoken, id, pageModify)

Update a Page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Page
    PageModify pageModify = new PageModify(); // PageModify | Page parameters.
    try {
      Page result = apiInstance.pagesIdJsonPut(login, authtoken, id, pageModify);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#pagesIdJsonPut");
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
| **id** | **Integer**| Id of the Page | |
| **pageModify** | [**PageModify**](PageModify.md)| Page parameters. | |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Page Not Found. |  -  |

<a id="pagesJsonGet"></a>
# **pagesJsonGet**
> List&lt;Page&gt; pagesJsonGet(login, authtoken, limit, page)

Retrieve all Pages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer limit = 50; // Integer | List restriction
    Integer page = 1; // Integer | List page
    try {
      List<Page> result = apiInstance.pagesJsonGet(login, authtoken, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#pagesJsonGet");
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
| **limit** | **Integer**| List restriction | [optional] [default to 50] |
| **page** | **Integer**| List page | [optional] [default to 1] |

### Return type

[**List&lt;Page&gt;**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Pages |  -  |

<a id="pagesJsonPost"></a>
# **pagesJsonPost**
> Page pagesJsonPost(login, authtoken, pageModify)

Create a new Page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    PageModify pageModify = new PageModify(); // PageModify | Page parameters.
    try {
      Page result = apiInstance.pagesJsonPost(login, authtoken, pageModify);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#pagesJsonPost");
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
| **pageModify** | [**PageModify**](PageModify.md)| Page parameters. | |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

