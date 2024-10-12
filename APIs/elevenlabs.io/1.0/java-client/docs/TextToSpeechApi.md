# TextToSpeechApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**textToSpeechV1TextToSpeechVoiceIdPost**](TextToSpeechApi.md#textToSpeechV1TextToSpeechVoiceIdPost) | **POST** /v1/text-to-speech/{voice_id} | Text To Speech |
| [**textToSpeechV1TextToSpeechVoiceIdStreamPost**](TextToSpeechApi.md#textToSpeechV1TextToSpeechVoiceIdStreamPost) | **POST** /v1/text-to-speech/{voice_id}/stream | Text To Speech |


<a id="textToSpeechV1TextToSpeechVoiceIdPost"></a>
# **textToSpeechV1TextToSpeechVoiceIdPost**
> textToSpeechV1TextToSpeechVoiceIdPost(voiceId, bodyTextToSpeechV1TextToSpeechVoiceIdPost, xiApiKey)

Text To Speech

Converts text into speech using a voice of your choice and returns audio.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextToSpeechApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TextToSpeechApi apiInstance = new TextToSpeechApi(defaultClient);
    String voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    BodyTextToSpeechV1TextToSpeechVoiceIdPost bodyTextToSpeechV1TextToSpeechVoiceIdPost = new BodyTextToSpeechV1TextToSpeechVoiceIdPost(); // BodyTextToSpeechV1TextToSpeechVoiceIdPost | 
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      apiInstance.textToSpeechV1TextToSpeechVoiceIdPost(voiceId, bodyTextToSpeechV1TextToSpeechVoiceIdPost, xiApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextToSpeechApi#textToSpeechV1TextToSpeechVoiceIdPost");
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
| **voiceId** | **String**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | |
| **bodyTextToSpeechV1TextToSpeechVoiceIdPost** | [**BodyTextToSpeechV1TextToSpeechVoiceIdPost**](BodyTextToSpeechV1TextToSpeechVoiceIdPost.md)|  | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: audio/mpeg, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="textToSpeechV1TextToSpeechVoiceIdStreamPost"></a>
# **textToSpeechV1TextToSpeechVoiceIdStreamPost**
> textToSpeechV1TextToSpeechVoiceIdStreamPost(voiceId, bodyTextToSpeechV1TextToSpeechVoiceIdStreamPost, xiApiKey)

Text To Speech

Converts text into speech using a voice of your choice and returns audio as an audio stream.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextToSpeechApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TextToSpeechApi apiInstance = new TextToSpeechApi(defaultClient);
    String voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost bodyTextToSpeechV1TextToSpeechVoiceIdStreamPost = new BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost(); // BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost | 
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      apiInstance.textToSpeechV1TextToSpeechVoiceIdStreamPost(voiceId, bodyTextToSpeechV1TextToSpeechVoiceIdStreamPost, xiApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextToSpeechApi#textToSpeechV1TextToSpeechVoiceIdStreamPost");
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
| **voiceId** | **String**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | |
| **bodyTextToSpeechV1TextToSpeechVoiceIdStreamPost** | [**BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost**](BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost.md)|  | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

