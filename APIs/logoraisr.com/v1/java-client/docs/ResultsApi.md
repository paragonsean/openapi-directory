# ResultsApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resultsRead**](ResultsApi.md#resultsRead) | **GET** /results/{result_file_id}/ | Get the result from image processing |


<a id="resultsRead"></a>
# **resultsRead**
> ResultResponse resultsRead(resultFileId)

Get the result from image processing

This GET-Method returns the URL where the result can downloaded from.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.logoraisr.com/rest-v1");
    
    // Configure API key authorization: Token
    ApiKeyAuth Token = (ApiKeyAuth) defaultClient.getAuthentication("Token");
    Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token.setApiKeyPrefix("Token");

    ResultsApi apiInstance = new ResultsApi(defaultClient);
    String resultFileId = "resultFileId_example"; // String | Id of the result_file for which the result_file_url is generated.
    try {
      ResultResponse result = apiInstance.resultsRead(resultFileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResultsApi#resultsRead");
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
| **resultFileId** | **String**| Id of the result_file for which the result_file_url is generated. | |

### Return type

[**ResultResponse**](ResultResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | BAD REQUEST |  -  |
| **403** | FORBIDDEN |  -  |

