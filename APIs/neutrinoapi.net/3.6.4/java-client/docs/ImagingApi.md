# ImagingApi

All URIs are relative to *https://neutrinoapi.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hTMLRender**](ImagingApi.md#hTMLRender) | **POST** /html-render | HTML Render |
| [**imageResize**](ImagingApi.md#imageResize) | **POST** /image-resize | Image Resize |
| [**imageWatermark**](ImagingApi.md#imageWatermark) | **POST** /image-watermark | Image Watermark |
| [**qRCode**](ImagingApi.md#qRCode) | **POST** /qr-code | QR Code |


<a id="hTMLRender"></a>
# **hTMLRender**
> File hTMLRender(content, css, delay, footer, format, grayscale, header, ignoreCertificateErrors, imageHeight, imageWidth, landscape, margin, marginBottom, marginLeft, marginRight, marginTop, pageHeight, pageSize, pageWidth, timeout, title, zoom)

HTML Render

Render HTML content to PDF, JPG or PNG

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    ImagingApi apiInstance = new ImagingApi(defaultClient);
    String content = "content_example"; // String | The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string
    String css = "css_example"; // String | Inject custom CSS into the HTML. e.g. 'body { background-color: red;}'
    Integer delay = 0; // Integer | Number of seconds to wait before rendering the page (can be useful for pages with animations etc)
    String footer = "footer_example"; // String | The footer HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages}
    String format = "PDF"; // String | Which format to output, available options are: PDF, PNG, JPG
    Boolean grayscale = false; // Boolean | Render the final document in grayscale
    String header = "header_example"; // String | The header HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages}
    Boolean ignoreCertificateErrors = false; // Boolean | Ignore any TLS/SSL certificate errors
    Integer imageHeight = 56; // Integer | If rendering to an image format (PNG or JPG) use this image height (in pixels). The default is automatic which dynamically sets the image height based on the content
    Integer imageWidth = 1024; // Integer | If rendering to an image format (PNG or JPG) use this image width (in pixels)
    Boolean landscape = false; // Boolean | Set the document to landscape orientation
    Double margin = 0D; // Double | The document margin (in mm)
    Double marginBottom = 0D; // Double | The document bottom margin (in mm)
    Double marginLeft = 0D; // Double | The document left margin (in mm)
    Double marginRight = 0D; // Double | The document right margin (in mm)
    Double marginTop = 0D; // Double | The document top margin (in mm)
    Double pageHeight = 3.4D; // Double | Set the PDF page height explicitly (in mm)
    String pageSize = "A4"; // String | Set the document page size, can be one of: A0 - A9, B0 - B10, Comm10E, DLE or Letter
    Double pageWidth = 3.4D; // Double | Set the PDF page width explicitly (in mm)
    Integer timeout = 300; // Integer | Timeout in seconds. Give up if still trying to load the HTML content after this number of seconds
    String title = "title_example"; // String | The document title
    Double zoom = 1D; // Double | Set the zoom factor when rendering the page (2.0 for double size, 0.5 for half size)
    try {
      File result = apiInstance.hTMLRender(content, css, delay, footer, format, grayscale, header, ignoreCertificateErrors, imageHeight, imageWidth, landscape, margin, marginBottom, marginLeft, marginRight, marginTop, pageHeight, pageSize, pageWidth, timeout, title, zoom);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagingApi#hTMLRender");
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
| **content** | **String**| The HTML content. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string | |
| **css** | **String**| Inject custom CSS into the HTML. e.g. &#39;body { background-color: red;}&#39; | [optional] |
| **delay** | **Integer**| Number of seconds to wait before rendering the page (can be useful for pages with animations etc) | [optional] [default to 0] |
| **footer** | **String**| The footer HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages} | [optional] |
| **format** | **String**| Which format to output, available options are: PDF, PNG, JPG | [optional] [default to PDF] |
| **grayscale** | **Boolean**| Render the final document in grayscale | [optional] [default to false] |
| **header** | **String**| The header HTML to insert into each page. The following dynamic tags are supported: {date}, {title}, {url}, {pageNumber}, {totalPages} | [optional] |
| **ignoreCertificateErrors** | **Boolean**| Ignore any TLS/SSL certificate errors | [optional] [default to false] |
| **imageHeight** | **Integer**| If rendering to an image format (PNG or JPG) use this image height (in pixels). The default is automatic which dynamically sets the image height based on the content | [optional] |
| **imageWidth** | **Integer**| If rendering to an image format (PNG or JPG) use this image width (in pixels) | [optional] [default to 1024] |
| **landscape** | **Boolean**| Set the document to landscape orientation | [optional] [default to false] |
| **margin** | **Double**| The document margin (in mm) | [optional] [default to 0] |
| **marginBottom** | **Double**| The document bottom margin (in mm) | [optional] [default to 0] |
| **marginLeft** | **Double**| The document left margin (in mm) | [optional] [default to 0] |
| **marginRight** | **Double**| The document right margin (in mm) | [optional] [default to 0] |
| **marginTop** | **Double**| The document top margin (in mm) | [optional] [default to 0] |
| **pageHeight** | **Double**| Set the PDF page height explicitly (in mm) | [optional] |
| **pageSize** | **String**| Set the document page size, can be one of: A0 - A9, B0 - B10, Comm10E, DLE or Letter | [optional] [default to A4] |
| **pageWidth** | **Double**| Set the PDF page width explicitly (in mm) | [optional] |
| **timeout** | **Integer**| Timeout in seconds. Give up if still trying to load the HTML content after this number of seconds | [optional] [default to 300] |
| **title** | **String**| The document title | [optional] |
| **zoom** | **Double**| Set the zoom factor when rendering the page (2.0 for double size, 0.5 for half size) | [optional] [default to 1] |

### Return type

[**File**](File.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="imageResize"></a>
# **imageResize**
> File imageResize(imageUrl, width, bgColor, format, height, resizeMode)

Image Resize

Resize an image and output as either JPEG or PNG

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    ImagingApi apiInstance = new ImagingApi(defaultClient);
    String imageUrl = "imageUrl_example"; // String | The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data
    Integer width = 56; // Integer | The width to resize to (in px)
    String bgColor = "transparent"; // String | The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of 'transparent' can also be used. For JPG output the default is black (#000000)
    String format = "png"; // String | The output image format, can be either png or jpg
    Integer height = 56; // Integer | The height to resize to (in px). If you don't set this field then the height will be automatic based on the requested width and image aspect ratio
    String resizeMode = "scale"; // String | The resize mode to use, we support 3 main resizing modes: <ul> <li><b>scale</b><br>Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio</li> <li><b>pad</b><br>Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the 'bg-color' value</li> <li><b>crop</b><br>Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image</li> </ul>
    try {
      File result = apiInstance.imageResize(imageUrl, width, bgColor, format, height, resizeMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagingApi#imageResize");
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
| **imageUrl** | **String**| The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data | |
| **width** | **Integer**| The width to resize to (in px) | |
| **bgColor** | **String**| The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of &#39;transparent&#39; can also be used. For JPG output the default is black (#000000) | [optional] [default to transparent] |
| **format** | **String**| The output image format, can be either png or jpg | [optional] [default to png] |
| **height** | **Integer**| The height to resize to (in px). If you don&#39;t set this field then the height will be automatic based on the requested width and image aspect ratio | [optional] |
| **resizeMode** | **String**| The resize mode to use, we support 3 main resizing modes: &lt;ul&gt; &lt;li&gt;&lt;b&gt;scale&lt;/b&gt;&lt;br&gt;Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio&lt;/li&gt; &lt;li&gt;&lt;b&gt;pad&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the &#39;bg-color&#39; value&lt;/li&gt; &lt;li&gt;&lt;b&gt;crop&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image&lt;/li&gt; &lt;/ul&gt; | [optional] [default to scale] |

### Return type

[**File**](File.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="imageWatermark"></a>
# **imageWatermark**
> File imageWatermark(imageUrl, watermarkUrl, bgColor, format, height, opacity, position, resizeMode, width)

Image Watermark

Watermark one image with another image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    ImagingApi apiInstance = new ImagingApi(defaultClient);
    String imageUrl = "imageUrl_example"; // String | The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data
    String watermarkUrl = "watermarkUrl_example"; // String | The URL or Base64 encoded Data URL for the watermark image. You can also upload an image file directly using multipart/form-data
    String bgColor = "transparent"; // String | The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of 'transparent' can also be used. For JPG output the default is black (#000000)
    String format = "png"; // String | The output image format, can be either png or jpg
    Integer height = 56; // Integer | If set resize the resulting image to this height (in px)
    Integer opacity = 50; // Integer | The opacity of the watermark (0 to 100)
    String position = "center"; // String | The position of the watermark image, possible values are: <br>center, top-left, top-center, top-right, bottom-left, bottom-center, bottom-right
    String resizeMode = "scale"; // String | The resize mode to use, we support 3 main resizing modes: <ul> <li><b>scale</b><br>Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio</li> <li><b>pad</b><br>Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the 'bg-color' value</li> <li><b>crop</b><br>Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image</li> </ul>
    Integer width = 56; // Integer | If set resize the resulting image to this width (in px)
    try {
      File result = apiInstance.imageWatermark(imageUrl, watermarkUrl, bgColor, format, height, opacity, position, resizeMode, width);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagingApi#imageWatermark");
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
| **imageUrl** | **String**| The URL or Base64 encoded Data URL for the source image. You can also upload an image file directly using multipart/form-data | |
| **watermarkUrl** | **String**| The URL or Base64 encoded Data URL for the watermark image. You can also upload an image file directly using multipart/form-data | |
| **bgColor** | **String**| The image background color in hexadecimal notation (e.g. #0000ff). For PNG output the special value of &#39;transparent&#39; can also be used. For JPG output the default is black (#000000) | [optional] [default to transparent] |
| **format** | **String**| The output image format, can be either png or jpg | [optional] [default to png] |
| **height** | **Integer**| If set resize the resulting image to this height (in px) | [optional] |
| **opacity** | **Integer**| The opacity of the watermark (0 to 100) | [optional] [default to 50] |
| **position** | **String**| The position of the watermark image, possible values are: &lt;br&gt;center, top-left, top-center, top-right, bottom-left, bottom-center, bottom-right | [optional] [default to center] |
| **resizeMode** | **String**| The resize mode to use, we support 3 main resizing modes: &lt;ul&gt; &lt;li&gt;&lt;b&gt;scale&lt;/b&gt;&lt;br&gt;Resize to within the width and height specified while preserving aspect ratio. In this mode the width or height will be automatically adjusted to fit the aspect ratio&lt;/li&gt; &lt;li&gt;&lt;b&gt;pad&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and pad any space left over. Any padded space will be filled in with the &#39;bg-color&#39; value&lt;/li&gt; &lt;li&gt;&lt;b&gt;crop&lt;/b&gt;&lt;br&gt;Resize to exactly the width and height specified while preserving aspect ratio and crop any space which fall outside the area. The cropping window is centered on the original image&lt;/li&gt; &lt;/ul&gt; | [optional] [default to scale] |
| **width** | **Integer**| If set resize the resulting image to this width (in px) | [optional] |

### Return type

[**File**](File.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="qRCode"></a>
# **qRCode**
> File qRCode(content, bgColor, fgColor, height, width)

QR Code

Generate a QR code as a PNG image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    ImagingApi apiInstance = new ImagingApi(defaultClient);
    String content = "content_example"; // String | The content to encode into the QR code (e.g. a URL or a phone number)
    String bgColor = "#ffffff"; // String | The QR code background color
    String fgColor = "#000000"; // String | The QR code foreground color
    Integer height = 256; // Integer | The height of the QR code (in px)
    Integer width = 256; // Integer | The width of the QR code (in px)
    try {
      File result = apiInstance.qRCode(content, bgColor, fgColor, height, width);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagingApi#qRCode");
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
| **content** | **String**| The content to encode into the QR code (e.g. a URL or a phone number) | |
| **bgColor** | **String**| The QR code background color | [optional] [default to #ffffff] |
| **fgColor** | **String**| The QR code foreground color | [optional] [default to #000000] |
| **height** | **Integer**| The height of the QR code (in px) | [optional] [default to 256] |
| **width** | **Integer**| The width of the QR code (in px) | [optional] [default to 256] |

### Return type

[**File**](File.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

