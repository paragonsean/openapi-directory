# VideoV1CompositionSettingsApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCompositionSettings**](VideoV1CompositionSettingsApi.md#createCompositionSettings) | **POST** /v1/CompositionSettings/Default |  |
| [**fetchCompositionSettings**](VideoV1CompositionSettingsApi.md#fetchCompositionSettings) | **GET** /v1/CompositionSettings/Default |  |


<a id="createCompositionSettings"></a>
# **createCompositionSettings**
> VideoV1CompositionSettings createCompositionSettings(friendlyName, awsCredentialsSid, awsS3Url, awsStorageEnabled, encryptionEnabled, encryptionKeySid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1CompositionSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1CompositionSettingsApi apiInstance = new VideoV1CompositionSettingsApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource and show to the user in the console
    String awsCredentialsSid = "awsCredentialsSid_example"; // String | The SID of the stored Credential resource.
    URI awsS3Url = new URI(); // URI | The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/compositions`, where `compositions` is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2).
    Boolean awsStorageEnabled = true; // Boolean | Whether all compositions should be written to the `aws_s3_url`. When `false`, all compositions are stored in our cloud.
    Boolean encryptionEnabled = true; // Boolean | Whether all compositions should be stored in an encrypted form. The default is `false`.
    String encryptionKeySid = "encryptionKeySid_example"; // String | The SID of the Public Key resource to use for encryption.
    try {
      VideoV1CompositionSettings result = apiInstance.createCompositionSettings(friendlyName, awsCredentialsSid, awsS3Url, awsStorageEnabled, encryptionEnabled, encryptionKeySid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1CompositionSettingsApi#createCompositionSettings");
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
| **friendlyName** | **String**| A descriptive string that you create to describe the resource and show to the user in the console | |
| **awsCredentialsSid** | **String**| The SID of the stored Credential resource. | [optional] |
| **awsS3Url** | **URI**| The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like &#x60;https://documentation-example-twilio-bucket/compositions&#x60;, where &#x60;compositions&#x60; is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2). | [optional] |
| **awsStorageEnabled** | **Boolean**| Whether all compositions should be written to the &#x60;aws_s3_url&#x60;. When &#x60;false&#x60;, all compositions are stored in our cloud. | [optional] |
| **encryptionEnabled** | **Boolean**| Whether all compositions should be stored in an encrypted form. The default is &#x60;false&#x60;. | [optional] |
| **encryptionKeySid** | **String**| The SID of the Public Key resource to use for encryption. | [optional] |

### Return type

[**VideoV1CompositionSettings**](VideoV1CompositionSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchCompositionSettings"></a>
# **fetchCompositionSettings**
> VideoV1CompositionSettings fetchCompositionSettings()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1CompositionSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1CompositionSettingsApi apiInstance = new VideoV1CompositionSettingsApi(defaultClient);
    try {
      VideoV1CompositionSettings result = apiInstance.fetchCompositionSettings();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1CompositionSettingsApi#fetchCompositionSettings");
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

[**VideoV1CompositionSettings**](VideoV1CompositionSettings.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

