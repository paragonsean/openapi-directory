# MonetizationApi

All URIs are relative to *https://androidpublisher.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**androidpublisherMonetizationConvertRegionPrices**](MonetizationApi.md#androidpublisherMonetizationConvertRegionPrices) | **POST** /androidpublisher/v3/applications/{packageName}/pricing:convertRegionPrices |  |
| [**androidpublisherMonetizationSubscriptionsArchive**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsArchive) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}:archive |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansActivate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansActivate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:activate |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans:batchMigratePrices |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans:batchUpdateStates |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansDeactivate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansDeactivate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:deactivate |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansDelete**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansDelete) | **DELETE** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId} |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansMigratePrices**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansMigratePrices) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:migratePrices |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersActivate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersActivate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:activate |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers:batchGet |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers:batchUpdate |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers:batchUpdateStates |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersCreate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersCreate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:deactivate |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersDelete**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersDelete) | **DELETE** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId} |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersGet**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersGet) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId} |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersList**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersList) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers |  |
| [**androidpublisherMonetizationSubscriptionsBasePlansOffersPatch**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersPatch) | **PATCH** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId} |  |
| [**androidpublisherMonetizationSubscriptionsBatchGet**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBatchGet) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions:batchGet |  |
| [**androidpublisherMonetizationSubscriptionsBatchUpdate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBatchUpdate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions:batchUpdate |  |
| [**androidpublisherMonetizationSubscriptionsCreate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsCreate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions |  |
| [**androidpublisherMonetizationSubscriptionsDelete**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsDelete) | **DELETE** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId} |  |
| [**androidpublisherMonetizationSubscriptionsGet**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsGet) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId} |  |
| [**androidpublisherMonetizationSubscriptionsList**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsList) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions |  |
| [**androidpublisherMonetizationSubscriptionsPatch**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsPatch) | **PATCH** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId} |  |


<a id="androidpublisherMonetizationConvertRegionPrices"></a>
# **androidpublisherMonetizationConvertRegionPrices**
> ConvertRegionPricesResponse androidpublisherMonetizationConvertRegionPrices(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, convertRegionPricesRequest)



