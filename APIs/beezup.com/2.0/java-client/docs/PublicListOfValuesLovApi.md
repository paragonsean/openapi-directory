# PublicListOfValuesLovApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPublicListOfValues**](PublicListOfValuesLovApi.md#getPublicListOfValues) | **GET** /v2/public/lov/{listName} | Get the list of values related to this list name |
| [**getPublicLovIndex**](PublicListOfValuesLovApi.md#getPublicLovIndex) | **GET** /v2/public/lov/ | Get all list names |


<a id="getPublicListOfValues"></a>
# **getPublicListOfValues**
> PublicListOfValuesResponse getPublicListOfValues(listName, acceptLanguage, ifNoneMatch)

Get the list of values related to this list name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicListOfValuesLovApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    PublicListOfValuesLovApi apiInstance = new PublicListOfValuesLovApi(defaultClient);
    String listName = "listName_example"; // String | The list of value name your want to get
    List<String> acceptLanguage = Arrays.asList(); // List<String> | Indicates that the client accepts the following languages.
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      PublicListOfValuesResponse result = apiInstance.getPublicListOfValues(listName, acceptLanguage, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicListOfValuesLovApi#getPublicListOfValues");
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
| **listName** | **String**| The list of value name your want to get | |
| **acceptLanguage** | [**List&lt;String&gt;**](String.md)| Indicates that the client accepts the following languages. | [optional] |
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**PublicListOfValuesResponse**](PublicListOfValuesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of values |  * Cache-Control - Indicates the directive around the caching mechanisms.\\ For more information, please go to this link: https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9  <br>  * Content-Language - Indicates the language use in the response <br>  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you can keep your version. |  * Cache-Control - Indicates the directive around the caching mechanisms.\\ For more information, please go to this link: https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9  <br>  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  |
| **404** | List not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getPublicLovIndex"></a>
# **getPublicLovIndex**
> PublicLovIndex getPublicLovIndex(ifNoneMatch)

Get all list names

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicListOfValuesLovApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    PublicListOfValuesLovApi apiInstance = new PublicListOfValuesLovApi(defaultClient);
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      PublicLovIndex result = apiInstance.getPublicLovIndex(ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicListOfValuesLovApi#getPublicLovIndex");
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
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**PublicLovIndex**](PublicLovIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the list names |  * Cache-Control - Indicates the directive around the caching mechanisms.\\ For more information, please go to this link: https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9  <br>  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you can keep your version. |  * Cache-Control - Indicates the directive around the caching mechanisms.\\ For more information, please go to this link: https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9  <br>  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  |
| **0** | Occurs when something goes wrong |  -  |

