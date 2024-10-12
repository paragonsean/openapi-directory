# PdfGenerationApi

All URIs are relative to *https://dynamicdocs.p.rapidapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**compile**](PdfGenerationApi.md#compile) | **POST** /templates/{template-token}/compile | Compile New Document PDF |


<a id="compile"></a>
# **compile**
> Object compile(templateToken, contentType, docUrlExpiresIn, latexCompiler, latexRuns, mainFileName, docFileName, body)

Compile New Document PDF

Compile a PDF document from a specific template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfGenerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dynamicdocs.p.rapidapi.com");
    
    // Configure API key authorization: Adv-Security-Token
    ApiKeyAuth Adv-Security-Token = (ApiKeyAuth) defaultClient.getAuthentication("Adv-Security-Token");
    Adv-Security-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Adv-Security-Token.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    PdfGenerationApi apiInstance = new PdfGenerationApi(defaultClient);
    String templateToken = "7a582350acb835ed"; // String | The template-token is available in your template settings after publishing your template.
    String contentType = "application/json"; // String | Should be set to \"application/json\"
    Integer docUrlExpiresIn = 3600; // Integer | The doc-url-expires-in is a numerical parameter which takes integers and describes after how many seconds the provided URL is available to download the document.
    String latexCompiler = "pdflatex"; // String | The latex-compiler parameter can take the following values:  pdflatex lualatex
    Integer latexRuns = 56; // Integer | The latex-runs is a numerical parameter and can take values of 1, 2 and 3. 
    String mainFileName = "inputFile.tex"; // String | The main-file-name is a string parameter which identifies the main file to compile.
    String docFileName = "brilliantDocument"; // String | The doc-file-name is a string parameter which determines the name of the file. Note that the extension of the file is not required.
    Object body = {"amount":"ZAR 100 000","client":{"address":"xx Long Street","company":"ABC Company Pty Ltd","firstName":"John","lastName":"Smith","location":"Cape Town, South Africa"},"consultant":{"address":"xx Rivonia Road","company":"XYZ Company Pty Ltd","firstName":"Kobus","lastName":"van der Merwe","location":"Sandton, South Africa"},"effectiveDate":"1 February 2021","servicesDescription":"perform analysis on the company's clients and identify existing market segments"}; // Object | Post the dynamic data for the template to compile the document PDF.
    try {
      Object result = apiInstance.compile(templateToken, contentType, docUrlExpiresIn, latexCompiler, latexRuns, mainFileName, docFileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfGenerationApi#compile");
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
| **templateToken** | **String**| The template-token is available in your template settings after publishing your template. | |
| **contentType** | **String**| Should be set to \&quot;application/json\&quot; | [default to application/json] |
| **docUrlExpiresIn** | **Integer**| The doc-url-expires-in is a numerical parameter which takes integers and describes after how many seconds the provided URL is available to download the document. | [optional] |
| **latexCompiler** | **String**| The latex-compiler parameter can take the following values:  pdflatex lualatex | [optional] [enum: pdflatex, lualatex] |
| **latexRuns** | **Integer**| The latex-runs is a numerical parameter and can take values of 1, 2 and 3.  | [optional] |
| **mainFileName** | **String**| The main-file-name is a string parameter which identifies the main file to compile. | [optional] |
| **docFileName** | **String**| The doc-file-name is a string parameter which determines the name of the file. Note that the extension of the file is not required. | [optional] |
| **body** | **Object**| Post the dynamic data for the template to compile the document PDF. | [optional] |

### Return type

**Object**

### Authorization

[Adv-Security-Token](../README.md#Adv-Security-Token), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document Status URL Created |  -  |
| **401** | Unauthorized |  -  |

