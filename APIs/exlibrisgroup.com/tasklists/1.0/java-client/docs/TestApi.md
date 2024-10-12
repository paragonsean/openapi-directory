# TestApi

All URIs are relative to *https://api-eu.hosted.exlibrisgroup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAlmawsV1TaskListsTest**](TestApi.md#getAlmawsV1TaskListsTest) | **GET** /almaws/v1/task-lists/test | GET Task-lists Test API |
| [**postAlmawsV1TaskListsTest**](TestApi.md#postAlmawsV1TaskListsTest) | **POST** /almaws/v1/task-lists/test | POST Task-lists Test API |


<a id="getAlmawsV1TaskListsTest"></a>
# **getAlmawsV1TaskListsTest**
> Object getAlmawsV1TaskListsTest()

GET Task-lists Test API

This API is used to test if the API key was configured correctly.It returns a short XML (no schema available - the output is subject to changes) with the following structure:&lt;test&gt;GET - OK - institutionCode: 01ABC_INST&lt;/test&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    try {
      Object result = apiInstance.getAlmawsV1TaskListsTest();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#getAlmawsV1TaskListsTest");
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

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request   |  -  |
| **500** | Internal Server Error |  -  |

<a id="postAlmawsV1TaskListsTest"></a>
# **postAlmawsV1TaskListsTest**
> Object postAlmawsV1TaskListsTest()

POST Task-lists Test API

This API is used to test if the API key was configured correctly, including read/write permissions.It returns a short XML (no schema available - the output is subject to changes) with the following structure:&lt;test&gt;POST - OK&lt;/test&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-eu.hosted.exlibrisgroup.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TestApi apiInstance = new TestApi(defaultClient);
    try {
      Object result = apiInstance.postAlmawsV1TaskListsTest();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#postAlmawsV1TaskListsTest");
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

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Exl-Api-Remaining -  <br>  |
| **400** | Bad Request   |  -  |
| **500** | Internal Server Error |  -  |

