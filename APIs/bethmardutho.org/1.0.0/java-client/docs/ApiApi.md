# ApiApi

All URIs are relative to *http://sedra.bethmardutho.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lexemeIdGet**](ApiApi.md#lexemeIdGet) | **GET** /lexeme/{id} | Get Syriac lexeme. |
| [**wordIdGet**](ApiApi.md#wordIdGet) | **GET** /word/{id} | Get Syriac word. |


<a id="lexemeIdGet"></a>
# **lexemeIdGet**
> LexemeIdGet200Response lexemeIdGet(id)

Get Syriac lexeme.

Returns linguistic information for a Syriac lexeme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://sedra.bethmardutho.org/api");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String id = "id_example"; // String | The Id of a lexeme from the Sedra database.
    try {
      LexemeIdGet200Response result = apiInstance.lexemeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#lexemeIdGet");
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
| **id** | **String**| The Id of a lexeme from the Sedra database. | |

### Return type

[**LexemeIdGet200Response**](LexemeIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Syriac lexeme. |  -  |

<a id="wordIdGet"></a>
# **wordIdGet**
> List&lt;WordIdGet200ResponseInner&gt; wordIdGet(id)

Get Syriac word.

Returns an array of linguistic information for every word that matches the Syriac word. Adjustment is made if the Syriac word is consonantal, partially, or fully vocalized.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://sedra.bethmardutho.org/api");

    ApiApi apiInstance = new ApiApi(defaultClient);
    String id = "id_example"; // String | The id parameters must contain either the Id of a word from the Sedra database or a Syriac word in the unicode character set. When the id parameter is a Syriac word it may be consonantal, partially vocalized, or fully vocalized. Fully vocalized Syriac words will have less false positive results than partially vocalized or consonantal Syriac words. When id is the Id of a word from the SEDRA database then that word will be the only word in the result.
    try {
      List<WordIdGet200ResponseInner> result = apiInstance.wordIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiApi#wordIdGet");
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
| **id** | **String**| The id parameters must contain either the Id of a word from the Sedra database or a Syriac word in the unicode character set. When the id parameter is a Syriac word it may be consonantal, partially vocalized, or fully vocalized. Fully vocalized Syriac words will have less false positive results than partially vocalized or consonantal Syriac words. When id is the Id of a word from the SEDRA database then that word will be the only word in the result. | |

### Return type

[**List&lt;WordIdGet200ResponseInner&gt;**](WordIdGet200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Syriac words. |  -  |

