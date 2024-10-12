# LanguagesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesLanguagesIdJsonGet**](LanguagesApi.md#resourcesLanguagesIdJsonGet) | **GET** /resources/languages/{id}.json | Get Language by ID |
| [**resourcesLanguagesJsonGet**](LanguagesApi.md#resourcesLanguagesJsonGet) | **GET** /resources/languages.json | Get Languages |


<a id="resourcesLanguagesIdJsonGet"></a>
# **resourcesLanguagesIdJsonGet**
> List&lt;LanguageWrapped&gt; resourcesLanguagesIdJsonGet(id)

Get Language by ID

Information about a specific language

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    LanguagesApi apiInstance = new LanguagesApi(defaultClient);
    Long id = 56L; // Long | The id of the language to look up
    try {
      List<LanguageWrapped> result = apiInstance.resourcesLanguagesIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguagesApi#resourcesLanguagesIdJsonGet");
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
| **id** | **Long**| The id of the language to look up | |

### Return type

[**List&lt;LanguageWrapped&gt;**](LanguageWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the Language identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesLanguagesJsonGet"></a>
# **resourcesLanguagesJsonGet**
> List&lt;LanguageWrapped&gt; resourcesLanguagesJsonGet(max, offset, sort)

Get Languages

Language Listings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    LanguagesApi apiInstance = new LanguagesApi(defaultClient);
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | Return records starting at the offset index.
    String sort = "sort_example"; // String | The name of the property to which sorting will be applied
    try {
      List<LanguageWrapped> result = apiInstance.resourcesLanguagesJsonGet(max, offset, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguagesApi#resourcesLanguagesJsonGet");
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
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| Return records starting at the offset index. | [optional] |
| **sort** | **String**| The name of the property to which sorting will be applied | [optional] |

### Return type

[**List&lt;LanguageWrapped&gt;**](LanguageWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list Languages. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

