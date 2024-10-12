# PhotoSequencesApi

All URIs are relative to *https://streetviewpublish.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**streetviewpublishPhotoSequencesList**](PhotoSequencesApi.md#streetviewpublishPhotoSequencesList) | **GET** /v1/photoSequences |  |


<a id="streetviewpublishPhotoSequencesList"></a>
# **streetviewpublishPhotoSequencesList**
> ListPhotoSequencesResponse streetviewpublishPhotoSequencesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Lists all the PhotoSequences that belong to the user, in descending CreatePhotoSequence timestamp order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhotoSequencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://streetviewpublish.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PhotoSequencesApi apiInstance = new PhotoSequencesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | Optional. The filter expression. For example: `imagery_type=SPHERICAL`. The filters supported are: `imagery_type`, `processing_state`, `min_latitude`, `max_latitude`, `min_longitude`, `max_longitude`, `filename_query`, `min_capture_time_seconds`, `max_capture_time_seconds. See https://google.aip.dev/160 for more information. Filename queries should sent as a Phrase in order to support multiple words and special characters by adding escaped quotes. Ex: filename_query=\"example of a phrase.mp4\"
    Integer pageSize = 56; // Integer | Optional. The maximum number of photo sequences to return. `pageSize` must be non-negative. If `pageSize` is zero or is not provided, the default page size of 100 is used. The number of photo sequences returned in the response may be less than `pageSize` if the number of matches is less than `pageSize`. This is currently unimplemented but is in process.
    String pageToken = "pageToken_example"; // String | Optional. The nextPageToken value returned from a previous ListPhotoSequences request, if any.
    try {
      ListPhotoSequencesResponse result = apiInstance.streetviewpublishPhotoSequencesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhotoSequencesApi#streetviewpublishPhotoSequencesList");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| Optional. The filter expression. For example: &#x60;imagery_type&#x3D;SPHERICAL&#x60;. The filters supported are: &#x60;imagery_type&#x60;, &#x60;processing_state&#x60;, &#x60;min_latitude&#x60;, &#x60;max_latitude&#x60;, &#x60;min_longitude&#x60;, &#x60;max_longitude&#x60;, &#x60;filename_query&#x60;, &#x60;min_capture_time_seconds&#x60;, &#x60;max_capture_time_seconds. See https://google.aip.dev/160 for more information. Filename queries should sent as a Phrase in order to support multiple words and special characters by adding escaped quotes. Ex: filename_query&#x3D;\&quot;example of a phrase.mp4\&quot; | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of photo sequences to return. &#x60;pageSize&#x60; must be non-negative. If &#x60;pageSize&#x60; is zero or is not provided, the default page size of 100 is used. The number of photo sequences returned in the response may be less than &#x60;pageSize&#x60; if the number of matches is less than &#x60;pageSize&#x60;. This is currently unimplemented but is in process. | [optional] |
| **pageToken** | **String**| Optional. The nextPageToken value returned from a previous ListPhotoSequences request, if any. | [optional] |

### Return type

[**ListPhotoSequencesResponse**](ListPhotoSequencesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

