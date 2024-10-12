# HeadlessChromeApi

All URIs are relative to *https://v2018.api2pdf.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chromeFromHtmlPost**](HeadlessChromeApi.md#chromeFromHtmlPost) | **POST** /chrome/html | Convert raw HTML to PDF |
| [**chromeFromUrlGET**](HeadlessChromeApi.md#chromeFromUrlGET) | **GET** /chrome/url | Convert URL to PDF |
| [**chromeFromUrlPost**](HeadlessChromeApi.md#chromeFromUrlPost) | **POST** /chrome/url | Convert URL to PDF |


<a id="chromeFromHtmlPost"></a>
# **chromeFromHtmlPost**
> ApiResponseSuccess chromeFromHtmlPost(chromeHtmlToPdfRequest)

Convert raw HTML to PDF

Convert HTML to a PDF using Headless Chrome on AWS Lambda. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeadlessChromeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://v2018.api2pdf.com");
    
    // Configure API key authorization: HeaderApiKey
    ApiKeyAuth HeaderApiKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderApiKey");
    HeaderApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderApiKey.setApiKeyPrefix("Token");

    HeadlessChromeApi apiInstance = new HeadlessChromeApi(defaultClient);
    ChromeHtmlToPdfRequest chromeHtmlToPdfRequest = new ChromeHtmlToPdfRequest(); // ChromeHtmlToPdfRequest | A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - `html` *(string, required)* - raw HTML to convert to PDF - `inlinePdf` *(boolean, optional)* - Open the PDF in a browser window. Default to false. - `fileName` *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - `options` *(object, optional)* - Include advanced Headless Chrome options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-headless-chrome/).
    try {
      ApiResponseSuccess result = apiInstance.chromeFromHtmlPost(chromeHtmlToPdfRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeadlessChromeApi#chromeFromHtmlPost");
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
| **chromeHtmlToPdfRequest** | [**ChromeHtmlToPdfRequest**](ChromeHtmlToPdfRequest.md)| A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;html&#x60; *(string, required)* - raw HTML to convert to PDF - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - &#x60;options&#x60; *(object, optional)* - Include advanced Headless Chrome options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-headless-chrome/). | [optional] |

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

<a id="chromeFromUrlGET"></a>
# **chromeFromUrlGET**
> ApiResponseSuccess chromeFromUrlGET(url, output)

Convert URL to PDF

Convert a URL or Web Page to PDF using Headless Chrome on AWS Lambda. This GET request is for convenience and does not support advanced options. Use the POST request for more flexibility. ### Authorize via Query String Parameter **apikey&#x3D;YOUR-API-KEY** ### Example &#x60;&#x60;&#x60; https://v2018.api2pdf.com/chrome/url?url&#x3D;{UrlToConvert}&amp;apikey&#x3D;{YourApiKey} &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeadlessChromeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://v2018.api2pdf.com");
    
    // Configure API key authorization: QueryApiKey
    ApiKeyAuth QueryApiKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryApiKey");
    QueryApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryApiKey.setApiKeyPrefix("Token");

    HeadlessChromeApi apiInstance = new HeadlessChromeApi(defaultClient);
    String url = "url_example"; // String | Url of the page to convert to PDF. Must start with http:// or https://.
    String output = "output_example"; // String | Specify output=json to receive a JSON output. Defaults to PDF file.
    try {
      ApiResponseSuccess result = apiInstance.chromeFromUrlGET(url, output);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeadlessChromeApi#chromeFromUrlGET");
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
| **url** | **String**| Url of the page to convert to PDF. Must start with http:// or https://. | |
| **output** | **String**| Specify output&#x3D;json to receive a JSON output. Defaults to PDF file. | [optional] |

### Return type

[**ApiResponseSuccess**](ApiResponseSuccess.md)

### Authorization

[QueryApiKey](../README.md#QueryApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A PDF file or a JSON object depending on the &#x60;output&#x60; query parameter |  -  |
| **401** | Failed to generate PDF |  -  |

<a id="chromeFromUrlPost"></a>
# **chromeFromUrlPost**
> ApiResponseSuccess chromeFromUrlPost(chromeUrlToPdfRequest)

Convert URL to PDF

Convert a URL or Web Page to PDF using Headless Chrome on AWS Lambda.. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeadlessChromeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://v2018.api2pdf.com");
    
    // Configure API key authorization: HeaderApiKey
    ApiKeyAuth HeaderApiKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderApiKey");
    HeaderApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderApiKey.setApiKeyPrefix("Token");

    HeadlessChromeApi apiInstance = new HeadlessChromeApi(defaultClient);
    ChromeUrlToPdfRequest chromeUrlToPdfRequest = new ChromeUrlToPdfRequest(); // ChromeUrlToPdfRequest | A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - `url` *(string, required)* - Url to the web page to convert to PDF - `inlinePdf` *(boolean, optional)* - Open the PDF in a browser window. Default to false. - `fileName` *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - `options` *(object, optional)* - Include advanced Headless Chrome options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-headless-chrome/).
    try {
      ApiResponseSuccess result = apiInstance.chromeFromUrlPost(chromeUrlToPdfRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeadlessChromeApi#chromeFromUrlPost");
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
| **chromeUrlToPdfRequest** | [**ChromeUrlToPdfRequest**](ChromeUrlToPdfRequest.md)| A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;url&#x60; *(string, required)* - Url to the web page to convert to PDF - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - &#x60;options&#x60; *(object, optional)* - Include advanced Headless Chrome options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-headless-chrome/). | [optional] |

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

