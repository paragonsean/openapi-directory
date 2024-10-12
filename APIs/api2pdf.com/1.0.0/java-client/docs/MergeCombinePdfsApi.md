# MergeCombinePdfsApi

All URIs are relative to *https://v2018.api2pdf.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mergePost**](MergeCombinePdfsApi.md#mergePost) | **POST** /merge | Merge multiple PDFs together |


<a id="mergePost"></a>
# **mergePost**
> ApiResponseSuccess mergePost(mergeRequest)

Merge multiple PDFs together

Merge two or more PDFs together on AWS Lambda. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MergeCombinePdfsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://v2018.api2pdf.com");
    
    // Configure API key authorization: HeaderApiKey
    ApiKeyAuth HeaderApiKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderApiKey");
    HeaderApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderApiKey.setApiKeyPrefix("Token");

    MergeCombinePdfsApi apiInstance = new MergeCombinePdfsApi(defaultClient);
    MergeRequest mergeRequest = new MergeRequest(); // MergeRequest | A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - `urls` *(array of urls, required)* - A JSON array of direct URLs to PDFs. Api2Pdf will consume the PDF files in the list and then merge them all together.. - `inlinePdf` *(boolean, optional)* - Open the PDF in a browser window. Default to false. - `fileName` *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. 
    try {
      ApiResponseSuccess result = apiInstance.mergePost(mergeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MergeCombinePdfsApi#mergePost");
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
| **mergeRequest** | [**MergeRequest**](MergeRequest.md)| A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;urls&#x60; *(array of urls, required)* - A JSON array of direct URLs to PDFs. Api2Pdf will consume the PDF files in the list and then merge them all together.. - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified.  | [optional] |

### Return type

[**ApiResponseSuccess**](ApiResponseSuccess.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON object containing the url to the PDF and other meta data |  -  |
| **401** | Failed to generate PDF |  -  |

