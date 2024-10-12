# GenerateApi

All URIs are relative to *https://api.mineskin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateUploadPost**](GenerateApi.md#generateUploadPost) | **POST** /generate/upload |  |
| [**generateUrlPost**](GenerateApi.md#generateUrlPost) | **POST** /generate/url |  |
| [**generateUserPost**](GenerateApi.md#generateUserPost) | **POST** /generate/user |  |


<a id="generateUploadPost"></a>
# **generateUploadPost**
> GenerateUploadPost200Response generateUploadPost(userAgent, model, name, variant, visibility, _file)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenerateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mineskin.org");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    GenerateApi apiInstance = new GenerateApi(defaultClient);
    String userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    String model = "steve"; // String | 
    String name = "name_example"; // String | 
    String variant = "classic"; // String | Skin variant - automatically determined based on the image if not specified
    Integer visibility = 0; // Integer | Visibility of the generated skin. 0 for public, 1 for private
    File _file = new File("/path/to/file"); // File | 
    try {
      GenerateUploadPost200Response result = apiInstance.generateUploadPost(userAgent, model, name, variant, visibility, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenerateApi#generateUploadPost");
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
| **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | |
| **model** | **String**|  | [optional] [default to steve] [enum: steve, slim] |
| **name** | **String**|  | [optional] |
| **variant** | **String**| Skin variant - automatically determined based on the image if not specified | [optional] [enum: classic, slim] |
| **visibility** | **Integer**| Visibility of the generated skin. 0 for public, 1 for private | [optional] [default to 0] [enum: 0, 1] |
| **_file** | **File**|  | [optional] |

### Return type

[**GenerateUploadPost200Response**](GenerateUploadPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully generated skin info |  -  |
| **400** | Response if an error occured |  -  |
| **429** | Response if the client sent a request too soon |  -  |
| **500** | Response if an error occured |  -  |

<a id="generateUrlPost"></a>
# **generateUrlPost**
> GenerateUploadPost200Response generateUrlPost(userAgent, generateUrlPostRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenerateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mineskin.org");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    GenerateApi apiInstance = new GenerateApi(defaultClient);
    String userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    GenerateUrlPostRequest generateUrlPostRequest = new GenerateUrlPostRequest(); // GenerateUrlPostRequest | 
    try {
      GenerateUploadPost200Response result = apiInstance.generateUrlPost(userAgent, generateUrlPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenerateApi#generateUrlPost");
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
| **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | |
| **generateUrlPostRequest** | [**GenerateUrlPostRequest**](GenerateUrlPostRequest.md)|  | |

### Return type

[**GenerateUploadPost200Response**](GenerateUploadPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully generated skin info |  -  |
| **400** | Response if an error occured |  -  |
| **429** | Response if the client sent a request too soon |  -  |
| **500** | Response if an error occured |  -  |

<a id="generateUserPost"></a>
# **generateUserPost**
> GenerateUploadPost200Response generateUserPost(userAgent, generateUserPostRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenerateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mineskin.org");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    GenerateApi apiInstance = new GenerateApi(defaultClient);
    String userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    GenerateUserPostRequest generateUserPostRequest = new GenerateUserPostRequest(); // GenerateUserPostRequest | 
    try {
      GenerateUploadPost200Response result = apiInstance.generateUserPost(userAgent, generateUserPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenerateApi#generateUserPost");
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
| **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | |
| **generateUserPostRequest** | [**GenerateUserPostRequest**](GenerateUserPostRequest.md)|  | |

### Return type

[**GenerateUploadPost200Response**](GenerateUploadPost200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully generated skin info |  -  |
| **400** | Response if an error occured |  -  |
| **429** | Response if the client sent a request too soon |  -  |
| **500** | Response if an error occured |  -  |

