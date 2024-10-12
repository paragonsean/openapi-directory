# TravelPartnerApi.AccountsApi

All URIs are relative to *https://travelpartner.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**travelpartnerAccountsAccountLinksCreate**](AccountsApi.md#travelpartnerAccountsAccountLinksCreate) | **POST** /v3/{parent}/accountLinks | 
[**travelpartnerAccountsAccountLinksDelete**](AccountsApi.md#travelpartnerAccountsAccountLinksDelete) | **DELETE** /v3/{name} | 
[**travelpartnerAccountsAccountLinksList**](AccountsApi.md#travelpartnerAccountsAccountLinksList) | **GET** /v3/{parent}/accountLinks | 
[**travelpartnerAccountsBrandsCreate**](AccountsApi.md#travelpartnerAccountsBrandsCreate) | **POST** /v3/{parent}/brands | 
[**travelpartnerAccountsBrandsList**](AccountsApi.md#travelpartnerAccountsBrandsList) | **GET** /v3/{parent}/brands | 
[**travelpartnerAccountsBrandsPatch**](AccountsApi.md#travelpartnerAccountsBrandsPatch) | **PATCH** /v3/{name} | 
[**travelpartnerAccountsFreeBookingLinksReportViewsQuery**](AccountsApi.md#travelpartnerAccountsFreeBookingLinksReportViewsQuery) | **GET** /v3/{name}/freeBookingLinksReportViews:query | 
[**travelpartnerAccountsHotelViewsList**](AccountsApi.md#travelpartnerAccountsHotelViewsList) | **GET** /v3/{parent}/hotelViews | 
[**travelpartnerAccountsHotelViewsSummarize**](AccountsApi.md#travelpartnerAccountsHotelViewsSummarize) | **GET** /v3/{parent}/hotelViews:summarize | 
[**travelpartnerAccountsHotelsSetLiveOnGoogle**](AccountsApi.md#travelpartnerAccountsHotelsSetLiveOnGoogle) | **POST** /v3/{account}/hotels:setLiveOnGoogle | 
[**travelpartnerAccountsIconsCreate**](AccountsApi.md#travelpartnerAccountsIconsCreate) | **POST** /v3/{parent}/icons | 
[**travelpartnerAccountsIconsList**](AccountsApi.md#travelpartnerAccountsIconsList) | **GET** /v3/{parent}/icons | 
[**travelpartnerAccountsListingsVerify**](AccountsApi.md#travelpartnerAccountsListingsVerify) | **POST** /v3/{parent}/listings:verify | 
[**travelpartnerAccountsParticipationReportViewsQuery**](AccountsApi.md#travelpartnerAccountsParticipationReportViewsQuery) | **GET** /v3/{name}/participationReportViews:query | 
[**travelpartnerAccountsPriceAccuracyViewsList**](AccountsApi.md#travelpartnerAccountsPriceAccuracyViewsList) | **GET** /v3/{parent}/priceAccuracyViews | 
[**travelpartnerAccountsPriceAccuracyViewsSummarize**](AccountsApi.md#travelpartnerAccountsPriceAccuracyViewsSummarize) | **GET** /v3/{parent}/priceAccuracyViews:summarize | 
[**travelpartnerAccountsPriceCoverageViewsGetLatest**](AccountsApi.md#travelpartnerAccountsPriceCoverageViewsGetLatest) | **GET** /v3/{parent}/priceCoverageViews:latest | 
[**travelpartnerAccountsPriceCoverageViewsList**](AccountsApi.md#travelpartnerAccountsPriceCoverageViewsList) | **GET** /v3/{parent}/priceCoverageViews | 
[**travelpartnerAccountsPropertyPerformanceReportViewsQuery**](AccountsApi.md#travelpartnerAccountsPropertyPerformanceReportViewsQuery) | **GET** /v3/{name}/propertyPerformanceReportViews:query | 
[**travelpartnerAccountsReconciliationReportsCreate**](AccountsApi.md#travelpartnerAccountsReconciliationReportsCreate) | **POST** /v3/{parent}/reconciliationReports | 
[**travelpartnerAccountsReconciliationReportsGet**](AccountsApi.md#travelpartnerAccountsReconciliationReportsGet) | **GET** /v3/{name} | 
[**travelpartnerAccountsReconciliationReportsList**](AccountsApi.md#travelpartnerAccountsReconciliationReportsList) | **GET** /v3/{parent}/reconciliationReports | 
[**travelpartnerAccountsReconciliationReportsValidate**](AccountsApi.md#travelpartnerAccountsReconciliationReportsValidate) | **POST** /v3/{parent}/reconciliationReports:validate | 



## travelpartnerAccountsAccountLinksCreate

> AccountLink travelpartnerAccountsAccountLinksCreate(parent, opts)



Creates a new account link between a Hotel Center account and a Google Ads account.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the Hotel Center account being queried. The format is `accounts/{account_id}`.
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
  'accountLink': new TravelPartnerApi.AccountLink() // AccountLink | 
};
apiInstance.travelpartnerAccountsAccountLinksCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the Hotel Center account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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
 **accountLink** | [**AccountLink**](AccountLink.md)|  | [optional] 

### Return type

[**AccountLink**](AccountLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## travelpartnerAccountsAccountLinksDelete

> Object travelpartnerAccountsAccountLinksDelete(name, opts)



Deletes an account link.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let name = "name_example"; // String | Required. The resource name of the account link being deleted. The format is `accounts/{account_id}/accountLinks/{account_link_id}`.
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
apiInstance.travelpartnerAccountsAccountLinksDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The resource name of the account link being deleted. The format is &#x60;accounts/{account_id}/accountLinks/{account_link_id}&#x60;. | 
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsAccountLinksList

> ListAccountLinksResponse travelpartnerAccountsAccountLinksList(parent, opts)



Returns the account links for a Hotel Center account.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
apiInstance.travelpartnerAccountsAccountLinksList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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

[**ListAccountLinksResponse**](ListAccountLinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsBrandsCreate

> Brand travelpartnerAccountsBrandsCreate(parent, opts)



Creates a new brand. Because Google detects brands from your existing properties, you only need this operation when you want to configure a brand before you send its properties to Google. Note that it might take a couple of days after your listing feed first provides a brand for the brand to appear.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | Required. The resource name of the Hotel Center account being queried. The format is `accounts/{account_id}`.
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
  'brandId': "brandId_example", // String | Required. The partner-determined brand identifier.
  'brand': new TravelPartnerApi.Brand() // Brand | 
};
apiInstance.travelpartnerAccountsBrandsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the Hotel Center account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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
 **brandId** | **String**| Required. The partner-determined brand identifier. | [optional] 
 **brand** | [**Brand**](Brand.md)|  | [optional] 

### Return type

[**Brand**](Brand.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## travelpartnerAccountsBrandsList

> ListBrandsResponse travelpartnerAccountsBrandsList(parent, opts)



Returns the brands for a partner account.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | Required. The resource name of the account being queried. The format is `accounts/{account_id}`.
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
apiInstance.travelpartnerAccountsBrandsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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

[**ListBrandsResponse**](ListBrandsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsBrandsPatch

> Brand travelpartnerAccountsBrandsPatch(name, opts)



Updates a brand.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let name = "name_example"; // String | Output only. The resource name for the brand in the format `accounts/{account_id}/brands/{brand_id}`. The `brand_id` corresponds to the partner's brand identifier used for landing page matching and the property-level brand identifier. A default brand is applied to properties that do not have a brand. The `brand_id` of the default brand is `NO_BRAND_ID`. It can be fetched and updated like any configured brand.
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
  'allowMissing': true, // Boolean | When true, and the Brand is not found, a new Brand will be created. In this situation, `update_mask` is ignored.
  'updateMask': "updateMask_example", // String | Required. The field to update. Only the `display_names` and `icon` fields can be updated. Use the syntax shown in the example URI below and provide the new value in the request body. Example request URI and request body: ``` PATCH https://travelpartner.googleapis.com/v3/accounts/123456789/ brands/my-brand?update_mask=brand.display_names ``` ``` { \"display_names\": [{ \"language\": \"en\" \"text\": \"Gilles' Gites\" }] } ``` The information above is sufficient for forming the URI and request body. The sentence below is auto-generated, supplemental information about the `FieldMask` format in general.
  'brand': new TravelPartnerApi.Brand() // Brand | 
};
apiInstance.travelpartnerAccountsBrandsPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| Output only. The resource name for the brand in the format &#x60;accounts/{account_id}/brands/{brand_id}&#x60;. The &#x60;brand_id&#x60; corresponds to the partner&#39;s brand identifier used for landing page matching and the property-level brand identifier. A default brand is applied to properties that do not have a brand. The &#x60;brand_id&#x60; of the default brand is &#x60;NO_BRAND_ID&#x60;. It can be fetched and updated like any configured brand. | 
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
 **allowMissing** | **Boolean**| When true, and the Brand is not found, a new Brand will be created. In this situation, &#x60;update_mask&#x60; is ignored. | [optional] 
 **updateMask** | **String**| Required. The field to update. Only the &#x60;display_names&#x60; and &#x60;icon&#x60; fields can be updated. Use the syntax shown in the example URI below and provide the new value in the request body. Example request URI and request body: &#x60;&#x60;&#x60; PATCH https://travelpartner.googleapis.com/v3/accounts/123456789/ brands/my-brand?update_mask&#x3D;brand.display_names &#x60;&#x60;&#x60; &#x60;&#x60;&#x60; { \&quot;display_names\&quot;: [{ \&quot;language\&quot;: \&quot;en\&quot; \&quot;text\&quot;: \&quot;Gilles&#39; Gites\&quot; }] } &#x60;&#x60;&#x60; The information above is sufficient for forming the URI and request body. The sentence below is auto-generated, supplemental information about the &#x60;FieldMask&#x60; format in general. | [optional] 
 **brand** | [**Brand**](Brand.md)|  | [optional] 

### Return type

[**Brand**](Brand.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## travelpartnerAccountsFreeBookingLinksReportViewsQuery

> QueryFreeBookingLinksReportResponse travelpartnerAccountsFreeBookingLinksReportViewsQuery(name, opts)



**DEPRECATED:** Use PropertyPerformanceReportService.QueryPropertyPerformanceReport, which also has impression reporting, instead. Provides the ability to query (get, filter, and segment) a free booking links report for a specific account.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let name = "name_example"; // String | The resource name of the account being queried. Format: accounts/{account_id}
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
  'aggregateBy': "aggregateBy_example", // String | Specifies how to segment the metrics returned by the query. For example, if `userRegionCode` is specified, the `freeBookingLinksResult` will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: `date`, `userRegionCode`, `deviceType`, `partnerHotelId`, and `partnerHotelDisplayName`. Only fields specified here are included in the FreeBookingLinksResult.
  'filter': "filter_example", // String | The conditions (fields and expressions) used to filter the free booking link metrics for the account being queried. The syntax requires spaces surrounding the `in` operator. Otherwise, spaces can be omitted. Conditions can be joined using the `and` operator. The `date` field is required. All other fields are optional. The `date` field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for `partnerHotelDisplayName` are matched case-insensitively. Examples of valid conditions are as follows: * `date = '2021-12-03'` * `date between '2021-12-03' and '2021-12-08'` * `deviceType = 'TABLET'` * `deviceType in ('MOBILE', 'TABLET')` * `partnerHotelId = 'AAA'` * `partnerHotelId in ('AAA', 'BBB')` * `partnerHotelDisplayName = 'hotel A'` * `partnerHotelDisplayName in ('Hotel A', 'HOTEL b')` * `userRegionCode = 'US'` * `userRegionCode in ('US', 'CA')`
  'pageSize': 56, // Number | The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.
  'pageToken': "pageToken_example" // String | A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token.
};
apiInstance.travelpartnerAccountsFreeBookingLinksReportViewsQuery(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the account being queried. Format: accounts/{account_id} | 
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
 **aggregateBy** | **String**| Specifies how to segment the metrics returned by the query. For example, if &#x60;userRegionCode&#x60; is specified, the &#x60;freeBookingLinksResult&#x60; will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: &#x60;date&#x60;, &#x60;userRegionCode&#x60;, &#x60;deviceType&#x60;, &#x60;partnerHotelId&#x60;, and &#x60;partnerHotelDisplayName&#x60;. Only fields specified here are included in the FreeBookingLinksResult. | [optional] 
 **filter** | **String**| The conditions (fields and expressions) used to filter the free booking link metrics for the account being queried. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions can be joined using the &#x60;and&#x60; operator. The &#x60;date&#x60; field is required. All other fields are optional. The &#x60;date&#x60; field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for &#x60;partnerHotelDisplayName&#x60; are matched case-insensitively. Examples of valid conditions are as follows: * &#x60;date &#x3D; &#39;2021-12-03&#39;&#x60; * &#x60;date between &#39;2021-12-03&#39; and &#39;2021-12-08&#39;&#x60; * &#x60;deviceType &#x3D; &#39;TABLET&#39;&#x60; * &#x60;deviceType in (&#39;MOBILE&#39;, &#39;TABLET&#39;)&#x60; * &#x60;partnerHotelId &#x3D; &#39;AAA&#39;&#x60; * &#x60;partnerHotelId in (&#39;AAA&#39;, &#39;BBB&#39;)&#x60; * &#x60;partnerHotelDisplayName &#x3D; &#39;hotel A&#39;&#x60; * &#x60;partnerHotelDisplayName in (&#39;Hotel A&#39;, &#39;HOTEL b&#39;)&#x60; * &#x60;userRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;userRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token. | [optional] 

### Return type

[**QueryFreeBookingLinksReportResponse**](QueryFreeBookingLinksReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsHotelViewsList

> ListHotelViewsResponse travelpartnerAccountsHotelViewsList(parent, opts)



Returns the list of hotel views.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
  'filter': "filter_example", // String | Optional. The conditions (fields and expressions) used to filter HotelViews. The syntax requires spaces surrounding the `in` operator. Otherwise, spaces can be omitted. Conditions cannot be joined. The `hotelId` field can be used to select specific hotels. The `liveOnGoogle` field can select properties that Google shows, or properties that are omitted in google search results. The `matchStatus` field can be used to filter the list of HotelViews returned for the account. Examples of valid conditions and their syntax are as follows: * `hotelId = 'hotel_ABC'` * `hotelId in ('hotel_ABC', 'hotel_XYZ')` * `liveOnGoogle = 'TRUE'` * `liveOnGoogle = 'FALSE'` * `matchStatus = 'NOT_MATCHED'` * `matchStatus in ('NOT_MATCHED', 'MATCHED', 'MAP_OVERLAP')`
  'pageSize': 56, // Number | Number of elements to retrieve in a single page.
  'pageToken': "pageToken_example" // String | Token of the page to retrieve.
};
apiInstance.travelpartnerAccountsHotelViewsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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
 **filter** | **String**| Optional. The conditions (fields and expressions) used to filter HotelViews. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions cannot be joined. The &#x60;hotelId&#x60; field can be used to select specific hotels. The &#x60;liveOnGoogle&#x60; field can select properties that Google shows, or properties that are omitted in google search results. The &#x60;matchStatus&#x60; field can be used to filter the list of HotelViews returned for the account. Examples of valid conditions and their syntax are as follows: * &#x60;hotelId &#x3D; &#39;hotel_ABC&#39;&#x60; * &#x60;hotelId in (&#39;hotel_ABC&#39;, &#39;hotel_XYZ&#39;)&#x60; * &#x60;liveOnGoogle &#x3D; &#39;TRUE&#39;&#x60; * &#x60;liveOnGoogle &#x3D; &#39;FALSE&#39;&#x60; * &#x60;matchStatus &#x3D; &#39;NOT_MATCHED&#39;&#x60; * &#x60;matchStatus in (&#39;NOT_MATCHED&#39;, &#39;MATCHED&#39;, &#39;MAP_OVERLAP&#39;)&#x60; | [optional] 
 **pageSize** | **Number**| Number of elements to retrieve in a single page. | [optional] 
 **pageToken** | **String**| Token of the page to retrieve. | [optional] 

### Return type

[**ListHotelViewsResponse**](ListHotelViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsHotelViewsSummarize

> SummarizeHotelViewsResponse travelpartnerAccountsHotelViewsSummarize(parent, opts)



Returns summarized information about hotels.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
apiInstance.travelpartnerAccountsHotelViewsSummarize(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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

[**SummarizeHotelViewsResponse**](SummarizeHotelViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsHotelsSetLiveOnGoogle

> SetLiveOnGoogleResponse travelpartnerAccountsHotelsSetLiveOnGoogle(account, opts)



Collection-level custom method to update the Live on Google status for multiple properties. Each call can turn on or off multiple hotels. To turn some hotels on and turn some hotels off, you will have to make multiple calls.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let account = "account_example"; // String | Required. The resource name of the account. The format is accounts/{account_id}.
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
  'setLiveOnGoogleRequest': new TravelPartnerApi.SetLiveOnGoogleRequest() // SetLiveOnGoogleRequest | 
};
apiInstance.travelpartnerAccountsHotelsSetLiveOnGoogle(account, opts, (error, data, response) => {
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
 **account** | **String**| Required. The resource name of the account. The format is accounts/{account_id}. | 
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
 **setLiveOnGoogleRequest** | [**SetLiveOnGoogleRequest**](SetLiveOnGoogleRequest.md)|  | [optional] 

### Return type

[**SetLiveOnGoogleResponse**](SetLiveOnGoogleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## travelpartnerAccountsIconsCreate

> Icon travelpartnerAccountsIconsCreate(parent, opts)



Uploads a new icon and starts its review process. Generates an &#x60;icon_id&#x60; and includes it in the icon&#39;s resource name, which is the format &#x60;accounts/{account_id}/icons/{icon_id}&#x60; Returns HTTP status 400 and doesn&#39;t trigger the review process if the icon has any of these conditions: * Image is not in PNG format, or not convertible to PNG format. * Size less than 72 pixels * Size greater than 1200 pixels * Aspect ratio other than 1:1

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | Required. The resource name of the partner account owning the icon. The format is `accounts/{account_id}`.
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
  'icon': new TravelPartnerApi.Icon() // Icon | 
};
apiInstance.travelpartnerAccountsIconsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the partner account owning the icon. The format is &#x60;accounts/{account_id}&#x60;. | 
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
 **icon** | [**Icon**](Icon.md)|  | [optional] 

### Return type

[**Icon**](Icon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## travelpartnerAccountsIconsList

> ListIconsResponse travelpartnerAccountsIconsList(parent, opts)



Returns the &#x60;Icon&#x60;s for a partner account.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | Required. The resource name of the queried partner account. The format is `accounts/{account_id}`.
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
apiInstance.travelpartnerAccountsIconsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the queried partner account. The format is &#x60;accounts/{account_id}&#x60;. | 
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

[**ListIconsResponse**](ListIconsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsListingsVerify

> VerifyListingsResponse travelpartnerAccountsListingsVerify(parent, opts)



returns verified listings with data issues and serving eligibilities

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
  'verifyListingsRequest': new TravelPartnerApi.VerifyListingsRequest() // VerifyListingsRequest | 
};
apiInstance.travelpartnerAccountsListingsVerify(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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
 **verifyListingsRequest** | [**VerifyListingsRequest**](VerifyListingsRequest.md)|  | [optional] 

### Return type

[**VerifyListingsResponse**](VerifyListingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## travelpartnerAccountsParticipationReportViewsQuery

> QueryParticipationReportResponse travelpartnerAccountsParticipationReportViewsQuery(name, opts)



Provides the ability to query (get, filter, and segment) a participation report for a particular account.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let name = "name_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
  'aggregateBy': "aggregateBy_example", // String | Specifies how to segment the metrics returned by the query. For example, if `userRegionCode` is specified as the `aggregate_by` value, the `participationResult` will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: `date`, `userRegionCode`, `deviceType`, `partnerHotelId`, `hotelRegionCode`, `advanceBookingWindow`, `lengthOfStayDays`, `checkinDate`, and `occupancy`. Fields that are not specified are not included in the ParticipationResult. Using an `aggregateBy` specification that produces a large number of rows will cause an error. This is especially true when aggregating by `partnerHotelId` or more than two fields. To reduce the possibiliy of an error, filter by `partnerHotelId` and `date` to only include a select number of hotels and dates. Accounts with a large number of hotels will need to further reduce data with more filtering.
  'filter': "filter_example", // String | The conditions (fields and expressions) used to filter the participation metrics for the account being queried. The syntax requires spaces surrounding the `in` operator. Otherwise, spaces can be omitted. Conditions can be joined using the `and` operator. The `date` field is required. All other fields are optional. Examples of valid conditions are as follows: * `advanceBookingWindow = 2` * `advanceBookingWindow >= 0` * `advanceBookingWindow <= 5` * `advanceBookingWindow between 1 and 5` * `checkinDate = '2020-10-01'` * `checkinDate >= '2020-10-01'` * `checkinDate <= '2020-10-01'` * `checkinDate between '2020-10-01' and '2020-10-05'` * `date = '2020-02-04'` * `date between '2020-02-04' and '2020-02-09'` * `deviceType = 'TABLET'` * `deviceType in ('MOBILE', 'TABLET')` * `hotelRegionCode = 'US'` * `hotelRegionCode in ('US', 'CA')` * `lengthOfStayDays = 2` * `lengthOfStayDays >= 0` * `lengthOfStayDays <= 5` * `lengthOfStayDays between 1 and 5` * `occupancy = 2` * `occupancy >= 0` * `occupancy <= 5` * `occupancy between 1 and 5` * `partnerHotelId = 'AAA'` * `partnerHotelId in ('AAA', 'BBB')` * `userRegionCode = 'US'` * `userRegionCode in ('US', 'CA')`
  'pageSize': 56, // Number | The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.
  'pageToken': "pageToken_example" // String | A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token.
};
apiInstance.travelpartnerAccountsParticipationReportViewsQuery(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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
 **aggregateBy** | **String**| Specifies how to segment the metrics returned by the query. For example, if &#x60;userRegionCode&#x60; is specified as the &#x60;aggregate_by&#x60; value, the &#x60;participationResult&#x60; will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: &#x60;date&#x60;, &#x60;userRegionCode&#x60;, &#x60;deviceType&#x60;, &#x60;partnerHotelId&#x60;, &#x60;hotelRegionCode&#x60;, &#x60;advanceBookingWindow&#x60;, &#x60;lengthOfStayDays&#x60;, &#x60;checkinDate&#x60;, and &#x60;occupancy&#x60;. Fields that are not specified are not included in the ParticipationResult. Using an &#x60;aggregateBy&#x60; specification that produces a large number of rows will cause an error. This is especially true when aggregating by &#x60;partnerHotelId&#x60; or more than two fields. To reduce the possibiliy of an error, filter by &#x60;partnerHotelId&#x60; and &#x60;date&#x60; to only include a select number of hotels and dates. Accounts with a large number of hotels will need to further reduce data with more filtering. | [optional] 
 **filter** | **String**| The conditions (fields and expressions) used to filter the participation metrics for the account being queried. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions can be joined using the &#x60;and&#x60; operator. The &#x60;date&#x60; field is required. All other fields are optional. Examples of valid conditions are as follows: * &#x60;advanceBookingWindow &#x3D; 2&#x60; * &#x60;advanceBookingWindow &gt;&#x3D; 0&#x60; * &#x60;advanceBookingWindow &lt;&#x3D; 5&#x60; * &#x60;advanceBookingWindow between 1 and 5&#x60; * &#x60;checkinDate &#x3D; &#39;2020-10-01&#39;&#x60; * &#x60;checkinDate &gt;&#x3D; &#39;2020-10-01&#39;&#x60; * &#x60;checkinDate &lt;&#x3D; &#39;2020-10-01&#39;&#x60; * &#x60;checkinDate between &#39;2020-10-01&#39; and &#39;2020-10-05&#39;&#x60; * &#x60;date &#x3D; &#39;2020-02-04&#39;&#x60; * &#x60;date between &#39;2020-02-04&#39; and &#39;2020-02-09&#39;&#x60; * &#x60;deviceType &#x3D; &#39;TABLET&#39;&#x60; * &#x60;deviceType in (&#39;MOBILE&#39;, &#39;TABLET&#39;)&#x60; * &#x60;hotelRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;hotelRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; * &#x60;lengthOfStayDays &#x3D; 2&#x60; * &#x60;lengthOfStayDays &gt;&#x3D; 0&#x60; * &#x60;lengthOfStayDays &lt;&#x3D; 5&#x60; * &#x60;lengthOfStayDays between 1 and 5&#x60; * &#x60;occupancy &#x3D; 2&#x60; * &#x60;occupancy &gt;&#x3D; 0&#x60; * &#x60;occupancy &lt;&#x3D; 5&#x60; * &#x60;occupancy between 1 and 5&#x60; * &#x60;partnerHotelId &#x3D; &#39;AAA&#39;&#x60; * &#x60;partnerHotelId in (&#39;AAA&#39;, &#39;BBB&#39;)&#x60; * &#x60;userRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;userRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token. | [optional] 

### Return type

[**QueryParticipationReportResponse**](QueryParticipationReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsPriceAccuracyViewsList

> ListPriceAccuracyViewsResponse travelpartnerAccountsPriceAccuracyViewsList(parent, opts)



Lists the available price accuracy views.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
apiInstance.travelpartnerAccountsPriceAccuracyViewsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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

[**ListPriceAccuracyViewsResponse**](ListPriceAccuracyViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsPriceAccuracyViewsSummarize

> SummarizePriceAccuracyResponse travelpartnerAccountsPriceAccuracyViewsSummarize(parent, opts)



Returns the price accuracy summary.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account that is being queried. The format is `accounts/{account_id}`.
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
apiInstance.travelpartnerAccountsPriceAccuracyViewsSummarize(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account that is being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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

[**SummarizePriceAccuracyResponse**](SummarizePriceAccuracyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsPriceCoverageViewsGetLatest

> PriceCoverageView travelpartnerAccountsPriceCoverageViewsGetLatest(parent, opts)



Returns the latest price coverage view in full detail.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
apiInstance.travelpartnerAccountsPriceCoverageViewsGetLatest(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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

[**PriceCoverageView**](PriceCoverageView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsPriceCoverageViewsList

> ListPriceCoverageViewsResponse travelpartnerAccountsPriceCoverageViewsList(parent, opts)



Returns the entire price coverage history.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
apiInstance.travelpartnerAccountsPriceCoverageViewsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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

[**ListPriceCoverageViewsResponse**](ListPriceCoverageViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsPropertyPerformanceReportViewsQuery

> QueryPropertyPerformanceReportResponse travelpartnerAccountsPropertyPerformanceReportViewsQuery(name, opts)



Provides the ability to query (get, filter, and segment) a property performance links report for a specific account.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let name = "name_example"; // String | The resource name of the account being queried. Format: accounts/{account_id}
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
  'aggregateBy': "aggregateBy_example", // String | Specifies how to segment the metrics returned by the query. For example, if `userRegionCode` is specified, the `PropertyPerformanceResult` will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: `advanceBookingWindow`, `brand`, `date`, `deviceType`, `highIntentUsers`, `lengthOfStay`, `propertyRegionCode`, `occupancy`, `partnerPropertyId`, `partnerPropertyDisplayName`, and `userRegionCode`. Only fields specified here are included in the PropertyPerformanceResult.
  'filter': "filter_example", // String | The conditions (fields and expressions) used to filter the property performance metrics for the account being queried. The syntax requires spaces surrounding the `in` operator. Otherwise, spaces can be omitted. Conditions can be joined using the `and` operator. The `date` field is required. All other fields are optional. The `date` field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for `partnerPropertyDisplayName` and `brand` are matched case-insensitively. Examples of valid conditions are as follows: * `advanceBookingWindow = 'ADVANCE_BOOKING_WINDOW_SAME_DAY'` * `advanceBookingWindow in ('ADVANCE_BOOKING_WINDOW_SAME_DAY', 'ADVANCE_BOOKING_WINDOW_DAYS_61_TO_90')` * `brand = 'Brand A'` * `brand in ('Brand A', 'brand B')` * `date = '2021-12-03'` * `date between '2021-12-03' and '2021-12-08'` * `deviceType = 'TABLET'` * `deviceType in ('MOBILE', 'TABLET')` * `highIntentUsers = 'TRUE'` * `highIntentUsers = 'FALSE'` * `lengthOfStay = 'LENGTH_OF_STAY_NIGHTS_2'` * `lengthOfStay in ('LENGTH_OF_STAY_NIGHTS_2', 'LENGTH_OF_STAY_NIGHTS_4_TO_7')` * `propertyRegionCode = 'US'` * `propertyRegionCode in ('US', 'CA')` * `occupancy = 'OCCUPANCY_2'` * `occupancy in ('OCCUPANCY_2', 'OCCUPANCY_OVER_4')` * `partnerPropertyId = 'AAA'` * `partnerPropertyId in ('AAA', 'BBB')` * `partnerPropertyDisplayName = 'hotel A'` * `partnerPropertyDisplayName in ('Hotel A', 'HOTEL b')` * `userRegionCode = 'US'` * `userRegionCode in ('US', 'CA')`
  'pageSize': 56, // Number | The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.
  'pageToken': "pageToken_example" // String | A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token.
};
apiInstance.travelpartnerAccountsPropertyPerformanceReportViewsQuery(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the account being queried. Format: accounts/{account_id} | 
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
 **aggregateBy** | **String**| Specifies how to segment the metrics returned by the query. For example, if &#x60;userRegionCode&#x60; is specified, the &#x60;PropertyPerformanceResult&#x60; will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: &#x60;advanceBookingWindow&#x60;, &#x60;brand&#x60;, &#x60;date&#x60;, &#x60;deviceType&#x60;, &#x60;highIntentUsers&#x60;, &#x60;lengthOfStay&#x60;, &#x60;propertyRegionCode&#x60;, &#x60;occupancy&#x60;, &#x60;partnerPropertyId&#x60;, &#x60;partnerPropertyDisplayName&#x60;, and &#x60;userRegionCode&#x60;. Only fields specified here are included in the PropertyPerformanceResult. | [optional] 
 **filter** | **String**| The conditions (fields and expressions) used to filter the property performance metrics for the account being queried. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions can be joined using the &#x60;and&#x60; operator. The &#x60;date&#x60; field is required. All other fields are optional. The &#x60;date&#x60; field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for &#x60;partnerPropertyDisplayName&#x60; and &#x60;brand&#x60; are matched case-insensitively. Examples of valid conditions are as follows: * &#x60;advanceBookingWindow &#x3D; &#39;ADVANCE_BOOKING_WINDOW_SAME_DAY&#39;&#x60; * &#x60;advanceBookingWindow in (&#39;ADVANCE_BOOKING_WINDOW_SAME_DAY&#39;, &#39;ADVANCE_BOOKING_WINDOW_DAYS_61_TO_90&#39;)&#x60; * &#x60;brand &#x3D; &#39;Brand A&#39;&#x60; * &#x60;brand in (&#39;Brand A&#39;, &#39;brand B&#39;)&#x60; * &#x60;date &#x3D; &#39;2021-12-03&#39;&#x60; * &#x60;date between &#39;2021-12-03&#39; and &#39;2021-12-08&#39;&#x60; * &#x60;deviceType &#x3D; &#39;TABLET&#39;&#x60; * &#x60;deviceType in (&#39;MOBILE&#39;, &#39;TABLET&#39;)&#x60; * &#x60;highIntentUsers &#x3D; &#39;TRUE&#39;&#x60; * &#x60;highIntentUsers &#x3D; &#39;FALSE&#39;&#x60; * &#x60;lengthOfStay &#x3D; &#39;LENGTH_OF_STAY_NIGHTS_2&#39;&#x60; * &#x60;lengthOfStay in (&#39;LENGTH_OF_STAY_NIGHTS_2&#39;, &#39;LENGTH_OF_STAY_NIGHTS_4_TO_7&#39;)&#x60; * &#x60;propertyRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;propertyRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; * &#x60;occupancy &#x3D; &#39;OCCUPANCY_2&#39;&#x60; * &#x60;occupancy in (&#39;OCCUPANCY_2&#39;, &#39;OCCUPANCY_OVER_4&#39;)&#x60; * &#x60;partnerPropertyId &#x3D; &#39;AAA&#39;&#x60; * &#x60;partnerPropertyId in (&#39;AAA&#39;, &#39;BBB&#39;)&#x60; * &#x60;partnerPropertyDisplayName &#x3D; &#39;hotel A&#39;&#x60; * &#x60;partnerPropertyDisplayName in (&#39;Hotel A&#39;, &#39;HOTEL b&#39;)&#x60; * &#x60;userRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;userRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; | [optional] 
 **pageSize** | **Number**| The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token. | [optional] 

### Return type

[**QueryPropertyPerformanceReportResponse**](QueryPropertyPerformanceReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsReconciliationReportsCreate

> CreateReconciliationReportResponse travelpartnerAccountsReconciliationReportsCreate(parent, opts)



Creates a reconciliation report and uploads it to Google.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
  'reconciliationReport': new TravelPartnerApi.ReconciliationReport() // ReconciliationReport | 
};
apiInstance.travelpartnerAccountsReconciliationReportsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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
 **reconciliationReport** | [**ReconciliationReport**](ReconciliationReport.md)|  | [optional] 

### Return type

[**CreateReconciliationReportResponse**](CreateReconciliationReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## travelpartnerAccountsReconciliationReportsGet

> ReconciliationReport travelpartnerAccountsReconciliationReportsGet(name, opts)



Returns a reconciliation report.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let name = "name_example"; // String | The resource name of the reconciliation report to fetch. The format is `accounts/{account_id}/reconciliationReports/{datetime}~{filename}`.
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
  'includeMatchedPrices': true, // Boolean | Set to true if matched prices are to be added into the report.
  'includeNonScoring': true, // Boolean | Set to true if non-account impacting rows are to be added into the report.
  'includePixels': true // Boolean | Set to true if pixel signals are to be added into the report.
};
apiInstance.travelpartnerAccountsReconciliationReportsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the reconciliation report to fetch. The format is &#x60;accounts/{account_id}/reconciliationReports/{datetime}~{filename}&#x60;. | 
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
 **includeMatchedPrices** | **Boolean**| Set to true if matched prices are to be added into the report. | [optional] 
 **includeNonScoring** | **Boolean**| Set to true if non-account impacting rows are to be added into the report. | [optional] 
 **includePixels** | **Boolean**| Set to true if pixel signals are to be added into the report. | [optional] 

### Return type

[**ReconciliationReport**](ReconciliationReport.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsReconciliationReportsList

> ListReconciliationReportsResponse travelpartnerAccountsReconciliationReportsList(parent, opts)



Returns a list of the names of created reconciliation reports.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
  'endDate': "endDate_example", // String | End of date range to fetch files for. Format is yyyy-mm-dd[THH[:MM[:SS]]]. If empty, reports until the end of time are fetched.
  'startDate': "startDate_example" // String | Beginning of date range to fetch files for. Format is yyyy-MM-dd[THH[:mm[:SS]]]. If empty, reports from the beginning of time onwards are fetched.
};
apiInstance.travelpartnerAccountsReconciliationReportsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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
 **endDate** | **String**| End of date range to fetch files for. Format is yyyy-mm-dd[THH[:MM[:SS]]]. If empty, reports until the end of time are fetched. | [optional] 
 **startDate** | **String**| Beginning of date range to fetch files for. Format is yyyy-MM-dd[THH[:mm[:SS]]]. If empty, reports from the beginning of time onwards are fetched. | [optional] 

### Return type

[**ListReconciliationReportsResponse**](ListReconciliationReportsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelpartnerAccountsReconciliationReportsValidate

> ValidateReconciliationReportResponse travelpartnerAccountsReconciliationReportsValidate(parent, opts)



Validates a reconciliation report.

### Example

```javascript
import TravelPartnerApi from 'travel_partner_api';

let apiInstance = new TravelPartnerApi.AccountsApi();
let parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
  'reconciliationReport': new TravelPartnerApi.ReconciliationReport() // ReconciliationReport | 
};
apiInstance.travelpartnerAccountsReconciliationReportsValidate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | 
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
 **reconciliationReport** | [**ReconciliationReport**](ReconciliationReport.md)|  | [optional] 

### Return type

[**ValidateReconciliationReportResponse**](ValidateReconciliationReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

