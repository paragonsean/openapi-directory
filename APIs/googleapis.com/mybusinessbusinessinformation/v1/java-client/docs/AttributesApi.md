# AttributesApi

All URIs are relative to *https://mybusinessbusinessinformation.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mybusinessbusinessinformationAttributesList**](AttributesApi.md#mybusinessbusinessinformationAttributesList) | **GET** /v1/attributes |  |


<a id="mybusinessbusinessinformationAttributesList"></a>
# **mybusinessbusinessinformationAttributesList**
> ListAttributeMetadataResponse mybusinessbusinessinformationAttributesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, categoryName, languageCode, pageSize, pageToken, parent, regionCode, showAll)



Returns the list of attributes that would be available for a location with the given primary category and country.

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
    defaultClient.setBasePath("https://mybusinessbusinessinformation.googleapis.com");

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
    String categoryName = "categoryName_example"; // String | The primary category stable ID to find available attributes. Must be of the format categories/{category_id}.
    String languageCode = "languageCode_example"; // String | The BCP 47 code of language to get attribute display names in. If this language is not available, they will be provided in English.
    Integer pageSize = 56; // Integer | How many attributes to include per page. Default is 200, minimum is 1.
    String pageToken = "pageToken_example"; // String | If specified, the next page of attribute metadata is retrieved.
    String parent = "parent_example"; // String | Resource name of the location to look up available attributes. If this field is set, category_name, region_code, language_code and show_all are not required and must not be set.
    String regionCode = "regionCode_example"; // String | The ISO 3166-1 alpha-2 country code to find available attributes.
    Boolean showAll = true; // Boolean | Metadata for all available attributes are returned when this field is set to true, disregarding parent and category_name fields. language_code and region_code are required when show_all is set to true.
    try {
      ListAttributeMetadataResponse result = apiInstance.mybusinessbusinessinformationAttributesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, categoryName, languageCode, pageSize, pageToken, parent, regionCode, showAll);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttributesApi#mybusinessbusinessinformationAttributesList");
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
| **categoryName** | **String**| The primary category stable ID to find available attributes. Must be of the format categories/{category_id}. | [optional] |
| **languageCode** | **String**| The BCP 47 code of language to get attribute display names in. If this language is not available, they will be provided in English. | [optional] |
| **pageSize** | **Integer**| How many attributes to include per page. Default is 200, minimum is 1. | [optional] |
| **pageToken** | **String**| If specified, the next page of attribute metadata is retrieved. | [optional] |
| **parent** | **String**| Resource name of the location to look up available attributes. If this field is set, category_name, region_code, language_code and show_all are not required and must not be set. | [optional] |
| **regionCode** | **String**| The ISO 3166-1 alpha-2 country code to find available attributes. | [optional] |
| **showAll** | **Boolean**| Metadata for all available attributes are returned when this field is set to true, disregarding parent and category_name fields. language_code and region_code are required when show_all is set to true. | [optional] |

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

