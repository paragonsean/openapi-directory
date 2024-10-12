# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1SuggestGet**](DefaultApi.md#apiV1SuggestGet) | **GET** /api/v1/suggest | Get .at domain name suggestions |


<a id="apiV1SuggestGet"></a>
# **apiV1SuggestGet**
> ApiV1SuggestGet200Response apiV1SuggestGet(term)

Get .at domain name suggestions

Provides a list of available .at domain names related to the given input term or domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String term = "mydomain"; // String | Domainname/term to obtain suggestions for
    try {
      ApiV1SuggestGet200Response result = apiInstance.apiV1SuggestGet(term);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiV1SuggestGet");
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
| **term** | **String**| Domainname/term to obtain suggestions for | |

### Return type

[**ApiV1SuggestGet200Response**](ApiV1SuggestGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of domain suggestions |  -  |

