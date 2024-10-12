# WebfontsApi

All URIs are relative to *https://webfonts.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webfontsWebfontsList**](WebfontsApi.md#webfontsWebfontsList) | **GET** /v1/webfonts |  |


<a id="webfontsWebfontsList"></a>
# **webfontsWebfontsList**
> WebfontList webfontsWebfontsList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, capability, family, sort, subset)



Retrieves the list of fonts currently served by the Google Fonts Developer API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebfontsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webfonts.googleapis.com");

    WebfontsApi apiInstance = new WebfontsApi(defaultClient);
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
    List<String> capability = Arrays.asList(); // List<String> | Controls the font urls in `Webfont.files`, by default, static ttf fonts are sent.
    List<String> family = Arrays.asList(); // List<String> | Filters by Webfont.family, using literal match. If not set, returns all families
    String sort = "SORT_UNDEFINED"; // String | Enables sorting of the list.
    String subset = "subset_example"; // String | Filters by Webfont.subset, if subset is found in Webfont.subsets. If not set, returns all families.
    try {
      WebfontList result = apiInstance.webfontsWebfontsList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, capability, family, sort, subset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebfontsApi#webfontsWebfontsList");
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
| **capability** | [**List&lt;String&gt;**](String.md)| Controls the font urls in &#x60;Webfont.files&#x60;, by default, static ttf fonts are sent. | [optional] [enum: CAPABILITY_UNSPECIFIED, WOFF2, VF] |
| **family** | [**List&lt;String&gt;**](String.md)| Filters by Webfont.family, using literal match. If not set, returns all families | [optional] |
| **sort** | **String**| Enables sorting of the list. | [optional] [enum: SORT_UNDEFINED, ALPHA, DATE, POPULARITY, STYLE, TRENDING] |
| **subset** | **String**| Filters by Webfont.subset, if subset is found in Webfont.subsets. If not set, returns all families. | [optional] |

### Return type

[**WebfontList**](WebfontList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

