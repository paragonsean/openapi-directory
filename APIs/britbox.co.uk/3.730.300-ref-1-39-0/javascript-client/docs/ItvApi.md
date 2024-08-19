# RocketServices.ItvApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activateSaveOffer**](ItvApi.md#activateSaveOffer) | **POST** /itv/save-offer | 
[**changeCardDetails**](ItvApi.md#changeCardDetails) | **PUT** /itv/cards/{platform} | 
[**changeEmail**](ItvApi.md#changeEmail) | **POST** /itv/changeemail | 
[**changeMarketing**](ItvApi.md#changeMarketing) | **POST** /itv/changemarketing | 
[**checkPreviousEntitlements**](ItvApi.md#checkPreviousEntitlements) | **GET** /itv/had/entitlements | 
[**checkVoucher**](ItvApi.md#checkVoucher) | **POST** /itv/voucher/{platform} | 
[**confirmPurchase**](ItvApi.md#confirmPurchase) | **POST** /itv/purchase/{platform} | 
[**confirmPurchaseStrong**](ItvApi.md#confirmPurchaseStrong) | **POST** /itv/purchase/{platform}/strong | 
[**confirmPurchaseWithOffer**](ItvApi.md#confirmPurchaseWithOffer) | **POST** /itv/purchase/{platform}/withoffer | 
[**deleteAccount**](ItvApi.md#deleteAccount) | **POST** /itv/deleteaccount | 
[**executeTransaction**](ItvApi.md#executeTransaction) | **POST** /itv/roku/transaction/{transactionid} | 
[**getAccountTokenWithPin**](ItvApi.md#getAccountTokenWithPin) | **POST** /itv/pinauthorization | 
[**getBillingHistory**](ItvApi.md#getBillingHistory) | **POST** /itv/billinghistory/{platform} | 
[**getCardDetails**](ItvApi.md#getCardDetails) | **POST** /itv/cards/{platform} | 
[**getCurrentEntitlement**](ItvApi.md#getCurrentEntitlement) | **GET** /itv/entitlements/current | 
[**getCurrentSubscription**](ItvApi.md#getCurrentSubscription) | **GET** /itv/purchase/{platform} | 
[**getEntitlementsHistory**](ItvApi.md#getEntitlementsHistory) | **GET** /itv/entitlements/history | 
[**getFeatureFlag**](ItvApi.md#getFeatureFlag) | **GET** /itv/featureFlag/{feature} | 
[**getFullPriceRenewal**](ItvApi.md#getFullPriceRenewal) | **GET** /itv/subscription/fullpricerenewal | 
[**getItvProfileToken**](ItvApi.md#getItvProfileToken) | **POST** /itv/profiletoken | 
[**getPublicPreview**](ItvApi.md#getPublicPreview) | **GET** /samsung-preview | 
[**getRecommendedList**](ItvApi.md#getRecommendedList) | **GET** /itv/profile/recommendation/list | 
[**getSaveOffer**](ItvApi.md#getSaveOffer) | **GET** /itv/save-offer | 
[**getSubscriptionState**](ItvApi.md#getSubscriptionState) | **GET** /itv/subscriptionstate | 
[**getSubscriptionStatus**](ItvApi.md#getSubscriptionStatus) | **GET** /itv/subscription/status/{platform} | 
[**getUpcomingInvoice**](ItvApi.md#getUpcomingInvoice) | **GET** /itv/upcominginvoice | 
[**getVoucherById**](ItvApi.md#getVoucherById) | **GET** /itv/voucher/{planId}/{voucherId} | 
[**googlePaySubscription**](ItvApi.md#googlePaySubscription) | **POST** /itv/googlepay/subscription | 
[**itvItemsummaryExternalIdGet**](ItvApi.md#itvItemsummaryExternalIdGet) | **GET** /itv/itemsummary/{externalId} | 
[**itvPlansPlatformGet**](ItvApi.md#itvPlansPlatformGet) | **GET** /itv/plans/{platform} | 
[**itvProfileGet**](ItvApi.md#itvProfileGet) | **GET** /itv/profile | 
[**itvPurchasePlatformDelete**](ItvApi.md#itvPurchasePlatformDelete) | **DELETE** /itv/purchase/{platform} | 
[**itvRokuPlansGet**](ItvApi.md#itvRokuPlansGet) | **GET** /itv/roku/plans | 
[**resubscribe**](ItvApi.md#resubscribe) | **POST** /itv/resubscribe/{platform} | 
[**updatePaymentIntentStrong**](ItvApi.md#updatePaymentIntentStrong) | **PUT** /itv/updateIntent/strong/{platform} | 
[**updatePaymentMethodStrong**](ItvApi.md#updatePaymentMethodStrong) | **PUT** /itv/updatePayment/strong/{platform} | 
[**updateProfile**](ItvApi.md#updateProfile) | **PUT** /itv/profile | 
[**upgradePlan**](ItvApi.md#upgradePlan) | **POST** /itv/plan/{platform} | 



## activateSaveOffer

> activateSaveOffer(body, opts)



Activates the discount for a user. Only Stripe platform is currently supported.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let body = "body_example"; // String | The coupon id to be checked.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.activateSaveOffer(body, opts, (error, data, response) => {
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
 **body** | **String**| The coupon id to be checked. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changeCardDetails

> changeCardDetails(platform, itvChangeCardDetailsRequest, opts)



Change payment card details.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let itvChangeCardDetailsRequest = new RocketServices.ItvChangeCardDetailsRequest(); // ItvChangeCardDetailsRequest | Details of change card details request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.changeCardDetails(platform, itvChangeCardDetailsRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **itvChangeCardDetailsRequest** | [**ItvChangeCardDetailsRequest**](ItvChangeCardDetailsRequest.md)| Details of change card details request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changeEmail

> changeEmail(itvChangeEmailRequest, opts)



Change email address related to account/profile.  The expected token scope is Settings. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let itvChangeEmailRequest = "itvChangeEmailRequest_example"; // ItvChangeEmailRequest | New email address & ITV profile token.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.changeEmail(itvChangeEmailRequest, opts, (error, data, response) => {
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
 **itvChangeEmailRequest** | [**ItvChangeEmailRequest**](ItvChangeEmailRequest.md)| New email address &amp; ITV profile token. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changeMarketing

> changeMarketing(itvChangeMarketingRequest, opts)



Change marketing preferences related to account/profile.  The expected token scope is Settings. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let itvChangeMarketingRequest = "itvChangeMarketingRequest_example"; // ItvChangeMarketingRequest | Updated marketing preferences & ITV profile token.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.changeMarketing(itvChangeMarketingRequest, opts, (error, data, response) => {
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
 **itvChangeMarketingRequest** | [**ItvChangeMarketingRequest**](ItvChangeMarketingRequest.md)| Updated marketing preferences &amp; ITV profile token. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkPreviousEntitlements

> ItvHadEntitlement checkPreviousEntitlements(opts)



Check whether the user has been previously entitled.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.checkPreviousEntitlements(opts, (error, data, response) => {
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
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvHadEntitlement**](ItvHadEntitlement.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkVoucher

> ItvVoucher checkVoucher(platform, itvVoucherRequest, opts)



Validates the coupon/voucher for specified payment platform.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let itvVoucherRequest = new RocketServices.ItvVoucherRequest(); // ItvVoucherRequest | Coupon/voucher.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.checkVoucher(platform, itvVoucherRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **itvVoucherRequest** | [**ItvVoucherRequest**](ItvVoucherRequest.md)| Coupon/voucher. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvVoucher**](ItvVoucher.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## confirmPurchase

> ItvPurchase confirmPurchase(platform, itvPurchaseRequest, opts)



Confirms purchase and returns the details of purchased subscription for specified payment platform.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let itvPurchaseRequest = new RocketServices.ItvPurchaseRequest(); // ItvPurchaseRequest | Details of a purchase request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.confirmPurchase(platform, itvPurchaseRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **itvPurchaseRequest** | [**ItvPurchaseRequest**](ItvPurchaseRequest.md)| Details of a purchase request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvPurchase**](ItvPurchase.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## confirmPurchaseStrong

> ItvPurchaseStrongResponse confirmPurchaseStrong(platform, itvPurchaseStrongRequest, opts)



Confirms purchase and returns the details of purchased subscription for specified payment platform.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let itvPurchaseStrongRequest = new RocketServices.ItvPurchaseStrongRequest(); // ItvPurchaseStrongRequest | Details of a purchase request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.confirmPurchaseStrong(platform, itvPurchaseStrongRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **itvPurchaseStrongRequest** | [**ItvPurchaseStrongRequest**](ItvPurchaseStrongRequest.md)| Details of a purchase request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvPurchaseStrongResponse**](ItvPurchaseStrongResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## confirmPurchaseWithOffer

> ItvPurchaseWithOfferResponse confirmPurchaseWithOffer(platform, itvPurchaseWithOfferRequest, opts)



Confirms purchase and returns the details of purchased subscription for specified payment platform.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let itvPurchaseWithOfferRequest = new RocketServices.ItvPurchaseWithOfferRequest(); // ItvPurchaseWithOfferRequest | Details of a purchase request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.confirmPurchaseWithOffer(platform, itvPurchaseWithOfferRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **itvPurchaseWithOfferRequest** | [**ItvPurchaseWithOfferRequest**](ItvPurchaseWithOfferRequest.md)| Details of a purchase request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvPurchaseWithOfferResponse**](ItvPurchaseWithOfferResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccount

> deleteAccount(itvDeleteAccountRequest, opts)



Delete account in compliance with GDPR.  The expected token scope is Settings. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let itvDeleteAccountRequest = "itvDeleteAccountRequest_example"; // ItvDeleteAccountRequest | New email address & ITV profile token.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.deleteAccount(itvDeleteAccountRequest, opts, (error, data, response) => {
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
 **itvDeleteAccountRequest** | [**ItvDeleteAccountRequest**](ItvDeleteAccountRequest.md)| New email address &amp; ITV profile token. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## executeTransaction

> executeTransaction(transactionid, itvRokuTransactionRequest, opts)



Sends request to execute specified transaction.

### Example

```javascript
import RocketServices from 'rocket_services';

let apiInstance = new RocketServices.ItvApi();
let transactionid = "transactionid_example"; // String | The identifier of the Roku transaction (subscribe/upgrade/downgrade/cancellation).
let itvRokuTransactionRequest = new RocketServices.ItvRokuTransactionRequest(); // ItvRokuTransactionRequest | Details of a transaction request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.executeTransaction(transactionid, itvRokuTransactionRequest, opts, (error, data, response) => {
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
 **transactionid** | **String**| The identifier of the Roku transaction (subscribe/upgrade/downgrade/cancellation). | 
 **itvRokuTransactionRequest** | [**ItvRokuTransactionRequest**](ItvRokuTransactionRequest.md)| Details of a transaction request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccountTokenWithPin

> [AccessToken] getAccountTokenWithPin(itvPinAuthRequest, opts)



Provides authorization with parental control pin.  Returns an array containing account token with Playback scope.  Requires access token with Catalog scope.  Pin must be a 4-digit string 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let itvPinAuthRequest = new RocketServices.ItvPinAuthRequest(); // ItvPinAuthRequest | Details of token request.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getAccountTokenWithPin(itvPinAuthRequest, opts, (error, data, response) => {
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
 **itvPinAuthRequest** | [**ItvPinAuthRequest**](ItvPinAuthRequest.md)| Details of token request. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**[AccessToken]**](AccessToken.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getBillingHistory

> ItvBillingHistory getBillingHistory(platform, itvBillingHistoryRequest, opts)



Returns the list of billing records for specified payment platform.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let itvBillingHistoryRequest = new RocketServices.ItvBillingHistoryRequest(); // ItvBillingHistoryRequest | Details of a billing history request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getBillingHistory(platform, itvBillingHistoryRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **itvBillingHistoryRequest** | [**ItvBillingHistoryRequest**](ItvBillingHistoryRequest.md)| Details of a billing history request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvBillingHistory**](ItvBillingHistory.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCardDetails

> ItvCardDetails getCardDetails(platform, itvGetCardDetailsRequest, opts)



Get payment card details.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let itvGetCardDetailsRequest = new RocketServices.ItvGetCardDetailsRequest(); // ItvGetCardDetailsRequest | ITV profile token in body.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getCardDetails(platform, itvGetCardDetailsRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **itvGetCardDetailsRequest** | [**ItvGetCardDetailsRequest**](ItvGetCardDetailsRequest.md)| ITV profile token in body. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvCardDetails**](ItvCardDetails.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCurrentEntitlement

> ItvEntitlementCurrent getCurrentEntitlement(opts)



Returns current entitlement.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getCurrentEntitlement(opts, (error, data, response) => {
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
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvEntitlementCurrent**](ItvEntitlementCurrent.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCurrentSubscription

> ItvCurrentSubscription getCurrentSubscription(platform, opts)



Returns the details of current subscription for specified payment platform.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getCurrentSubscription(platform, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvCurrentSubscription**](ItvCurrentSubscription.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEntitlementsHistory

> ItvEntitlementsHistory getEntitlementsHistory(opts)



Returns the state of subscription for any payment platform.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getEntitlementsHistory(opts, (error, data, response) => {
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
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvEntitlementsHistory**](ItvEntitlementsHistory.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFeatureFlag

> ItvFeatureFlag getFeatureFlag(feature, opts)



Gets info whether or not a feature is enabled or disabled using a feature flag. Feature flags are set as a custom field within PM. It also supports custom feature flag data if needed. Such data can be return as well.

### Example

```javascript
import RocketServices from 'rocket_services';

let apiInstance = new RocketServices.ItvApi();
let feature = "feature_example"; // String | The identifier of the feature to check for feature flag.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getFeatureFlag(feature, opts, (error, data, response) => {
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
 **feature** | **String**| The identifier of the feature to check for feature flag. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvFeatureFlag**](ItvFeatureFlag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFullPriceRenewal

> ItvSubscriptionFullPriceRenewal getFullPriceRenewal(opts)



Returns full price renewal state and reason for specific user.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getFullPriceRenewal(opts, (error, data, response) => {
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
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvSubscriptionFullPriceRenewal**](ItvSubscriptionFullPriceRenewal.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItvProfileToken

> ItvProfileToken getItvProfileToken(itvProfileTokenRequest, opts)



Returns the ITV profile token.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let itvProfileTokenRequest = new RocketServices.ItvProfileTokenRequest(); // ItvProfileTokenRequest | Details of token request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getItvProfileToken(itvProfileTokenRequest, opts, (error, data, response) => {
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
 **itvProfileTokenRequest** | [**ItvProfileTokenRequest**](ItvProfileTokenRequest.md)| Details of token request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvProfileToken**](ItvProfileToken.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getPublicPreview

> SamsungPreview getPublicPreview()



Returns public preview for Samsung based on the page &#39;/samsung-preview&#39; configured in PresentationManager. There is a hard limit of max 40 items to be returned. It splits evenly items count into the page rows, remaining items are added into the first row. 

### Example

```javascript
import RocketServices from 'rocket_services';

let apiInstance = new RocketServices.ItvApi();
apiInstance.getPublicPreview((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SamsungPreview**](SamsungPreview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecommendedList

> ItemList getRecommendedList(opts)



Get the list of recommended items under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'itemTypes': ["null"], // [String] | List of item types to filter the recommendation list
  'page': 1, // Number | The page of items to load. Starts from page 1.
  'pageSize': 12, // Number | The number of items to return in a page.
  'device': "'web_browser'", // String | The type of device the content is targeting.
  'sub': "sub_example", // String | The active subscription code.
  'segments': ["null"], // [String] | The list of segments to filter the response by.
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getRecommendedList(opts, (error, data, response) => {
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
 **itemTypes** | [**[String]**](String.md)| List of item types to filter the recommendation list | [optional] 
 **page** | **Number**| The page of items to load. Starts from page 1. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return in a page. | [optional] [default to 12]
 **device** | **String**| The type of device the content is targeting. | [optional] [default to &#39;web_browser&#39;]
 **sub** | **String**| The active subscription code. | [optional] 
 **segments** | [**[String]**](String.md)| The list of segments to filter the response by. | [optional] 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItemList**](ItemList.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSaveOffer

> ItvGetDiscountResponse getSaveOffer(opts)



Checks the provided coupon id for a user. Only Stripe platform is currently supported.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getSaveOffer(opts, (error, data, response) => {
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
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvGetDiscountResponse**](ItvGetDiscountResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubscriptionState

> ItvSubscriptionState getSubscriptionState(opts)



Returns the state of subscription for any payment platform.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getSubscriptionState(opts, (error, data, response) => {
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
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvSubscriptionState**](ItvSubscriptionState.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubscriptionStatus

> ItvSubscriptionStatusResponse getSubscriptionStatus(platform, opts)



Returns status of latest payment intent.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getSubscriptionStatus(platform, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvSubscriptionStatusResponse**](ItvSubscriptionStatusResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUpcomingInvoice

> ItvGetDiscountResponse getUpcomingInvoice(opts)



Returns an upcoming invoice

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getUpcomingInvoice(opts, (error, data, response) => {
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
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvGetDiscountResponse**](ItvGetDiscountResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoucherById

> ItvVoucher getVoucherById(voucherId, planId, opts)



Checks the provided coupon id for a user. Only Stripe platform is currently supported.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let voucherId = "voucherId_example"; // String | The identifier of the voucher.
let planId = "planId_example"; // String | The identifier of the plan.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getVoucherById(voucherId, planId, opts, (error, data, response) => {
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
 **voucherId** | **String**| The identifier of the voucher. | 
 **planId** | **String**| The identifier of the plan. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvVoucher**](ItvVoucher.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## googlePaySubscription

> googlePaySubscription(itvGooglePaySubscriptionRequest, opts)



Get the list of recommended items under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let itvGooglePaySubscriptionRequest = new RocketServices.ItvGooglePaySubscriptionRequest(); // ItvGooglePaySubscriptionRequest | Details of googlePay subscription request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.googlePaySubscription(itvGooglePaySubscriptionRequest, opts, (error, data, response) => {
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
 **itvGooglePaySubscriptionRequest** | [**ItvGooglePaySubscriptionRequest**](ItvGooglePaySubscriptionRequest.md)| Details of googlePay subscription request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## itvItemsummaryExternalIdGet

> ServiceError itvItemsummaryExternalIdGet(externalId)



Redirects to corresponding Axis Item details page.

### Example

```javascript
import RocketServices from 'rocket_services';

let apiInstance = new RocketServices.ItvApi();
let externalId = "externalId_example"; // String | The external identifier of the item.
apiInstance.itvItemsummaryExternalIdGet(externalId, (error, data, response) => {
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
 **externalId** | **String**| The external identifier of the item. | 

### Return type

[**ServiceError**](ServiceError.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## itvPlansPlatformGet

> ItvPlans itvPlansPlatformGet(platform, opts)



Returns the plans available for specified payment platform.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.itvPlansPlatformGet(platform, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvPlans**](ItvPlans.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## itvProfileGet

> Object itvProfileGet(opts)



Returns the ITV profile object.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.itvProfileGet(opts, (error, data, response) => {
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
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

**Object**

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## itvPurchasePlatformDelete

> itvPurchasePlatformDelete(platform, itvCancelSubscriptionRequest, opts)



Cancel a plan subscription.  A cancelled subscription will continue to be valid until the subscription expiry date or next renewal date. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
let itvCancelSubscriptionRequest = new RocketServices.ItvCancelSubscriptionRequest(); // ItvCancelSubscriptionRequest | Details of a cancellation request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.itvPurchasePlatformDelete(platform, itvCancelSubscriptionRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). | 
 **itvCancelSubscriptionRequest** | [**ItvCancelSubscriptionRequest**](ItvCancelSubscriptionRequest.md)| Details of a cancellation request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itvRokuPlansGet

> RokuPlans itvRokuPlansGet(opts)



Gets available Roku plans.

### Example

```javascript
import RocketServices from 'rocket_services';

let apiInstance = new RocketServices.ItvApi();
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.itvRokuPlansGet(opts, (error, data, response) => {
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
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**RokuPlans**](RokuPlans.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resubscribe

> Object resubscribe(planId, platform, opts)



Resubscription for a user.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let planId = "planId_example"; // String | The id of the plan to renew.
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes). Only stripe is currently supported.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.resubscribe(planId, platform, opts, (error, data, response) => {
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
 **planId** | **String**| The id of the plan to renew. | 
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). Only stripe is currently supported. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

**Object**

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePaymentIntentStrong

> ItvUpdateIntentStrongResponse updatePaymentIntentStrong(platform, itvUpdateIntentStrongRequest, opts)



Change payment method details.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe only is currently supported).
let itvUpdateIntentStrongRequest = new RocketServices.ItvUpdateIntentStrongRequest(); // ItvUpdateIntentStrongRequest | Details of change card details request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.updatePaymentIntentStrong(platform, itvUpdateIntentStrongRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe only is currently supported). | 
 **itvUpdateIntentStrongRequest** | [**ItvUpdateIntentStrongRequest**](ItvUpdateIntentStrongRequest.md)| Details of change card details request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItvUpdateIntentStrongResponse**](ItvUpdateIntentStrongResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePaymentMethodStrong

> updatePaymentMethodStrong(platform, itvUpdatePaymentStrongRequest, opts)



Change payment method details.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe only is currently supported).
let itvUpdatePaymentStrongRequest = new RocketServices.ItvUpdatePaymentStrongRequest(); // ItvUpdatePaymentStrongRequest | Details of change card details request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.updatePaymentMethodStrong(platform, itvUpdatePaymentStrongRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe only is currently supported). | 
 **itvUpdatePaymentStrongRequest** | [**ItvUpdatePaymentStrongRequest**](ItvUpdatePaymentStrongRequest.md)| Details of change card details request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProfile

> updateProfile(itvUpdateProfileRequest, opts)



Update ITV profile.  The expected token scope is Settings. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let itvUpdateProfileRequest = "itvUpdateProfileRequest_example"; // ItvUpdateProfileRequest | ITV profile object with updated values & ITV profile token.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.updateProfile(itvUpdateProfileRequest, opts, (error, data, response) => {
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
 **itvUpdateProfileRequest** | [**ItvUpdateProfileRequest**](ItvUpdateProfileRequest.md)| ITV profile object with updated values &amp; ITV profile token. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upgradePlan

> upgradePlan(platform, itvUpgradePlanRequest, opts)



Upgrades the plan for the current user.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: accountAuth
let accountAuth = defaultClient.authentications['accountAuth'];
accountAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ItvApi();
let platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes). Only Stripe is supported
let itvUpgradePlanRequest = new RocketServices.ItvUpgradePlanRequest(); // ItvUpgradePlanRequest | Details of an upgrade request.
let opts = {
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.upgradePlan(platform, itvUpgradePlanRequest, opts, (error, data, response) => {
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
 **platform** | **String**| The identifier of the payment platform (stripe/itunes). Only Stripe is supported | 
 **itvUpgradePlanRequest** | [**ItvUpgradePlanRequest**](ItvUpgradePlanRequest.md)| Details of an upgrade request. | 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

