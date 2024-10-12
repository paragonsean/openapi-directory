# ReportTypesApi

All URIs are relative to *https://youtubereporting.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**youtubereportingReportTypesList**](ReportTypesApi.md#youtubereportingReportTypesList) | **GET** /v1/reportTypes |  |


<a id="youtubereportingReportTypesList"></a>
# **youtubereportingReportTypesList**
> ListReportTypesResponse youtubereportingReportTypesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeSystemManaged, onBehalfOfContentOwner, pageSize, pageToken)



Lists report types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://youtubereporting.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReportTypesApi apiInstance = new ReportTypesApi(defaultClient);
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
    Boolean includeSystemManaged = true; // Boolean | If set to true, also system-managed report types will be returned; otherwise only the report types that can be used to create new reporting jobs will be returned.
    String onBehalfOfContentOwner = "onBehalfOfContentOwner_example"; // String | The content owner's external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel).
    Integer pageSize = 56; // Integer | Requested page size. Server may return fewer report types than requested. If unspecified, server will pick an appropriate default.
    String pageToken = "pageToken_example"; // String | A token identifying a page of results the server should return. Typically, this is the value of ListReportTypesResponse.next_page_token returned in response to the previous call to the `ListReportTypes` method.
    try {
      ListReportTypesResponse result = apiInstance.youtubereportingReportTypesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeSystemManaged, onBehalfOfContentOwner, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportTypesApi#youtubereportingReportTypesList");
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
| **includeSystemManaged** | **Boolean**| If set to true, also system-managed report types will be returned; otherwise only the report types that can be used to create new reporting jobs will be returned. | [optional] |
| **onBehalfOfContentOwner** | **String**| The content owner&#39;s external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel). | [optional] |
| **pageSize** | **Integer**| Requested page size. Server may return fewer report types than requested. If unspecified, server will pick an appropriate default. | [optional] |
| **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of ListReportTypesResponse.next_page_token returned in response to the previous call to the &#x60;ListReportTypes&#x60; method. | [optional] |

### Return type

[**ListReportTypesResponse**](ListReportTypesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

