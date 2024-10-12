# DefaultApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aiAlphaSearchMessages**](DefaultApi.md#aiAlphaSearchMessages) | **POST** /ai.alpha.search.messages |  |


<a id="aiAlphaSearchMessages"></a>
# **aiAlphaSearchMessages**
> AiAlphaSearchMessages200Response aiAlphaSearchMessages(searchRequest)



Search for messages matching a query

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
    defaultClient.setBasePath("https://slack.com/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SearchRequest searchRequest = new SearchRequest(); // SearchRequest | 
    try {
      AiAlphaSearchMessages200Response result = apiInstance.aiAlphaSearchMessages(searchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#aiAlphaSearchMessages");
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
| **searchRequest** | [**SearchRequest**](SearchRequest.md)|  | |

### Return type

[**AiAlphaSearchMessages200Response**](AiAlphaSearchMessages200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success response |  -  |

