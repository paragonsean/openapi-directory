# JodApi

All URIs are relative to *https://api.jokes.one*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jodCategoriesGet**](JodApi.md#jodCategoriesGet) | **GET** /jod/categories |  |
| [**jodGet**](JodApi.md#jodGet) | **GET** /jod |  |


<a id="jodCategoriesGet"></a>
# **jodCategoriesGet**
> jodCategoriesGet()



Gets a list of &#x60;Joke of the Day&#x60; Categories. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");
    
    // Configure API key authorization: X-JokesOne-Api-Secret
    ApiKeyAuth X-JokesOne-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-JokesOne-Api-Secret");
    X-JokesOne-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-JokesOne-Api-Secret.setApiKeyPrefix("Token");

    JodApi apiInstance = new JodApi(defaultClient);
    try {
      apiInstance.jodCategoriesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling JodApi#jodCategoriesGet");
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

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |

<a id="jodGet"></a>
# **jodGet**
> JokeOfTheDayResponse jodGet(category)



Gets &#x60;Joke of the Day&#x60;. Optional &#x60;category&#x60; param determines the category of returned joke of the day 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jokes.one");
    
    // Configure API key authorization: X-JokesOne-Api-Secret
    ApiKeyAuth X-JokesOne-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-JokesOne-Api-Secret");
    X-JokesOne-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-JokesOne-Api-Secret.setApiKeyPrefix("Token");

    JodApi apiInstance = new JodApi(defaultClient);
    String category = "category_example"; // String | JOD Category
    try {
      JokeOfTheDayResponse result = apiInstance.jodGet(category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JodApi#jodGet");
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
| **category** | **String**| JOD Category | [optional] |

### Return type

[**JokeOfTheDayResponse**](JokeOfTheDayResponse.md)

### Authorization

[X-JokesOne-Api-Secret](../README.md#X-JokesOne-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |

