# PdfApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPdfGet**](PdfApi.md#apiPdfGet) | **GET** /api/pdf | Basic method to verify api is up and running |
| [**apiPdfPdfconcatPost**](PdfApi.md#apiPdfPdfconcatPost) | **POST** /api/pdf/pdfconcat | Concatenate multiple pdf files into single pdf file.. |
| [**apiPdfPdftoimagePost**](PdfApi.md#apiPdfPdftoimagePost) | **POST** /api/pdf/pdftoimage | Generate an image of to provided pdf file |
| [**apiPdfPdfwritestringPost**](PdfApi.md#apiPdfPdfwritestringPost) | **POST** /api/pdf/pdfwritestring | Write text on a page in a pdf document. |
| [**apiPdfWkhtmltopdfPost**](PdfApi.md#apiPdfWkhtmltopdfPost) | **POST** /api/pdf/wkhtmltopdf | Generate pdf file from url using the excellent tool wkhtmltopdf. |
| [**apiPdfXslfoPost**](PdfApi.md#apiPdfXslfoPost) | **POST** /api/pdf/xslfo | Create pdf-file from complete XSL-FO document. |
| [**apiPdfXslfowithtransformPost**](PdfApi.md#apiPdfXslfowithtransformPost) | **POST** /api/pdf/xslfowithtransform | Create pdf-file from transforming xml document with Xsl-Fo transform document. |


<a id="apiPdfGet"></a>
# **apiPdfGet**
> apiPdfGet()

Basic method to verify api is up and running

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PdfApi apiInstance = new PdfApi(defaultClient);
    try {
      apiInstance.apiPdfGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfApi#apiPdfGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | If any error occurs parsing input |  -  |
| **415** | If content-type of request is not set to multipart/form-data or application/json |  -  |
| **429** | If you reach the monthly request limit for your subscription plan |  -  |

<a id="apiPdfPdfconcatPost"></a>
# **apiPdfPdfconcatPost**
> PdfResponseDto apiPdfPdfconcatPost(pdfConcatenationRequestDto)

Concatenate multiple pdf files into single pdf file..

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PdfApi apiInstance = new PdfApi(defaultClient);
    PdfConcatenationRequestDto pdfConcatenationRequestDto = new PdfConcatenationRequestDto(); // PdfConcatenationRequestDto | PdfConcat Request. Add two or more pdf files and concatenate pages into single pdf document.
    try {
      PdfResponseDto result = apiInstance.apiPdfPdfconcatPost(pdfConcatenationRequestDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfApi#apiPdfPdfconcatPost");
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
| **pdfConcatenationRequestDto** | [**PdfConcatenationRequestDto**](PdfConcatenationRequestDto.md)| PdfConcat Request. Add two or more pdf files and concatenate pages into single pdf document. | [optional] |

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the newly created pdf file. Either the file directly or serialized as Json if Accept-header is set to application/json |  -  |
| **400** | If any error occurs parsing input |  -  |
| **415** | If content-type of request is not set to multipart/form-data or application/json |  -  |
| **429** | If you reach the monthly request limit for your subscription plan |  -  |

<a id="apiPdfPdftoimagePost"></a>
# **apiPdfPdftoimagePost**
> ImageResponseDto apiPdfPdftoimagePost(pdfToImageRequestDto)

Generate an image of to provided pdf file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PdfApi apiInstance = new PdfApi(defaultClient);
    PdfToImageRequestDto pdfToImageRequestDto = new PdfToImageRequestDto(); // PdfToImageRequestDto | PdfToImage Request. Create an image of a page in an existing pdf document.
    try {
      ImageResponseDto result = apiInstance.apiPdfPdftoimagePost(pdfToImageRequestDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfApi#apiPdfPdftoimagePost");
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
| **pdfToImageRequestDto** | [**PdfToImageRequestDto**](PdfToImageRequestDto.md)| PdfToImage Request. Create an image of a page in an existing pdf document. | [optional] |

### Return type

[**ImageResponseDto**](ImageResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, image/gif, image/jpeg, image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generate an image of the provided pdf file. Either the image file directly or serialized as Json if Accept-header is set to application/json |  -  |
| **400** | If any error occurs parsing input |  -  |
| **415** | If content-type of request is not set to multipart/form-data or application/json |  -  |
| **429** | If you reach the monthly request limit for your subscription plan |  -  |

<a id="apiPdfPdfwritestringPost"></a>
# **apiPdfPdfwritestringPost**
> PdfResponseDto apiPdfPdfwritestringPost(pdfWriteStringRequestDto)

Write text on a page in a pdf document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PdfApi apiInstance = new PdfApi(defaultClient);
    PdfWriteStringRequestDto pdfWriteStringRequestDto = new PdfWriteStringRequestDto(); // PdfWriteStringRequestDto | PdfWriteString Request. Write string on page in pdf document
    try {
      PdfResponseDto result = apiInstance.apiPdfPdfwritestringPost(pdfWriteStringRequestDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfApi#apiPdfPdfwritestringPost");
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
| **pdfWriteStringRequestDto** | [**PdfWriteStringRequestDto**](PdfWriteStringRequestDto.md)| PdfWriteString Request. Write string on page in pdf document | [optional] |

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the newly created pdf file. Either the file directly or serialized as Json if Accept-header is set to application/json |  -  |
| **400** | If any error occurs parsing input |  -  |
| **415** | If content-type of request is not set to multipart/form-data or application/json |  -  |
| **429** | If you reach the monthly request limit for your subscription plan |  -  |

<a id="apiPdfWkhtmltopdfPost"></a>
# **apiPdfWkhtmltopdfPost**
> PdfResponseDto apiPdfWkhtmltopdfPost(wkHtmlToPdfRequestDto)

Generate pdf file from url using the excellent tool wkhtmltopdf.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PdfApi apiInstance = new PdfApi(defaultClient);
    WkHtmlToPdfRequestDto wkHtmlToPdfRequestDto = new WkHtmlToPdfRequestDto(); // WkHtmlToPdfRequestDto | WkHtmlToPdf Request. Generate pdf from html, either from url or base64 encoded html string
    try {
      PdfResponseDto result = apiInstance.apiPdfWkhtmltopdfPost(wkHtmlToPdfRequestDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfApi#apiPdfWkhtmltopdfPost");
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
| **wkHtmlToPdfRequestDto** | [**WkHtmlToPdfRequestDto**](WkHtmlToPdfRequestDto.md)| WkHtmlToPdf Request. Generate pdf from html, either from url or base64 encoded html string | [optional] |

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the newly created pdf file. Either the file directly or serialized as Json if Accept-header is set to application/json |  -  |
| **400** | If any error occurs executing request |  -  |
| **415** | If content-type of request is not set to application/json |  -  |
| **429** | If you reach the monthly request limit for your subscription plan |  -  |

<a id="apiPdfXslfoPost"></a>
# **apiPdfXslfoPost**
> PdfResponseDto apiPdfXslfoPost(foRequestDto)

Create pdf-file from complete XSL-FO document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PdfApi apiInstance = new PdfApi(defaultClient);
    FoRequestDto foRequestDto = new FoRequestDto(); // FoRequestDto | XSL-FO Request, the basic XSL-FO request. Post your XSL-FO document and digital resources, either as 'multipart/form-data' or 'application/json'
    try {
      PdfResponseDto result = apiInstance.apiPdfXslfoPost(foRequestDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfApi#apiPdfXslfoPost");
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
| **foRequestDto** | [**FoRequestDto**](FoRequestDto.md)| XSL-FO Request, the basic XSL-FO request. Post your XSL-FO document and digital resources, either as &#39;multipart/form-data&#39; or &#39;application/json&#39; | [optional] |

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the newly created pdf file. Either the file directly or serialized as Json if Accept-header is set to application/json |  -  |
| **400** | If any error occurs parsing input |  -  |
| **415** | If content-type of request is not set to multipart/form-data or application/json |  -  |
| **429** | If you reach the monthly request limit for your subscription plan |  -  |

<a id="apiPdfXslfowithtransformPost"></a>
# **apiPdfXslfowithtransformPost**
> PdfResponseDto apiPdfXslfowithtransformPost(foTransformRequestDto)

Create pdf-file from transforming xml document with Xsl-Fo transform document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PdfApi apiInstance = new PdfApi(defaultClient);
    FoTransformRequestDto foTransformRequestDto = new FoTransformRequestDto(); // FoTransformRequestDto | XSL-FO Transform Request. The XSL-FO is transformed on the supplied xml data document. Post your XSL-FO transform document and xml data document aloing with your digital resources, either as 'multipart/form-data' or 'application/json'
    try {
      PdfResponseDto result = apiInstance.apiPdfXslfowithtransformPost(foTransformRequestDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PdfApi#apiPdfXslfowithtransformPost");
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
| **foTransformRequestDto** | [**FoTransformRequestDto**](FoTransformRequestDto.md)| XSL-FO Transform Request. The XSL-FO is transformed on the supplied xml data document. Post your XSL-FO transform document and xml data document aloing with your digital resources, either as &#39;multipart/form-data&#39; or &#39;application/json&#39; | [optional] |

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the newly created pdf file. Either the file directly or serialized as Json if Accept-header is set to application/json |  -  |
| **400** | If any error occurs parsing input |  -  |
| **415** | If content-type of request is not set to multipart/form-data or application/json |  -  |
| **429** | If you reach the monthly request limit for your subscription plan |  -  |

