# VisionPredictionApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**detectMultipart**](VisionPredictionApi.md#detectMultipart) | **POST** /v2/vision/detect | Detection with Image File |
| [**ocrMultipart**](VisionPredictionApi.md#ocrMultipart) | **POST** /v2/vision/ocr | Detect Text |
| [**predictMultipart**](VisionPredictionApi.md#predictMultipart) | **POST** /v2/vision/predict | Make Prediction |


<a id="detectMultipart"></a>
# **detectMultipart**
> ObjectDetectionResponse detectMultipart(objectDetectionRequest)

Detection with Image File

Returns labels, probabilities, and bounding box coordinates for items detected in the specified local image file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionPredictionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionPredictionApi apiInstance = new VisionPredictionApi(defaultClient);
    ObjectDetectionRequest objectDetectionRequest = new ObjectDetectionRequest(); // ObjectDetectionRequest | 
    try {
      ObjectDetectionResponse result = apiInstance.detectMultipart(objectDetectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionPredictionApi#detectMultipart");
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
| **objectDetectionRequest** | [**ObjectDetectionRequest**](ObjectDetectionRequest.md)|  | [optional] |

### Return type

[**ObjectDetectionResponse**](ObjectDetectionResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detection Result |  -  |

<a id="ocrMultipart"></a>
# **ocrMultipart**
> OCRPredictResponse ocrMultipart(modelId, sampleContent, sampleId, sampleLocation, task)

Detect Text

Returns a prediction from an OCR model for the specified image URL or local image file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionPredictionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionPredictionApi apiInstance = new VisionPredictionApi(defaultClient);
    String modelId = "modelId_example"; // String | ID of the model that makes the prediction. Valid values are OCRModel and tabulatev2.
    File sampleContent = new File("/path/to/file"); // File | Binary content of image file uploaded as multipart/form-data. Optional.
    String sampleId = "sampleId_example"; // String | String that you can pass in to tag the prediction. Optional. Can be any value, and is returned in the response.
    String sampleLocation = "sampleLocation_example"; // String | URL of the image file. Use this parameter when sending in a file from a web location. Optional.
    String task = "text"; // String | Optional. Designates the type of data in the image. Default is text. Valid values: contact, table, and text.
    try {
      OCRPredictResponse result = apiInstance.ocrMultipart(modelId, sampleContent, sampleId, sampleLocation, task);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionPredictionApi#ocrMultipart");
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
| **modelId** | **String**| ID of the model that makes the prediction. Valid values are OCRModel and tabulatev2. | [optional] |
| **sampleContent** | **File**| Binary content of image file uploaded as multipart/form-data. Optional. | [optional] |
| **sampleId** | **String**| String that you can pass in to tag the prediction. Optional. Can be any value, and is returned in the response. | [optional] |
| **sampleLocation** | **String**| URL of the image file. Use this parameter when sending in a file from a web location. Optional. | [optional] |
| **task** | **String**| Optional. Designates the type of data in the image. Default is text. Valid values: contact, table, and text. | [optional] [default to text] |

### Return type

[**OCRPredictResponse**](OCRPredictResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OCR Result |  -  |

<a id="predictMultipart"></a>
# **predictMultipart**
> ImageClassificationResponse predictMultipart(imageClassificationRequest)

Make Prediction

Returns a prediction from an image or multi-label model for the specified image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionPredictionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionPredictionApi apiInstance = new VisionPredictionApi(defaultClient);
    ImageClassificationRequest imageClassificationRequest = new ImageClassificationRequest(); // ImageClassificationRequest | 
    try {
      ImageClassificationResponse result = apiInstance.predictMultipart(imageClassificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionPredictionApi#predictMultipart");
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
| **imageClassificationRequest** | [**ImageClassificationRequest**](ImageClassificationRequest.md)|  | [optional] |

### Return type

[**ImageClassificationResponse**](ImageClassificationResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prediction Result |  -  |

