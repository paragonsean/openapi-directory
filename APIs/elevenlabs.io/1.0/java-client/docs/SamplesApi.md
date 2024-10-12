# SamplesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete**](SamplesApi.md#deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete) | **DELETE** /v1/voices/{voice_id}/samples/{sample_id} | Delete Sample |
| [**getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet**](SamplesApi.md#getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet) | **GET** /v1/voices/{voice_id}/samples/{sample_id}/audio | Get Audio From Sample |


<a id="deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete"></a>
# **deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete**
> Object deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete(voiceId, sampleId, xiApiKey)

Delete Sample

Removes a sample by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SamplesApi apiInstance = new SamplesApi(defaultClient);
    String voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    String sampleId = "VW7YKqPnjY4h39yTbx2L"; // String | Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice.
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      Object result = apiInstance.deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete(voiceId, sampleId, xiApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamplesApi#deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete");
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
| **sampleId** | **String**| Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice. | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet"></a>
# **getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet**
> getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet(voiceId, sampleId, xiApiKey)

Get Audio From Sample

Returns the audio corresponding to a sample attached to a voice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SamplesApi apiInstance = new SamplesApi(defaultClient);
    String voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    String sampleId = "VW7YKqPnjY4h39yTbx2L"; // String | Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice.
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      apiInstance.getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet(voiceId, sampleId, xiApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SamplesApi#getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet");
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
| **sampleId** | **String**| Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice. | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

