# TodosApi

All URIs are relative to *https://gitlab.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteV3Todos**](TodosApi.md#deleteV3Todos) | **DELETE** /v3/todos | Mark all todos as done |
| [**deleteV3TodosId**](TodosApi.md#deleteV3TodosId) | **DELETE** /v3/todos/{id} | Mark a todo as done |
| [**getV3Todos**](TodosApi.md#getV3Todos) | **GET** /v3/todos | Get a todo list |


<a id="deleteV3Todos"></a>
# **deleteV3Todos**
> deleteV3Todos()

Mark all todos as done

Mark all todos as done

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    TodosApi apiInstance = new TodosApi(defaultClient);
    try {
      apiInstance.deleteV3Todos();
    } catch (ApiException e) {
      System.err.println("Exception when calling TodosApi#deleteV3Todos");
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

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Mark all todos as done |  -  |

<a id="deleteV3TodosId"></a>
# **deleteV3TodosId**
> Todo deleteV3TodosId(id)

Mark a todo as done

Mark a todo as done

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    TodosApi apiInstance = new TodosApi(defaultClient);
    Integer id = 56; // Integer | The ID of the todo being marked as done
    try {
      Todo result = apiInstance.deleteV3TodosId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodosApi#deleteV3TodosId");
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
| **id** | **Integer**| The ID of the todo being marked as done | |

### Return type

[**Todo**](Todo.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Mark a todo as done |  -  |

<a id="getV3Todos"></a>
# **getV3Todos**
> Todo getV3Todos(page, perPage)

Get a todo list

Get a todo list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TodosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gitlab.com/api");
    
    // Configure API key authorization: private_token_query
    ApiKeyAuth private_token_query = (ApiKeyAuth) defaultClient.getAuthentication("private_token_query");
    private_token_query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_query.setApiKeyPrefix("Token");

    // Configure API key authorization: private_token_header
    ApiKeyAuth private_token_header = (ApiKeyAuth) defaultClient.getAuthentication("private_token_header");
    private_token_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_token_header.setApiKeyPrefix("Token");

    TodosApi apiInstance = new TodosApi(defaultClient);
    Integer page = 56; // Integer | Current page number
    Integer perPage = 56; // Integer | Number of items per page
    try {
      Todo result = apiInstance.getV3Todos(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TodosApi#getV3Todos");
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
| **page** | **Integer**| Current page number | [optional] |
| **perPage** | **Integer**| Number of items per page | [optional] |

### Return type

[**Todo**](Todo.md)

### Authorization

[private_token_query](../README.md#private_token_query), [private_token_header](../README.md#private_token_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a todo list |  -  |

