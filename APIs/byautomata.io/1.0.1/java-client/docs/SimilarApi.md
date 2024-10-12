# SimilarApi

All URIs are relative to *https://api.byautomata.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**similarGet**](SimilarApi.md#similarGet) | **GET** /similar | Send a company website to receive a list of companies related to them. |


<a id="similarGet"></a>
# **similarGet**
> SimilarGet200Response similarGet(link, page)

Send a company website to receive a list of companies related to them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SimilarApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.byautomata.io");

    SimilarApi apiInstance = new SimilarApi(defaultClient);
    String link = "link_example"; // String | We'll provide information about related companies based on the site you provide. If a LinkedIn page is sent, we will try to identify the company related to the page. Ex. https://api.byautomata.io/similar?link=ibm.com
    String page = "0"; // String | Page number of search results. Ex. https://api.byautomata.io/similar?link=ibm.com&page=1
    try {
      SimilarGet200Response result = apiInstance.similarGet(link, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SimilarApi#similarGet");
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
| **link** | [**String**](.md)| We&#39;ll provide information about related companies based on the site you provide. If a LinkedIn page is sent, we will try to identify the company related to the page. Ex. https://api.byautomata.io/similar?link&#x3D;ibm.com | |
| **page** | [**String**](.md)| Page number of search results. Ex. https://api.byautomata.io/similar?link&#x3D;ibm.com&amp;page&#x3D;1 | [optional] [default to 0] |

### Return type

[**SimilarGet200Response**](SimilarGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation |  -  |
| **400** | Your request was not valid. Please refer to the API documentation https://api-specs.byautomata.io. |  -  |
| **403** | Invalid API Key. Please refer to the API documentation https://api-specs.byautomata.io. |  -  |
| **501** | There was a server error. Please try again later or contact support@byautomata.io |  -  |

