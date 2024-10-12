# FilesApi

All URIs are relative to *https://connect.apptigent.com/api/utilities*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**convertImage**](FilesApi.md#convertImage) | **POST** /ConvertImage | Files - Convert Image |
| [**cropImage**](FilesApi.md#cropImage) | **POST** /CropImage | Files - Crop Image |
| [**fileToString**](FilesApi.md#fileToString) | **POST** /FileToString | Files - File to string |
| [**flipImage**](FilesApi.md#flipImage) | **POST** /FlipImage | Files - Flip Image |
| [**generateQRCode**](FilesApi.md#generateQRCode) | **POST** /GenerateQRCode | Files - Generate QR code |
| [**resizeImage**](FilesApi.md#resizeImage) | **POST** /ResizeImage | Files - Resize Image |
| [**rotateImage**](FilesApi.md#rotateImage) | **POST** /RotateImage | Files - Rotate Image |
| [**watermarkImage**](FilesApi.md#watermarkImage) | **POST** /WatermarkImage | Files - Watermark Image |


<a id="convertImage"></a>
# **convertImage**
> File convertImage(_file, format)

Files - Convert Image

Convert an image from one format to another

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.apptigent.com/api/utilities");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    File _file = new File("/path/to/file"); // File | Source image file
    String format = "PNG"; // String | Output file format
    try {
      File result = apiInstance.convertImage(_file, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#convertImage");
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
| **_file** | **File**| Source image file | |
| **format** | **String**| Output file format | [default to PNG] [enum: PNG, JPG, GIF, BMP, TIF] |

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/bmp, image/gif, image/jpeg, image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | ERROR |  -  |

<a id="cropImage"></a>
# **cropImage**
> File cropImage(height, width, _file, position)

Files - Crop Image

Crop an image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.apptigent.com/api/utilities");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    BigDecimal height = new BigDecimal(78); // BigDecimal | Height (Y-axis down, negative to reverse)
    BigDecimal width = new BigDecimal(78); // BigDecimal | Width (X-axis right, negative to reverse)
    File _file = new File("/path/to/file"); // File | Source image file
    String position = "TopLeft"; // String | Crop start position (use negative values to reverse crop area)
    try {
      File result = apiInstance.cropImage(height, width, _file, position);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#cropImage");
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
| **height** | **BigDecimal**| Height (Y-axis down, negative to reverse) | |
| **width** | **BigDecimal**| Width (X-axis right, negative to reverse) | |
| **_file** | **File**| Source image file | |
| **position** | **String**| Crop start position (use negative values to reverse crop area) | [default to TopLeft] [enum: TopLeft, TopCenter, TopRight, MiddleLeft, MiddleCenter, MiddleRight, BottomLeft, BottomCenter, BottomRight] |

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/bmp, image/gif, image/jpeg, image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | ERROR |  -  |

<a id="fileToString"></a>
# **fileToString**
> OutputString fileToString(_file)

Files - File to string

Convert a file to a Base64 string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.apptigent.com/api/utilities");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    File _file = new File("/path/to/file"); // File | Source file (10MB limit)
    try {
      OutputString result = apiInstance.fileToString(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileToString");
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
| **_file** | **File**| Source file (10MB limit) | |

### Return type

[**OutputString**](OutputString.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | ERROR |  -  |

<a id="flipImage"></a>
# **flipImage**
> File flipImage(_file, orientation)

Files - Flip Image

Flip an image (horizontal or vertical)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.apptigent.com/api/utilities");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    File _file = new File("/path/to/file"); // File | Source image file
    String orientation = "Horizontal"; // String | Horizontal or Vertical
    try {
      File result = apiInstance.flipImage(_file, orientation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#flipImage");
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
| **_file** | **File**| Source image file | |
| **orientation** | **String**| Horizontal or Vertical | [default to Horizontal] [enum: Horizontal, Vertical] |

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | ERROR |  -  |

<a id="generateQRCode"></a>
# **generateQRCode**
> File generateQRCode(inputQRCode)

Files - Generate QR code

Generate a QR code image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.apptigent.com/api/utilities");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    InputQRCode inputQRCode = new InputQRCode(); // InputQRCode | 
    try {
      File result = apiInstance.generateQRCode(inputQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#generateQRCode");
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
| **inputQRCode** | [**InputQRCode**](InputQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | ERROR |  -  |

<a id="resizeImage"></a>
# **resizeImage**
> File resizeImage(algorithm, _file, units, height, width)

Files - Resize Image

Resize an image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.apptigent.com/api/utilities");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String algorithm = "Bicubic (default)"; // String | Optimize output quality of the target image
    File _file = new File("/path/to/file"); // File | Source image file
    String units = "Pixels"; // String | Image adjustment units
    BigDecimal height = new BigDecimal(78); // BigDecimal | Image height (pixels or percent)
    BigDecimal width = new BigDecimal(78); // BigDecimal | Image width (pixels or percent)
    try {
      File result = apiInstance.resizeImage(algorithm, _file, units, height, width);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#resizeImage");
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
| **algorithm** | **String**| Optimize output quality of the target image | [default to Bicubic (default)] [enum: Bicubic (default), Bilinear, Cubic (Box), Cubic (Catmull-Rom), Cubic (Hermite), Cubic (Spline), Nearest Neighbor, Sinc (Lanczos2), Sinc (Lanczos3), Sinc (Lanczos5), Sinc (Lanczos8), Robidoux, Robidoux Sharp] |
| **_file** | **File**| Source image file | |
| **units** | **String**| Image adjustment units | [default to Pixels] [enum: Pixels, Percent] |
| **height** | **BigDecimal**| Image height (pixels or percent) | [optional] |
| **width** | **BigDecimal**| Image width (pixels or percent) | [optional] |

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: image/bmp, image/gif, image/jpeg, image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | ERROR |  -  |

<a id="rotateImage"></a>
# **rotateImage**
> File rotateImage(degrees, _file)

Files - Rotate Image

Rotate an image by specified number of degrees

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.apptigent.com/api/utilities");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String degrees = "degrees_example"; // String | Number of degrees
    File _file = new File("/path/to/file"); // File | Source image file
    try {
      File result = apiInstance.rotateImage(degrees, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#rotateImage");
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
| **degrees** | **String**| Number of degrees | |
| **_file** | **File**| Source image file | |

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | ERROR |  -  |

<a id="watermarkImage"></a>
# **watermarkImage**
> File watermarkImage(color, _file, font, horizontal, size, text, vertical)

Files - Watermark Image

Add watermark text to an image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.apptigent.com/api/utilities");
    
    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String color = "000000"; // String | Text color hex value
    File _file = new File("/path/to/file"); // File | Source image file
    String font = "Arial"; // String | Text font
    String horizontal = "Left"; // String | Horizontal alignment
    BigDecimal size = new BigDecimal(78); // BigDecimal | Font size (points)
    String text = "text_example"; // String | Watermark text
    String vertical = "Top"; // String | Vertical alignment
    try {
      File result = apiInstance.watermarkImage(color, _file, font, horizontal, size, text, vertical);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#watermarkImage");
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
| **color** | **String**| Text color hex value | [default to 000000] |
| **_file** | **File**| Source image file | |
| **font** | **String**| Text font | [default to Arial] [enum: Arial, Arial Black, Arial Narrow, Book Antiqua, Britannic Bold, Brush Script MT, Calisto MT, Century Gothic, Century Schoolbook, Colonna MT, Comic Sans MS, Cooper Black, Copperplate Gothic Bold, Copperplate Gothic Light, Courier New, Edwardian Script ITC, Engravers MT, Franklin Gothic Demi, Franklin Gothic Heavy, Franklin Gothic Medium, Garamond, Georgia, Gill Sans MT, Gill Sans MT Condensed, Gill Sans Ultra Bold, Gill Sans Ultra Bold Condensed, Goudy Old Style, Haettenschweiler, Holidays MT, Impact, Lucida Calligraphy, Lucida Console, Lucida Handwriting, Lucida Sans Typewriter, Lucida Sans Unicode, Marlett, Microsoft Sans Serif, MS Outlook, Palace Script MT, Palatino Linotype, Papyrus, Playbill, Rockwell, Rockwell Condensed, Rockwell Extra Bold, Script MT Bold, Stencil, Symbol, Tahoma, Times New Roman, Trebuchet MS, Verdana, Vivaldi, Webdings, Wingdings 1, Wingdings 2, Wingdings 3] |
| **horizontal** | **String**| Horizontal alignment | [default to Center] [enum: Left, Center, Right] |
| **size** | **BigDecimal**| Font size (points) | |
| **text** | **String**| Watermark text | |
| **vertical** | **String**| Vertical alignment | [default to Center] [enum: Top, Center, Bottom] |

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | ERROR |  -  |

