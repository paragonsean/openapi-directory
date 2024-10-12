# ImageModerationApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**imageModerationEvaluate**](ImageModerationApi.md#imageModerationEvaluate) | **POST** /contentmoderator/moderate/v1.0/ProcessImage/Evaluate |  |
| [**imageModerationFindFaces**](ImageModerationApi.md#imageModerationFindFaces) | **POST** /contentmoderator/moderate/v1.0/ProcessImage/FindFaces |  |
| [**imageModerationMatch**](ImageModerationApi.md#imageModerationMatch) | **POST** /contentmoderator/moderate/v1.0/ProcessImage/Match |  |
| [**imageModerationOCR**](ImageModerationApi.md#imageModerationOCR) | **POST** /contentmoderator/moderate/v1.0/ProcessImage/OCR |  |


<a id="imageModerationEvaluate"></a>
# **imageModerationEvaluate**
> Evaluate imageModerationEvaluate(cacheImage)



Returns probabilities of the image containing racy or adult content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImageModerationApi apiInstance = new ImageModerationApi(defaultClient);
    Boolean cacheImage = true; // Boolean | Whether to retain the submitted image for future use; defaults to false if omitted.
    try {
      Evaluate result = apiInstance.imageModerationEvaluate(cacheImage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageModerationApi#imageModerationEvaluate");
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
| **cacheImage** | **Boolean**| Whether to retain the submitted image for future use; defaults to false if omitted. | [optional] |

### Return type

[**Evaluate**](Evaluate.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** | Error response. |  -  |

<a id="imageModerationFindFaces"></a>
# **imageModerationFindFaces**
> FoundFaces imageModerationFindFaces(cacheImage)



Returns the list of faces found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImageModerationApi apiInstance = new ImageModerationApi(defaultClient);
    Boolean cacheImage = true; // Boolean | Whether to retain the submitted image for future use; defaults to false if omitted.
    try {
      FoundFaces result = apiInstance.imageModerationFindFaces(cacheImage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageModerationApi#imageModerationFindFaces");
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
| **cacheImage** | **Boolean**| Whether to retain the submitted image for future use; defaults to false if omitted. | [optional] |

### Return type

[**FoundFaces**](FoundFaces.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of faces found. |  -  |
| **0** | Error response. |  -  |

<a id="imageModerationMatch"></a>
# **imageModerationMatch**
> MatchResponse imageModerationMatch(listId, cacheImage)



Fuzzily match an image against one of your custom Image Lists. You can create and manage your custom image lists using &lt;a href&#x3D;\&quot;/docs/services/578ff44d2703741568569ab9/operations/578ff7b12703741568569abe\&quot;&gt;this&lt;/a&gt; API.     Returns ID and tags of matching image.&lt;br/&gt;  &lt;br/&gt;  Note: Refresh Index must be run on the corresponding Image List before additions and removals are reflected in the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImageModerationApi apiInstance = new ImageModerationApi(defaultClient);
    String listId = "listId_example"; // String | The list Id.
    Boolean cacheImage = true; // Boolean | Whether to retain the submitted image for future use; defaults to false if omitted.
    try {
      MatchResponse result = apiInstance.imageModerationMatch(listId, cacheImage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageModerationApi#imageModerationMatch");
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
| **listId** | **String**| The list Id. | [optional] |
| **cacheImage** | **Boolean**| Whether to retain the submitted image for future use; defaults to false if omitted. | [optional] |

### Return type

[**MatchResponse**](MatchResponse.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Supported values for tags are:  &lt;ul&gt;  &lt;li&gt;101: Nudity&lt;/li&gt;  &lt;li&gt;102: Sexual Content&lt;/li&gt;  &lt;li&gt;201: Alcohol&lt;/li&gt;  &lt;li&gt;202: Tobacco&lt;/li&gt;  &lt;li&gt;203: Drugs&lt;/li&gt;  &lt;li&gt;301: Child Exploitation&lt;/li&gt;  &lt;li&gt;401: Violence&lt;/li&gt;  &lt;li&gt;402: Weapons&lt;/li&gt;  &lt;li&gt;403: Gore&lt;/li&gt;  &lt;li&gt;501: Profanity&lt;/li&gt;  &lt;li&gt;502: Vulgarity&lt;/li&gt;  &lt;/ul&gt;. |  -  |
| **0** | Error response. |  -  |

<a id="imageModerationOCR"></a>
# **imageModerationOCR**
> OCR imageModerationOCR(language, cacheImage, enhanced)



Returns any text found in the image for the language specified. If no language is specified in input then the detection defaults to English.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageModerationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ImageModerationApi apiInstance = new ImageModerationApi(defaultClient);
    String language = "language_example"; // String | Language of the terms.
    Boolean cacheImage = true; // Boolean | Whether to retain the submitted image for future use; defaults to false if omitted.
    Boolean enhanced = false; // Boolean | When set to True, the image goes through additional processing to come with additional candidates.  image/tiff is not supported when enhanced is set to true  Note: This impacts the response time.
    try {
      OCR result = apiInstance.imageModerationOCR(language, cacheImage, enhanced);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageModerationApi#imageModerationOCR");
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
| **language** | **String**| Language of the terms. | |
| **cacheImage** | **Boolean**| Whether to retain the submitted image for future use; defaults to false if omitted. | [optional] |
| **enhanced** | **Boolean**| When set to True, the image goes through additional processing to come with additional candidates.  image/tiff is not supported when enhanced is set to true  Note: This impacts the response time. | [optional] [default to false] |

### Return type

[**OCR**](OCR.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The text found and list of candidate text details. |  -  |
| **0** | Error response. |  -  |

