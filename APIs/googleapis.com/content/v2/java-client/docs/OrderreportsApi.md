# OrderreportsApi

All URIs are relative to *https://shoppingcontent.googleapis.com/content/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentOrderreportsListdisbursements**](OrderreportsApi.md#contentOrderreportsListdisbursements) | **GET** /{merchantId}/orderreports/disbursements |  |
| [**contentOrderreportsListtransactions**](OrderreportsApi.md#contentOrderreportsListtransactions) | **GET** /{merchantId}/orderreports/disbursements/{disbursementId}/transactions |  |


<a id="contentOrderreportsListdisbursements"></a>
# **contentOrderreportsListdisbursements**
> OrderreportsListDisbursementsResponse contentOrderreportsListdisbursements(merchantId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, disbursementEndDate, disbursementStartDate, maxResults, pageToken)



Retrieves a report for disbursements from your Merchant Center account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderreportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://shoppingcontent.googleapis.com/content/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrderreportsApi apiInstance = new OrderreportsApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The ID of the account that manages the order. This cannot be a multi-client account.
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
    String disbursementEndDate = "disbursementEndDate_example"; // String | The last date which disbursements occurred. In ISO 8601 format. Default: current date.
    String disbursementStartDate = "disbursementStartDate_example"; // String | The first date which disbursements occurred. In ISO 8601 format.
    Integer maxResults = 56; // Integer | The maximum number of disbursements to return in the response, used for paging.
    String pageToken = "pageToken_example"; // String | The token returned by the previous request.
    try {
      OrderreportsListDisbursementsResponse result = apiInstance.contentOrderreportsListdisbursements(merchantId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, disbursementEndDate, disbursementStartDate, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderreportsApi#contentOrderreportsListdisbursements");
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
| **merchantId** | **String**| The ID of the account that manages the order. This cannot be a multi-client account. | |
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
| **disbursementEndDate** | **String**| The last date which disbursements occurred. In ISO 8601 format. Default: current date. | [optional] |
| **disbursementStartDate** | **String**| The first date which disbursements occurred. In ISO 8601 format. | [optional] |
| **maxResults** | **Integer**| The maximum number of disbursements to return in the response, used for paging. | [optional] |
| **pageToken** | **String**| The token returned by the previous request. | [optional] |

### Return type

[**OrderreportsListDisbursementsResponse**](OrderreportsListDisbursementsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="contentOrderreportsListtransactions"></a>
# **contentOrderreportsListtransactions**
> OrderreportsListTransactionsResponse contentOrderreportsListtransactions(merchantId, disbursementId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken, transactionEndDate, transactionStartDate)



Retrieves a list of transactions for a disbursement from your Merchant Center account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderreportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://shoppingcontent.googleapis.com/content/v2");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrderreportsApi apiInstance = new OrderreportsApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The ID of the account that manages the order. This cannot be a multi-client account.
    String disbursementId = "disbursementId_example"; // String | The Google-provided ID of the disbursement (found in Wallet).
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
    Integer maxResults = 56; // Integer | The maximum number of disbursements to return in the response, used for paging.
    String pageToken = "pageToken_example"; // String | The token returned by the previous request.
    String transactionEndDate = "transactionEndDate_example"; // String | The last date in which transaction occurred. In ISO 8601 format. Default: current date.
    String transactionStartDate = "transactionStartDate_example"; // String | The first date in which transaction occurred. In ISO 8601 format.
    try {
      OrderreportsListTransactionsResponse result = apiInstance.contentOrderreportsListtransactions(merchantId, disbursementId, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken, transactionEndDate, transactionStartDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderreportsApi#contentOrderreportsListtransactions");
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
| **merchantId** | **String**| The ID of the account that manages the order. This cannot be a multi-client account. | |
| **disbursementId** | **String**| The Google-provided ID of the disbursement (found in Wallet). | |
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
| **maxResults** | **Integer**| The maximum number of disbursements to return in the response, used for paging. | [optional] |
| **pageToken** | **String**| The token returned by the previous request. | [optional] |
| **transactionEndDate** | **String**| The last date in which transaction occurred. In ISO 8601 format. Default: current date. | [optional] |
| **transactionStartDate** | **String**| The first date in which transaction occurred. In ISO 8601 format. | [optional] |

### Return type

[**OrderreportsListTransactionsResponse**](OrderreportsListTransactionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

