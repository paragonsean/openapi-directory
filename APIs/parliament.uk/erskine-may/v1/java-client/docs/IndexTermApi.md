# IndexTermApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiIndexTermBrowseGet**](IndexTermApi.md#apiIndexTermBrowseGet) | **GET** /api/IndexTerm/browse | Returns a list of index terms by start letter. |
| [**apiIndexTermIndexTermIdGet**](IndexTermApi.md#apiIndexTermIndexTermIdGet) | **GET** /api/IndexTerm/{indexTermId} | Returns an index term by id. |


<a id="apiIndexTermBrowseGet"></a>
# **apiIndexTermBrowseGet**
> ErskineMayIndexTermSearchResultErskineMaySearch apiIndexTermBrowseGet(startLetter, skip, take)

Returns a list of index terms by start letter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexTermApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    IndexTermApi apiInstance = new IndexTermApi(defaultClient);
    String startLetter = "startLetter_example"; // String | Index terms by start letter
    Integer skip = 0; // Integer | The number of records to skip from the first, default is 0.
    Integer take = 20; // Integer | The number of records to return, default is 20, maximum is 20.
    try {
      ErskineMayIndexTermSearchResultErskineMaySearch result = apiInstance.apiIndexTermBrowseGet(startLetter, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexTermApi#apiIndexTermBrowseGet");
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
| **startLetter** | **String**| Index terms by start letter | [optional] |
| **skip** | **Integer**| The number of records to skip from the first, default is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of records to return, default is 20, maximum is 20. | [optional] [default to 20] |

### Return type

[**ErskineMayIndexTermSearchResultErskineMaySearch**](ErskineMayIndexTermSearchResultErskineMaySearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiIndexTermIndexTermIdGet"></a>
# **apiIndexTermIndexTermIdGet**
> ErskineMayIndexTerm apiIndexTermIndexTermIdGet(indexTermId)

Returns an index term by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexTermApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    IndexTermApi apiInstance = new IndexTermApi(defaultClient);
    Integer indexTermId = 56; // Integer | Index term by if
    try {
      ErskineMayIndexTerm result = apiInstance.apiIndexTermIndexTermIdGet(indexTermId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexTermApi#apiIndexTermIndexTermIdGet");
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
| **indexTermId** | **Integer**| Index term by if | |

### Return type

[**ErskineMayIndexTerm**](ErskineMayIndexTerm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

