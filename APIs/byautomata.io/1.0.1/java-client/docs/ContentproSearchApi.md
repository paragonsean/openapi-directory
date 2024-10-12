# ContentproSearchApi

All URIs are relative to *https://api.byautomata.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentproSearchGet**](ContentproSearchApi.md#contentproSearchGet) | **GET** /contentpro-search | Send search terms to receive the most relevant articles and companies. |


<a id="contentproSearchGet"></a>
# **contentproSearchGet**
> ContentproSearchGet200Response contentproSearchGet(terms)

Send search terms to receive the most relevant articles and companies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentproSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.byautomata.io");

    ContentproSearchApi apiInstance = new ContentproSearchApi(defaultClient);
    String terms = "terms_example"; // String | We provide information about related companies and articles based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/contentpro-search?terms=cloud+computing,enterprise,security
    try {
      ContentproSearchGet200Response result = apiInstance.contentproSearchGet(terms);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentproSearchApi#contentproSearchGet");
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
| **terms** | [**String**](.md)| We provide information about related companies and articles based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/contentpro-search?terms&#x3D;cloud+computing,enterprise,security | |

### Return type

[**ContentproSearchGet200Response**](ContentproSearchGet200Response.md)

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

