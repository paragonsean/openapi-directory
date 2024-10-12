# GooglePlayAndroidDeveloperApi.MonetizationApi

All URIs are relative to *https://androidpublisher.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidpublisherMonetizationConvertRegionPrices**](MonetizationApi.md#androidpublisherMonetizationConvertRegionPrices) | **POST** /androidpublisher/v3/applications/{packageName}/pricing:convertRegionPrices | 
[**androidpublisherMonetizationSubscriptionsArchive**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsArchive) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}:archive | 
[**androidpublisherMonetizationSubscriptionsBasePlansActivate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansActivate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:activate | 
[**androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans:batchMigratePrices | 
[**androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans:batchUpdateStates | 
[**androidpublisherMonetizationSubscriptionsBasePlansDeactivate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansDeactivate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:deactivate | 
[**androidpublisherMonetizationSubscriptionsBasePlansDelete**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansDelete) | **DELETE** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId} | 
[**androidpublisherMonetizationSubscriptionsBasePlansMigratePrices**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansMigratePrices) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}:migratePrices | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersActivate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersActivate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:activate | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers:batchGet | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers:batchUpdate | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers:batchUpdateStates | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersCreate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersCreate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId}:deactivate | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersDelete**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersDelete) | **DELETE** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId} | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersGet**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersGet) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId} | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersList**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersList) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers | 
[**androidpublisherMonetizationSubscriptionsBasePlansOffersPatch**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBasePlansOffersPatch) | **PATCH** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId}/basePlans/{basePlanId}/offers/{offerId} | 
[**androidpublisherMonetizationSubscriptionsBatchGet**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBatchGet) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions:batchGet | 
[**androidpublisherMonetizationSubscriptionsBatchUpdate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsBatchUpdate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions:batchUpdate | 
[**androidpublisherMonetizationSubscriptionsCreate**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsCreate) | **POST** /androidpublisher/v3/applications/{packageName}/subscriptions | 
[**androidpublisherMonetizationSubscriptionsDelete**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsDelete) | **DELETE** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId} | 
[**androidpublisherMonetizationSubscriptionsGet**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsGet) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId} | 
[**androidpublisherMonetizationSubscriptionsList**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsList) | **GET** /androidpublisher/v3/applications/{packageName}/subscriptions | 
[**androidpublisherMonetizationSubscriptionsPatch**](MonetizationApi.md#androidpublisherMonetizationSubscriptionsPatch) | **PATCH** /androidpublisher/v3/applications/{packageName}/subscriptions/{productId} | 



## androidpublisherMonetizationConvertRegionPrices

> ConvertRegionPricesResponse androidpublisherMonetizationConvertRegionPrices(packageName, opts)



Calculates the region prices, using today&#39;s exchange rate and country-specific pricing patterns, based on the price in the request for a set of regions.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The app package name.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'convertRegionPricesRequest': new GooglePlayAndroidDeveloperApi.ConvertRegionPricesRequest() // ConvertRegionPricesRequest | 
};
apiInstance.androidpublisherMonetizationConvertRegionPrices(packageName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The app package name. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **convertRegionPricesRequest** | [**ConvertRegionPricesRequest**](ConvertRegionPricesRequest.md)|  | [optional] 

### Return type

[**ConvertRegionPricesResponse**](ConvertRegionPricesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsArchive

> Subscription androidpublisherMonetizationSubscriptionsArchive(packageName, productId, opts)



Deprecated: subscription archiving is not supported.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the app of the subscription to delete.
let productId = "productId_example"; // String | Required. The unique product ID of the subscription to delete.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'body': {key: null} // Object | 
};
apiInstance.androidpublisherMonetizationSubscriptionsArchive(packageName, productId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the app of the subscription to delete. | 
 **productId** | **String**| Required. The unique product ID of the subscription to delete. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansActivate

> Subscription androidpublisherMonetizationSubscriptionsBasePlansActivate(packageName, productId, basePlanId, opts)



Activates a base plan. Once activated, base plans will be available to new subscribers.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the base plan to activate.
let productId = "productId_example"; // String | Required. The parent subscription (ID) of the base plan to activate.
let basePlanId = "basePlanId_example"; // String | Required. The unique base plan ID of the base plan to activate.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'activateBasePlanRequest': new GooglePlayAndroidDeveloperApi.ActivateBasePlanRequest() // ActivateBasePlanRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansActivate(packageName, productId, basePlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the base plan to activate. | 
 **productId** | **String**| Required. The parent subscription (ID) of the base plan to activate. | 
 **basePlanId** | **String**| Required. The unique base plan ID of the base plan to activate. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **activateBasePlanRequest** | [**ActivateBasePlanRequest**](ActivateBasePlanRequest.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices

> BatchMigrateBasePlanPricesResponse androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices(packageName, productId, opts)



Batch variant of the MigrateBasePlanPrices endpoint. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the Subscription resources.
let productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \"-\". Must be set.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'batchMigrateBasePlanPricesRequest': new GooglePlayAndroidDeveloperApi.BatchMigrateBasePlanPricesRequest() // BatchMigrateBasePlanPricesRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansBatchMigratePrices(packageName, productId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the Subscription resources. | 
 **productId** | **String**| Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **batchMigrateBasePlanPricesRequest** | [**BatchMigrateBasePlanPricesRequest**](BatchMigrateBasePlanPricesRequest.md)|  | [optional] 

### Return type

[**BatchMigrateBasePlanPricesResponse**](BatchMigrateBasePlanPricesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates

> BatchUpdateBasePlanStatesResponse androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates(packageName, productId, opts)



Activates or deactivates base plans across one or multiple subscriptions. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the updated base plans.
let productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated base plans belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \"-\". Must be set.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'batchUpdateBasePlanStatesRequest': new GooglePlayAndroidDeveloperApi.BatchUpdateBasePlanStatesRequest() // BatchUpdateBasePlanStatesRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansBatchUpdateStates(packageName, productId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the updated base plans. | 
 **productId** | **String**| Required. The product ID of the parent subscription, if all updated base plans belong to the same subscription. If this batch update spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **batchUpdateBasePlanStatesRequest** | [**BatchUpdateBasePlanStatesRequest**](BatchUpdateBasePlanStatesRequest.md)|  | [optional] 

### Return type

[**BatchUpdateBasePlanStatesResponse**](BatchUpdateBasePlanStatesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansDeactivate

> Subscription androidpublisherMonetizationSubscriptionsBasePlansDeactivate(packageName, productId, basePlanId, opts)



Deactivates a base plan. Once deactivated, the base plan will become unavailable to new subscribers, but existing subscribers will maintain their subscription

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the base plan to deactivate.
let productId = "productId_example"; // String | Required. The parent subscription (ID) of the base plan to deactivate.
let basePlanId = "basePlanId_example"; // String | Required. The unique base plan ID of the base plan to deactivate.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'deactivateBasePlanRequest': new GooglePlayAndroidDeveloperApi.DeactivateBasePlanRequest() // DeactivateBasePlanRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansDeactivate(packageName, productId, basePlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the base plan to deactivate. | 
 **productId** | **String**| Required. The parent subscription (ID) of the base plan to deactivate. | 
 **basePlanId** | **String**| Required. The unique base plan ID of the base plan to deactivate. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **deactivateBasePlanRequest** | [**DeactivateBasePlanRequest**](DeactivateBasePlanRequest.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansDelete

> androidpublisherMonetizationSubscriptionsBasePlansDelete(packageName, productId, basePlanId, opts)



Deletes a base plan. Can only be done for draft base plans. This action is irreversible.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the base plan to delete.
let productId = "productId_example"; // String | Required. The parent subscription (ID) of the base plan to delete.
let basePlanId = "basePlanId_example"; // String | Required. The unique offer ID of the base plan to delete.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansDelete(packageName, productId, basePlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the base plan to delete. | 
 **productId** | **String**| Required. The parent subscription (ID) of the base plan to delete. | 
 **basePlanId** | **String**| Required. The unique offer ID of the base plan to delete. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherMonetizationSubscriptionsBasePlansMigratePrices

> Object androidpublisherMonetizationSubscriptionsBasePlansMigratePrices(packageName, productId, basePlanId, opts)



Migrates subscribers who are receiving an historical subscription price to the currently-offered price for the specified region. Requests will cause price change notifications to be sent to users who are currently receiving an historical price older than the supplied timestamp. Subscribers who do not agree to the new price will have their subscription ended at the next renewal.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. Package name of the parent app. Must be equal to the package_name field on the Subscription resource.
let productId = "productId_example"; // String | Required. The ID of the subscription to update. Must be equal to the product_id field on the Subscription resource.
let basePlanId = "basePlanId_example"; // String | Required. The unique base plan ID of the base plan to update prices on.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'migrateBasePlanPricesRequest': new GooglePlayAndroidDeveloperApi.MigrateBasePlanPricesRequest() // MigrateBasePlanPricesRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansMigratePrices(packageName, productId, basePlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. Package name of the parent app. Must be equal to the package_name field on the Subscription resource. | 
 **productId** | **String**| Required. The ID of the subscription to update. Must be equal to the product_id field on the Subscription resource. | 
 **basePlanId** | **String**| Required. The unique base plan ID of the base plan to update prices on. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **migrateBasePlanPricesRequest** | [**MigrateBasePlanPricesRequest**](MigrateBasePlanPricesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansOffersActivate

> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersActivate(packageName, productId, basePlanId, offerId, opts)



Activates a subscription offer. Once activated, subscription offers will be available to new subscribers.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the offer to activate.
let productId = "productId_example"; // String | Required. The parent subscription (ID) of the offer to activate.
let basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) of the offer to activate.
let offerId = "offerId_example"; // String | Required. The unique offer ID of the offer to activate.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'activateSubscriptionOfferRequest': new GooglePlayAndroidDeveloperApi.ActivateSubscriptionOfferRequest() // ActivateSubscriptionOfferRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersActivate(packageName, productId, basePlanId, offerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the offer to activate. | 
 **productId** | **String**| Required. The parent subscription (ID) of the offer to activate. | 
 **basePlanId** | **String**| Required. The parent base plan (ID) of the offer to activate. | 
 **offerId** | **String**| Required. The unique offer ID of the offer to activate. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **activateSubscriptionOfferRequest** | [**ActivateSubscriptionOfferRequest**](ActivateSubscriptionOfferRequest.md)|  | [optional] 

### Return type

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet

> BatchGetSubscriptionOffersResponse androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet(packageName, productId, basePlanId, opts)



Reads one or more subscription offers.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the requests.
let productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \"-\". Must be set.
let basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offers should be read. May be specified as '-' to read offers from multiple base plans.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'batchGetSubscriptionOffersRequest': new GooglePlayAndroidDeveloperApi.BatchGetSubscriptionOffersRequest() // BatchGetSubscriptionOffersRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersBatchGet(packageName, productId, basePlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be created or updated. Must be equal to the package_name field on all the requests. | 
 **productId** | **String**| Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | 
 **basePlanId** | **String**| Required. The parent base plan (ID) for which the offers should be read. May be specified as &#39;-&#39; to read offers from multiple base plans. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **batchGetSubscriptionOffersRequest** | [**BatchGetSubscriptionOffersRequest**](BatchGetSubscriptionOffersRequest.md)|  | [optional] 

### Return type

[**BatchGetSubscriptionOffersResponse**](BatchGetSubscriptionOffersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate

> BatchUpdateSubscriptionOffersResponse androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate(packageName, productId, basePlanId, opts)



Updates a batch of subscription offers. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources.
let productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \"-\". Must be set.
let basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offers should be updated. May be specified as '-' to update offers from multiple base plans.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'batchUpdateSubscriptionOffersRequest': new GooglePlayAndroidDeveloperApi.BatchUpdateSubscriptionOffersRequest() // BatchUpdateSubscriptionOffersRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdate(packageName, productId, basePlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources. | 
 **productId** | **String**| Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | 
 **basePlanId** | **String**| Required. The parent base plan (ID) for which the offers should be updated. May be specified as &#39;-&#39; to update offers from multiple base plans. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **batchUpdateSubscriptionOffersRequest** | [**BatchUpdateSubscriptionOffersRequest**](BatchUpdateSubscriptionOffersRequest.md)|  | [optional] 

### Return type

[**BatchUpdateSubscriptionOffersResponse**](BatchUpdateSubscriptionOffersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates

> BatchUpdateSubscriptionOfferStatesResponse androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates(packageName, productId, basePlanId, opts)



Updates a batch of subscription offer states. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources.
let productId = "productId_example"; // String | Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \"-\". Must be set.
let basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offers should be updated. May be specified as '-' to update offers from multiple base plans.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'batchUpdateSubscriptionOfferStatesRequest': new GooglePlayAndroidDeveloperApi.BatchUpdateSubscriptionOfferStatesRequest() // BatchUpdateSubscriptionOfferStatesRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersBatchUpdateStates(packageName, productId, basePlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the updated subscription offers. Must be equal to the package_name field on all the updated SubscriptionOffer resources. | 
 **productId** | **String**| Required. The product ID of the parent subscription, if all updated offers belong to the same subscription. If this request spans multiple subscriptions, set this field to \&quot;-\&quot;. Must be set. | 
 **basePlanId** | **String**| Required. The parent base plan (ID) for which the offers should be updated. May be specified as &#39;-&#39; to update offers from multiple base plans. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **batchUpdateSubscriptionOfferStatesRequest** | [**BatchUpdateSubscriptionOfferStatesRequest**](BatchUpdateSubscriptionOfferStatesRequest.md)|  | [optional] 

### Return type

[**BatchUpdateSubscriptionOfferStatesResponse**](BatchUpdateSubscriptionOfferStatesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansOffersCreate

> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersCreate(packageName, productId, basePlanId, opts)



Creates a new subscription offer. Only auto-renewing base plans can have subscription offers. The offer state will be DRAFT until it is activated.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) for which the offer should be created. Must be equal to the package_name field on the Subscription resource.
let productId = "productId_example"; // String | Required. The parent subscription (ID) for which the offer should be created. Must be equal to the product_id field on the SubscriptionOffer resource.
let basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offer should be created. Must be equal to the base_plan_id field on the SubscriptionOffer resource.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'offerId': "offerId_example", // String | Required. The ID to use for the offer. For the requirements on this format, see the documentation of the offer_id field on the SubscriptionOffer resource.
  'regionsVersionVersion': "regionsVersionVersion_example", // String | Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
  'subscriptionOffer': new GooglePlayAndroidDeveloperApi.SubscriptionOffer() // SubscriptionOffer | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersCreate(packageName, productId, basePlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) for which the offer should be created. Must be equal to the package_name field on the Subscription resource. | 
 **productId** | **String**| Required. The parent subscription (ID) for which the offer should be created. Must be equal to the product_id field on the SubscriptionOffer resource. | 
 **basePlanId** | **String**| Required. The parent base plan (ID) for which the offer should be created. Must be equal to the base_plan_id field on the SubscriptionOffer resource. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **offerId** | **String**| Required. The ID to use for the offer. For the requirements on this format, see the documentation of the offer_id field on the SubscriptionOffer resource. | [optional] 
 **regionsVersionVersion** | **String**| Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02. | [optional] 
 **subscriptionOffer** | [**SubscriptionOffer**](SubscriptionOffer.md)|  | [optional] 

### Return type

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate

> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate(packageName, productId, basePlanId, offerId, opts)



Deactivates a subscription offer. Once deactivated, existing subscribers will maintain their subscription, but the offer will become unavailable to new subscribers.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the offer to deactivate.
let productId = "productId_example"; // String | Required. The parent subscription (ID) of the offer to deactivate.
let basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) of the offer to deactivate.
let offerId = "offerId_example"; // String | Required. The unique offer ID of the offer to deactivate.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'deactivateSubscriptionOfferRequest': new GooglePlayAndroidDeveloperApi.DeactivateSubscriptionOfferRequest() // DeactivateSubscriptionOfferRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersDeactivate(packageName, productId, basePlanId, offerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the offer to deactivate. | 
 **productId** | **String**| Required. The parent subscription (ID) of the offer to deactivate. | 
 **basePlanId** | **String**| Required. The parent base plan (ID) of the offer to deactivate. | 
 **offerId** | **String**| Required. The unique offer ID of the offer to deactivate. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **deactivateSubscriptionOfferRequest** | [**DeactivateSubscriptionOfferRequest**](DeactivateSubscriptionOfferRequest.md)|  | [optional] 

### Return type

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansOffersDelete

> androidpublisherMonetizationSubscriptionsBasePlansOffersDelete(packageName, productId, basePlanId, offerId, opts)



Deletes a subscription offer. Can only be done for draft offers. This action is irreversible.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the offer to delete.
let productId = "productId_example"; // String | Required. The parent subscription (ID) of the offer to delete.
let basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) of the offer to delete.
let offerId = "offerId_example"; // String | Required. The unique offer ID of the offer to delete.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersDelete(packageName, productId, basePlanId, offerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the offer to delete. | 
 **productId** | **String**| Required. The parent subscription (ID) of the offer to delete. | 
 **basePlanId** | **String**| Required. The parent base plan (ID) of the offer to delete. | 
 **offerId** | **String**| Required. The unique offer ID of the offer to delete. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherMonetizationSubscriptionsBasePlansOffersGet

> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersGet(packageName, productId, basePlanId, offerId, opts)



Reads a single offer

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the offer to get.
let productId = "productId_example"; // String | Required. The parent subscription (ID) of the offer to get.
let basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) of the offer to get.
let offerId = "offerId_example"; // String | Required. The unique offer ID of the offer to get.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersGet(packageName, productId, basePlanId, offerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the offer to get. | 
 **productId** | **String**| Required. The parent subscription (ID) of the offer to get. | 
 **basePlanId** | **String**| Required. The parent base plan (ID) of the offer to get. | 
 **offerId** | **String**| Required. The unique offer ID of the offer to get. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansOffersList

> ListSubscriptionOffersResponse androidpublisherMonetizationSubscriptionsBasePlansOffersList(packageName, productId, basePlanId, opts)



Lists all offers under a given subscription.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be read.
let productId = "productId_example"; // String | Required. The parent subscription (ID) for which the offers should be read. May be specified as '-' to read all offers under an app.
let basePlanId = "basePlanId_example"; // String | Required. The parent base plan (ID) for which the offers should be read. May be specified as '-' to read all offers under a subscription or an app. Must be specified as '-' if product_id is specified as '-'.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
  'pageToken': "pageToken_example" // String | A page token, received from a previous `ListSubscriptionsOffers` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSubscriptionOffers` must match the call that provided the page token.
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersList(packageName, productId, basePlanId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be read. | 
 **productId** | **String**| Required. The parent subscription (ID) for which the offers should be read. May be specified as &#39;-&#39; to read all offers under an app. | 
 **basePlanId** | **String**| Required. The parent base plan (ID) for which the offers should be read. May be specified as &#39;-&#39; to read all offers under a subscription or an app. Must be specified as &#39;-&#39; if product_id is specified as &#39;-&#39;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListSubscriptionsOffers&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListSubscriptionOffers&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**ListSubscriptionOffersResponse**](ListSubscriptionOffersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBasePlansOffersPatch

> SubscriptionOffer androidpublisherMonetizationSubscriptionsBasePlansOffersPatch(packageName, productId, basePlanId, offerId, opts)



Updates an existing subscription offer.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. Immutable. The package name of the app the parent subscription belongs to.
let productId = "productId_example"; // String | Required. Immutable. The ID of the parent subscription this offer belongs to.
let basePlanId = "basePlanId_example"; // String | Required. Immutable. The ID of the base plan to which this offer is an extension.
let offerId = "offerId_example"; // String | Required. Immutable. Unique ID of this subscription offer. Must be unique within the base plan.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'allowMissing': true, // Boolean | Optional. If set to true, and the subscription offer with the given package_name, product_id, base_plan_id and offer_id doesn't exist, an offer will be created. If a new offer is created, update_mask is ignored.
  'latencyTolerance': "latencyTolerance_example", // String | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.
  'regionsVersionVersion': "regionsVersionVersion_example", // String | Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
  'updateMask': "updateMask_example", // String | Required. The list of fields to be updated.
  'subscriptionOffer': new GooglePlayAndroidDeveloperApi.SubscriptionOffer() // SubscriptionOffer | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBasePlansOffersPatch(packageName, productId, basePlanId, offerId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. Immutable. The package name of the app the parent subscription belongs to. | 
 **productId** | **String**| Required. Immutable. The ID of the parent subscription this offer belongs to. | 
 **basePlanId** | **String**| Required. Immutable. The ID of the base plan to which this offer is an extension. | 
 **offerId** | **String**| Required. Immutable. Unique ID of this subscription offer. Must be unique within the base plan. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **allowMissing** | **Boolean**| Optional. If set to true, and the subscription offer with the given package_name, product_id, base_plan_id and offer_id doesn&#39;t exist, an offer will be created. If a new offer is created, update_mask is ignored. | [optional] 
 **latencyTolerance** | **String**| Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. | [optional] 
 **regionsVersionVersion** | **String**| Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02. | [optional] 
 **updateMask** | **String**| Required. The list of fields to be updated. | [optional] 
 **subscriptionOffer** | [**SubscriptionOffer**](SubscriptionOffer.md)|  | [optional] 

### Return type

[**SubscriptionOffer**](SubscriptionOffer.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBatchGet

> BatchGetSubscriptionsResponse androidpublisherMonetizationSubscriptionsBatchGet(packageName, opts)



Reads one or more subscriptions.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be retrieved. Must be equal to the package_name field on all the requests.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'productIds': ["null"] // [String] | Required. A list of up to 100 subscription product IDs to retrieve. All the IDs must be different.
};
apiInstance.androidpublisherMonetizationSubscriptionsBatchGet(packageName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be retrieved. Must be equal to the package_name field on all the requests. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **productIds** | [**[String]**](String.md)| Required. A list of up to 100 subscription product IDs to retrieve. All the IDs must be different. | [optional] 

### Return type

[**BatchGetSubscriptionsResponse**](BatchGetSubscriptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsBatchUpdate

> BatchUpdateSubscriptionsResponse androidpublisherMonetizationSubscriptionsBatchUpdate(packageName, opts)



Updates a batch of subscriptions. Set the latencyTolerance field on nested requests to PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT to achieve maximum update throughput.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be updated. Must be equal to the package_name field on all the Subscription resources.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'batchUpdateSubscriptionsRequest': new GooglePlayAndroidDeveloperApi.BatchUpdateSubscriptionsRequest() // BatchUpdateSubscriptionsRequest | 
};
apiInstance.androidpublisherMonetizationSubscriptionsBatchUpdate(packageName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be updated. Must be equal to the package_name field on all the Subscription resources. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **batchUpdateSubscriptionsRequest** | [**BatchUpdateSubscriptionsRequest**](BatchUpdateSubscriptionsRequest.md)|  | [optional] 

### Return type

[**BatchUpdateSubscriptionsResponse**](BatchUpdateSubscriptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsCreate

> Subscription androidpublisherMonetizationSubscriptionsCreate(packageName, opts)



Creates a new subscription. Newly added base plans will remain in draft state until activated.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscription should be created. Must be equal to the package_name field on the Subscription resource.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'productId': "productId_example", // String | Required. The ID to use for the subscription. For the requirements on this format, see the documentation of the product_id field on the Subscription resource.
  'regionsVersionVersion': "regionsVersionVersion_example", // String | Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
  'subscription': new GooglePlayAndroidDeveloperApi.Subscription() // Subscription | 
};
apiInstance.androidpublisherMonetizationSubscriptionsCreate(packageName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) for which the subscription should be created. Must be equal to the package_name field on the Subscription resource. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **productId** | **String**| Required. The ID to use for the subscription. For the requirements on this format, see the documentation of the product_id field on the Subscription resource. | [optional] 
 **regionsVersionVersion** | **String**| Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02. | [optional] 
 **subscription** | [**Subscription**](Subscription.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsDelete

> androidpublisherMonetizationSubscriptionsDelete(packageName, productId, opts)



Deletes a subscription. A subscription can only be deleted if it has never had a base plan published.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the app of the subscription to delete.
let productId = "productId_example"; // String | Required. The unique product ID of the subscription to delete.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.androidpublisherMonetizationSubscriptionsDelete(packageName, productId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the app of the subscription to delete. | 
 **productId** | **String**| Required. The unique product ID of the subscription to delete. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## androidpublisherMonetizationSubscriptionsGet

> Subscription androidpublisherMonetizationSubscriptionsGet(packageName, productId, opts)



Reads a single subscription.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) of the subscription to get.
let productId = "productId_example"; // String | Required. The unique product ID of the subscription to get.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.androidpublisherMonetizationSubscriptionsGet(packageName, productId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) of the subscription to get. | 
 **productId** | **String**| Required. The unique product ID of the subscription to get. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsList

> ListSubscriptionsResponse androidpublisherMonetizationSubscriptionsList(packageName, opts)



Lists all subscriptions under a given app.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Required. The parent app (package name) for which the subscriptions should be read.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
  'pageToken': "pageToken_example", // String | A page token, received from a previous `ListSubscriptions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSubscriptions` must match the call that provided the page token.
  'showArchived': true // Boolean | Deprecated: subscription archiving is not supported.
};
apiInstance.androidpublisherMonetizationSubscriptionsList(packageName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Required. The parent app (package name) for which the subscriptions should be read. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of subscriptions to return. The service may return fewer than this value. If unspecified, at most 50 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListSubscriptions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListSubscriptions&#x60; must match the call that provided the page token. | [optional] 
 **showArchived** | **Boolean**| Deprecated: subscription archiving is not supported. | [optional] 

### Return type

[**ListSubscriptionsResponse**](ListSubscriptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidpublisherMonetizationSubscriptionsPatch

> Subscription androidpublisherMonetizationSubscriptionsPatch(packageName, productId, opts)



Updates an existing subscription.

### Example

```javascript
import GooglePlayAndroidDeveloperApi from 'google_play_android_developer_api';
let defaultClient = GooglePlayAndroidDeveloperApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayAndroidDeveloperApi.MonetizationApi();
let packageName = "packageName_example"; // String | Immutable. Package name of the parent app.
let productId = "productId_example"; // String | Immutable. Unique product ID of the product. Unique within the parent app. Product IDs must be composed of lower-case letters (a-z), numbers (0-9), underscores (_) and dots (.). It must start with a lower-case letter or number, and be between 1 and 40 (inclusive) characters in length.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'allowMissing': true, // Boolean | Optional. If set to true, and the subscription with the given package_name and product_id doesn't exist, the subscription will be created. If a new subscription is created, update_mask is ignored.
  'latencyTolerance': "latencyTolerance_example", // String | Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive.
  'regionsVersionVersion': "regionsVersionVersion_example", // String | Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region's version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02.
  'updateMask': "updateMask_example", // String | Required. The list of fields to be updated.
  'subscription': new GooglePlayAndroidDeveloperApi.Subscription() // Subscription | 
};
apiInstance.androidpublisherMonetizationSubscriptionsPatch(packageName, productId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| Immutable. Package name of the parent app. | 
 **productId** | **String**| Immutable. Unique product ID of the product. Unique within the parent app. Product IDs must be composed of lower-case letters (a-z), numbers (0-9), underscores (_) and dots (.). It must start with a lower-case letter or number, and be between 1 and 40 (inclusive) characters in length. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **allowMissing** | **Boolean**| Optional. If set to true, and the subscription with the given package_name and product_id doesn&#39;t exist, the subscription will be created. If a new subscription is created, update_mask is ignored. | [optional] 
 **latencyTolerance** | **String**| Optional. The latency tolerance for the propagation of this product update. Defaults to latency-sensitive. | [optional] 
 **regionsVersionVersion** | **String**| Required. A string representing the version of available regions being used for the specified resource. Regional prices for the resource have to be specified according to the information published in [this article](https://support.google.com/googleplay/android-developer/answer/10532353). Each time the supported locations substantially change, the version will be incremented. Using this field will ensure that creating and updating the resource with an older region&#39;s version and set of regional prices and currencies will succeed even though a new version is available. The latest version is 2022/02. | [optional] 
 **updateMask** | **String**| Required. The list of fields to be updated. | [optional] 
 **subscription** | [**Subscription**](Subscription.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

