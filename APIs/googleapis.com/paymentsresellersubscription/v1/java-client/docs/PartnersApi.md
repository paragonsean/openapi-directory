# PartnersApi

All URIs are relative to *https://paymentsresellersubscription.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentsresellersubscriptionPartnersProductsList**](PartnersApi.md#paymentsresellersubscriptionPartnersProductsList) | **GET** /v1/{parent}/products |  |
| [**paymentsresellersubscriptionPartnersPromotionsFindEligible**](PartnersApi.md#paymentsresellersubscriptionPartnersPromotionsFindEligible) | **POST** /v1/{parent}/promotions:findEligible |  |
| [**paymentsresellersubscriptionPartnersPromotionsList**](PartnersApi.md#paymentsresellersubscriptionPartnersPromotionsList) | **GET** /v1/{parent}/promotions |  |
| [**paymentsresellersubscriptionPartnersSubscriptionsCancel**](PartnersApi.md#paymentsresellersubscriptionPartnersSubscriptionsCancel) | **POST** /v1/{name}:cancel |  |
| [**paymentsresellersubscriptionPartnersSubscriptionsCreate**](PartnersApi.md#paymentsresellersubscriptionPartnersSubscriptionsCreate) | **POST** /v1/{parent}/subscriptions |  |
| [**paymentsresellersubscriptionPartnersSubscriptionsEntitle**](PartnersApi.md#paymentsresellersubscriptionPartnersSubscriptionsEntitle) | **POST** /v1/{name}:entitle |  |
| [**paymentsresellersubscriptionPartnersSubscriptionsExtend**](PartnersApi.md#paymentsresellersubscriptionPartnersSubscriptionsExtend) | **POST** /v1/{name}:extend |  |
| [**paymentsresellersubscriptionPartnersSubscriptionsGet**](PartnersApi.md#paymentsresellersubscriptionPartnersSubscriptionsGet) | **GET** /v1/{name} |  |
| [**paymentsresellersubscriptionPartnersSubscriptionsProvision**](PartnersApi.md#paymentsresellersubscriptionPartnersSubscriptionsProvision) | **POST** /v1/{parent}/subscriptions:provision |  |
| [**paymentsresellersubscriptionPartnersSubscriptionsUndoCancel**](PartnersApi.md#paymentsresellersubscriptionPartnersSubscriptionsUndoCancel) | **POST** /v1/{name}:undoCancel |  |


<a id="paymentsresellersubscriptionPartnersProductsList"></a>
# **paymentsresellersubscriptionPartnersProductsList**
> GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse paymentsresellersubscriptionPartnersProductsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



To retrieve the products that can be resold by the partner. It should be autenticated with a service account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent, the partner that can resell. Format: partners/{partner}
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
    String filter = "filter_example"; // String | Optional. Specifies the filters for the product results. The syntax is defined in https://google.aip.dev/160 with the following caveats: 1. Only the following features are supported: - Logical operator `AND` - Comparison operator `=` (no wildcards `*`) - Traversal operator `.` - Has operator `:` (no wildcards `*`) 2. Only the following fields are supported: - `regionCodes` - `youtubePayload.partnerEligibilityId` - `youtubePayload.postalCode` 3. Unless explicitly mentioned above, other features are not supported. Example: `regionCodes:US AND youtubePayload.postalCode=94043 AND youtubePayload.partnerEligibilityId=eligibility-id`
    Integer pageSize = 56; // Integer | Optional. The maximum number of products to return. The service may return fewer than this value. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    String pageToken = "pageToken_example"; // String | Optional. A page token, received from a previous `ListProducts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListProducts` must match the call that provided the page token.
    try {
      GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse result = apiInstance.paymentsresellersubscriptionPartnersProductsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersProductsList");
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
| **parent** | **String**| Required. The parent, the partner that can resell. Format: partners/{partner} | |
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
| **filter** | **String**| Optional. Specifies the filters for the product results. The syntax is defined in https://google.aip.dev/160 with the following caveats: 1. Only the following features are supported: - Logical operator &#x60;AND&#x60; - Comparison operator &#x60;&#x3D;&#x60; (no wildcards &#x60;*&#x60;) - Traversal operator &#x60;.&#x60; - Has operator &#x60;:&#x60; (no wildcards &#x60;*&#x60;) 2. Only the following fields are supported: - &#x60;regionCodes&#x60; - &#x60;youtubePayload.partnerEligibilityId&#x60; - &#x60;youtubePayload.postalCode&#x60; 3. Unless explicitly mentioned above, other features are not supported. Example: &#x60;regionCodes:US AND youtubePayload.postalCode&#x3D;94043 AND youtubePayload.partnerEligibilityId&#x3D;eligibility-id&#x60; | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of products to return. The service may return fewer than this value. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] |
| **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListProducts&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListProducts&#x60; must match the call that provided the page token. | [optional] |

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse**](GoogleCloudPaymentsResellerSubscriptionV1ListProductsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="paymentsresellersubscriptionPartnersPromotionsFindEligible"></a>
# **paymentsresellersubscriptionPartnersPromotionsFindEligible**
> GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponse paymentsresellersubscriptionPartnersPromotionsFindEligible(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest)



To find eligible promotions for the current user. The API requires user authorization via OAuth. The bare minimum oauth scope &#x60;openid&#x60; is sufficient, which will skip the consent screen.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent, the partner that can resell. Format: partners/{partner}
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
    GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest googleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest = new GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest(); // GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest | 
    try {
      GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponse result = apiInstance.paymentsresellersubscriptionPartnersPromotionsFindEligible(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersPromotionsFindEligible");
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
| **parent** | **String**| Required. The parent, the partner that can resell. Format: partners/{partner} | |
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
| **googleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest** | [**GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest**](GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsRequest.md)|  | [optional] |

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponse**](GoogleCloudPaymentsResellerSubscriptionV1FindEligiblePromotionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="paymentsresellersubscriptionPartnersPromotionsList"></a>
# **paymentsresellersubscriptionPartnersPromotionsList**
> GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse paymentsresellersubscriptionPartnersPromotionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



To retrieve the promotions, such as free trial, that can be used by the partner. It should be autenticated with a service account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent, the partner that can resell. Format: partners/{partner}
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
    String filter = "filter_example"; // String | Optional. Specifies the filters for the promotion results. The syntax is defined in https://google.aip.dev/160 with the following caveats: 1. Only the following features are supported: - Logical operator `AND` - Comparison operator `=` (no wildcards `*`) - Traversal operator `.` - Has operator `:` (no wildcards `*`) 2. Only the following fields are supported: - `applicableProducts` - `regionCodes` - `youtubePayload.partnerEligibilityId` - `youtubePayload.postalCode` 3. Unless explicitly mentioned above, other features are not supported. Example: `applicableProducts:partners/partner1/products/product1 AND regionCodes:US AND youtubePayload.postalCode=94043 AND youtubePayload.partnerEligibilityId=eligibility-id`
    Integer pageSize = 56; // Integer | Optional. The maximum number of promotions to return. The service may return fewer than this value. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    String pageToken = "pageToken_example"; // String | Optional. A page token, received from a previous `ListPromotions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListPromotions` must match the call that provided the page token.
    try {
      GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse result = apiInstance.paymentsresellersubscriptionPartnersPromotionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersPromotionsList");
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
| **parent** | **String**| Required. The parent, the partner that can resell. Format: partners/{partner} | |
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
| **filter** | **String**| Optional. Specifies the filters for the promotion results. The syntax is defined in https://google.aip.dev/160 with the following caveats: 1. Only the following features are supported: - Logical operator &#x60;AND&#x60; - Comparison operator &#x60;&#x3D;&#x60; (no wildcards &#x60;*&#x60;) - Traversal operator &#x60;.&#x60; - Has operator &#x60;:&#x60; (no wildcards &#x60;*&#x60;) 2. Only the following fields are supported: - &#x60;applicableProducts&#x60; - &#x60;regionCodes&#x60; - &#x60;youtubePayload.partnerEligibilityId&#x60; - &#x60;youtubePayload.postalCode&#x60; 3. Unless explicitly mentioned above, other features are not supported. Example: &#x60;applicableProducts:partners/partner1/products/product1 AND regionCodes:US AND youtubePayload.postalCode&#x3D;94043 AND youtubePayload.partnerEligibilityId&#x3D;eligibility-id&#x60; | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of promotions to return. The service may return fewer than this value. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] |
| **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListPromotions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListPromotions&#x60; must match the call that provided the page token. | [optional] |

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse**](GoogleCloudPaymentsResellerSubscriptionV1ListPromotionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="paymentsresellersubscriptionPartnersSubscriptionsCancel"></a>
# **paymentsresellersubscriptionPartnersSubscriptionsCancel**
> GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse paymentsresellersubscriptionPartnersSubscriptionsCancel(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest)



Used by partners to cancel a subscription service either immediately or by the end of the current billing cycle for their customers. It should be called directly by the partner using service accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the subscription resource to be cancelled. It will have the format of \"partners/{partner_id}/subscriptions/{subscription_id}\"
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
    GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest googleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest = new GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest(); // GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest | 
    try {
      GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse result = apiInstance.paymentsresellersubscriptionPartnersSubscriptionsCancel(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersSubscriptionsCancel");
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
| **name** | **String**| Required. The name of the subscription resource to be cancelled. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot; | |
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
| **googleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest** | [**GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest**](GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionRequest.md)|  | [optional] |

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse**](GoogleCloudPaymentsResellerSubscriptionV1CancelSubscriptionResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="paymentsresellersubscriptionPartnersSubscriptionsCreate"></a>
# **paymentsresellersubscriptionPartnersSubscriptionsCreate**
> GoogleCloudPaymentsResellerSubscriptionV1Subscription paymentsresellersubscriptionPartnersSubscriptionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, subscriptionId, googleCloudPaymentsResellerSubscriptionV1Subscription)



Used by partners to create a subscription for their customers. The created subscription is associated with the end user inferred from the end user credentials. This API must be authorized by the end user using OAuth.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent resource name, which is the identifier of the partner. It will have the format of \"partners/{partner_id}\".
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
    String subscriptionId = "subscriptionId_example"; // String | Required. Identifies the subscription resource on the Partner side. The value is restricted to 63 ASCII characters at the maximum. If a subscription was previously created with the same subscription_id, we will directly return that one.
    GoogleCloudPaymentsResellerSubscriptionV1Subscription googleCloudPaymentsResellerSubscriptionV1Subscription = new GoogleCloudPaymentsResellerSubscriptionV1Subscription(); // GoogleCloudPaymentsResellerSubscriptionV1Subscription | 
    try {
      GoogleCloudPaymentsResellerSubscriptionV1Subscription result = apiInstance.paymentsresellersubscriptionPartnersSubscriptionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, subscriptionId, googleCloudPaymentsResellerSubscriptionV1Subscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersSubscriptionsCreate");
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
| **parent** | **String**| Required. The parent resource name, which is the identifier of the partner. It will have the format of \&quot;partners/{partner_id}\&quot;. | |
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
| **subscriptionId** | **String**| Required. Identifies the subscription resource on the Partner side. The value is restricted to 63 ASCII characters at the maximum. If a subscription was previously created with the same subscription_id, we will directly return that one. | [optional] |
| **googleCloudPaymentsResellerSubscriptionV1Subscription** | [**GoogleCloudPaymentsResellerSubscriptionV1Subscription**](GoogleCloudPaymentsResellerSubscriptionV1Subscription.md)|  | [optional] |

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1Subscription**](GoogleCloudPaymentsResellerSubscriptionV1Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="paymentsresellersubscriptionPartnersSubscriptionsEntitle"></a>
# **paymentsresellersubscriptionPartnersSubscriptionsEntitle**
> GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponse paymentsresellersubscriptionPartnersSubscriptionsEntitle(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest)



Used by partners to entitle a previously provisioned subscription to the current end user. The end user identity is inferred from the authorized credential of the request. This API must be authorized by the end user using OAuth.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the subscription resource that is entitled to the current end user. It will have the format of \"partners/{partner_id}/subscriptions/{subscription_id}\"
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
    GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest googleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest = new GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest(); // GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest | 
    try {
      GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponse result = apiInstance.paymentsresellersubscriptionPartnersSubscriptionsEntitle(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersSubscriptionsEntitle");
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
| **name** | **String**| Required. The name of the subscription resource that is entitled to the current end user. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot; | |
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
| **googleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest** | [**GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest**](GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequest.md)|  | [optional] |

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponse**](GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="paymentsresellersubscriptionPartnersSubscriptionsExtend"></a>
# **paymentsresellersubscriptionPartnersSubscriptionsExtend**
> GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponse paymentsresellersubscriptionPartnersSubscriptionsExtend(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest)



[Opt-in only] Most partners should be on auto-extend by default. Used by partners to extend a subscription service for their customers on an ongoing basis for the subscription to remain active and renewable. It should be called directly by the partner using service accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the subscription resource to be extended. It will have the format of \"partners/{partner_id}/subscriptions/{subscription_id}\".
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
    GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest googleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest = new GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest(); // GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest | 
    try {
      GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponse result = apiInstance.paymentsresellersubscriptionPartnersSubscriptionsExtend(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersSubscriptionsExtend");
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
| **name** | **String**| Required. The name of the subscription resource to be extended. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot;. | |
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
| **googleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest** | [**GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest**](GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest.md)|  | [optional] |

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponse**](GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="paymentsresellersubscriptionPartnersSubscriptionsGet"></a>
# **paymentsresellersubscriptionPartnersSubscriptionsGet**
> GoogleCloudPaymentsResellerSubscriptionV1Subscription paymentsresellersubscriptionPartnersSubscriptionsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Used by partners to get a subscription by id. It should be called directly by the partner using service accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the subscription resource to retrieve. It will have the format of \"partners/{partner_id}/subscriptions/{subscription_id}\"
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
    try {
      GoogleCloudPaymentsResellerSubscriptionV1Subscription result = apiInstance.paymentsresellersubscriptionPartnersSubscriptionsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersSubscriptionsGet");
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
| **name** | **String**| Required. The name of the subscription resource to retrieve. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot; | |
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

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1Subscription**](GoogleCloudPaymentsResellerSubscriptionV1Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="paymentsresellersubscriptionPartnersSubscriptionsProvision"></a>
# **paymentsresellersubscriptionPartnersSubscriptionsProvision**
> GoogleCloudPaymentsResellerSubscriptionV1Subscription paymentsresellersubscriptionPartnersSubscriptionsProvision(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, subscriptionId, googleCloudPaymentsResellerSubscriptionV1Subscription)



Used by partners to provision a subscription for their customers. This creates a subscription without associating it with the end user account. EntitleSubscription must be called separately using OAuth in order for the end user account to be associated with the subscription. It should be called directly by the partner using service accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent resource name, which is the identifier of the partner. It will have the format of \"partners/{partner_id}\".
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
    String subscriptionId = "subscriptionId_example"; // String | Required. Identifies the subscription resource on the Partner side. The value is restricted to 63 ASCII characters at the maximum. If a subscription was previously created with the same subscription_id, we will directly return that one.
    GoogleCloudPaymentsResellerSubscriptionV1Subscription googleCloudPaymentsResellerSubscriptionV1Subscription = new GoogleCloudPaymentsResellerSubscriptionV1Subscription(); // GoogleCloudPaymentsResellerSubscriptionV1Subscription | 
    try {
      GoogleCloudPaymentsResellerSubscriptionV1Subscription result = apiInstance.paymentsresellersubscriptionPartnersSubscriptionsProvision(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, subscriptionId, googleCloudPaymentsResellerSubscriptionV1Subscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersSubscriptionsProvision");
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
| **parent** | **String**| Required. The parent resource name, which is the identifier of the partner. It will have the format of \&quot;partners/{partner_id}\&quot;. | |
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
| **subscriptionId** | **String**| Required. Identifies the subscription resource on the Partner side. The value is restricted to 63 ASCII characters at the maximum. If a subscription was previously created with the same subscription_id, we will directly return that one. | [optional] |
| **googleCloudPaymentsResellerSubscriptionV1Subscription** | [**GoogleCloudPaymentsResellerSubscriptionV1Subscription**](GoogleCloudPaymentsResellerSubscriptionV1Subscription.md)|  | [optional] |

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1Subscription**](GoogleCloudPaymentsResellerSubscriptionV1Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="paymentsresellersubscriptionPartnersSubscriptionsUndoCancel"></a>
# **paymentsresellersubscriptionPartnersSubscriptionsUndoCancel**
> GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponse paymentsresellersubscriptionPartnersSubscriptionsUndoCancel(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body)



Used by partners to revoke the pending cancellation of a subscription, which is currently in &#x60;STATE_CANCEL_AT_END_OF_CYCLE&#x60; state. If the subscription is already cancelled, the request will fail. It should be called directly by the partner using service accounts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://paymentsresellersubscription.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PartnersApi apiInstance = new PartnersApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the subscription resource whose pending cancellation needs to be undone. It will have the format of \"partners/{partner_id}/subscriptions/{subscription_id}\"
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
    Object body = null; // Object | 
    try {
      GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponse result = apiInstance.paymentsresellersubscriptionPartnersSubscriptionsUndoCancel(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartnersApi#paymentsresellersubscriptionPartnersSubscriptionsUndoCancel");
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
| **name** | **String**| Required. The name of the subscription resource whose pending cancellation needs to be undone. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot; | |
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
| **body** | **Object**|  | [optional] |

### Return type

[**GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponse**](GoogleCloudPaymentsResellerSubscriptionV1UndoCancelSubscriptionResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

