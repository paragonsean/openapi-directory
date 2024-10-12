# MerchantsupportApi

All URIs are relative to *https://shoppingcontent.googleapis.com/content/v2.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentMerchantsupportRenderaccountissues**](MerchantsupportApi.md#contentMerchantsupportRenderaccountissues) | **POST** /{merchantId}/merchantsupport/renderaccountissues |  |
| [**contentMerchantsupportRenderproductissues**](MerchantsupportApi.md#contentMerchantsupportRenderproductissues) | **POST** /{merchantId}/merchantsupport/renderproductissues/{productId} |  |


<a id="contentMerchantsupportRenderaccountissues"></a>
# **contentMerchantsupportRenderaccountissues**
> RenderAccountIssuesResponse contentMerchantsupportRenderaccountissues(merchantId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, timeZone, renderAccountIssuesRequestPayload)



Provide a list of merchant&#39;s issues with a support content and available actions. This content and actions are meant to be rendered and shown in third-party applications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantsupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://shoppingcontent.googleapis.com/content/v2.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MerchantsupportApi apiInstance = new MerchantsupportApi(defaultClient);
    String merchantId = "merchantId_example"; // String | Required. The ID of the account to fetch issues for.
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
    String languageCode = "languageCode_example"; // String | Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language `en-US`.
    String timeZone = "timeZone_example"; // String | Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example 'America/Los_Angeles'. If not set, results will use as a default UTC.
    RenderAccountIssuesRequestPayload renderAccountIssuesRequestPayload = new RenderAccountIssuesRequestPayload(); // RenderAccountIssuesRequestPayload | 
    try {
      RenderAccountIssuesResponse result = apiInstance.contentMerchantsupportRenderaccountissues(merchantId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, timeZone, renderAccountIssuesRequestPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantsupportApi#contentMerchantsupportRenderaccountissues");
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
| **merchantId** | **String**| Required. The ID of the account to fetch issues for. | |
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
| **languageCode** | **String**| Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language &#x60;en-US&#x60;. | [optional] |
| **timeZone** | **String**| Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example &#39;America/Los_Angeles&#39;. If not set, results will use as a default UTC. | [optional] |
| **renderAccountIssuesRequestPayload** | [**RenderAccountIssuesRequestPayload**](RenderAccountIssuesRequestPayload.md)|  | [optional] |

### Return type

[**RenderAccountIssuesResponse**](RenderAccountIssuesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="contentMerchantsupportRenderproductissues"></a>
# **contentMerchantsupportRenderproductissues**
> RenderProductIssuesResponse contentMerchantsupportRenderproductissues(merchantId, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, timeZone, renderProductIssuesRequestPayload)



Provide a list of issues for merchant&#39;s product with a support content and available actions. This content and actions are meant to be rendered and shown in third-party applications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MerchantsupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://shoppingcontent.googleapis.com/content/v2.1");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MerchantsupportApi apiInstance = new MerchantsupportApi(defaultClient);
    String merchantId = "merchantId_example"; // String | Required. The ID of the account that contains the product.
    String productId = "productId_example"; // String | Required. The [REST_ID](https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.id) of the product to fetch issues for.
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
    String languageCode = "languageCode_example"; // String | Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language `en-US`.
    String timeZone = "timeZone_example"; // String | Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example 'America/Los_Angeles'. If not set, results will use as a default UTC.
    RenderProductIssuesRequestPayload renderProductIssuesRequestPayload = new RenderProductIssuesRequestPayload(); // RenderProductIssuesRequestPayload | 
    try {
      RenderProductIssuesResponse result = apiInstance.contentMerchantsupportRenderproductissues(merchantId, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, timeZone, renderProductIssuesRequestPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MerchantsupportApi#contentMerchantsupportRenderproductissues");
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
| **merchantId** | **String**| Required. The ID of the account that contains the product. | |
| **productId** | **String**| Required. The [REST_ID](https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.id) of the product to fetch issues for. | |
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
| **languageCode** | **String**| Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language &#x60;en-US&#x60;. | [optional] |
| **timeZone** | **String**| Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example &#39;America/Los_Angeles&#39;. If not set, results will use as a default UTC. | [optional] |
| **renderProductIssuesRequestPayload** | [**RenderProductIssuesRequestPayload**](RenderProductIssuesRequestPayload.md)|  | [optional] |

### Return type

[**RenderProductIssuesResponse**](RenderProductIssuesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

