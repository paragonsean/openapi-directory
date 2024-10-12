# AToZApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProgrammesAtoZSearch**](AToZApi.md#getProgrammesAtoZSearch) | **GET** /atoz/{letter}/programmes | Programmes by initial title character |


<a id="getProgrammesAtoZSearch"></a>
# **getProgrammesAtoZSearch**
> Object getProgrammesAtoZSearch(letter, rights, page, perPage, initialChildCount, sort, sortDirection, availability)

Programmes by initial title character

Get the Programmes whose title begins with the given initial character.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AToZApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    AToZApi apiInstance = new AToZApi(defaultClient);
    String letter = "letter_example"; // String | Letter to search by, a to z or the string '0-9'
    String rights = "mobile"; // String | The rights group to limit results to.
    Long page = 56L; // Long | The page index.
    Long perPage = 56L; // Long | The number of results to return.
    Integer initialChildCount = 4; // Integer | The depth to return child entities.
    String sort = "title"; // String | The sort order of the results.
    String sortDirection = "asc"; // String | Whether to sort ascending or descending
    String availability = "all"; // String | Whether to return all, or available programmes
    try {
      Object result = apiInstance.getProgrammesAtoZSearch(letter, rights, page, perPage, initialChildCount, sort, sortDirection, availability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AToZApi#getProgrammesAtoZSearch");
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
| **letter** | **String**| Letter to search by, a to z or the string &#39;0-9&#39; | |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **page** | **Long**| The page index. | |
| **perPage** | **Long**| The number of results to return. | |
| **initialChildCount** | **Integer**| The depth to return child entities. | [default to 4] |
| **sort** | **String**| The sort order of the results. | [enum: title] |
| **sortDirection** | **String**| Whether to sort ascending or descending | [enum: asc, desc] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

