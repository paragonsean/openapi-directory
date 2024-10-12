# DefaultApi

All URIs are relative to *https://azure.local/vision/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyzeImage**](DefaultApi.md#analyzeImage) | **POST** /analyze |  |
| [**analyzeImageByDomain**](DefaultApi.md#analyzeImageByDomain) | **POST** /models/{model}/analyze |  |
| [**describeImage**](DefaultApi.md#describeImage) | **POST** /describe |  |
| [**generateThumbnail**](DefaultApi.md#generateThumbnail) | **POST** /generateThumbnail |  |
| [**getTextOperationResult**](DefaultApi.md#getTextOperationResult) | **GET** /textOperations/{operationId} |  |
| [**listModels**](DefaultApi.md#listModels) | **GET** /models |  |
| [**recognizePrintedText**](DefaultApi.md#recognizePrintedText) | **POST** /ocr |  |
| [**recognizeText**](DefaultApi.md#recognizeText) | **POST** /recognizeText |  |
| [**tagImage**](DefaultApi.md#tagImage) | **POST** /tag |  |


<a id="analyzeImage"></a>
# **analyzeImage**
> ImageAnalysis analyzeImage(imageUrl, visualFeatures, details, language)



This operation extracts a rich set of visual features based on the image content. Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  Within your request, there is an optional parameter to allow you to choose which features to return.  By default, image categories are returned in the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/vision/v1.0");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    AnalyzeImageRequest imageUrl = new AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
    List<String> visualFeatures = Arrays.asList(); // List<String> | A string indicating what visual feature types to return. Multiple values should be comma-separated. Valid visual feature types include:Categories - categorizes image content according to a taxonomy defined in documentation. Tags - tags the image with a detailed list of words related to the image content. Description - describes the image content with a complete English sentence. Faces - detects if faces are present. If present, generate coordinates, gender and age. ImageType - detects if image is clipart or a line drawing. Color - determines the accent color, dominant color, and whether an image is black&white.Adult - detects if the image is pornographic in nature (depicts nudity or a sex act).  Sexually suggestive content is also detected.
    List<String> details = Arrays.asList(); // List<String> | A string indicating which domain-specific details to return. Multiple values should be comma-separated. Valid visual feature types include:Celebrities - identifies celebrities if detected in the image.
    String language = "en"; // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    try {
      ImageAnalysis result = apiInstance.analyzeImage(imageUrl, visualFeatures, details, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyzeImage");
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
| **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **visualFeatures** | [**List&lt;String&gt;**](String.md)| A string indicating what visual feature types to return. Multiple values should be comma-separated. Valid visual feature types include:Categories - categorizes image content according to a taxonomy defined in documentation. Tags - tags the image with a detailed list of words related to the image content. Description - describes the image content with a complete English sentence. Faces - detects if faces are present. If present, generate coordinates, gender and age. ImageType - detects if image is clipart or a line drawing. Color - determines the accent color, dominant color, and whether an image is black&amp;white.Adult - detects if the image is pornographic in nature (depicts nudity or a sex act).  Sexually suggestive content is also detected. | [optional] [enum: ImageType, Faces, Adult, Categories, Color, Tags, Description] |
| **details** | [**List&lt;String&gt;**](String.md)| A string indicating which domain-specific details to return. Multiple values should be comma-separated. Valid visual feature types include:Celebrities - identifies celebrities if detected in the image. | [optional] [enum: Celebrities, Landmarks] |
| **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to en] [enum: en, es, ja, pt, zh] |

### Return type

[**ImageAnalysis**](ImageAnalysis.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response include the extracted features in JSON format.Here is the definitions for enumeration typesClipartTypeNon-clipart &#x3D; 0,  ambiguous &#x3D; 1, normal-clipart &#x3D; 2, good-clipart &#x3D; 3.LineDrawingTypeNon-LineDrawing &#x3D; 0,LineDrawing &#x3D; 1. |  -  |
| **0** | Error response. |  -  |

<a id="analyzeImageByDomain"></a>
# **analyzeImageByDomain**
> DomainModelResults analyzeImageByDomain(model, imageUrl, language)



This operation recognizes content within an image by applying a domain-specific model.  The list of domain-specific models that are supported by the Computer Vision API can be retrieved using the /models GET request.  Currently, the API only provides a single domain-specific model: celebrities. Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL. A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/vision/v1.0");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String model = "model_example"; // String | The domain-specific content to recognize.
    AnalyzeImageRequest imageUrl = new AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
    String language = "en"; // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    try {
      DomainModelResults result = apiInstance.analyzeImageByDomain(model, imageUrl, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyzeImageByDomain");
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
| **model** | **String**| The domain-specific content to recognize. | |
| **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to en] [enum: en, es, ja, pt, zh] |

### Return type

[**DomainModelResults**](DomainModelResults.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Analysis result based on the domain model |  -  |
| **0** | Error response. |  -  |

<a id="describeImage"></a>
# **describeImage**
> ImageDescription describeImage(imageUrl, maxCandidates, language)



This operation generates a description of an image in human readable language with complete sentences.  The description is based on a collection of content tags, which are also returned by the operation. More than one description can be generated for each image.  Descriptions are ordered by their confidence score. All descriptions are in English. Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/vision/v1.0");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    AnalyzeImageRequest imageUrl = new AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
    String maxCandidates = "1"; // String | Maximum number of candidate descriptions to be returned.  The default is 1.
    String language = "en"; // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    try {
      ImageDescription result = apiInstance.describeImage(imageUrl, maxCandidates, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeImage");
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
| **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **maxCandidates** | **String**| Maximum number of candidate descriptions to be returned.  The default is 1. | [optional] [default to 1] |
| **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to en] [enum: en, es, ja, pt, zh] |

### Return type

[**ImageDescription**](ImageDescription.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image description object. |  -  |
| **0** | Error response. |  -  |

<a id="generateThumbnail"></a>
# **generateThumbnail**
> File generateThumbnail(width, height, imageUrl, smartCropping)



This operation generates a thumbnail image with the user-specified width and height. By default, the service analyzes the image, identifies the region of interest (ROI), and generates smart cropping coordinates based on the ROI. Smart cropping helps when you specify an aspect ratio that differs from that of the input image. A successful response contains the thumbnail image binary. If the request failed, the response contains an error code and a message to help determine what went wrong.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/vision/v1.0");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer width = 56; // Integer | Width of the thumbnail. It must be between 1 and 1024. Recommended minimum of 50.
    Integer height = 56; // Integer | Height of the thumbnail. It must be between 1 and 1024. Recommended minimum of 50.
    AnalyzeImageRequest imageUrl = new AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
    Boolean smartCropping = false; // Boolean | Boolean flag for enabling smart cropping.
    try {
      File result = apiInstance.generateThumbnail(width, height, imageUrl, smartCropping);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#generateThumbnail");
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
| **width** | **Integer**| Width of the thumbnail. It must be between 1 and 1024. Recommended minimum of 50. | |
| **height** | **Integer**| Height of the thumbnail. It must be between 1 and 1024. Recommended minimum of 50. | |
| **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **smartCropping** | **Boolean**| Boolean flag for enabling smart cropping. | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The generated thumbnail in binary format. |  -  |
| **0** | Error response. |  -  |

<a id="getTextOperationResult"></a>
# **getTextOperationResult**
> TextOperationResult getTextOperationResult(operationId)



This interface is used for getting text operation result. The URL to this interface should be retrieved from &#39;Operation-Location&#39; field returned from Recognize Text interface.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/vision/v1.0");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operationId = "operationId_example"; // String | Id of the text operation returned in the response of the 'Recognize Handwritten Text'
    try {
      TextOperationResult result = apiInstance.getTextOperationResult(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTextOperationResult");
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
| **operationId** | **String**| Id of the text operation returned in the response of the &#39;Recognize Handwritten Text&#39; | |

### Return type

[**TextOperationResult**](TextOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the operation status. |  -  |
| **0** | Error response. |  -  |

<a id="listModels"></a>
# **listModels**
> ListModelsResult listModels()



This operation returns the list of domain-specific models that are supported by the Computer Vision API.  Currently, the API only supports one domain-specific model: a celebrity recognizer. A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/vision/v1.0");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      ListModelsResult result = apiInstance.listModels();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listModels");
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

[**ListModelsResult**](ListModelsResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of available domain models. |  -  |
| **0** | Error response. |  -  |

<a id="recognizePrintedText"></a>
# **recognizePrintedText**
> OcrResult recognizePrintedText(detectOrientation, imageUrl, language)



Optical Character Recognition (OCR) detects printed text in an image and extracts the recognized characters into a machine-usable character stream.   Upon success, the OCR results will be returned. Upon failure, the error code together with an error message will be returned. The error code can be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, NotSupportedImage,  NotSupportedLanguage, or InternalServerError.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/vision/v1.0");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean detectOrientation = true; // Boolean | Whether detect the text orientation in the image. With detectOrientation=true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it's upside-down). 
    AnalyzeImageRequest imageUrl = new AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
    String language = "unk"; // String | The BCP-47 language code of the text to be detected in the image. The default value is 'unk'
    try {
      OcrResult result = apiInstance.recognizePrintedText(detectOrientation, imageUrl, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#recognizePrintedText");
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
| **detectOrientation** | **Boolean**| Whether detect the text orientation in the image. With detectOrientation&#x3D;true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it&#39;s upside-down).  | [default to true] |
| **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **language** | **String**| The BCP-47 language code of the text to be detected in the image. The default value is &#39;unk&#39; | [optional] [default to unk] [enum: unk, zh-Hans, zh-Hant, cs, da, nl, en, fi, fr, de, el, hu, it, ja, ko, nb, pl, pt, ru, es, sv, tr, ar, ro, sr-Cyrl, sr-Latn, sk] |

### Return type

[**OcrResult**](OcrResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The OCR results in the hierarchy of region/line/word. The results include text, bounding box for regions, lines and words.textAngleThe angle, in degrees, of the detected text with respect to the closest horizontal or vertical direction. After rotating the input image clockwise by this angle, the recognized text lines become horizontal or vertical. In combination with the orientation property it can be used to overlay recognition results correctly on the original image, by rotating either the original image or recognition results by a suitable angle around the center of the original image. If the angle cannot be confidently detected, this property is not present. If the image contains text at different angles, only part of the text will be recognized correctly. |  -  |
| **0** | Error response. |  -  |

<a id="recognizeText"></a>
# **recognizeText**
> recognizeText(imageUrl, detectHandwriting)



Recognize Text operation. When you use the Recognize Text interface, the response contains a field called &#39;Operation-Location&#39;. The &#39;Operation-Location&#39; field contains the URL that you must use for your Get Handwritten Text Operation Result operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/vision/v1.0");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    AnalyzeImageRequest imageUrl = new AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
    Boolean detectHandwriting = false; // Boolean | If 'true' is specified, handwriting recognition is performed. If this parameter is set to 'false' or is not specified, printed text recognition is performed.
    try {
      apiInstance.recognizeText(imageUrl, detectHandwriting);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#recognizeText");
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
| **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **detectHandwriting** | **Boolean**| If &#39;true&#39; is specified, handwriting recognition is performed. If this parameter is set to &#39;false&#39; or is not specified, printed text recognition is performed. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The service has accepted the request and will start processing later. It will return Accepted immediately and include an Operation-Location header. Client side should further query the operation status using the URL specified in this header. The operation ID will expire in 48 hours. |  * Operation-Location - URL to query for status of the operation. The operation ID will expire in 48 hours.  <br>  |
| **0** | Error response. |  -  |

<a id="tagImage"></a>
# **tagImage**
> TagResult tagImage(imageUrl, language)



This operation generates a list of words, or tags, that are relevant to the content of the supplied image. The Computer Vision API can return tags based on objects, living beings, scenery or actions found in images. Unlike categories, tags are not organized according to a hierarchical classification system, but correspond to image content. Tags may contain hints to avoid ambiguity or provide context, for example the tag &#39;cello&#39; may be accompanied by the hint &#39;musical instrument&#39;. All tags are in English.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local/vision/v1.0");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    AnalyzeImageRequest imageUrl = new AnalyzeImageRequest(); // AnalyzeImageRequest | A JSON document with a URL pointing to the image that is to be analyzed.
    String language = "en"; // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    try {
      TagResult result = apiInstance.tagImage(imageUrl, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagImage");
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
| **imageUrl** | [**AnalyzeImageRequest**](AnalyzeImageRequest.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to en] [enum: en, es, ja, pt, zh] |

### Return type

[**TagResult**](TagResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image tags object. |  -  |
| **0** | Error response. |  -  |

