# LibreOfficeApi

All URIs are relative to *https://v2018.api2pdf.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**libreConvertPost**](LibreOfficeApi.md#libreConvertPost) | **POST** /libreoffice/convert | Convert office document or image to PDF |


<a id="libreConvertPost"></a>
# **libreConvertPost**
> ApiResponseSuccess libreConvertPost(libreOfficeConvertRequest)

Convert office document or image to PDF

Convert an office document (Word, Excel, Powerpoint) or an image (jpg, gif, png) to a PDF using LibreOffice on AWS Lambda. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LibreOfficeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://v2018.api2pdf.com");
    
    // Configure API key authorization: HeaderApiKey
    ApiKeyAuth HeaderApiKey = (ApiKeyAuth) defaultClient.getAuthentication("HeaderApiKey");
    HeaderApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //HeaderApiKey.setApiKeyPrefix("Token");

    LibreOfficeApi apiInstance = new LibreOfficeApi(defaultClient);
    LibreOfficeConvertRequest libreOfficeConvertRequest = new LibreOfficeConvertRequest(); // LibreOfficeConvertRequest | A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - `url` *(string, required)* - A direct URL to the file. Api2Pdf will consume the file at that URL and then convert it. - `inlinePdf` *(boolean, optional)* - Open the PDF in a browser window. Default to false. - `fileName` *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. 
    try {
      ApiResponseSuccess result = apiInstance.libreConvertPost(libreOfficeConvertRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LibreOfficeApi#libreConvertPost");
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
| **libreOfficeConvertRequest** | [**LibreOfficeConvertRequest**](LibreOfficeConvertRequest.md)| A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;url&#x60; *(string, required)* - A direct URL to the file. Api2Pdf will consume the file at that URL and then convert it. - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified.  | [optional] |

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

