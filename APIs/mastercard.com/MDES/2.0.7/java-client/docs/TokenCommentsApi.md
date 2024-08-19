# TokenCommentsApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tokenCommentsPost**](TokenCommentsApi.md#tokenCommentsPost) | **POST** /token/comments |  |


<a id="tokenCommentsPost"></a>
# **tokenCommentsPost**
> TokenCommentsResponseSchema tokenCommentsPost(tokenCommentsRequestSchema)



Used to retrieve all comments associated with a token. Typically the response includes comments created earlier by Issuer Customer Service representatives detailing additional information about a particular inquiry or event. There may also be comments with warnings of potential fraud. These comments are created automatically by the MDES system when a Token requestor indicates a high risk of fraud during digitization. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/mdes/csapi/v2");

    TokenCommentsApi apiInstance = new TokenCommentsApi(defaultClient);
    TokenCommentsRequestSchema tokenCommentsRequestSchema = new TokenCommentsRequestSchema(); // TokenCommentsRequestSchema | Contains the details of the request message.
    try {
      TokenCommentsResponseSchema result = apiInstance.tokenCommentsPost(tokenCommentsRequestSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenCommentsApi#tokenCommentsPost");
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
| **tokenCommentsRequestSchema** | [**TokenCommentsRequestSchema**](TokenCommentsRequestSchema.md)| Contains the details of the request message. | [optional] |

### Return type

[**TokenCommentsResponseSchema**](TokenCommentsResponseSchema.md)

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

