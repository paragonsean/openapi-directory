# NodeApi

All URIs are relative to *https://api.breadcrumbs.one*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**nodePost**](NodeApi.md#nodePost) | **POST** /node | Shows the incoming and outgoing transactions from blockchain address |


<a id="nodePost"></a>
# **nodePost**
> BreadcrumbsAPIModelsNodeNodeResponse nodePost(breadcrumbsAPIModelsNodeNodeRequest)

Shows the incoming and outgoing transactions from blockchain address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.breadcrumbs.one");
    
    // Configure API key authorization: X-API-KEY
    ApiKeyAuth X-API-KEY = (ApiKeyAuth) defaultClient.getAuthentication("X-API-KEY");
    X-API-KEY.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-KEY.setApiKeyPrefix("Token");

    NodeApi apiInstance = new NodeApi(defaultClient);
    BreadcrumbsAPIModelsNodeNodeRequest breadcrumbsAPIModelsNodeNodeRequest = new BreadcrumbsAPIModelsNodeNodeRequest(); // BreadcrumbsAPIModelsNodeNodeRequest | 
    try {
      BreadcrumbsAPIModelsNodeNodeResponse result = apiInstance.nodePost(breadcrumbsAPIModelsNodeNodeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NodeApi#nodePost");
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
| **breadcrumbsAPIModelsNodeNodeRequest** | [**BreadcrumbsAPIModelsNodeNodeRequest**](BreadcrumbsAPIModelsNodeNodeRequest.md)|  | [optional] |

### Return type

[**BreadcrumbsAPIModelsNodeNodeResponse**](BreadcrumbsAPIModelsNodeNodeResponse.md)

### Authorization

[X-API-KEY](../README.md#X-API-KEY)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **422** | Client Error |  -  |

