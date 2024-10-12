# WikisApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**wikiContent**](WikisApi.md#wikiContent) | **GET** /wikis/{wiki_id}/content/ | Retrieve the Content of a Wiki |
| [**wikiRead**](WikisApi.md#wikiRead) | **GET** /wikis/{wiki_id}/ | Retrieve a Wiki |


<a id="wikiContent"></a>
# **wikiContent**
> wikiContent(wikiId)

Retrieve the Content of a Wiki

Retrieves the plaintext content of a wiki in markdown format. #### Returns Returns &#x60;text/markdown&#x60; of the wiki content itself. If the request is unsuccessful, plaintext with the error message will be displayed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WikisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    WikisApi apiInstance = new WikisApi(defaultClient);
    String wikiId = "wikiId_example"; // String | The unique identifier of the wiki.
    try {
      apiInstance.wikiContent(wikiId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WikisApi#wikiContent");
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
| **wikiId** | **String**| The unique identifier of the wiki. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="wikiRead"></a>
# **wikiRead**
> Wiki wikiRead(wikiId)

Retrieve a Wiki

Retrieves the details about a specific wiki. A wiki is a collection of markdown text pages that can be used to describe the project or dataset of contained in the attached node. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested wiki, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WikisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    WikisApi apiInstance = new WikisApi(defaultClient);
    String wikiId = "wikiId_example"; // String | The unique identifier of the wiki.
    try {
      Wiki result = apiInstance.wikiRead(wikiId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WikisApi#wikiRead");
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
| **wikiId** | **String**| The unique identifier of the wiki. | |

### Return type

[**Wiki**](Wiki.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

