# AttributesApi

All URIs are relative to *https://mybusiness.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mybusinessAttributesList**](AttributesApi.md#mybusinessAttributesList) | **GET** /v4/attributes |  |


<a id="mybusinessAttributesList"></a>
# **mybusinessAttributesList**
> ListAttributeMetadataResponse mybusinessAttributesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, categoryId, country, languageCode, name, pageSize, pageToken)



Returns the list of available attributes that would be available for a location with the given primary category and country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mybusiness.googleapis.com");

    AttributesApi apiInstance = new AttributesApi(defaultClient);
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
    String categoryId = "categoryId_example"; // String | The primary category stable ID to find available attributes.
    String country = "country_example"; // String | The ISO 3166-1 alpha-2 country code to find available attributes.
    String languageCode = "languageCode_example"; // String | The BCP 47 code of language to get attribute display names in. If this language is not available, they will be provided in English.
    String name = "name_example"; // String | Resource name of the location to look up available attributes.
    Integer pageSize = 56; // Integer | How many attributes to include per page. Default is 200, minimum is 1.
    String pageToken = "pageToken_example"; // String | If specified, the next page of attribute metadata is retrieved. The `pageToken` is returned when a call to `attributes.list` returns more results than can fit into the requested page size.
    try {
      ListAttributeMetadataResponse result = apiInstance.mybusinessAttributesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, categoryId, country, languageCode, name, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributesApi#mybusinessAttributesList");
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
| **categoryId** | **String**| The primary category stable ID to find available attributes. | [optional] |
| **country** | **String**| The ISO 3166-1 alpha-2 country code to find available attributes. | [optional] |
| **languageCode** | **String**| The BCP 47 code of language to get attribute display names in. If this language is not available, they will be provided in English. | [optional] |
| **name** | **String**| Resource name of the location to look up available attributes. | [optional] |
| **pageSize** | **Integer**| How many attributes to include per page. Default is 200, minimum is 1. | [optional] |
| **pageToken** | **String**| If specified, the next page of attribute metadata is retrieved. The &#x60;pageToken&#x60; is returned when a call to &#x60;attributes.list&#x60; returns more results than can fit into the requested page size. | [optional] |

### Return type

[**ListAttributeMetadataResponse**](ListAttributeMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

