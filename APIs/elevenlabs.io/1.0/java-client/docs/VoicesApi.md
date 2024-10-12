# VoicesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVoiceV1VoicesAddPost**](VoicesApi.md#addVoiceV1VoicesAddPost) | **POST** /v1/voices/add | Add Voice |
| [**deleteVoiceV1VoicesVoiceIdDelete**](VoicesApi.md#deleteVoiceV1VoicesVoiceIdDelete) | **DELETE** /v1/voices/{voice_id} | Delete Voice |
| [**editVoiceSettingsV1VoicesVoiceIdSettingsEditPost**](VoicesApi.md#editVoiceSettingsV1VoicesVoiceIdSettingsEditPost) | **POST** /v1/voices/{voice_id}/settings/edit | Edit Voice Settings |
| [**editVoiceV1VoicesVoiceIdEditPost**](VoicesApi.md#editVoiceV1VoicesVoiceIdEditPost) | **POST** /v1/voices/{voice_id}/edit | Edit Voice |
| [**getDefaultVoiceSettingsV1VoicesSettingsDefaultGet**](VoicesApi.md#getDefaultVoiceSettingsV1VoicesSettingsDefaultGet) | **GET** /v1/voices/settings/default | Get Default Voice Settings. |
| [**getVoiceSettingsV1VoicesVoiceIdSettingsGet**](VoicesApi.md#getVoiceSettingsV1VoicesVoiceIdSettingsGet) | **GET** /v1/voices/{voice_id}/settings | Get Voice Settings |
| [**getVoiceV1VoicesVoiceIdGet**](VoicesApi.md#getVoiceV1VoicesVoiceIdGet) | **GET** /v1/voices/{voice_id} | Get Voice |
| [**getVoicesV1VoicesGet**](VoicesApi.md#getVoicesV1VoicesGet) | **GET** /v1/voices | Get Voices |


<a id="addVoiceV1VoicesAddPost"></a>
# **addVoiceV1VoicesAddPost**
> AddVoiceResponseModel addVoiceV1VoicesAddPost(files, name, xiApiKey, description, labels)

Add Voice

Add a new voice to your collection of voices in VoiceLab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VoicesApi apiInstance = new VoicesApi(defaultClient);
    List<File> files = Arrays.asList(); // List<File> | One or more audio files to clone the voice from
    String name = "name_example"; // String | The name that identifies this voice. This will be displayed in the dropdown of the website.
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    String description = "description_example"; // String | How would you describe the voice?
    String labels = "labels_example"; // String | Serialized labels dictionary for the voice.
    try {
      AddVoiceResponseModel result = apiInstance.addVoiceV1VoicesAddPost(files, name, xiApiKey, description, labels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoicesApi#addVoiceV1VoicesAddPost");
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
| **files** | **List&lt;File&gt;**| One or more audio files to clone the voice from | |
| **name** | **String**| The name that identifies this voice. This will be displayed in the dropdown of the website. | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |
| **description** | **String**| How would you describe the voice? | [optional] |
| **labels** | **String**| Serialized labels dictionary for the voice. | [optional] |

### Return type

[**AddVoiceResponseModel**](AddVoiceResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="deleteVoiceV1VoicesVoiceIdDelete"></a>
# **deleteVoiceV1VoicesVoiceIdDelete**
> Object deleteVoiceV1VoicesVoiceIdDelete(voiceId, xiApiKey)

Delete Voice

Deletes a voice by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VoicesApi apiInstance = new VoicesApi(defaultClient);
    String voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      Object result = apiInstance.deleteVoiceV1VoicesVoiceIdDelete(voiceId, xiApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoicesApi#deleteVoiceV1VoicesVoiceIdDelete");
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

<a id="editVoiceSettingsV1VoicesVoiceIdSettingsEditPost"></a>
# **editVoiceSettingsV1VoicesVoiceIdSettingsEditPost**
> Object editVoiceSettingsV1VoicesVoiceIdSettingsEditPost(voiceId, voiceSettingsResponseModel, xiApiKey)

Edit Voice Settings

Edit your settings for a specific voice. \&quot;similarity_boost\&quot; corresponds to\&quot;Clarity + Similarity Enhancement\&quot; in the web app and \&quot;stability\&quot; corresponds to \&quot;Stability\&quot; slider in the web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VoicesApi apiInstance = new VoicesApi(defaultClient);
    String voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    VoiceSettingsResponseModel voiceSettingsResponseModel = new VoiceSettingsResponseModel(); // VoiceSettingsResponseModel | 
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      Object result = apiInstance.editVoiceSettingsV1VoicesVoiceIdSettingsEditPost(voiceId, voiceSettingsResponseModel, xiApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoicesApi#editVoiceSettingsV1VoicesVoiceIdSettingsEditPost");
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
| **voiceSettingsResponseModel** | [**VoiceSettingsResponseModel**](VoiceSettingsResponseModel.md)|  | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

**Object**

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

<a id="editVoiceV1VoicesVoiceIdEditPost"></a>
# **editVoiceV1VoicesVoiceIdEditPost**
> Object editVoiceV1VoicesVoiceIdEditPost(voiceId, name, xiApiKey, description, files, labels)

Edit Voice

Edit a voice created by you.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VoicesApi apiInstance = new VoicesApi(defaultClient);
    String voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    String name = "name_example"; // String | The name that identifies this voice. This will be displayed in the dropdown of the website.
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    String description = "description_example"; // String | How would you describe the voice?
    List<File> files = Arrays.asList(); // List<File> | Audio files to add to the voice
    String labels = "labels_example"; // String | Serialized labels dictionary for the voice.
    try {
      Object result = apiInstance.editVoiceV1VoicesVoiceIdEditPost(voiceId, name, xiApiKey, description, files, labels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoicesApi#editVoiceV1VoicesVoiceIdEditPost");
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
| **name** | **String**| The name that identifies this voice. This will be displayed in the dropdown of the website. | |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |
| **description** | **String**| How would you describe the voice? | [optional] |
| **files** | **List&lt;File&gt;**| Audio files to add to the voice | [optional] |
| **labels** | **String**| Serialized labels dictionary for the voice. | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="getDefaultVoiceSettingsV1VoicesSettingsDefaultGet"></a>
# **getDefaultVoiceSettingsV1VoicesSettingsDefaultGet**
> VoiceSettingsResponseModel getDefaultVoiceSettingsV1VoicesSettingsDefaultGet()

Get Default Voice Settings.

Gets the default settings for voices. \&quot;similarity_boost\&quot; corresponds to\&quot;Clarity + Similarity Enhancement\&quot; in the web app and \&quot;stability\&quot; corresponds to \&quot;Stability\&quot; slider in the web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VoicesApi apiInstance = new VoicesApi(defaultClient);
    try {
      VoiceSettingsResponseModel result = apiInstance.getDefaultVoiceSettingsV1VoicesSettingsDefaultGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoicesApi#getDefaultVoiceSettingsV1VoicesSettingsDefaultGet");
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

[**VoiceSettingsResponseModel**](VoiceSettingsResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getVoiceSettingsV1VoicesVoiceIdSettingsGet"></a>
# **getVoiceSettingsV1VoicesVoiceIdSettingsGet**
> VoiceSettingsResponseModel getVoiceSettingsV1VoicesVoiceIdSettingsGet(voiceId, xiApiKey)

Get Voice Settings

Returns the settings for a specific voice. \&quot;similarity_boost\&quot; corresponds to\&quot;Clarity + Similarity Enhancement\&quot; in the web app and \&quot;stability\&quot; corresponds to \&quot;Stability\&quot; slider in the web app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VoicesApi apiInstance = new VoicesApi(defaultClient);
    String voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      VoiceSettingsResponseModel result = apiInstance.getVoiceSettingsV1VoicesVoiceIdSettingsGet(voiceId, xiApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoicesApi#getVoiceSettingsV1VoicesVoiceIdSettingsGet");
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
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

[**VoiceSettingsResponseModel**](VoiceSettingsResponseModel.md)

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

<a id="getVoiceV1VoicesVoiceIdGet"></a>
# **getVoiceV1VoicesVoiceIdGet**
> VoiceResponseModel getVoiceV1VoicesVoiceIdGet(voiceId, withSettings, xiApiKey)

Get Voice

Returns metadata about a specific voice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VoicesApi apiInstance = new VoicesApi(defaultClient);
    String voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    Boolean withSettings = false; // Boolean | If set will return settings information corresponding to the voice, requires authorization.
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      VoiceResponseModel result = apiInstance.getVoiceV1VoicesVoiceIdGet(voiceId, withSettings, xiApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoicesApi#getVoiceV1VoicesVoiceIdGet");
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
| **withSettings** | **Boolean**| If set will return settings information corresponding to the voice, requires authorization. | [optional] [default to false] |
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

[**VoiceResponseModel**](VoiceResponseModel.md)

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

<a id="getVoicesV1VoicesGet"></a>
# **getVoicesV1VoicesGet**
> GetVoicesResponseModel getVoicesV1VoicesGet(xiApiKey)

Get Voices

Gets a list of all available voices for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    VoicesApi apiInstance = new VoicesApi(defaultClient);
    String xiApiKey = "xiApiKey_example"; // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
    try {
      GetVoicesResponseModel result = apiInstance.getVoicesV1VoicesGet(xiApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoicesApi#getVoicesV1VoicesGet");
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
| **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] |

### Return type

[**GetVoicesResponseModel**](GetVoicesResponseModel.md)

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

