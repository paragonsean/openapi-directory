# VideoV1RecordingSettingsApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRecordingSettings**](VideoV1RecordingSettingsApi.md#createRecordingSettings) | **POST** /v1/RecordingSettings/Default |  |
| [**fetchRecordingSettings**](VideoV1RecordingSettingsApi.md#fetchRecordingSettings) | **GET** /v1/RecordingSettings/Default |  |


<a id="createRecordingSettings"></a>
# **createRecordingSettings**
> VideoV1RecordingSettings createRecordingSettings(friendlyName, awsCredentialsSid, awsS3Url, awsStorageEnabled, encryptionEnabled, encryptionKeySid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RecordingSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RecordingSettingsApi apiInstance = new VideoV1RecordingSettingsApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource and be shown to users in the console
    String awsCredentialsSid = "awsCredentialsSid_example"; // String | The SID of the stored Credential resource.
    URI awsS3Url = new URI(); // URI | The URL of the AWS S3 bucket where the recordings should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/recordings`, where `recordings` is the path in which you want the recordings to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2).
    Boolean awsStorageEnabled = true; // Boolean | Whether all recordings should be written to the `aws_s3_url`. When `false`, all recordings are stored in our cloud.
    Boolean encryptionEnabled = true; // Boolean | Whether all recordings should be stored in an encrypted form. The default is `false`.
    String encryptionKeySid = "encryptionKeySid_example"; // String | The SID of the Public Key resource to use for encryption.
    try {
      VideoV1RecordingSettings result = apiInstance.createRecordingSettings(friendlyName, awsCredentialsSid, awsS3Url, awsStorageEnabled, encryptionEnabled, encryptionKeySid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RecordingSettingsApi#createRecordingSettings");
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
| **friendlyName** | **String**| A descriptive string that you create to describe the resource and be shown to users in the console | |
| **awsCredentialsSid** | **String**| The SID of the stored Credential resource. | [optional] |
| **awsS3Url** | **URI**| The URL of the AWS S3 bucket where the recordings should be stored. We only support DNS-compliant URLs like &#x60;https://documentation-example-twilio-bucket/recordings&#x60;, where &#x60;recordings&#x60; is the path in which you want the recordings to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2). | [optional] |
| **awsStorageEnabled** | **Boolean**| Whether all recordings should be written to the &#x60;aws_s3_url&#x60;. When &#x60;false&#x60;, all recordings are stored in our cloud. | [optional] |
| **encryptionEnabled** | **Boolean**| Whether all recordings should be stored in an encrypted form. The default is &#x60;false&#x60;. | [optional] |
| **encryptionKeySid** | **String**| The SID of the Public Key resource to use for encryption. | [optional] |

### Return type

[**VideoV1RecordingSettings**](VideoV1RecordingSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchRecordingSettings"></a>
# **fetchRecordingSettings**
> VideoV1RecordingSettings fetchRecordingSettings()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RecordingSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RecordingSettingsApi apiInstance = new VideoV1RecordingSettingsApi(defaultClient);
    try {
      VideoV1RecordingSettings result = apiInstance.fetchRecordingSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RecordingSettingsApi#fetchRecordingSettings");
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

[**VideoV1RecordingSettings**](VideoV1RecordingSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

