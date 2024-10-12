# SubjectApi

All URIs are relative to *https://api.isbndb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subjectNameGet**](SubjectApi.md#subjectNameGet) | **GET** /subject/{name} | Gets subject details |
| [**subjectsQueryGet**](SubjectApi.md#subjectsQueryGet) | **GET** /subjects/{query} | Search subjects |


<a id="subjectNameGet"></a>
# **subjectNameGet**
> Subject subjectNameGet(name)

Gets subject details

Returns details and a list of books with subject.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SubjectApi apiInstance = new SubjectApi(defaultClient);
    String name = "name_example"; // String | A subject in the Subject's database
    try {
      Subject result = apiInstance.subjectNameGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubjectApi#subjectNameGet");
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
| **name** | **String**| A subject in the Subject&#39;s database | |

### Return type

[**Subject**](Subject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The subject was found in the database |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |
| **404** | Subject not found |  -  |

<a id="subjectsQueryGet"></a>
# **subjectsQueryGet**
> subjectsQueryGet(query, pageSize, page)

Search subjects

This returns a list of subjects that match the given query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SubjectApi apiInstance = new SubjectApi(defaultClient);
    String query = "query_example"; // String | A string to search for in the Subject’s database
    String pageSize = "pageSize_example"; // String | How many items should be returned per page, maximum of 1,000
    String page = "page_example"; // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    try {
      apiInstance.subjectsQueryGet(query, pageSize, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubjectApi#subjectsQueryGet");
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
| **query** | **String**| A string to search for in the Subject’s database | |
| **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] |
| **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The query string found results in the subject&#39;s database |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |
| **404** | There are no results in the subject&#39;s database for the given query |  -  |

