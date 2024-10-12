# TokenDeleteApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tokenDeletePost**](TokenDeleteApi.md#tokenDeletePost) | **POST** /token/delete |  |


<a id="tokenDeletePost"></a>
# **tokenDeletePost**
> TokenDeleteResponseSchema tokenDeletePost(tokenDeleteRequestSchema)



Used to delete a token so that it may not initiate any new transactions. All authorizations for a deleted token will be declined. A deleted token may not be returned to an active state. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    TokenDeleteApi apiInstance = new TokenDeleteApi(defaultClient);
    TokenDeleteRequestSchema tokenDeleteRequestSchema = new TokenDeleteRequestSchema(); // TokenDeleteRequestSchema | Contains the details of the request message.
    try {
      TokenDeleteResponseSchema result = apiInstance.tokenDeletePost(tokenDeleteRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenDeleteApi#tokenDeletePost");
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
| **tokenDeleteRequestSchema** | [**TokenDeleteRequestSchema**](TokenDeleteRequestSchema.md)| Contains the details of the request message. | [optional] |

### Return type

[**TokenDeleteResponseSchema**](TokenDeleteResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains the details of the response message. |  -  |
| **0** | unexpected error |  -  |