Calculates the region prices, using today&#39;s exchange rate and country-specific pricing patterns, based on the price in the request for a set of regions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The app package name.
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
    ConvertRegionPricesRequest convertRegionPricesRequest = new ConvertRegionPricesRequest(); // ConvertRegionPricesRequest | 
    try {
      ConvertRegionPricesResponse result = apiInstance.androidpublisherMonetizationConvertRegionPrices(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, convertRegionPricesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationConvertRegionPrices");
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
| **packageName** | **String**| Required. The app package name. | |
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
| **convertRegionPricesRequest** | [**ConvertRegionPricesRequest**](ConvertRegionPricesRequest.md)|  | [optional] |

### Return type

[**ConvertRegionPricesResponse**](ConvertRegionPricesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsArchive"></a>
# **androidpublisherMonetizationSubscriptionsArchive**
> Subscription androidpublisherMonetizationSubscriptionsArchive(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body)



Deprecated: subscription archiving is not supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the app of the subscription to delete.
    String productId = "productId_example"; // String | Required. The unique product ID of the subscription to delete.
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
      Subscription result = apiInstance.androidpublisherMonetizationSubscriptionsArchive(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsArchive");
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
| **packageName** | **String**| Required. The parent app (package name) of the app of the subscription to delete. | |
| **productId** | **String**| Required. The unique product ID of the subscription to delete. | |
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

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansActivate"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansActivate**
> Subscription androidpublisherMonetizationSubscriptionsBasePlansActivate(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, activateBasePlanRequest)



Activates a base plan. Once activated, base plans will be available to new subscribers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the base plan to activate.
    String productId = "productId_example"; // String | Required. The parent subscription (ID) of the base plan to activate.
    String basePlanId = "basePlanId_example"; // String | Required. The unique base plan ID of the base plan to activate.
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
    ActivateBasePlanRequest activateBasePlanRequest = new ActivateBasePlanRequest(); // ActivateBasePlanRequest | 
    try {
      Subscription result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansActivate(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, activateBasePlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansActivate");
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
| **packageName** | **String**| Required. The parent app (package name) of the base plan to activate. | |
| **productId** | **String**| Required. The parent subscription (ID) of the base plan to activate. | |
| **basePlanId** | **String**| Required. The unique base plan ID of the base plan to activate. | |
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
| **activateBasePlanRequest** | [**ActivateBasePlanRequest**](ActivateBasePlanRequest.md)|  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices**
> BatchMigrateBasePlanPricesResponse androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchMigrateBasePlanPricesRequest)



Batch variant of the MigrateBasePlanPrices endpoint. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the Subscription resources.
    String productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \"-\". Must be set.
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
    BatchMigrateBasePlanPricesRequest batchMigrateBasePlanPricesRequest = new BatchMigrateBasePlanPricesRequest(); // BatchMigrateBasePlanPricesRequest | 
    try {
      BatchMigrateBasePlanPricesResponse result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchMigrateBasePlanPricesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices");
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
| **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the Subscription resources. | |
| **productId** | **String**| Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | |
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
| **batchMigrateBasePlanPricesRequest** | [**BatchMigrateBasePlanPricesRequest**](BatchMigrateBasePlanPricesRequest.md)|  | [optional] |

### Return type

[**BatchMigrateBasePlanPricesResponse**](BatchMigrateBasePlanPricesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates**
> BatchUpdateBasePlanStatesResponse androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchUpdateBasePlanStatesRequest)



Activates or deactivates base plans across one or multiple subscriptions. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the updated base plans.
    String productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated base plans belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \"-\". Must be set.
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
    BatchUpdateBasePlanStatesRequest batchUpdateBasePlanStatesRequest = new BatchUpdateBasePlanStatesRequest(); // BatchUpdateBasePlanStatesRequest | 
    try {
      BatchUpdateBasePlanStatesResponse result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchUpdateBasePlanStatesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates");
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
| **packageName** | **String**| Required. The parent app (package name) of the updated base plans. | |
| **productId** | **String**| Required. The product ID of the parent subscription, if all updated base plans belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | |
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
| **batchUpdateBasePlanStatesRequest** | [**BatchUpdateBasePlanStatesRequest**](BatchUpdateBasePlanStatesRequest.md)|  | [optional] |

### Return type

[**BatchUpdateBasePlanStatesResponse**](BatchUpdateBasePlanStatesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansDeactivate"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansDeactivate**
> Subscription androidpublisherMonetizationSubscriptionsBasePlansDeactivate(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, deactivateBasePlanRequest)



Deactivates a base plan. Once deactivated, the base plan will become unavailable to new subscribers, but existing subscribers will maintain their subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the base plan to deactivate.
    String productId = "productId_example"; // String | Required. The parent subscription (ID) of the base plan to deactivate.
    String basePlanId = "basePlanId_example"; // String | Required. The unique base plan ID of the base plan to deactivate.
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
    DeactivateBasePlanRequest deactivateBasePlanRequest = new DeactivateBasePlanRequest(); // DeactivateBasePlanRequest | 
    try {
      Subscription result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansDeactivate(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, deactivateBasePlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansDeactivate");
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
| **packageName** | **String**| Required. The parent app (package name) of the base plan to deactivate. | |
| **productId** | **String**| Required. The parent subscription (ID) of the base plan to deactivate. | |
| **basePlanId** | **String**| Required. The unique base plan ID of the base plan to deactivate. | |
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
| **deactivateBasePlanRequest** | [**DeactivateBasePlanRequest**](DeactivateBasePlanRequest.md)|  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansDelete"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansDelete**
> androidpublisherMonetizationSubscriptionsBasePlansDelete(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Deletes a base plan. Can only be done for draft base plans. This action is irreversible.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the base plan to delete.
    String productId = "productId_example"; // String | Required. The parent subscription (ID) of the base plan to delete.
    String basePlanId = "basePlanId_example"; // String | Required. The unique offer ID of the base plan to delete.
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
      apiInstance.androidpublisherMonetizationSubscriptionsBasePlansDelete(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansDelete");
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
| **packageName** | **String**| Required. The parent app (package name) of the base plan to delete. | |
| **productId** | **String**| Required. The parent subscription (ID) of the base plan to delete. | |
| **basePlanId** | **String**| Required. The unique offer ID of the base plan to delete. | |
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

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansMigratePrices"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansMigratePrices**
> Object androidpublisherMonetizationSubscriptionsBasePlansMigratePrices(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, migrateBasePlanPricesRequest)



Migrates subscribers who are receiving an historical subscription price to the currently-offered price for the specified region. Requests will cause price change notifications to be sent to users who are currently receiving an historical price older than the supplied timestamp. Subscribers who do not agree to the new price will have their subscription ended at the next renewal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. Package name of the parent app. Must be equal to the package_name field on the Subscription resource.
    String productId = "productId_example"; // String | Required. The ID of the subscription to update. Must be equal to the product_id field on the Subscription resource.
    String basePlanId = "basePlanId_example"; // String | Required. The unique base plan ID of the base plan to update prices on.
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
    MigrateBasePlanPricesRequest migrateBasePlanPricesRequest = new MigrateBasePlanPricesRequest(); // MigrateBasePlanPricesRequest | 
    try {
      Object result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansMigratePrices(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, migrateBasePlanPricesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansMigratePrices");
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
| **packageName** | **String**| Required. Package name of the parent app. Must be equal to the package_name field on the Subscription resource. | |
| **productId** | **String**| Required. The ID of the subscription to update. Must be equal to the product_id field on the Subscription resource. | |
| **basePlanId** | **String**| Required. The unique base plan ID of the base plan to update prices on. | |
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
| **migrateBasePlanPricesRequest** | [**MigrateBasePlanPricesRequest**](MigrateBasePlanPricesRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersActivate"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersActivate**
> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersActivate(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, activateSubscriptionOfferRequest)



Activates a subscription offer. Once activated, subscription offers will be available to new subscribers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the offer to activate.
    String productId = "productId_example"; // String | Required. The parent subscription (ID) of the offer to activate.
    String basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) of the offer to activate.
    String offerId = "offerId_example"; // String | Required. The unique offer ID of the offer to activate.
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
    ActivateSubscriptionOfferRequest activateSubscriptionOfferRequest = new ActivateSubscriptionOfferRequest(); // ActivateSubscriptionOfferRequest | 
    try {
      SubscriptionOffer result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersActivate(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, activateSubscriptionOfferRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersActivate");
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
| **packageName** | **String**| Required. The parent app (package name) of the offer to activate. | |
| **productId** | **String**| Required. The parent subscription (ID) of the offer to activate. | |
| **basePlanId** | **String**| Required. The parent base plan (ID) of the offer to activate. | |
| **offerId** | **String**| Required. The unique offer ID of the offer to activate. | |
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
| **activateSubscriptionOfferRequest** | [**ActivateSubscriptionOfferRequest**](ActivateSubscriptionOfferRequest.md)|  | [optional] |

### Return type

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet**
> BatchGetSubscriptionOffersResponse androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchGetSubscriptionOffersRequest)



Reads one or more subscription offers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the requests.
    String productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \"-\". Must be set.
    String basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offers should be read. May be specified as '-' to read offers from multiple base plans.
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
    BatchGetSubscriptionOffersRequest batchGetSubscriptionOffersRequest = new BatchGetSubscriptionOffersRequest(); // BatchGetSubscriptionOffersRequest | 
    try {
      BatchGetSubscriptionOffersResponse result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchGetSubscriptionOffersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet");
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
| **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the requests. | |
| **productId** | **String**| Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | |
| **basePlanId** | **String**| Required. The parent base plan (ID) for which the offers should be read. May be specified as &#39;-&#39; to read offers from multiple base plans. | |
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
| **batchGetSubscriptionOffersRequest** | [**BatchGetSubscriptionOffersRequest**](BatchGetSubscriptionOffersRequest.md)|  | [optional] |

### Return type

[**BatchGetSubscriptionOffersResponse**](BatchGetSubscriptionOffersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate**
> BatchUpdateSubscriptionOffersResponse androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchUpdateSubscriptionOffersRequest)



Updates a batch of subscription offers. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources.
    String productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \"-\". Must be set.
    String basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offers should be updated. May be specified as '-' to update offers from multiple base plans.
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
    BatchUpdateSubscriptionOffersRequest batchUpdateSubscriptionOffersRequest = new BatchUpdateSubscriptionOffersRequest(); // BatchUpdateSubscriptionOffersRequest | 
    try {
      BatchUpdateSubscriptionOffersResponse result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchUpdateSubscriptionOffersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate");
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
| **packageName** | **String**| Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources. | |
| **productId** | **String**| Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | |
| **basePlanId** | **String**| Required. The parent base plan (ID) for which the offers should be updated. May be specified as &#39;-&#39; to update offers from multiple base plans. | |
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
| **batchUpdateSubscriptionOffersRequest** | [**BatchUpdateSubscriptionOffersRequest**](BatchUpdateSubscriptionOffersRequest.md)|  | [optional] |

### Return type

[**BatchUpdateSubscriptionOffersResponse**](BatchUpdateSubscriptionOffersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates**
> BatchUpdateSubscriptionOfferStatesResponse androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchUpdateSubscriptionOfferStatesRequest)



Updates a batch of subscription offer states. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources.
    String productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \"-\". Must be set.
    String basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offers should be updated. May be specified as '-' to update offers from multiple base plans.
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
    BatchUpdateSubscriptionOfferStatesRequest batchUpdateSubscriptionOfferStatesRequest = new BatchUpdateSubscriptionOfferStatesRequest(); // BatchUpdateSubscriptionOfferStatesRequest | 
    try {
      BatchUpdateSubscriptionOfferStatesResponse result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchUpdateSubscriptionOfferStatesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates");
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
| **packageName** | **String**| Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources. | |
| **productId** | **String**| Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | |
| **basePlanId** | **String**| Required. The parent base plan (ID) for which the offers should be updated. May be specified as &#39;-&#39; to update offers from multiple base plans. | |
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
| **batchUpdateSubscriptionOfferStatesRequest** | [**BatchUpdateSubscriptionOfferStatesRequest**](BatchUpdateSubscriptionOfferStatesRequest.md)|  | [optional] |

### Return type

[**BatchUpdateSubscriptionOfferStatesResponse**](BatchUpdateSubscriptionOfferStatesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersCreate"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersCreate**
> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersCreate(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, offerId, regionsVersionVersion, subscriptionOffer)



Creates a new subscription offer. Only auto-renewing base plans can have subscription offers. The offer state will be DRAFT until it is activated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) for which the offer should be created. Must be equal to the package_name field on the Subscription resource.
    String productId = "productId_example"; // String | Required. The parent subscription (ID) for which the offer should be created. Must be equal to the product_id field on the SubscriptionOffer resource.
    String basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offer should be created. Must be equal to the base_plan_id field on the SubscriptionOffer resource.
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
    String offerId = "offerId_example"; // String | Required. The ID to use for the offer. For the requirements on this format, see the documentation of the offer_id field on the SubscriptionOffer resource.
    String regionsVersionVersion = "regionsVersionVersion_example"; // String | Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
    SubscriptionOffer subscriptionOffer = new SubscriptionOffer(); // SubscriptionOffer | 
    try {
      SubscriptionOffer result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersCreate(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, offerId, regionsVersionVersion, subscriptionOffer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersCreate");
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
| **packageName** | **String**| Required. The parent app (package name) for which the offer should be created. Must be equal to the package_name field on the Subscription resource. | |
| **productId** | **String**| Required. The parent subscription (ID) for which the offer should be created. Must be equal to the product_id field on the SubscriptionOffer resource. | |
| **basePlanId** | **String**| Required. The parent base plan (ID) for which the offer should be created. Must be equal to the base_plan_id field on the SubscriptionOffer resource. | |
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
| **offerId** | **String**| Required. The ID to use for the offer. For the requirements on this format, see the documentation of the offer_id field on the SubscriptionOffer resource. | [optional] |
| **regionsVersionVersion** | **String**| Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02. | [optional] |
| **subscriptionOffer** | [**SubscriptionOffer**](SubscriptionOffer.md)|  | [optional] |

### Return type

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate**
> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, deactivateSubscriptionOfferRequest)



Deactivates a subscription offer. Once deactivated, existing subscribers will maintain their subscription, but the offer will become unavailable to new subscribers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the offer to deactivate.
    String productId = "productId_example"; // String | Required. The parent subscription (ID) of the offer to deactivate.
    String basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) of the offer to deactivate.
    String offerId = "offerId_example"; // String | Required. The unique offer ID of the offer to deactivate.
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
    DeactivateSubscriptionOfferRequest deactivateSubscriptionOfferRequest = new DeactivateSubscriptionOfferRequest(); // DeactivateSubscriptionOfferRequest | 
    try {
      SubscriptionOffer result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, deactivateSubscriptionOfferRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate");
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
| **packageName** | **String**| Required. The parent app (package name) of the offer to deactivate. | |
| **productId** | **String**| Required. The parent subscription (ID) of the offer to deactivate. | |
| **basePlanId** | **String**| Required. The parent base plan (ID) of the offer to deactivate. | |
| **offerId** | **String**| Required. The unique offer ID of the offer to deactivate. | |
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
| **deactivateSubscriptionOfferRequest** | [**DeactivateSubscriptionOfferRequest**](DeactivateSubscriptionOfferRequest.md)|  | [optional] |

### Return type

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersDelete"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersDelete**
> androidpublisherMonetizationSubscriptionsBasePlansOffersDelete(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Deletes a subscription offer. Can only be done for draft offers. This action is irreversible.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the offer to delete.
    String productId = "productId_example"; // String | Required. The parent subscription (ID) of the offer to delete.
    String basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) of the offer to delete.
    String offerId = "offerId_example"; // String | Required. The unique offer ID of the offer to delete.
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
      apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersDelete(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersDelete");
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
| **packageName** | **String**| Required. The parent app (package name) of the offer to delete. | |
| **productId** | **String**| Required. The parent subscription (ID) of the offer to delete. | |
| **basePlanId** | **String**| Required. The parent base plan (ID) of the offer to delete. | |
| **offerId** | **String**| Required. The unique offer ID of the offer to delete. | |
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

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersGet"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersGet**
> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersGet(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Reads a single offer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the offer to get.
    String productId = "productId_example"; // String | Required. The parent subscription (ID) of the offer to get.
    String basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) of the offer to get.
    String offerId = "offerId_example"; // String | Required. The unique offer ID of the offer to get.
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
      SubscriptionOffer result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersGet(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersGet");
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
| **packageName** | **String**| Required. The parent app (package name) of the offer to get. | |
| **productId** | **String**| Required. The parent subscription (ID) of the offer to get. | |
| **basePlanId** | **String**| Required. The parent base plan (ID) of the offer to get. | |
| **offerId** | **String**| Required. The unique offer ID of the offer to get. | |
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

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersList"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersList**
> ListSubscriptionOffersResponse androidpublisherMonetizationSubscriptionsBasePlansOffersList(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Lists all offers under a given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be read.
    String productId = "productId_example"; // String | Required. The parent subscription (ID) for which the offers should be read. May be specified as '-' to read all offers under an app.
    String basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offers should be read. May be specified as '-' to read all offers under a subscription or an app. Must be specified as '-' if product_id is specified as '-'.
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
    Integer pageSize = 56; // Integer | The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous `ListSubscriptionsOffers` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSubscriptionOffers` must match the call that provided the page token.
    try {
      ListSubscriptionOffersResponse result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersList(packageName, productId, basePlanId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersList");
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
| **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be read. | |
| **productId** | **String**| Required. The parent subscription (ID) for which the offers should be read. May be specified as &#39;-&#39; to read all offers under an app. | |
| **basePlanId** | **String**| Required. The parent base plan (ID) for which the offers should be read. May be specified as &#39;-&#39; to read all offers under a subscription or an app. Must be specified as &#39;-&#39; if product_id is specified as &#39;-&#39;. | |
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
| **pageSize** | **Integer**| The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] |
| **pageToken** | **String**| A page token, received from a previous &#x60;ListSubscriptionsOffers&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListSubscriptionOffers&#x60; must match the call that provided the page token. | [optional] |

### Return type

[**ListSubscriptionOffersResponse**](ListSubscriptionOffersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBasePlansOffersPatch"></a>
# **androidpublisherMonetizationSubscriptionsBasePlansOffersPatch**
> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersPatch(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, latencyTolerance, regionsVersionVersion, updateMask, subscriptionOffer)



Updates an existing subscription offer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. Immutable. The package name of the app the parent subscription belongs to.
    String productId = "productId_example"; // String | Required. Immutable. The ID of the parent subscription this offer belongs to.
    String basePlanId = "basePlanId_example"; // String | Required. Immutable. The ID of the base plan to which this offer is an extension.
    String offerId = "offerId_example"; // String | Required. Immutable. Unique ID of this subscription offer. Must be unique within the base plan.
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
    Boolean allowMissing = true; // Boolean | Optional. If set to true, and the subscription offer with the given package_name, product_id, base_plan_id and offer_id doesn't exist, an offer will be created. If a new offer is created, update_mask is ignored.
    String latencyTolerance = "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"; // String | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.
    String regionsVersionVersion = "regionsVersionVersion_example"; // String | Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
    String updateMask = "updateMask_example"; // String | Required. The list of fields to be updated.
    SubscriptionOffer subscriptionOffer = new SubscriptionOffer(); // SubscriptionOffer | 
    try {
      SubscriptionOffer result = apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersPatch(packageName, productId, basePlanId, offerId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, latencyTolerance, regionsVersionVersion, updateMask, subscriptionOffer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBasePlansOffersPatch");
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
| **packageName** | **String**| Required. Immutable. The package name of the app the parent subscription belongs to. | |
| **productId** | **String**| Required. Immutable. The ID of the parent subscription this offer belongs to. | |
| **basePlanId** | **String**| Required. Immutable. The ID of the base plan to which this offer is an extension. | |
| **offerId** | **String**| Required. Immutable. Unique ID of this subscription offer. Must be unique within the base plan. | |
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
| **allowMissing** | **Boolean**| Optional. If set to true, and the subscription offer with the given package_name, product_id, base_plan_id and offer_id doesn&#39;t exist, an offer will be created. If a new offer is created, update_mask is ignored. | [optional] |
| **latencyTolerance** | **String**| Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. | [optional] [enum: PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED, PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE, PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT] |
| **regionsVersionVersion** | **String**| Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02. | [optional] |
| **updateMask** | **String**| Required. The list of fields to be updated. | [optional] |
| **subscriptionOffer** | [**SubscriptionOffer**](SubscriptionOffer.md)|  | [optional] |

### Return type

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBatchGet"></a>
# **androidpublisherMonetizationSubscriptionsBatchGet**
> BatchGetSubscriptionsResponse androidpublisherMonetizationSubscriptionsBatchGet(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, productIds)



Reads one or more subscriptions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be retrieved. Must be equal to the package_name field on all the requests.
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
    List<String> productIds = Arrays.asList(); // List<String> | Required. A list of up to 100 subscription product IDs to retrieve. All the IDs must be different.
    try {
      BatchGetSubscriptionsResponse result = apiInstance.androidpublisherMonetizationSubscriptionsBatchGet(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, productIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBatchGet");
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
| **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be retrieved. Must be equal to the package_name field on all the requests. | |
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
| **productIds** | [**List&lt;String&gt;**](String.md)| Required. A list of up to 100 subscription product IDs to retrieve. All the IDs must be different. | [optional] |

### Return type

[**BatchGetSubscriptionsResponse**](BatchGetSubscriptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsBatchUpdate"></a>
# **androidpublisherMonetizationSubscriptionsBatchUpdate**
> BatchUpdateSubscriptionsResponse androidpublisherMonetizationSubscriptionsBatchUpdate(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchUpdateSubscriptionsRequest)



Updates a batch of subscriptions. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be updated. Must be equal to the package_name field on all the Subscription resources.
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
    BatchUpdateSubscriptionsRequest batchUpdateSubscriptionsRequest = new BatchUpdateSubscriptionsRequest(); // BatchUpdateSubscriptionsRequest | 
    try {
      BatchUpdateSubscriptionsResponse result = apiInstance.androidpublisherMonetizationSubscriptionsBatchUpdate(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, batchUpdateSubscriptionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsBatchUpdate");
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
| **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be updated. Must be equal to the package_name field on all the Subscription resources. | |
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
| **batchUpdateSubscriptionsRequest** | [**BatchUpdateSubscriptionsRequest**](BatchUpdateSubscriptionsRequest.md)|  | [optional] |

### Return type

[**BatchUpdateSubscriptionsResponse**](BatchUpdateSubscriptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsCreate"></a>
# **androidpublisherMonetizationSubscriptionsCreate**
> Subscription androidpublisherMonetizationSubscriptionsCreate(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, productId, regionsVersionVersion, subscription)



Creates a new subscription. Newly added base plans will remain in draft state until activated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscription should be created. Must be equal to the package_name field on the Subscription resource.
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
    String productId = "productId_example"; // String | Required. The ID to use for the subscription. For the requirements on this format, see the documentation of the product_id field on the Subscription resource.
    String regionsVersionVersion = "regionsVersionVersion_example"; // String | Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
    Subscription subscription = new Subscription(); // Subscription | 
    try {
      Subscription result = apiInstance.androidpublisherMonetizationSubscriptionsCreate(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, productId, regionsVersionVersion, subscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsCreate");
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
| **packageName** | **String**| Required. The parent app (package name) for which the subscription should be created. Must be equal to the package_name field on the Subscription resource. | |
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
| **productId** | **String**| Required. The ID to use for the subscription. For the requirements on this format, see the documentation of the product_id field on the Subscription resource. | [optional] |
| **regionsVersionVersion** | **String**| Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02. | [optional] |
| **subscription** | [**Subscription**](Subscription.md)|  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsDelete"></a>
# **androidpublisherMonetizationSubscriptionsDelete**
> androidpublisherMonetizationSubscriptionsDelete(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Deletes a subscription. A subscription can only be deleted if it has never had a base plan published.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the app of the subscription to delete.
    String productId = "productId_example"; // String | Required. The unique product ID of the subscription to delete.
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
      apiInstance.androidpublisherMonetizationSubscriptionsDelete(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsDelete");
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
| **packageName** | **String**| Required. The parent app (package name) of the app of the subscription to delete. | |
| **productId** | **String**| Required. The unique product ID of the subscription to delete. | |
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

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsGet"></a>
# **androidpublisherMonetizationSubscriptionsGet**
> Subscription androidpublisherMonetizationSubscriptionsGet(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Reads a single subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) of the subscription to get.
    String productId = "productId_example"; // String | Required. The unique product ID of the subscription to get.
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
      Subscription result = apiInstance.androidpublisherMonetizationSubscriptionsGet(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsGet");
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
| **packageName** | **String**| Required. The parent app (package name) of the subscription to get. | |
| **productId** | **String**| Required. The unique product ID of the subscription to get. | |
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

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsList"></a>
# **androidpublisherMonetizationSubscriptionsList**
> ListSubscriptionsResponse androidpublisherMonetizationSubscriptionsList(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, showArchived)



Lists all subscriptions under a given app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be read.
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
    Integer pageSize = 56; // Integer | The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous `ListSubscriptions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSubscriptions` must match the call that provided the page token.
    Boolean showArchived = true; // Boolean | Deprecated: subscription archiving is not supported.
    try {
      ListSubscriptionsResponse result = apiInstance.androidpublisherMonetizationSubscriptionsList(packageName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, showArchived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsList");
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
| **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be read. | |
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
| **pageSize** | **Integer**| The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] |
| **pageToken** | **String**| A page token, received from a previous &#x60;ListSubscriptions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListSubscriptions&#x60; must match the call that provided the page token. | [optional] |
| **showArchived** | **Boolean**| Deprecated: subscription archiving is not supported. | [optional] |

### Return type

[**ListSubscriptionsResponse**](ListSubscriptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="androidpublisherMonetizationSubscriptionsPatch"></a>
# **androidpublisherMonetizationSubscriptionsPatch**
> Subscription androidpublisherMonetizationSubscriptionsPatch(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, latencyTolerance, regionsVersionVersion, updateMask, subscription)



Updates an existing subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonetizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://androidpublisher.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MonetizationApi apiInstance = new MonetizationApi(defaultClient);
    String packageName = "packageName_example"; // String | Immutable. Package name of the parent app.
    String productId = "productId_example"; // String | Immutable. Unique product ID of the product. Unique within the parent app. Product IDs must be composed of lower-case letters (a-z), numbers (0-9), underscores (_) and dots (.). It must start with a lower-case letter or number, and be between 1 and 40 (inclusive) characters in length.
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
    Boolean allowMissing = true; // Boolean | Optional. If set to true, and the subscription with the given package_name and product_id doesn't exist, the subscription will be created. If a new subscription is created, update_mask is ignored.
    String latencyTolerance = "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED"; // String | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.
    String regionsVersionVersion = "regionsVersionVersion_example"; // String | Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
    String updateMask = "updateMask_example"; // String | Required. The list of fields to be updated.
    Subscription subscription = new Subscription(); // Subscription | 
    try {
      Subscription result = apiInstance.androidpublisherMonetizationSubscriptionsPatch(packageName, productId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, latencyTolerance, regionsVersionVersion, updateMask, subscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonetizationApi#androidpublisherMonetizationSubscriptionsPatch");
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
| **packageName** | **String**| Immutable. Package name of the parent app. | |
| **productId** | **String**| Immutable. Unique product ID of the product. Unique within the parent app. Product IDs must be composed of lower-case letters (a-z), numbers (0-9), underscores (_) and dots (.). It must start with a lower-case letter or number, and be between 1 and 40 (inclusive) characters in length. | |
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
| **allowMissing** | **Boolean**| Optional. If set to true, and the subscription with the given package_name and product_id doesn&#39;t exist, the subscription will be created. If a new subscription is created, update_mask is ignored. | [optional] |
| **latencyTolerance** | **String**| Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. | [optional] [enum: PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED, PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE, PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT] |
| **regionsVersionVersion** | **String**| Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02. | [optional] |
| **updateMask** | **String**| Required. The list of fields to be updated. | [optional] |
| **subscription** | [**Subscription**](Subscription.md)|  | [optional] |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

