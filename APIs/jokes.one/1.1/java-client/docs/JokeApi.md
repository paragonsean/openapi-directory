# JokeApi

All URIs are relative to *https://api.jokes.one*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jokeCategoriesSearchGet**](JokeApi.md#jokeCategoriesSearchGet) | **GET** /joke/categories/search |  |
| [**jokeDelete**](JokeApi.md#jokeDelete) | **DELETE** /joke |  |
| [**jokeGet**](JokeApi.md#jokeGet) | **GET** /joke |  |
| [**jokeListGet**](JokeApi.md#jokeListGet) | **GET** /joke/list |  |
| [**jokePatch**](JokeApi.md#jokePatch) | **PATCH** /joke |  |
| [**jokePut**](JokeApi.md#jokePut) | **PUT** /joke |  |
| [**jokeRandomGet**](JokeApi.md#jokeRandomGet) | **GET** /joke/random |  |
| [**jokeSearchGet**](JokeApi.md#jokeSearchGet) | **GET** /joke/search |  |
| [**jokeTagsAddPost**](JokeApi.md#jokeTagsAddPost) | **POST** /joke/tags/add |  |
| [**jokeTagsRemovePost**](JokeApi.md#jokeTagsRemovePost) | **POST** /joke/tags/remove |  |


<a id="jokeCategoriesSearchGet"></a>
# **jokeCategoriesSearchGet**
> jokeCategoriesSearchGet(query, start)



Gets a list of &#x60;Joke&#x60; Categories, based on a query term. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");
    
    // Configure API key authorization: X-JokesOne-Api-Secret
    ApiKeyAuth X-JokesOne-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-JokesOne-Api-Secret");
    X-JokesOne-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-JokesOne-Api-Secret.setApiKeyPrefix("Token");

    JokeApi apiInstance = new JokeApi(defaultClient);
    String query = "query_example"; // String | Search Query
    Integer start = 0; // Integer | Response is paged. This parameter controls where response starts the listing at
    try {
      apiInstance.jokeCategoriesSearchGet(query, start);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokeCategoriesSearchGet");
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
| **query** | **String**| Search Query | |
| **start** | **Integer**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0] |

### Return type

null (empty response body)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |

<a id="jokeDelete"></a>
# **jokeDelete**
> jokeDelete(id)



Delete a joke. The user needs to be the owner of the joke to be able to delete it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");
    
    // Configure API key authorization: X-JokesOne-Api-Secret
    ApiKeyAuth X-JokesOne-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-JokesOne-Api-Secret");
    X-JokesOne-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-JokesOne-Api-Secret.setApiKeyPrefix("Token");

    JokeApi apiInstance = new JokeApi(defaultClient);
    String id = "id_example"; // String | Joke ID
    try {
      apiInstance.jokeDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokeDelete");
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
| **id** | **String**| Joke ID | |

### Return type

null (empty response body)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="jokeGet"></a>
# **jokeGet**
> JokeResponse jokeGet(id)



Gets a &#x60;Joke&#x60; with a given &#x60;id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");
    
    // Configure API key authorization: X-JokesOne-Api-Secret
    ApiKeyAuth X-JokesOne-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-JokesOne-Api-Secret");
    X-JokesOne-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-JokesOne-Api-Secret.setApiKeyPrefix("Token");

    JokeApi apiInstance = new JokeApi(defaultClient);
    String id = "id_example"; // String | Joke ID
    try {
      JokeResponse result = apiInstance.jokeGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokeGet");
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
| **id** | **String**| Joke ID | [optional] |

### Return type

[**JokeResponse**](JokeResponse.md)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="jokeListGet"></a>
# **jokeListGet**
> jokeListGet(start)



Get the list of jokes in your private collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");

    JokeApi apiInstance = new JokeApi(defaultClient);
    Integer start = 0; // Integer | Response is paged. This parameter controls where response starts the listing at
    try {
      apiInstance.jokeListGet(start);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokeListGet");
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
| **start** | **Integer**| Response is paged. This parameter controls where response starts the listing at | [optional] [default to 0] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="jokePatch"></a>
# **jokePatch**
> jokePatch(id, title, text, author, tags)



Update a joke

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");

    JokeApi apiInstance = new JokeApi(defaultClient);
    String id = "id_example"; // String | Joke ID
    String title = "title_example"; // String | title
    String text = "text_example"; // String | text
    String author = "author_example"; // String | Joke Author
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.jokePatch(id, title, text, author, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokePatch");
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
| **id** | **String**| Joke ID | |
| **title** | **String**| title | [optional] |
| **text** | **String**| text | [optional] |
| **author** | **String**| Joke Author | [optional] |
| **tags** | **String**| Comma Separated tags | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="jokePut"></a>
# **jokePut**
> jokePut(title, text, author, tags)



Add a new joke to your private collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");

    JokeApi apiInstance = new JokeApi(defaultClient);
    String title = "title_example"; // String | Joke Title
    String text = "text_example"; // String | Joke Text
    String author = "author_example"; // String | Joke Author
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.jokePut(title, text, author, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokePut");
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
| **title** | **String**| Joke Title | |
| **text** | **String**| Joke Text | |
| **author** | **String**| Joke Author | [optional] |
| **tags** | **String**| Comma Separated tags | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="jokeRandomGet"></a>
# **jokeRandomGet**
> JokeResponse jokeRandomGet()



Gets a &#x60;Random Joke&#x60;. When you are in a hurry this is what you call to get a random famous joke.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");

    JokeApi apiInstance = new JokeApi(defaultClient);
    try {
      JokeResponse result = apiInstance.jokeRandomGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokeRandomGet");
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

[**JokeResponse**](JokeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, application/js

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="jokeSearchGet"></a>
# **jokeSearchGet**
> JokeResponse jokeSearchGet(category, query, minlength, maxlength, author, _private)



Search for a &#x60;Joke&#x60; in Jokes One platform. Optional &#x60;category&#x60; , &#x60;author&#x60;, &#x60;minlength&#x60;, &#x60;maxlength&#x60; params determines the filters applied while searching for the joke. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");
    
    // Configure API key authorization: X-JokesOne-Api-Secret
    ApiKeyAuth X-JokesOne-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-JokesOne-Api-Secret");
    X-JokesOne-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-JokesOne-Api-Secret.setApiKeyPrefix("Token");

    JokeApi apiInstance = new JokeApi(defaultClient);
    String category = "category_example"; // String | Joke Category
    String query = "query_example"; // String | keyword to search for in the joke
    Integer minlength = 100; // Integer | Joke minimum Length
    Integer maxlength = 300; // Integer | Joke maximum Length
    String author = "author_example"; // String | Joke Author
    Boolean _private = false; // Boolean | Should search private collection? Default searches public collection.
    try {
      JokeResponse result = apiInstance.jokeSearchGet(category, query, minlength, maxlength, author, _private);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokeSearchGet");
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
| **category** | **String**| Joke Category | [optional] |
| **query** | **String**| keyword to search for in the joke | [optional] |
| **minlength** | **Integer**| Joke minimum Length | [optional] [default to 100] |
| **maxlength** | **Integer**| Joke maximum Length | [optional] [default to 300] |
| **author** | **String**| Joke Author | [optional] |
| **_private** | **Boolean**| Should search private collection? Default searches public collection. | [optional] [default to false] |

### Return type

[**JokeResponse**](JokeResponse.md)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="jokeTagsAddPost"></a>
# **jokeTagsAddPost**
> jokeTagsAddPost(id, tags)



Add a tag to a given Joke.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");

    JokeApi apiInstance = new JokeApi(defaultClient);
    String id = "id_example"; // String | Joke ID
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.jokeTagsAddPost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokeTagsAddPost");
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
| **id** | **String**| Joke ID | |
| **tags** | **String**| Comma Separated tags | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

<a id="jokeTagsRemovePost"></a>
# **jokeTagsRemovePost**
> jokeTagsRemovePost(id, tags)



Remove a tag from a given joke.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JokeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");

    JokeApi apiInstance = new JokeApi(defaultClient);
    String id = "id_example"; // String | Joke ID
    String tags = "tags_example"; // String | Comma Separated tags
    try {
      apiInstance.jokeTagsRemovePost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling JokeApi#jokeTagsRemovePost");
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
| **id** | **String**| Joke ID | |
| **tags** | **String**| Comma Separated tags | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |
| **404** | 404  response |  -  |

