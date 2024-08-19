# DefaultApi

All URIs are relative to *https://westcentralus.api.cognitive.microsoft.com/vision/v2.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyzeImage**](DefaultApi.md#analyzeImage) | **POST** /analyze |  |
| [**analyzeImageByDomain**](DefaultApi.md#analyzeImageByDomain) | **POST** /models/{model}/analyze |  |
| [**describeImage**](DefaultApi.md#describeImage) | **POST** /describe |  |
| [**detectObjects**](DefaultApi.md#detectObjects) | **POST** /detect |  |
| [**generateThumbnail**](DefaultApi.md#generateThumbnail) | **POST** /generateThumbnail |  |
| [**getAreaOfInterest**](DefaultApi.md#getAreaOfInterest) | **POST** /areaOfInterest |  |
| [**listModels**](DefaultApi.md#listModels) | **GET** /models |  |
| [**recognizePrintedText**](DefaultApi.md#recognizePrintedText) | **POST** /ocr |  |
| [**tagImage**](DefaultApi.md#tagImage) | **POST** /tag |  |


<a id="analyzeImage"></a>
# **analyzeImage**
> ImageAnalysis analyzeImage(imageUrl, visualFeatures, details, language, descriptionExclude)



This operation extracts a rich set of visual features based on the image content.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL. Within your request, there is an optional parameter to allow you to choose which features to return. By default, image categories are returned in the response.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

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
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
    List<String> visualFeatures = Arrays.asList(); // List<String> | A string indicating what visual feature types to return. Multiple values should be comma-separated. Valid visual feature types include: Categories - categorizes image content according to a taxonomy defined in documentation. Tags - tags the image with a detailed list of words related to the image content. Description - describes the image content with a complete English sentence. Faces - detects if faces are present. If present, generate coordinates, gender and age. ImageType - detects if image is clipart or a line drawing. Color - determines the accent color, dominant color, and whether an image is black&white. Adult - detects if the image is pornographic in nature (depicts nudity or a sex act), or is gory (depicts extreme violence or blood). Sexually suggestive content (aka racy content) is also detected. Objects - detects various objects within an image, including the approximate location. The Objects argument is only available in English. Brands - detects various brands within an image, including the approximate location. The Brands argument is only available in English.
    List<String> details = Arrays.asList(); // List<String> | A string indicating which domain-specific details to return. Multiple values should be comma-separated. Valid visual feature types include: Celebrities - identifies celebrities if detected in the image, Landmarks - identifies notable landmarks in the image.
    String language = "en"; // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    List<String> descriptionExclude = Arrays.asList(); // List<String> | Turn off specified domain models when generating the description.
    try {
      ImageAnalysis result = apiInstance.analyzeImage(imageUrl, visualFeatures, details, language, descriptionExclude);
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
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **visualFeatures** | [**List&lt;String&gt;**](String.md)| A string indicating what visual feature types to return. Multiple values should be comma-separated. Valid visual feature types include: Categories - categorizes image content according to a taxonomy defined in documentation. Tags - tags the image with a detailed list of words related to the image content. Description - describes the image content with a complete English sentence. Faces - detects if faces are present. If present, generate coordinates, gender and age. ImageType - detects if image is clipart or a line drawing. Color - determines the accent color, dominant color, and whether an image is black&amp;white. Adult - detects if the image is pornographic in nature (depicts nudity or a sex act), or is gory (depicts extreme violence or blood). Sexually suggestive content (aka racy content) is also detected. Objects - detects various objects within an image, including the approximate location. The Objects argument is only available in English. Brands - detects various brands within an image, including the approximate location. The Brands argument is only available in English. | [optional] [enum: ImageType, Faces, Adult, Categories, Color, Tags, Description, Objects, Brands] |
| **details** | [**List&lt;String&gt;**](String.md)| A string indicating which domain-specific details to return. Multiple values should be comma-separated. Valid visual feature types include: Celebrities - identifies celebrities if detected in the image, Landmarks - identifies notable landmarks in the image. | [optional] [enum: Celebrities, Landmarks] |
| **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to en] [enum: en, es, ja, pt, zh] |
| **descriptionExclude** | [**List&lt;String&gt;**](String.md)| Turn off specified domain models when generating the description. | [optional] [enum: Celebrities, Landmarks] |

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
| **200** | The response include the extracted features in JSON format. Here is the definitions for enumeration types:   ClipartType   Non - clipart &#x3D; 0, ambiguous &#x3D; 1, normal - clipart &#x3D; 2, good - clipart &#x3D; 3. LineDrawingTypeNon - LineDrawing &#x3D; 0, LineDrawing &#x3D; 1. |  -  |
| **0** | Error response. |  -  |

<a id="analyzeImageByDomain"></a>
# **analyzeImageByDomain**
> DomainModelResults analyzeImageByDomain(model, imageUrl, language)



This operation recognizes content within an image by applying a domain-specific model. The list of domain-specific models that are supported by the Computer Vision API can be retrieved using the /models GET request. Currently, the API provides following domain-specific models: celebrities, landmarks.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.

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
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String model = "Celebrities"; // String | The domain-specific content to recognize.
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
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
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
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
| **200** | Analysis result based on the domain model. |  -  |
| **0** | Error response. |  -  |

<a id="describeImage"></a>
# **describeImage**
> ImageDescription describeImage(imageUrl, maxCandidates, language, descriptionExclude)



This operation generates a description of an image in human readable language with complete sentences. The description is based on a collection of content tags, which are also returned by the operation. More than one description can be generated for each image. Descriptions are ordered by their confidence score. Descriptions may include results from celebrity and landmark domain models, if applicable.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

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
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
    Integer maxCandidates = 1; // Integer | Maximum number of candidate descriptions to be returned.  The default is 1.
    String language = "en"; // String | The desired language for output generation. If this parameter is not specified, the default value is &quot;en&quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese.
    List<String> descriptionExclude = Arrays.asList(); // List<String> | Turn off specified domain models when generating the description.
    try {
      ImageDescription result = apiInstance.describeImage(imageUrl, maxCandidates, language, descriptionExclude);
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
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **maxCandidates** | **Integer**| Maximum number of candidate descriptions to be returned.  The default is 1. | [optional] [default to 1] |
| **language** | **String**| The desired language for output generation. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.Supported languages:en - English, Default. es - Spanish, ja - Japanese, pt - Portuguese, zh - Simplified Chinese. | [optional] [default to en] [enum: en, es, ja, pt, zh] |
| **descriptionExclude** | [**List&lt;String&gt;**](String.md)| Turn off specified domain models when generating the description. | [optional] [enum: Celebrities, Landmarks] |

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

<a id="detectObjects"></a>
# **detectObjects**
> DetectResult detectObjects(imageUrl)



Performs object detection on the specified image.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

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
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
    try {
      DetectResult result = apiInstance.detectObjects(imageUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#detectObjects");
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
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |

### Return type

[**DetectResult**](DetectResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response include the detected objects in JSON format. |  -  |
| **0** | Error response. |  -  |

<a id="generateThumbnail"></a>
# **generateThumbnail**
> File generateThumbnail(width, height, imageUrl, smartCropping)



This operation generates a thumbnail image with the user-specified width and height. By default, the service analyzes the image, identifies the region of interest (ROI), and generates smart cropping coordinates based on the ROI. Smart cropping helps when you specify an aspect ratio that differs from that of the input image.  A successful response contains the thumbnail image binary. If the request failed, the response contains an error code and a message to help determine what went wrong.  Upon failure, the error code and an error message are returned. The error code could be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, InvalidThumbnailSize, NotSupportedImage, FailedToProcess, Timeout, or InternalServerError.

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
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer width = 500; // Integer | Width of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50.
    Integer height = 500; // Integer | Height of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50.
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
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
| **width** | **Integer**| Width of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50. | |
| **height** | **Integer**| Height of the thumbnail, in pixels. It must be between 1 and 1024. Recommended minimum of 50. | |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
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

<a id="getAreaOfInterest"></a>
# **getAreaOfInterest**
> AreaOfInterestResult getAreaOfInterest(imageUrl)



This operation returns a bounding box around the most important area of the image.  A successful response will be returned in JSON. If the request failed, the response contains an error code and a message to help determine what went wrong.  Upon failure, the error code and an error message are returned. The error code could be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, NotSupportedImage, FailedToProcess, Timeout, or InternalServerError.

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
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
    try {
      AreaOfInterestResult result = apiInstance.getAreaOfInterest(imageUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAreaOfInterest");
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
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |

### Return type

[**AreaOfInterestResult**](AreaOfInterestResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response includes the extracted area of interest in JSON format. |  -  |
| **0** | Error response. |  -  |

<a id="listModels"></a>
# **listModels**
> ListModelsResult listModels()



This operation returns the list of domain-specific models that are supported by the Computer Vision API. Currently, the API supports following domain-specific models: celebrity recognizer, landmark recognizer.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

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
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
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



Optical Character Recognition (OCR) detects text in an image and extracts the recognized characters into a machine-usable character stream.  Upon success, the OCR results will be returned.  Upon failure, the error code together with an error message will be returned. The error code can be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, NotSupportedImage, NotSupportedLanguage, or InternalServerError.

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
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean detectOrientation = true; // Boolean | Whether detect the text orientation in the image. With detectOrientation=true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it's upside-down).
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
    String language = "unk"; // String | The BCP-47 language code of the text to be detected in the image. The default value is 'unk'.
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
| **detectOrientation** | **Boolean**| Whether detect the text orientation in the image. With detectOrientation&#x3D;true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it&#39;s upside-down). | [default to true] |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
| **language** | **String**| The BCP-47 language code of the text to be detected in the image. The default value is &#39;unk&#39;. | [optional] [default to unk] [enum: unk, zh-Hans, zh-Hant, cs, da, nl, en, fi, fr, de, el, hu, it, ja, ko, nb, pl, pt, ru, es, sv, tr, ar, ro, sr-Cyrl, sr-Latn, sk] |

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
| **200** | The OCR results in the hierarchy of region/line/word. The results include text, bounding box for regions, lines and words. The angle, in radians, of the detected text with respect to the closest horizontal or vertical direction. After rotating the input image clockwise by this angle, the recognized text lines become horizontal or vertical. In combination with the orientation property it can be used to overlay recognition results correctly on the original image, by rotating either the original image or recognition results by a suitable angle around the center of the original image. If the angle cannot be confidently detected, this property is not present. If the image contains text at different angles, only part of the text will be recognized correctly. |  -  |
| **0** | Error response. |  -  |

<a id="tagImage"></a>
# **tagImage**
> TagResult tagImage(imageUrl, language)



This operation generates a list of words, or tags, that are relevant to the content of the supplied image. The Computer Vision API can return tags based on objects, living beings, scenery or actions found in images. Unlike categories, tags are not organized according to a hierarchical classification system, but correspond to image content. Tags may contain hints to avoid ambiguity or provide context, for example the tag \&quot;ascomycete\&quot; may be accompanied by the hint \&quot;fungus\&quot;.  Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.

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
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
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
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |
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

