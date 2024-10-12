# AccountsApi

All URIs are relative to *https://travelpartner.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**travelpartnerAccountsAccountLinksCreate**](AccountsApi.md#travelpartnerAccountsAccountLinksCreate) | **POST** /v3/{parent}/accountLinks |  |
| [**travelpartnerAccountsAccountLinksDelete**](AccountsApi.md#travelpartnerAccountsAccountLinksDelete) | **DELETE** /v3/{name} |  |
| [**travelpartnerAccountsAccountLinksList**](AccountsApi.md#travelpartnerAccountsAccountLinksList) | **GET** /v3/{parent}/accountLinks |  |
| [**travelpartnerAccountsBrandsCreate**](AccountsApi.md#travelpartnerAccountsBrandsCreate) | **POST** /v3/{parent}/brands |  |
| [**travelpartnerAccountsBrandsList**](AccountsApi.md#travelpartnerAccountsBrandsList) | **GET** /v3/{parent}/brands |  |
| [**travelpartnerAccountsBrandsPatch**](AccountsApi.md#travelpartnerAccountsBrandsPatch) | **PATCH** /v3/{name} |  |
| [**travelpartnerAccountsFreeBookingLinksReportViewsQuery**](AccountsApi.md#travelpartnerAccountsFreeBookingLinksReportViewsQuery) | **GET** /v3/{name}/freeBookingLinksReportViews:query |  |
| [**travelpartnerAccountsHotelViewsList**](AccountsApi.md#travelpartnerAccountsHotelViewsList) | **GET** /v3/{parent}/hotelViews |  |
| [**travelpartnerAccountsHotelViewsSummarize**](AccountsApi.md#travelpartnerAccountsHotelViewsSummarize) | **GET** /v3/{parent}/hotelViews:summarize |  |
| [**travelpartnerAccountsHotelsSetLiveOnGoogle**](AccountsApi.md#travelpartnerAccountsHotelsSetLiveOnGoogle) | **POST** /v3/{account}/hotels:setLiveOnGoogle |  |
| [**travelpartnerAccountsIconsCreate**](AccountsApi.md#travelpartnerAccountsIconsCreate) | **POST** /v3/{parent}/icons |  |
| [**travelpartnerAccountsIconsList**](AccountsApi.md#travelpartnerAccountsIconsList) | **GET** /v3/{parent}/icons |  |
| [**travelpartnerAccountsListingsVerify**](AccountsApi.md#travelpartnerAccountsListingsVerify) | **POST** /v3/{parent}/listings:verify |  |
| [**travelpartnerAccountsParticipationReportViewsQuery**](AccountsApi.md#travelpartnerAccountsParticipationReportViewsQuery) | **GET** /v3/{name}/participationReportViews:query |  |
| [**travelpartnerAccountsPriceAccuracyViewsList**](AccountsApi.md#travelpartnerAccountsPriceAccuracyViewsList) | **GET** /v3/{parent}/priceAccuracyViews |  |
| [**travelpartnerAccountsPriceAccuracyViewsSummarize**](AccountsApi.md#travelpartnerAccountsPriceAccuracyViewsSummarize) | **GET** /v3/{parent}/priceAccuracyViews:summarize |  |
| [**travelpartnerAccountsPriceCoverageViewsGetLatest**](AccountsApi.md#travelpartnerAccountsPriceCoverageViewsGetLatest) | **GET** /v3/{parent}/priceCoverageViews:latest |  |
| [**travelpartnerAccountsPriceCoverageViewsList**](AccountsApi.md#travelpartnerAccountsPriceCoverageViewsList) | **GET** /v3/{parent}/priceCoverageViews |  |
| [**travelpartnerAccountsPropertyPerformanceReportViewsQuery**](AccountsApi.md#travelpartnerAccountsPropertyPerformanceReportViewsQuery) | **GET** /v3/{name}/propertyPerformanceReportViews:query |  |
| [**travelpartnerAccountsReconciliationReportsCreate**](AccountsApi.md#travelpartnerAccountsReconciliationReportsCreate) | **POST** /v3/{parent}/reconciliationReports |  |
| [**travelpartnerAccountsReconciliationReportsGet**](AccountsApi.md#travelpartnerAccountsReconciliationReportsGet) | **GET** /v3/{name} |  |
| [**travelpartnerAccountsReconciliationReportsList**](AccountsApi.md#travelpartnerAccountsReconciliationReportsList) | **GET** /v3/{parent}/reconciliationReports |  |
| [**travelpartnerAccountsReconciliationReportsValidate**](AccountsApi.md#travelpartnerAccountsReconciliationReportsValidate) | **POST** /v3/{parent}/reconciliationReports:validate |  |


<a id="travelpartnerAccountsAccountLinksCreate"></a>
# **travelpartnerAccountsAccountLinksCreate**
> AccountLink travelpartnerAccountsAccountLinksCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, accountLink)



Creates a new account link between a Hotel Center account and a Google Ads account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the Hotel Center account being queried. The format is `accounts/{account_id}`.
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
    AccountLink accountLink = new AccountLink(); // AccountLink | 
    try {
      AccountLink result = apiInstance.travelpartnerAccountsAccountLinksCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, accountLink);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsAccountLinksCreate");
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
| **parent** | **String**| The resource name of the Hotel Center account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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
| **accountLink** | [**AccountLink**](AccountLink.md)|  | [optional] |

### Return type

[**AccountLink**](AccountLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsAccountLinksDelete"></a>
# **travelpartnerAccountsAccountLinksDelete**
> Object travelpartnerAccountsAccountLinksDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Deletes an account link.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String name = "name_example"; // String | Required. The resource name of the account link being deleted. The format is `accounts/{account_id}/accountLinks/{account_link_id}`.
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
      Object result = apiInstance.travelpartnerAccountsAccountLinksDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsAccountLinksDelete");
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
| **name** | **String**| Required. The resource name of the account link being deleted. The format is &#x60;accounts/{account_id}/accountLinks/{account_link_id}&#x60;. | |
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsAccountLinksList"></a>
# **travelpartnerAccountsAccountLinksList**
> ListAccountLinksResponse travelpartnerAccountsAccountLinksList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Returns the account links for a Hotel Center account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
      ListAccountLinksResponse result = apiInstance.travelpartnerAccountsAccountLinksList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsAccountLinksList");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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

[**ListAccountLinksResponse**](ListAccountLinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsBrandsCreate"></a>
# **travelpartnerAccountsBrandsCreate**
> Brand travelpartnerAccountsBrandsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, brandId, brand)



Creates a new brand. Because Google detects brands from your existing properties, you only need this operation when you want to configure a brand before you send its properties to Google. Note that it might take a couple of days after your listing feed first provides a brand for the brand to appear.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the Hotel Center account being queried. The format is `accounts/{account_id}`.
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
    String brandId = "brandId_example"; // String | Required. The partner-determined brand identifier.
    Brand brand = new Brand(); // Brand | 
    try {
      Brand result = apiInstance.travelpartnerAccountsBrandsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, brandId, brand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsBrandsCreate");
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
| **parent** | **String**| Required. The resource name of the Hotel Center account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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
| **brandId** | **String**| Required. The partner-determined brand identifier. | [optional] |
| **brand** | [**Brand**](Brand.md)|  | [optional] |

### Return type

[**Brand**](Brand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsBrandsList"></a>
# **travelpartnerAccountsBrandsList**
> ListBrandsResponse travelpartnerAccountsBrandsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Returns the brands for a partner account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the account being queried. The format is `accounts/{account_id}`.
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
      ListBrandsResponse result = apiInstance.travelpartnerAccountsBrandsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsBrandsList");
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
| **parent** | **String**| Required. The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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

[**ListBrandsResponse**](ListBrandsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsBrandsPatch"></a>
# **travelpartnerAccountsBrandsPatch**
> Brand travelpartnerAccountsBrandsPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, updateMask, brand)



Updates a brand.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String name = "name_example"; // String | Output only. The resource name for the brand in the format `accounts/{account_id}/brands/{brand_id}`. The `brand_id` corresponds to the partner's brand identifier used for landing page matching and the property-level brand identifier. A default brand is applied to properties that do not have a brand. The `brand_id` of the default brand is `NO_BRAND_ID`. It can be fetched and updated like any configured brand.
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
    Boolean allowMissing = true; // Boolean | When true, and the Brand is not found, a new Brand will be created. In this situation, `update_mask` is ignored.
    String updateMask = "updateMask_example"; // String | Required. The field to update. Only the `display_names` and `icon` fields can be updated. Use the syntax shown in the example URI below and provide the new value in the request body. Example request URI and request body: ``` PATCH https://travelpartner.googleapis.com/v3/accounts/123456789/ brands/my-brand?update_mask=brand.display_names ``` ``` { \"display_names\": [{ \"language\": \"en\" \"text\": \"Gilles' Gites\" }] } ``` The information above is sufficient for forming the URI and request body. The sentence below is auto-generated, supplemental information about the `FieldMask` format in general.
    Brand brand = new Brand(); // Brand | 
    try {
      Brand result = apiInstance.travelpartnerAccountsBrandsPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, updateMask, brand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsBrandsPatch");
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
| **name** | **String**| Output only. The resource name for the brand in the format &#x60;accounts/{account_id}/brands/{brand_id}&#x60;. The &#x60;brand_id&#x60; corresponds to the partner&#39;s brand identifier used for landing page matching and the property-level brand identifier. A default brand is applied to properties that do not have a brand. The &#x60;brand_id&#x60; of the default brand is &#x60;NO_BRAND_ID&#x60;. It can be fetched and updated like any configured brand. | |
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
| **allowMissing** | **Boolean**| When true, and the Brand is not found, a new Brand will be created. In this situation, &#x60;update_mask&#x60; is ignored. | [optional] |
| **updateMask** | **String**| Required. The field to update. Only the &#x60;display_names&#x60; and &#x60;icon&#x60; fields can be updated. Use the syntax shown in the example URI below and provide the new value in the request body. Example request URI and request body: &#x60;&#x60;&#x60; PATCH https://travelpartner.googleapis.com/v3/accounts/123456789/ brands/my-brand?update_mask&#x3D;brand.display_names &#x60;&#x60;&#x60; &#x60;&#x60;&#x60; { \&quot;display_names\&quot;: [{ \&quot;language\&quot;: \&quot;en\&quot; \&quot;text\&quot;: \&quot;Gilles&#39; Gites\&quot; }] } &#x60;&#x60;&#x60; The information above is sufficient for forming the URI and request body. The sentence below is auto-generated, supplemental information about the &#x60;FieldMask&#x60; format in general. | [optional] |
| **brand** | [**Brand**](Brand.md)|  | [optional] |

### Return type

[**Brand**](Brand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsFreeBookingLinksReportViewsQuery"></a>
# **travelpartnerAccountsFreeBookingLinksReportViewsQuery**
> QueryFreeBookingLinksReportResponse travelpartnerAccountsFreeBookingLinksReportViewsQuery(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, aggregateBy, filter, pageSize, pageToken)



**DEPRECATED:** Use PropertyPerformanceReportService.QueryPropertyPerformanceReport, which also has impression reporting, instead. Provides the ability to query (get, filter, and segment) a free booking links report for a specific account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String name = "name_example"; // String | The resource name of the account being queried. Format: accounts/{account_id}
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
    String aggregateBy = "aggregateBy_example"; // String | Specifies how to segment the metrics returned by the query. For example, if `userRegionCode` is specified, the `freeBookingLinksResult` will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: `date`, `userRegionCode`, `deviceType`, `partnerHotelId`, and `partnerHotelDisplayName`. Only fields specified here are included in the FreeBookingLinksResult.
    String filter = "filter_example"; // String | The conditions (fields and expressions) used to filter the free booking link metrics for the account being queried. The syntax requires spaces surrounding the `in` operator. Otherwise, spaces can be omitted. Conditions can be joined using the `and` operator. The `date` field is required. All other fields are optional. The `date` field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for `partnerHotelDisplayName` are matched case-insensitively. Examples of valid conditions are as follows: * `date = '2021-12-03'` * `date between '2021-12-03' and '2021-12-08'` * `deviceType = 'TABLET'` * `deviceType in ('MOBILE', 'TABLET')` * `partnerHotelId = 'AAA'` * `partnerHotelId in ('AAA', 'BBB')` * `partnerHotelDisplayName = 'hotel A'` * `partnerHotelDisplayName in ('Hotel A', 'HOTEL b')` * `userRegionCode = 'US'` * `userRegionCode in ('US', 'CA')`
    Integer pageSize = 56; // Integer | The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token.
    try {
      QueryFreeBookingLinksReportResponse result = apiInstance.travelpartnerAccountsFreeBookingLinksReportViewsQuery(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, aggregateBy, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsFreeBookingLinksReportViewsQuery");
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
| **name** | **String**| The resource name of the account being queried. Format: accounts/{account_id} | |
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
| **aggregateBy** | **String**| Specifies how to segment the metrics returned by the query. For example, if &#x60;userRegionCode&#x60; is specified, the &#x60;freeBookingLinksResult&#x60; will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: &#x60;date&#x60;, &#x60;userRegionCode&#x60;, &#x60;deviceType&#x60;, &#x60;partnerHotelId&#x60;, and &#x60;partnerHotelDisplayName&#x60;. Only fields specified here are included in the FreeBookingLinksResult. | [optional] |
| **filter** | **String**| The conditions (fields and expressions) used to filter the free booking link metrics for the account being queried. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions can be joined using the &#x60;and&#x60; operator. The &#x60;date&#x60; field is required. All other fields are optional. The &#x60;date&#x60; field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for &#x60;partnerHotelDisplayName&#x60; are matched case-insensitively. Examples of valid conditions are as follows: * &#x60;date &#x3D; &#39;2021-12-03&#39;&#x60; * &#x60;date between &#39;2021-12-03&#39; and &#39;2021-12-08&#39;&#x60; * &#x60;deviceType &#x3D; &#39;TABLET&#39;&#x60; * &#x60;deviceType in (&#39;MOBILE&#39;, &#39;TABLET&#39;)&#x60; * &#x60;partnerHotelId &#x3D; &#39;AAA&#39;&#x60; * &#x60;partnerHotelId in (&#39;AAA&#39;, &#39;BBB&#39;)&#x60; * &#x60;partnerHotelDisplayName &#x3D; &#39;hotel A&#39;&#x60; * &#x60;partnerHotelDisplayName in (&#39;Hotel A&#39;, &#39;HOTEL b&#39;)&#x60; * &#x60;userRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;userRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; | [optional] |
| **pageSize** | **Integer**| The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000. | [optional] |
| **pageToken** | **String**| A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token. | [optional] |

### Return type

[**QueryFreeBookingLinksReportResponse**](QueryFreeBookingLinksReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsHotelViewsList"></a>
# **travelpartnerAccountsHotelViewsList**
> ListHotelViewsResponse travelpartnerAccountsHotelViewsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Returns the list of hotel views.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
    String filter = "filter_example"; // String | Optional. The conditions (fields and expressions) used to filter HotelViews. The syntax requires spaces surrounding the `in` operator. Otherwise, spaces can be omitted. Conditions cannot be joined. The `hotelId` field can be used to select specific hotels. The `liveOnGoogle` field can select properties that Google shows, or properties that are omitted in google search results. The `matchStatus` field can be used to filter the list of HotelViews returned for the account. Examples of valid conditions and their syntax are as follows: * `hotelId = 'hotel_ABC'` * `hotelId in ('hotel_ABC', 'hotel_XYZ')` * `liveOnGoogle = 'TRUE'` * `liveOnGoogle = 'FALSE'` * `matchStatus = 'NOT_MATCHED'` * `matchStatus in ('NOT_MATCHED', 'MATCHED', 'MAP_OVERLAP')`
    Integer pageSize = 56; // Integer | Number of elements to retrieve in a single page.
    String pageToken = "pageToken_example"; // String | Token of the page to retrieve.
    try {
      ListHotelViewsResponse result = apiInstance.travelpartnerAccountsHotelViewsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsHotelViewsList");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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
| **filter** | **String**| Optional. The conditions (fields and expressions) used to filter HotelViews. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions cannot be joined. The &#x60;hotelId&#x60; field can be used to select specific hotels. The &#x60;liveOnGoogle&#x60; field can select properties that Google shows, or properties that are omitted in google search results. The &#x60;matchStatus&#x60; field can be used to filter the list of HotelViews returned for the account. Examples of valid conditions and their syntax are as follows: * &#x60;hotelId &#x3D; &#39;hotel_ABC&#39;&#x60; * &#x60;hotelId in (&#39;hotel_ABC&#39;, &#39;hotel_XYZ&#39;)&#x60; * &#x60;liveOnGoogle &#x3D; &#39;TRUE&#39;&#x60; * &#x60;liveOnGoogle &#x3D; &#39;FALSE&#39;&#x60; * &#x60;matchStatus &#x3D; &#39;NOT_MATCHED&#39;&#x60; * &#x60;matchStatus in (&#39;NOT_MATCHED&#39;, &#39;MATCHED&#39;, &#39;MAP_OVERLAP&#39;)&#x60; | [optional] |
| **pageSize** | **Integer**| Number of elements to retrieve in a single page. | [optional] |
| **pageToken** | **String**| Token of the page to retrieve. | [optional] |

### Return type

[**ListHotelViewsResponse**](ListHotelViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsHotelViewsSummarize"></a>
# **travelpartnerAccountsHotelViewsSummarize**
> SummarizeHotelViewsResponse travelpartnerAccountsHotelViewsSummarize(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Returns summarized information about hotels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
      SummarizeHotelViewsResponse result = apiInstance.travelpartnerAccountsHotelViewsSummarize(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsHotelViewsSummarize");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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

[**SummarizeHotelViewsResponse**](SummarizeHotelViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsHotelsSetLiveOnGoogle"></a>
# **travelpartnerAccountsHotelsSetLiveOnGoogle**
> SetLiveOnGoogleResponse travelpartnerAccountsHotelsSetLiveOnGoogle(account, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, setLiveOnGoogleRequest)



Collection-level custom method to update the Live on Google status for multiple properties. Each call can turn on or off multiple hotels. To turn some hotels on and turn some hotels off, you will have to make multiple calls.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String account = "account_example"; // String | Required. The resource name of the account. The format is accounts/{account_id}.
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
    SetLiveOnGoogleRequest setLiveOnGoogleRequest = new SetLiveOnGoogleRequest(); // SetLiveOnGoogleRequest | 
    try {
      SetLiveOnGoogleResponse result = apiInstance.travelpartnerAccountsHotelsSetLiveOnGoogle(account, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, setLiveOnGoogleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsHotelsSetLiveOnGoogle");
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
| **account** | **String**| Required. The resource name of the account. The format is accounts/{account_id}. | |
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
| **setLiveOnGoogleRequest** | [**SetLiveOnGoogleRequest**](SetLiveOnGoogleRequest.md)|  | [optional] |

### Return type

[**SetLiveOnGoogleResponse**](SetLiveOnGoogleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsIconsCreate"></a>
# **travelpartnerAccountsIconsCreate**
> Icon travelpartnerAccountsIconsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, icon)



Uploads a new icon and starts its review process. Generates an &#x60;icon_id&#x60; and includes it in the icon&#39;s resource name, which is the format &#x60;accounts/{account_id}/icons/{icon_id}&#x60; Returns HTTP status 400 and doesn&#39;t trigger the review process if the icon has any of these conditions: * Image is not in PNG format, or not convertible to PNG format. * Size less than 72 pixels * Size greater than 1200 pixels * Aspect ratio other than 1:1

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the partner account owning the icon. The format is `accounts/{account_id}`.
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
    Icon icon = new Icon(); // Icon | 
    try {
      Icon result = apiInstance.travelpartnerAccountsIconsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, icon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsIconsCreate");
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
| **parent** | **String**| Required. The resource name of the partner account owning the icon. The format is &#x60;accounts/{account_id}&#x60;. | |
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
| **icon** | [**Icon**](Icon.md)|  | [optional] |

### Return type

[**Icon**](Icon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsIconsList"></a>
# **travelpartnerAccountsIconsList**
> ListIconsResponse travelpartnerAccountsIconsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Returns the &#x60;Icon&#x60;s for a partner account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the queried partner account. The format is `accounts/{account_id}`.
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
      ListIconsResponse result = apiInstance.travelpartnerAccountsIconsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsIconsList");
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
| **parent** | **String**| Required. The resource name of the queried partner account. The format is &#x60;accounts/{account_id}&#x60;. | |
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

[**ListIconsResponse**](ListIconsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsListingsVerify"></a>
# **travelpartnerAccountsListingsVerify**
> VerifyListingsResponse travelpartnerAccountsListingsVerify(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, verifyListingsRequest)



returns verified listings with data issues and serving eligibilities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
    VerifyListingsRequest verifyListingsRequest = new VerifyListingsRequest(); // VerifyListingsRequest | 
    try {
      VerifyListingsResponse result = apiInstance.travelpartnerAccountsListingsVerify(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, verifyListingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsListingsVerify");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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
| **verifyListingsRequest** | [**VerifyListingsRequest**](VerifyListingsRequest.md)|  | [optional] |

### Return type

[**VerifyListingsResponse**](VerifyListingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsParticipationReportViewsQuery"></a>
# **travelpartnerAccountsParticipationReportViewsQuery**
> QueryParticipationReportResponse travelpartnerAccountsParticipationReportViewsQuery(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, aggregateBy, filter, pageSize, pageToken)



Provides the ability to query (get, filter, and segment) a participation report for a particular account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String name = "name_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
    String aggregateBy = "aggregateBy_example"; // String | Specifies how to segment the metrics returned by the query. For example, if `userRegionCode` is specified as the `aggregate_by` value, the `participationResult` will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: `date`, `userRegionCode`, `deviceType`, `partnerHotelId`, `hotelRegionCode`, `advanceBookingWindow`, `lengthOfStayDays`, `checkinDate`, and `occupancy`. Fields that are not specified are not included in the ParticipationResult. Using an `aggregateBy` specification that produces a large number of rows will cause an error. This is especially true when aggregating by `partnerHotelId` or more than two fields. To reduce the possibiliy of an error, filter by `partnerHotelId` and `date` to only include a select number of hotels and dates. Accounts with a large number of hotels will need to further reduce data with more filtering.
    String filter = "filter_example"; // String | The conditions (fields and expressions) used to filter the participation metrics for the account being queried. The syntax requires spaces surrounding the `in` operator. Otherwise, spaces can be omitted. Conditions can be joined using the `and` operator. The `date` field is required. All other fields are optional. Examples of valid conditions are as follows: * `advanceBookingWindow = 2` * `advanceBookingWindow >= 0` * `advanceBookingWindow <= 5` * `advanceBookingWindow between 1 and 5` * `checkinDate = '2020-10-01'` * `checkinDate >= '2020-10-01'` * `checkinDate <= '2020-10-01'` * `checkinDate between '2020-10-01' and '2020-10-05'` * `date = '2020-02-04'` * `date between '2020-02-04' and '2020-02-09'` * `deviceType = 'TABLET'` * `deviceType in ('MOBILE', 'TABLET')` * `hotelRegionCode = 'US'` * `hotelRegionCode in ('US', 'CA')` * `lengthOfStayDays = 2` * `lengthOfStayDays >= 0` * `lengthOfStayDays <= 5` * `lengthOfStayDays between 1 and 5` * `occupancy = 2` * `occupancy >= 0` * `occupancy <= 5` * `occupancy between 1 and 5` * `partnerHotelId = 'AAA'` * `partnerHotelId in ('AAA', 'BBB')` * `userRegionCode = 'US'` * `userRegionCode in ('US', 'CA')`
    Integer pageSize = 56; // Integer | The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token.
    try {
      QueryParticipationReportResponse result = apiInstance.travelpartnerAccountsParticipationReportViewsQuery(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, aggregateBy, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsParticipationReportViewsQuery");
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
| **name** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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
| **aggregateBy** | **String**| Specifies how to segment the metrics returned by the query. For example, if &#x60;userRegionCode&#x60; is specified as the &#x60;aggregate_by&#x60; value, the &#x60;participationResult&#x60; will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: &#x60;date&#x60;, &#x60;userRegionCode&#x60;, &#x60;deviceType&#x60;, &#x60;partnerHotelId&#x60;, &#x60;hotelRegionCode&#x60;, &#x60;advanceBookingWindow&#x60;, &#x60;lengthOfStayDays&#x60;, &#x60;checkinDate&#x60;, and &#x60;occupancy&#x60;. Fields that are not specified are not included in the ParticipationResult. Using an &#x60;aggregateBy&#x60; specification that produces a large number of rows will cause an error. This is especially true when aggregating by &#x60;partnerHotelId&#x60; or more than two fields. To reduce the possibiliy of an error, filter by &#x60;partnerHotelId&#x60; and &#x60;date&#x60; to only include a select number of hotels and dates. Accounts with a large number of hotels will need to further reduce data with more filtering. | [optional] |
| **filter** | **String**| The conditions (fields and expressions) used to filter the participation metrics for the account being queried. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions can be joined using the &#x60;and&#x60; operator. The &#x60;date&#x60; field is required. All other fields are optional. Examples of valid conditions are as follows: * &#x60;advanceBookingWindow &#x3D; 2&#x60; * &#x60;advanceBookingWindow &gt;&#x3D; 0&#x60; * &#x60;advanceBookingWindow &lt;&#x3D; 5&#x60; * &#x60;advanceBookingWindow between 1 and 5&#x60; * &#x60;checkinDate &#x3D; &#39;2020-10-01&#39;&#x60; * &#x60;checkinDate &gt;&#x3D; &#39;2020-10-01&#39;&#x60; * &#x60;checkinDate &lt;&#x3D; &#39;2020-10-01&#39;&#x60; * &#x60;checkinDate between &#39;2020-10-01&#39; and &#39;2020-10-05&#39;&#x60; * &#x60;date &#x3D; &#39;2020-02-04&#39;&#x60; * &#x60;date between &#39;2020-02-04&#39; and &#39;2020-02-09&#39;&#x60; * &#x60;deviceType &#x3D; &#39;TABLET&#39;&#x60; * &#x60;deviceType in (&#39;MOBILE&#39;, &#39;TABLET&#39;)&#x60; * &#x60;hotelRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;hotelRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; * &#x60;lengthOfStayDays &#x3D; 2&#x60; * &#x60;lengthOfStayDays &gt;&#x3D; 0&#x60; * &#x60;lengthOfStayDays &lt;&#x3D; 5&#x60; * &#x60;lengthOfStayDays between 1 and 5&#x60; * &#x60;occupancy &#x3D; 2&#x60; * &#x60;occupancy &gt;&#x3D; 0&#x60; * &#x60;occupancy &lt;&#x3D; 5&#x60; * &#x60;occupancy between 1 and 5&#x60; * &#x60;partnerHotelId &#x3D; &#39;AAA&#39;&#x60; * &#x60;partnerHotelId in (&#39;AAA&#39;, &#39;BBB&#39;)&#x60; * &#x60;userRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;userRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; | [optional] |
| **pageSize** | **Integer**| The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000. | [optional] |
| **pageToken** | **String**| A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token. | [optional] |

### Return type

[**QueryParticipationReportResponse**](QueryParticipationReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsPriceAccuracyViewsList"></a>
# **travelpartnerAccountsPriceAccuracyViewsList**
> ListPriceAccuracyViewsResponse travelpartnerAccountsPriceAccuracyViewsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Lists the available price accuracy views.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
      ListPriceAccuracyViewsResponse result = apiInstance.travelpartnerAccountsPriceAccuracyViewsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsPriceAccuracyViewsList");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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

[**ListPriceAccuracyViewsResponse**](ListPriceAccuracyViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsPriceAccuracyViewsSummarize"></a>
# **travelpartnerAccountsPriceAccuracyViewsSummarize**
> SummarizePriceAccuracyResponse travelpartnerAccountsPriceAccuracyViewsSummarize(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Returns the price accuracy summary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account that is being queried. The format is `accounts/{account_id}`.
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
      SummarizePriceAccuracyResponse result = apiInstance.travelpartnerAccountsPriceAccuracyViewsSummarize(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsPriceAccuracyViewsSummarize");
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
| **parent** | **String**| The resource name of the account that is being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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

[**SummarizePriceAccuracyResponse**](SummarizePriceAccuracyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsPriceCoverageViewsGetLatest"></a>
# **travelpartnerAccountsPriceCoverageViewsGetLatest**
> PriceCoverageView travelpartnerAccountsPriceCoverageViewsGetLatest(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Returns the latest price coverage view in full detail.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
      PriceCoverageView result = apiInstance.travelpartnerAccountsPriceCoverageViewsGetLatest(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsPriceCoverageViewsGetLatest");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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

[**PriceCoverageView**](PriceCoverageView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsPriceCoverageViewsList"></a>
# **travelpartnerAccountsPriceCoverageViewsList**
> ListPriceCoverageViewsResponse travelpartnerAccountsPriceCoverageViewsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Returns the entire price coverage history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
      ListPriceCoverageViewsResponse result = apiInstance.travelpartnerAccountsPriceCoverageViewsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsPriceCoverageViewsList");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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

[**ListPriceCoverageViewsResponse**](ListPriceCoverageViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsPropertyPerformanceReportViewsQuery"></a>
# **travelpartnerAccountsPropertyPerformanceReportViewsQuery**
> QueryPropertyPerformanceReportResponse travelpartnerAccountsPropertyPerformanceReportViewsQuery(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, aggregateBy, filter, pageSize, pageToken)



Provides the ability to query (get, filter, and segment) a property performance links report for a specific account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String name = "name_example"; // String | The resource name of the account being queried. Format: accounts/{account_id}
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
    String aggregateBy = "aggregateBy_example"; // String | Specifies how to segment the metrics returned by the query. For example, if `userRegionCode` is specified, the `PropertyPerformanceResult` will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: `advanceBookingWindow`, `brand`, `date`, `deviceType`, `highIntentUsers`, `lengthOfStay`, `propertyRegionCode`, `occupancy`, `partnerPropertyId`, `partnerPropertyDisplayName`, and `userRegionCode`. Only fields specified here are included in the PropertyPerformanceResult.
    String filter = "filter_example"; // String | The conditions (fields and expressions) used to filter the property performance metrics for the account being queried. The syntax requires spaces surrounding the `in` operator. Otherwise, spaces can be omitted. Conditions can be joined using the `and` operator. The `date` field is required. All other fields are optional. The `date` field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for `partnerPropertyDisplayName` and `brand` are matched case-insensitively. Examples of valid conditions are as follows: * `advanceBookingWindow = 'ADVANCE_BOOKING_WINDOW_SAME_DAY'` * `advanceBookingWindow in ('ADVANCE_BOOKING_WINDOW_SAME_DAY', 'ADVANCE_BOOKING_WINDOW_DAYS_61_TO_90')` * `brand = 'Brand A'` * `brand in ('Brand A', 'brand B')` * `date = '2021-12-03'` * `date between '2021-12-03' and '2021-12-08'` * `deviceType = 'TABLET'` * `deviceType in ('MOBILE', 'TABLET')` * `highIntentUsers = 'TRUE'` * `highIntentUsers = 'FALSE'` * `lengthOfStay = 'LENGTH_OF_STAY_NIGHTS_2'` * `lengthOfStay in ('LENGTH_OF_STAY_NIGHTS_2', 'LENGTH_OF_STAY_NIGHTS_4_TO_7')` * `propertyRegionCode = 'US'` * `propertyRegionCode in ('US', 'CA')` * `occupancy = 'OCCUPANCY_2'` * `occupancy in ('OCCUPANCY_2', 'OCCUPANCY_OVER_4')` * `partnerPropertyId = 'AAA'` * `partnerPropertyId in ('AAA', 'BBB')` * `partnerPropertyDisplayName = 'hotel A'` * `partnerPropertyDisplayName in ('Hotel A', 'HOTEL b')` * `userRegionCode = 'US'` * `userRegionCode in ('US', 'CA')`
    Integer pageSize = 56; // Integer | The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token.
    try {
      QueryPropertyPerformanceReportResponse result = apiInstance.travelpartnerAccountsPropertyPerformanceReportViewsQuery(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, aggregateBy, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsPropertyPerformanceReportViewsQuery");
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
| **name** | **String**| The resource name of the account being queried. Format: accounts/{account_id} | |
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
| **aggregateBy** | **String**| Specifies how to segment the metrics returned by the query. For example, if &#x60;userRegionCode&#x60; is specified, the &#x60;PropertyPerformanceResult&#x60; will provide metrics aggregated by user region. The string value is a comma-separated list of fields. Valid fields are: &#x60;advanceBookingWindow&#x60;, &#x60;brand&#x60;, &#x60;date&#x60;, &#x60;deviceType&#x60;, &#x60;highIntentUsers&#x60;, &#x60;lengthOfStay&#x60;, &#x60;propertyRegionCode&#x60;, &#x60;occupancy&#x60;, &#x60;partnerPropertyId&#x60;, &#x60;partnerPropertyDisplayName&#x60;, and &#x60;userRegionCode&#x60;. Only fields specified here are included in the PropertyPerformanceResult. | [optional] |
| **filter** | **String**| The conditions (fields and expressions) used to filter the property performance metrics for the account being queried. The syntax requires spaces surrounding the &#x60;in&#x60; operator. Otherwise, spaces can be omitted. Conditions can be joined using the &#x60;and&#x60; operator. The &#x60;date&#x60; field is required. All other fields are optional. The &#x60;date&#x60; field values are inclusive and must be in YYYY-MM-DD format. The earliest acceptable date is 2021-03-09; earlier date values will be coerced to 2021-03-09. Values for &#x60;partnerPropertyDisplayName&#x60; and &#x60;brand&#x60; are matched case-insensitively. Examples of valid conditions are as follows: * &#x60;advanceBookingWindow &#x3D; &#39;ADVANCE_BOOKING_WINDOW_SAME_DAY&#39;&#x60; * &#x60;advanceBookingWindow in (&#39;ADVANCE_BOOKING_WINDOW_SAME_DAY&#39;, &#39;ADVANCE_BOOKING_WINDOW_DAYS_61_TO_90&#39;)&#x60; * &#x60;brand &#x3D; &#39;Brand A&#39;&#x60; * &#x60;brand in (&#39;Brand A&#39;, &#39;brand B&#39;)&#x60; * &#x60;date &#x3D; &#39;2021-12-03&#39;&#x60; * &#x60;date between &#39;2021-12-03&#39; and &#39;2021-12-08&#39;&#x60; * &#x60;deviceType &#x3D; &#39;TABLET&#39;&#x60; * &#x60;deviceType in (&#39;MOBILE&#39;, &#39;TABLET&#39;)&#x60; * &#x60;highIntentUsers &#x3D; &#39;TRUE&#39;&#x60; * &#x60;highIntentUsers &#x3D; &#39;FALSE&#39;&#x60; * &#x60;lengthOfStay &#x3D; &#39;LENGTH_OF_STAY_NIGHTS_2&#39;&#x60; * &#x60;lengthOfStay in (&#39;LENGTH_OF_STAY_NIGHTS_2&#39;, &#39;LENGTH_OF_STAY_NIGHTS_4_TO_7&#39;)&#x60; * &#x60;propertyRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;propertyRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; * &#x60;occupancy &#x3D; &#39;OCCUPANCY_2&#39;&#x60; * &#x60;occupancy in (&#39;OCCUPANCY_2&#39;, &#39;OCCUPANCY_OVER_4&#39;)&#x60; * &#x60;partnerPropertyId &#x3D; &#39;AAA&#39;&#x60; * &#x60;partnerPropertyId in (&#39;AAA&#39;, &#39;BBB&#39;)&#x60; * &#x60;partnerPropertyDisplayName &#x3D; &#39;hotel A&#39;&#x60; * &#x60;partnerPropertyDisplayName in (&#39;Hotel A&#39;, &#39;HOTEL b&#39;)&#x60; * &#x60;userRegionCode &#x3D; &#39;US&#39;&#x60; * &#x60;userRegionCode in (&#39;US&#39;, &#39;CA&#39;)&#x60; | [optional] |
| **pageSize** | **Integer**| The maximum number of participation results to return. The service may return fewer than this value. If unspecified, at most 10,000 results will be returned. The maximum value is 10,000; values above 10,000 will be coerced to 10,000. | [optional] |
| **pageToken** | **String**| A page token, received from a previous QueryParticipationReport request. Provide this to receive the subsequent page. When paginating, all other parameters provided to QueryParticipationReport must match the call that provided the page token. | [optional] |

### Return type

[**QueryPropertyPerformanceReportResponse**](QueryPropertyPerformanceReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsReconciliationReportsCreate"></a>
# **travelpartnerAccountsReconciliationReportsCreate**
> CreateReconciliationReportResponse travelpartnerAccountsReconciliationReportsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, reconciliationReport)



Creates a reconciliation report and uploads it to Google.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
    ReconciliationReport reconciliationReport = new ReconciliationReport(); // ReconciliationReport | 
    try {
      CreateReconciliationReportResponse result = apiInstance.travelpartnerAccountsReconciliationReportsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, reconciliationReport);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsReconciliationReportsCreate");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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
| **reconciliationReport** | [**ReconciliationReport**](ReconciliationReport.md)|  | [optional] |

### Return type

[**CreateReconciliationReportResponse**](CreateReconciliationReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsReconciliationReportsGet"></a>
# **travelpartnerAccountsReconciliationReportsGet**
> ReconciliationReport travelpartnerAccountsReconciliationReportsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeMatchedPrices, includeNonScoring, includePixels)



Returns a reconciliation report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String name = "name_example"; // String | The resource name of the reconciliation report to fetch. The format is `accounts/{account_id}/reconciliationReports/{datetime}~{filename}`.
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
    Boolean includeMatchedPrices = true; // Boolean | Set to true if matched prices are to be added into the report.
    Boolean includeNonScoring = true; // Boolean | Set to true if non-account impacting rows are to be added into the report.
    Boolean includePixels = true; // Boolean | Set to true if pixel signals are to be added into the report.
    try {
      ReconciliationReport result = apiInstance.travelpartnerAccountsReconciliationReportsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, includeMatchedPrices, includeNonScoring, includePixels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsReconciliationReportsGet");
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
| **name** | **String**| The resource name of the reconciliation report to fetch. The format is &#x60;accounts/{account_id}/reconciliationReports/{datetime}~{filename}&#x60;. | |
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
| **includeMatchedPrices** | **Boolean**| Set to true if matched prices are to be added into the report. | [optional] |
| **includeNonScoring** | **Boolean**| Set to true if non-account impacting rows are to be added into the report. | [optional] |
| **includePixels** | **Boolean**| Set to true if pixel signals are to be added into the report. | [optional] |

### Return type

[**ReconciliationReport**](ReconciliationReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsReconciliationReportsList"></a>
# **travelpartnerAccountsReconciliationReportsList**
> ListReconciliationReportsResponse travelpartnerAccountsReconciliationReportsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, endDate, startDate)



Returns a list of the names of created reconciliation reports.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
    String endDate = "endDate_example"; // String | End of date range to fetch files for. Format is yyyy-mm-dd[THH[:MM[:SS]]]. If empty, reports until the end of time are fetched.
    String startDate = "startDate_example"; // String | Beginning of date range to fetch files for. Format is yyyy-MM-dd[THH[:mm[:SS]]]. If empty, reports from the beginning of time onwards are fetched.
    try {
      ListReconciliationReportsResponse result = apiInstance.travelpartnerAccountsReconciliationReportsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, endDate, startDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsReconciliationReportsList");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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
| **endDate** | **String**| End of date range to fetch files for. Format is yyyy-mm-dd[THH[:MM[:SS]]]. If empty, reports until the end of time are fetched. | [optional] |
| **startDate** | **String**| Beginning of date range to fetch files for. Format is yyyy-MM-dd[THH[:mm[:SS]]]. If empty, reports from the beginning of time onwards are fetched. | [optional] |

### Return type

[**ListReconciliationReportsResponse**](ListReconciliationReportsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="travelpartnerAccountsReconciliationReportsValidate"></a>
# **travelpartnerAccountsReconciliationReportsValidate**
> ValidateReconciliationReportResponse travelpartnerAccountsReconciliationReportsValidate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, reconciliationReport)



Validates a reconciliation report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://travelpartner.googleapis.com");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String parent = "parent_example"; // String | The resource name of the account being queried. The format is `accounts/{account_id}`.
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
    ReconciliationReport reconciliationReport = new ReconciliationReport(); // ReconciliationReport | 
    try {
      ValidateReconciliationReportResponse result = apiInstance.travelpartnerAccountsReconciliationReportsValidate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, reconciliationReport);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#travelpartnerAccountsReconciliationReportsValidate");
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
| **parent** | **String**| The resource name of the account being queried. The format is &#x60;accounts/{account_id}&#x60;. | |
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
| **reconciliationReport** | [**ReconciliationReport**](ReconciliationReport.md)|  | [optional] |

### Return type

[**ValidateReconciliationReportResponse**](ValidateReconciliationReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

