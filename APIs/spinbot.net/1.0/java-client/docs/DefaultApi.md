# DefaultApi

All URIs are relative to *https://api.spinbot.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInfo**](DefaultApi.md#getInfo) | **GET** /api/acc | Return the user credit information. |
| [**postArticle**](DefaultApi.md#postArticle) | **POST** /api/article | Extracting the main article of the given URL. |
| [**postPrettySpinner**](DefaultApi.md#postPrettySpinner) | **POST** /api/pretty-spinner | Human readable auto rewrite your article. |
| [**postSpinner**](DefaultApi.md#postSpinner) | **POST** /api/spinner | Rewriting (spinning) your input article. |
| [**postSpintax**](DefaultApi.md#postSpintax) | **POST** /api/spintax | Generate Spintax format for the input article |


<a id="getInfo"></a>
# **getInfo**
> Object getInfo(key)

Return the user credit information.

Return the user credit information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spinbot.net");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | Your api key
    try {
      Object result = apiInstance.getInfo(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getInfo");
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
| **key** | **String**| Your api key | |

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="postArticle"></a>
# **postArticle**
> Object postArticle(key, url, fasterMode)

Extracting the main article of the given URL.

Extracting the main article of the given URL. The response is in JSON format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spinbot.net");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | Your spinbot API key
    String url = "url_example"; // String | The url of target article
    String fasterMode = "fasterMode_example"; // String | you can set this input value to 1 to skip detecting the size (width and height in pixel) of all the images inside the extracted article. The response time of your request will be shortened if you set this input value to 1.
    try {
      Object result = apiInstance.postArticle(key, url, fasterMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postArticle");
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
| **key** | **String**| Your spinbot API key | |
| **url** | **String**| The url of target article | |
| **fasterMode** | **String**| you can set this input value to 1 to skip detecting the size (width and height in pixel) of all the images inside the extracted article. The response time of your request will be shortened if you set this input value to 1. | [optional] |

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

<a id="postPrettySpinner"></a>
# **postPrettySpinner**
> Object postPrettySpinner(key, text, keep, accuracy)

Human readable auto rewrite your article.

Human readable auto rewrite your article. The response is in JSON format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spinbot.net");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | Your spinbot API key
    String text = "text_example"; // String | Input article that need to be rewrited.
    String keep = "keep_example"; // String | Keep words/phrases, separated by newline, those remain unchanged during the rewrite process.
    String accuracy = "accuracy_example"; // String | Rewrite accuracy profile, accepted values are very-low, low, medium, high, very-high
    try {
      Object result = apiInstance.postPrettySpinner(key, text, keep, accuracy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postPrettySpinner");
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
| **key** | **String**| Your spinbot API key | |
| **text** | **String**| Input article that need to be rewrited. | |
| **keep** | **String**| Keep words/phrases, separated by newline, those remain unchanged during the rewrite process. | |
| **accuracy** | **String**| Rewrite accuracy profile, accepted values are very-low, low, medium, high, very-high | |

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

<a id="postSpinner"></a>
# **postSpinner**
> Object postSpinner(key, text)

Rewriting (spinning) your input article.

Rewriting (spinning) you input article. The response is in JSON format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spinbot.net");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | Your spinbot API key
    String text = "text_example"; // String | Input article that need to be rewrited.
    try {
      Object result = apiInstance.postSpinner(key, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postSpinner");
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
| **key** | **String**| Your spinbot API key | |
| **text** | **String**| Input article that need to be rewrited. | |

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

<a id="postSpintax"></a>
# **postSpintax**
> Object postSpintax(key, text, fullMode)

Generate Spintax format for the input article

Generate Spintax format for the input article, so you can rewrite it yourself. The response is in JSON format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.spinbot.net");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | Your spinbot API key
    String text = "text_example"; // String | Input article that need to be rewritten.
    String fullMode = "fullMode_example"; // String | Full mode option.
    try {
      Object result = apiInstance.postSpintax(key, text, fullMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postSpintax");
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
| **key** | **String**| Your spinbot API key | |
| **text** | **String**| Input article that need to be rewritten. | |
| **fullMode** | **String**| Full mode option. | [optional] |

### Return type

**Object**

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

