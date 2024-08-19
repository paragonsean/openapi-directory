# ItvApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateSaveOffer**](ItvApi.md#activateSaveOffer) | **POST** /itv/save-offer |  |
| [**changeCardDetails**](ItvApi.md#changeCardDetails) | **PUT** /itv/cards/{platform} |  |
| [**changeEmail**](ItvApi.md#changeEmail) | **POST** /itv/changeemail |  |
| [**changeMarketing**](ItvApi.md#changeMarketing) | **POST** /itv/changemarketing |  |
| [**checkPreviousEntitlements**](ItvApi.md#checkPreviousEntitlements) | **GET** /itv/had/entitlements |  |
| [**checkVoucher**](ItvApi.md#checkVoucher) | **POST** /itv/voucher/{platform} |  |
| [**confirmPurchase**](ItvApi.md#confirmPurchase) | **POST** /itv/purchase/{platform} |  |
| [**confirmPurchaseStrong**](ItvApi.md#confirmPurchaseStrong) | **POST** /itv/purchase/{platform}/strong |  |
| [**confirmPurchaseWithOffer**](ItvApi.md#confirmPurchaseWithOffer) | **POST** /itv/purchase/{platform}/withoffer |  |
| [**deleteAccount**](ItvApi.md#deleteAccount) | **POST** /itv/deleteaccount |  |
| [**executeTransaction**](ItvApi.md#executeTransaction) | **POST** /itv/roku/transaction/{transactionid} |  |
| [**getAccountTokenWithPin**](ItvApi.md#getAccountTokenWithPin) | **POST** /itv/pinauthorization |  |
| [**getBillingHistory**](ItvApi.md#getBillingHistory) | **POST** /itv/billinghistory/{platform} |  |
| [**getCardDetails**](ItvApi.md#getCardDetails) | **POST** /itv/cards/{platform} |  |
| [**getCurrentEntitlement**](ItvApi.md#getCurrentEntitlement) | **GET** /itv/entitlements/current |  |
| [**getCurrentSubscription**](ItvApi.md#getCurrentSubscription) | **GET** /itv/purchase/{platform} |  |
| [**getEntitlementsHistory**](ItvApi.md#getEntitlementsHistory) | **GET** /itv/entitlements/history |  |
| [**getFeatureFlag**](ItvApi.md#getFeatureFlag) | **GET** /itv/featureFlag/{feature} |  |
| [**getFullPriceRenewal**](ItvApi.md#getFullPriceRenewal) | **GET** /itv/subscription/fullpricerenewal |  |
| [**getItvProfileToken**](ItvApi.md#getItvProfileToken) | **POST** /itv/profiletoken |  |
| [**getPublicPreview**](ItvApi.md#getPublicPreview) | **GET** /samsung-preview |  |
| [**getRecommendedList**](ItvApi.md#getRecommendedList) | **GET** /itv/profile/recommendation/list |  |
| [**getSaveOffer**](ItvApi.md#getSaveOffer) | **GET** /itv/save-offer |  |
| [**getSubscriptionState**](ItvApi.md#getSubscriptionState) | **GET** /itv/subscriptionstate |  |
| [**getSubscriptionStatus**](ItvApi.md#getSubscriptionStatus) | **GET** /itv/subscription/status/{platform} |  |
| [**getUpcomingInvoice**](ItvApi.md#getUpcomingInvoice) | **GET** /itv/upcominginvoice |  |
| [**getVoucherById**](ItvApi.md#getVoucherById) | **GET** /itv/voucher/{planId}/{voucherId} |  |
| [**googlePaySubscription**](ItvApi.md#googlePaySubscription) | **POST** /itv/googlepay/subscription |  |
| [**itvItemsummaryExternalIdGet**](ItvApi.md#itvItemsummaryExternalIdGet) | **GET** /itv/itemsummary/{externalId} |  |
| [**itvPlansPlatformGet**](ItvApi.md#itvPlansPlatformGet) | **GET** /itv/plans/{platform} |  |
| [**itvProfileGet**](ItvApi.md#itvProfileGet) | **GET** /itv/profile |  |
| [**itvPurchasePlatformDelete**](ItvApi.md#itvPurchasePlatformDelete) | **DELETE** /itv/purchase/{platform} |  |
| [**itvRokuPlansGet**](ItvApi.md#itvRokuPlansGet) | **GET** /itv/roku/plans |  |
| [**resubscribe**](ItvApi.md#resubscribe) | **POST** /itv/resubscribe/{platform} |  |
| [**updatePaymentIntentStrong**](ItvApi.md#updatePaymentIntentStrong) | **PUT** /itv/updateIntent/strong/{platform} |  |
| [**updatePaymentMethodStrong**](ItvApi.md#updatePaymentMethodStrong) | **PUT** /itv/updatePayment/strong/{platform} |  |
| [**updateProfile**](ItvApi.md#updateProfile) | **PUT** /itv/profile |  |
| [**upgradePlan**](ItvApi.md#upgradePlan) | **POST** /itv/plan/{platform} |  |


<a id="activateSaveOffer"></a>
# **activateSaveOffer**
> activateSaveOffer(body, lang)



Activates the discount for a user. Only Stripe platform is currently supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String body = "body_example"; // String | The coupon id to be checked.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.activateSaveOffer(body, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#activateSaveOffer");
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
| **body** | **String**| The coupon id to be checked. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Authentication  passes, the user has an active subscription and the coupon id is valid. The response body is the updated subscription object. |  -  |
| **401** | Unauthorised. In the case of a token this can happen if the token is missing, invalid, or if the token bearer does not match the user in the path. |  -  |
| **404** | The customer could not be found.The customer does not have an active subscription. The coupon could not be found. |  -  |
| **406** | Invalid Token/Customer Not Eligible for Offer. |  -  |

<a id="changeCardDetails"></a>
# **changeCardDetails**
> changeCardDetails(platform, itvChangeCardDetailsRequest, lang)



Change payment card details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    ItvChangeCardDetailsRequest itvChangeCardDetailsRequest = new ItvChangeCardDetailsRequest(); // ItvChangeCardDetailsRequest | Details of change card details request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.changeCardDetails(platform, itvChangeCardDetailsRequest, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#changeCardDetails");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **itvChangeCardDetailsRequest** | [**ItvChangeCardDetailsRequest**](ItvChangeCardDetailsRequest.md)| Details of change card details request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="changeEmail"></a>
# **changeEmail**
> changeEmail(itvChangeEmailRequest, ff, lang)



Change email address related to account/profile.  The expected token scope is Settings. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    ItvChangeEmailRequest itvChangeEmailRequest = new ItvChangeEmailRequest(); // ItvChangeEmailRequest | New email address & ITV profile token.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.changeEmail(itvChangeEmailRequest, ff, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#changeEmail");
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
| **itvChangeEmailRequest** | [**ItvChangeEmailRequest**](ItvChangeEmailRequest.md)| New email address &amp; ITV profile token. | |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="changeMarketing"></a>
# **changeMarketing**
> changeMarketing(itvChangeMarketingRequest, ff, lang)



Change marketing preferences related to account/profile.  The expected token scope is Settings. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    ItvChangeMarketingRequest itvChangeMarketingRequest = new ItvChangeMarketingRequest(); // ItvChangeMarketingRequest | Updated marketing preferences & ITV profile token.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.changeMarketing(itvChangeMarketingRequest, ff, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#changeMarketing");
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
| **itvChangeMarketingRequest** | [**ItvChangeMarketingRequest**](ItvChangeMarketingRequest.md)| Updated marketing preferences &amp; ITV profile token. | |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="checkPreviousEntitlements"></a>
# **checkPreviousEntitlements**
> ItvHadEntitlement checkPreviousEntitlements(lang)



Check whether the user has been previously entitled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvHadEntitlement result = apiInstance.checkPreviousEntitlements(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#checkPreviousEntitlements");
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
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvHadEntitlement**](ItvHadEntitlement.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="checkVoucher"></a>
# **checkVoucher**
> ItvVoucher checkVoucher(platform, itvVoucherRequest, lang)



Validates the coupon/voucher for specified payment platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    ItvVoucherRequest itvVoucherRequest = new ItvVoucherRequest(); // ItvVoucherRequest | Coupon/voucher.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvVoucher result = apiInstance.checkVoucher(platform, itvVoucherRequest, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#checkVoucher");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **itvVoucherRequest** | [**ItvVoucherRequest**](ItvVoucherRequest.md)| Coupon/voucher. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvVoucher**](ItvVoucher.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of requested coupon/voucher. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="confirmPurchase"></a>
# **confirmPurchase**
> ItvPurchase confirmPurchase(platform, itvPurchaseRequest, lang)



Confirms purchase and returns the details of purchased subscription for specified payment platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    ItvPurchaseRequest itvPurchaseRequest = new ItvPurchaseRequest(); // ItvPurchaseRequest | Details of a purchase request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvPurchase result = apiInstance.confirmPurchase(platform, itvPurchaseRequest, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#confirmPurchase");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **itvPurchaseRequest** | [**ItvPurchaseRequest**](ItvPurchaseRequest.md)| Details of a purchase request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvPurchase**](ItvPurchase.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of purchased subscription. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="confirmPurchaseStrong"></a>
# **confirmPurchaseStrong**
> ItvPurchaseStrongResponse confirmPurchaseStrong(platform, itvPurchaseStrongRequest, lang)



Confirms purchase and returns the details of purchased subscription for specified payment platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    ItvPurchaseStrongRequest itvPurchaseStrongRequest = new ItvPurchaseStrongRequest(); // ItvPurchaseStrongRequest | Details of a purchase request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvPurchaseStrongResponse result = apiInstance.confirmPurchaseStrong(platform, itvPurchaseStrongRequest, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#confirmPurchaseStrong");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **itvPurchaseStrongRequest** | [**ItvPurchaseStrongRequest**](ItvPurchaseStrongRequest.md)| Details of a purchase request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvPurchaseStrongResponse**](ItvPurchaseStrongResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of purchased subscription. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="confirmPurchaseWithOffer"></a>
# **confirmPurchaseWithOffer**
> ItvPurchaseWithOfferResponse confirmPurchaseWithOffer(platform, itvPurchaseWithOfferRequest, lang)



Confirms purchase and returns the details of purchased subscription for specified payment platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    ItvPurchaseWithOfferRequest itvPurchaseWithOfferRequest = new ItvPurchaseWithOfferRequest(); // ItvPurchaseWithOfferRequest | Details of a purchase request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvPurchaseWithOfferResponse result = apiInstance.confirmPurchaseWithOffer(platform, itvPurchaseWithOfferRequest, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#confirmPurchaseWithOffer");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **itvPurchaseWithOfferRequest** | [**ItvPurchaseWithOfferRequest**](ItvPurchaseWithOfferRequest.md)| Details of a purchase request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvPurchaseWithOfferResponse**](ItvPurchaseWithOfferResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of purchased subscription. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="deleteAccount"></a>
# **deleteAccount**
> deleteAccount(itvDeleteAccountRequest, ff, lang)



Delete account in compliance with GDPR.  The expected token scope is Settings. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    ItvDeleteAccountRequest itvDeleteAccountRequest = new ItvDeleteAccountRequest(); // ItvDeleteAccountRequest | New email address & ITV profile token.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.deleteAccount(itvDeleteAccountRequest, ff, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#deleteAccount");
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
| **itvDeleteAccountRequest** | [**ItvDeleteAccountRequest**](ItvDeleteAccountRequest.md)| New email address &amp; ITV profile token. | |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="executeTransaction"></a>
# **executeTransaction**
> executeTransaction(transactionid, itvRokuTransactionRequest, lang)



Sends request to execute specified transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String transactionid = "transactionid_example"; // String | The identifier of the Roku transaction (subscribe/upgrade/downgrade/cancellation).
    ItvRokuTransactionRequest itvRokuTransactionRequest = new ItvRokuTransactionRequest(); // ItvRokuTransactionRequest | Details of a transaction request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.executeTransaction(transactionid, itvRokuTransactionRequest, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#executeTransaction");
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
| **transactionid** | **String**| The identifier of the Roku transaction (subscribe/upgrade/downgrade/cancellation). | |
| **itvRokuTransactionRequest** | [**ItvRokuTransactionRequest**](ItvRokuTransactionRequest.md)| Details of a transaction request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getAccountTokenWithPin"></a>
# **getAccountTokenWithPin**
> List&lt;AccessToken&gt; getAccountTokenWithPin(itvPinAuthRequest, ff, lang)



Provides authorization with parental control pin.  Returns an array containing account token with Playback scope.  Requires access token with Catalog scope.  Pin must be a 4-digit string 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    ItvPinAuthRequest itvPinAuthRequest = new ItvPinAuthRequest(); // ItvPinAuthRequest | Details of token request.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      List<AccessToken> result = apiInstance.getAccountTokenWithPin(itvPinAuthRequest, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getAccountTokenWithPin");
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
| **itvPinAuthRequest** | [**ItvPinAuthRequest**](ItvPinAuthRequest.md)| Details of token request. | |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**List&lt;AccessToken&gt;**](AccessToken.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getBillingHistory"></a>
# **getBillingHistory**
> ItvBillingHistory getBillingHistory(platform, itvBillingHistoryRequest, lang)



Returns the list of billing records for specified payment platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    ItvBillingHistoryRequest itvBillingHistoryRequest = new ItvBillingHistoryRequest(); // ItvBillingHistoryRequest | Details of a billing history request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvBillingHistory result = apiInstance.getBillingHistory(platform, itvBillingHistoryRequest, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getBillingHistory");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **itvBillingHistoryRequest** | [**ItvBillingHistoryRequest**](ItvBillingHistoryRequest.md)| Details of a billing history request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvBillingHistory**](ItvBillingHistory.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of billing records. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getCardDetails"></a>
# **getCardDetails**
> ItvCardDetails getCardDetails(platform, itvGetCardDetailsRequest, lang)



Get payment card details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    ItvGetCardDetailsRequest itvGetCardDetailsRequest = new ItvGetCardDetailsRequest(); // ItvGetCardDetailsRequest | ITV profile token in body.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvCardDetails result = apiInstance.getCardDetails(platform, itvGetCardDetailsRequest, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getCardDetails");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **itvGetCardDetailsRequest** | [**ItvGetCardDetailsRequest**](ItvGetCardDetailsRequest.md)| ITV profile token in body. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvCardDetails**](ItvCardDetails.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getCurrentEntitlement"></a>
# **getCurrentEntitlement**
> ItvEntitlementCurrent getCurrentEntitlement(lang)



Returns current entitlement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvEntitlementCurrent result = apiInstance.getCurrentEntitlement(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getCurrentEntitlement");
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
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvEntitlementCurrent**](ItvEntitlementCurrent.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current entitlement. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getCurrentSubscription"></a>
# **getCurrentSubscription**
> ItvCurrentSubscription getCurrentSubscription(platform, lang)



Returns the details of current subscription for specified payment platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvCurrentSubscription result = apiInstance.getCurrentSubscription(platform, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getCurrentSubscription");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvCurrentSubscription**](ItvCurrentSubscription.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of current subscription. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getEntitlementsHistory"></a>
# **getEntitlementsHistory**
> ItvEntitlementsHistory getEntitlementsHistory(lang)



Returns the state of subscription for any payment platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvEntitlementsHistory result = apiInstance.getEntitlementsHistory(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getEntitlementsHistory");
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
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvEntitlementsHistory**](ItvEntitlementsHistory.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of current subscription. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getFeatureFlag"></a>
# **getFeatureFlag**
> ItvFeatureFlag getFeatureFlag(feature, lang)



Gets info whether or not a feature is enabled or disabled using a feature flag. Feature flags are set as a custom field within PM. It also supports custom feature flag data if needed. Such data can be return as well.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String feature = "feature_example"; // String | The identifier of the feature to check for feature flag.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvFeatureFlag result = apiInstance.getFeatureFlag(feature, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getFeatureFlag");
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
| **feature** | **String**| The identifier of the feature to check for feature flag. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvFeatureFlag**](ItvFeatureFlag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request succeeded. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getFullPriceRenewal"></a>
# **getFullPriceRenewal**
> ItvSubscriptionFullPriceRenewal getFullPriceRenewal(lang)



Returns full price renewal state and reason for specific user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvSubscriptionFullPriceRenewal result = apiInstance.getFullPriceRenewal(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getFullPriceRenewal");
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
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvSubscriptionFullPriceRenewal**](ItvSubscriptionFullPriceRenewal.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | full price renewal state and reason for specific user. |  -  |

<a id="getItvProfileToken"></a>
# **getItvProfileToken**
> ItvProfileToken getItvProfileToken(itvProfileTokenRequest, lang)



Returns the ITV profile token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    ItvProfileTokenRequest itvProfileTokenRequest = new ItvProfileTokenRequest(); // ItvProfileTokenRequest | Details of token request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvProfileToken result = apiInstance.getItvProfileToken(itvProfileTokenRequest, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getItvProfileToken");
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
| **itvProfileTokenRequest** | [**ItvProfileTokenRequest**](ItvProfileTokenRequest.md)| Details of token request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvProfileToken**](ItvProfileToken.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ITV profile token. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getPublicPreview"></a>
# **getPublicPreview**
> SamsungPreview getPublicPreview()



Returns public preview for Samsung based on the page &#39;/samsung-preview&#39; configured in PresentationManager. There is a hard limit of max 40 items to be returned. It splits evenly items count into the page rows, remaining items are added into the first row. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ItvApi apiInstance = new ItvApi(defaultClient);
    try {
      SamsungPreview result = apiInstance.getPublicPreview();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getPublicPreview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The samsung public preview requested. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getRecommendedList"></a>
# **getRecommendedList**
> ItemList getRecommendedList(itemTypes, page, pageSize, device, sub, segments, ff, lang)



Get the list of recommended items under the active profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: profileAuth
    OAuth profileAuth = (OAuth) defaultClient.getAuthentication("profileAuth");
    profileAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    List<String> itemTypes = Arrays.asList(); // List<String> | List of item types to filter the recommendation list
    Integer page = 1; // Integer | The page of items to load. Starts from page 1.
    Integer pageSize = 12; // Integer | The number of items to return in a page.
    String device = "web_browser"; // String | The type of device the content is targeting.
    String sub = "sub_example"; // String | The active subscription code.
    List<String> segments = Arrays.asList(); // List<String> | The list of segments to filter the response by.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItemList result = apiInstance.getRecommendedList(itemTypes, page, pageSize, device, sub, segments, ff, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getRecommendedList");
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
| **itemTypes** | [**List&lt;String&gt;**](String.md)| List of item types to filter the recommendation list | [optional] |
| **page** | **Integer**| The page of items to load. Starts from page 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return in a page. | [optional] [default to 12] |
| **device** | **String**| The type of device the content is targeting. | [optional] [default to web_browser] |
| **sub** | **String**| The active subscription code. | [optional] |
| **segments** | [**List&lt;String&gt;**](String.md)| The list of segments to filter the response by. | [optional] |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItemList**](ItemList.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of items requested. |  -  |
| **400** | Bad request. |  -  |
| **401** | Invalid access token. |  -  |
| **403** | Forbidden. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getSaveOffer"></a>
# **getSaveOffer**
> ItvGetDiscountResponse getSaveOffer(lang)



Checks the provided coupon id for a user. Only Stripe platform is currently supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvGetDiscountResponse result = apiInstance.getSaveOffer(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getSaveOffer");
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
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvGetDiscountResponse**](ItvGetDiscountResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Avalable save offer plan, if any. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getSubscriptionState"></a>
# **getSubscriptionState**
> ItvSubscriptionState getSubscriptionState(lang)



Returns the state of subscription for any payment platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvSubscriptionState result = apiInstance.getSubscriptionState(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getSubscriptionState");
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
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvSubscriptionState**](ItvSubscriptionState.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of current subscription. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getSubscriptionStatus"></a>
# **getSubscriptionStatus**
> ItvSubscriptionStatusResponse getSubscriptionStatus(platform, lang)



Returns status of latest payment intent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvSubscriptionStatusResponse result = apiInstance.getSubscriptionStatus(platform, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getSubscriptionStatus");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvSubscriptionStatusResponse**](ItvSubscriptionStatusResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status of the latest payment intent |  -  |

<a id="getUpcomingInvoice"></a>
# **getUpcomingInvoice**
> ItvGetDiscountResponse getUpcomingInvoice(lang)



Returns an upcoming invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvGetDiscountResponse result = apiInstance.getUpcomingInvoice(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getUpcomingInvoice");
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
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvGetDiscountResponse**](ItvGetDiscountResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Avalable save offer plan, if any. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getVoucherById"></a>
# **getVoucherById**
> ItvVoucher getVoucherById(voucherId, planId, lang)



Checks the provided coupon id for a user. Only Stripe platform is currently supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String voucherId = "voucherId_example"; // String | The identifier of the voucher.
    String planId = "planId_example"; // String | The identifier of the plan.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvVoucher result = apiInstance.getVoucherById(voucherId, planId, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#getVoucherById");
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
| **voucherId** | **String**| The identifier of the voucher. | |
| **planId** | **String**| The identifier of the plan. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvVoucher**](ItvVoucher.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Avalable voucher, if any. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="googlePaySubscription"></a>
# **googlePaySubscription**
> googlePaySubscription(itvGooglePaySubscriptionRequest, lang)



Get the list of recommended items under the active profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: profileAuth
    OAuth profileAuth = (OAuth) defaultClient.getAuthentication("profileAuth");
    profileAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    ItvGooglePaySubscriptionRequest itvGooglePaySubscriptionRequest = new ItvGooglePaySubscriptionRequest(); // ItvGooglePaySubscriptionRequest | Details of googlePay subscription request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.googlePaySubscription(itvGooglePaySubscriptionRequest, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#googlePaySubscription");
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
| **itvGooglePaySubscriptionRequest** | [**ItvGooglePaySubscriptionRequest**](ItvGooglePaySubscriptionRequest.md)| Details of googlePay subscription request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | missing purchase token/subscription item in body, or subscription item undefined |  -  |
| **401** | Invalid or missing grant |  -  |
| **409** | Purchase token is already attached to a different user |  -  |
| **415** | wrong content-type |  -  |
| **500** | something bad has happened |  -  |

<a id="itvItemsummaryExternalIdGet"></a>
# **itvItemsummaryExternalIdGet**
> ServiceError itvItemsummaryExternalIdGet(externalId)



Redirects to corresponding Axis Item details page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String externalId = "externalId_example"; // String | The external identifier of the item.
    try {
      ServiceError result = apiInstance.itvItemsummaryExternalIdGet(externalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#itvItemsummaryExternalIdGet");
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
| **externalId** | **String**| The external identifier of the item. | |

### Return type

[**ServiceError**](ServiceError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Item found. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="itvPlansPlatformGet"></a>
# **itvPlansPlatformGet**
> ItvPlans itvPlansPlatformGet(platform, lang)



Returns the plans available for specified payment platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvPlans result = apiInstance.itvPlansPlatformGet(platform, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#itvPlansPlatformGet");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvPlans**](ItvPlans.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of available plans. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="itvProfileGet"></a>
# **itvProfileGet**
> Object itvProfileGet(lang)



Returns the ITV profile object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      Object result = apiInstance.itvProfileGet(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#itvProfileGet");
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
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

**Object**

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ITV profile object. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="itvPurchasePlatformDelete"></a>
# **itvPurchasePlatformDelete**
> itvPurchasePlatformDelete(platform, itvCancelSubscriptionRequest, lang)



Cancel a plan subscription.  A cancelled subscription will continue to be valid until the subscription expiry date or next renewal date. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes).
    ItvCancelSubscriptionRequest itvCancelSubscriptionRequest = new ItvCancelSubscriptionRequest(); // ItvCancelSubscriptionRequest | Details of a cancellation request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.itvPurchasePlatformDelete(platform, itvCancelSubscriptionRequest, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#itvPurchasePlatformDelete");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). | |
| **itvCancelSubscriptionRequest** | [**ItvCancelSubscriptionRequest**](ItvCancelSubscriptionRequest.md)| Details of a cancellation request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="itvRokuPlansGet"></a>
# **itvRokuPlansGet**
> RokuPlans itvRokuPlansGet(lang)



Gets available Roku plans.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      RokuPlans result = apiInstance.itvRokuPlansGet(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#itvRokuPlansGet");
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
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**RokuPlans**](RokuPlans.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of available Roku plans. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="resubscribe"></a>
# **resubscribe**
> Object resubscribe(planId, platform, lang)



Resubscription for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String planId = "planId_example"; // String | The id of the plan to renew.
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes). Only stripe is currently supported.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      Object result = apiInstance.resubscribe(planId, platform, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#resubscribe");
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
| **planId** | **String**| The id of the plan to renew. | |
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). Only stripe is currently supported. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

**Object**

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The response body is the updated plan information. |  -  |
| **401** | Invalid Rocket token. |  -  |
| **404** | Customer not found or no active subscription. |  -  |
| **406** | Invalid ITV token. |  -  |
| **409** | Customer not already set for cancellation. |  -  |
| **500** | Third party API internal server error. |  -  |

<a id="updatePaymentIntentStrong"></a>
# **updatePaymentIntentStrong**
> ItvUpdateIntentStrongResponse updatePaymentIntentStrong(platform, itvUpdateIntentStrongRequest, lang)



Change payment method details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe only is currently supported).
    ItvUpdateIntentStrongRequest itvUpdateIntentStrongRequest = new ItvUpdateIntentStrongRequest(); // ItvUpdateIntentStrongRequest | Details of change card details request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      ItvUpdateIntentStrongResponse result = apiInstance.updatePaymentIntentStrong(platform, itvUpdateIntentStrongRequest, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#updatePaymentIntentStrong");
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
| **platform** | **String**| The identifier of the payment platform (stripe only is currently supported). | |
| **itvUpdateIntentStrongRequest** | [**ItvUpdateIntentStrongRequest**](ItvUpdateIntentStrongRequest.md)| Details of change card details request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

[**ItvUpdateIntentStrongResponse**](ItvUpdateIntentStrongResponse.md)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="updatePaymentMethodStrong"></a>
# **updatePaymentMethodStrong**
> updatePaymentMethodStrong(platform, itvUpdatePaymentStrongRequest, lang)



Change payment method details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe only is currently supported).
    ItvUpdatePaymentStrongRequest itvUpdatePaymentStrongRequest = new ItvUpdatePaymentStrongRequest(); // ItvUpdatePaymentStrongRequest | Details of change card details request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.updatePaymentMethodStrong(platform, itvUpdatePaymentStrongRequest, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#updatePaymentMethodStrong");
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
| **platform** | **String**| The identifier of the payment platform (stripe only is currently supported). | |
| **itvUpdatePaymentStrongRequest** | [**ItvUpdatePaymentStrongRequest**](ItvUpdatePaymentStrongRequest.md)| Details of change card details request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="updateProfile"></a>
# **updateProfile**
> updateProfile(itvUpdateProfileRequest, ff, lang)



Update ITV profile.  The expected token scope is Settings. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    ItvUpdateProfileRequest itvUpdateProfileRequest = new ItvUpdateProfileRequest(); // ItvUpdateProfileRequest | ITV profile object with updated values & ITV profile token.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.updateProfile(itvUpdateProfileRequest, ff, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#updateProfile");
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
| **itvUpdateProfileRequest** | [**ItvUpdateProfileRequest**](ItvUpdateProfileRequest.md)| ITV profile object with updated values &amp; ITV profile token. | |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="upgradePlan"></a>
# **upgradePlan**
> upgradePlan(platform, itvUpgradePlanRequest, lang)



Upgrades the plan for the current user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ItvApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: accountAuth
    OAuth accountAuth = (OAuth) defaultClient.getAuthentication("accountAuth");
    accountAuth.setAccessToken("YOUR ACCESS TOKEN");

    ItvApi apiInstance = new ItvApi(defaultClient);
    String platform = "platform_example"; // String | The identifier of the payment platform (stripe/itunes). Only Stripe is supported
    ItvUpgradePlanRequest itvUpgradePlanRequest = new ItvUpgradePlanRequest(); // ItvUpgradePlanRequest | Details of an upgrade request.
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.upgradePlan(platform, itvUpgradePlanRequest, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling ItvApi#upgradePlan");
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
| **platform** | **String**| The identifier of the payment platform (stripe/itunes). Only Stripe is supported | |
| **itvUpgradePlanRequest** | [**ItvUpgradePlanRequest**](ItvUpgradePlanRequest.md)| Details of an upgrade request. | |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[accountAuth](../README.md#accountAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Upgrade succeeded. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

